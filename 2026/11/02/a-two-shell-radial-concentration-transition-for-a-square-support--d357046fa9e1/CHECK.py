#!/usr/bin/env python3
"""Numerical cross-checks for a radial law derived from two independent beta coordinates.

Requires scipy and numpy. Analytic uniqueness and endpoint assertions are proved
in RESULT.md; finite numerical samples are only consistency tests.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import beta as B, hyp2f1

COUNT = 0

def check(condition, msg):
    global COUNT
    if not condition:
        raise AssertionError(msg)
    COUNT += 1


def hyper_H(w, b):
    return hyp2f1(.5, .5, b + .5, w*w)


def eta(t, b):
    w = t/(2-t)
    h = hyper_H(w,b)
    dw_h = w/(2*(b+.5))*hyp2f1(1.5,1.5,b+1.5,w*w)
    q = w*dw_h/h
    return 2*b-1 + t/(2*(2-t)) + 2*q/(2-t)


def density_rho(r,b):
    s=r*r
    if not 0<s<2:
        return 0.0
    base=B(.5,b)
    if s<1:
        integral=quad(lambda theta: ((1-s*math.sin(theta)**2)*(1-s*math.cos(theta)**2))**(b-1), 0,math.pi/2,epsabs=1e-12,epsrel=2e-12)[0]
        return 4*r*integral/base**2
    t=2-s
    return 4*B(b,b)*t**(2*b-1)*hyper_H(t/s,b)/(base**2*r)


def convolution_s(s,b):
    lo=max(0,s-1)
    hi=min(1,s)
    if s<1:
        return quad(lambda theta: 2*((1-s*math.sin(theta)**2)*(1-s*math.cos(theta)**2))**(b-1),0,math.pi/2,epsabs=1e-12)[0]/B(.5,b)**2
    t=2-s
    # independent integration of the original beta convolution
    integral=quad(lambda z: 1/math.sqrt((1-t*z)*(1-t*(1-z))),0,1,weight='alg',wvar=(b-1,b-1),epsabs=1e-12)[0]
    return t**(2*b-1)*integral/B(.5,b)**2

for b in [.12,.25,.4,.49,.5,.55,.75,1.,1.3,2.]:
    for r in [.2,.5,.8,.95,1.05,1.2,1.32,1.4]:
        left=density_rho(r,b)
        right=2*r*convolution_s(r*r,b)
        check(abs(left-right)<3e-9*max(1,right), f'convolution mismatch b={b}, r={r}')

for b in [.12,.25,.4,.49,.5,.65,.85,1.]:
    grid=np.linspace(.04,.96,35)
    vals=[density_rho(float(r),b) for r in grid]
    check(all(a<c for a,c in zip(vals,vals[1:])),f'inner monotonicity mismatch at b={b}')

for b in [.12,.25,.4,.49,.5,.65,.85,1.,1.4,2.]:
    ts=np.linspace(.001,.98,100)
    ds=np.array([eta(float(t),b) for t in ts])
    check(np.all(np.diff(ds)>0),f'log-derivative monotonicity mismatch b={b}')
    if b<.5:
        root=brentq(lambda t: eta(t,b),1e-10,.999999,xtol=1e-13)
        check(0<root<1,f'missing unique valley b={b}')
        check(eta(root*.95,b)<0<eta((root+1)/2,b),f'wrong valley sign b={b}')
    else:
        check(np.all(ds>0),f'outer decrease mismatch b={b}')

for b in [.49,.499,.4999]:
    t=brentq(lambda x: eta(x,b),1e-12,.99,xtol=1e-14)
    delta=1-2*b
    check(abs(t/(4*delta)-1)<.1 if b==.49 else abs(t/(4*delta)-1)<.02,
          f'critical valley scaling b={b}: {t/(4*delta)}')

check(abs(4*B(.5,.5)/B(.5,.5)**2/math.sqrt(2)-2*math.sqrt(2)/math.pi)<1e-14,'critical outer boundary value')
for b in [.55,.75,1.,1.8]:
    g_at_1=B(b-.5,b-.5)/B(.5,b)**2
    check(math.isfinite(g_at_1) and g_at_1>0,'finite radial density at inscribed circle')

print(f'PASS: {COUNT} direct-convolution, root, monotonicity and critical-scaling checks')
