#!/usr/bin/env python3
"""Algebraic and numerical checks for the planar radial covariance theorem.
Requires Python 3 and the public packages sympy, scipy, numpy.
This executable is evidence for finite checks; the all-frequency result is proved in RESULT.md.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import j0
from scipy.spatial.distance import cdist

u,t=sp.symbols('u t',real=True)
p=(3 +30*t*u +(-30*t+35*t*t)*u**2-60*t*t*u**3
   +(15*t*t-14*t**3)*u**4+6*t**3*u**5-t**4*u**6)
bs=[3, 3+5*t, (t+3)*(7*t+3)/3, 3+9*t+4*t*t,
    (45+120*t+45*t*t-14*t**3)/15,
    (1+t)*(9+6*t-11*t*t)/3,
    (1+t)**2*(3-6*t-t*t)]
assert sp.expand(p-sum(sp.binomial(6,k)*bs[k]*u**k*(1-u)**(6-k) for k in range(7)))==0
q,w=sp.symbols('q w',real=True)
Pq=sp.expand(3*sp.re((1+sp.I*q)**5*(1-sp.I*w)**2)+w*w*(3-q*q)*(1+q*q)**2)
assert sp.expand(Pq-p.subs({u:q/w,t:w*w}))==0
assert sp.factor(p.subs(u,1)-(1+t)**2*(3-6*t-t*t))==0
print('Exact polynomial and seven-term Bernstein identities: PASS')

critical=math.sqrt(2*math.sqrt(3)-3)

def formula(lam,rho):
    z=1-1j*lam
    D=z*z+rho*rho
    return 2*math.pi*((-1j*lam)*D**(-1.5)+3*z*z*D**(-2.5)).real

max_err=0.0
count=0
for lam in [0.0,0.2,0.5,critical,0.8]:
    for rho in [0.0,0.3,1.3,3.5,7.0]:
        integ=2*math.pi*quad(lambda r:r*(1+r)*math.exp(-r)*math.cos(lam*r)*j0(rho*r),0,100,epsabs=8e-12,limit=600)[0]
        err=abs(formula(lam,rho)-integ)
        max_err=max(max_err,err)
        assert err<3e-9,(lam,rho,err)
        count+=1
print(f'Bessel integral comparisons: {count} PASS; max abs err {max_err:.3g}')
assert abs(formula(critical,0))<1e-12
for rho in np.geomspace(1e-4,20,100):
    assert formula(critical,float(rho))>0
for lam in [0.70,0.8,1.0]:
    assert formula(lam,0)<0
print('Critical zero, positive nonzero frequencies, inadmissible negative origin: PASS')

points=np.array([(2*i,2*j) for i in range(6) for j in range(6)],dtype=float)
d=cdist(points,points)
K=(1+d)*np.exp(-d)*np.cos(0.8*d)
ev=np.linalg.eigvalsh(K)
assert ev[0]<-0.01
print(f'6x6 lattice finite Gram witness for lambda=0.8: min eigenvalue {ev[0]:.12f} PASS')
print(f'Critical ratio sqrt(2sqrt(3)-3): {critical:.15f}')
