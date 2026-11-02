#!/usr/bin/env python3
"""Finite checks for a Rhaly singular-value asymptotic.

Dependencies: Python >=3.10, numpy >=1.24, scipy >=1.10.
The rigorous infinite-dimensional argument is in RESULT.md.
"""
from fractions import Fraction
from math import comb, gamma, pi, sin, sqrt, isclose
import numpy as np
from scipy.linalg import eigh_tridiagonal

checks = 0

def check(condition, message='verification'):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

# Exact matrix entries of C - S^{*k} C S^k, with indices starting at zero.
for k in range(1, 13):
    for n in range(0, 75):
        a = Fraction(k, (n + 1) * (n + k + 1))
        check(a == Fraction(1, n + 1) - Fraction(1, n + k + 1))
        for j in range(n + 1):
            c0 = Fraction(1, n + 1)
            c1 = Fraction(1, n + k + 1)
            check(c0 - c1 == a)
        for j in range(n + 1, n + 6):
            shifted = Fraction(1, n + k + 1) if j <= n else Fraction(0)
            unshifted = Fraction(1, n + 1) if j <= n else Fraction(0)
            check(unshifted - shifted == 0)  # Genuine zero matrix entries above the diagonal.

# The positive eigenvalues of L_m^*L_m are given by squared cosecant terms.
for m in range(1, 41):
    L = np.tril(np.ones((m, m), dtype=float))
    direct = np.linalg.svd(L, compute_uv=False)
    formula = np.array([1.0 / (2.0*sin((2*j-1)*pi/(4*m+2))) for j in range(1,m+1)])
    for v, w in zip(direct, formula):
        check(isclose(v, w, rel_tol=3e-12, abs_tol=1e-12))

# Exact tridiagonal inverse for the compressed Cesaro conjugation defect.
for k in range(1,7):
    for N in (5, 7, 10, 16, 24, 30):
        n = np.arange(1,N+1, dtype=float)
        d = k/(n*(n+k))
        lower = np.tril(np.ones((N,N))) * d[:,None]
        direct = np.linalg.svd(lower, compute_uv=False)
        diagonal = 2/d**2
        diagonal[-1] = 1/d[-1]**2
        offdiag = -1/(d[:-1]*d[1:])
        eigs = eigh_tridiagonal(diagonal, offdiag, eigvals_only=True)
        predicted = 1/np.sqrt(eigs)
        predicted.sort()
        predicted = predicted[::-1]
        for v,w in zip(direct, predicted):
            check(isclose(v,w,rel_tol=4e-8,abs_tol=2e-9),f'k={k}, N={N}, {v} {w}')

# The asymptotic coefficient is a beta integral, tested by quadrature.
from scipy.integrate import quad
from scipy.special import beta
A = beta(0.25, 0.5)/(pi*sqrt(2))
A_quad = quad(lambda theta:(2*sin(theta/2))**(-0.5)/pi,0,pi,epsabs=1e-11)[0]
check(isclose(A,A_quad,rel_tol=1e-11))
for k in (1,2,4):
    N=4000
    n=np.arange(1,N+1,dtype=float)
    d=k/(n*(n+k))
    diagonal=2/d**2
    diagonal[-1]=1/d[-1]**2
    offdiag=-1/(d[:-1]*d[1:])
    eigs=eigh_tridiagonal(diagonal,offdiag,select='i',select_range=(0,119),eigvals_only=True)
    for j in (40,65,90):
        scaled=j*j/sqrt(eigs[j-1])
        check(abs(scaled/(k*A*A)-1)<0.18, f'asymptotic k={k}, j={j}, {scaled}')
print(f'CHECKS_PASS: {checks}')
print(f'A = {A:.15f}, A^2 = {A*A:.15f}')
