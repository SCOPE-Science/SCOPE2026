#!/usr/bin/env python3
"""Independent checks for the geometry and algebra of cylinder shadow-area moments.
Run: python3 verify.py   (Python 3 standard library only.)
"""
from fractions import Fraction as F
from math import pi, sin, cos, sqrt
from random import Random

LOW, HIGH = F(157, 50), F(22, 7)
assert LOW < pi < HIGH

def quartic(x):
    return x**4 - 6*x**3 + 4*x*x + 36*x - 64

def derivative(x):
    return 4*x**3 - 18*x*x + 8*x + 36

# The derivative lower bound is valid everywhere on [LOW,HIGH],
# using coordinate-wise monotonicity of powers on nonnegative inputs.
dmin = 4*LOW**3 - 18*HIGH**2 + 8*LOW + 36
assert dmin > 0 and quartic(HIGH) < 0
assert HIGH**2 < 12 and LOW**2 > 8 and HIGH < 4
assert derivative(LOW) > 0


def moments(r, h):
    return (pi*r*(r+h)/2,
            (pi*pi*r**4 + 4*pi*r**3*h + 8*r*r*h*h)/3,
            (pi**3*r**6/4 + 3*pi**3*r**5*h/8
             + 3*pi*r**4*h*h + 3*pi*r**3*h**3/2))

def integrate_moment(r,h,k,N=2048):
    # x=cos(theta); dx=sin(theta) dtheta, theta in [0,pi/2]
    def f(theta):
        return (pi*r*r*cos(theta) + 2*r*h*sin(theta))**k*sin(theta)
    step=pi/(2*N)
    return step/3*(f(0)+f(pi/2)+4*sum(f(i*step) for i in range(1,N,2))
                   +2*sum(f(i*step) for i in range(2,N,2)))

for r,h in [(0.2,0.8), (0.5,1), (1,0.3), (1,1), (1,4), (1.3,0.7), (2,13)]:
    expected=moments(r,h)
    for k,e in enumerate(expected,1):
        val=integrate_moment(r,h,k)
        assert abs(val-e) < 3e-9*max(1,abs(e)),(r,h,k,val,e)

S=2*pi*(pi-2)/(pi*pi-4*pi+8)
y0=S/2
assert 0 < S-1 < y0 < 1

def h2(y):
    return 4/(3*pi*pi)*(pi*pi*(1-y)**2 + 4*pi*y*(1-y) + 8*y*y)

def h3(y):
    return 2-3*y+24*y*y/(pi*pi)+(1-12/(pi*pi))*y**3

def D_max():
    p=pi
    a=p*p-4*p+8
    return 12*quartic(p)/(p*a*a)
assert D_max() < 0
for y in [(S-1)+0.02, .48, .5, .6, y0-.01]:
    z=S-y
    assert 0<y<z<1
    assert abs(h2(y)-h2(z))<1e-13
    # The third moment strictly orders equal-second-moment branches.
    assert h3(y)>h3(z)
    assert (h3(y)-h3(z))/(y-z) < 0

# Concrete exact collision family: y=1/2 vs its reflected counterpart.
y1=0.5
y2=S-y1
t1=y1/(1-y1)
t2=y2/(1-y2)
r1=1
r2=sqrt((1+t1)/(1+t2))
h1=t1*r1
h2c=t2*r2
ma=moments(r1,h1)
mb=moments(r2,h2c)
assert abs(ma[0]-mb[0])<1e-12 and abs(ma[1]-mb[1])<1e-12
assert abs(ma[2]-mb[2])>1e-5

# Independent planar convex-hull construction of random-angle cylinder shadows:
# these are projected vertices of top and bottom circles, not the Minkowski area formula.
def hull_area(pts):
    pts=sorted(set(pts))
    def cross(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lower=[]
    for pt in pts:
        while len(lower)>=2 and cross(lower[-2],lower[-1],pt)<=0:lower.pop()
        lower.append(pt)
    upper=[]
    for pt in reversed(pts):
        while len(upper)>=2 and cross(upper[-2],upper[-1],pt)<=0:upper.pop()
        upper.append(pt)
    hull=lower[:-1]+upper[:-1]
    return abs(sum(p[0]*q[1]-q[0]*p[1]
                   for p,q in zip(hull,hull[1:]+hull[:1])))/2

rng=Random(20261025)
checks=0
N=384
for _ in range(48):
    r=0.2+3*rng.random()
    h=0.1+5*rng.random()
    theta=(pi/2)*rng.random()
    ct,st=cos(theta),sin(theta)
    pts=[]
    for j in range(N):
        phi=2*pi*j/N
        for side in (-1,1):
            pts.append((r*cos(phi)*ct - side*h*st/2,r*sin(phi)))
    polygon=hull_area(pts)
    theory=pi*r*r*ct+2*r*h*st
    assert abs(polygon-theory) < 2e-4*max(1,theory),(polygon,theory)
    checks+=1

print('PASS: exact rational pi-interval and quartic sign, normalized-moment collision and strict third-moment separation,')
print('      21 smooth integral cross-checks, and',checks,'independent polygonal projected-hull cross-checks.')
print('t_critical=',(S-1)/(2-S),' t_vertex=',y0/(1-y0),' t_pair=',t2)
print('third-moment gap for unit-radius t=1 pair=',ma[2]-mb[2])
