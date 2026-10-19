#!/usr/bin/env python3
"""Exact coefficientwise balance check over all positive run partitions up to 18 letters."""
from functools import lru_cache

@lru_cache(None)
def profile(parts):
    arr=(1,)
    for L in parts:
        b=[0]*(len(arr)+L)
        for i,a in enumerate(arr):
            for j in range(L+1):b[i+j]+=a
        arr=tuple(b)
    return arr

def comps(total, r):
    if r==1:
        yield (total,)
    else:
        for first in range(1,total-r+2):
            for rest in comps(total-first,r-1):yield (first,)+rest

def main():
    count=0
    for m in range(1,19):
        for r in range(1,m+1):
            t,s=divmod(m,r)
            target=profile((t,)*(r-s)+(t+1,)*s)
            for x in comps(m,r):
                actual=profile(x)
                assert len(actual)==len(target)
                assert all(a<=b for a,b in zip(actual,target)), (m,r,x)
                count+=1
    print('MAJORIZATION_OK', 'compositions=', count, 'total_a<=18')

if __name__=='__main__':main()
