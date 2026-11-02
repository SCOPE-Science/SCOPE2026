"""Supplementary checks for real Blaschke quotient phase boundaries.

Run with Python 3.10+; only standard-library dependencies.  These tests
check exact identities and finite samples, not the quantified analytic proof.
"""
from fractions import Fraction as F
from math import sqrt
import random

count = 0

def check(test):
    global count
    assert test
    count += 1

def N(a,b,x):
    return (4*a*b*x*x - 4*b*(1+a*b)*x +
            1-a*a+3*b*b+a*a*b*b)

def Nraw(a,b,x):
    da = 1-2*a*x+a*a
    db = 1-2*b*x+b*b
    return da*db+(1-a*a)*db-(1-b*b)*da

def criterion(a,b,strict=True):
    lo=-(1-a)/(3+a)
    hi=(1+a)/(3-a)
    if not (lo<b<hi if strict else lo<=b<=hi):
        return False
    if a*b>0 and abs(a)>=sqrt(3)/2:
        s=abs(a)
        disc=sqrt(max(0.0,4*s*s-3))
        rm=(1-disc)/(2*s)
        rp=(1+disc)/(2*s)
        if (rm<=abs(b)<=rp if strict else rm<abs(b)<rp):
            return False
    return True

def actual_positive(a,b):
    v=[N(a,b,-1),N(a,b,1)]
    if a*b>0:
        x0=(1+a*b)/(2*a)
        if -1<x0<1:
            v.append(N(a,b,x0))
    return min(v)>0

vals=[F(k,12) for k in range(-11,12)]
for a in vals:
    for b in vals:
        for x in vals:
            check(N(a,b,x)==Nraw(a,b,x))
        check(N(a,b,F(1))==(a-1)*(b-1)*(a*b+a-3*b+1))
        check(N(a,b,F(-1))==(a+1)*(b+1)*(a*b-a+3*b+1))
        if a:
            v=(1+a*b)/(2*a)
            check(N(a,b,v)==(a-b)*(1-a*a-a*b+a*a*b*b)/a)

# A rational four-turning-point witness with positive endpoint speeds.
a=F(9,10); b=F(1,2); x=F(29,36)
check(N(a,b,x)==-F(23,900))
check(N(a,b,F(1))==F(17,400))
check(N(a,b,F(-1))==F(2337,400))

rng=random.Random(53017)
for _ in range(80000):
    a=rng.uniform(-.999,.999)
    b=rng.uniform(-.999,.999)
    check(criterion(a,b,True)==actual_positive(a,b))

# The non-regular homeomorphic boundaries are included by weak inequalities.
for a in [F(-10,11),F(-1,2),F(0),F(1,2),F(9,10)]:
    for b in [-(1-a)/(3+a),(1+a)/(3-a)]:
        check(N(a,b,F(-1))>=0 and N(a,b,F(1))>=0)

print('PASS:',count,'supplementary exact and numerical assertions')
