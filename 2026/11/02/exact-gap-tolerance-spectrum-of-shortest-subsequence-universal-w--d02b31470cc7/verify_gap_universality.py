#!/usr/bin/env python3
"""Independent exact checks for shortest-host bounded-jump subsequence universality.

Run: python3 verify_gap_universality.py
This is finite verification; the accompanying proof establishes the infinite case.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import factorial


def gap_radius(w, pattern):
    """Minimum of the maximum consecutive-index jump over all embeddings."""
    n, k = len(w), len(pattern)
    best = None
    for locations in combinations(range(n), k):
        if all(w[locations[j]] == pattern[j] for j in range(k)):
            radius = max(locations[j + 1] - locations[j] for j in range(k - 1))
            if best is None or radius < best:
                best = radius
    return best


def expected_cumulative(q, k, d):
    choices = factorial(d + 1) * (d + 1) ** (q - d - 1)
    return factorial(q) * choices ** (k - 1)


def check_all(q, k):
    patterns = list(product(range(q), repeat=k))
    hist = Counter()
    eligible = 0
    exact_universal = 0
    patterned_embeddings = 0
    for w in product(range(q), repeat=q * k):
        if any(w.count(a) != k for a in range(q)):
            continue
        eligible += 1
        radii = []
        for pattern in patterns:
            r = gap_radius(w, pattern)
            patterned_embeddings += 1
            if r is None:
                break
            radii.append(r)
        universal = len(radii) == len(patterns)
        blocks = [w[i*q:(i+1)*q] for i in range(k)]
        permuted = all(len(set(block)) == q for block in blocks)
        assert universal == permuted, (q, k, w, universal, permuted)
        if universal:
            exact_universal += 1
            observed = max(radii)
            predicted = max(q + blocks[i+1].index(a) - blocks[i].index(a)
                            for i in range(k-1) for a in range(q))
            assert observed == predicted, (q, k, w, observed, predicted)
            hist[observed] += 1
    assert exact_universal == factorial(q)**k, (q,k, exact_universal)
    for d in range(q):
        observed = sum(c for rad, c in hist.items() if rad <= q+d)
        assert observed == expected_cumulative(q,k,d), (q,k,d,observed,expected_cumulative(q,k,d))
    print(f'PASS q={q} k={k} balanced_hosts={eligible} universal_hosts={exact_universal} '
          f'pattern_checks={patterned_embeddings} radius_spectrum={dict(sorted(hist.items()))}')
    return eligible, exact_universal, patterned_embeddings


def check_permutation_drop_counts():
    checked = 0
    for q in range(2,8):
        for d in range(q):
            actual = sum(max(i+1 - p[i] for i in range(q)) <= d for p in permutations(range(1, q+1)))
            predicted = factorial(d+1)*(d+1)**(q-d-1)
            assert actual == predicted, (q, d, actual, predicted)
            checked += 1
    print(f'PASS bounded_drop_counts={checked} q=2..7')


if __name__ == '__main__':
    check_permutation_drop_counts()
    totals = [0, 0, 0]
    for q, k in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2)]:
        got = check_all(q,k)
        totals = [a+b for a,b in zip(totals,got)]
    print(f'VERIFY_OK parameter_cases=7 balanced_hosts={totals[0]} '
          f'universal_hosts={totals[1]} exact_pattern_checks={totals[2]}')
