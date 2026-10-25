#!/usr/bin/env python3
"""Exact checks for the component–singleton covariance identity.

Python 3 standard library only. Finite checks supplement, not replace, the proof.
"""
from fractions import Fraction as F
from itertools import product
from math import prod


def hst(n, p):
    h = prod((1 - p / F(j) for j in range(1, n)), start=F(1))
    s = sum((1 / (F(j) - p) for j in range(1, n)), F(0))
    t = sum((1 / (F(j) - p) ** 2 for j in range(1, n)), F(0))
    return h, s, t


def closed_form(n, p):
    assert n >= 1 and F(0) < p < F(1)
    q = 1 - p
    h, s, t = hst(n, p)
    b = 2 * p * p / (1 + p)
    bp = 2 * p * (p + 2) / (1 + p) ** 2
    c = p * q * (2 * p ** 4 + 5 * p ** 3 + 3 * p ** 2 - p + 1) / (1 + p) ** 3
    return c * n - 2 * p * p * q + h * (
        p * q * (1 + 2 * p) - c + p * p * q * (
            (b - bp) * s + b * (s * s - t) / 2
        )
    )


def first_moment_isolates(n, p):
    h, _, _ = hst(n, p)
    return n * p * (1 - p) / (1 + p) + 2 * p * p * h / (1 + p)


def covariance_recurrence(n, p):
    q = 1 - p
    value = p * q
    for m in range(1, n):
        h, s, _ = hst(m, p)
        a = p * q / (1 + p)
        b = 2 * p * p / (1 + p)
        ap = (1 - 2 * p - p * p) / (1 + p) ** 2
        bp = 2 * p * (p + 2) / (1 + p) ** 2
        isol = a * m + b * h
        isol_derivative = ap * m + h * (bp - b * s)
        cov_m_k = p * q * (m - 2 * p * (m - 1))
        cov_m_i = p * q * isol_derivative
        value = ((1 - p / m) * value + p * q * (1 - p * q)
                 - p / m * (cov_m_k + cov_m_i) + p * p * q / m * isol)
    return value


def exhaustive_moments(n, p):
    """Enumerate all (n-1)! recursive trees and 2^n open/closed patterns."""
    q = 1 - p
    count_trees = prod(range(1, n), start=1)
    expected_k = expected_i = expected_ki = F(0)
    for parents in product(*(range(j) for j in range(1, n))):
        # With zero-based labels, vertex v>=1 attaches to parent[v-1].
        edges = [(v, u) for v, u in enumerate(parents, start=1)]
        for mask in range(1 << n):
            retained = mask.bit_count()
            weight = p ** retained * q ** (n - retained) / count_trees
            retained_edges = sum(
                bool(mask & (1 << u)) and bool(mask & (1 << v))
                for v, u in edges
            )
            k = retained - retained_edges
            incident_retained = [0] * n
            for v, u in edges:
                if mask & (1 << u) and mask & (1 << v):
                    incident_retained[u] += 1
                    incident_retained[v] += 1
            i = sum(bool(mask & (1 << v)) and incident_retained[v] == 0
                    for v in range(n))
            expected_k += weight * k
            expected_i += weight * i
            expected_ki += weight * k * i
    return expected_k, expected_i, expected_ki - expected_k * expected_i


def main():
    nchecks = 0
    for p in (F(1, 4), F(1, 2), F(3, 4)):
        for n in range(1, 8):
            k, i, cov = exhaustive_moments(n, p)
            assert k == n * p - (n - 1) * p * p
            assert i == first_moment_isolates(n, p)
            assert cov == closed_form(n, p)
            assert cov == covariance_recurrence(n, p)
            nchecks += 4
        for n in range(8, 101):
            assert closed_form(n, p) == covariance_recurrence(n, p)
            nchecks += 1
        assert closed_form(2, p) == 2 * p * (1 - p) ** 3
        nchecks += 1
    assert closed_form(1, F(1, 2)) == F(1, 4)
    nchecks += 1
    print(f"PASS: {nchecks} exact-rational assertions; tree/site enumeration through n=7")


if __name__ == '__main__':
    main()
