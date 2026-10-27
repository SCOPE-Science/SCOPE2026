#!/usr/bin/env python3
"""Independent finite checks for distinct-part-size partition counting.

Run: python3 verify.py
All operations use exact integers except the displayed asymptotic comparison.
"""
from math import comb, factorial, log, pi


def exact_partition_counts(max_n, max_k):
    # Each size a is selected zero times or with a positive multiplicity.
    old = [[0] * (max_n + 1) for _ in range(max_k + 1)]
    old[0][0] = 1
    for a in range(1, max_n + 1):
        for k in range(max_k, 0, -1):
            tail = [0] * (max_n + 1)
            for n in range(a, max_n + 1):
                tail[n] = tail[n - a] + old[k - 1][n - a]
            for n in range(a, max_n + 1):
                old[k][n] += tail[n]
    return old


def divisor_data(max_n):
    d = [0] * (max_n + 1)
    sigma = [0] * (max_n + 1)
    triple = [0] * (max_n + 1)
    for a in range(1, max_n + 1):
        for n in range(a, max_n + 1, a):
            d[n] += 1
            sigma[n] += a
            v = n // a
            if v >= 3:
                triple[n] += comb(v - 1, 2)
    return d, sigma, triple


def convolution(a, b, max_n):
    out = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        if not a[i]:
            continue
        for j in range(1, max_n - i + 1):
            out[i + j] += a[i] * b[j]
    return out


def test_identity():
    nmax = 120
    p = exact_partition_counts(nmax, 3)
    d, sigma, t = divisor_data(nmax)
    b = [sigma[n] - d[n] for n in range(nmax + 1)]
    dd = convolution(d, d, nmax)
    ddd = convolution(dd, d, nmax)
    bd = convolution(b, d, nmax)
    for n in range(nmax + 1):
        assert 2 * p[2][n] == dd[n] - b[n], (2, n)
        assert 6 * p[3][n] == ddd[n] - 3 * bd[n] + 2 * t[n], (3, n)
    print('EXACT_COEFFICIENT_IDENTITIES_OK', nmax)


def test_cumulative_two():
    nmax = 100_000
    d, _, _ = divisor_data(nmax)
    pref = [0] * (nmax + 1)
    for n in range(1, nmax + 1):
        pref[n] = pref[n - 1] + d[n]
    gamma = 0.57721566490153286060651209
    for x in (1_000, 10_000, 100_000):
        ordered = sum(d[n] * pref[x - n] for n in range(1, x))
        collision = sum((x // a) * (x // a - 1) // 2 for a in range(1, x + 1))
        assert (ordered - collision) % 2 == 0
        exact = (ordered - collision) // 2
        H = 1.5
        H2 = 1.25
        z2 = pi * pi / 6
        a = 2 * gamma - H
        L = log(x)
        model = x * x / 4 * (L * L + 2 * a * L + a * a + H2 - 2 * z2)
        delta = (exact - model) / exact
        print('CUMULATIVE_K2', x, exact, 'model', format(model, '.2f'), 'relative_residual', format(delta, '.9g'))
        assert abs(delta) < 0.002


if __name__ == '__main__':
    test_identity()
    test_cumulative_two()
    print('VERIFY_OK')
