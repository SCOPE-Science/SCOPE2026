#!/usr/bin/env python3
"""Finite checks for the sharp equitable two-colour wild-number theorem.

Run with Python 3 standard library only: python verify.py
The exhaustive checks are finite corroboration, not an asymptotic proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, exp, log

EXPECTED = {
    4: {0: 12, 1: 8},
    5: {0: 192, 1: 60},
    6: {0: 5430, 1: 1005},
    7: {0: 321930, 1: 30765, 2: 21},
}


def components(n, edge_indices, edges):
    parent = list(range(n))
    size = [1] * n

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for index in edge_indices:
        u, v = edges[index]
        a, b = root(u), root(v)
        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
    return len({root(u) for u in range(n)})


def check_exhaustive(n):
    edges = list(combinations(range(n), 2))
    N, m = len(edges), len(edges) // 2
    all_indices = frozenset(range(N))
    histogram = Counter()
    total_isolates = 0
    checked = 0
    for subset in combinations(range(N), m):
        red = frozenset(subset)
        blue = all_indices.difference(red)
        w = (components(n, red, edges) - 1) + (components(n, blue, edges) - 1)
        histogram[w] += 1
        checked += 1
        for v in range(n):
            incidences = {j for j, (a, b) in enumerate(edges) if a == v or b == v}
            total_isolates += int(incidences.isdisjoint(red))
            total_isolates += int(incidences.isdisjoint(blue))
    assert checked == comb(N, m), (n, checked)
    assert histogram == EXPECTED[n], (n, histogram)
    q_red = Fraction(comb(N - n + 1, m), comb(N, m)) if N - n + 1 >= m else Fraction(0)
    q_blue = Fraction(comb(N - n + 1, N - m), comb(N, m)) if N - n + 1 >= N - m else Fraction(0)
    assert Fraction(total_isolates, checked) == n * (q_red + q_blue)
    return checked


def check_limit(n):
    N = n * (n - 1) // 2
    m = N // 2
    d = n - 1

    def q_log(a):
        return sum(log((a-j) / (N-j)) for j in range(d))

    p = n * (exp(q_log(m)) + exp(q_log(N-m)))
    main = (4 / exp(1)) * n * (2.0 ** (-n))
    return p / main


def main():
    cases = sum(check_exhaustive(n) for n in EXPECTED)
    ratio = [check_limit(n) for n in (16, 32, 64, 128, 256)]
    assert all(abs(z - 1) < 0.01 for z in ratio), ratio
    assert all(abs(ratio[i+1]-1) < abs(ratio[i]-1) for i in range(len(ratio)-1))
    print(f"VERIFY_OK exhaustive_colorings={cases} dimensions=4..7 exact_isolate_identities=4 numerical_ratio_cases=5")


if __name__ == '__main__':
    main()
