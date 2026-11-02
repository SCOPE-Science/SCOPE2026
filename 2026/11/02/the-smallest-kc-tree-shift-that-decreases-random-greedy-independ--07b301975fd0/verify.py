#!/usr/bin/env python3
"""Exact verification of a nine-vertex KC shift counterexample.

Only the Python standard library is required. First-vertex recursion and
exhaustive permutation counting independently verify the witness. A complete
isomorphism-reduced tree census verifies minimal order among proper KC shifts.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import factorial

ORDER = 9
TREE = ((0, 1), (1, 2), (1, 3), (3, 4),
        (4, 5), (5, 6), (6, 7), (6, 8))
SHIFTED = ((0, 1), (1, 2), (1, 3), (3, 4),
           (3, 6), (4, 5), (6, 7), (6, 8))
EXPECTED_TREE = {3: Fraction(29, 405), 4: Fraction(52, 135),
                 5: Fraction(4, 27), 6: Fraction(32, 81)}
EXPECTED_SHIFTED = {3: Fraction(55, 567), 4: Fraction(19, 54),
                    5: Fraction(4, 27), 6: Fraction(457, 1134)}
UNLABELED_TREE_COUNTS = (1, 1, 1, 2, 3, 6, 11, 23, 47)


def adjacency(n, edges):
    masks = [0] * n
    for u, v in edges:
        assert 0 <= u < n and 0 <= v < n and u != v
        masks[u] |= 1 << v
        masks[v] |= 1 << u
    return tuple(masks)


def exact_distribution(adj):
    n = len(adj)

    @lru_cache(None)
    def recursion(remaining):
        if remaining == 0:
            return (Fraction(1),)
        ans = [Fraction(0)] * (remaining.bit_count() + 1)
        for v in range(n):
            if remaining & (1 << v):
                smaller = remaining & ~(1 << v) & ~adj[v]
                for k, probability in enumerate(recursion(smaller)):
                    ans[k + 1] += probability / remaining.bit_count()
        return tuple(ans)

    return recursion((1 << n) - 1)


def exact_mean(adj):
    n = len(adj)

    @lru_cache(None)
    def recursion(remaining):
        if remaining == 0:
            return Fraction(0)
        return 1 + sum(
            (recursion(remaining & ~(1 << v) & ~adj[v])
             for v in range(n) if remaining & (1 << v)),
            Fraction(0)) / remaining.bit_count()

    return recursion((1 << n) - 1)


def direct_permutations(adj):
    n = len(adj)
    counts = Counter()
    for order in permutations(range(n)):
        selected = 0
        for v in order:
            if not (selected & adj[v]):
                selected |= 1 << v
        counts[selected.bit_count()] += 1
    assert sum(counts.values()) == factorial(n)
    return tuple(Fraction(counts[k], factorial(n)) for k in range(n + 1))


def neighbors(n, edges):
    out = [set() for _ in range(n)]
    for u, v in edges:
        out[u].add(v)
        out[v].add(u)
    return out


def path_between(n, edges, start, stop):
    adj = neighbors(n, edges)
    predecessor = {start: -1}
    queue = [start]
    for v in queue:
        for w in adj[v]:
            if w not in predecessor:
                predecessor[w] = v
                queue.append(w)
    assert stop in predecessor
    path = []
    v = stop
    while v != -1:
        path.append(v)
        v = predecessor[v]
    return list(reversed(path))


def proper_shift(n, edges, x, y):
    path = path_between(n, edges, x, y)
    adj = neighbors(n, edges)
    if any(len(adj[v]) != 2 for v in path[1:-1]):
        return None
    old_leaves = sum(len(a) == 1 for a in adj)
    next_to_y = path[-2]
    moved = adj[y] - {next_to_y}
    if not moved:
        return None
    new = {tuple(sorted(e)) for e in edges}
    for w in moved:
        new.remove(tuple(sorted((y, w))))
        new.add(tuple(sorted((x, w))))
    new = tuple(sorted(new))
    if sum(len(a) == 1 for a in neighbors(n, new)) != old_leaves + 1:
        return None
    return new


def canonical_tree_code(n, edges):
    """Complete unlabeled-tree isomorphism code (root at a tree center)."""
    adj = neighbors(n, edges)
    stripped = [set(s) for s in adj]
    remaining = set(range(n))
    while len(remaining) > 2:
        leaves = [v for v in remaining if len(stripped[v]) <= 1]
        assert leaves
        for v in leaves:
            for w in stripped[v]:
                stripped[w].discard(v)
        remaining.difference_update(leaves)

    def root_code(v, parent):
        return '(' + ''.join(sorted(root_code(w, v)
                                  for w in adj[v] if w != parent)) + ')'

    return min(root_code(center, -1) for center in remaining)


def census_through_nine():
    # Every tree of order n+1 is obtainable by attaching a leaf to a tree
    # of order n. Canonical codes remove all duplicate labeled examples.
    current = {canonical_tree_code(1, ()): ()}
    rows = []
    negatives_at_nine = []
    for n in range(1, 10):
        assert len(current) == UNLABELED_TREE_COUNTS[n - 1]
        transitions = 0
        negatives = []
        for edges in current.values():
            before = exact_mean(adjacency(n, edges))
            for x in range(n):
                for y in range(n):
                    if x == y:
                        continue
                    shifted = proper_shift(n, edges, x, y)
                    if shifted is None:
                        continue
                    transitions += 1
                    gap = exact_mean(adjacency(n, shifted)) - before
                    if gap < 0:
                        negatives.append(gap)
        rows.append((n, len(current), transitions, len(negatives)))
        if n < 9:
            assert not negatives, ('unexpected smaller counterexample', n)
            larger = {}
            for edges in current.values():
                for attach in range(n):
                    new = tuple(sorted(edges + ((attach, n),)))
                    larger[canonical_tree_code(n + 1, new)] = new
            current = larger
        else:
            negatives_at_nine = negatives
    assert negatives_at_nine and min(negatives_at_nine) == -Fraction(1, 105)
    return rows


def run():
    original = adjacency(ORDER, TREE)
    transformed = adjacency(ORDER, SHIFTED)
    assert proper_shift(ORDER, TREE, 3, 5) == tuple(sorted(SHIFTED))
    assert len(TREE) == len(SHIFTED) == ORDER - 1
    assert sum(m.bit_count() == 1 for m in original) == 4
    assert sum(m.bit_count() == 1 for m in transformed) == 5
    for name, adj, target, mean in (
        ('original', original, EXPECTED_TREE, Fraction(73, 15)),
        ('shifted', transformed, EXPECTED_SHIFTED, Fraction(34, 7))):
        probabilities = exact_distribution(adj)
        assert {k: x for k, x in enumerate(probabilities) if x} == target
        assert sum(probabilities) == 1
        assert sum(k * x for k, x in enumerate(probabilities)) == mean
        assert exact_mean(adj) == mean
        assert direct_permutations(adj) == probabilities
        print(name, 'mean', str(mean), 'distribution', target,
              'permutations', factorial(ORDER))
    assert exact_mean(transformed) - exact_mean(original) == -Fraction(1, 105)
    rows = census_through_nine()
    print('order,unlabeled_trees,oriented_proper_shifts,strict_decreases')
    for row in rows:
        print(*row, sep=',')
    print('PASS: independent 9! enumeration, exact recursion, exhaustive minimality census')


if __name__ == '__main__':
    run()
