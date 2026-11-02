#!/usr/bin/env python3
"""Finite independent checks of zero-sum elliptic matroid symmetries.

Uses only the Python standard library. The general theorem is proved
mathematically; exhaustive finite tests are supplementary evidence.
"""
from itertools import combinations
from math import gcd


def triples(n):
    return [t for t in combinations(range(n), 3) if sum(t) % n == 0]


def full_automorphism_count(n):
    """Exhaustively enumerate all zero-sum-triple-preserving permutations.

    Backtracking maintains a partial injection. Triangle incidence and
    nonincidence are checked when each triple becomes completely assigned.
    Each optional degree filter and forced image is logically necessary.
    """
    inc = [[] for _ in range(n)]
    for t in triples(n):
        for v in t:
            inc[v].append(t)
    degree = [len(t) for t in inc]
    by_degree = {d: {j for j in range(n) if degree[j] == d}
                 for d in set(degree)}
    count = 0

    def search(mapping, used):
        nonlocal count
        if len(mapping) == n:
            count += 1
            return
        best = None
        for v in range(n):
            if v in mapping:
                continue
            candidates = by_degree[degree[v]] - used
            for t in inc[v]:
                a, b = (w for w in t if w != v)
                if a in mapping and b in mapping:
                    forced = (-mapping[a] - mapping[b]) % n
                    candidates = {forced} if forced in candidates else set()
                    break
            if not candidates:
                return
            if best is None or len(candidates) < len(best[1]):
                best = (v, candidates)
        v, candidates = best
        for c in sorted(candidates):
            valid = True
            for t in inc[v]:
                if all(a == v or a in mapping for a in t):
                    if (c + sum(mapping[a] for a in t if a != v)) % n:
                        valid = False
                        break
            if valid:
                for i, j in combinations(mapping, 2):
                    # A basis triple must not become a nonbasis triple.
                    if (v + i + j) % n and (c + mapping[i] + mapping[j]) % n == 0:
                        valid = False
                        break
            if valid:
                mapping[v] = c
                search(mapping, used | {c})
                del mapping[v]

    search({}, set())
    return count


def affine_permutations(n):
    return {tuple((a * i + b) % n for i in range(n))
            for a in range(n) if gcd(a, n) == 1
            for b in range(n) if 3 * b % n == 0}


def verify():
    sizes = {}
    for n in range(5, 34, 2):
        ts = set(triples(n))
        affine = affine_permutations(n)
        assert len(affine) == gcd(n, 3) * sum(gcd(a, n) == 1 for a in range(n))
        for permutation in affine:
            assert {tuple(sorted(permutation[i] for i in t)) for t in ts} == ts
        full = full_automorphism_count(n)
        sizes[n] = (full, len(affine))
        if n >= 11:
            assert full == len(affine), (n, full, len(affine))
    assert sizes[9] == (36, 18), sizes[9]
    nonaffine_nine = (0, 1, 5, 6, 7, 2, 3, 4, 8)
    assert nonaffine_nine not in affine_permutations(9)
    ts9 = set(triples(9))
    assert {tuple(sorted(nonaffine_nine[i] for i in t)) for t in ts9} == ts9
    # Every nonzero x has a legal auxiliary t for the doubling identity.
    for n in range(11, 152, 2):
        half = pow(2, -1, n)
        for x in range(1, n):
            excluded = {0, x % n, -x % n, 2*x % n, -2*x % n,
                        (half*x) % n, (-half*x) % n,
                        3*x % n, -3*x % n}
            assert len(excluded) <= 9 < n
            assert any(t not in excluded for t in range(n))
    print("VERIFY_OK: exhaustive automorphism counts all odd n=11..33;")
    print("VERIFY_OK: n=9 nonaffine boundary witness; affine incidences and doubling auxiliaries checked")
    print("counts (n: full/affine):", ', '.join(f'{n}:{v[0]}/{v[1]}' for n,v in sizes.items()))


if __name__ == '__main__':
    verify()
