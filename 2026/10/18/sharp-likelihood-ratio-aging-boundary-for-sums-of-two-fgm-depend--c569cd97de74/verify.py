#!/usr/bin/env python3
"""Stand-alone exact witness and illustrative numeric checks for an exponential FGM sum."""
from fractions import Fraction as F
from math import exp, factorial, sqrt, isclose

def alt_sum(n):
    s=F(3,2)
    return sum(((-s)**k/F(factorial(k)) for k in range(n+1)),F(0))

lo,hi=alt_sum(19),alt_sum(20)
assert F(223,1000)<lo<hi<F(224,1000)

def d_witness(r):
    return -16*r*r+22*r-4
assert d_witness(F(223,1000))>0
assert d_witness(F(224,1000))>0
# Its derivative in r is 22-32r>0 throughout the rational bracket.
assert 22-32*F(224,1000)>0
print('EXACT WITNESS PASS: D(3/2)>0 using rational alternating-series bounds')

def g(s,theta):
    return s+theta*(s-4+4*(s+1)*exp(-s))

def gp(s,theta):
    return 1+theta*(1-4*s*exp(-s))

def gpp(s,theta):
    return 4*theta*(s-1)*exp(-s)

def D(s,theta):
    return g(s,theta)*gpp(s,theta)-gp(s,theta)**2

def Cplus(s):
    return 4*(s*(s+1)*exp(-s)-1)

def Dplus(s):
    r=exp(-s)
    return -4*(4*r*r-2*s*s*r+2*s*r-4*r+1)

# Independently compare the exact quadratic identity against the direct derivatives.
for s in (0.125,0.5,1.0,1.5,2.0,3.0,7.0):
    for theta in (-1.0,-0.7,0.0,0.4,0.85,0.9,1.0):
        if theta>=0:
            expected=-(1-theta)**2+theta*(1-theta)*Cplus(s)+theta**2*Dplus(s)
            assert isclose(D(s,theta),expected,abs_tol=1e-12,rel_tol=1e-12)
        assert g(s,theta)>0
        h=0.00001
        dnum=(g(s+h,theta)-g(s-h,theta))/(2*h)
        assert abs(dnum-gp(s,theta))<3e-8
print('ALGEBRA AND NUMERICAL DERIVATIVE CROSS-CHECKS PASS')

# Exploratory maximum only, not proof of where the supremum lies.
def T(s):
    d=Dplus(s)
    if d<=0:
        return 0.0
    c=Cplus(s)
    return (c+sqrt(c*c+4*d))/2

max_t=0.0
max_s=None
for j in range(1,200001):
    s=8*j/200000
    t=T(s)
    if t>max_t:
        max_t,max_s=t,s
crit=1/(1+max_t)
assert 0.859<crit<0.862
assert D(1.5,1)>0
assert D(1.5,0.5)<0
print('EXPLORATORY NUMERIC theta critical:',format(crit,'.12f'),'at s around',format(max_s,'.5f'))
print('SUCCESS: all reproducibility checks completed')
