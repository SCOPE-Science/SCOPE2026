#!/usr/bin/env python3
"""Independent exhaustive anti-forcing census for GP(12,5); Python standard library only.

Run: python NAURU_VERIFY_EXHAUSTIVE.py
This uses perfect-matching backtracking and all deletion subsets, not an optimizer.
"""
import hashlib
import itertools
import json
from collections import Counter

N = 12
V = 24
edges = sorted(set(tuple(sorted(e)) for e in (
    [(i, (i + 1) % N) for i in range(N)]
    + [(12 + i, 12 + (i + 5) % N) for i in range(N)]
    + [(i, 12 + i) for i in range(N)]
)))
assert len(edges) == 36
incident = [[] for _ in range(V)]
for i, (u, v) in enumerate(edges):
    incident[u].append((i, v))
    incident[v].append((i, u))


def enumerate_matchings(free=(1 << V) - 1, selected=0):
    if free == 0:
        yield selected
        return
    u = (free & -free).bit_length() - 1
    for i, v in incident[u]:
        if free & (1 << v):
            yield from enumerate_matchings(free ^ (1 << u) ^ (1 << v), selected | (1 << i))


def complementary_cycle_type(m):
    remaining = set(range(V))
    degree2 = [[] for _ in range(V)]
    for i, (u, v) in enumerate(edges):
        if not (m >> i) & 1:
            degree2[u].append(v)
            degree2[v].append(u)
    assert all(len(a) == 2 for a in degree2)
    parts = []
    while remaining:
        stack = [min(remaining)]
        seen = set()
        while stack:
            u = stack.pop()
            if u in seen:
                continue
            seen.add(u)
            stack.extend(degree2[u])
        remaining.difference_update(seen)
        parts.append(len(seen))
    return tuple(sorted(parts))


def minimum_and_count(m, matchings):
    outside = [i for i in range(36) if not (m >> i) & 1]
    # Every different matching must be destroyed, and at least one of its
    # outside-the-reference edges must therefore be deleted.
    constraints = set()
    for other in matchings:
        if other != m:
            constraints.add(sum(1 << j for j, i in enumerate(outside) if other >> i & 1))
    ordered = sorted(constraints, key=lambda a: (a.bit_count(), a))
    minimal = []
    for s in ordered:
        if not any((q & s) == q for q in minimal):
            minimal.append(s)
    bits = [1 << j for j in range(24)]
    for k in range(9):
        count = 0
        for subset in itertools.combinations(bits, k):
            candidate = sum(subset)
            if all(candidate & mask for mask in minimal):
                count += 1
        if count:
            return k, count
    raise AssertionError('No anti-forcing set of at most eight edges')


def main():
    matchings = sorted(set(enumerate_matchings()))
    assert len(matchings) == 120
    results = []
    for m in matchings:
        k, number = minimum_and_count(m, matchings)
        results.append((complementary_cycle_type(m), k, number))
    counts = Counter((t, k, c) for t, k, c in results)
    spectrum = Counter(k for t, k, c in results)
    types = Counter(t for t, k, c in results)
    assert spectrum == {5: 6, 6: 93, 7: 18, 8: 3}
    assert sum(c for _, _, c in results) == 25092
    print(json.dumps({'method': 'exhaustive_all_120_matchings',
                      'perfect_matchings': len(matchings),
                      'anti_forcing_spectrum': dict(sorted(spectrum.items())),
                      'cycle_types': [(list(k), v) for k, v in sorted(types.items())],
                      'refined_profile': [(list(t), a, b, count)
                                          for (t, a, b), count in sorted(counts.items())],
                      'minimum_set_pairs': 25092}, sort_keys=True))

if __name__ == '__main__':
    main()
