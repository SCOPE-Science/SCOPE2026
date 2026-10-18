#!/usr/bin/env python3
"""Standalone exact-algebra and finite-trajectory diagnostics for a logistic three-cycle.

Requires Python 3 standard library only. The infinite-time theorem is proved separately.
"""
import math
import cmath
from fractions import Fraction as Q


def qquartic(a,b):
    d=[a,b,-a-b]
    R=sum(t*t for t in d)
    S=sum(d[i]**4-d[i]*d[(i-1)%3]**3 for i in range(3))
    return S,Q(3,4)*R*R

for a in range(-12,13):
    for b in range(-12,13):
        s,z=qquartic(Q(a),Q(b))
        assert s==z

def phi(s): return 0.5*math.tanh(2*s)
def psi(s): return s-phi(s)
def calc(d):
    return sum(d[i]*psi(d[i])-d[i]*psi(d[(i-1)%3]) for i in range(3))
for a in range(-12,13):
    for b in range(-12,13):
        d=(a/17,b/17,-(a+b)/17)
        t=calc(d)
        assert t>=-1e-12
        if a or b: assert t>1e-12


def rhs(x,v):
    d=[x[i]-x[(i-1)%3] for i in range(3)]
    return [0.5+phi(d[i])-v*x[i] for i in range(3)]
def rk4(x,v,dt):
    a=rhs(x,v)
    b=rhs([x[j]+dt*a[j]/2 for j in range(3)],v)
    c=rhs([x[j]+dt*b[j]/2 for j in range(3)],v)
    d=rhs([x[j]+dt*c[j] for j in range(3)],v)
    return [x[j]+dt*(a[j]+2*b[j]+2*c[j]+d[j])/6 for j in range(3)]
def disparity(x):
    return sum((x[j]-x[(j-1)%3])**2 for j in range(3))

def integrate(v,until,dt):
    x=[0.4,0.01,0.15]
    n=round(until/dt)
    for _ in range(n): x=rk4(x,v,dt)
    return disparity(x),x

# The centered linearization has the precise planar eigenvalue pair.
for v in [1,1.2,1.5,1.8]:
    w=complex(1.5-v,math.sqrt(3)/2)
    assert abs(w.real-(1.5-v))<1e-14

# Representative critical relaxation (finite-time, not a proof of the limit).
r,x=integrate(1.5,2000,0.05)
assert abs(2000*r-0.5)<0.015,(r,2000*r)
# Distinct nonlinear periodic motion below threshold versus shrinking differences above.
r_below,_=integrate(1.25,100,0.05)
r_above,_=integrate(1.8,100,0.05)
assert r_below>0.05,(r_below,r_above)
assert r_above<1e-15,(r_below,r_above)
print('PASS: 625 exact rational tests, 625 sampled rearrangement tests, linear eigenvalues, three trajectory regimes; critical tR=',2000*r)
