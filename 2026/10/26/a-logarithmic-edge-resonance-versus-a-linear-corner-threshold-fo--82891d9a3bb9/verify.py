#!/usr/bin/env python3
"""Finite quadrature checks for an edge/corner Dirichlet square-lattice defect.

Requires Python 3 standard library only. Quadrature is a numerical sanity check,
not a rigorous enclosure or a substitute for the analytic spectral argument.
"""
from math import cos, pi, sqrt, log, isfinite


def edge(j, eps, n=60000):
    step = pi / n
    total = 0.0
    for q in range(n):
        y = (q + 0.5) * step
        z = eps + 4.0 - 2.0 * cos(y)
        total += (1.0 - cos(2.0 * j * y)) / sqrt((z - 2.0) * (z + 2.0))
    return total / n


def corner(a, b, eps, n=440, derivative=False):
    step = pi / n
    accum = 0.0
    for q in range(n):
        x = (q + 0.5) * step
        wx = 1 - cos(2 * a * x)
        c1 = 2 - 2 * cos(x)
        for z in range(n):
            y = (z + 0.5) * step
            omega = c1 + 2 - 2 * cos(y)
            numerator = wx * (1 - cos(2 * b * y))
            denom = omega + eps
            accum += numerator / (denom * denom if derivative else denom)
    return accum / (n * n)


def main():
    f_h = edge(1, 0.0)
    f_h_exact = 1 - 2 / pi
    assert abs(f_h - f_h_exact) < 2e-7, (f_h, f_h_exact)
    f_q = corner(1, 1, 0.0)
    b_q = corner(1, 1, 0.0, derivative=True)
    assert abs(f_q - 0.30234727368645) < 1e-5
    assert abs(b_q - 0.1366197724) < 1e-5
    dq = (f_q - corner(1, 1, 0.0001)) / 0.0001
    assert abs(dq - b_q) < 0.0001, (dq, b_q)
    for e in [0.0001, 0.00001]:
        edge_delta = (f_h - edge(1, e)) / (e * log(1 / e))
        assert isfinite(edge_delta) and 0.07 < edge_delta < 0.11
    print("NUMERICAL_CHECKS_OK")
    print("F_H(1) = %.12f, lambda_H = %.10f" % (f_h, 1 / f_h))
    print("F_Q(1,1) = %.12f, lambda_Q = %.10f" % (f_q, 1 / f_q))
    print("B_Q(1,1) = %.10f, near-critical slope = %.9f" % (b_q, f_q*f_q/b_q))
    print("The quadrature and asymptotic checks are finite, not certified bounds.")

if __name__ == "__main__":
    main()
