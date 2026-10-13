#!/usr/bin/env python3
"""Exact finite census for branch-count phylogenetic-diversity sampling laws.

No external packages. Run: python3 phylo_sampling_verify.py
All sampled-subset distributions are counted with integers, not simulated.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations
from math import comb

L = 'L'

@lru_cache(None)
def rooted_shapes(n):
    if n == 1:
        return (L,)
    result = []
    for left_n in range(1, n // 2 + 1):
        right_n = n - left_n
        for i, left in enumerate(rooted_shapes(left_n)):
            for j, right in enumerate(rooted_shapes(right_n)):
                if left_n < right_n or i <= j:
                    result.append((left, right))
    return tuple(result)

@lru_cache(None)
def pd_polynomial(tree):
    # Coefficient of z^k y^d is the number of k-tip sets with PD d.
    if tree == L:
        return {(0, 0): 1, (1, 0): 1}
    left, right = tree
    result = defaultdict(int)
    a = pd_polynomial(left)
    b = pd_polynomial(right)
    for (k, d), x in a.items():
        for (j, e), y in b.items():
            # The two root-to-child edges are included exactly when occupied.
            result[k + j, d + e + (k > 0) + (j > 0)] += x * y
    return dict(result)

def leaves_to_root_edges(tree, prefix=''):
    if tree == L:
        return (frozenset(prefix[:i] for i in range(1, len(prefix) + 1)),)
    left, right = tree
    return (leaves_to_root_edges(left, prefix + '0')
            + leaves_to_root_edges(right, prefix + '1'))

def direct_polynomial(tree):
    # Logically independent verifier: enumerate every marked leaf subset and
    # count the union of its root-to-leaf edges explicitly.
    paths = leaves_to_root_edges(tree)
    total = Counter()
    for k in range(len(paths) + 1):
        for subset in combinations(paths, k):
            selected_edges = set()
            for path in subset:
                selected_edges.update(path)
            total[k, len(selected_edges)] += 1
    return dict(total)

def signature(polynomial, k):
    return tuple(sorted((d, count) for (j, d), count in polynomial.items() if j == k))

def collision_pairs(signatures):
    classes = defaultdict(list)
    for index, sig in enumerate(signatures):
        classes[sig].append(index)
    return {tuple(pair) for members in classes.values() for pair in combinations(members, 2)}

def check():
    shape_counts = (1, 1, 1, 2, 3, 6, 11, 23, 46, 98)
    subset_cases = 0
    tree_cases = 0
    for n in range(1, 11):
        trees = rooted_shapes(n)
        assert len(trees) == shape_counts[n - 1]
        assert len(set(map(str, trees))) == len(trees)
        for t in trees:
            p = pd_polynomial(t)
            for k in range(n + 1):
                assert sum(v for (j, _), v in p.items() if j == k) == comb(n, k)
            assert p == direct_polynomial(t)
            tree_cases += 1
            subset_cases += 2 ** n
        if 4 <= n <= 9:
            assert len({signature(pd_polynomial(t), 2) for t in trees}) == len(trees)
    n = 10
    trees = rooted_shapes(n)
    collisions = {
        k: collision_pairs([signature(pd_polynomial(t), k) for t in trees])
        for k in range(1, n)
    }
    assert {k: len(v) for k, v in collisions.items()} == {
        1: 94, 2: 1, 3: 13, 4: 39, 5: 102,
        6: 232, 7: 576, 8: 1654, 9: 4753,
    }
    # No single sampling depth identifies every one of the 98 shapes.
    assert all(collisions[k] for k in range(1, n))
    two_depth_designs = {
        (a, b) for a, b in combinations(range(1, n), 2)
        if not collisions[a].intersection(collisions[b])
    }
    assert two_depth_designs == {
        (1, 3), (1, 4), (1, 5), (2, 3), (2, 4),
        (2, 5), (2, 6), (2, 7), (2, 8),
    }
    assert collisions[2] == {(85, 96)}
    t1, t2 = trees[85], trees[96]
    assert t1 != t2
    assert signature(pd_polynomial(t1), 1) == signature(pd_polynomial(t2), 1)
    assert signature(pd_polynomial(t1), 2) == signature(pd_polynomial(t2), 2)
    assert signature(pd_polynomial(t1), 3) != signature(pd_polynomial(t2), 3)
    assert signature(pd_polynomial(t1), 2) == ((4, 1), (5, 14), (6, 10), (7, 12), (8, 8))
    assert signature(pd_polynomial(t1), 1) == ((2, 1), (3, 3), (4, 6))
    print('VERIFY_OK shapes_through_10=%d direct_subsets=%d '
          'pair_ambiguity_10=1 admissible_two_depth_designs=9'
          % (tree_cases, subset_cases))

if __name__ == '__main__':
    check()
