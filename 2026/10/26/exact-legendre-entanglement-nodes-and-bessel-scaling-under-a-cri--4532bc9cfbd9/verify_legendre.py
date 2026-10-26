#!/usr/bin/env python3
"""Exact and numerical checks of a reset-age/entanglement identity.
External dependency: mpmath (tested 1.3.0) and numpy (tested 2.3.5).
This is supporting finite verification, not a substitute for the proof.
"""
from fractions import Fraction
from math import comb, pi, cos, sin, factorial
import cmath
import numpy as np
import mpmath as mp
from scipy.special import eval_legendre


def probability_by_process(t):
    """Propagate the age process with hazard 1/[2(n+1)] using exact fractions."""
    law = [Fraction(1)]
    for _ in range(t):
        next_law = [Fraction(0) for _ in range(len(law)+1)]
        for n,p in enumerate(law):
            r = Fraction(1,2*(n+1))
            next_law[0] += p*r
            next_law[n+1] += p*(1-r)
        law = next_law
    return law


def pochhammer_half_ratio(n):
    return Fraction(comb(2*n,n),4**n)


def legendre_coeffs(t):
    if t==0: return [Fraction(1)]
    a=[Fraction(1)];b=[Fraction(0),Fraction(1)]
    if t==1: return b
    for n in range(1,t):
        xpoly=[Fraction(0)]+b
        c=[((2*n+1)*(xpoly[k] if k<len(xpoly) else 0)-n*(a[k] if k<len(a) else 0))/Fraction(n+1) for k in range(len(xpoly))]
        a,b=b,c
    return b


def eval_poly(poly,x):
    z=0
    for a in reversed(poly): z=z*x+a
    return z

for t in range(0,24):
    law=probability_by_process(t)
    want=[pochhammer_half_ratio(n)*pochhammer_half_ratio(t-n) for n in range(t+1)]
    assert law==want,(t,law,want)
    assert sum(law)==1
    for theta in [0, 0.27, 1.21, 2.77, pi, 3.7, 5.13, 2*pi]:
        ph=sum(float(w)*cmath.exp(1j*n*theta) for n,w in enumerate(law))
        predicted=cmath.exp(1j*t*theta/2)*float(eval_legendre(t,cos(theta/2)))
        assert abs(ph-predicted)<5e-12,(t,theta,abs(ph-predicted))
print('exact transfer recursion agrees with beta-binomial coefficients: t=0..23')
print('Fourier polynomial agrees with Legendre expression on all samples')

sy=np.array([[0,-1j],[1j,0]],complex)
flip=np.kron(sy,sy)
for t in [1,2,3,4,5,8,10,12]:
    law=probability_by_process(t)
    for theta in [0.21,1.08,2.56,3.14,5.5]:
        rho=np.zeros((4,4),complex)
        for n,w in enumerate(law):
            v=np.array([1,0,0,cmath.exp(1j*n*theta)],complex)/np.sqrt(2)
            rho+=float(w)*np.outer(v,np.conjugate(v))
        R=rho@flip@rho.conj()@flip
        eig=np.sort(np.real_if_close(np.linalg.eigvals(R)).real)[::-1]
        z=np.sqrt(np.maximum(eig,0))
        conc=max(0.,z[0]-sum(z[1:]))
        predicted=abs(float(eval_legendre(t,cos(theta/2))))
        assert abs(conc-predicted)<1e-7,(t,theta,conc,predicted)
print('independent spin-flip two-qubit concurrence agrees on 40 states')

for t in [5,10,20,40,80,160]:
    roots,_=np.polynomial.legendre.leggauss(t)
    roots=np.sort(2*np.arccos(roots))
    assert len(roots)==t and np.all(np.diff(roots)>0)
    for k in [0,min(t-1,1),min(t-1,2)]:
        a=abs(np.polynomial.legendre.legval(cos(roots[k]/2),[0]*t+[1]))
        assert a<1e-11,(t,k,a)
    first_scaled=t*roots[0]
    print(f't={t:3d} zeros={len(roots):3d} t*first_zero={first_scaled:.9f} Bessel limit={2*float(mp.besseljzero(0,1)):.9f}')

for s in [0.7,2.1,4.5,7.5,10.0]:
    t=500
    approximate=np.polynomial.legendre.legval(cos(s/(2*t)),[0]*t+[1])
    bessel=float(mp.besselj(0,s/2))
    print(f'Bessel boundary s={s:4.1f} t=500 amplitude={approximate:.8f} limit={bessel:.8f}')
    assert abs(approximate-bessel)<0.018
print('PASS')
