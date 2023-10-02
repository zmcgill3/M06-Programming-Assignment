# 13.1 Write the current date as a string to the text file today.txt

from datetime import date, datetime
import time

dateToday = date.today()
fout = open("today.txt", 'wt')
print(dateToday, file=fout)
fout.close()

# 13.2 Read the text file today.txt into the string today_string

fin = open("today.txt", 'rt')
today_string = fin.read()
fin.close()

# 13.3 Parse the date from today_string

fmt = "%Y-%m-%d "
time.strptime(today_string, fmt)

# 15.1 Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between zero and one, print the current time, and then exit

import random
import multiprocessing

def wait():
    waitTime = random.random()
    time.sleep(waitTime)
    now = datetime.now()
    fmt = "It is %H:%M:%S in military time"
    print(now.strftime(fmt))

if __name__ == "__main__":    
    for n in range(3):
        p = multiprocessing.Process(target=wait)
        p.start()