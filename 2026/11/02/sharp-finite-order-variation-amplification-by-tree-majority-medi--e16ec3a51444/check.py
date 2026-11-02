"""Reproducible tests of the sharp finite-tree majority-median variation bound.

Only Python standard library is required. Finite tests support but do not prove
claims for all tree orders or all real-valued inputs.
"""
from itertools import product
from random import Random
from fractions import Fraction


def tree_edges_from_prufer(code, n):
    if n == 2:
        return [(0, 1)]
    degree = [1] * n
    for v in code:
        degree[v] += 1
    edges = []
    for v in code:
        leaf = min(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, v))
        degree[leaf] -= 1
        degree[v] -= 1
    a, b = [i for i, d in enumerate(degree) if d == 1]
    edges.append((a, b))
    return edges


def majority(x, edges):
    adj = [[] for _ in x]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    y = []
    for i, neighbors in enumerate(adj):
        d = len(neighbors)
        # Include the current value only to break a neighbor-count tie.
        sample = [x[j] for j in neighbors] + ([x[i]] if d % 2 == 0 else [])
        y.append(sorted(sample)[len(sample) // 2])
    return y


def variation(x, edges):
    return sum(abs(x[a] - x[b]) for a, b in edges)


def check_binary(n, edges, stats):
    factor = Fraction(2) - Fraction(1, n // 2)
    for mask in range(1, (1 << n) - 1):
        x = [((mask >> j) & 1) for j in range(n)]
        y = majority(x, edges)
        before, after = variation(x, edges), variation(y, edges)
        assert Fraction(after, before) <= factor, (n, edges, mask, before, after)
        flips = [j for j in range(n) if x[j] != y[j]]
        if flips:
            components = len(flips) - sum(a in flips and b in flips for a, b in edges)
            assert after <= 2 * before - components, (n, edges, mask)
        else:
            assert after == before
        stats['binary'] += 1


def sharp_example(n):
    q = n // 2
    if n == 2:
        return [(0, 1)], [0, 1]
    if n == 3:
        return [(0, 1), (0, 2)], [0, 1, 1]
    # Star on 2q vertices, root 0, with q active leaves and q-1 inactive ones.
    edges = [(0, i) for i in range(1, 2 * q)]
    x = [0] + [1] * q + [0] * (q - 1)
    if n == 2 * q + 1:
        # Subdivide one originally agreeing root-leaf edge.
        target = q + 1
        edges.remove((0, target))
        edges += [(0, n - 1), (n - 1, target)]
        x.append(0)
    return edges, x


def main():
    stats = {'binary': 0, 'trees': 0, 'real': 0, 'sharp': 0}
    for n in range(2, 7):
        for seq in product(range(n), repeat=max(0, n - 2)):
            edges = tree_edges_from_prufer(seq, n)
            check_binary(n, edges, stats)
            stats['trees'] += 1
    rng = Random(271828)
    for n in range(7, 31):
        for _ in range(180):
            edges = tree_edges_from_prufer([rng.randrange(n) for j in range(n - 2)], n)
            x = [rng.randrange(-10, 11) for _ in range(n)]
            before = variation(x, edges)
            if before:
                after = variation(majority(x, edges), edges)
                assert Fraction(after, before) <= 2 - Fraction(1, n // 2)
                stats['real'] += 1
    for n in range(2, 151):
        edges, x = sharp_example(n)
        before, after = variation(x, edges), variation(majority(x, edges), edges)
        assert Fraction(after, before) == 2 - Fraction(1, n // 2), (n, before, after)
        stats['sharp'] += 1
    print('PASS', stats)

if __name__ == '__main__':
    main()
