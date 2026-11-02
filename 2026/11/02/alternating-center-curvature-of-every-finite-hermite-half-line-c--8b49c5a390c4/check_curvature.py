#!/usr/bin/env python3
"""Reproducible finite checks for a Hermite half-line variance curvature identity.

Requires Python >=3.9; optional scipy for independent Gaussian quadrature.
The theorem for all positive integers rests on the written induction, not these tests.
"""
from fractions import Fraction
from math import comb, pi, sqrt


def c(k):
    return Fraction(comb(2 * k, k), 4 ** k)


def closed_coeff(q):
    m = (q + 1) // 2
    return (-1 if q % 2 else 1) * sum((c(k) ** 2 for k in range(m)), Fraction())


def direct_coeff(q):
    # V''_q(0) = (2/pi)*direct_coeff(q), from the boundary
    # Wronskian formula and exact Hermite values at zero.
    evens, odds = (q + 1) // 2, q // 2
    coupling = sum((Fraction(2 * (2 * i + 1), 2 * i - 2 * k + 1)
                    * c(i) * c(k)
                    for i in range(odds) for k in range(evens)), Fraction())
    baseline = sum((c(k) for k in range(evens)), Fraction()) ** 2
    return coupling - baseline


def check_exact():
    count = 0
    for m in range(1, 81):
        s = sum((c(k) for k in range(m)), Fraction())
        h = sum((c(k) ** 2 for k in range(m)), Fraction())
        r = sum((c(k) / (2 * m - 2 * k - 1) for k in range(m)), Fraction())
        assert s == 2 * m * c(m)
        assert s * r == h
        count += 2
    for q in range(1, 101):
        assert direct_coeff(q) == closed_coeff(q)
        count += 1
    return count


def check_quadrature():
    try:
        import numpy as np
        from scipy.integrate import quad
        from scipy.special import eval_hermite, gammaln
    except ImportError:
        return 'scipy not installed: numerical quadrature skipped'

    def h(j, x):
        return float(eval_hermite(j, x) * np.exp(-x * x / 2 - (j * np.log(2) + gammaln(j + 1) + .5 * np.log(np.pi)) / 2))

    # Independently evaluate V''=-2(u'u)^T B correction -2||u||^4,
    # with B=I-2 A(0) and A(0) obtained by numerical integration.
    count = 0
    for q in range(1, 17):
        u = np.array([h(j, 0) for j in range(q)])
        up = np.array([sqrt(2 * j) * h(j - 1, 0) if j else 0.0 for j in range(q)])
        A = np.array([[quad(lambda x: h(i, x) * h(j, x), 0., 13., epsabs=1e-12, limit=300)[0]
                       for j in range(q)] for i in range(q)])
        val = -2.0 * float(up @ (np.eye(q) - 2 * A) @ u) - 2 * float(u @ u) ** 2
        exact = 2.0 / pi * float(closed_coeff(q))
        assert abs(val - exact) < 5e-8, (q, val, exact)
        count += 1
    return f'{count} independent numerical Hermite-integral comparisons passed'


if __name__ == '__main__':
    n = check_exact()
    print(f'{n} exact rational checks passed')
    print(check_quadrature())
