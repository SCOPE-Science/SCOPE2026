#!/usr/bin/env python3
"""Self-contained exact finite checks for a Hoppe-tree root/leaf joint limit.

These checks validate algebraic finite identities and numerical Riemann limits;
they do not replace the analytic martingale central limit theorem.
"""
from fractions import Fraction
from itertools import product
from math import log1p


def exact_enumeration(n, theta):
    # Vertex 2 attaches to the root. Node k>=3 selects parent 1,...,k-1.
    m_r = m_l = m_rl = Fraction(0)
    mass = Fraction(0)
    for choices in product(*(range(1, k) for k in range(3, n + 1))):
        degrees = [0] * (n + 1)
        degrees[1] = 1
        prob = Fraction(1)
        for k, parent in enumerate(choices, start=3):
            prob *= (theta if parent == 1 else 1) / (theta + k - 2)
            degrees[parent] += 1
        r = degrees[1]
        l = sum(degrees[j] == 0 for j in range(2, n + 1))
        mass += prob
        m_r += prob * r
        m_l += prob * l
        m_rl += prob * r * l
    assert mass == 1, (n, theta, mass)
    exact_mu = Fraction(n - 1, 2) + theta * (n - 1) / (2 * (theta + n - 2))
    exact_rmean = 1 + sum((theta / (theta + j - 1) for j in range(2, n)))
    exact_cov = theta * (n - 1) * (n - 2) / (2 * (theta + n - 2) ** 2)
    assert m_l == exact_mu, (n, theta, m_l, exact_mu)
    assert m_r == exact_rmean, (n, theta, m_r, exact_rmean)
    assert m_rl - m_r * m_l == exact_cov, (n, theta, m_rl - m_r * m_l, exact_cov)
    return 1


def u(c):
    return c * (log1p(1 / c) - 1 / (c + 1))


def v(c):
    return (6 * c * c + 4 * c + 1) / (12 * (c + 1) ** 3)


def kappa(c):
    return c / (2 * (c + 1) ** 2)


def grid_covariances(n, c):
    theta = c * n
    accum_r = accum_l = accum_rl = 0.0
    for j in range(2, n):
        den = theta + j - 1
        p = theta / den
        mu = (j - 1) / 2 + theta * (j - 1) / (2 * (theta + j - 2))
        q = mu / den
        b = den / (theta + n - 2)
        accum_r += p * (1 - p)
        accum_l += b * b * q * (1 - q)
        accum_rl += b * p * q
    return (accum_r / n, accum_l / n, accum_rl / n)


def main():
    total = 0
    for theta in [Fraction(1, 3), Fraction(1), Fraction(5, 2)]:
        for n in range(2, 8):
            total += exact_enumeration(n, theta)
    assert total == 18
    for n in [1000, 10000]:
        for c in [0.25, 1.0, 3.0]:
            r, l, rl = grid_covariances(n, c)
            bound = 0.003 if n == 1000 else 0.0005
            assert abs(r - u(c)) < bound, (n, c, 'root', r, u(c))
            assert abs(l - v(c)) < bound, (n, c, 'leaf', l, v(c))
            assert abs(rl - kappa(c)) < bound, (n, c, 'cross', rl, kappa(c))
            assert u(c) * v(c) > kappa(c)**2
    print('VERIFY_OK: 18 exact enumerations and 6 finite-to-asymptotic covariance checks')

if __name__ == '__main__':
    main()
