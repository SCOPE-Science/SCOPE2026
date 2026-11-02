#!/usr/bin/env python3
"""Reproduce rational Fisher reductions and numerical design checks.

The analytic uniqueness and monotonicity proofs are in RESULT.md; finite checks
here are corroborative and are not certificates of the continuum statements.
"""
from fractions import Fraction as F
from math import exp, e, log, sqrt

exact = 0
numeric = 0

def trial(p, r):
    global exact
    q = F(1, 2)
    a = p*q
    c = p*p*q*(1-q)*r
    aq = p
    cq = p*p*(1-2*q)*r
    cr = p*p*q*(1-q)
    cells = [(a*a+c, 2*a*aq+cq, cr),
             (a*(1-a)-c, aq*(1-2*a)-cq, -cr),
             (a*(1-a)-c, aq*(1-2*a)-cq, -cr),
             ((1-a)**2+c, -2*(1-a)*aq+cq, cr)]
    assert all(t[0] > 0 for t in cells)
    assert sum(t[0] for t in cells) == 1
    jqq = sum(t[1]*t[1]/t[0] for t in cells)
    jqr = sum(t[1]*t[2]/t[0] for t in cells)
    jrr = sum(t[2]*t[2]/t[0] for t in cells)
    eff = jrr - jqr*jqr/jqq
    D = (2-p)**2 + 4*(1-p)**2*r -p*p*r*r
    assert eff == p*p/D
    assert jqq > 0 and eff > 0
    exact += 5

for i in range(1,21):
    p = F(i,20)
    for j in range(1,24):
        r=F(j,24)
        trial(p,r)


def D(p,x):
    r=exp(-x)
    return (2-p)**2 + 4*(1-p)**2*r -p*p*r*r

def g(p,x):
    A=(2-p)**2
    B=4*(1-p)**2
    C=p*p
    r=exp(-x)
    return x*(2*A+B*r)-2*(A+B*r-C*r*r)

def deriv_g(p,x):
    A=(2-p)**2
    B=4*(1-p)**2
    C=p*p
    r=exp(-x)
    return 2*A+B*r*(3-x)-4*C*r*r

def optimum(p):
    global numeric
    a=log(2)
    b=2.0
    assert g(p,a)<0<g(p,b)
    for _ in range(70):
        m=(a+b)/2
        if g(p,m)<0:a=m
        else:b=m
    x=(a+b)/2
    assert abs(g(p,x))<1e-11
    assert deriv_g(p,x)>0
    numeric+=3
    return x

pc=sqrt(2*e)/(1+sqrt(2*e))
x1=optimum(1.0)
# The p=0 optimizer is a limiting design: information itself vanishes at p=0.
x0=optimum(0.0)
assert abs(x1-0.7968121300200200)<1e-11
assert abs(x0-1.1380908540666150)<1e-11
assert abs(pc-0.6998478812491184)<1e-12
numeric+=3
last=100
for i in range(1,101):
    p=i/100
    x=optimum(p)
    assert x<last and x1-1e-10<=x<x0+1e-10
    if p<pc:assert x>1
    if p>pc:assert x<1
    # Spot-check log-score sign on each side of the root.
    assert g(p,max(.001,x-.02))<0 and g(p,x+.02)>0
    last=x
    numeric+=5

# Independent finite-difference check on the Fisher objective.
for p in (0.05, 0.2, 0.5, 0.7, 0.9, 1.0):
    x=optimum(p)
    def obj(z):return p*p*z*z*exp(-2*z)/D(p,z)
    for h in (0.001, 0.02, 0.15):
        assert obj(x)>obj(x-h) and obj(x)>obj(x+h)
        numeric+=2

print(f'VERIFICATION_OK exact_assertions={exact} numerical_assertions={numeric} ' 
      f'perfect={x1:.12f} low_detection_limit={x0:.12f} crossing={pc:.12f}')
