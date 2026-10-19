#!/usr/bin/env python3
"""Independent computational checks for the signed-equicorrelation cyclic Kaczmarz law.

Requires Python 3, NumPy, SciPy. All universal claims rely on a proof, not finite tests.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.optimize import brentq
from scipy.special import lambertw

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def root_x(n, alpha):
    def s(x):
        if x == 0:
            return 1.0
        z = math.expm1(x / n)
        return (math.expm1(x) - z) / ((n - 1) * z)
    return brentq(lambda x: s(x) - 1 / alpha, 0, 100, xtol=3e-13)


def limit_x(alpha):
    return -alpha - lambertw(-alpha * math.exp(-alpha), -1).real


# Exact rational Gauss--Seidel matrix and powers, independently of floating-point root formulas.
for n in range(2, 9):
    for alpha in (Fraction(1, 7), Fraction(1, 2), Fraction(4, 5)):
        beta = alpha / (n - 1)
        G = [[Fraction(1) if i == j else -beta for j in range(n)] for i in range(n)]
        B = [[Fraction(1) if i == j else (-beta if i > j else Fraction(0)) for j in range(n)] for i in range(n)]
        # Recurrence for entries of exact B^{-1}, with B=I-beta*lower-all-ones.
        invB = [[Fraction(1) if i == j else (beta * (1 + beta) ** (i - j - 1) if i > j else Fraction(0)) for j in range(n)] for i in range(n)]
        check(all(sum(B[i][k] * invB[k][j] for k in range(n)) == (i == j)
                  for i in range(n) for j in range(n)), 'inverse mismatch')
        U = [[beta if i < j else Fraction(0) for j in range(n)] for i in range(n)]
        T_exact = [[sum(invB[i][k] * U[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        T_float = np.array([[float(v) for v in row] for row in T_exact])
        x = root_x(n, float(alpha))
        t = math.exp(-x / n)
        eigvec = np.array([t ** i for i in range(n)])
        eigvalue = math.exp(-x)
        check(np.linalg.norm(T_float @ eigvec - eigvalue * eigvec) < 5e-11,
              'positive Perron vector identity')
        check(abs(max(abs(np.linalg.eigvals(T_float))) - eigvalue) < 1e-9,
              'spectral radius mismatch')
        check(np.linalg.eigvalsh(np.array([[float(v) for v in row] for row in G]))[0] > 0,
              'Gram not SPD')
        check(all(T_exact[i][j] > 0 for i in range(1, n) for j in range(1, n)),
              'positive principal block')
        check(all(T_exact[i][0] == 0 for i in range(n)), 'nonzero first column')
        # Independently reconstruct the whole sweep by exact coordinate corrections.
        for j in range(n):
            v = [Fraction(int(k == j)) for k in range(n)]
            for i in range(n):
                correction = sum(G[i][k] * v[k] for k in range(n))
                v[i] -= correction
            check(all(v[i] == T_exact[i][j] for i in range(n)),
                  'coordinate-sweep mismatch')

# Infinite-dimensional limit and sharp first finite-size correction.
for alpha in (0.035, 0.1, 0.25, 0.5, 0.75, 0.92):
    x = limit_x(alpha)
    I = math.expm1(x) / x
    E = (1 + math.exp(x)) / 2
    Ip = ((x - 1) * math.exp(x) + 1) / x ** 2
    coefficient = (E - I) / Ip
    check(abs(I - 1 / alpha) < 1e-10, 'Lambert root identity')
    check(coefficient > 0, 'finite-size coefficient must be positive')
    for n in (30, 100, 300, 1000):
        x_n = root_x(n, alpha)
        check(x_n > x, 'finite root should exceed limit')
        check(abs((n - 1) * (x_n - x) - coefficient) < 3 * coefficient / n,
              'finite-size asymptotic mismatch')

# Fixed-n sharp near-simplex behavior, also checking the second coefficient.
for n in (2, 3, 4, 7, 11, 20):
    second = (4 * n - 2) / (3 * n)
    for eps in (0.002, 0.001):
        lam = math.exp(-root_x(n, 1 - eps))
        rem = abs(lam - (1 - 2 * eps + second * eps ** 2))
        check(rem < 7 * eps ** 3, 'near-simplex second-order coefficient mismatch')

# Sparse/orthogonal asymptotic at the n=infinity end.
for alpha in (1e-3, 1e-4, 1e-5, 1e-6):
    lam = math.exp(-limit_x(alpha))
    check(abs(lam / (alpha / math.log(1 / alpha)) - 1) < 0.6,
          'near-orthogonality scaling order mismatch')

print('PASS', checks, 'exact rational, spectral, asymptotic and endpoint checks')
