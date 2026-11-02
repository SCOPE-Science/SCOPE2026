#!/usr/bin/env python3
"""Exact-arithmetic checks for a source-anchored complete-graph copying model."""
from fractions import Fraction
from math import prod


def forward_cdf(n, z, horizon):
    # State k = number of non-source agents holding the wrong opinion.
    m = n - z
    dist = [Fraction(0)] * (m + 1)
    dist[m] = Fraction(1)
    cdf = [dist[0]]
    for _ in range(horizon):
        new = [Fraction(0)] * (m + 1)
        for k, q in enumerate(dist):
            if not q:
                continue
            down = Fraction(k * (n - k), n * n) if k else Fraction(0)
            up = Fraction(k * (m - k), n * n) if k < m else Fraction(0)
            new[k] += q * (1 - down - up)
            if k:
                new[k - 1] += q * down
            if k < m:
                new[k + 1] += q * up
        assert sum(new) == 1
        dist = new
        cdf.append(dist[0])
    return cdf


def geometric_sum_cdf(n, z, horizon):
    m = n - z
    pmf = [Fraction(0)] * (horizon + 1)
    pmf[0] = Fraction(1)
    for j in range(1, m + 1):
        p = Fraction(j * (j + z - 1), n * n)
        geom = [Fraction(0)] * (horizon + 1)
        for t in range(1, horizon + 1):
            geom[t] = p * (1 - p) ** (t - 1)
        nxt = [Fraction(0)] * (horizon + 1)
        for t in range(horizon + 1):
            if not pmf[t]:
                continue
            for d in range(1, horizon - t + 1):
                nxt[t + d] += pmf[t] * geom[d]
        pmf = nxt
    return [sum(pmf[:t + 1]) for t in range(horizon + 1)]


def survival_spectral(n, z, t):
    m = n - z
    rates = [Fraction(j * (j + z - 1), n * n) for j in range(1, m + 1)]
    ans = Fraction(0)
    for i, p in enumerate(rates):
        coef = prod((q / (q - p) for k, q in enumerate(rates) if k != i), start=Fraction(1))
        ans += coef * (1 - p) ** t
    return ans


def run():
    cases = 0
    for n in range(2, 12):
        for z in range(1, n):
            horizon = 13
            left = forward_cdf(n, z, horizon)
            right = geometric_sum_cdf(n, z, horizon)
            assert left == right, (n, z)
            for t in range(horizon + 1):
                assert 1 - left[t] == survival_spectral(n, z, t), (n, z, t)
                cases += 1
            m = n - z
            slow_coefficient = prod((Fraction(j * (j + z - 1), (j-1) * (j+z)) for j in range(2, m+1)), start=Fraction(1))
            assert slow_coefficient == Fraction(m * (z+1), n)
            assert sum(Fraction(n*n, j*(j+z-1)) for j in range(1,m+1)) > 0
    assert cases == 770
    print('PASS', cases, 'exact rational CDF/survival comparisons across 55 n,z pairs, plus leading-tail coefficients')

if __name__ == '__main__':
    run()
