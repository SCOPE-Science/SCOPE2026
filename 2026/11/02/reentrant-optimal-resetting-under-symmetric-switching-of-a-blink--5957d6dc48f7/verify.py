#!/usr/bin/env python3
"""Finite numerical consistency checks for a Brownian gated-target optimum theorem.

The global statements are analytical. This script checks source-formula
specialization, independent derivatives, and asymptotic predictions.
Python 3 standard library only.
"""
from math import exp, sqrt, isclose
from random import Random

checks = 0

def check(test, label):
    global checks
    checks += 1
    if not test:
        raise AssertionError(label)


def objective(x,h):
    assert x>0 and h>0
    s=sqrt(x*x+2*h)
    t=x/s
    return ((1+t)*exp(x)-1)/(x*x) + t*exp(x-s)/(2*h)


def source_formula(x,h):
    """Dimensionless specialization of Mercado-Vasquez--Boyer (2021), Eq. 26."""
    s=sqrt(x*x+2*h)
    return (exp(x)-1)/x**2 + exp(x)*(2*h + x*x*exp(-s))/(2*h*x*s)


def derivative(x,h):
    s=sqrt(x*x+2*h)
    b=(exp(x)*(x-2)+2)/x**3
    c1=exp(x)/(x*s)
    c2=x*exp(x-s)/(2*h*s)
    return b + c1*(1-1/x-x/s**2) + c2*(1-x/s+1/x-x/s**2)


def H(x):
    return (2*exp(x)-1.5)/x**2 - 1/(2*x)


def J(x):
    return (x*x+3*x+3-4*exp(x))/(4*x**4)


def N(x):
    return 2*exp(x)*(x-2)+3+x/2


def P(x):
    return exp(x)*(x-2)+2


def root(f,a,b):
    fa=f(a)
    fb=f(b)
    assert fa*fb<0
    for _ in range(160):
        c=(a+b)/2
        if f(c)*fa<=0:
            b=c
        else:
            a=c
            fa=f(c)
    return (a+b)/2


xslow=root(N,1.5,2)
xfast=root(P,1,2)
check(1.62446<xslow<1.62447,'rare-gate root bracket')
check(1.59362<xfast<1.59363,'fast-gate root bracket')
check(xslow>xfast,'rare-gate optimum exceeds always-active optimum')

Ns_prime=2*exp(xslow)*(xslow-1)+0.5
Hsecond=Ns_prime/xslow**3
Jprime=(xslow*xslow+2*xslow-4)/(2*xslow**4*(2-xslow))
dslow=Jprime/Hsecond
check(0.225<dslow<0.228,'positive slow-gate displacement coefficient')

rng=Random(20261025)
for _ in range(400):
    x=exp(rng.uniform(-1.3,1.4))
    h=exp(rng.uniform(-7,6))
    a=objective(x,h)
    b=source_formula(x,h)
    check(isclose(a,b,rel_tol=2e-13,abs_tol=4e-12),'source equation comparison')
    check(a >= (exp(x)-1)/x**2,'objective above permanently active')
    # Uniform endpoint control used in the proof.
    check(a-1/(2*h) >= 1/x-1e-8,'uniform small-x lower bound')

for h in [0.001,0.02,0.2,1,10,100]:
    for x in [0.45,0.8,1.2,1.5,2.0,3.1]:
        step=1e-5
        numerical=(objective(x+step,h)-objective(x-step,h))/(2*step)
        check(isclose(numerical,derivative(x,h),rel_tol=3e-6,abs_tol=1e-5),'derivative check')

for h in [0.001,0.002,0.005]:
    for x in [1.2,1.6,1.9,2.5]:
        diff=objective(x,h)-1/(2*h)-H(x)-h*J(x)
        check(abs(diff)<4*h*h,'compact rare-gate expansion')

for h in [1000,10000,50000]:
    for x in [1.1,1.6,2.5]:
        approx=(exp(x)-1)/x**2+exp(x)/(x*sqrt(2*h))
        check(abs(objective(x,h)-approx)<30/h**1.5,'compact fast-gate expansion')

values=[]
for h in [0.001,0.01,0.1,0.5,1,2,5,10,100,1000,10000]:
    x=root(lambda z: derivative(z,h),0.5,3)
    values.append((h,x))
    step=1e-4
    check(objective(x,h)<objective(x-step,h),'local min left')
    check(objective(x,h)<objective(x+step,h),'local min right')
    for gridx in [0.1,0.2,0.5,0.9,1.2,1.5,2,3,4,6,10]:
        check(objective(x,h)<objective(gridx,h),'sampled global comparison')

for h,x in values:
    if h<=0.01:
        check(abs(x-(xslow-dslow*h))<0.8*h*h,'rare-optimum expansion')
    if h>=1000:
        check(abs(x-xfast*(1-1/sqrt(2*h)))<5/h,'fast-optimum expansion')
check(values[0][1]>xfast,'rare optimum above active benchmark')
check(next(x for h,x in values if h==5)<xfast,'intermediate minimum below benchmark')
check(values[-1][1]>next(x for h,x in values if h==5),'rebound at fast switching')
print('PASS: %d finite assertions' % checks)
print('x_slow=%.12f, x_active=%.12f, d_slow=%.12f' % (xslow,xfast,dslow))
for h,x in values:
    print('h=%g x_opt=%.10f scaled_rate=%.10f' % (h,x,x*x))
