#!/usr/bin/env python3
"""
Numerical checks for the second-variation analysis of the Coronel-Huancas
power-exponential product inequality.

The theorem in RESULT.md is analytic; these computations are supplementary.
"""
import mpmath as mp

mp.mp.dps = 80
E = mp.e
T = mp.e**(-2)

def deficit(n, r, eps):
    xs = [T + eps] + [T] * (n - 1)
    product = mp.fprod(xs)
    lhs = n * mp.fprod([x ** (r * x) for x in xs])
    rhs = mp.fsum([product ** (r * x) for x in xs])
    return lhs - rhs

def quadratic_coefficient(n, r):
    # y=(1,0,...,0), so n*sum(y_i^2)-(sum y_i)^2 = n-1.
    return mp.e**(-2*r*n/E**2) * r * (E**2 - 2*n*r) * (n - 1)

def critical_cubic_coefficient(n):
    return -(n - 1) * (n - 2) * E**5 / (12 * n**2)

print("r=1: comparison of D/eps^2 with the predicted quadratic coefficient")
for n in [2, 3, 4, 5, 8]:
    c = quadratic_coefficient(n, mp.mpf(1))
    d = deficit(n, mp.mpf(1), mp.mpf("1e-5")) / mp.mpf("1e-10")
    print(n, mp.nstr(d, 24), mp.nstr(c, 24))

print("\nExplicit n=4 counterexample at r=1, eps=1e-3")
d4 = deficit(4, mp.mpf(1), mp.mpf("1e-3"))
print(mp.nstr(d4, 40))
assert d4 < 0

print("\nr=e: negative deficits for n=2,...,6")
for n in range(2, 7):
    d = deficit(n, E, mp.mpf("1e-4"))
    print(n, mp.nstr(d, 30))
    assert d < 0

print("\nCritical r=e^2/(2n): comparison of D/eps^3 with predicted cubic coefficient")
for n in [3, 4, 5, 8]:
    r0 = E**2 / (2*n)
    eps = mp.mpf("1e-6")
    d = deficit(n, r0, eps) / eps**3
    c = critical_cubic_coefficient(n)
    print(n, mp.nstr(d, 24), mp.nstr(c, 24))

print("\nall checks passed")
