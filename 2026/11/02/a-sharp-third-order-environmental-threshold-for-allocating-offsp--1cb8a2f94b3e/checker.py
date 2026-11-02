#!/usr/bin/env python3
"""Reproduce exact finite calculations for a three-habitat log-growth model.

Requires only Python 3 standard library. The paper's all-parameter proof is analytic;
this checker tests its identities over an explicit finite rational test set.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt

EVEN = ((0,0,0),(0,1,1),(1,0,1),(1,1,0))
ODD = ((0,0,1),(0,1,0),(1,0,0),(1,1,1))
checks=0

def assert_eq(x,y):
    global checks
    assert x == y, (x,y)
    checks += 1

def thresholds(a):
    return a*(3*a+4)/(a+2)**2, a*(3*a+4)/(4*(a+1))

def derivative(a,b,z,t):
    """Direct four-state differentiation, not the closed-form threshold."""
    d=F(0)
    for support,weight in ((EVEN,1-t),(ODD,t)):
        for x,y,q in support:
            base=1+a*(x+y)/2
            slope=b*q-a*(x+y)/2
            d += weight*slope/(base+slope*z)/4
    return d

def curvature(a,b,z,t):
    result=F(0)
    for support,weight in ((EVEN,1-t),(ODD,t)):
        for x,y,q in support:
            base=1+a*(x+y)/2
            slope=b*q-a*(x+y)/2
            result-=weight*slope*slope/(base+slope*z)**2/4
    return result

def d_zero_closed(a,b,t):
    return (b*(4*(a+1)+t*a*a)-a*(3*a+4))/(4*(a+1)*(a+2))

def d_one_closed(a,b):
    return (2*b-2*a-a*b)/(4*(1+b))

for a_num,a_den,b_num,b_den,t_num,t_den,z_num,z_den in product(
        range(1,9), (1,2,3), range(1,9), (1,2,3), (0,1,2,3), (3,), (0,1,2,3), (3,)):
    a=F(a_num,a_den);b=F(b_num,b_den)
    if not 0<b<a: continue
    t=F(t_num,t_den); z=F(z_num,z_den)
    assert_eq(derivative(a,b,F(0),t),d_zero_closed(a,b,t))
    assert_eq(derivative(a,b,F(1),t),d_one_closed(a,b))
    assert curvature(a,b,z,t)<0
    checks+=1

for a in (F(1,10),F(1,3),F(1),F(2),F(3),F(7,2),F(8),F(100)):
    low,high=thresholds(a)
    assert 0<low<high<a
    checks+=1
    for t in (F(0),F(1,4),F(1,3),F(1,2),F(3,4),F(1)):
        boundary=a*(3*a+4)/(4*(a+1)+t*a*a)
        assert_eq(d_zero_closed(a,boundary,t),F(0))
        assert low<=boundary<=high
        checks+=1

# Each of the two parity laws is individually pairwise independent Bernoulli(1/2).
for support in (EVEN,ODD):
    for i in range(3):
        assert_eq(sum(x[i] for x in support),2)
        for j in range(i+1,3):
            assert_eq(sum(x[i]*x[j] for x in support),1)

# Explicit strict threshold example: a=2, b=3/2, t*=1/3.
a=F(2);b=F(3,2)
assert_eq(thresholds(a),(F(5,4),F(5,3)))
assert_eq(d_zero_closed(a,b,F(0)),F(-1,24))
assert_eq(d_zero_closed(a,b,F(1)),F(1,12))
assert_eq(d_zero_closed(a,b,F(1,3)),F(0))
root=(15-sqrt(201))/6
assert 0.137<root<0.138
assert abs(float(derivative(a,b,F(root).limit_denominator(10**10),F(1))))<1e-9
checks+=2
print('PASS:',checks,'exact rational and deterministic example assertions')
