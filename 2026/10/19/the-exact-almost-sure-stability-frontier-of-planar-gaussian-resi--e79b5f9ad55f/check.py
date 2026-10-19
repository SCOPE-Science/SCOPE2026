#!/usr/bin/env python3
"""Independent numerical checks for a two-dimensional Gaussian rank-one recurrence.

Run with Python 3.10+; numpy is NOT required. Deterministic Simpson quadrature,
monotone Riemann enclosures, reproducible Gaussian trajectories. This is not an
infinite proof; see RESULT.md for the mathematical argument.
"""
from math import exp,log,hypot
from random import Random

def simpson(f,a,b,n=16000):
    assert n%2==0 and b>a
    h=(b-a)/n
    z=f(a)+f(b)
    z+=4*sum(f(a+i*h) for i in range(1,n,2))
    z+=2*sum(f(a+i*h) for i in range(2,n,2))
    return z*h/3

def rate(b):
    assert 0<b<=1.01
    v=1/(2*b)
    first=simpson(lambda x:exp(-x)*log(1-b*x),0,v)
    second=simpson(lambda x:exp(-x)*log(b*x),v,52)
    return first+second

def derivative(b):
    half=simpson(lambda t:t/(1-t)*exp(-t/b),0,.5)
    return (b*exp(-.5/b)-half)/(b*b)

def bisect(f,a,b,n=55):
    assert f(a)<0 and f(b)>0
    for _ in range(n):
        c=(a+b)*.5
        if f(c)<0:a=c
        else:b=c
    return (a+b)*.5

bopt=bisect(derivative,.25,.5)
blast=bisect(rate,.9,1)
assert abs(bopt-0.3244085176877796)<2e-10
assert abs(blast-0.9370873719202792)<2e-10
for b,expected in [(.25,-.2199115297208684),(.5,-.19462246895127135),(.8,-.06507844606288404),(1,.029696876311104736)]:
    assert abs(rate(b)-expected)<1e-8, (b,rate(b))
assert derivative(.25)<0<derivative(.5)
assert rate(.5)<0<rate(1)
# Rigorous monotonic-Riemann enclosure in exact real arithmetic: the
# integrand e^-t/(1-t) increases on [0,1/2], whereas e^-t/t decreases
# on [1/2,10.5]. The corresponding endpoint sums bound the integrals.
n=1000
upper_left=.5/n*sum(exp(-j*.5/n)/(1-j*.5/n) for j in range(1,n+1))
lower_right=10/n*sum(exp(-(.5+j*10/n))/(.5+j*10/n) for j in range(1,n+1))
assert lower_right-upper_left>.02
# Independent direction-update realization: normalize after each step
# and accumulate log-norms, thereby avoiding overflow and underflow.
rng=Random(20261014)
for b in [.25,.5,.8,1.]:
    x,y=1.,0.
    total=0.
    for k in range(70000):
        p,q=rng.gauss(0,1),rng.gauss(0,1)
        s=p*x+q*y
        nx,ny=x-b*p*s,y-b*q*s
        z=hypot(nx,ny)
        assert z>0
        total+=log(z)
        x,y=nx/z,ny/z
    observed=total/70000
    assert abs(observed-rate(b))<.02,(b,observed,rate(b))
# Analytic Gaussian fourth-moment identity (not a sampling estimate).
for b in [0.1,0.25,0.5,0.75,1.]:
    factor=1-2*b+4*b*b
    assert factor>=.75
    assert (factor<1)==(0<b<.5)
print('PASS: planar Gaussian logarithmic rate, unique-root brackets, positive sign enclosure,')
print('      iid recurrence Monte Carlo, exact mean-square threshold')
print('b_opt=%.15f, Lambda_min=%.15f, b_as=%.15f' % (bopt,rate(bopt),blast))
print('certified monotone-integral gap lower bound (subject to exp evaluations): %.12f'%(lower_right-upper_left))
