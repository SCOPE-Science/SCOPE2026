#!/usr/bin/env python3
"""Exact small-case checks for dense bipartite graph complements and Rips complexes."""
from collections import deque
from itertools import combinations
from math import prod


def deleted_even_cycles(parts):
    """Return the forbidden bipartite 2-factor on two equally sized sides."""
    n = sum(parts)
    edges = set()
    offset = 0
    for ell in parts:
        for j in range(ell):
            b = n + offset + j
            edges.add((offset + j, b))
            edges.add((offset + (j + 1) % ell, b))
        offset += ell
    return n, n, edges


def dense_complement(p, q, forbidden):
    V = p + q
    neigh = [set() for _ in range(V)]
    for a in range(p):
        for b in range(p, V):
            if (a, b) not in forbidden:
                neigh[a].add(b)
                neigh[b].add(a)
    return neigh


def distances(neigh):
    n = len(neigh)
    ans = []
    for root in range(n):
        dist = [-1] * n
        dist[root] = 0
        queue = deque([root])
        while queue:
            v = queue.popleft()
            for w in neigh[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    queue.append(w)
        ans.append(dist)
    return ans


def verify_distances(p, q, forbidden):
    d = distances(dense_complement(p, q, forbidden))
    for u in range(p + q):
        for v in range(u + 1, p + q):
            if (u < p) == (v < p):
                expected = 2
            else:
                expected = 3 if (min(u, v), max(u, v)) in forbidden else 1
            assert d[u][v] == expected, (p, q, u, v, d[u][v], expected)
    return d


def independent_faces(n, forbidden):
    banned = [0] * n
    for u, v in forbidden:
        banned[u] |= 1 << v
        banned[v] |= 1 << u
    families = [[] for _ in range(n)]
    # Enumerate all nonempty independent subsets; no clique-search heuristics.
    for face in range(1, 1 << n):
        good = True
        x = face
        while x:
            vbit = x & -x
            v = vbit.bit_length() - 1
            if face & banned[v]:
                good = False
                break
            x ^= vbit
        if good:
            families[face.bit_count() - 1].append(face)
    while families and not families[-1]:
        families.pop()
    return families


def mod2_rank(columns):
    pivots = {}
    for col in columns:
        while col:
            p = col.bit_length() - 1
            if p not in pivots:
                pivots[p] = col
                break
            col ^= pivots[p]
    return len(pivots)


def betti_mod2(faces):
    sizes = [len(f) for f in faces]
    ranks = []
    for k in range(1, len(faces)):
        row = {mask: i for i, mask in enumerate(faces[k - 1])}
        cols = []
        for face in faces[k]:
            boundary = 0
            for bit in range(face.bit_length()):
                if face & (1 << bit):
                    boundary ^= 1 << row[face ^ (1 << bit)]
            cols.append(boundary)
        ranks.append(mod2_rank(cols))
    result = []
    for k, size in enumerate(sizes):
        out = ranks[k] if k < len(ranks) else 0
        incoming = ranks[k - 1] if k else 0
        b = size - incoming - out - (1 if k == 0 else 0)
        assert b >= 0
        result.append(b)
    return tuple(result), sizes, ranks


def fundamental_cycles(neigh):
    n = len(neigh)
    par = [-1] * n
    depth = [-1] * n
    depth[0] = 0
    todo = deque([0])
    tree = set()
    while todo:
        v = todo.popleft()
        for w in sorted(neigh[v]):
            if depth[w] < 0:
                depth[w] = depth[v] + 1
                par[w] = v
                todo.append(w)
                tree.add(tuple(sorted((v, w))))
    assert all(d >= 0 for d in depth)
    cycles = []
    for u in range(n):
        for v in neigh[u]:
            if u < v and (u, v) not in tree:
                path_u = [u]
                path_v = [v]
                a, b = u, v
                while depth[a] > depth[b]:
                    a = par[a]
                    path_u.append(a)
                while depth[b] > depth[a]:
                    b = par[b]
                    path_v.append(b)
                while a != b:
                    a = par[a]
                    b = par[b]
                    path_u.append(a)
                    path_v.append(b)
                cyc = path_u + path_v[-2::-1]
                assert len(cyc) % 2 == 0
                cycles.append(cyc)
    return cycles


def check_fillings(p, q, forbidden):
    graph = dense_complement(p, q, forbidden)
    cycles = fundamental_cycles(graph)
    for cyc in cycles:
        # Start the alternating cycle at an A-side vertex, then orient A,B,A,B,... .
        if cyc[0] >= p:
            cyc = cyc[1:] + cyc[:1]
        assert all(cyc[i] < p and cyc[i + 1] >= p for i in range(0, len(cyc), 2))
        k = len(cyc) // 2
        aa = cyc[0::2]
        bb = cyc[1::2]
        triangles = []
        for i in range(k):
            triangles.append((aa[i], bb[i], aa[(i + 1) % k]))
        for i in range(1, k - 1):
            triangles.append((aa[0], aa[i], aa[i + 1]))
        # Over F2 the boundary is the original cycle; the same argument
        # with coherent triangle orientations works over Z.
        bdry = set()
        for tri in triangles:
            assert len(set(tri)) == 3
            for a, b in combinations(tri, 2):
                edge = tuple(sorted((a, b)))
                if edge in bdry:
                    bdry.remove(edge)
                else:
                    bdry.add(edge)
        target = set()
        for i in range(len(cyc)):
            target.add(tuple(sorted((cyc[i], cyc[(i + 1) % len(cyc)]))))
        assert bdry == target, (cyc, bdry ^ target)
        # Independently verify the *integral* oriented boundary, not only parity.
        signed = {}

        def add_edge(u, v, coef):
            lo, hi = sorted((u, v))
            signed[(lo, hi)] = signed.get((lo, hi), 0) + (coef if u < v else -coef)

        for u, v, w in triangles:
            add_edge(v, w, 1)
            add_edge(u, w, -1)
            add_edge(u, v, 1)
        for i, u in enumerate(cyc):
            v = cyc[(i + 1) % len(cyc)]
            add_edge(u, v, -1)
        assert all(c == 0 for c in signed.values()), (cyc, signed)
    return len(cycles)


def check_case(parts):
    p, q, forbidden = deleted_even_cycles(parts)
    n = p + q
    assert p >= 5
    d = verify_distances(p, q, forbidden)
    faces = independent_faces(n, forbidden)
    # Direct comparison: scale-two metric adjacency is the complement
    # of forbidden adjacency, on every subset, not merely on homology.
    for dimfaces in faces:
        for face in dimfaces:
            verts = [i for i in range(n) if face & (1 << i)]
            assert all(d[u][v] <= 2 for u, v in combinations(verts, 2))
    assert all(d[u][v] > 2 for u, v in forbidden)
    betti, sizes, ranks = betti_mod2(faces)
    D = sum((2 * ell + 1) // 3 for ell in parts) - 1
    h = sum(ell % 3 == 0 for ell in parts)
    assert D >= 2
    assert betti == tuple((2**h if k == D else 0) for k in range(len(betti))), (parts, betti, D, h)
    loops = check_fillings(p, q, forbidden)
    assert loops == p * q - len(forbidden) - (p + q) + 1
    return parts, D, 2**h, loops, len(faces), sum(sizes), len(ranks)


def main():
    cases = [
        [5], [2, 3],
        [6], [2, 4], [3, 3], [2, 2, 2],
        [7], [2, 5], [3, 4], [2, 2, 3],
        [8], [2, 6], [3, 5], [4, 4], [2, 2, 4], [2, 3, 3], [2, 2, 2, 2],
    ]
    for parts in cases:
        r = check_case(parts)
        print('case', ','.join(map(str, r[0])), 'sphere_degree', r[1], 'multiplicity', r[2], 'one_cycles', r[3], 'faces', r[5])
    # Non-regular forbidden graphs on unequal bipartition sizes test
    # the full graph-square transfer independently of the 2-factor formula.
    examples = [
        (5, 5, {(0, 5), (0, 6), (1, 6), (2, 8), (3, 9)}),
        (7, 8, {(0, 7), (0, 8), (0, 9), (1, 7), (1, 11), (2, 8), (2, 10),
                (3, 11), (3, 12), (4, 9), (4, 13), (5, 10), (6, 12), (6, 14)}),
    ]
    for p, q, forbidden in examples:
        da = max(sum(a == x for a, _ in forbidden) for x in range(p))
        db = max(sum(b == y for _, b in forbidden) for y in range(p, p + q))
        assert q > 2 * da and p > 2 * db
        verify_distances(p, q, forbidden)
        count = check_fillings(p, q, forbidden)
        print('irregular', p, q, 'forbidden', len(forbidden), 'fundamental_cycles', count)
    print('VERIFY_OK cycle_partitions=17 irregular_examples=2 Rips_equals_Ind=yes integral_cycle_fillings_checked=yes')


if __name__ == '__main__':
    main()
