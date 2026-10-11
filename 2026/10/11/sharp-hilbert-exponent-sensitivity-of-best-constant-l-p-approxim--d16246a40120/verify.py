#!/usr/bin/env python3
"""Numerical consistency checks for the exponent-response formulas.
Analytic uniqueness, universal inequalities and empirical asymptotics are proved
in RESULT.md; finite tests here are checks, not certificates of those theorems.
"""
from math import log, sqrt, isfinite

def h(a):
    return ((a*a-1)/(a*a+1))*log(a)-1
lo, hi = 1.0, 10.0
assert h(lo) < 0 < h(hi)
for _ in range(100):
    mid=(lo+hi)/2
    if h(mid)<0:lo=mid
    else:hi=mid
a=(lo+hi)/2
b=1/a
prob=1/(1+a*a)
kappa=2*a*log(a)/(1+a*a)
assert abs(h(a))<1e-14
assert abs(prob*a+(1-prob)*(-b))<1e-14
assert abs(prob*a*a+(1-prob)*b*b-1)<1e-14
assert abs(prob*a*log(a)+(1-prob)*(-b)*log(b)-kappa)<1e-14
assert abs(kappa-2*a/(a*a-1))<1e-13

def scalar(y):
    return y*log(abs(y)) if y else 0
c=kappa/2
for k in range(-50000,50001):
    y = 50*k/50000
    assert scalar(y) <= c*(1+y*y)+1e-10
for k in range(-10000,10001):
    y=(k/3000.)
    assert scalar(y) <= c*(1+y*y)+1e-10

def optimal_m(p):
    q=(1-prob)/prob
    ratio=q**(1/(p-1))
    return (a-ratio*b)/(1+ratio)
for epsilon in (0.01,0.001,0.0001, -0.01,-0.001,-0.0001):
    approx=(optimal_m(2+epsilon)-optimal_m(2))/epsilon
    assert abs(approx-kappa)<0.04
for n in (30,100,1000,10000):
    j=max(1,min(n-1,int(n*prob+0.5)))
    t=j/n
    s=sqrt(t*(1-t))*log((1-t)/t)
    assert s<=kappa+1e-11
    assert abs(s-kappa)<= 20/(n*n)
print('EXPONENT_SENSITIVITY_CHECK_OK')
print('a=', format(a,'.15g'), 'kappa=',format(kappa,'.15g'), 'prob=',format(prob,'.15g'))
