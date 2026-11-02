"""Reproducible finite checks for acyclic-orientation shattering on small graphs.

Run with Python 3.9+ as: python verify.py
No external packages or inputs are needed except certificates/diamond_tree.json.
The all-order structural theorem is established by the separate mathematical proof;
these computations corroborate small cases and authenticate the finite gadget.
"""
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path


def acyclic_orientations(n, edges):
    out = []
    for bits in range(1 << len(edges)):
        reach = [0] * n
        for j, (u, v) in enumerate(edges):
            if not ((bits >> j) & 1):
                u, v = v, u
            reach[u] |= 1 << v
        for k in range(n):
            for i in range(n):
                if (reach[i] >> k) & 1:
                    reach[i] |= reach[k]
        if all(not ((reach[i] >> i) & 1) for i in range(n)):
            out.append(bits)
    return out


def rank_graph(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for a, b in edges:
        a, b = find(a), find(b)
        if a != b:
            parent[a] = b
    return n - len({find(v) for v in range(n)})


def littlestone_dimension(orientations, m):
    if not orientations:
        return -1
    queries = []
    for j in range(m):
        positive = 0
        for i, bits in enumerate(orientations):
            if (bits >> j) & 1:
                positive |= 1 << i
        queries.append(positive)
    whole = (1 << len(orientations)) - 1

    @lru_cache(maxsize=None)
    def dim(mask):
        best = 0
        for positive in queries:
            yes = mask & positive
            no = mask & ~positive
            if yes and no:
                best = max(best, 1 + min(dim(yes), dim(no)))
        return best
    return dim(whole)


def is_cactus(n, edges):
    # Exhaustively find undirected simple cycles via connected degree-two edge sets.
    masks = []
    for mask in range(1 << len(edges)):
        selected = [edge for j, edge in enumerate(edges) if (mask >> j) & 1]
        if len(selected) < 3:
            continue
        incident = set(v for edge in selected for v in edge)
        if len(incident) != len(selected):
            continue
        degree = {v: 0 for v in incident}
        for a, b in selected:
            degree[a] += 1
            degree[b] += 1
        if any(k != 2 for k in degree.values()):
            continue
        seen = {min(incident)}
        frontier = list(seen)
        while frontier:
            x = frontier.pop()
            for a, b in selected:
                y = b if a == x else a if b == x else None
                if y is not None and y not in seen:
                    seen.add(y)
                    frontier.append(y)
        if seen == incident:
            masks.append(mask)
    return all(not (a & b) for a, b in combinations(masks, 2))


def check_certificate():
    p = Path(__file__).resolve().parent / 'certificates' / 'diamond_tree.json'
    document = json.loads(p.read_text(encoding='utf-8'))
    edges = [tuple(e) for e in document['edges']]
    assert edges == [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)]
    orientations = set(acyclic_orientations(4, edges))
    assert len(orientations) == 18
    witnesses = []

    def walk(node, depth, requirements):
        if depth == 4:
            assert set(node) == {'orientation_bits'}
            bits = int(node['orientation_bits'], 2)
            assert len(node['orientation_bits']) == 5
            assert bits in orientations
            assert all(((bits >> j) & 1) == value for j, value in requirements)
            witnesses.append(bits)
            return
        assert set(node) == {'query_edge_index', 'zero', 'one'}
        q = node['query_edge_index']
        assert isinstance(q, int) and 0 <= q < len(edges)
        assert all(q != j for j, _ in requirements)
        walk(node['zero'], depth + 1, requirements + [(q, 0)])
        walk(node['one'], depth + 1, requirements + [(q, 1)])

    walk(document['tree'], 0, [])
    assert len(witnesses) == len(set(witnesses)) == 16
    assert littlestone_dimension(sorted(orientations), len(edges)) == 4
    assert rank_graph(4, edges) == 3
    print('DIAMOND_COMPLETE_TREE_PASS 16 18 3 4')


def check_theta():
    for lengths in [(1, 2, 2), (2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3), (2, 2, 5)]:
        n, edges = 2, []
        for ell in lengths:
            last = 0
            for _ in range(ell - 1):
                edges.append(tuple(sorted((last, n))))
                last = n
                n += 1
            edges.append(tuple(sorted((last, 1))))
        orientations = acyclic_orientations(n, edges)
        assert littlestone_dimension(orientations, len(edges)) == rank_graph(n, edges) + 1
    print('THETA_SUBDIVISION_EXAMPLES_PASS 6')


def check_small_graphs():
    totals = {}
    for n in (4, 5):
        all_edges = list(combinations(range(n), 2))
        tally = [0, 0]
        for mask in range(1 << len(all_edges)):
            edges = [e for j, e in enumerate(all_edges) if (mask >> j) & 1]
            orientations = acyclic_orientations(n, edges)
            actual_dim = littlestone_dimension(orientations, len(edges))
            vc = rank_graph(n, edges)
            cactus = is_cactus(n, edges)
            assert (actual_dim == vc) == cactus, (n, edges, vc, actual_dim, cactus)
            assert actual_dim >= vc
            tally[int(not cactus)] += 1
        totals[n] = tuple(tally)
    assert totals == {4: (57, 7), 5: (623, 401)}
    print('ALL_LABELED_GRAPHS_TO_FIVE_VERTICES_PASS 1088')
    print('CACTUS_NONCACTUS_CENSUS_PASS n4:57,7 n5:623,401')


def main():
    check_certificate()
    check_theta()
    check_small_graphs()
    print('ACYCLIC_ORIENTATION_CACTUS_ALL_CHECKS_PASS')


if __name__ == '__main__':
    main()
