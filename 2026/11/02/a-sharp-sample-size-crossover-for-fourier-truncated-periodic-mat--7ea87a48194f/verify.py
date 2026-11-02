"""Reproduce the finite Fourier Gram-truncation identities and asymptotic constants.

Run: python verify.py. Dependencies: Python standard library, numpy, mpmath.
The infinite-dimensional claims are proved analytically in RESULT.md; this
script supplies independent finite-spectrum and asymptotic spot checks.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import math
import numpy as np
import mpmath as mp

checks = 0

def ok(assertion, explanation):
    global checks
    if not assertion:
        raise AssertionError(explanation)
    checks += 1


def coefficients(d, power, m, L):
    # Strictly positive rational finite periodic spectral kernel.
    grid = product(range(-L, L + 1), repeat=d)
    raw = {k: Fraction(1, (1 + sum(v*v for v in k))**power) for k in grid}
    z = sum(raw.values(), Fraction(0))
    return {k: a/z for k, a in raw.items() if max(abs(v) for v in k) > m}


def statistics(b):
    D = sum(b.values(), Fraction(0))
    S = sum((v*v for v in b.values()), Fraction(0))
    convolution = defaultdict(Fraction)
    for k, v in b.items():
        for l, w in b.items():
            convolution[tuple(a+c for a, c in zip(k,l))] += v*w
    fourth = sum((v*v for v in convolution.values()), Fraction(0))
    return D, S, fourth


for d, power, m, L in [(1, 1, 2, 5), (1, 2, 3, 7), (1, 3, 1, 4),
                        (2, 2, 1, 3), (2, 3, 2, 4)]:
    b = coefficients(d, power, m, L)
    D, S, C = statistics(b)
    ok(D > 0 and S > 0, 'positive tails')
    ok(C >= S*S, 'nonnegative variance')
    ok(C <= D*D*S, 'fourth-moment envelope')
    for N in [1, 2, 3, 7, 21]:
        E = N*D*D + N*(N-1)*S
        V = 2*N*(N-1)*(C - S*S)
        ok(E > 0 and V >= 0, 'exact moment nonnegativity')
        if N > 1:
            q = Fraction(N-1)*S/(D*D)
            ratio = V/(E*E)
            ok(ratio == 2*q*(C-S*S)/(N*D*D*S*(1+q)**2), 'variance ratio algebra')
            ok(ratio <= Fraction(1,2*N), 'universal relative-variance bound')
    # Fourier integration by a uniform periodic trapezoid with enough points
    # to resolve the degree of |E_m|^4 without aliasing.
    Q = 4*L + 3
    grid = np.indices((Q,)*d).reshape(d, -1).T / Q
    x = np.array(list(b), dtype=float)
    y = np.array([float(v) for v in b.values()])
    values = np.cos(2*np.pi*grid @ x.T) @ y
    integral2 = np.mean(values**2)
    integral4 = np.mean(values**4)
    ok(abs(integral2-float(S)) < 2e-11, 'Parseval via exact-order grid quadrature')
    ok(abs(integral4-float(C)) < 2e-11, 'fourth moment via grid quadrature')
    ok(abs(np.max(values)-float(D)) < 2e-11, 'attained positive Fourier envelope')

# The dimension-one nu=1/2 example has a closed-form full spectral sum.
mp.mp.dps = 70
Z = mp.pi*mp.coth(mp.pi)
T2 = (mp.pi*mp.coth(mp.pi) + mp.pi**2/mp.sinh(mp.pi)**2)/2
for m in [100, 200, 400, 800, 1200]:
    T = Z - (1 + 2*sum((mp.mpf(1)/(1+k*k) for k in range(1,m+1)),mp.mpf('0')))
    S = T2 - (1 + 2*sum((mp.mpf(1)/(1+k*k)**2 for k in range(1,m+1)),mp.mpf('0')))
    ok(T > 0 and S > 0, 'untruncated positive infinite tails')
    ok(abs(m*T-2) < mp.mpf('0.11'), 'T_m ~ 2/m')
    ok(abs(m**3*S-mp.mpf(2)/3) < mp.mpf('0.015'), 'S_m ~ (2/3)/m^3')
    ok(abs(m*S/T**2-mp.mpf(1)/6) < mp.mpf('0.015'), 'critical sample ratio 1/6')

print(f'PASS: {checks} exact-rational and numerical check groups')
