#!/usr/bin/env python3
"""Independent finite-dimensional numerical checks of explicit Legendre--Jacobi coefficients.

Uses Python, NumPy, SciPy. These tests are not a proof of the asymptotic theorem.
"""
import numpy as np
from numpy.polynomial.legendre import Legendre
from scipy.linalg import eigh_tridiagonal
from scipy.special import ai_zeros

# The primitive of the normalized shifted Legendre basis has precisely three terms.
for k in range(1, 12):
    p = Legendre.basis(k) * np.sqrt(2*k+1)
    primitive = 0.5 * p.integ()
    primitive -= primitive(-1)
    coeff = primitive.coef
    c_hi = 1/(2*np.sqrt((2*k+1)*(2*k+3)))
    c_lo = 1/(2*np.sqrt((2*k-1)*(2*k+1)))
    assert np.isclose(coeff[k+1], c_hi*np.sqrt(2*k+3), atol=1e-12)
    assert np.isclose(coeff[k-1], -c_lo*np.sqrt(2*k-1), atol=1e-12)
    assert np.max(np.abs(np.delete(coeff,[k-1,k+1]))) < 1e-10

C = abs(ai_zeros(1)[0][0]) / 2**(4/3)
last_dev = None
for n in [50, 100, 300, 1000, 3000, 10000, 30000, 100000]:
    L = int(36*n**(1/3)+30)
    idx = n + np.arange(L-1,dtype=float)
    a = 1/(2*np.sqrt((2*idx+1)*(2*idx+3)))
    op_norm = eigh_tridiagonal(np.zeros(L),a,select='i',select_range=(L-1,L-1),eigvals_only=True)[0]
    estimate = n**(5/3)*(0.5/n-op_norm)
    assert 0 < estimate < C
    deviation = abs(estimate-C)
    if last_dev is not None: assert deviation < last_dev
    last_dev = deviation
    print(f'n={n:<7} scaled_correction={estimate:.12f} Airy_constant={C:.12f}')
print('PASS: coefficient identity and eight finite Jacobi edge checks')
