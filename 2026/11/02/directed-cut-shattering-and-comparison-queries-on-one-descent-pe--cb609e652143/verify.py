"""Reproduce finite checks of star-forest shattering for binary directed cuts.
Uses only Python's standard library. Run: python verify.py
"""
from itertools import combinations, permutations, product
from math import comb


def is_eligible(n, edges, chosen):
    # edges are ordered directed pairs (tail, head), with no repeated unordered pair
    adj = [[] for _ in range(n)]
    for j in chosen:
        u, v = edges[j]
        adj[u].append(v)
        adj[v].append(u)
    seen = set()
    for start in range(n):
        if start in seen or not adj[start]:
            continue
        component = set()
        pending = [start]
        while pending:
            v = pending.pop()
            if v in component:
                continue
            component.add(v)
            pending.extend(adj[v])
        seen.update(component)
        if sum(len(adj[v]) for v in component) != 2 * (len(component) - 1):
            return False
        if len(component) >= 3:
            centers = [v for v in component if len(adj[v]) == len(component) - 1]
            if len(centers) != 1:
                return False
            center = centers[0]
            if not (all(edges[j][0] == center for j in chosen
                        if center in edges[j]) or
                    all(edges[j][1] == center for j in chosen
                        if center in edges[j])):
                return False
    return True


def actually_shattered(n, edges, chosen, concepts=None):
    if concepts is None:
        concepts = range(1 << n)
        def value(x, u, v):
            return ((x >> u) & 1) == 0 and ((x >> v) & 1) == 1
    else:
        def value(perm, u, v):
            return perm.index(v) < perm.index(u)
    patterns = set()
    for obj in concepts:
        pattern = sum((1 << k) for k, j in enumerate(chosen)
                      if value(obj, *edges[j]))
        patterns.add(pattern)
    return len(patterns) == (1 << len(chosen))


def shattering_polynomial(n):
    rows = [[1]]
    for size in range(1, n + 1):
        row = [0] * size
        for block in range(1, size + 1):
            multiplicity = (2 if block >= 3 else 1)
            factor = comb(size - 1, block - 1) * multiplicity
            for degree, coefficient in enumerate(rows[size - block]):
                row[degree + block - 1] += factor * coefficient
        rows.append(row)
    return rows[n]


def check_ranking_classes():
    for n in range(1, 7):
        edges = list(combinations(range(n), 2))
        concepts = [p for p in permutations(range(n))
                    if sum(p[i] > p[i + 1] for i in range(n-1)) <= 1]
        # The comparison predicate is inverted iff the larger label appears before the smaller.
        histogram = [0] * n
        for subset in range(1 << len(edges)):
            chosen = [j for j in range(len(edges)) if (subset >> j) & 1]
            predicted = is_eligible(n, edges, chosen)
            actual = actually_shattered(n, edges, chosen, concepts)
            assert actual == predicted, (n, subset, predicted, actual)
            if actual:
                histogram[len(chosen)] += 1
        assert histogram == shattering_polynomial(n), (n, histogram, shattering_polynomial(n))
        assert len(concepts) == (1 << n) - n
        print('RANKINGS_PASS', n, len(concepts), histogram)


def check_all_four_vertex_oriented_graphs():
    n = 4
    pairs = list(combinations(range(n), 2))
    cases = 0
    support_checks = 0
    for status in product((0, 1, -1), repeat=len(pairs)):
        edges = [(u, v) if t == 1 else (v, u)
                 for (u, v), t in zip(pairs, status) if t]
        for support in range(1 << len(edges)):
            chosen = [j for j in range(len(edges)) if support >> j & 1]
            assert is_eligible(n, edges, chosen) == actually_shattered(n, edges, chosen), (status, support)
            support_checks += 1
        cases += 1
    print('ORIENTED_GRAPHS_PASS', cases, support_checks)


if __name__ == '__main__':
    check_ranking_classes()
    check_all_four_vertex_oriented_graphs()
    print('ONE_DESCENT_STAR_FOREST_ALL_CHECKS_PASS')
