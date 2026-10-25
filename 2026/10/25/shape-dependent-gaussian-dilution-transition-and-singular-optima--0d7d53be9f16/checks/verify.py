#!/usr/bin/env python3
"""Exact finite identities for the Gaussian–Gamma-jump concentration pole."""
from fractions import Fraction as F
from math import isqrt

checks=0

def test(ok, name):
    global checks
    if not ok: raise AssertionError(name)
    checks+=1

def a(alpha,m):
    p=F(2)
    for k in range(m): p*=F(alpha+k+2)
    from math import factorial
    return p/F(factorial(m+2))

def m2(s): return (3-2*s)/(3*(1-s)**2)

def phi(s,r): return r*(4-3*s)/(3*(1-s)**2+r*s*(4-3*s))

def dphi_sign(s,r): return (1-r)*(4-3*s)**2-1

# a_0=1, a_1=(alpha+2)/3, a_2=(alpha+2)(alpha+3)/12.
for alpha in [F(1,4),F(1,2),F(1),F(2),F(3),F(5),F(17,4)]:
    test(a(alpha,0)==1,'a0')
    test(a(alpha,1)==(alpha+2)/3,'a1')
    test(a(alpha,2)==(alpha+2)*(alpha+3)/12,'a2')
    rc=a(alpha,2)/a(alpha,1)**2
    test(rc==3*(alpha+3)/(4*(alpha+2)),'critical fraction')
    for m in range(1,8):
        test(a(alpha,m+1)/a(alpha,m)==(alpha+m+2)/F(m+3),'ratio')
        if alpha<=1: test(a(alpha,m)<=1,'nonincreasing')
        else: test(a(alpha,m+1)/a(alpha,m)<=a(alpha,2)/a(alpha,1),'decreasing ratios')

# The independent cumulant transform at alpha=2, beta=1 is M_2(s).
for s in [F(1,20),F(1,9),F(1,5),F(1,3),F(1,2),F(3,4),F(9,10)]:
    raw=((1-s)**-2-1-2*s)/(3*s*s)
    test(raw==m2(s),'compound Poisson Gamma cumulant')
    for r in [F(1,16),F(1,4),F(1,2),F(3,4),F(15,16),F(1)]:
        M=1+r*(raw-1)
        test(phi(s,r)==(1-1/M)/s,'canonical pole')
        h=F(1,1000000)
        if s+h<F(1):
            # A positive difference is expected if and only if the exact
            # derivative numerator is positive away from a critical point.
            actual=phi(s+h,r)-phi(s,r)
            d=dphi_sign(s,r)
            if d>F(1,100): test(actual>0,'derivative positive')
            if d<-F(1,100): test(actual<0,'derivative negative')

# Rationalize sqrt(1-r) by taking 1-r=q*q.
for q in [F(1,3),F(1,2),F(2,3),F(3,4),F(7,8),F(15,16)]:
    r=1-q*q
    if r<F(15,16):
        s=F(4,3)-1/(3*q)
        test(0<s<1,'interior optimizer')
        result=3*(1+q)/(2*(1+2*q))
        test(phi(s,r)==result,'closed Erlang-two pole')
        test(dphi_sign(s,r)==0,'exact stationary argument')
        test(result>max(F(1),F(4,3)*r),'interior strict improvement')

print('PASS exact-rational assertions:',checks)
