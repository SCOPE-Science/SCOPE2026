#!/usr/bin/env python3
"""Independent numerical checks of the shrinking-pole Fourier formulas.
Requirements: Python 3, NumPy, SciPy. Finite checks supplement analytic proofs.
"""
import numpy as np
from scipy.special import jv, jn_zeros
from scipy.optimize import brentq

NFFT = 8192
phase = 2*np.pi*np.arange(NFFT)/NFFT
z = np.exp(1j*phase)

def fourier_coefficients(n, c):
    lam = c/n
    H = (1-lam/z)**(n-1)/(1-lam*z)**n
    return np.fft.fft(H)/NFFT

def bessel_terms(c):
    k = np.arange(-80,81)
    a = jv(k,2*c)
    b = c*jv(k+1,2*c)+(c*c/2)*(jv(k-2,2*c)-jv(k+2,2*c))
    return a,b

for c in [0.1,0.5,1,1.4,2,3]:
    a,b = bessel_terms(c)
    baseline = np.abs(a).sum()
    derivative = (np.sign(a)*b).sum()
    errors = []
    for n in [80,160,320]:
        w = np.abs(fourier_coefficients(n,c)).sum()
        errors.append(abs(n*(w-baseline)-derivative))
    assert errors[2] < errors[1] < errors[0], (c,errors)
    print('Wiener limit and first-order trend',c,errors)

for m in [0,1,2,3]:
    c0 = jn_zeros(m,1)[0]/2
    for n in [80,160,320]:
        for k in ([0] if m==0 else [m,-m]):
            def realco(c): return fourier_coefficients(n,c)[k%NFFT].real
            root = brentq(realco,c0-.3,c0+.3,xtol=1e-12)
            predicted_shift = c0*(1-k)/2
            residual = abs(n*(root-c0)-predicted_shift)
            assert residual < 0.15, (m,n,k,residual)
            if n==320: print('zero splitting',m,k,n,root,predicted_shift,residual)
print('All finite checks passed.')
