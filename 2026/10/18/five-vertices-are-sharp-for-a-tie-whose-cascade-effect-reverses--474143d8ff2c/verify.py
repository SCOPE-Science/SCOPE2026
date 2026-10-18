"""Exact finite enumeration for fractional-threshold cascade edge-response reversals.

Run with Python 3.10 or newer: python verify.py
Uses only the Python standard library. All threshold decisions use integer arithmetic.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations


def edge_list(n):
    return list(combinations(range(n), 2))


def adjacency(n, edge_mask, edges):
    a = [0] * n
    for i, (u, v) in enumerate(edges):
        if (edge_mask >> i) & 1:
            a[u] |= 1 << v
            a[v] |= 1 << u
    return a


def connected(adj):
    n = len(adj)
    seen = 1
    boundary = 1
    while boundary:
        upcoming = 0
        for v in range(n):
            if (boundary >> v) & 1:
                upcoming |= adj[v]
        upcoming &= ~seen
        seen |= upcoming
        boundary = upcoming
    return seen == (1 << n) - 1


def final_count(adj, seed, numerator, denominator):
    """Progressive simultaneous fractional activation; a/d >= p/q iff a*q >= p*d."""
    n = len(adj)
    active = 1 << seed
    while True:
        nxt = active
        for v in range(n):
            if (active >> v) & 1:
                continue
            d = adj[v].bit_count()
            if d and (adj[v] & active).bit_count() * denominator >= numerator * d:
                nxt |= 1 << v
        if nxt == active:
            return active.bit_count()
        active = nxt


def representative_thresholds(n):
    critical = sorted({Fraction(0), Fraction(1)} |
                      {Fraction(k, d) for d in range(1, n) for k in range(1, d + 1)})
    reps = sorted(set(critical[1:]) |
                  {(lo + hi) / 2 for lo, hi in zip(critical, critical[1:])})
    return reps


def canonical_key(mask, edge_index, seed, n, edges, mapping):
    edge = edges[edge_index]
    best = None
    for p in permutations(range(n)):
        remapped_mask = 0
        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1:
                uu, vv = sorted((p[u], p[v]))
                remapped_mask |= 1 << mapping[(uu, vv)]
        uu, vv = sorted((p[edge[0]], p[edge[1]]))
        key = (remapped_mask, mapping[(uu, vv)], p[seed])
        if best is None or key < best:
            best = key
    return best


def census():
    total = {}
    class_counts = Counter()
    canonical_profiles = {}
    for n in range(2, 6):
        edges = edge_list(n)
        mapping = {edge: i for i, edge in enumerate(edges)}
        reps = representative_thresholds(n)
        connected_count = 0
        positive = negative = reversals = 0
        for mask in range(1 << len(edges)):
            before = adjacency(n, mask, edges)
            if not connected(before):
                continue
            connected_count += 1
            for i, (u, v) in enumerate(edges):
                if (mask >> i) & 1:
                    continue
                after = before.copy()
                after[u] |= 1 << v
                after[v] |= 1 << u
                for seed in range(n):
                    differences = tuple(final_count(after, seed, t.numerator, t.denominator) -
                                        final_count(before, seed, t.numerator, t.denominator)
                                        for t in reps)
                    if min(differences) < 0:
                        negative += 1
                    if max(differences) > 0:
                        positive += 1
                    if min(differences) < 0 < max(differences):
                        reversals += 1
                        key = canonical_key(mask, i, seed, n, edges, mapping)
                        class_counts[key] += 1
                        if key in canonical_profiles:
                            assert canonical_profiles[key] == differences
                        else:
                            canonical_profiles[key] = differences
        total[n] = (connected_count, positive, negative, reversals)
    assert total[3][3] == 0 and total[4][3] == 0
    assert total[5][3] == 420
    assert sorted(class_counts.values()) == [60, 60, 60, 120, 120]
    assert len(class_counts) == 5
    reps = representative_thresholds(5)
    for key, profile in canonical_profiles.items():
        for t, diff in zip(reps, profile):
            expected = 0 if t <= Fraction(1, 3) else 3 if t <= Fraction(1, 2) else -1
            assert diff == expected, (key, t, diff, expected)
    print('n: connected labeled graphs; positive-edge responses; negative-edge responses; reversals')
    for n in sorted(total):
        print(n, *total[n])
    print('Five equivalence classes (base-edge-mask, added-edge-index, seed):')
    for key in sorted(class_counts):
        mask, eindex, seed = key
        E = edge_list(5)
        present = [edge for i, edge in enumerate(E) if (mask >> i) & 1]
        print('base',present,'added',E[eindex],'seed',seed,'labeled',class_counts[key])
    print('Verified universal 5-vertex step profile: zero to 1/3, +3 on (1/3,1/2], -1 on (1/2,1].')


def family(n):
    """Start with edges 01,03,04,12, attach a path to vertex 3, add edge 02."""
    assert n >= 5
    base = [(0, 1), (0, 3), (0, 4), (1, 2)]
    if n >= 6:
        base.append((3, 5))
        base.extend((k, k + 1) for k in range(5, n - 1))
    def build(added):
        a = [0] * n
        for u, v in base + ([(0, 2)] if added else []):
            a[u] |= 1 << v
            a[v] |= 1 << u
        return a
    g, h = build(False), build(True)
    assert connected(g) and connected(h)
    assert final_count(g, 1, 1, 2) == 2
    assert final_count(h, 1, 1, 2) == n
    assert final_count(g, 1, 2, 3) == 2
    assert final_count(h, 1, 2, 3) == 1


if __name__ == '__main__':
    census()
    for n in range(5, 41):
        family(n)
    print('Analytic family spot-check passed at sizes 5 through 40.')
