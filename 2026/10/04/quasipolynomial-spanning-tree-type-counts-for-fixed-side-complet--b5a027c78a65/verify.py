#!/usr/bin/env python3
"""Finite checks for the fixed-side complete-bipartite core/Burnside formula."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial


def connected_core(d, k, edges):
    n = d + k
    adj = [[] for _ in range(n)]
    for a, b in edges:
        u, v = a, d + b
        adj[u].append(v)
        adj[v].append(u)
    if len(edges) != n - 1:
        return False
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == n and all(len(adj[d + b]) >= 2 for b in range(k))


def canonical_core(d, k, edges):
    edges = set(edges)
    best = None
    for pa in permutations(range(d)):
        for pb in permutations(range(k)):
            mapped = tuple(sorted((pa[a], pb[b]) for a, b in edges))
            if best is None or mapped < best:
                best = mapped
    return best


def core_classes(d):
    classes = {}
    for k in range(1, d):
        possible = [(a, b) for a in range(d) for b in range(k)]
        for edges in combinations(possible, d + k - 1):
            if connected_core(d, k, edges):
                c = canonical_core(d, k, edges)
                classes[(k, c)] = c
    return [(k, c) for k, c in sorted(classes)]


def automorphism_actions(d, k, edges):
    edges = set(edges)
    actions = []
    for pa in permutations(range(d)):
        for pb in permutations(range(k)):
            if {(pa[a], pb[b]) for a, b in edges} == edges:
                actions.append(pa)
    # A core automorphism fixing the d-side pointwise must be trivial:
    # two distinct core vertices on the other side have degree at least two,
    # so equal neighbourhoods would create a 4-cycle in a tree.
    assert len(actions) == len(set(actions))
    return actions


def weak_compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, length - 1):
            yield (first,) + rest


def permute_vector(x, p):
    y = [0] * len(x)
    for i, j in enumerate(p):
        y[j] = x[i]
    return tuple(y)


def direct_orbit_count(d, k, edges, total):
    actions = automorphism_actions(d, k, edges)
    seen = set()
    count = 0
    for x in weak_compositions(total, d):
        if x in seen:
            continue
        orbit = {permute_vector(x, p) for p in actions}
        seen.update(orbit)
        count += 1
    return count


def cycle_lengths(p):
    used = [False] * len(p)
    out = []
    for i in range(len(p)):
        if used[i]:
            continue
        j = i
        size = 0
        while not used[j]:
            used[j] = True
            size += 1
            j = p[j]
        out.append(size)
    return out


def fixed_weight_vectors(p, total):
    # A p-fixed vector is constant on every cycle of p.
    dp = [0] * (total + 1)
    dp[0] = 1
    for weight in cycle_lengths(p):
        ndp = [0] * (total + 1)
        for s, value in enumerate(dp):
            if not value:
                continue
            for q in range((total - s) // weight + 1):
                ndp[s + q * weight] += value
        dp = ndp
    return dp[total]


def burnside_orbit_count(d, k, edges, total):
    actions = automorphism_actions(d, k, edges)
    numerator = sum(fixed_weight_vectors(p, total) for p in actions)
    assert numerator % len(actions) == 0
    return numerator // len(actions)


def stirling2(n, k):
    dp = [[0] * (k + 2) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j - 1] + j * dp[i - 1][j]
    return dp[n][k]


def type_count_from_cores(d, m, classes):
    assert m > d
    return sum(burnside_orbit_count(d, k, edges, m - k) for k, edges in classes)


def known_k3(m):
    correction = 2 if m % 3 == 1 else -1
    return (3 * m * m + 3 * m + 1 + correction) // 9


def is_tree_on_bipartition(d, m, edges):
    n = d + m
    if len(edges) != n - 1:
        return False
    adj = [[] for _ in range(n)]
    for a, b in edges:
        u, v = a, d + b
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == n


def canonical_full_bipartite_tree(d, m, edges):
    edges = set(edges)
    best = None
    for pa in permutations(range(d)):
        for pb in permutations(range(m)):
            mapped = tuple(sorted((pa[a], pb[b]) for a, b in edges))
            if best is None or mapped < best:
                best = mapped
    return best


def brute_type_count(d, m):
    possible = [(a, b) for a in range(d) for b in range(m)]
    classes = set()
    for edges in combinations(possible, d + m - 1):
        if is_tree_on_bipartition(d, m, edges):
            classes.add(canonical_full_bipartite_tree(d, m, edges))
    return len(classes)


def main():
    class_counts = {}
    computed = {}
    for d in range(2, 5):
        classes = core_classes(d)
        class_counts[d] = dict(sorted(Counter(k for k, _ in classes).items()))

        # Burnside is checked independently against literal orbit construction.
        for k, edges in classes:
            for total in range(0, 9):
                assert burnside_orbit_count(d, k, edges, total) == direct_orbit_count(d, k, edges, total)

        # Check the reciprocal-automorphism sum against the labelled-core count.
        by_k = defaultdict(Fraction)
        for k, edges in classes:
            by_k[k] += Fraction(1, len(automorphism_actions(d, k, edges)))
        for k in range(1, d):
            expected = Fraction(d ** (k - 1) * stirling2(d - 1, k), factorial(d))
            assert by_k[k] == expected

        values = {m: type_count_from_cores(d, m, classes) for m in range(d + 1, 10)}
        computed[d] = values

    # Old exact formulas for d=2 and d=3.
    for m, value in computed[2].items():
        assert value == (m + 1) // 2
    for m, value in computed[3].items():
        assert value == known_k3(m)

    # Published 2009 K_{4,m} table for m=5,...,9.
    assert [computed[4][m] for m in range(5, 10)] == [28, 45, 73, 105, 152]

    # Independent literal spanning-tree enumeration for two nontrivial K_{3,m} cases.
    assert brute_type_count(3, 4) == computed[3][4] == 7
    assert brute_type_count(3, 5) == computed[3][5] == 10

    # Leading coefficients from exact core automorphism sums agree with the
    # explicit asymptotic constant for d=2,3,4.
    leading = {}
    for d in range(2, 5):
        classes = core_classes(d)
        lhs = sum(Fraction(1, len(automorphism_actions(d, k, edges))) for k, edges in classes)
        lhs /= factorial(d - 1)
        rhs = Fraction(
            sum(d ** (k - 1) * stirling2(d - 1, k) for k in range(1, d)),
            factorial(d) * factorial(d - 1),
        )
        assert lhs == rhs
        leading[d] = str(lhs)

    print("ALL CHECKS PASSED")
    print("core_class_counts=", class_counts)
    print("K2_values=", computed[2])
    print("K3_values=", computed[3])
    print("K4_values=", computed[4])
    print("leading_coefficients=", leading)
    print("brute_full_tree_checks=K3,4:7;K3,5:10")


if __name__ == "__main__":
    main()
