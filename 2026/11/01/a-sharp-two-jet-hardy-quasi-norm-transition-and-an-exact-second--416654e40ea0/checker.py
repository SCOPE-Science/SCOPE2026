#!/usr/bin/env python3
"""Independent standard-library arithmetic and sampling checks for the displayed Hardy formulas.

This supplements, but does not replace, the infinite-dimensional analytic argument.
"""
from fractions import Fraction as Q
from math import sqrt, isclose
import random

# Exact identities at the two-branch contact.
r=Q(1,3); tau=Q(1,2); x=Q(9,10)
assert tau == r/(1-3*r*r)
assert (1+4*tau*r)/(1+r*r)**2 == Q(27,20)
assert 27*tau*tau/(16*tau-3) == Q(27,20)
assert 6*tau*x+(1-Q(16,3)*tau)*x*x == Q(27,20)
assert x == 9*tau/(16*tau-3)
assert Q(486,125)-Q(81,125)==Q(81,25)
# The high-frequency endpoint and fixed-origin crossover.
y=Q(9,10)
assert 6*y-Q(16,3)*y*y == 4*y*y*Q(1,3)
assert 6*Q(9,16)-Q(16,3)*Q(81,256)==Q(27,16)
assert (Q(9,16))**2==Q(81,256)
assert (Q(9,10))**2==Q(81,100)

def analytic_value(t):
    if t<=0: return 1., 1., 0.,0.,0.
    if t<=0.5:
        r=(sqrt(1+12*t*t)-1)/(6*t)
        a=1/sqrt(1+r*r)
        return (1+4*t*r)/(1+r*r)**2,a,0.,a*r,r
    a=sqrt(9*t/(16*t-3))
    u=sqrt((2*t-1)/(3*t))
    return 27*t*t/(16*t-3),a,a*u,a/3,u

count=0
for tau in [0.0,0.01,0.1,0.3,0.499,0.5,0.501,1,2,10,100]:
    expected,a,b,c,_=analytic_value(tau)
    assert isclose(a*a+b*b+c*c,1.0,abs_tol=2e-12)
    assert isclose(a**4+tau*(4*a**3*c+6*a*a*b*b),expected,abs_tol=2e-11)
    for coeff in (b,c):
        assert coeff>=0
    # Random complex unit vectors of length five model first coefficients
    rng=random.Random(100+int(10000*tau))
    for _ in range(500):
        coeff=[complex(rng.gauss(0,1),rng.gauss(0,1)) for j in range(5)]
        norm=sqrt(sum(abs(v)**2 for v in coeff)); coeff=[v/norm for v in coeff]
        aa,bb,cc=coeff[:3]
        sample=abs(aa**4+tau*(4*aa**3*cc+6*aa*aa*bb**2))
        assert sample <= expected+1e-10,(tau,sample,expected)
        count+=1
assert count==5500
# Fixed-origin coefficients attained by explicit analytic bases
for y in [9/16,0.6,0.75,0.9,0.93,1.]:
    t=y*y
    if y<=0.9:
        a=sqrt(y)
        c=a/3
        b=sqrt(max(0,1-a*a-c*c))
        val=a**4*(4/3+6*(b/a)**2)
        formula=6*y-16*t/3
    else:
        r=sqrt(1/y-1)
        a=1/sqrt(1+r*r)
        val=4*a**4*r
        formula=4*t**0.75*sqrt(1-sqrt(t))
    assert isclose(val,formula,abs_tol=2e-12),(y,val,formula)
print('CHECKER_OK: 5500 deterministic complex-triple comparisons; exact rational contact; finite fixed-origin examples')
