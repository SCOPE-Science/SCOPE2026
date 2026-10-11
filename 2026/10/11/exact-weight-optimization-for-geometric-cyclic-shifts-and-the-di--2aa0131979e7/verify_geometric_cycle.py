#!/usr/bin/env python3
"""Finite consistency checks and exact certificates for geometric cyclic shifts."""
from fractions import Fraction
from math import log, exp, isclose


def upper_direct(n, a, r, theta):
    weights = [a**j for j in range(n)]
    sums = [weights[j]**(4*r*theta) + weights[(j+1)%n]**(4*r*(1-theta)) for j in range(n)]
    products = [weights[j]**(2*r*theta)*weights[(j+1)%n]**(2*r*(1-theta)) for j in range(n)]
    return max(sums)/4 + max(products)/2


def upper_reduced(n, a, r, theta):
    u = a**(4*r*(n-2)*theta)
    v = a**(4*r*(n-1)*(1-theta))
    z = a**(4*r*(n-1)*theta)
    p = a**(2*r*(n-1-theta))
    q = a**(2*r*(n-1)*theta)
    return max(u+v,z+1)/4 + max(p,q)/2


def root_bisect(f, lo, hi, increasing=False):
    flo, fhi = f(lo), f(hi)
    assert (flo < 0 < fhi) if increasing else (flo > 0 > fhi)
    for _ in range(90):
        mid = (lo+hi)/2
        if ((f(mid) < 0) if increasing else (f(mid) > 0)):
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def optimum(n, a, r):
    if n == 2:
        return 0.5
    k = 4*r*log(a)
    def f(t):
        return exp(k*(n-2)*t)+exp(k*(n-1)*(1-t))-exp(k*(n-1)*t)-1
    def g(t):
        return (n-2)*exp(k*(n-2)*t)-(n-1)*exp(k*(n-1)*(1-t))-exp(k*(n-1-t)/2)
    tau = root_bisect(f,0.5,(n-1)/n)
    return root_bisect(g,0.5,tau,increasing=True) if g(tau)>0 else tau


for n in (2, 3, 4, 5, 10, 20):
    for a,r in ((1.2,1.0),(2.0,1.0),(1.1,2.3)):
        for j in range(21):
            t=j/20
            x,y=upper_direct(n,a,r,t),upper_reduced(n,a,r,t)
            assert isclose(x,y,rel_tol=5e-13,abs_tol=1e-11)
        t=optimum(n,a,r)
        assert isclose(upper_direct(n,a,r,t),upper_reduced(n,a,r,t),rel_tol=5e-13)
        assert (abs(t-.5)<1e-13 if n==2 else (.5<t<(n-1)/n and upper_direct(n,a,r,t)<upper_direct(n,a,r,.5)))
        for dt in (-.005,-.001,.001,.005):
            theta=t+dt
            if 0<=theta<=1:
                assert upper_direct(n,a,r,t) <= upper_direct(n,a,r,theta)*(1+1e-12)

# Complete *exact rational* sign certificate for n=10, a=6/5, r=1.
y_lo=Fraction(10183,10000)
y_hi=Fraction(10185,10000)
a=Fraction(6,5)
assert y_lo**10 < a < y_hi**10
assert y_lo**176+y_lo**162-y_hi**198-1 > 0
assert a**7 > Fraction(9,8)**10
assert .5 < optimum(10,1.2,1.0) < .55

# Dimension-three closed expression, independently checked at a=2, r=1.
t=optimum(3,2.0,1.0)
h=2.0**(4*t)
assert abs(h**4-h**3+h**2-256)<1e-9
value=(1+h*h)/4+8/h**.5
assert abs(value-upper_direct(3,2.0,1.0,t))<1e-10
assert 8.57<value<8.58 and value<9

print('GEOMETRIC_CYCLE_WEIGHT_OPTIMIZATION_EXACT_RATIONAL_AND_CONSISTENCY_OK')
