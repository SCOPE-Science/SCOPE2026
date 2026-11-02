"""Supplementary checks for Gaussian-Fock exterior Laurent Hankel spectral tails.

Run with `python checker.py` (requires mpmath and sympy).
Numerical assertions are supplementary and do not certify infinite-dimensional claims.
"""
from math import factorial
import mpmath as mp
import sympy as sp

mp.mp.dps = 90
checks = 0
n = sp.symbols('n', integer=True, positive=True)
for j in range(1, 9):
    # The no-cutoff moment difference, valid for n>j.
    v = sp.prod(1/(n-i) for i in range(j)) - sp.prod(1/(n+i) for i in range(1,j+1))
    leading = sp.limit(n**(j+1)*v, n, sp.oo)
    assert leading == j*j, (j, leading)
    checks += 1

def normsq_conj(j, N, t):
    g = mp.gammainc(N-j+1, t, mp.inf)
    q = mp.gammainc(N+1, t, mp.inf)
    return g/mp.factorial(N)-q*q/(mp.factorial(N)*mp.factorial(N+j))

def normsq_direct(j, N, t):
    g = mp.gammainc(N-j+1, t, mp.inf)
    if N < j:
        return g/mp.factorial(N)
    return g/mp.factorial(N)*(1-g/mp.factorial(N-j))

for j in (1,2,3,4,5):
    for t in (mp.mpf('0.25'),mp.mpf('1.0'),mp.mpf('3.24')):
        for N in (40,90,180):
            lam = normsq_conj(j,N,t)
            assert lam > 0, (j,t,N,lam)
            asym = (j*j)*mp.power(N,-j-1)
            assert abs(lam/asym-1) < mp.mpf('0.39'), (j,t,N,lam/asym)
            d = normsq_direct(j,N,t)
            assert d >= 0
            assert d < mp.mpf('1e-8'), (j,t,N,d)
            checks += 3

# Moment normalization and cancellation for cut-off indicator with R^2 = t.
for t in (mp.mpf('.2'),mp.mpf('1'),mp.mpf('2')):
    for j in (1,2,3):
        for N in (2*j+4,2*j+9):
            m = mp.gammainc(N-j+1,t,mp.inf)/mp.factorial(N)
            q = mp.gammainc(N+1,t,mp.inf)
            projection_sq = q*q/(mp.factorial(N)*mp.factorial(N+j))
            assert 0 <= projection_sq <= m
            assert mp.almosteq(m-projection_sq, normsq_conj(j,N,t))
            checks += 2
print(f'PASS: {checks} supplementary exact/symbolic and numerical assertions')
