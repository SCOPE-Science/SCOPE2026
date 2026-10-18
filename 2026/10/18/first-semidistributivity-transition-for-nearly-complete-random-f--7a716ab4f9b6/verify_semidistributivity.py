#!/usr/bin/env python3
"""Exact finite checks for semidistributive concept lattices from missing-incidence trees.

Only Python's standard library is required. Every labelled tree up to seven
vertices is generated exactly once from its Prufer sequence, and the FCA
closure is recomputed from the complementary incidence relation.
"""
from itertools import product
from collections import Counter
from math import factorial


def prufer_edges(n, code):
    if n == 1:
        return []
    deg = [1] * n
    for v in code:
        deg[v] += 1
    edges = []
    for v in code:
        leaf = next(i for i, d in enumerate(deg) if d == 1)
        edges.append((leaf, v))
        deg[leaf] -= 1
        deg[v] -= 1
    u, v = [i for i, d in enumerate(deg) if d == 1]
    edges.append((u, v))
    return edges


def bipartition(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    color = [-1] * n
    color[0] = 0
    queue = [0]
    for a in queue:
        for b in adj[a]:
            if color[b] < 0:
                color[b] = color[a] ^ 1
                queue.append(b)
            else:
                assert color[b] != color[a]
    return ([i for i in range(n) if color[i] == 0],
            [i for i in range(n) if color[i] == 1])


def extents_and_ops(n_objects, n_attributes, missing_edges):
    """Return every closed object extent as a bitmask and its closure table."""
    missing = [0] * n_objects
    for i, j in missing_edges:
        missing[i] |= 1 << j
    full_a = (1 << n_attributes) - 1
    closed = []
    for s in range(1 << n_objects):
        forbidden = 0
        for i in range(n_objects):
            if s & (1 << i):
                forbidden |= missing[i]
        common = full_a & ~forbidden
        x = 0
        for i in range(n_objects):
            if not missing[i] & common:
                x |= 1 << i
        closed.append(x)
    return sorted(set(closed)), closed


def semidistributive(extents, closure):
    # For closed extents: meet is intersection and join is closure of union.
    for x in extents:
        for y in extents:
            for z in extents:
                xy, xz = closure[x | y], closure[x | z]
                if xy == xz and closure[x | (y & z)] != xy:
                    return False, ('join', x, y, z, xy, closure[x | (y & z)])
                xy, xz = x & y, x & z
                if xy == xz and x & closure[y | z] != xy:
                    return False, ('meet', x, y, z, xy, x & closure[y | z])
    return True, None


def check_all_labelled_trees():
    counts = []
    for n in range(1, 8):
        bad = 0
        paths = 0
        for code in product(range(n), repeat=max(0, n - 2)):
            edges = prufer_edges(n, code)
            left, right = bipartition(n, edges)
            index_l = {v: i for i, v in enumerate(left)}
            index_r = {v: i for i, v in enumerate(right)}
            missing = []
            for a, b in edges:
                if a in index_l:
                    missing.append((index_l[a], index_r[b]))
                else:
                    missing.append((index_l[b], index_r[a]))
            E, close = extents_and_ops(len(left), len(right), missing)
            ok, witness = semidistributive(E, close)
            degrees = Counter(u for e in edges for u in e)
            is_path = n >= 2 and max(degrees.values()) <= 2
            paths += is_path
            if not ok:
                bad += 1
                assert n == 7 and is_path, (n, edges, witness)
            if n == 7 and is_path:
                assert not ok, (n, edges)
        total = n ** (n - 2) if n >= 2 else 1
        if n == 7:
            assert bad == paths == factorial(7) // 2 == 2520
        else:
            assert bad == 0
        counts.append((n, total, bad, paths))
    return counts


def check_explicit_witness():
    # Missing incidence edges form O0-A0-O1-A1-O2-A2-O3.
    M = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2)]
    ext, close = extents_and_ops(4, 3, M)
    assert ext == [0, 1, 3, 9, 12, 8, 15] or sorted(ext) == [0, 1, 3, 8, 9, 12, 15]
    x, y, z = 0b1001, 0b0011, 0b1100
    assert x in ext and y in ext and z in ext
    assert close[x | y] == close[x | z] == 15
    assert close[x | (y & z)] == x == 9
    return sorted(ext)


def independent_sets_equivalence():
    # Verify the complement-context concepts = maximal independent sets.
    cases = 0
    for n_o, n_a in [(2, 3), (3, 3)]:
        e_all = [(i, j) for i in range(n_o) for j in range(n_a)]
        for pattern in range(1 << len(e_all)):
            E = [e for i, e in enumerate(e_all) if pattern & (1 << i)]
            ext, close = extents_and_ops(n_o, n_a, E)
            found = set()
            for mask in range(1 << (n_o + n_a)):
                left = {i for i in range(n_o) if mask & (1 << i)}
                right = {j for j in range(n_a) if mask & (1 << (n_o + j))}
                if any((i, j) in E for i in left for j in right):
                    continue
                if any(all((i, j) not in E for j in right) for i in range(n_o) if i not in left):
                    continue
                if any(all((i, j) not in E for i in left) for j in range(n_a) if j not in right):
                    continue
                found.add(sum(1 << i for i in left))
            assert found == set(ext)
            cases += 1
    return cases


if __name__ == '__main__':
    print('TREE_CENSUS', check_all_labelled_trees())
    print('P7_EXTENTS', check_explicit_witness())
    print('MIS_FCA_EQUIVALENCE', independent_sets_equivalence())
    print('VERIFY_OK')
