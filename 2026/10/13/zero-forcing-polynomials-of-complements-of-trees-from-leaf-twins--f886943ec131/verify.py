"""Independent exact checks for a formula for zero-forcing polynomials of tree complements.
Uses only Python 3 standard library; no network or precomputed tables.
"""
from itertools import combinations, product
from math import comb
from random import Random


def prufer_tree(seq):
    n = len(seq) + 2
    degrees = [1] * n
    for v in seq:
        degrees[v] += 1
    edges = []
    for v in seq:
        leaf = next(i for i in range(n) if degrees[i] == 1)
        edges.append((leaf, v))
        degrees[leaf] -= 1
        degrees[v] -= 1
    a, b = (i for i in range(n) if degrees[i] == 1)
    edges.append((a, b))
    return edges


def adjacency(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        assert 0 <= a < n and 0 <= b < n and a != b
        adj[a].add(b)
        adj[b].add(a)
    assert len(edges) == n - 1
    return adj


def predicted(adj):
    n = len(adj)
    degrees = [len(s) for s in adj]
    if max(degrees) == n - 1:
        return (1, n - 1, 0, 0)
    leaf_counts = [sum(degrees[u] == 1 for u in adj[v]) for v in range(n)]
    count_two = comb(n, 2) - sum(comb(c, 2) for c in leaf_counts)
    count_witnesses = sum(
        (comb(degrees[v], 2) - comb(leaf_counts[v], 2)) * (n - degrees[v] - 1)
        for v in range(n)
    )
    count_paths = sum(
        (degrees[u] - 1) * (degrees[w] - 1)
        for v in range(n) for u, w in combinations(sorted(adj[v]), 2)
    )
    return (1, n, count_two, count_witnesses - count_paths)


def forcing(adj, white):
    n = len(adj)
    white = set(white)
    blue = set(range(n)) - white
    while white:
        changes = set()
        for v in blue:
            # Complement neighbors are all vertices other than v and its neighbors in the tree.
            complement_white_neighbors = white - adj[v] - {v}
            if len(complement_white_neighbors) == 1:
                changes.update(complement_white_neighbors)
        if not changes:
            return False
        blue.update(changes)
        white.difference_update(changes)
    return True


def check_tree(n, edges, full_four=False):
    adj = adjacency(n, edges)
    predicted_counts = predicted(adj)
    actual = tuple(sum(forcing(adj, W) for W in combinations(range(n), k)) for k in range(4))
    if predicted_counts != actual:
        raise AssertionError((n, edges, predicted_counts, actual))
    if full_four and any(forcing(adj, W) for W in combinations(range(n), 4)):
        raise AssertionError(('four-white counterexample', n, edges))
    return sum(comb(n, k) for k in range(4)) + (comb(n, 4) if full_four else 0)


def main():
    total_trees = 0
    total_trials = 0
    for n in range(5, 8):
        m = 0
        for seq in product(range(n), repeat=n - 2):
            total_trials += check_tree(n, prufer_tree(seq), full_four=True)
            total_trees += 1
            m += 1
        print('ALL_LABELED_TREES', n, m)
    rng = Random(814211)
    for n in range(8, 27):
        copies = 140 if n <= 18 else 40
        for j in range(copies):
            seq = [rng.randrange(n) for _ in range(n - 2)]
            total_trials += check_tree(n, prufer_tree(seq), full_four=(n <= 10))
            total_trees += 1
        print('SEEDED_TREES', n, copies)
    for n in range(5, 27):
        edges = [(0, v) for v in range(1, n)]
        total_trials += check_tree(n, edges, full_four=(n <= 10))
        total_trees += 1
    print('VERIFY_OK trees=', total_trees, 'white-subsets=', total_trials)

if __name__ == '__main__':
    main()
