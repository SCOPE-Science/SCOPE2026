#!/usr/bin/env python3
"""Exact finite checking and stable tail-ratio checks for conditional
one-step counting formulas on uniformly colored rooted trees.
No symbolic proof is inferred from numerical tests.
"""
from fractions import Fraction
from itertools import product
from math import comb, ceil


def exact_bin_tail_ratio(n, a, b, h):
    # n leaves, each with a successes among b equally likely atomic colors.
    p=Fraction(a,b)
    lower=(n+1)//2
    weights=[comb(n,x)*p**x*(1-p)**(n-x) for x in range(lower,n+1)]
    den=sum(weights)
    num=sum(w for x,w in zip(range(lower,n+1),weights) if 2*x-n>=h)
    return num/den


def overshoot_ratio(n, p, h):
    # Conditional distribution of j=X-ceil(n/2), normalized by mass at j=0.
    # Stable recursion, not a numerical summation of exponentially rare tails.
    k=(n+1)//2
    w=1.0
    all_w=1.0
    good_w=float(2*k-n>=h)
    for j in range(1,n-k+1):
        w *= ((n-k-j+1)/(k+j))*(p/(1-p))
        all_w+=w
        if 2*(k+j)-n>=h:good_w+=w
    return good_w/all_w


def check():
    # Independent model enumeration using four equally likely truth colors.
    for n in range(1,8):
        den=0; num=0
        for bits in product(range(4),repeat=n):
            x=sum(t==3 for t in bits)  # conjunction of two letters
            if 2*x >= n:
                den+=1
                if 2*x-n>=3:num+=1
        assert den>0
        value=Fraction(num,den)
        assert value==exact_bin_tail_ratio(n,1,4,3)
    print('CHECK_ENUM', 'n=1..7', '4^n colorings', 'matched exactly')
    for a,b in [(1,4),(3,8),(1,2),(5,8)]:
        for n in range(1,28):
            for h in range(1,7):
                exact=float(exact_bin_tail_ratio(n,a,b,h))
                approx=overshoot_ratio(n,a/b,h)
                assert abs(exact-approx)<1e-12,(n,a,b,h,exact,approx)
    print('CHECK_EXACT_TAIL', 'p=1/4,3/8,1/2,5/8','n=1..27','h=1..6')
    for a,b in [(1,4),(3,8)]:
        rho=a/(b-a)
        for h in range(1,8):
            le=rho**ceil(h/2)
            lo=rho**ceil((h-1)/2)
            for n,target in [(3000,le),(3001,lo)]:
                actual=overshoot_ratio(n,a/b,h)
                assert abs(actual-target)<0.005,(n,a,b,h,actual,target)
    print('CHECK_PHASE', 'subsequential geometric limits through h=7')
    for p in [0.5,0.625]:
        for n in (3000,3001):
            assert overshoot_ratio(n,p,3)>0.90
    print('CHECK_NONRARE', 'p=1/2,5/8', 'n=3000,3001')
    for n in (100,101,1000,1001,3000,3001):
        print('EXAMPLE',n,round(overshoot_ratio(n,0.25,3),9))
    print('ALL_CHECKS_OK')

if __name__=='__main__':check()
