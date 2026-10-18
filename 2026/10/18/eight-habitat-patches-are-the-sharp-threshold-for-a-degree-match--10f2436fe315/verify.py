#!/usr/bin/env python3
"""Exact enumeration of finite habitat trees under independent patch retention.

Run with Python 3.9+ and no third-party packages. All counts are integers.
"""
import json
from collections import Counter, defaultdict
from itertools import combinations


def canonical_tree(edges, n):
    """Complete unrooted-tree invariant via minimum rooted AHU word."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def rooted(u, parent):
        return '(' + ''.join(sorted(rooted(v, u) for v in adj[u] if v != parent)) + ')'

    return min(rooted(u, -1) for u in range(n))


def unlabeled_trees_through(n_max):
    """Leaf addition is exhaustive because every nontrivial tree has a leaf."""
    trees = {1: [()]}
    for n in range(2, n_max + 1):
        new = {}
        for edges in trees[n - 1]:
            for v in range(n - 1):
                candidate = tuple(sorted(edges + ((v, n - 1),)))
                new.setdefault(canonical_tree(candidate, n), candidate)
        trees[n] = list(new.values())
    return trees


def largest_by_dfs(edges, n, subset):
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    best = 0
    remaining = subset
    while remaining:
        one = remaining & -remaining
        component = one
        frontier = one
        while frontier:
            neighbors = 0
            x = frontier
            while x:
                z = x & -x
                x -= z
                neighbors |= adj[z.bit_length() - 1]
            frontier = neighbors & remaining & ~component
            component |= frontier
        best = max(best, component.bit_count())
        remaining &= ~component
    return best


def largest_by_union_find(edges, n, subset):
    """Independent exact implementation, using union-find rather than flood fill."""
    active = set(i for i in range(n) if (subset >> i) & 1)
    if not active:
        return 0
    parent = list(range(n))
    size = [1] * n

    def root(i):
        while i != parent[i]:
            i = parent[i]
        return i

    for u, v in edges:
        if u in active and v in active:
            a, b = root(u), root(v)
            if a != b:
                parent[b] = a
                size[a] += size[b]
    return max(size[root(i)] for i in active)


def fixed_survivor_sums(edges, n, implementation=largest_by_dfs):
    sums = [0] * (n + 1)
    for mask in range(1 << n):
        sums[mask.bit_count()] += implementation(edges, n, mask)
    return tuple(sums)


def degree_sequence(edges, n):
    degrees = [0] * n
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
    return tuple(sorted(degrees))


def spider(arm_lengths):
    edges = []
    next_vertex = 1
    for arm_length in arm_lengths:
        previous = 0
        for _ in range(arm_length):
            edges.append((previous, next_vertex))
            previous = next_vertex
            next_vertex += 1
    return tuple(edges), next_vertex


def compare_trees(trees, n):
    grouped = defaultdict(list)
    for edges in trees:
        grouped[degree_sequence(edges, n)].append((fixed_survivor_sums(edges, n), edges))
    comparison_count = 0
    incomparable = []
    oriented_differences = []
    for degree, family in grouped.items():
        for i in range(len(family)):
            for j in range(i):
                comparison_count += 1
                v = tuple(a - b for a, b in zip(family[i][0], family[j][0]))
                if any(x > 0 for x in v) and any(x < 0 for x in v):
                    incomparable.append((degree, family[i][1], family[j][1], v))
                else:
                    oriented_differences.append(tuple(-x for x in v) if any(x < 0 for x in v) else v)
    return comparison_count, incomparable, oriented_differences


def main():
    all_trees = unlabeled_trees_through(8)
    counts = [len(all_trees[n]) for n in range(1, 9)]
    assert counts == [1, 1, 1, 2, 3, 6, 11, 23], counts
    comparisons = {}
    expected_lower_bound_differences = {
        6: [(0, 0, 0, 0, 1, 0, 0)],
        7: [(0, 0, 0, 0, 1, 0, 1, 0),
            (0, 0, 0, 0, 2, 0, 1, 0),
            (0, 0, 0, 0, 1, 0, 0, 0),
            (0, 0, 0, 0, 2, 1, 0, 0),
            (0, 0, 0, 0, 2, 1, 1, 0)]
    }
    for n in range(1, 9):
        count, bad, vectors = compare_trees(all_trees[n], n)
        comparisons[str(n)] = {'degree_matched_pairs': count, 'coefficientwise_incomparable_pairs': len(bad)}
        if n <= 7:
            assert len(bad) == 0, (n, bad)
            assert Counter(vectors) == Counter(expected_lower_bound_differences.get(n, [])), (n, vectors)
        else:
            assert count == 23 and len(bad) == 1, (count, bad)

    a, na = spider((3, 3, 1))
    b, nb = spider((4, 2, 1))
    assert na == nb == 8
    assert degree_sequence(a, 8) == degree_sequence(b, 8) == (1, 1, 1, 2, 2, 2, 2, 3)
    assert canonical_tree(a, 8) != canonical_tree(b, 8)
    ha = fixed_survivor_sums(a, 8)
    hb = fixed_survivor_sums(b, 8)
    assert ha == (0, 8, 35, 98, 167, 177, 119, 46, 8), ha
    assert hb == (0, 8, 35, 98, 167, 178, 118, 46, 8), hb
    assert tuple(x - y for x, y in zip(ha, hb)) == (0, 0, 0, 0, 0, -1, 1, 0, 0)
    # Independent method: union-find recomputes every one of the 512 subset outcomes.
    assert fixed_survivor_sums(a, 8, largest_by_union_find) == ha
    assert fixed_survivor_sums(b, 8, largest_by_union_find) == hb
    # The only eight-vertex incomparable pair must be these two tree isomorphism classes.
    _, exceptional, _ = compare_trees(all_trees[8], 8)
    keys = {canonical_tree(x, 8) for x in (exceptional[0][1], exceptional[0][2])}
    assert keys == {canonical_tree(a, 8), canonical_tree(b, 8)}

    report = {
        'verified_tree_class_counts_n1_to_n8': counts,
        'degree_matched_comparisons': comparisons,
        'unique_n8_incomparable_pair': ['spider(3,3,1)', 'spider(4,2,1)'],
        'eight_vertex_sum_largest_component_by_survivor_count_A': list(ha),
        'eight_vertex_sum_largest_component_by_survivor_count_B': list(hb),
        'difference_coefficients_k0_to_k8': [x - y for x, y in zip(ha, hb)],
        'difference_mean_independent_retention': 'p^5*(1-p)^2*(2*p-1)',
        'crossing_probability': '1/2',
        'crosschecked_with_union_find': True,
        'scope': 'all unlabeled undirected trees with n<=8; all fixed-size vertex-survivor subsets'
    }
    print(json.dumps(report, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
