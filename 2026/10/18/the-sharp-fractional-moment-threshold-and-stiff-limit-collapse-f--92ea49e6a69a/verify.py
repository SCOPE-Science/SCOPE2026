#!/usr/bin/env python3
"""Reproduce deterministic checks for a scalar randomized implicit RK2 moment law."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

count = 0

def check(test):
    global count
    count += 1
    if not test:
        raise AssertionError('assertion ' + str(count))

def x(a, u):
    return (1.0-a+a*u)/(1.0+a*u)

def moment(a, p):
    c = 1.0-1.0/a
    f = lambda u: abs(x(a, u))**p
    if 0.0 < c < 1.0:
        return quad(f, 0, c, epsabs=1e-11, epsrel=1e-11, limit=300)[0] + quad(f, c, 1, epsabs=1e-11, epsrel=1e-11, limit=300)[0]
    return quad(f, 0, 1, epsabs=1e-11, epsrel=1e-11)[0]

def root(a):
    lo, hi = 1.e-4, 2.0
    while moment(a, hi) < 1.0:
        hi *= 2.0
    return brentq(lambda p: moment(a, p)-1.0, lo, hi, xtol=2e-11)

for a in [0.1, .5, 1.5, 2.0, 2.1, 3., 4., 10., 100.]:
    for u in np.linspace(0, 1, 117):
        check(abs(x(a, u)-(1.0-a/(1.0+a*u))) < 1e-12)
    for p in [.1, .3, .6, 1., 2., 3.]:
        val = moment(a, p)
        check(val > 0)
        if a <= 2.0: check(val < 1.0)
    if a > 1.0:
        g = ((a-1)*math.log(a-1)-(a+1)*math.log(a+1))/a
        c = 1.0-1.0/a
        integral = (quad(lambda u: math.log(abs(x(a,u))),0,c,epsabs=2e-10)[0] + quad(lambda u: math.log(abs(x(a,u))),c,1,epsabs=2e-10)[0]) if (a != 1) else float('nan')
        check(abs(g-integral) < 5e-8)
        check(g < 0)
    # Check published second-moment formula at z=-a.
    formula = 1+a*a/(1+a)-2*math.log(1+a)
    check(abs(moment(a, 2)-formula) < 1e-8)

for a in [2.1, 3., 4., 4.04, 5., 10., 100., 1000.]:
    p = root(a)
    check(moment(a, p-.001*p) < 1.0)
    check(abs(moment(a,p)-1.0) < 1.e-8)
    check(moment(a,p+.001*p) > 1.0)
    print('stiffness=',a,'critical p=',format(p,'.12g'))
for a in [100.,1000.,10000.]:
    p = root(a)
    ratio = p/(12.*math.log(a)/(math.pi**2*a))
    print('asymptotic a=',a,'ratio=',format(ratio,'.7g'))
    check(0.65<ratio<1.8)
# Check strict convexity numerically away from zero.
for a in [2.4, 4.0, 10.0]:
    for p in [.2,.6,1.0,2.0]:
        k1=math.log(moment(a,p-.01));k2=math.log(moment(a,p));k3=math.log(moment(a,p+.01))
        check(k1+k3 > 2*k2)
# Check exact expectation of finite independent products via a tensor grid quadrature.
for a in [.4, 4., 10.]:
    for p in [.5, 1.,2.]:
        one = moment(a,p)
        check(abs(one**4 - (one*one)**2)<1e-11)
print('PASS:',count,'deterministic numerical assertions')
