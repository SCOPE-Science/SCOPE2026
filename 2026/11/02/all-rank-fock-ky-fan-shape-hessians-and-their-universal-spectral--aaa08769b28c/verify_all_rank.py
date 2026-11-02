#!/usr/bin/env python3
"""Standalone finite arithmetic and matrix checks of Fock Ky Fan shape formulas.

Analytical limits and infinite-dimensional perturbation theory are proved in RESULT.md,
not certified by numerical truncations. Requires numpy and scipy for matrix checks.
"""
from fractions import Fraction
from math import factorial, exp, log, lgamma
import numpy as np
from scipy.special import gammainc, gammaln

checks = 0

def check(assertion, note):
    global checks
    if not assertion:
        raise AssertionError(note)
    checks += 1

def p_exact(x, j):
    return x**j / factorial(j)

def curvature_exact(N, x, k):
    p = lambda j: p_exact(x, j)
    return p(N-1) - sum(
        p(i) * p(i+k) / sum(p(l) for l in range(i+1, i+k+1))
        for i in range(max(0, N-k), N)
    )

for N in range(2, 12):
    for x in [Fraction(1, 3), Fraction(1), Fraction(5, 2), Fraction(7)]:
        check(curvature_exact(N, x, 1) == 0, ('translation', N, x))
        quadrupole = p_exact(x, N-1) * (N+1+2*x) / ((N+x)*(N+1+x))
        check(curvature_exact(N, x, 2) == quadrupole, ('quadrupole', N, x))
        for k in [2,3,4,6]:
            check(curvature_exact(N, x, k) > 0, ('finite curvature', N, x, k))

# Check each finite polynomial identity underlying the balanced-edge expansion.
for k in range(1, 61):
    alpha = lambda s: Fraction(s * (s+1), 2)
    endpoint_sum = sum(alpha(u-k)+alpha(u) for u in range(k))
    interior_sum = sum(
        sum(alpha(s) for s in range(u-k+1, u+1))/k
        for u in range(k)
    )
    check(endpoint_sum == Fraction(k*(k*k-1), 3), ('endpoint sum', k))
    check(interior_sum == Fraction(k*(k*k-1), 12), ('interior sum', k))
    check((endpoint_sum-interior_sum)/k == Fraction(k*k-1, 4), ('edge coefficient', k))

# Direct numerical checks use a truncated Fock-basis Toeplitz matrix.
def kyfan_finite(N,x,epsilon,k, dim=None, nodes=1200):
    if dim is None:
        dim = N+16
    theta = 2*np.pi*np.arange(nodes)/nodes
    R = x + epsilon*np.cos(k*theta)
    M = np.empty((dim,dim), dtype=complex)
    for j in range(dim):
        for l in range(dim):
            s = (j+l)/2 + 1
            val = np.exp(gammaln(s)-(gammaln(j+1)+gammaln(l+1))/2)*gammainc(s,R)
            M[j,l] = np.mean(val*np.exp(1j*(l-j)*theta))
    eigenvalues = np.linalg.eigvalsh((M+M.conj().T)/2)
    return np.sum(eigenvalues[-N:])

for N in [2,3,5]:
    for x in [0.75,2.0,5.0]:
        for k in [1,2,3,5]:
            step = 0.008
            center = kyfan_finite(N,x,0,k)
            right = kyfan_finite(N,x,step,k)
            left = kyfan_finite(N,x,-step,k)
            observed = (right+left-2*center)/(step**2)
            xx = Fraction(str(x))
            expected = -0.5*exp(-x)*float(curvature_exact(N,xx,k))
            check(abs(observed-expected) < 3e-5,
                  ('spectral second variation',N,x,k,observed,expected))

# Avoid gigantic factorials in the edge limit by taking adjacent ratios.
def normalized_poisson(N,s):
    v=1.
    if s>=0:
        for r in range(s+1):
            v*=N/(N+r)
    else:
        for r in range(-1,s,-1):
            v*=(N+r)/N
    return v

for k in [1,2,3,4,6,9]:
    for N in [100,500,2000]:
        S=sum(
            normalized_poisson(N,i-N)*normalized_poisson(N,i+k-N)/
            sum(normalized_poisson(N,j-N) for j in range(i+1,i+k+1))
            for i in range(N-k,N)
        )
        scaled = N*(1-S)
        limit = (k*k-1)/4
        check(abs(scaled-limit) < (20*k**4)/N if k>=2 else abs(scaled)<1e-6,
              ('balanced edge convergence',N,k,scaled,limit))

print(f'{checks} finite arithmetic, truncated-spectrum, and asymptotic checks passed.')
print('These checks do not independently certify the infinite-dimensional proof.')
