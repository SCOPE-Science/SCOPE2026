#!/usr/bin/env python3
"""Numerical checks for sharp antithetic nested-MLMC correction laws.

Requires Python >=3.9 standard library only. No network, external source or data.
"""
import math
import random

PI = math.pi
CHECKS = 0

def near(a, b, rtol=1e-8, atol=1e-12):
    global CHECKS
    CHECKS += 1
    if not math.isclose(a, b, rel_tol=rtol, abs_tol=atol):
        raise AssertionError(f'check {CHECKS}: {a!r} != {b!r}')

def gap(y, a, b):
    pos = lambda x: max(x, 0.0)
    return (pos(y+a)+pos(y+b))/2 - pos(y+(a+b)/2)

def normal_abs_moment(k):
    return 2.0**(k/2)*math.gamma((k+1)/2)/math.sqrt(PI)

def angular_moment(tau, sigma, n, r, panels=8000):
    t = sigma*sigma/n
    w = tau*tau+t
    theta = math.atan(math.sqrt(t/w))
    h = theta/panels
    s = 0.0
    for j in range(panels):
        ang=(j+0.5)*h
        v=math.sqrt(t)*math.cos(ang)-math.sqrt(w)*math.sin(ang)
        s += max(0.0, v)**r
    return 2.0**(1-r/2)*math.gamma(1+r/2)/PI*s*h

def finite_gaussian(tau, sigma, n):
    t=sigma*sigma/n
    w=tau*tau+t
    v=tau*tau+2*t
    theta=math.atan(math.sqrt(t/w))
    p=2*theta/PI
    mean=(math.sqrt(v)-math.sqrt(w))/math.sqrt(2*PI)
    second=(v*theta-math.sqrt(t*w))/(2*PI)
    return p,mean,second

def asymptotic_constant(fzero,sigma,r):
    return fzero*sigma**(r+1)*2**(1-r)*normal_abs_moment(r+1)/(r+1)

rng=random.Random(20261030)
# Exact triangle and integrated powers for arbitrary real offsets.
for _ in range(42):
    a=rng.uniform(-3,3)
    b=rng.uniform(-3,3)
    if abs(a-b)<0.05:
        b+=0.2
    c=(a+b)/2
    d=abs(a-b)
    for frac in (-0.6,-0.5,-0.4,-0.2,0,0.2,0.4,0.5,0.6):
        y=-c+frac*d
        near(gap(y,a,b),max(d/4-abs(y+c)/2,0),rtol=1e-9,atol=1e-13)
    for r in (1,2,3,4):
        # midpoint integration of a degree-r piecewise polynomial
        pieces=6000
        width=d/pieces
        approx=0.0
        for k in range(pieces):
            y=-c-d/2+(k+0.5)*width
            approx += max(d/4-abs(y+c)/2,0)**r
        approx *= width
        exact = d**(r+1)/(4**r*(r+1))
        near(approx,exact,rtol=2.0e-7)

# Gaussian exact formulas compared against a separate angular integration.
for tau,sigma,n in ((1,1,2),(1,1,4),(1,1,32),(0.7,1.6,128),(2,0.3,6),(5,3,128),(0.3,0.9,18)):
    p,mean,second=finite_gaussian(tau,sigma,n)
    near(p,angular_moment(tau,sigma,n,0),rtol=5e-9)
    near(mean,angular_moment(tau,sigma,n,1),rtol=5e-8)
    near(second,angular_moment(tau,sigma,n,2),rtol=5e-8)
    assert 0<p<0.5 and mean>0 and second>mean*mean

# Sharp universal constants in exactly soluble Gaussian subfamily.
for tau,sigma in ((1,1),(2,0.5),(0.75,1.6)):
    fzero=1/(math.sqrt(2*PI)*tau)
    n=1000000
    for r in (0,1,2,3,4,5):
        empirical=angular_moment(tau,sigma,n,r)
        limit=asymptotic_constant(fzero,sigma,r)
        near(empirical*n**((r+1)/2),limit,rtol=0.02)

# Sharp kurtosis normalisation and empty-pilot crossover.
for tau,sigma in ((1.0,1.0),(2.0,0.5)):
    n=1000000
    moments=[angular_moment(tau,sigma,n,r) for r in (1,2,3,4)]
    mu,m2,m3,m4=moments
    var=m2-mu*mu
    central4=m4-4*mu*m3+6*mu*mu*m2-3*mu**4
    kurt=central4/var**2
    predicted=9*PI*tau/(5*sigma)
    near(kurt/math.sqrt(n),predicted,rtol=0.04)
    pn=finite_gaussian(tau,sigma,n)[0]
    for c in (0.1,0.5,2.0):
        M=round(c*math.sqrt(n))
        no_event=(1-pn)**M
        asymp=math.exp(-c*2*sigma/(PI*tau))
        near(no_event,asymp,rtol=0.006)

print(f'PASS {CHECKS} deterministic identity, angular-integral, moment, kurtosis and rare-event comparisons')
