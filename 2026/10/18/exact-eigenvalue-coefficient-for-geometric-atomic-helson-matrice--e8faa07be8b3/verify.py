#!/usr/bin/env python3
"""Finite numerical cross-checks only; does not prove asymptotic spectral statements.
Dependencies: Python 3, NumPy, SciPy. No network access required.
"""
import math
import numpy as np
from scipy.special import zeta
from scipy.linalg import eigh

for q in (2.0, 4.0, 16.0):
    a = math.log(q)/2
    for j in range(1, 16):
        for k in range(1, 16):
            dj, dk = q**(-j), q**(-k)
            cauchy = 2*math.sqrt(dj*dk)/(dj+dk)
            assert abs(cauchy - 1/math.cosh(a*(j-k))) < 2e-12
for q in (2.0,4.0):
    for j in range(1, 7):
        for k in range(1, 7):
            t = 0.125*(q**(-j)+q**(-k))
            rem = float(zeta(1+t) - 1/t)
            assert -1e-7 <= rem <= 1+1e-7, (q,j,k,rem)

for q in (4.0, 64.0):
    a=math.log(q)/2
    k=np.arange(1,60,dtype=float)
    c=1/np.cosh(a*k)
    theta=np.linspace(-math.pi,math.pi,8192,endpoint=False)
    f=1+2*np.sum(c[:,None]*np.cos(k[:,None]*theta),axis=0)
    assert np.min(f)>0
    m1=float(np.mean(f)); m2=float(np.mean(f*f))
    assert abs(m1-1)<1e-10
    assert abs(m2-(1+2*np.sum(c*c)))<1e-10

# Banded covariance already yields the asymptotic coefficient; we use a
# finite section of this exact limiting kernel, not an unverified approximate
# infinite zeta matrix. The large-q test avoids edge sensitivity.
q=64.0; a=math.log(q)/2; N=320
ind=np.arange(1,N+1,dtype=float)
dif=ind[:,None]-ind[None,:]
K=1/np.cosh(np.clip(a*dif,-700,700))
for r in (0.5, 1.0):
    A=(ind[:,None]*ind[None,:])**(-r/2)*K
    ev=eigh(A,eigvals_only=True,driver='evr')[::-1]
    theta=np.linspace(-math.pi,math.pi,8192,endpoint=False)
    k=np.arange(1,60,dtype=float)
    f=1+2*np.sum((1/np.cosh(a*k))[:,None]*np.cos(k[:,None]*theta),axis=0)
    predicted=float(np.mean(f**(1/r))**r)
    # n=80 and 100 remain sufficiently far from the finite-section edge.
    for n in (80,100):
        observed=float(ev[n-1]*n**r)
        assert abs(observed/predicted-1)<0.02, (r,n,observed,predicted)
print('GEOMETRIC_ATOMIC_HELSON_COVARIANCE_AND_SPECTRAL_CHECKS_OK')
