#!/usr/bin/env python3
"""Standalone numerical checks for a two-point inverse-power shot-noise limit.

Run with python verify_two_pole.py. Requires scipy.
No finite check is used as a substitute for an asymptotic proof.
"""
import math
from scipy.integrate import quad
from scipy.special import gamma

CHECKS = 0

def check(cond, label):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(label)

def f(x, z, beta):
    if abs(x) < 1e-200:
        return 1.0
    return -math.expm1(-z / abs(x)**beta)

def J(delta, s, t, beta):
    def g(x):
        return f(x, s, beta)*f(x-delta, t, beta)
    # Split at both singular centers even though integrand extends smoothly.
    cuts = sorted(set([0.0, delta]))
    limits = [-math.inf]+cuts+[math.inf]
    return sum(quad(g, lo, hi, epsabs=2e-11, epsrel=2e-11,
                    limit=300)[0] for lo,hi in zip(limits[:-1],limits[1:]))

def finite_L(n, delta, s, t, beta):
    def g(x):
        d0 = abs(x)
        dd = abs(x-delta)
        dd = min(dd,n-dd)
        a = float('inf') if d0==0 else s/d0**beta
        b = float('inf') if dd==0 else t/dd**beta
        return -math.expm1(-a-b)
    cuts=sorted(set([-n/2,0,delta-n/2,delta,n/2]))
    return sum(quad(g,lo,hi,epsabs=1e-10,epsrel=1e-10,
                    limit=300)[0] for lo,hi in zip(cuts[:-1],cuts[1:]))

def finite_L_density(n, delta, s, t, beta, eta):
    g0 = 1.0 + eta
    L = n*g0
    def g(x):
        d0 = abs(x)
        dd = min(abs(x-delta),L-abs(x-delta))
        a = float('inf') if d0==0 else s/d0**beta
        b = float('inf') if dd==0 else t/dd**beta
        multiplier=(1+eta*math.cos(2*math.pi*x/L))/g0
        return multiplier*(-math.expm1(-a-b))
    cuts=sorted(set([-L/2,0,delta-L/2,delta,L/2]))
    return sum(quad(g,lo,hi,epsabs=1e-10,epsrel=1e-10,
                    limit=300)[0] for lo,hi in zip(cuts[:-1],cuts[1:]))

for beta in (1.5,2.0,3.0):
    alpha=1/beta
    C=2*gamma(1-alpha)
    for s,t in ((0.7,1.4),(1.0,1.0),(2.0,0.3)):
        vals=[J(d,s,t,beta) for d in (0,0.01,0.03,0.1,0.5,1,2,5,10,20,50,100)]
        check(abs(vals[0]-C*(s**alpha+t**alpha-(s+t)**alpha))<2e-8,
              'zero separation exact coefficient')
        for v,w in zip(vals[:-1], vals[1:]):
            check(v>w, 'strict separation ordering')
        A=beta*s*t*gamma(2+alpha)/(s+t)**(2+alpha)
        check(abs((vals[0]-vals[1])/0.01**2/A-1)<0.001,
              'local quadratic coefficient')
        asym=C*(t*s**alpha+s*t**alpha)
        check(abs(vals[-1]*100**beta/asym-1)<0.15,
              'far-field power-law coefficient')
        for c in (0.3,1.7,3.0):
            lhs=J(1.2,c*s,c*t,beta)
            rhs=c**alpha*J(1.2*c**(-alpha),s,t,beta)
            check(abs(lhs-rhs)<1e-8*max(1.0,lhs,rhs),'scaling identity')
    s,t=0.7,1.4
    target=C*(s**alpha+t**alpha)-J(1,s,t,beta)
    errors=[]
    for n in (40,80,160,320):
        L=finite_L(n,1,s,t,beta)
        errors.append(abs(L-target))
        check(abs(L-target)<2.0,'finite circle Laplace exponent bounded')
    check(errors[-1]<errors[0],'finite circle convergence')

for eta in (-0.4,0.2,0.6):
    beta=2.0; s,t=.7,1.4; delta=1.0;alpha=.5
    C=2*gamma(1-alpha)
    target=C*(s**alpha+t**alpha)-J(delta,s,t,beta)
    errors=[]
    for n in (50,100,200,400):
        err=abs(finite_L_density(n,delta,s,t,beta,eta)-target)
        errors.append(err)
        check(err<0.5, 'continuous nonuniform density error')
    check(errors[-1]<errors[0], 'density universality convergence')

print('PASS',CHECKS,'numeric assertions; analytic infinite-n statements require proof')
