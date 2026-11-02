#!/usr/bin/env python3
"""Independent reproducibility checks for regular-polygon Euclidean roundings.
All geometric claims in the accompanying result are established analytically.
This file supplies finite consistency checks rather than infinite certification.
Requires only Python 3's standard library.
"""
from fractions import Fraction
from math import pi, sin, cos, tan, sqrt
import math

checks = 0

def assert_close(a, b, tol=2e-8):
    global checks
    checks += 1
    assert math.isfinite(a) and math.isfinite(b)
    assert abs(a-b) <= tol * max(1.0, abs(a), abs(b)), (a,b)

def assert_true(x):
    global checks
    checks += 1
    assert x

def simpson(f, a, b, N=3000):
    assert N % 2 == 0
    h=(b-a)/N
    z=f(a)+f(b)
    for j in range(1,N):
        z+=(4 if j&1 else 2)*f(a+j*h)
    return z*h/3

def constants(n):
    alpha=pi/n
    R=1/cos(alpha)
    mu=tan(alpha)/alpha
    return alpha,R,mu

def volume_product(n,t):
    alpha,R,mu=constants(n)
    A=n*tan(alpha)*(1+2*t)+pi*t*t
    J=n*simpson(lambda th:1/(t+R*cos(th))**2,0,alpha)
    return A*J

def derivative_integral(n,t):
    alpha,R,mu=constants(n)
    a=n*tan(alpha)
    return 2*n*simpson(lambda th:(a*(R*cos(th)-1)+t*(pi*R*cos(th)-a))/(t+R*cos(th))**3,0,alpha)

def polar_area_from_vertices(n,t):
    alpha,R,mu=constants(n)
    vertices=[(R*cos(2*pi*j/n),R*sin(2*pi*j/n)) for j in range(n)]
    def integrand(th):
        x,y=cos(th),sin(th)
        h=max(vx*x+vy*y for vx,vy in vertices)+t
        return 1/h**2
    return .5*simpson(integrand,0,2*pi,24000)

# Rational algebra checks for the exact derivative identity, with no symbolic library.
for p in range(1,13):
    for q in range(1,9):
        mu=Fraction(6+p,6)
        z=Fraction(8+q,8)
        t=Fraction((p+q),7)
        N=t*t+2*mu*t+mu
        D=t+z
        lhs=(t+mu)/(D*D)-N/(D*D*D)
        rhs=(t*(z-mu)+mu*(z-1))/(D*D*D)
        assert_true(lhs==rhs)

for n in [3,4,5,6,9,17]:
    alpha,R,mu=constants(n)
    assert_close(volume_product(n,0),n*n*sin(alpha)**2)
    for t in [0.,.1,.5,2.,7.]:
        A=n*tan(alpha)*(1+2*t)+pi*t*t
        assert_close(A*polar_area_from_vertices(n,t),volume_product(n,t),5e-8)
        # Direct derivative integral versus centered finite difference.
        h=1e-5
        d=(volume_product(n,t+h)-volume_product(n,t-h)) / (2*h) if t>=h else (-3*volume_product(n,0)+4*volume_product(n,h)-volume_product(n,2*h))/(2*h)
        assert_close(d,derivative_integral(n,t),2e-6)
        assert_true(derivative_integral(n,t)>0)
    # Positive terminal deficit coefficient; a separate integral computation.
    nu=(R*R+mu)/2
    C=pi*pi*(4*mu*mu-mu-3*nu)
    assert_true(C>0)
    assert_close((pi*pi-volume_product(n,2000))*2000**2,C,0.005)

for n in range(3,71):
    vals=[volume_product(n,t) for t in [0,.002,.02,.2,2,20,200]]
    assert_true(all(b>a for a,b in zip(vals,vals[1:])))
    assert_true(vals[-1]<pi*pi)

# A direct test of the deterministic inequality used in the analytic derivative proof.
for n in range(3,71):
    alpha,R,mu=constants(n)
    var=(R*R+mu)/2-mu*mu
    assert_true(mu*(mu-1)>Fraction(81,16)*var)
    assert_true(mu*(mu-1)> (alpha*alpha)/3+11*alpha**4/45-1e-13)
    assert_true(var<R*R*alpha**4/45+1e-13)

# Sharp large-rounding coefficient and large-polygon fixed-rounding profile.
for n in (3,4,10,50):
    alpha,R,mu=constants(n)
    nu=(R*R+mu)/2
    C=pi*pi*(4*mu*mu-mu-3*nu)
    for t in [3000,6000]:
        assert_close((pi*pi-volume_product(n,t))*t*t,C,0.008)
for n in (250,500):
    alpha,R,mu=constants(n)
    for t in [0., .5, 3.,10.]:
        deficit=(pi*pi-volume_product(n,t))/(pi*pi)
        target=alpha*alpha/(3*(1+t)**2)
        assert_close(deficit,target,0.002)
print(f'PASS: {checks} finite checks (standard-library exact rationals and two independent polar quadratures).')
