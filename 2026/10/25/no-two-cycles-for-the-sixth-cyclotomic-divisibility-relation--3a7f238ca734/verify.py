#!/usr/bin/env python3
"""Exact arithmetic corroboration of the sixth-cyclotomic two-cycle lemma."""
from math import gcd
from functools import reduce
from operator import mul

def F(x): return x*x-x+1

def main():
    bound=1000
    checks=0
    for x in range(2,bound+1):
        fx=F(x)
        for y in range(x+1, min(bound,fx)+1):
            if fx % y == 0:
                checks += 1
                assert F(y) % x != 0, (x,y)
    for x in range(2,bound+1):
        assert F(x) % x == 1
    P=(7,13,43,157)
    N=reduce(mul,P,1)
    assert N == 614341
    # The first argument in each pair divides F(second argument).
    edges=((7,157),(157,13),(13,43),(43,7))
    assert all(F(q) % p == 0 for p,q in edges)
    A=reduce(mul, (F(p) for p in P),1)
    assert A % N == 0 and A//N == 486361
    assert sum(N//gcd(N,j) for j in range(1,N+1)) == A
    assert sum(1 for j in range(1,N+1) if gcd(N,j)==1)>0
    print('CERTIFICATE_OK bound=%d tested_divisibility_candidates=%d four_cycle=1 exact_average=486361' % (bound,checks))

if __name__ == '__main__': main()
