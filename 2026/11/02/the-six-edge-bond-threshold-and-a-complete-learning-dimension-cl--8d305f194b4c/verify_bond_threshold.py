"""Standalone exact checks for bond concepts of finite simple graphs.

Only Python's standard library is required. Bit i encodes edge i. The
Littlestone recurrence is evaluated exactly over finite version spaces.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product
import json
from pathlib import Path

HOUSE_EDGES = [(0, 1), (0, 4), (1, 4), (0, 3), (2, 3), (1, 2)]


def connected(vertices, edges):
    if len(vertices) < 2:
        return True
    vertices = set(vertices)
    seen = {min(vertices)}
    while True:
        newer = seen | {b for a,b in edges if a in seen and b in vertices} \
                    | {a for a,b in edges if b in seen and a in vertices}
        if newer == seen:
            return seen == vertices
        seen = newer


def bond_masks(n, edges):
    """Connected bipartitions; each unordered cut is represented once."""
    if not connected(range(n), edges):
        raise ValueError('Graph is not connected')
    ans = set()
    full = set(range(n))
    for bits in range(1 << (n - 1)):
        A = {0} | {i + 1 for i in range(n - 1) if bits >> i & 1}
        B = full - A
        if B and connected(A, edges) and connected(B, edges):
            ans.add(sum(1 << k for k, (a, b) in enumerate(edges)
                        if (a in A) != (b in A)))
    return sorted(ans)


def bond_masks_by_deletion(n, edges):
    """Independent check: inclusion-minimal disconnecting edge subsets."""
    m = len(edges)
    ans = set()
    for mask in range(1, 1 << m):
        remaining = [e for k, e in enumerate(edges) if not (mask >> k & 1)]
        if connected(range(n), remaining):
            continue
        if all(connected(range(n), [e for k, e in enumerate(edges)
                                    if not ((mask ^ (1 << bit)) >> k & 1)])
               for bit in range(m) if mask >> bit & 1):
            ans.add(mask)
    return sorted(ans)


def vc_dimension(concepts, edge_count):
    for size in range(min(edge_count, len(concepts)), -1, -1):
        for chosen in combinations(range(edge_count), size):
            traces = {sum(((concept >> bit) & 1) << j
                          for j, bit in enumerate(chosen)) for concept in concepts}
            if len(traces) == (1 << size):
                return size
    raise AssertionError('Empty support must be shattered for a nonempty class')


def littlestone_dimension(concepts, edge_count):
    masks = [sum(1 << j for j, c in enumerate(concepts) if c >> i & 1)
             for i in range(edge_count)]

    @lru_cache(None)
    def rank(space):
        best = 0
        for mask in masks:
            positive, negative = space & mask, space & ~mask
            if positive and negative:
                best = max(best, 1 + min(rank(positive), rank(negative)))
        return best

    return rank((1 << len(concepts)) - 1)


def house_tree_certificate(concepts):
    masks = [sum(1 << j for j, c in enumerate(concepts) if c >> i & 1)
             for i in range(len(HOUSE_EDGES))]

    @lru_cache(None)
    def feasible(space, depth):
        if depth == 0:
            return bool(space)
        return any(feasible(space & m, depth - 1) and
                   feasible(space & ~m, depth - 1) for m in masks)

    def build(space, depth):
        if depth == 0:
            return {'witness': concepts[(space & -space).bit_length() - 1]}
        for i, m in enumerate(masks):
            if feasible(space & ~m, depth - 1) and feasible(space & m, depth - 1):
                return {'query_edge': i,
                        'zero': build(space & ~m, depth - 1),
                        'one': build(space & m, depth - 1)}
        raise AssertionError('No depth certificate')

    all_space = (1 << len(concepts)) - 1
    assert feasible(all_space, 3)
    return build(all_space, 3)


def check_certificate(node, concepts, path=()):
    if 'witness' in node:
        witness = node['witness']
        assert witness in concepts
        assert all(((witness >> edge) & 1) == bit for edge, bit in path)
        return [witness]
    edge = node['query_edge']
    assert 0 <= edge < len(HOUSE_EDGES)
    assert all(previous_edge != edge for previous_edge, _ in path)
    return (check_certificate(node['zero'], concepts, path + ((edge, 0),)) +
            check_certificate(node['one'], concepts, path + ((edge, 1),)))


def theta_bonds(a, b, c):
    assert a >= 1 and b >= 2 and c >= b
    parts = (range(a), range(a, a + b), range(a + b, a + b + c))
    return sorted([sum(1 << x for x in pair)
                   for part in parts for pair in combinations(part, 2)] +
                  [sum(1 << x for x in triple) for triple in product(*parts)])


def theta_graph(a, b, c):
    """Three internally disjoint paths between endpoints 0 and 1."""
    paths = []
    count = 2
    for length in (a, b, c):
        internal = list(range(count, count + length - 1))
        count += length - 1
        route = [0] + internal + [1]
        paths.append([(route[j], route[j+1]) for j in range(length)])
    edges = [e for path in paths for e in path]
    assert len(set(map(frozenset, edges))) == len(edges)
    return count, edges


def canonical_edges(n, edges):
    positions = {edge: i for i, edge in enumerate(combinations(range(n), 2))}
    best = None
    for sigma in permutations(range(n)):
        signature = sum(1 << positions[tuple(sorted((sigma[u], sigma[v])))]
                        for u, v in edges)
        if best is None or signature < best:
            best = signature
    return best


def run(certificate_path=None):
    house = bond_masks(5, HOUSE_EDGES)
    assert house == [6, 11, 13, 19, 21, 24, 35, 37, 40, 48]
    assert house == bond_masks_by_deletion(5, HOUSE_EDGES)
    assert (vc_dimension(house, 6), littlestone_dimension(house, 6)) == (2, 3)
    assert house == theta_bonds(1, 2, 3)
    assert all(len({sum((c >> i & 1) << j for j, i in enumerate(S))
                    for c in house}) < 8 for S in combinations(range(6), 3))
    t = house_tree_certificate(house)
    witness = check_certificate(t, house)
    assert len(witness) == 8 and len(set(witness)) == 8
    if certificate_path is not None:
        with open(certificate_path, encoding='utf-8') as fp:
            cert = json.load(fp)
        assert cert['edges'] == [list(edge) for edge in HOUSE_EDGES]
        assert cert['bond_masks'] == house
        assert cert['depth_three_tree'] == t

    # The abstract theta formula must agree with two unrelated graph tests.
    tests = [(1,2,2),(1,2,3),(1,2,4),(1,3,3),(1,3,4),
             (2,2,2),(2,2,3),(2,3,3),(3,3,3)]
    for a,b,c in tests:
        n, edges = theta_graph(a,b,c)
        expected = theta_bonds(a,b,c)
        direct = bond_masks(n, edges)
        assert direct == expected
        assert direct == bond_masks_by_deletion(n, edges)
        vc = vc_dimension(direct, a+b+c)
        ld = littlestone_dimension(direct, a+b+c)
        if a >= 2:
            assert (vc, ld) == (3,3)
        elif (b,c) == (2,2):
            assert (vc,ld) == (2,2)
        else:
            assert (vc,ld) == (2,3)
    print('THETA_GRAPH_BOND_FORMULAS_PASS tests=%d' % len(tests))

    # All connected labeled simple graphs on <=5 vertices, <=6 edges.
    # Larger connected graphs with <=6 edges are trees or unicyclic.
    by_order = Counter()
    gap = []
    for n in range(2,6):
        universe = list(combinations(range(n), 2))
        for chosen_size in range(n - 1, min(len(universe), 6) + 1):
            for chosen in combinations(universe, chosen_size):
                if not connected(range(n), chosen):
                    continue
                B = bond_masks(n, chosen)
                assert B == bond_masks_by_deletion(n, chosen)
                v = vc_dimension(B, chosen_size)
                ell = littlestone_dimension(B, chosen_size)
                by_order[(n,chosen_size)] += 1
                if ell > v:
                    gap.append((n, chosen_size, chosen, v, ell))
    assert len(gap) == 60
    assert all(n == 5 and m == 6 and (v, ell) == (2,3)
               for n,m,_,v,ell in gap)
    iso = canonical_edges(5, HOUSE_EDGES)
    assert all(canonical_edges(5, edges) == iso for _,_,edges,_,_ in gap)
    print('EXHAUSTIVE_SHARP_SIX_EDGE_THRESHOLD_PASS',
          'connected_labeled_graphs=%d' % sum(by_order.values()),
          'exceptional_labelings=%d' % len(gap),
          'exceptional_isomorphism_types=1')
    print('HOUSE_CERTIFICATE_PASS leaves=8 bonds=10 vc=2 ldim=3')
    print('ALL_GRAPHIC_BOND_SHATTERING_CHECKS_PASS')
    return t, house, by_order


if __name__ == '__main__':
    import sys
    run(Path(sys.argv[1]) if len(sys.argv) > 1 else None)
