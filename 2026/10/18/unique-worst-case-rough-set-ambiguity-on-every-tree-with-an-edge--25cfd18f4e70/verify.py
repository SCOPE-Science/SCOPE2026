"""Finite checks for maximum rough-approximation fibers on trees.

Standalone standard-library Python 3 program; exact integer arithmetic.
"""
from collections import Counter, defaultdict
from itertools import product
from random import Random


def tree_from_prufer(code):
    n = len(code) + 2
    degree = [1] * n
    for v in code:
        degree[v] += 1
    edges = []
    for v in code:
        u = next(i for i in range(n) if degree[i] == 1)
        edges.append((u, v))
        degree[u] -= 1
        degree[v] -= 1
    u, v = [i for i in range(n) if degree[i] == 1]
    edges.append((u, v))
    return edges


def edge_cover_poly(n, edges):
    out = Counter()
    for mask in range(1 << len(edges)):
        endpoints = 0
        count = 0
        for k, (u, v) in enumerate(edges):
            if (mask >> k) & 1:
                endpoints |= (1 << u) | (1 << v)
                count += 1
        if endpoints == (1 << n) - 1:
            out[count] += 1
    return out


def tree_dp(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def recurse(v, parent):
        pairs = [recurse(w, v) for w in adj[v] if w != parent]
        covered = 1
        none_selected = 1
        for need, ready in pairs:
            covered *= need + ready
            none_selected *= need
        return covered - none_selected, covered

    return recurse(0, -1)[0]


def analyze(n, edges, detail=False):
    adj = [1 << i for i in range(n)]
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    fibers = defaultdict(Counter)
    for x in range(1 << n):
        low = 0
        up = 0
        for v in range(n):
            if adj[v] & x == adj[v]:
                low |= 1 << v
            if adj[v] & x:
                up |= 1 << v
        cuts = sum(((x >> u) ^ (x >> v)) & 1 for u, v in edges)
        fibers[(low, up)][cuts] += 1
    ec_poly = edge_cover_poly(n, edges)
    assert tree_dp(n, edges) == sum(ec_poly.values())
    center = (0, (1 << n) - 1)
    assert fibers[center] == Counter({k: 2 * c for k, c in ec_poly.items()})
    edgecover = sum(ec_poly.values())
    for (low, up), poly in fibers.items():
        if (low, up) == center:
            continue
        mixed = up & (~low) & ((1 << n) - 1)
        h = sum(1 for u, v in edges if not (mixed >> u & 1 and mixed >> v & 1))
        assert h > 0
        for k, c in poly.items():
            assert c <= ec_poly[k + h], (n, edges, (low, up), k, c, h, ec_poly)
        assert sum(poly.values()) <= edgecover
        assert 2 * sum(poly.values()) <= sum(fibers[center].values())
    return len(fibers), edgecover, sum(fibers[center].values())


def main():
    seen = 0
    total_fibers = 0
    center_weight_sum = 0
    for n in range(2, 8):
        count = 0
        for code in product(range(n), repeat=n - 2):
            edges = tree_from_prufer(code)
            fs, ec, center_count = analyze(n, edges)
            assert center_count == 2 * ec
            total_fibers += fs
            center_weight_sum += center_count
            count += 1
        seen += count
        print('LABELED_TREES', n, count)
    rng = Random(173)
    samples = 0
    for n in (8, 9, 10, 11):
        for _ in range(150):
            code = tuple(rng.randrange(n) for _ in range(n - 2))
            analyze(n, tree_from_prufer(code))
            samples += 1
    print('VERIFY_OK exhaustive_labeled_trees=', seen,
          'individual_rough_fibers=', total_fibers,
          'central_colorings=', center_weight_sum,
          'sampled_larger_trees=', samples,
          'edge_cover_polynomial=PASS',
          'fiber_shift_dominance=PASS',
          'unique_maximum=PASS',
          'tree_dp=PASS')


if __name__ == '__main__':
    main()
