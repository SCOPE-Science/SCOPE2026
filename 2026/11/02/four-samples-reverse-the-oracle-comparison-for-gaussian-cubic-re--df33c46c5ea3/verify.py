#!/usr/bin/env python3
"""Exact-rational and simulation checks for Gaussian cubic control-variate risk.

Run: python3 verify.py
Standard library only; simulation is diagnostic, not a proof.
"""
from fractions import Fraction as F
import random

def risk_closed(n):
    assert isinstance(n, int) and n >= 2
    return F(6 * (n**5 + 4*n**4 - 13*n**3 + 176*n**2 - 168*n + 480),
             n**3 * (n+1) * (n+3) * (n+5))

def risk_moments(n):
    # Exact Wick and spherical moment formulas, independently assembled.
    d = n-1
    el = F(6*d, n*(n+1))
    eu2 = F(3*d * (3*n**3 + 23*n**2 - 63*n + 45), n*n)
    el2 = F(9*d*(d+2), n*n) - F(18*d*d, n*n) + eu2 / ((d+4)*(d+6))
    et2 = F(6*d*(n-2), n)
    et2q = et2 / (d+4)
    et2q2 = et2 / ((d+2)*(d+4))
    return F(60,n**3) - F(12,n*n)*el + el2/n + (et2-6*et2q+27*et2q2)/(n*n)

def sample_intercept(xs, mu=F(0), b=F(0), c=F(1)):
    n=len(xs)
    avg=sum(xs)/n
    residuals=[x-avg for x in xs]
    q=sum(z*z for z in residuals)
    if q==0: raise ValueError('degenerate sample')
    ys=[mu+b*x+c*x**3 for x in xs]
    mean_y=sum(ys)/n
    slope=sum(z*y for z,y in zip(residuals,ys))/q
    return mean_y-slope*avg

def centered_formula(xs):
    n=len(xs)
    m=sum(xs)/n
    r=[x-m for x in xs]
    q=sum(x*x for x in r)
    t=sum(x**3 for x in r)
    u=sum(x**4 for x in r)
    return -2*m**3 + 3*m*q/n + t/n - 3*m*m*t/q - m*u/q

checks=0
for n in range(2,201):
    a=risk_closed(n)
    assert a==risk_moments(n)
    assert a>0
    oracle=F(6,n)
    assert (a>oracle if n in (2,3) else a<oracle)
    checks+=3
assert risk_closed(2)==6
assert risk_closed(3)==F(37,18)
assert risk_closed(4)==F(8,7)
checks+=3
rng=random.Random(20261031)
for n in range(2,16):
    for j in range(85):
        xs=[F(rng.randint(-9,9), rng.randint(1,6)) for _ in range(n)]
        if len(set(xs))==1: continue
        mu=F(rng.randint(-9,9),rng.randint(1,6))
        b=F(rng.randint(-9,9),rng.randint(1,6))
        c=F(rng.randint(1,9),rng.randint(1,6))
        assert sample_intercept(xs,mu,b,c)==mu+c*centered_formula(xs)
        checks+=1
# The two-observation intercept is a polynomial and has risk 6 exactly.
a,b=F(2),F(5)
assert centered_formula([a,b]) == -a*b*(a+b)
checks+=1
print(f'PASS: {checks} independent exact-rational assertions')
# An optional independent distributional simulation, deliberately not used for acceptance.
rng=random.Random(6102022)
for n in (2,3,4,6,10):
    trials=30000
    ss=0.0
    for _ in range(trials):
        xs=[rng.gauss(0,1) for k in range(n)]
        m=sum(xs)/n
        r=[x-m for x in xs]
        q=sum(x*x for x in r)
        y=[x**3 for x in xs]
        intercept=sum(y)/n - (sum(z*v for z,v in zip(r,y))/q)*m
        ss+=intercept*intercept
    empirical=ss/trials
    expected=float(risk_closed(n))
    assert abs(empirical-expected) < 0.12*expected, (n,empirical,expected)
    print(f'n={n}: simulated risk={empirical:.6f}, exact={expected:.6f}')
print('PASS: simulation diagnostics (not an infinite-domain proof)')
