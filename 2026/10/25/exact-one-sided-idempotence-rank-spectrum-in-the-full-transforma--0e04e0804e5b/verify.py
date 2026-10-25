#!/usr/bin/env python3
"""Independent finite tests for a closed rank-triple count of idempotent products.

Only Python's standard library is used.  All maps are represented as value tuples.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial

def is_idempotent(f):
    return all(f[f[x]] == f[x] for x in range(len(f)))

def compose(e, f):
    # e after f; no semigroup library or normal-form code used.
    return tuple(e[f[x]] for x in range(len(e)))

def rank(f):
    return len(set(f))

def formula(n, r, s, t):
    if not (1 <= r <= n and 1 <= s <= n and
            1 <= t <= min(r, s) and r + s - t <= n):
        return 0
    m = n - r - s + t
    pref = Fraction(
        factorial(n) * (s ** (r-t)) * (t ** (s-t)),
        factorial(t) * factorial(r-t) * factorial(s-t))
    coef = sum((Fraction(comb(t, j) * ((r*s) ** (m-j)),
                         factorial(m-j))
                for j in range(min(t, m)+1)), Fraction(0))
    ans = pref * coef
    assert ans.denominator == 1
    return int(ans)

def brute(n):
    maps = [f for f in product(range(n), repeat=n) if is_idempotent(f)]
    found = Counter()
    for e in maps:
        er = rank(e)
        for f in maps:
            h = compose(e, f)
            if is_idempotent(h):
                found[er, rank(f), rank(h)] += 1
    return maps, found

def direct_root_choices(e, s, t):
    """Second count: select each possible set of f-roots, not f itself."""
    n = len(e)
    roots = set(e)
    fibers = {a: set() for a in roots}
    for x, a in enumerate(e):
        fibers[a].add(x)
    number = 0
    for B_tuple in combinations(range(n), s):
        B = set(B_tuple)
        occupied = [a for a in roots if B & fibers[a]]
        if len(occupied) != t:
            continue
        nonfixed_anchor_in_active = sum(a not in B for a in occupied)
        # These anchors must choose an f-root within their e-fiber.
        weight = 1
        for a in occupied:
            if a not in B:
                weight *= len(B & fibers[a])
        # All remaining non-f-root positions choose any of the s roots.
        free = n - s - nonfixed_anchor_in_active
        number += weight * s**free
    return number

def main():
    total_profile_tests = 0
    for n in range(1, 7):
        E, counts = brute(n)
        expected = {(r, s, t): formula(n, r, s, t)
                    for r in range(1, n+1)
                    for s in range(1, n+1)
                    for t in range(1, min(r, s)+1)}
        for key in set(counts) | set(expected):
            assert counts[key] == expected.get(key, 0), (n, key, counts[key], expected.get(key))
            total_profile_tests += 1
        assert sum(counts.values()) <= len(E)**2
        if n <= 4:
            for e in E:
                for s in range(1, n+1):
                    for t in range(1, min(rank(e), s)+1):
                        actual = sum(rank(f) == s and
                                     is_idempotent(compose(e, f)) and
                                     rank(compose(e, f)) == t for f in E)
                        predicted = direct_root_choices(e, s, t)
                        assert actual == predicted, (n, e, s, t, actual, predicted)
        print("n=%d idempotents=%d idempotent_products=%d rank_triples=%d"
              % (n, len(E), sum(counts.values()), len(counts)))
    for n in range(1, 15):
        for r in range(1, n+1):
            for s in range(1, n+1):
                for t in range(1, min(r,s)+1):
                    ans = formula(n, r, s, t)
                    assert (ans > 0) == (r+s-t <= n)
    print("VERIFY_OK_IDEMPOTENT_PRODUCT_RANK_TRIPLES", total_profile_tests)

if __name__ == "__main__":
    main()
