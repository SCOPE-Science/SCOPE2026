#!/usr/bin/env python3
"""Finite diagnostics for two-Hermite half-line concentration.

The rigorous uniqueness proof is the monotone integral-ratio argument in RESULT.md;
this code checks formulas independently by numerical quadrature.
"""
from math import erf, erfc, exp, pi, sqrt, isfinite


def hermite_product(x, j, k):
    base = exp(-x*x) / sqrt(pi)
    coeffs = (1.0, sqrt(2.0)*x)
    return base*coeffs[j]*coeffs[k]


def simpson(f, lo, hi, n=2000):
    assert n > 0 and n % 2 == 0
    step = (hi-lo)/n
    total = f(lo)+f(hi)
    for k in range(1,n):
        total += (4.0 if k%2 else 2.0)*f(lo+step*k)
    return total*step/3.0


def matrix(t):
    f = exp(-t*t)/sqrt(pi)
    q = erfc(t)/2.0
    return ((q,f/sqrt(2.0)),(f/sqrt(2.0),q+t*f))


def variance(t):
    m = matrix(t)
    a,b = m[0]
    _,d = m[1]
    return a+d-a*a-d*d-2*b*b


def derivative(t):
    f=exp(-t*t)/sqrt(pi)
    return f*(4*t*(1+t*t)*f-(1+2*t*t)*erf(t))


def equation(t):
    return erf(t)/(2*t*exp(-t*t)/sqrt(pi))-2*(1+t*t)/(1+2*t*t)


def solve_root():
    a,b=.7,.8
    assert equation(a)<0<equation(b)
    for _ in range(75):
        mid=(a+b)/2
        if equation(mid)<0:
            a=mid
        else:
            b=mid
    return (a+b)/2


checks=0
# Numerical quadrature is independent of the closed-form tail antiderivatives.
for i in range(-20,21):
    t=i/8
    m=matrix(t)
    for j in (0,1):
        for k in (0,1):
            numerical=simpson(lambda x:hermite_product(x,j,k),t,12)
            assert abs(numerical-m[j][k])<2e-9,(t,j,k,numerical,m[j][k])
            checks+=1
    a,b=m[0]
    _,d=m[1]
    disc=sqrt((a-d)**2+4*b*b)
    lower=(a+d-disc)/2
    upper=(a+d+disc)/2
    assert 0<lower<upper<1
    checks+=1
    e=erf(t)
    f=exp(-t*t)/sqrt(pi)
    closed=(1-e*e)/2+t*f*e-(1+t*t)*f*f
    assert abs(variance(t)-closed)<4e-15
    assert abs(variance(t)-variance(-t))<4e-15
    checks+=2

star=solve_root()
assert .748111391995<star<.748111391997
assert .257120277197<variance(star)<.257120277200
assert abs(derivative(star))<1e-14
checks+=3
for k in range(1,100):
    t=star*k/100
    assert derivative(t)>0
    checks+=1
for k in range(1,100):
    t=star+k/100
    assert derivative(t)<0
    checks+=1

# Ratio proof independently sampled; the proof is analytic, not this grid.
for k in range(1,40):
    x=.1*k
    dx=1e-5
    assert equation(x+dx)>equation(x-dx)
    checks+=1

assert isfinite(star)
print(f'VERIFY_OK checks={checks} tstar={star:.15f} Vmax={variance(star):.15f}')
