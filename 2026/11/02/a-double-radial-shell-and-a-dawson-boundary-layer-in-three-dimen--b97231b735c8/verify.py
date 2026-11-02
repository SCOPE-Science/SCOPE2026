#!/usr/bin/env python3
"""Numerical diagnostic checks for phase-mixed 3D Boltzmann-breather radius.
No claims of interval-certified or exhaustive global mode counts.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar,brentq
from scipy.special import dawsn, k0, k1
SQRT2PI = math.sqrt(2/math.pi)
P0 = 2/math.pi**1.5

def density_q(r,q):
    # Symmetric change u=1+cos(theta) in [0,2], with the angular arcsine law.
    # Map u = 1 - cos(phi), phi in [0,pi]; robust even near the tight phase.
    def fun(phi):
        a=1-q*math.cos(phi)
        return a**(-1.5)*math.exp(-r*r/(2*a))
    return SQRT2PI*r*r*quad(fun,0,math.pi,epsabs=1e-11,epsrel=1e-11,limit=800,points=[0])[0]/math.pi

def limit_q1(r):
    z=r*r/8
    return r*r/(4*math.pi**1.5)*math.exp(-z)*(k0(z)+k1(z))

def F(y):return math.sqrt(2)*y*dawsn(y/math.sqrt(2))
def Fprime(y):return y+(1-y*y)*F(y)/y

y_star=brentq(Fprime,2,3,xtol=1e-14)
assert 2<y_star<3
assert F(2)>F(5)
assert F(y_star)>1.28
assert limit_q1(.8)>limit_q1(.2)
assert limit_q1(.8)>limit_q1(2.0)
assert limit_q1(.1)>P0
print('Dawson edge y*=',format(y_star,'.13f'))
print('F(y*)=',format(F(y_star),'.13f'))
print('F(2), F(5)',F(2),F(5))
print('q=1 density relative heights (.2,.8,2)=',*[limit_q1(r)/P0 for r in (.2,.8,2.)])
for q in [.98,.99,.999,.9999]:
    e=1-q
    inner=minimize_scalar(lambda y:-density_q(math.sqrt(e)*y,q),bounds=(1.5,3.0),method='bounded',options={'xatol':1e-8})
    outer=minimize_scalar(lambda r:-density_q(r,q),bounds=(.35,1.5),method='bounded',options={'xatol':1e-8})
    ri=inner.x*math.sqrt(e)
    ro=outer.x
    print('q',q,'inner r',format(ri,'.9f'),'r/sqrt(e)',format(inner.x,'.9f'),'outer r',format(ro,'.9f'),'inner h',format(-inner.fun,'.9f'),'outer h',format(-outer.fun,'.9f'))
    if q>=.9999:
        assert -inner.fun>density_q(.2,q)
        assert -outer.fun>density_q(.2,q)
        assert -outer.fun>density_q(2,q)
for r in [.2,.8,2]:
    assert abs(density_q(r,.9999)-limit_q1(r))<.002
print('All diagnostic assertions passed.')
