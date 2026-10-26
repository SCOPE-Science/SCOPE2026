#!/usr/bin/env python3
"""Exact-rational checks for Gaussian Toeplitz localization in one Landau level."""
from fractions import Fraction as F
from math import factorial, comb

def via_integral(k, u):
    s = 1/u
    if k == 0:
        terms = {2:1}
    elif k == 1:
        terms = {3:1,2:-4,1:4}
    else:
        a = k*(k-1)
        terms = {k+2:1,k+1:-4*k,k:4*k*k+2*a,k-1:-4*k*a,k-2:a*a}
    return sum((F(c*factorial(j),2*factorial(k))*s**(-j-1) for j,c in terms.items()),F(0))

def closed(k,u):
    if k==0:return u**3
    if k==1:return u**2*(3*u*u-4*u+2)
    return u**(k-1)*(F(comb(k,2))*(1-u)**4+2*k*u*u*(1-u)**2+u**4)

def q(k,r):
    return F(comb(k,2))*r**4-k*r**3+2*k*r*r-2*r+1

cases=0
for u in [F(1,100),F(1,10),F(1,4),F(1,2),F(2,3),F(3,4),F(9,10),F(99,100)]:
    for k in range(21):
        assert closed(k,u)==via_integral(k,u),(k,u)
        cases+=1
    assert closed(1,u)-closed(0,u)==u*u*(u-1)*(3*u-2)
    assert closed(2,u)-closed(1,u)==u*(u-1)*(2*u-1)*(3*u*u-3*u+1)
    cases+=2
    r=(1-u)/u
    for k in range(2,20):
        assert closed(k+1,u)-closed(k,u)==-u**(k+3)*(1-u)*q(k,r)
        assert q(k,r)>0
        cases+=2
for k in range(21):
    assert closed(k,F(1))==1
    cases+=1
for tau,winners in [(F(1,5),{0}),(F(1,2),{0,1}),(F(3,4),{1}),(F(1),{1,2}),(F(2),{2}),(F(10),{2})]:
    u=1/(1+tau)
    vals=[closed(k,u) for k in range(40)]
    winners_actual={k for k,v in enumerate(vals) if v==max(vals)}
    assert winners_actual==winners,(tau,winners_actual)
    cases+=1
print(f'EXACT_RATIONAL_CHECKS_PASS: {cases}')
