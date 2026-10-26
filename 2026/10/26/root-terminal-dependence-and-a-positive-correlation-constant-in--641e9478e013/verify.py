#!/usr/bin/env python3
"""Exact finite verification for the root-terminal dependence in Moran forests.

Run with Python 3 and its standard library: python verify.py.
The sample space is the product of uniform parent choices in the
increasing-label construction. Finite checks do not replace the proof.
"""
from fractions import Fraction as F
from itertools import product
from math import e, sqrt


def formulas(n):
    q = F(n - 2, n - 1)
    r = F(n - 3, n - 1)
    mean_r = F(n, 2)
    mean_l = sum((q ** (n - i) for i in range(1, n + 1)), F(0))
    vr = F(n * (n - 2), 6 * (n - 1))
    vl = sum((q ** (n - i) * (1 - q ** (n - i)) for i in range(1, n + 1)), F(0))
    vl += 2 * sum((q ** (j - i) * r ** (n - j)
                   - q ** (2 * n - i - j)
                   for i in range(1, n + 1) for j in range(i + 1, n + 1)), F(0))
    cov = sum((F(m * (m - 1), 2 * (n - 1) ** 2) * q ** (m - 1)
               for m in range(1, n)), F(0))
    delta = {j: sum((q ** (n - i - 1) for i in range(1, j)), F(0)) / (j - 1)
             for j in range(2, n)}
    return mean_r, mean_l, vr, vl, cov, delta


def exact_enumerate(n):
    options = [[u for u in range(1, n + 1) if u != j]
               for j in range(2, n + 1)]
    sum_r = sum_l = sum_rr = sum_ll = sum_rl = 0
    root_yes = {j: [0, 0] for j in range(2, n)}
    root_no = {j: [0, 0] for j in range(2, n)}
    total = 0
    for choices in product(*options):
        parent = {j: u for j, u in zip(range(2, n + 1), choices)}
        links = [(u, j) for j, u in parent.items() if u < j]
        roots = n - len(links)
        children = {u for u, _ in links}
        terminal = n - len(children)
        sum_r += roots
        sum_l += terminal
        sum_rr += roots * roots
        sum_ll += terminal * terminal
        sum_rl += roots * terminal
        for j in range(2, n):
            bucket = root_yes if parent[j] > j else root_no
            bucket[j][0] += 1
            bucket[j][1] += terminal
        total += 1
    m_r, m_l = F(sum_r, total), F(sum_l, total)
    vr = F(sum_rr, total) - m_r * m_r
    vl = F(sum_ll, total) - m_l * m_l
    cov = F(sum_rl, total) - m_r * m_l
    delta = {j: F(*root_yes[j][::-1]) - F(*root_no[j][::-1])
             for j in range(2, n)}
    return total, m_r, m_l, vr, vl, cov, delta


def main():
    for n in range(3, 8):
        total, *observed = exact_enumerate(n)
        expected = formulas(n)
        assert observed == list(expected), (n, observed, expected)
        d = list(expected[-1].values())
        assert all(d[k] < d[k + 1] for k in range(len(d) - 1))
        assert expected[-2] > 0
        print('EXHAUSTIVE_MORAN_PASS', n, 'configurations', total)
    for n in range(3, 121):
        mean_r, mean_l, vr, vl, cov, delta = formulas(n)
        assert vr > 0 and vl > 0 and cov > 0
        assert all(a < b for a, b in zip(list(delta.values()), list(delta.values())[1:]))
    print('EXACT_MOMENTS_AND_INFLUENCE_PASS n=3..120')
    limit_cov = 1 - 5 / (2 * e)
    limit_vl = 1 / e - 2 / (e * e)
    limit_corr = (2 * e - 5) * sqrt(6 / (e - 2)) / 2
    assert abs(limit_cov - 0.08030139707139416) < 1e-13
    assert abs(limit_vl - 0.09720887469821693) < 1e-13
    assert abs(limit_corr - 0.6308785600416852) < 1e-13
    print('ASYMPTOTIC_CONSTANTS_PASS')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
