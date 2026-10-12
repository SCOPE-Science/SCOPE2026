#!/usr/bin/env python3
"""Exact census for tree-shaped interaction networks and fixed-size sampling.

Requires Python >= 3.10 standard library only. Run: python verify.py
"""
from collections import Counter
from itertools import combinations
from math import comb


def canonical_tree(n, edges):
    """AHU code of an unrooted tree, rooted at its one or two centers."""
    nbr = [[] for _ in range(n)]
    for u, v in edges:
        nbr[u].append(v)
        nbr[v].append(u)
    alive = set(range(n))
    while len(alive) > 2:
        leaves = [u for u in alive if sum(v in alive for v in nbr[u]) <= 1]
        assert leaves and len(leaves) < len(alive)
        alive.difference_update(leaves)

    def rooted(u, parent):
        return '(' + ''.join(sorted(rooted(v, u) for v in nbr[u]
                                  if v != parent)) + ')'

    centers = sorted(alive)
    if len(centers) == 1:
        return rooted(centers[0], -1)
    u, v = centers
    return '[' + ''.join(sorted((rooted(u, v), rooted(v, u)))) + ']'


def unlabeled_trees(max_order):
    """Enumerate each unrooted tree shape by all one-leaf augmentations."""
    representatives = {canonical_tree(1, ()): ()}
    yield 1, representatives
    for n in range(2, max_order + 1):
        next_representatives = {}
        for edges in representatives.values():
            for attach_to in range(n-1):
                augmented = edges + ((attach_to, n-1),)
                next_representatives.setdefault(
                    canonical_tree(n, augmented), augmented)
        representatives = next_representatives
        yield n, representatives


def distribution_counts(n, edges):
    """H[k][j] counts k-vertex subsets inducing exactly j edges."""
    masks = [(1 << u) | (1 << v) for u, v in edges]
    H = [[0] * n for _ in range(n + 1)]
    for subset in range(1 << n):
        k = subset.bit_count()
        e = sum((subset & mask) == mask for mask in masks)
        assert 0 <= e < n
        H[k][e] += 1
    for k in range(n + 1):
        assert sum(H[k]) == comb(n, k)
    return tuple(tuple(row) for row in H)


def pair_collisions(signatures):
    multiplicity = Counter(signatures)
    return sum(v * (v - 1) // 2 for v in multiplicity.values())


def verify():
    known_tree_counts = (1, 1, 1, 2, 3, 6, 11, 23, 47, 106)
    optimal_single_depths = {4: (3,), 5: (3, 4), 6: (4,),
                             7: (4, 5), 8: (5,)}
    expected_9_collisions = {2: 1081, 3: 117, 4: 10,
                             5: 1, 6: 1, 7: 7, 8: 96}
    summary = []
    for n, shapes in unlabeled_trees(10):
        assert len(shapes) == known_tree_counts[n - 1], (n, len(shapes))
        assert len(set(shapes)) == len(shapes)
        assert all(len(edges) == n-1 for edges in shapes.values())
        H = [distribution_counts(n, edges) for edges in shapes.values()]
        assert pair_collisions(H) == (1 if n == 10 else 0)
        if 4 <= n <= 8:
            successful = tuple(k for k in range(2, n)
                               if pair_collisions([h[k] for h in H]) == 0)
            assert successful == optimal_single_depths[n]
        if n == 9:
            for k in range(2, 9):
                observed = pair_collisions([h[k] for h in H])
                assert observed == expected_9_collisions[k] > 0
            success_pairs = tuple((k, l) for k, l in combinations(range(2, 9), 2)
                                  if pair_collisions([(h[k], h[l]) for h in H]) == 0)
            assert success_pairs == ((4, 6), (5, 6), (5, 7), (6, 7), (6, 8))
            assert len(H) == 47
        if n == 10:
            duplicates = {}
            for edges, h in zip(shapes.values(), H):
                if h in duplicates:
                    other = duplicates[h]
                    assert canonical_tree(n, edges) != canonical_tree(n, other)
                    print('FULL_COLLISION_10', other, edges)
                else:
                    duplicates[h] = edges
        summary.append((n, len(shapes)))
    print('TREE_SHAPES', summary)
    print('OPTIMAL_ONE_DEPTH_SCHEMES', optimal_single_depths)
    print('NINE_SINGLE_K_PAIR_COLLISIONS', expected_9_collisions)
    print('OPTIMAL_TWO_DEPTH_SCHEMES_9', ((4, 6), (5, 6), (5, 7),
                                          (6, 7), (6, 8)))
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
