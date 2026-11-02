#!/usr/bin/env python3
"""Reproducible finite checks for the operator-valued Drury–Arveson Bohr profile.

Only exact finite combinatorics and numerical examples are checked here;
the unrestricted theorem requires the accompanying analytic proof.
"""
import itertools
import math
from fractions import Fraction


def multiindices(d, n):
    if d == 1:
        yield (n,)
    else:
        for a in range(n + 1):
            for tail in multiindices(d - 1, n - a):
                yield (a,) + tail


def weight_squared(alpha, beta):
    n, m = sum(alpha), sum(beta)
    num = math.prod(math.comb(a + b, a) for a, b in zip(alpha, beta))
    den = math.comb(n + m, n)
    return Fraction(num, den)


def profile(z, max_degree=80):
    d = len(z)
    result = 0.0
    for n in range(1, max_degree + 1):
        for alpha in multiindices(d, n):
            multinomial = math.factorial(n) // math.prod(math.factorial(a) for a in alpha)
            result += math.sqrt(multinomial) * math.prod(abs(v) ** a for v, a in zip(z, alpha))
    return result


def main():
    checks = 0
    for d in range(1, 5):
        for n in range(1, 7):
            for alpha in multiindices(d, n):
                assert weight_squared(alpha, (0,) * d) == 1
                checks += 1
                for m in range(0, 7):
                    for beta in multiindices(d, m):
                        assert weight_squared(alpha, beta) <= 1, (alpha, beta)
                        checks += 1
    # A genuinely 2-by-2 operator-valued contractive Schur polynomial:
    # F(w) = diag(w,w^2); its coefficient majorant exceeds one within |w|<1/sqrt(2).
    radius = Fraction(2, 3)
    assert radius * radius < Fraction(1, 2)
    assert radius + radius * radius == Fraction(10, 9)
    checks += 2
    # Exact scalar-in-one-variable operator-valued profile and its threshold.
    for r_num in range(1, 20):
        r = Fraction(r_num, 20)
        assert (r / (1-r) <= 1) == (r <= Fraction(1, 2))
        checks += 1
    # Same Euclidean radius but distinct Bohr behavior in dimension two.
    r = 0.4
    axial = r/(1-r)
    balanced = profile([r/math.sqrt(2)]*2, 8)
    assert axial < 1 < balanced
    assert profile([r/math.sqrt(2)]*2, 4) > 1
    checks += 2
    # Arbitrarily small-norm finite-support infinite-dimensional obstructions.
    for r in [0.02, 0.08, 0.15, 0.33]:
        n = math.floor(1/r**2) + 2
        assert r * math.sqrt(n) > 1
        checks += 1
    print(f'PASS: {checks} supplementary finite checks')
    print(f'Exact 2x2 disk witness: r=2/3, majorant=10/9, r^2<1/2')
    print(f'Dimension-two radial contrast r=2/5: axis={axial:.12f}; balanced partial degree 8={balanced:.12f}')


if __name__ == '__main__':
    main()
