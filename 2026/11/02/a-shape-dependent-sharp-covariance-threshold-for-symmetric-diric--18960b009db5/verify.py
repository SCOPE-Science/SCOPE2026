#!/usr/bin/env python3
"""Exact finite checks for Dirichlet exceedance--convex-score dependence.

The mathematical proof, rather than finite checks, covers all real shape
parameters and smooth strictly convex scores. Requires Python 3 stdlib only.
"""
from fractions import Fraction as F
from math import comb, factorial


def rising(a, k):
    ans = 1
    for j in range(k):
        ans *= a + j
    return ans


def beta_tail_moment(a, b, k, t):
    """E[X**k * 1{X > t}], X~Beta(a,b); integer a,b >= 1."""
    normalizer = F(factorial(a + b - 1), factorial(a - 1) * factorial(b - 1))
    return normalizer * sum((F((-1)**j * comb(b - 1, j), a + k + j)
                             * (1 - t ** (a + k + j)) for j in range(b)), F(0))


def direct_cov(n, alpha, q, t):
    a = alpha
    b = (n - 1) * a
    total = n * a
    sibling_moment = F(rising(a, q), rising(b, q))
    mean_q = n * F(rising(a, q), rising(total, q))
    # E[Q_q | X_1=s] = s**q + (n-1)*sibling_moment*(1-s)**q.
    p = beta_tail_moment(a, b, 0, t)
    val = beta_tail_moment(a, b, q, t) - mean_q * p
    for j in range(q + 1):
        val += (n - 1) * sibling_moment * (-1)**j * comb(q, j) * beta_tail_moment(a, b, j, t)
    return n * val


def closed_quadratic(n, alpha, t):
    a = alpha
    b = (n - 1) * a
    total = n * a
    inv_beta = F(factorial(total - 1), factorial(a - 1) * factorial(b - 1))
    return (n * inv_beta * t**a * (1 - t)**b
            * F((total + 2) * t - (a + 1), (b + 1) * (total + 1)))


def run():
    checks = 0
    for n in range(2, 10):
        for a in range(1, 6):
            root = F(a + 1, n * a + 2)
            assert direct_cov(n, a, 2, root) == 0
            assert direct_cov(n, a, 2, root / 2) < 0
            assert direct_cov(n, a, 2, (root + 1) / 2) > 0
            checks += 3
            for j in range(1, 20):
                t = F(j, 20)
                assert direct_cov(n, a, 2, t) == closed_quadratic(n, a, t), (n, a, t)
                checks += 1
    # Separate polynomial statistics (not used to prove the all-score theorem).
    for q in (3, 4, 5):
        for n in range(2, 9):
            for a in range(1, 5):
                signs = []
                for j in range(1, 40):
                    v = direct_cov(n, a, q, F(j, 40))
                    signs.append((v > 0) - (v < 0))
                    checks += 1
                seen_positive = False
                for sign in signs:
                    if sign > 0:
                        seen_positive = True
                    if seen_positive:
                        assert sign >= 0
    return checks


if __name__ == '__main__':
    print(f'PASS: {run()} exact Fraction comparisons')
