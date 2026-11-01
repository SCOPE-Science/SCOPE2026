#!/usr/bin/env python3
"""Independent numerical cross-checks and rational endpoint certificates.

Run: python3 CHECK.py (Python standard library only). These finite tests
supplement the analytical argument; they do not prove the continuum theorem.
"""
from fractions import Fraction as F
from math import cos, pi, log, sqrt


def arctan_interval(q, n):
    x = F(1,q)
    s = sum((-1)**j * x**(2*j+1)/F(2*j+1) for j in range(n))
    error = x**(2*n+1)/F(2*n+1)
    return (s-error, s) if n%2 == 0 else (s,s+error)


def ln2_interval(n):
    x = F(1,3)
    s = 2*sum(x**(2*j+1)/F(2*j+1) for j in range(n))
    error = 2*x**(2*n+1)/F(2*n+1)/(1-x*x)
    return s,s+error


a1,b1=arctan_interval(5,15)
a2,b2=arctan_interval(239,6)
pi_l,pi_u=16*a1-4*b2,16*b1-4*a2
ln_l,ln_u=ln2_interval(16)
# alpha 2: u-v=12+3*pi/2-24 log 2
assert F(12)+F(3,2)*pi_l-24*ln_u>0
# alpha 3: u-v=102-6*pi-120 log 2
assert F(102)-6*pi_l-120*ln_l<0
assert F('3.14159')<pi_l<pi_u<F('3.14160')
assert F('0.69314')<ln_l<ln_u<F('0.69315')


def simpson(fn, steps=10000):
    assert steps%2==0
    h=1/steps
    acc=fn(0)+fn(1)
    for j in range(1,steps):
        acc+=(4 if j%2 else 2)*fn(j*h)
    return h*acc/3


def curv(a):
    u=4*(a+1)*simpson(lambda t:t*(1-t*t)*(1-t)**a/(1+t*t)**3)
    v=(a+1)*simpson(lambda t:(1-t)**(a+1)/(1+t)**3)
    return u,v


def phi(a,angle):
    c=cos(angle)
    return (a+1)*simpson(lambda t:(1-t)**a*(c-t)/(1-2*t*c+t*t))


def pair_energy(a,angles):
    return 2*sum(phi(a,angles[j]-angles[k]) for j in range(4) for k in range(j+1,4))


def rayleigh_fd(a,v,h=0.0006):
    square=[j*pi/2 for j in range(4)]
    e0=pair_energy(a,square)
    ep=pair_energy(a,[square[j]+h*v[j] for j in range(4)])
    em=pair_energy(a,[square[j]-h*v[j] for j in range(4)])
    return (ep+em-2*e0)/(h*h*sum(x*x for x in v))


cases=0
for a in (0.25,0.5,1,2,3,5,10,30):
    u,v=curv(a)
    assert u>0 and v>0
    # expected square spectrum: double first mode, single alternating mode
    first=4*(u+v)
    alternating=8*u
    numerical_first=rayleigh_fd(a,[1,0,-1,0])
    numerical_alternating=rayleigh_fd(a,[1,-1,1,-1])
    assert abs(numerical_first-first)<0.00005,(a,numerical_first,first)
    assert abs(numerical_alternating-alternating)<0.00005,(a,numerical_alternating,alternating)
    cases+=4

# Endpoint exact integral formulas against independent quadrature.
u2,v2=curv(2)
u3,v3=curv(3)
assert abs(u2-(1.5*pi-6*log(2)))<1e-9
assert abs(v2-(18*log(2)-12))<1e-9
assert abs(u3-(36-6*pi-24*log(2)))<1e-9
assert abs(v3-(96*log(2)-66))<1e-9
assert u2>v2 and u3<v3
assert curv(0.001)[0]>curv(0.001)[1]
# Check strict monotonicity of u/v on a nontrivial grid.
params=[j/4 for j in range(1,61)]
ratios=[]
for a in params:
    u,v=curv(a)
    ratios.append(u/v)
assert all(ratios[j]>ratios[j+1] for j in range(len(ratios)-1))
print('PASS: exact rational endpoint certificates, integral formulas, independent finite-difference Hessian and ratio monotonicity (',cases,'modal checks)')
