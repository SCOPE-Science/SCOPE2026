#!/usr/bin/env python3
"""Exact checks of conditional fixed-point identities for uniform random mappings."""
from collections import defaultdict, Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial


def fall(x, k):
    v=1
    for t in range(k):v*=x-t
    return v


def elementary(d,k):
    e=[0]*(k+1)
    e[0]=1
    for x in d:
        for j in range(k,0,-1): e[j]+=x*e[j-1]
    return e[k]


def exact_factorial_moments_from_counts(counts,maxk):
    total=sum(counts.values())
    return [Fraction(sum(fall(f,k)*c for f,c in counts.items()),total) for k in range(maxk+1)]


def run():
    tests=0
    for n in range(2,7):
        by_degree=defaultdict(Counter)
        by_rank=defaultdict(Counter)
        for choices in product(range(n),repeat=n):
            d=[0]*n
            for c in choices:d[c]+=1
            f=sum(i==c for i,c in enumerate(choices))
            by_degree[tuple(d)][f]+=1
            by_rank[sum(x>0 for x in d)][f]+=1
        for d,counts in by_degree.items():
            a=exact_factorial_moments_from_counts(counts,n)
            for k in range(n+1):
                assert a[k]==Fraction(factorial(k)*elementary(d,k),fall(n,k))
                tests+=1
            collision=Fraction(sum(x*(x-1) for x in d),n*(n-1))
            assert a[1]==1 and a[2]==1-collision
            tests+=2
            for k in range(2,n+1):
                assert 0<=1-a[k]<=comb(k,2)*collision
                tests+=1
        for r,counts in by_rank.items():
            a=exact_factorial_moments_from_counts(counts,n)
            for k in range(n+1):
                if k>r:
                    target=Fraction(0)
                else:
                    # Number of length n-k sequences that hit each of r-k unmarked boxes.
                    cover=sum((-1)**j*comb(r-k,j)*(r-j)**(n-k) for j in range(r-k+1))
                    surj=sum((-1)**j*comb(r,j)*(r-j)**n for j in range(r+1))
                    target=Fraction(fall(r,k)*cover,surj)
                assert a[k]==target,(n,r,k,a[k],target)
                tests+=1
                if k<=r:
                    assert Fraction(fall(r,k),r**k)<=a[k]<=1
                    tests+=1
            assert a[1]==1
            tests+=1
    print('PASS:',tests,'exact finite-size assertions; all maps exhaustively enumerated through n=6')

if __name__=='__main__':run()
