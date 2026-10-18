#!/usr/bin/env python3
"""Exact finite verification of a small Schelling swap-game theorem.

Run: python3 verify.py
Uses only the Python standard library. All utility comparisons use integers.
"""
from itertools import combinations, permutations
from fractions import Fraction


def pairs(n):
    return tuple(combinations(range(n), 2))


def edges_from_mask(n, mask):
    return tuple(e for k, e in enumerate(pairs(n)) if (mask >> k) & 1)


def mask_from_edges(n, edges):
    lookup = {e: k for k, e in enumerate(pairs(n))}
    return sum(1 << lookup[tuple(sorted(e))] for e in edges)


def graph(n, mask):
    adj = [set() for _ in range(n)]
    for i, j in edges_from_mask(n, mask):
        adj[i].add(j)
        adj[j].add(i)
    seen = {0}
    stack = [0]
    while stack:
        for j in adj[stack.pop()]:
            if j not in seen:
                seen.add(j)
                stack.append(j)
    if len(seen) != n:
        return None
    return tuple(tuple(sorted(row)) for row in adj)


def canonical_mask(n, mask):
    edges = edges_from_mask(n, mask)
    lookup = {e: k for k, e in enumerate(pairs(n))}
    best = None
    for perm in permutations(range(n)):
        shifted = sum(1 << lookup[tuple(sorted((perm[i], perm[j])))]
                      for i, j in edges)
        if best is None or shifted < best:
            best = shifted
    return best


def scores(adj, color):
    return [sum(color[i] == color[j] for j in adj[i]) for i in range(len(adj))]


def profitable_and_harmful(adj, color, i, j):
    if color[i] == color[j]:
        return False, False
    degree = [len(row) for row in adj]
    before = scores(adj, color)
    changed = list(color)
    changed[i], changed[j] = changed[j], changed[i]
    after = scores(adj, changed)
    # Agent initially at i moves to j, and conversely; denominators
    # remain the fixed vertex degrees.
    profitable = (after[j] * degree[i] > before[i] * degree[j]
                  and after[i] * degree[j] > before[j] * degree[i])
    if not profitable:
        return False, False
    happy_before = sum(2 * before[k] >= degree[k] for k in range(len(adj)))
    happy_after = sum(2 * after[k] >= degree[k] for k in range(len(adj)))
    return True, happy_after < happy_before


def examine(adj):
    n = len(adj)
    num_profitable = 0
    num_harmful = 0
    for bits in range(1 << n):
        color = tuple((bits >> k) & 1 for k in range(n))
        if min(sum(color), n - sum(color)) < 2:
            continue
        for i, j in pairs(n):
            profitable, harmful = profitable_and_harmful(adj, color, i, j)
            num_profitable += profitable
            num_harmful += harmful
    return num_profitable, num_harmful


WITNESS_SIX = [(0, 1), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
WITNESS_SEVEN = [(0, 4), (1, 2), (1, 3), (1, 4),
                 (2, 3), (2, 4), (3, 4)]


def test_witness():
    adj = graph(5, mask_from_edges(5, WITNESS_SIX))
    assert adj is not None
    a = (1, 0, 0, 1, 0)
    b = list(a)
    b[0], b[4] = b[4], b[0]
    d = [len(row) for row in adj]
    x, y = scores(adj, a), scores(adj, b)
    pre = [Fraction(x[i], d[i]) for i in range(5)]
    post = [Fraction(y[i], d[i]) for i in range(5)]
    assert pre == [Fraction(0), Fraction(1, 3), Fraction(1, 2),
                   Fraction(0), Fraction(2, 3)]
    assert post == [Fraction(1), Fraction(1, 3), Fraction(0),
                    Fraction(1, 3), Fraction(1, 3)]
    assert post[4] > pre[0] and post[0] > pre[4]
    assert sum(z >= Fraction(1, 2) for z in pre) == 2
    assert sum(z >= Fraction(1, 2) for z in post) == 1
    assert sum(pre) == Fraction(3, 2)
    assert sum(post) == Fraction(2)
    print('Six-edge witness: two profitable movers; happy 2 -> 1; total utility 3/2 -> 2.')


def main():
    test_witness()
    for n, expected_classes, expected_connected in [(2, 1, 1), (3, 2, 4),
                                                      (4, 6, 38), (5, 21, 728)]:
        representatives = {}
        connected_count = 0
        harmful_labeled = 0
        for mask in range(1 << len(pairs(n))):
            adj = graph(n, mask)
            if adj is None:
                continue
            connected_count += 1
            canonical = canonical_mask(n, mask)
            if canonical not in representatives:
                representatives[canonical] = examine(adj)
            # Every relabeling preserves the exact profitable and harmful counts.
            harmful_labeled += representatives[canonical][1]
        assert connected_count == expected_connected, (n, connected_count)
        assert len(representatives) == expected_classes
        bad = {m: result for m, result in representatives.items() if result[1]}
        if n <= 4:
            assert not bad
        else:
            assert len(bad) == 2, bad
            known = {canonical_mask(5, mask_from_edges(5, WITNESS_SIX)),
                     canonical_mask(5, mask_from_edges(5, WITNESS_SEVEN))}
            assert set(bad) == known, (bad, known)
            assert sorted(v.bit_count() for v in bad) == [6, 7]
        print('n=%d: connected labeled=%d; unlabeled classes=%d; '
              'witness classes=%d; labeled harmful configurations=%d' %
              (n, connected_count, len(representatives), len(bad), harmful_labeled))
        if bad:
            for m, (num_moves, num_harmful) in sorted(bad.items(), key=lambda kv: kv[0].bit_count()):
                print(' witness topology: edges=%d; profitable=%d; harmful=%d; canonical_mask=%d'
                      % (m.bit_count(), num_moves, num_harmful, m))
    print('PASS: all checks exact and exhaustive for connected graphs of order at most five.')


if __name__ == '__main__':
    main()
