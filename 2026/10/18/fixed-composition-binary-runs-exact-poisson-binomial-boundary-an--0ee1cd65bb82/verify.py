#!/usr/bin/env python3
"""Exact finite checks for the fixed-composition run-count theorem."""
from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import comb

def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0

def formula(a, b):
    n = a + b
    return Counter({t: (2*c(a-1,(t+1)//2-1)*c(b-1,(t+1)//2-1)
                        if t % 2 else
                        c(a-1,t//2)*c(b-1,t//2-1)
                        +c(a-1,t//2-1)*c(b-1,t//2))
                    for t in range(1, n) if
                    (2*c(a-1,(t+1)//2-1)*c(b-1,(t+1)//2-1)
                     if t%2 else c(a-1,t//2)*c(b-1,t//2-1)
                     +c(a-1,t//2-1)*c(b-1,t//2)) > 0})

def exhaustive(a, b):
    n=a+b
    out=Counter()
    for positions in combinations(range(n),a):
        ones=set(positions)
        transitions=sum((i in ones)!=(i+1 in ones) for i in range(n-1))
        out[transitions]+=1
    return out

def mean_var(counts, nways):
    mean=Fraction(sum(t*cnt for t,cnt in counts.items()),nways)
    var=Fraction(sum(t*t*cnt for t,cnt in counts.items()),nways)-mean*mean
    return mean,var

checks=0
for a in range(1,7):
    for b in range(1,7):
        e=exhaustive(a,b); f=formula(a,b)
        assert e==f,(a,b,e,f)
        assert sum(f.values())==comb(a+b,a)
        mean,var=mean_var(e,comb(a+b,a));n=a+b
        assert mean==Fraction(2*a*b,n)
        assert var==Fraction(2*a*b*(2*a*b-n),n*n*(n-1))
        checks+=4
for m in range(2,25):
    for h in range(m,81):
        n=m+h; mean=Fraction(2*m*h,n)
        var=Fraction(2*m*h*(2*m*h-n),n*n*(n-1))
        M=2*m-int(h==m)
        ceiling=(mean-1)*(M-mean)/Fraction(M-1)
        gap=var-ceiling
        if h>m:
            expected=Fraction(2*m*(m-1)*(h-m)*(2*m*h-m-h),
                         n*n*(2*m-1)*(n-1))
        else:
            expected=Fraction(m-1,2*(2*m-1))
        assert gap==expected and gap>0,(m,h,gap,expected)
        checks+=1
for h in range(1,81):
    a=1;b=h
    fs=formula(a,b)
    assert fs[1]==2 and fs[2]==h-1 or h==1 and fs==Counter({1:2})
    checks+=1
print(f'PASS: {checks} exact checks of counting, moments, boundaries, variance gaps')
