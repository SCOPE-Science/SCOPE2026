"""Reproduce finite checks for classical edge-label teaching of spanning trees.

Requires only the Python standard library. Independent of the proofs of the
all-size statements; finite checks do not establish universality.
"""
from itertools import combinations


def is_tree(n, edges):
    if len(edges) != n - 1:
        return False
    parent = list(range(n))
    def root(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edges:
        u, v = root(u), root(v)
        if u == v:
            return False
        parent[u] = v
    return len({root(i) for i in range(n)}) == 1


def tree_masks(n, edges):
    return [sum(1 << j for j in js)
            for js in combinations(range(len(edges)), n - 1)
            if is_tree(n, [edges[j] for j in js])]


def matching_dimension(mask, nedge, bases):
    E = list(range(nedge))
    inside = [j for j in E if (mask >> j) & 1]
    outside = [j for j in E if not ((mask >> j) & 1)]
    base_set = set(bases)
    adjacency = {
        i: [j for j in outside if (mask ^ (1 << i) ^ (1 << j)) in base_set]
        for i in inside
    }
    owner = {}
    def augment(i, seen):
        for j in adjacency[i]:
            if j in seen:
                continue
            seen.add(j)
            if j not in owner or augment(owner[j], seen):
                owner[j] = i
                return True
        return False
    return sum(augment(i, set()) for i in inside)


def partitions(n):
    # Restricted-growth strings, one representative per set partition.
    if n == 0:
        yield ()
        return
    def rec(z, k):
        if len(z) == n:
            yield tuple(z)
            return
        for a in range(k + 1):
            yield from rec(z + [a], max(k, a + 1))
    yield from rec([0], 1)


def has_two_disjoint_spanning_trees(n, edges):
    for part in partitions(n):
        k = max(part) + 1
        crossing = sum(part[u] != part[v] for u, v in edges)
        if crossing < 2 * (k - 1):
            return False
    return True


def covered_by_two_forests(n, edges):
    for s in range(1, 1 << n):
        count_vertices = s.bit_count()
        count_edges = sum(((s >> u) & 1) and ((s >> v) & 1)
                          for u, v in edges)
        if count_edges > 2 * (count_vertices - 1):
            return False
    return True


def direct_teaching_number(mask, nedge, bases):
    # Separate definition-based implementation: search samples and distinguish
    # every other candidate, without constructing the exchange graph.
    others = [other for other in bases if other != mask]
    for size in range(nedge + 1):
        for sample in combinations(range(nedge), size):
            S = sum(1 << i for i in sample)
            if all(((mask ^ other) & S) != 0 for other in others):
                return size
    raise AssertionError('no teaching sample')


def verify(n, edges, direct=False):
    bs = tree_masks(n, edges)
    if not bs:
        return None
    r, c = n - 1, len(edges) - n + 1
    values = [matching_dimension(b, len(edges), bs) for b in bs]
    assert all(x <= min(r, c) for x in values)
    assert (all(x == r for x in values)
            == has_two_disjoint_spanning_trees(n, edges)), (n, edges, 'packing')
    assert (all(x == c for x in values)
            == covered_by_two_forests(n, edges)), (n, edges, 'covering')
    if direct:
        for b, x in zip(bs, values):
            assert direct_teaching_number(b, len(edges), bs) == x, (n, edges, b)
    return len(bs), min(values), max(values)


def main():
    total_graphs = total_trees = 0
    for n in range(2, 6):
        potential = list(combinations(range(n), 2))
        count = tree_count = 0
        for mask in range(1 << len(potential)):
            es = [e for i, e in enumerate(potential) if (mask >> i) & 1]
            result = verify(n, es, direct=(n <= 4))
            if result is not None:
                count += 1
                tree_count += result[0]
        total_graphs += count
        total_trees += tree_count
        print('LABELED_CONNECTED_PASS', 'n=', n, 'graphs=', count,
              'target_trees=', tree_count, flush=True)
    # Direct teaching search for K5 (125 target trees) and K3,3 (81 target trees).
    for p, q in [(1, 4), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4)]:
        n = p + q
        E = [(i, p + j) for i in range(p) for j in range(q)]
        bs = tree_masks(n, E)
        dimensions = [matching_dimension(b, len(E), bs) for b in bs]
        expected = min(n - 1, len(E) - (n - 1))
        assert set(dimensions) == {expected}, (p, q, set(dimensions))
        assert (all(x == n - 1 for x in dimensions)
                == has_two_disjoint_spanning_trees(n, E))
        assert (all(x == len(E) - n + 1 for x in dimensions)
                == covered_by_two_forests(n, E))
        if (p, q) in [(3, 3)]:
            for b in bs:
                assert direct_teaching_number(b, len(E), bs) == expected
        print('COMPLETE_BIPARTITE_PASS', 'p=', p, 'q=', q,
              'trees=', len(bs), 'teaching_number=', expected, flush=True)
    E5 = list(combinations(range(5), 2))
    assert verify(5, E5, direct=True) == (125, 4, 4)
    print('INDEPENDENT_K5_TEACHING_PASS', flush=True)
    # A bridged dense core realizes neither global extremal condition.
    dense_bridge = list(combinations(range(5), 2)) + [(4, 5)]
    count, mini, maxi = verify(6, dense_bridge)
    assert (mini, maxi) == (4, 4)
    assert not has_two_disjoint_spanning_trees(6, dense_bridge)
    assert not covered_by_two_forests(6, dense_bridge)
    print('NONEXTREMAL_BRIDGED_K5_PASS', count, mini, maxi, flush=True)
    print('ALL_SPANNING_TREE_TEACHING_CHECKS_PASS',
          'labeled_graphs=', total_graphs, 'target_trees=', total_trees)


if __name__ == '__main__':
    main()
