#!/usr/bin/env python3
"""Direct definition-based checks for the exact LCSS phase theorem."""
from itertools import product

def is_subsequence(source, target):
    i = 0
    for symbol in source:
        if i < len(target) and target[i] == symbol:
            i += 1
    return i == len(target)

def brute(q, m, n):
    x = tuple(range(q)) * m
    y = tuple(reversed(range(q))) * n
    for length in range(len(y), 0, -1):
        good = set()
        for start in range(len(y) - length + 1):
            word = y[start:start + length]
            if is_subsequence(x, word):
                good.add(word)
        if good:
            return length, len(good), good
    raise AssertionError('one-letter solutions always exist')

def prediction(q, m, n):
    length = min(q*n, m+n-1, m+(m+q-2)//(q-1))
    lo = max(0, q*(length-m) - length + 1)
    hi = min(q-1, q*n-length)
    phases = range(lo, hi+1) if lo <= hi else range(0)
    y = tuple(reversed(range(q))) * n
    good = {y[r:r+length] for r in phases}
    return length, len(good), good

def check():
    cases=0
    for q,m,n in product(range(2,9),range(1,10),range(1,10)):
        b=brute(q,m,n)
        p=prediction(q,m,n)
        assert b==p, (q,m,n,b,p)
        cases+=1
    print(f'PASS: length, number and exact identity of all optimal distinct factors in {cases} parameter cells (q=2..8, m=1..9, n=1..9).')
    # Independent greedy-descent equivalence, checked for every factor, not only winners.
    cells=0
    for q,m,n in product(range(2,8), range(1,8), range(1,8)):
        x=tuple(range(q))*m; y=tuple(reversed(range(q)))*n
        for length in range(1,len(y)+1):
            for s in range(len(y)-length+1):
                wraps=(s+length-1)//q-s//q
                assert is_subsequence(x,y[s:s+length]) == (length-1-wraps<=m-1), (q,m,n,length,s)
                cells+=1
    print(f'PASS: greedy criterion in {cells} individual substring cells (q=2..7, m,n=1..7).')

if __name__=='__main__':check()
