"""Reproduce finite numerical checks for the three-site Poisson establishment allocation theorem.

The theorem is analytic; these checks exercise its probability formula, stationary condition,
and global optimality over a deterministic finite sample, not an exhaustive continuum proof.
"""
import math
import random

COUNT = 0

def test(cond, message):
    global COUNT
    COUNT += 1
    if not cond:
        raise AssertionError(message)

def success(x1,x2,x3,a,b):
    p1=-math.expm1(-a*x1)
    p2=-math.expm1(-a*x2)
    p3=-math.expm1(-b*x3)
    return p1*p2 + p3*(p1+p2-2*p1*p2)

def optimum(B,h):
    assert B>0 and 0<h<=1
    if h<=0.5:
        return 0.0
    lo,hi=0.0,B
    for _ in range(120):
        z=(lo+hi)/2
        # Stable logarithmic form of (exp(h*z)-1)/(exp((B-z)/2)-1).
        lhs=math.expm1(h*z)
        rhs=(2*h-1)*math.expm1((B-z)/2)
        if lhs<rhs: lo=z
        else: hi=z
    return (lo+hi)/2

def value(z,B,h):
    u=math.exp(-(B-z)/2)
    v=math.exp(-h*z)
    return 1-u*u-2*u*(1-u)*v

rng=random.Random(73421)
for h in [0.01,0.1,0.4,0.499999,0.5,0.500001,0.51,0.6,0.75,0.9,1.0]:
    for B in [0.005,0.1,0.5,1.0,3.0,5.0,15.0,30.0]:
        z=optimum(B,h)
        test(0<=z<=B,'bounded allocation')
        test((z==0)==(h<=0.5),'sharp threshold')
        if h==1:
            test(abs(z-B/3)<1e-10,'identical efficiency')
        if h>0.5:
            left=math.expm1(h*z)
            right=(2*h-1)*math.expm1((B-z)/2)
            test(abs(left-right)<1e-8*(1+left+right),'stationary root')
        best=value(z,B,h)
        test(abs(best-success((B-z)/2,(B-z)/2,z,1,h))<5e-13,'formula equivalence')
        for j in range(101):
            zz=B*j/100
            test(value(zz,B,h)<=best+5e-13,'global one-dimensional grid')
        for j in range(80):
            u=rng.random();v=rng.random()
            # Random simplex via triangle folding.
            if u+v>1: u,v=1-u,1-v
            x1,x2,x3=B*u,B*v,B*(1-u-v)
            test(success(x1,x2,x3,1,h)<=best+5e-13,'global simplex sample')
        for j in range(30):
            zz=B*rng.random()
            first=(B-zz)*rng.random()
            mid=(B-zz)/2
            test(success(first,B-zz-first,zz,1,h)<=success(mid,mid,zz,1,h)+5e-13,'equalization')

for h in [0.51,0.6,0.75,0.95,1.0]:
    target_small=(2*h-1)/(4*h-1)
    B=1e-6
    test(abs(optimum(B,h)/B-target_small)<1e-5,'small-budget asymptotic')
    target_large=1/(2*h+1)
    B=1000.0
    # Exponential roots overflow at B=1000 for h near 1; bracket logarithmic equation.
    def f(z):
        def log_expm1(t):
            return t+math.log1p(-math.exp(-t)) if t>30 else math.log(math.expm1(t))
        return log_expm1(h*z)-log_expm1((B-z)/2)-math.log(2*h-1)
    lo,hi=1e-9,B-1e-9
    for _ in range(100):
        z=(lo+hi)/2
        if f(z)<0:lo=z
        else:hi=z
    root=(lo+hi)/2
    test(abs(root/B-target_large)<0.005,'large-budget asymptotic')

print('VERIFY_OK assertions=',COUNT)
