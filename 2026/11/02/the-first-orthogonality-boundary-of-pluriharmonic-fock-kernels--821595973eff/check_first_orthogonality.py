#!/usr/bin/env python3
"""Numerical illustrations for the first zero of a pluriharmonic Fock kernel.
This finite program supports but does not prove the infinite-family statements.
Requires only Python's standard library; run with `python check_first_orthogonality.py`.
"""
from math import pi, sin, cos, sqrt, exp, log, asin

t0=log(2)
def scaled(t,theta):
    return 2*cos(t*sin(theta))-exp(-t*cos(theta))

def root(t):
    assert t>=t0
    if t==t0:return pi
    upper=asin(pi/(2*t)) if t>=pi/2 else pi
    lo=0.
    assert scaled(t,lo)>0 and scaled(t,upper)<0
    for _ in range(75):
        mid=(lo+upper)/2
        if scaled(t,mid)>0:lo=mid
        else:upper=mid
    return (lo+upper)/2

previous=pi
points=[t0+1e-8,t0+1e-6,t0+.0001,t0+.01,.8,1,1.4,pi/2,2,3,5,10,20,50,100]
for t in points:
    a=root(t)
    assert 0<a<previous and abs(scaled(t,a))<3e-13
    q=a+t*sin(a)
    assert pi/2<q<pi
    previous=a
    d=2*sqrt(t)*sin(a/2)
    if t>=20:
        asym=pi/(2*sqrt(t))+pi**3/(64*t**(5/2))
        assert abs(d-asym)<2/t**4.5
    if t-t0<1e-4:
        ratio=(pi-a)/sqrt(t-t0)
        constant=sqrt(2/(t0*(1-t0)))
        assert abs(ratio-constant)<.001
print('PASS: 15 first-zero roots, signs, angular ordering, and asymptotic checks')
for t in [t0+.01,1,2,10,100]:
    a=root(t)
    print(f't={t:.9f}, theta={a:.12f}, chord={2*sqrt(t)*sin(a/2):.12f}')
