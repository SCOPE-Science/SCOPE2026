#!/usr/bin/env python3
"""Supplementary reproducibility tests for a finite Blaschke product Airy-edge law.

Requires NumPy and SciPy. Numerical checks are not a proof of the limit.
"""
from fractions import Fraction as F
from math import pi
import numpy as np
from scipy.special import airy
from scipy.integrate import quad

radii=(F(1,5),F(1,2))
U=sum(2*a*(1+a)/(1-a)**3 for a in radii)
V=sum(2*a*(1-a)/(1+a)**3 for a in radii)
lo=sum((1-a)/(1+a) for a in radii)
hi=sum((1+a)/(1-a) for a in radii)
assert (U,V,lo,hi)==(F(207,16),F(1,3),F(1,1),F(9,2))

def coeffs(n):
    # Sufficient Fourier grid to avoid coefficient wrap near the two folds.
    N=1
    while N<16*n: N*=2
    theta=2*np.pi*np.arange(N)/N
    z=np.exp(1j*theta)
    B=np.ones(N,complex)
    for a in radii:
        aa=float(a)
        B*=(z-aa)/(1-aa*z)
    c=np.fft.fft(B**n)/N
    return c[:int(8*n)]

U,V=float(U),float(V)
def Ftheta(t):
    return sum((1-float(a)**2)/(1-2*float(a)*np.cos(t)+float(a)**2) for a in radii)
for theta,expect in ((0,-U),(np.pi,V)):
    h=1e-3
    second=(Ftheta(theta+h)-2*Ftheta(theta)+Ftheta(theta-h))/h**2
    assert abs(second-expect)<2e-3, (second,expect)
for n in (500,1000,2000):
    c=coeffs(n)
    # Check both folds at several scaled displacements.
    for lam,curv,sgn in ((4.5,U,+1),(1.0,V,-1)):
        h=(2/(n*curv))**(1/3)
        for s in (-1.0,0.0,1.0):
            k=round(n*lam+sgn*s/h)
            t=sgn*(k-n*lam)*h
            prediction=h*airy(t)[0]
            # Phases depend on parity at the lower fold, so compare absolute values.
            error=abs(abs(c[k])-abs(prediction))
            assert error<0.09*h, (n,k,error,h)

# The universal sixth Airy moment has an integrable oscillatory negative tail.
# Numerical tail asymptotic provides a consistency scale, not a certificate.
T=100.0
I=quad(lambda x:abs(airy(x)[0])**6,-T,50,epsabs=1e-10,limit=500)[0]
# Leading negative Airy tail: mean(sin^6)=5/16, amplitude=(pi sqrt(t))^(-1).
# Integral of (5/(16*pi**3))*t^(-3/2) from T to infinity = 5/(8*pi**3*sqrt(T)).
# This tail estimate is asymptotic, not a rigorous certified quadrature enclosure.
I+=5/(8*np.pi**3*np.sqrt(T))
C=2**(5/3)*(U**(-5/3)+V**(-5/3))*I
assert 0.70<C<0.75,(I,C)
vals=[]
for n in (500,1000,2000):
    c=coeffs(n)
    vals.append(n**(5/3)*float(np.sum(np.abs(c)**6)))
assert vals[0]<vals[1]<vals[2]<C, (vals,C)
print('PASS: exact curvature identities; 18 Airy edge samples; sixth moment trend')
print('finite-size normalized sixth moments:',vals)
print('truncated Airy constant (for reference only):',C)
