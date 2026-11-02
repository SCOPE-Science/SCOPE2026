#!/usr/bin/env python3
"""Independent numerical diagnostics for symmetric planar lens Mahler formulas.

Proof of the universal claims is analytic in RESULT.md. This script checks
polar integration, scaling limits, and inequalities at deterministic inputs.
No external packages are required.
"""
from math import acos, asin, cos, pi, sin, sqrt

def simpson(f, lo, hi, n=4000):
    assert n % 2 == 0
    h = (hi - lo)/n
    s = f(lo) + f(hi)
    for k in range(1, n):
        s += (4 if k % 2 else 2)*f(lo + k*h)
    return s*h/3

def area_lens(a):
    b = sqrt(1-a*a)
    return 2*(acos(a)-a*b)

def area_polar(a):
    return (pi+4*a)/(1-a*a)**1.5

def direct_area(a):
    return 8*(1-a)**1.5*simpson(lambda u:u*u*sqrt(2-(1-a)*u*u),0.,1.)

def h_lens(a,theta):
    b=sqrt(1-a*a)
    t=abs(cos(theta))
    return 1-a*t if t>=a else b*abs(sin(theta))

def direct_polar(a):
    b=sqrt(1-a*a)
    th=acos(a)
    return 2*(simpson(lambda t:1/(1-a*cos(t))**2,0,th)
              + simpson(lambda t:1/(b*b*sin(t)**2),th,pi/2))

def product(a):
    return area_lens(a)*area_polar(a)

def derivative_numerator(a):
    b=sqrt(1-a*a)
    n=acos(a)-a*b
    return (4+8*a*a+3*pi*a)*n-2*(pi+4*a)*b**3

checks=0
for a in (0., .02, .12, .25, .4, .5, .63, .8, .9, .96):
    A=area_lens(a)
    B=area_polar(a)
    assert abs(A-direct_area(a)) < max(1e-8,1e-8*A), (a,A,direct_area(a))
    checks+=1
    assert abs(B-direct_polar(a)) < max(1e-7,1e-8*B), (a,B,direct_polar(a))
    checks+=1
    th=acos(a)
    if a<1:
        assert abs(h_lens(a,th)-(1-a*a))<1e-13
        checks+=1
    if 0<a<1:
        assert derivative_numerator(a)<0, (a,derivative_numerator(a))
        checks+=1
for k in range(1,1000):
    a=k/1000
    assert derivative_numerator(a)<0
    checks+=1
for k in range(1,1000):
    a=k/1000
    assert product(a) < product(a-1/1000)
    checks+=1
for a in (.02,.04,.08):
    asym=pi*pi+(1.5*pi*pi-16)*a*a
    assert abs(product(a)-asym) < 0.25*a*a
    checks+=1
# Affine parabolic-lens limit: verify values at modest separations.
limit=4*(pi+4)/3
for a in (.95,.98,.99,.999):
    assert product(a) > limit
    checks+=1
assert product(0)==pi*pi
checks+=1
print(f"PASS: {checks} deterministic geometric/numerical assertions; analytic proof required for all parameters.")
print('ball endpoint:', pi*pi, 'parabolic-lens endpoint:',limit)
