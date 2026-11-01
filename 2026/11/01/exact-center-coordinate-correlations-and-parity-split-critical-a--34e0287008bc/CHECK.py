#!/usr/bin/env python3
"""Exact finite checks for stationary center-coordinate correlations of balanced heterochaos baker maps.

Only Python's standard library is required. Finite tests support, but do not replace,
the ballot/reflection and singularity arguments in the accompanying proof.
"""
from fractions import Fraction as F
from math import comb


def walk_cov(m, n):
    out = F(0)
    for r in range(n % 2, n + 1, 2):
        p = F(comb(n, (n + r) // 2), 2**n)
        q = F(comb(n, (n + r + 2) // 2), 2**n) if r + 2 <= n else F(0)
        out += F(r + 1, m**r) * (p - q)
    return out / 12


def transfer_step(m, prev):
    """Apply the annealed Koopman map to piecewise-affine functions exactly."""
    size = len(prev)
    next_terms = []
    for j in range(m * size):
        a, b = F(0), F(0)
        for digit in range(m):
            idx = 0 if size == 1 else digit * (size // m) + j // (m*m)
            old_a, old_b = prev[idx]
            a += old_a / (2 * m * m)
            b += (old_a * F(digit, m) + old_b) / (2 * m)
        old_a, old_b = prev[j % size]
        a += old_a * F(m, 2)
        b += (old_b - old_a * (j // size)) / 2
        next_terms.append((a, b))
    return next_terms


def transfer_cov(terms):
    """Integrate (y-1/2)*h(y) over each cell without quadrature."""
    size = len(terms)
    total = F(0)
    for j, (a, b) in enumerate(terms):
        left, right = F(j, size), F(j + 1, size)
        total += a * (right**3-left**3) / 3
        total += (b-a/2) * (right**2-left**2) / 2
        total -= b * (right-left) / 2
    return total


def formal_cov(m, length):
    """Coefficient expansion of G(z)=(1+t(z)^2)/(12*(1-t(z)/m)^2)."""
    t = [F(0) for _ in range(length)]
    for n in range(1, length):
        t[n] = (F(1) if n == 1 else F(0)) / 2
        t[n] += sum((t[i]*t[n-1-i] for i in range(1, n)), F(0)) / 2
    t2 = [sum((t[j]*t[n-j] for j in range(n+1)), F(0)) for n in range(length)]
    inv = [F(1)] + [F(0) for _ in range(length-1)]
    for n in range(1, length):
        inv[n] = sum((t[j]*inv[n-j]/m for j in range(1,n+1)),F(0))
    inv2 = [sum((inv[j]*inv[n-j] for j in range(n+1)), F(0)) for n in range(length)]
    return [(inv2[n]+sum((t2[j]*inv2[n-j] for j in range(n+1)),F(0)))/12 for n in range(length)]


def main():
    total_checks = 0
    for m, max_n in [(2, 8), (3, 5), (4, 4), (5, 3)]:
        terms = [(F(1), F(-1,2))]
        coeffs = formal_cov(m, max_n+1)
        for n in range(max_n+1):
            via_walk = walk_cov(m, n)
            via_transfer = transfer_cov(terms)
            via_series = coeffs[n]
            assert via_walk == via_transfer == via_series, (m,n,via_walk,via_transfer,via_series)
            total_checks += 1
            if n < max_n:
                terms = transfer_step(m, terms)
        assert coeffs[0] == F(1,12)
        assert coeffs[1] == F(1,12*m)
    print(f'PASS: {total_checks} exact-rational triple-method covariance comparisons')
    print('PASS: all first- and zero-lag normalization checks')

if __name__ == '__main__':
    main()
