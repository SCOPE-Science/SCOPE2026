#!/usr/bin/env python3
"""Independent direct enumeration of binary length-three support fibers."""
from collections import defaultdict

def profile(word, n):
    mask=0
    for shift in range(n-2):
        triple=(word >> shift)&7
        mask |= 1<<triple
    return mask

def count_profiles(n):
    c=[0]*256
    for w in range(1<<n):
        c[profile(w,n)] += 1
    return c

if __name__=='__main__':
    for n in range(3,19):
        c=count_profiles(n)
        best=max(c)
        winning=[mask for mask, count in enumerate(c) if count==best]
        print(n, best, c[255],len(winning),','.join(f'{x:02x}' for x in winning),max(c[:255]))
