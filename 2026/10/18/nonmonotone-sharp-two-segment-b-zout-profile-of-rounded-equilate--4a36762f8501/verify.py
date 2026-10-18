#!/usr/bin/env python3
"""Reproducible supplementary checks for a planar mixed-area identity."""
import math
import random

S3 = math.sqrt(3.0)
A, B = 1.5, S3
VERTICES = ((1., 0.), (-0.5, S3 / 2), (-0.5, -S3 / 2))

def width(t):
    nx, ny = math.cos(t), math.sin(t)
    z = [nx * x + ny * y for x, y in VERTICES]
    return max(z) - min(z)

def area(r):
    return 3 * S3 / 4 + 3 * S3 * r + math.pi * r * r

def bound(r):
    return 2 * area(r) / ((A + 2*r)*(B + 2*r))

def quotient(r, u, v):
    return 2 * area(r) * abs(math.sin(v-u)) / ((width(u) + 2*r)*(width(v) + 2*r))

def poly(r):
    return (18 - 9*S3/2 + (6*S3*math.pi-12*S3)*r
           + (6*math.pi+4*S3*math.pi-24*S3)*r*r)

assert abs(width(0) - A) < 1e-14
assert abs(width(math.pi/6) - B) < 1e-14
assert abs(width(math.pi/2) - B) < 1e-14
assert abs(area(0) - 3*S3/4) < 1e-14
assert abs(bound(0)-1) < 1e-14
assert abs(2*area(1000000)/((A+2000000)*(B+2000000))-math.pi/2) < 2e-7
p0=18 - 9*S3/2
p1=6*S3*(math.pi-2)
p2=6*math.pi+4*S3*math.pi-24*S3
assert p0>0 and p1>0 and p2<0
roots=[(-p1+math.sqrt(p1*p1-4*p2*p0))/(2*p2),(-p1-math.sqrt(p1*p1-4*p2*p0))/(2*p2)]
positive=[r for r in roots if r>0]
assert len(positive)==1
rstar=positive[0]
assert abs(poly(rstar))<1e-10
assert 13.2426<rstar<13.2428
assert bound(rstar)>math.pi/2
for r in (0,0.001,0.01,0.1,1,10,rstar,20,100):
    assert abs(quotient(r,0,math.pi/2)-bound(r))<1e-12
    assert abs(quotient(r,math.pi/6,math.pi/6+math.pi/2)-bound(r))<1e-12
    h=1e-5*(1+r)
    if r>h:
        d=(bound(r+h)-bound(r-h))/(2*h)
        assert abs(d-poly(r)/((A+2*r)*(B+2*r))**2)<1e-8

# Independent sampled geometry, with all tested random radii and directions.
rng = random.Random(193871)
for r in (0,0.01,0.3,1,3,10,rstar,100):
    ub = bound(r)
    for _ in range(30000):
        u,v=rng.random()*2*math.pi,rng.random()*2*math.pi
        s=abs(math.sin(v-u)); wu,wv=width(u),width(v)
        assert wu*wv+1e-12>=A*B*s
        assert wu+wv+1e-12>=(A+B)*s
        assert quotient(r,u,v)<=ub+1e-12

# Interval samples independently check the shape of the root and asymptotics.
for r in (0.01,0.5,3,12):
    assert bound(r+1e-4)>bound(r)
for r in (15,20,40,300):
    assert bound(r+1e-4)<bound(r)
    assert bound(r)>math.pi/2

print('VERIFY_OK')
print('positive_root =',format(rstar,'.13f'))
print('maximum =',format(bound(rstar),'.13f'))
