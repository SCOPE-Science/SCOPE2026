#!/usr/bin/env python3
"""Standalone checks for the exact two-marker shuffle-root spectrum.

Checks a dynamic-programming self-shuffle recognizer independently of the
interval criterion, then checks all tail and exact-multiplicity identities
by exhaustive gap enumeration over a wider finite range.
"""
from functools import lru_cache
from collections import Counter
from math import comb


def count_roots_interval(n,a,b,c):
    assert n >= 1 and min(a,b,c) >= 0 and a+b+c == 2*n-2
    lo=max((a+1)//2,n-1-c)
    hi=min(a,(a+b)//2)
    return max(0,hi-lo+1)


def is_shuffle_of(w,x):
    n=len(x)
    assert len(w)==2*n
    @lru_cache(None)
    def can(i,j):
        if i+j==2*n:
            return i==j==n
        p=i+j
        return (i<n and w[p]==x[i] and can(i+1,j)) or (j<n and w[p]==x[j] and can(i,j+1))
    return can(0,0)


def count_roots_independently(n,a,b,c):
    w='0'*a+'1'+'0'*b+'1'+'0'*c
    return sum(is_shuffle_of(w,'0'*u+'1'+'0'*(n-u-1)) for u in range(n))


def T(m):
    return 1+3*m*(m-1)//2 if m>=1 else 0


def test():
    dp_cases=0
    for n in range(1,13):
        for a in range(2*n-1):
            for b in range(2*n-1-a):
                c=2*n-2-a-b
                expected=count_roots_interval(n,a,b,c)
                found=count_roots_independently(n,a,b,c)
                assert expected==found,(n,a,b,c,expected,found)
                dp_cases += 1
    print('Independent DP / interval comparisons:',dp_cases)

    cases=0
    for n in range(1,101):
        counts=Counter()
        for a in range(2*n-1):
            for b in range(2*n-1-a):
                c=2*n-2-a-b
                r=count_roots_interval(n,a,b,c)
                counts[r]+=1
                cases += 1
                assert r<=min(a,b,c)//2+1
                if min(a,b,c)>=2:
                    m=n-3
                    assert m>=1
                    assert count_roots_interval(m,a-2,b-2,c-2)==max(0,r-1)
        assert sum(counts.values())==comb(2*n,2)
        maxroot=(n+2)//3
        assert max(counts)==maxroot
        for r in range(1,maxroot+2):
            tail=sum(val for roots,val in counts.items() if roots>=r)
            assert tail==T(n-3*(r-1)),(n,r,tail,T(n-3*(r-1)))
            exact=counts[r]
            assert exact==T(n-3*(r-1))-T(n-3*r)
        assert sum(r*count for r,count in counts.items())==comb(n+2,3)
    print('Finite enumeration and contraction checks:',cases)
    print('Maximum, tail, exact-multiplicity, incidence identities: n=1..100')
    print('VERIFY_OK')

if __name__=='__main__': test()
