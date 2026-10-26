#!/usr/bin/env python3
"""Finite exhaustive checks for rank-refined mutually annihilating nilpotent partial injections.

Runs with Python 3 standard library only. No research workflow or environment dependencies.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb, factorial


def maps(n):
    yield (-1,) * n
    for r in range(1, n + 1):
        for domain in combinations(range(n), r):
            for targets in permutations(range(n), r):
                a = [-1] * n
                for i, j in zip(domain, targets):
                    a[i] = j
                yield tuple(a)


def nilpotent(a):
    n = len(a)
    for i in range(n):
        x = i
        for _ in range(n):
            if x == -1:
                break
            x = a[x]
        if x != -1:
            return False
    return True


def composition_zero(a, b):
    return all(a[b[i]] == -1 for i in range(len(b)) if b[i] != -1)


def expected(n, r, s):
    h = n - r - s
    if h < 0 or r >= n or s >= n:
        return 0
    if n == 1:
        return int(r == 0 and s == 0)
    numerator = factorial(n) * factorial(n - 2) * (h * (n - 1) + r * s)
    denominator = factorial(r) * factorial(s) * factorial(h) ** 2
    assert numerator % denominator == 0
    return numerator // denominator


def main():
    totals = [1, 7, 55, 565, 7141, 106891]
    for n in range(1, 7):
        nils = [a for a in maps(n) if nilpotent(a)]
        records = []
        for a in nils:
            d = sum(x >= 0 for x in a)
            dom = sum(1 << i for i, x in enumerate(a) if x != -1)
            img = sum(1 << x for x in a if x != -1)
            records.append((a, d, dom, img))
        actual = Counter()
        for a, r, da, ia in records:
            for b, s, db, ib in records:
                # Independent direct-composition check up through n=5.
                if n <= 5:
                    good = composition_zero(a, b) and composition_zero(b, a)
                else:
                    good = not (da & ib or db & ia)
                if good:
                    actual[r, s] += 1
        for r in range(n):
            for s in range(n):
                want = expected(n, r, s)
                assert actual[r, s] == want, (n, r, s, actual[r, s], want)
                assert want == expected(n, s, r)
        assert sum(actual.values()) == totals[n - 1]
        print(f"n={n}; nilpotents={len(nils)}; ordered annihilating pairs={sum(actual.values())}; checked all {n*n} rank cells")
    print("VERIFY_OK_NILPOTENT_MUTUAL_ZERO_RANKS")

if __name__ == "__main__":
    main()
