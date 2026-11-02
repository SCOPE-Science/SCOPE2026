#!/usr/bin/env python3
"""Finite checks for cograph enumerators in two cliques joined by a matching.

Run with Python 3. This program checks exact finite instances; it is not
intended as a proof of the identities for arbitrarily large parameters.
"""
from collections import Counter
from itertools import combinations
from math import comb


def adjacency(a, b, t):
    """Two cliques of sizes a,b and t disjoint edges between them."""
    adj = [0] * (a + b)
    for i in range(a + b):
        for j in range(i + 1, a + b):
            edge = (i < a and j < a) or (i >= a and j >= a)
            edge |= i < t and j == a + i
            if edge:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    return adj


def graph_is_cograph(mask, adj):
    """Independent graph-level test: forbid an induced path on four vertices."""
    vertices = [i for i in range(len(adj)) if mask >> i & 1]
    for four in combinations(vertices, 4):
        degree = [0] * 4
        edge_count = 0
        for i in range(4):
            for j in range(i + 1, 4):
                if adj[four[i]] >> four[j] & 1:
                    degree[i] += 1
                    degree[j] += 1
                    edge_count += 1
        if edge_count == 3 and sorted(degree) == [1, 1, 2, 2]:
            return False
    return True


def classified_cograph(mask, a, b, t):
    left = {i for i in range(a) if mask >> i & 1}
    right = {i for i in range(b) if mask >> (a + i) & 1}
    paired = left & right & set(range(t))
    return (not paired or min(len(left), len(right)) <= 1
            or (len(left) == len(right) == 2
                and left == right == paired))


def classified_maximal(mask, a, b, t):
    left = {i for i in range(a) if mask >> i & 1}
    right = {i for i in range(b) if mask >> (a + i) & 1}
    paired = left & right & set(range(t))
    if len(paired) == 2 and left == right == paired:
        return True
    if len(paired) == 1:
        i = next(iter(paired))
        return ((left == set(range(a)) and right == {i})
                or (right == set(range(b)) and left == {i}))
    if paired:
        return False
    if not set(range(t, a)) <= left or not set(range(t, b)) <= right:
        return False
    if any((i in left) == (i in right) for i in range(t)):
        return False
    l, r = len(left), len(right)
    return ((l >= 2 and r >= 2)
            or (l == 1 and left <= set(range(t, a)))
            or (r == 1 and right <= set(range(t, b))))


def predicted_all(a, b, t):
    out = Counter()
    # Each matching position: no vertex, left, or right.
    for j in range(t + 1):
        for k in range(a + b - 2 * t + 1):
            out[j + k] += (comb(t, j) * 2 ** j
                           * comb(a + b - 2 * t, k))
    for k in range(a):
        out[k + 2] += t * comb(a - 1, k)
    for k in range(b):
        out[k + 2] += t * comb(b - 1, k)
    out[2] -= t
    out[4] += comb(t, 2)
    return +out


def predicted_maximal(a, b, t):
    out = Counter()
    out[4] += comb(t, 2)
    out[a + 1] += t
    out[b + 1] += t
    out[a + b - t] += (2 ** t - (t + 1)
                       * (int(a == t) + int(b == t)))
    return +out


def test(a, b, t):
    adj = adjacency(a, b, t)
    n = a + b
    cograph = [graph_is_cograph(s, adj) for s in range(1 << n)]
    all_sizes, maximal_sizes = Counter(), Counter()
    for s, admissible in enumerate(cograph):
        assert classified_cograph(s, a, b, t) == admissible, (a,b,t,s)
        maximal = admissible and all(
            not cograph[s | (1 << i)] for i in range(n)
            if not s >> i & 1)
        assert classified_maximal(s, a, b, t) == maximal, (a,b,t,s)
        if admissible:
            all_sizes[s.bit_count()] += 1
        if maximal:
            maximal_sizes[s.bit_count()] += 1
    assert all_sizes == predicted_all(a, b, t), (a,b,t,all_sizes)
    assert maximal_sizes == predicted_maximal(a, b, t), (a,b,t,maximal_sizes)
    return 1 << n, sum(maximal_sizes.values())


def main():
    cases = [(a,b,t) for a in range(3,8) for b in range(3,8)
             for t in range(3,min(a,b)+1)]
    cases += [(8,8,8), (8,7,5)]
    tested = 0
    for a,b,t in cases:
        count, _ = test(a,b,t)
        tested += count
    print('VERIFY_OK graph_instances=%d direct_subsets=%d'
          ' cograph_and_maximal_structural_checks=PASS'
          ' both_polynomials=PASS' % (len(cases),tested))

if __name__ == '__main__':
    main()
