#!/usr/bin/env python3
"""Exact finite checks of induced habitat-component distributions on trees.

No external packages; deterministic output. This is a finite check only: the
all-order theorem is proved by the combinatorial moment argument in RESULT.md.
"""
import itertools
import json
from collections import Counter, defaultdict
from functools import lru_cache
from math import comb


def prufer_edges(n, seq):
    if n == 2:
        return ((0, 1),)
    deg = [1] * n
    for v in seq:
        deg[v] += 1
    edges = []
    for v in seq:
        leaf = min(i for i, d in enumerate(deg) if d == 1)
        edges.append(tuple(sorted((leaf, v))))
        deg[leaf] -= 1
        deg[v] -= 1
    rest = [i for i, d in enumerate(deg) if d == 1]
    edges.append(tuple(rest))
    return tuple(sorted(edges))


@lru_cache(None)
def permutations(n):
    return tuple(itertools.permutations(range(n)))


def canonical(n, edges):
    return min(tuple(sorted(tuple(sorted((perm[u], perm[v]))) for u, v in edges))
               for perm in permutations(n))


def component_counts(n, edges):
    counts = Counter()
    for mask in range(1 << n):
        k = mask.bit_count()
        e = sum((mask >> u & 1) * (mask >> v & 1) for u, v in edges)
        counts[(k, k - e)] += 1
    return counts


def l3_and_w(n, edges):
    degree = [0] * n
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    l3 = sum((degree[u] - 1) * (degree[v] - 1) for u, v in edges)
    wedge = sum(comb(d, 2) for d in degree)
    return tuple(sorted(degree)), l3, wedge


def falling(k, a):
    value = 1
    for j in range(a):
        value *= k - j
    return value


def expected_raw_factorial_coeffs(n, counts, order):
    """Coefficients indexed by retained size for the Bernstein basis p^k q^(n-k)."""
    return tuple(sum(v * falling(c, order) for (k, c), v in counts.items() if k == i)
                 for i in range(n + 1))


def assert_moment_law(n, trees):
    groups = defaultdict(list)
    for edges in trees:
        deg, l3, W = l3_and_w(n, edges)
        cnt = component_counts(n, edges)
        groups[deg].append((edges, l3, W, cnt))
    pairs = 0
    for group in groups.values():
        for a, b in itertools.combinations(group, 2):
            pairs += 1
            for order in (0, 1, 2):
                assert expected_raw_factorial_coeffs(n, a[3], order) == expected_raw_factorial_coeffs(n, b[3], order)
            # Third factorial-moment polynomial difference must be -6 delta(L3) p^4 q^2.
            delta = [x - y for x, y in zip(expected_raw_factorial_coeffs(n, a[3], 3),
                                            expected_raw_factorial_coeffs(n, b[3], 3))]
            expected = [0] * (n + 1)
            for j in range(n - 5):
                expected[4+j] = -6 * (a[1] - b[1]) * comb(n - 6, j)
            # p^4 q^2 expressed in Bernstein basis of degree n by
            # p^4 q^2(p+q)^(n-6); valid since p+q=1.
            assert delta == expected, (n, a[0], b[0], delta, expected)
    return pairs


def main():
    classes = {}
    group_sizes = {}
    for n in range(2, 7):
        reps = {}
        for seq in itertools.product(range(n), repeat=max(0, n - 2)):
            e = prufer_edges(n, seq)
            reps.setdefault(canonical(n, e), e)
        classes[n] = list(reps.values())
        group_sizes[n] = len(reps)
    assert group_sizes == {2: 1, 3: 1, 4: 2, 5: 3, 6: 6}
    pairs_by_n = {n: assert_moment_law(n, ts) for n, ts in classes.items()}
    assert pairs_by_n == {2: 0, 3: 0, 4: 0, 5: 0, 6: 1}

    a = ((0, 1), (1, 2), (2, 3), (0, 4), (0, 5))  # arms 3,1,1
    b = ((0, 1), (1, 2), (0, 3), (3, 4), (0, 5))  # arms 2,2,1
    da, la, wa = l3_and_w(6, a)
    db, lb, wb = l3_and_w(6, b)
    assert da == db == (1, 1, 1, 2, 2, 3) and (la, lb) == (3, 4) and wa == wb == 5
    ca, cb = component_counts(6, a), component_counts(6, b)
    difference = {f'{k}:{c}': ca[(k, c)] - cb[(k, c)]
                  for k in range(7) for c in range(7) if ca[(k, c)] != cb[(k, c)]}
    assert difference == {'4:1': -1, '4:2': 3, '4:3': -3, '4:4': 1}
    for order in range(1, 4):
        assert sum((ca[4, c] - cb[4, c]) * falling(c, order) for c in range(7)) == (6 if order == 3 else 0)
    print(json.dumps({'class_counts_n2_to_n6':group_sizes,
                      'degree_matched_class_pairs':pairs_by_n,
                      'witness_degrees':da,'witness_length3_path_counts':[la,lb],
                      'witness_degree_wedge_count':wa,
                      'witness_subgraph_coefficient_difference':difference,
                      'witness_pgf_difference':'p^4*(1-p)^2*z*(z-1)^3',
                      'witness_third_cumulant_difference':'6*p^4*(1-p)^2',
                      'checks':'passed'},sort_keys=True,separators=(',',':')))

if __name__ == '__main__':
    main()
