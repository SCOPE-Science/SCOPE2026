#!/usr/bin/env python3
"""Numerical cross-checks for Gaussian-smoothed beta-law modal transition.
This is a finite diagnostic, not a replacement for the proof in RESULT.md.
Requires Python 3, NumPy and SciPy. Run: python verification.py
"""
import math
import numpy as np
from scipy.special import roots_jacobi
from scipy.optimize import brentq

COUNT=0

def check(condition, msg):
    global COUNT
    assert condition, msg
    COUNT+=1

def nodes(k, degree=360):
    x, w = roots_jacobi(degree, k - 1., -0.5)
    y = (1.+x)/2.
    return y, w/w.sum()

def moments(y, w, t, upto=5):
    v=w*np.exp(-t*y)
    v/=v.sum()
    return [float(np.dot(v,y**j)) for j in range(upto+1)]

def critical_t(y,w):
    def F(t): return 2.*t*moments(y,w,t,1)[1]-1.
    return brentq(F,0.001,100.,xtol=1e-12)

def deriv(x,th,y,w):
    t=1./th
    a=np.sqrt(y)
    return t*np.sum(w*((a-x)*np.exp(-t*(x-a)**2)+(-a-x)*np.exp(-t*(x+a)**2)))

for k in (.02,.1,.3,.6,.8,.95):
    y,w=nodes(k)
    tc=critical_t(y,w); theta_c=1/tc
    M=moments(y,w,tc,6)
    check(abs(2*tc*M[1]-1.)<1e-9, f'critical equation k={k}')
    check(abs(M[2]/M[1]**2-(1+2*k))<3e-7, f'critical kurtosis k={k}')
    for n in range(0,5):
        lhs=2*tc*(M[n+1]-M[n+2])
        rhs=(2*n+1)*M[n]-(2*n+2*k+1)*M[n+1]
        check(abs(lhs-rhs)<2e-7, f'IBP identity k={k} n={n}')
    eps=1e-4*tc
    def F(t):return 2*t*moments(y,w,t,1)[1]-1
    num=(F(tc+eps)-F(tc-eps))/(2*eps)
    check(abs(num-(1-k)/tc)<1e-5, f'critical transversality k={k}')
    # Exact normalized quartic curvature at the bifurcation.
    f4=(16*tc**4*M[2]-48*tc**3*M[1]+12*tc**2)
    check(abs(f4+8*(1-k)*tc**2)<2e-6, f'quartic coefficient k={k}')
    check(F(tc*.8)<0 and F(tc*1.2)>0, f'unique-root orientations k={k}')
    # Global derivative-sign tests: one mode above critical variance;
    # two symmetric modes below, and only one positive-side zero.
    for factor in (.75,1.,1.25):
        th=theta_c*factor
        grid=np.linspace(.006,1.6,260)
        signs=[deriv(float(x),th,y,w) for x in grid]
        flips=sum((a*b<0) for a,b in zip(signs,signs[1:]))
        check(flips == (1 if factor<1 else 0),f'modal count k={k} factor={factor}, flips={flips}')
        check(signs[-1]<0,f'far-tail monotone k={k} factor={factor}')
    for delta in (.003,.001):
        th=theta_c-delta
        peak=brentq(lambda x:deriv(x,th,y,w),.001,1.4)
        check(abs(peak/math.sqrt(delta)-math.sqrt(1.5))<.007,
              f'universal peak splitting k={k} delta={delta}: {peak/math.sqrt(delta)}')
    print(f'k={k:.3f} theta_c={theta_c:.12f}; fourth derivative ratio={f4:.9g}')

for k in (1.,1.1,1.5,2.,4.):
    y,w=nodes(k)
    for theta in (.05,.3,1.,4.):
        for x in (.04,.1,.3,.5,.8,1.,1.5):
            check(deriv(x,theta,y,w)<0,f'passive unimodality k={k} theta={theta} x={x}')

# Monotonic decline of the critical thermal-to-active ratio with tumble parameter.
crit=[]
for k in np.linspace(.05,.95,19):
    y,w=nodes(float(k)); crit.append(1/critical_t(y,w))
for a,b in zip(crit,crit[1:]): check(a>b,'strict threshold monotonicity')
print('PASS',COUNT,'deterministic checks')
