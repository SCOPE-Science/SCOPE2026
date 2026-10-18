#!/usr/bin/env python3
"""Exact enumeration for the cyclic chord-length/crossing covariance law.
Usage: python3 verify.py. Python standard library only.
"""
from collections import Counter
from fractions import Fraction
from math import comb,isqrt

def matchings(seq):
    if not seq:
        yield ()
        return
    x=seq[0]
    for k in range(1,len(seq)):
        y=seq[k]
        for tail in matchings(seq[1:k]+seq[k+1:]):
            yield ((x,y),)+tail

def crossing(pairs):
    return sum(a<c<b<d or c<a<d<b for i,(a,b) in enumerate(pairs) for c,d in pairs[i+1:])

def profile(pairs,n):
    return Counter(min(b-a-1,2*n-(b-a)-1) for a,b in pairs)

def prediction(n,j):
    edges=2*n if j<n-1 else n
    bracket=Fraction(j*(2*n-2-j),2*n-3)-Fraction(n-1,3)
    return Fraction(edges,2*n-1)*bracket

checks=0
for n in range(2,8):
    totals=[Fraction(0) for _ in range(n)]
    moment=[Fraction(0) for _ in range(n)]
    meanC=Fraction(0)
    num=0
    for m in matchings(tuple(range(2*n))):
        num+=1
        c=crossing(m)
        meanC+=c
        p=profile(m,n)
        for j in range(n):
            totals[j]+=p[j]
            moment[j]+=p[j]*c
    expect=1
    for q in range(1,2*n,2):expect*=q
    assert num==expect
    checks+=1
    meanC/=num
    assert meanC==Fraction(n*(n-1),6)
    checks+=1
    for j in range(n):
        EJ=totals[j]/num
        EJ2=Fraction(2*n if j<n-1 else n,2*n-1)
        assert EJ==EJ2
        cov=moment[j]/num-EJ*meanC
        assert cov==prediction(n,j),(n,j,cov,prediction(n,j))
        t=n-1
        iszero=(3*(t-j)**2==t*(t+1))
        assert (cov==0)==iszero
        checks+=3
    assert sum(prediction(n,j) for j in range(n))==0
    checks+=1

# Elementary Pell recurrence (x+b sqrt(12))*(7+2 sqrt(12)), x^2-12b^2=1.
x,b=1,0
for n0,j0 in [(4,1),(49,20),(676,285),(9409,3976)]:
    x,b=7*x+24*b,2*x+7*b
    n=(x+1)//2
    j=(x-1)//2-b
    assert x*x-12*b*b==1
    assert (n,j)==(n0,j0),(n,j,n0,j0)
    assert prediction(n,j)==0
    checks+=3
print(f'PASS: {checks} exact assertions; all matchings n=2..7 and Pell cases')
