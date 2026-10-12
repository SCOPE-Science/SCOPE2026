#!/usr/bin/env python3
"""Exact finite checks for the first binary product-covering compression threshold."""
from itertools import combinations

WITNESS6 = (0,3,4,7,9,12,14,15,17,18,20,23,25,26,29,32,33,37,38,42,43,45,50,53,55,56,59,60,62)

def covering_direct(C,n):
    C=set(C)
    for x in range(1<<n):
        for y in range(1<<n):
            success=False
            for i in range(n):
                # The two centers may be different, but both have to match
                # the respective targets outside the same coordinate i.
                if (x in C or (x^(1<<i)) in C) and (y in C or (y^(1<<i)) in C):
                    success=True
                    break
            if not success:
                return False,(x,y)
    return True,None

def binary_small_exhaustion(n):
    words=list(range(1<<n))
    upper=1<<(n-1)
    success,err=covering_direct([x for x in words if x&1==0],n)
    assert success,err
    if n==1:
        return
    for size in range(0,upper):
        for C in combinations(words,size):
            good,_=covering_direct(C,n)
            assert not good,(n,size,C)

if __name__=='__main__':
    assert len(WITNESS6)==29 and len(set(WITNESS6))==29
    for n in range(1,5):
        binary_small_exhaustion(n)
    success,err=covering_direct(WITNESS6,6)
    assert success,err
    print('VERIFY_OK n=1,2,3,4 exhaustive; n=6 explicit 29-word witness; n=5 requires finite_check.cpp')
