#!/usr/bin/env python3
"""Exact finite checks for the 2x2 characteristic-polynomial count formula."""
from collections import Counter
from itertools import product


def valuation(a, p, m):
    modulus = p ** m
    a %= modulus
    if a == 0:
        return m
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v


def W(p, m, s):
    if s < m:
        return (s + 1) * (p - 1) * p ** (m - 1)
    return p ** (m - 1) * (m * (p - 1) + p)


def formula_sum(p, m, delta_disc):
    modulus = p ** m
    return sum(W(p, m, valuation(delta_disc - x * x, p, m)) for x in range(modulus))


def formula_closed(p, m, delta_disc):
    modulus = p ** m
    D = delta_disc % modulus
    v = valuation(D, p, m)
    if v == m:
        return W(p, m, m) + sum(
            (p - 1) * p ** (m - r - 1) * W(p, m, min(2 * r, m))
            for r in range(m)
        )
    if v % 2:
        h = v // 2
        return sum(
            (p - 1) * p ** (m - r - 1) * W(p, m, 2 * r)
            for r in range(h + 1)
        ) + p ** (m - h - 1) * W(p, m, v)
    h = v // 2
    k = m - 2 * h
    unit = (D // (p ** v)) % p
    is_square = pow(unit, (p - 1) // 2, p) == 1
    base = sum(
        (p - 1) * p ** (m - r - 1) * W(p, m, 2 * r)
        for r in range(h)
    )
    if not is_square:
        return base + p ** (m - h) * W(p, m, v)
    ans = base + (p - 2) * p ** (m - h - 1) * W(p, m, v)
    for j in range(1, k):
        ans += 2 * (p - 1) * p ** (m - h - j - 1) * W(p, m, v + j)
    ans += 2 * p ** h * W(p, m, m)
    return ans


def brute_distribution(p, m):
    mod = p ** m
    counts = Counter()
    for a, b, c, d in product(range(mod), repeat=4):
        tr = (a + d) % mod
        det = (a * d - b * c) % mod
        counts[(tr, det)] += 1
    return counts


def run_case(p, m):
    mod = p ** m
    counts = brute_distribution(p, m)
    checked = 0
    for t in range(mod):
        for det in range(mod):
            disc = (t * t - 4 * det) % mod
            expected = formula_sum(p, m, disc)
            closed = formula_closed(p, m, disc)
            observed = counts[(t, det)]
            assert expected == closed, (p, m, t, det, disc, expected, closed)
            assert observed == expected, (p, m, t, det, disc, observed, expected)
            checked += 1
    assert sum(counts.values()) == mod ** 4
    print(f"p={p}, m={m}: {checked} (trace,determinant) fibers verified; total={mod**4}; OK")


if __name__ == "__main__":
    for p, m in [(3, 2), (5, 2), (3, 3)]:
        run_case(p, m)
    print("VERIFY_OK")
