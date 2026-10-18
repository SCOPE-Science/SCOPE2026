#!/usr/bin/env python3
"""Exact checks for the Cayley-tree leaf/rare-hub covariance theorem."""
from fractions import Fraction
from math import comb, factorial
from itertools import product
from functools import lru_cache

def limited(n,m,k):
    """Number of maps from m labeled balls to n bins with loads < k."""
    @lru_cache(None)
    def f(b,s):
        if b==0:
            return int(s==0)
        return sum(comb(s,j)*f(b-1,s-j) for j in range(min(k-1,s)+1))
    return f(n,m)

def by_formula(n,k):
    m=n-2
    q=Fraction(limited(n,m,k),n**m)
    both=Fraction(n*limited(n-1,m,k),n**m)
    EL=Fraction(n*(n-1)**m,n**m)
    return EL*q-both, q

def by_enumeration(n,k):
    m=n-2; s0=sL=sA=sLA=0
    for word in product(range(n),repeat=m):
        hist=[0]*n
        for i in word: hist[i]+=1
        L=sum(t==0 for t in hist)
        A=int(max(hist)>=k)
        s0+=1; sL+=L; sA+=A; sLA+=L*A
    return Fraction(sLA,s0)-Fraction(sL*sA,s0*s0), Fraction(s0-sA,s0)

def test():
    checks=0
    for n in range(3,8):
        for k in range(1,n):
            a,q=by_formula(n,k)
            b,p=by_enumeration(n,k)
            assert (a,q)==(b,p),(n,k,a,b,q,p)
            checks+=2
    for n,k in [(12,3),(30,4),(60,4),(120,4),(326,5)]:
        a,p=by_formula(n,k)
        assert a>=0,(n,k,a)
        checks+=1
        print('MOMENT',n,k,'cov=',float(a),'scale=',float(a/k),'no_hub=',float(p))
    print('VERIFY_OK',checks)
if __name__=='__main__': test()
