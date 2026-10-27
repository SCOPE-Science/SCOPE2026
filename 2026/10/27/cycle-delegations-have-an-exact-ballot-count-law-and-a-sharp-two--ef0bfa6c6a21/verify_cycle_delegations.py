"""Exact independent finite-case verification for the cycle delegation theorem.

Usage: python verify_cycle_delegations.py
Only the Python standard library is required.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import prod


def gap_lengths(n, gurus):
    return tuple((gurus[(j + 1) % len(gurus)] - gurus[j] - 1) % n
                 for j in range(len(gurus)))


def direct_distribution(n, gurus):
    """Brute-force all neighboring choices, reject actual directed cycles."""
    guru_set = set(gurus)
    others = [i for i in range(n) if i not in guru_set]
    counts = Counter()
    for turns in product((-1, 1), repeat=len(others)):
        out = {v: (v + turn) % n for v, turn in zip(others, turns)}
        weights = {v: 1 for v in gurus}
        good = True
        for v in others:
            path = set()
            u = v
            while u not in guru_set:
                if u in path:
                    good = False
                    break
                path.add(u)
                u = out[u]
            if not good:
                break
            weights[u] += 1
        if good:
            counts[tuple(weights[v] for v in gurus)] += 1
    return counts


def factor_distribution(n, gurus):
    """Independent split variables, with their orientation explicit."""
    lengths = gap_lengths(n, gurus)
    k = len(gurus)
    counts = Counter()
    for cutpoints in product(*(range(m + 1) for m in lengths)):
        weights = [1 + lengths[(j - 1) % k]
                   + cutpoints[j] - cutpoints[(j - 1) % k]
                   for j in range(k)]
        counts[tuple(weights)] += 1
    return counts


def check():
    tests = 0
    examined = 0
    for n in range(3, 11):
        for k in range(2, min(n, 5) + 1):
            for gurus in combinations(range(n), k):
                a = direct_distribution(n, gurus)
                b = factor_distribution(n, gurus)
                assert a == b, (n, gurus, a, b)
                gaps = gap_lengths(n, gurus)
                assert sum(a.values()) == prod(m + 1 for m in gaps)
                assert all(sum(w) == n for w in a)
                size = sum(a.values())
                means = [sum((Fraction(c * w[j], size) for w, c in a.items()), Fraction(0))
                         for j in range(k)]
                for j in range(k):
                    m = 1 + Fraction(gaps[j-1] + gaps[j], 2)
                    assert means[j] == m
                # Check each coalition's exact cut-variance identity.
                for mask in range(1, (1 << k) - 1):
                    s = [j for j in range(k) if mask & (1 << j)]
                    ex = sum(Fraction(c * sum(w[j] for j in s), size)
                             for w, c in a.items())
                    v = sum(Fraction(c * sum(w[j] for j in s)**2, size)
                            for w, c in a.items()) - ex*ex
                    bound = sum(Fraction(m * (m + 2), 12)
                                for j, m in enumerate(gaps)
                                if ((mask >> j) & 1) != ((mask >> ((j+1) % k)) & 1))
                    assert v == bound, (n, gurus, mask, v, bound)
                # Independent coefficient identity for every nontrivial A-coalition.
                for mask in range(1, (1 << k) - 1):
                    A = {j for j in range(k) if mask & (1 << j)}
                    actual = Counter()
                    for w, multiplicity in a.items():
                        actual[sum(w[j] for j in A)] += multiplicity
                    poly = [1]
                    offset = len(A)
                    for j, m in enumerate(gaps):
                        left, right = (j in A), ((j + 1) % k in A)
                        if left and right:
                            offset += m
                            poly = [c * (m + 1) for c in poly]
                        elif not left and not right:
                            poly = [c * (m + 1) for c in poly]
                        else:
                            nxt = [0] * (len(poly) + m)
                            for degree, c in enumerate(poly):
                                for d in range(m + 1):
                                    nxt[degree + d] += c
                            poly = nxt
                    expected = Counter({offset + i: c for i, c in enumerate(poly) if c})
                    assert actual == expected, (n, gurus, mask, actual, expected)
                    assert sum(c for count, c in actual.items() if count > n / 2) == sum(
                        c for count, c in expected.items() if 2*count > n)
                if k == 2:
                    m0, m1 = gaps
                    ties = sum(c for w, c in a.items() if w[0] == w[1])
                    expected = (min(m0, m1) + 1) if n % 2 == 0 else 0
                    assert ties == expected
                    if n % 2 == 0:
                        assert Fraction(ties, size) == Fraction(1, max(m0, m1) + 1)
                tests += 1
                examined += size
    print(f'PASS {tests} cycle/guru configurations, {examined} legal delegations; exact laws, cut variances, tie formula.')


if __name__ == '__main__':
    check()
