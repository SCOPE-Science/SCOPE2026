#!/usr/bin/env python3
"""Exact-integer cross-check for an arithmetic binomial-divisibility theorem."""
from math import comb

def prediction(b):
    if b % 3 == 0:
        return 0
    if b % 3 == 2:
        return 1
    a = b + 2
    pow3 = 1
    while a % 3 == 0:
        pow3 *= 3
        a //= 3
    return (pow3 + 1)//2

def direct(b,n):
    return comb((b+3)*n,3*n) % (b*n+1) == 0

def main():
    tests=0
    for b in range(1,151):
        f=prediction(b)
        bound=min(80,f+1) if f else 80
        for n in range(1,bound+1):
            value=direct(b,n)
            expected = f == 0 or n < f if f else True
            if f and n>f: # no prediction about subsequent failures
                continue
            if value != expected:
                raise AssertionError((b,n,f,value))
            tests+=1
    for s in range(1,7):
        b=3**s-2
        f=(3**s+1)//2
        assert not direct(b,f),(s,b,f)
        tests+=1
    print('VERIFY_OK b_range=1..150 exact_divisibility_tests=%d higher_depth_witnesses=6' % tests)
if __name__=='__main__': main()
