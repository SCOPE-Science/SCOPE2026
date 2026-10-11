#!/usr/bin/env python3
"""Finite exact and numerical consistency tests for the facet-angle theorem.

The universal proof is analytic; this script is not a substitute for it.
No external packages required.
"""
from fractions import Fraction
from math import acos, cos, factorial, pi, sin, sqrt


def legendre(n):
    p0, p1 = [Fraction(1)], [Fraction(0), Fraction(1)]
    if n == 0:
        return p0
    for j in range(1, n):
        shifted = [Fraction(0)] + [(2*j+1)*a for a in p1]
        prev = [j*a for a in p0] + [Fraction(0)]*(len(shifted)-len(p0))
        new = [(a-b)/Fraction(j+1) for a,b in zip(shifted,prev)]
        p0,p1=p1,new
    return p1


def eigen_integral(k):
    return sum(a/Fraction(i+2) for i,a in enumerate(legendre(2*k)))


def closed_integral(k):
    if k == 0:
        return Fraction(1,2)
    return Fraction(((-1)**(k+1))*factorial(2*k-2),
                    4**k*factorial(k-1)*factorial(k+1))


for k in range(13):
    assert eigen_integral(k) == closed_integral(k), ('cosine eigenvalue', k)


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def normalize(v):
    r=sqrt(dot(v,v))
    return tuple(x/r for x in v)


def check_config(normals, sep, steps=90):
    m=len(normals)
    lower=sin(sep/2)**(2*(m-1))
    for k in range(steps):
        phi=2*pi*(k+0.314159265358979)/steps
        for j in range(1,steps):
            z=-1+2*j/steps
            r=sqrt(1-z*z)
            u=(r*cos(phi),r*sin(phi),z)
            factors=[max(0.0,1-dot(u,v)**2) for v in normals]
            rho2=min(factors)
            prod=1.0
            for f in factors:
                prod*=f
            assert prod+2e-14>=rho2*lower, ('angular product',j,k)


axes=[(1,0,0),(0,1,0),(0,0,1)]
check_config(axes,pi/2)
quad=[normalize(v) for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
check_config(quad,acos(Fraction(1,3)))

v=(1.0,0.0,0.0)
t=(0.0,1.0,0.0)
for k in range(1,60):
    th=0.001*k
    cp,sp=cos(th),sin(th)
    wm=(cp,-sp,0.0)
    wp=(cp,sp,0.0)
    for j in range(1,500):
        u=normalize((cos(j*0.39),sin(j*0.97),cos(j*0.73)))
        new=(abs(dot(u,wp))+abs(dot(u,wm)))/cp
        old=2*abs(dot(u,v))
        assert new+1e-13>=old, ('split-projection',k,j)
    delta=1/cp-1
    angular_mass=2*sp*sp/cp
    assert abs(angular_mass/delta-2*(1+cp))<1e-8

print('VERIFY_OK: 13 exact Legendre moments, two spherical-grid tests, 29,441 split-projection checks')
