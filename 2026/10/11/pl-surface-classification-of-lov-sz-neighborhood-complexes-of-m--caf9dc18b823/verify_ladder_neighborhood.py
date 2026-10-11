#!/usr/bin/env python3
"""Standalone finite checks for the open-neighborhood complexes of cyclic ladders.
The proof of the all-parameter theorem is combinatorial and appears in RESULT.md.
This script supplies independent finite cross-checks, not an infinite certificate.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations


def graph(kind, n):
    if kind == 'mobius':
        size = 2 * n
        edges = set()
        for i in range(size):
            for j in ((i - 1) % size, (i + 1) % size, (i + n) % size):
                edges.add(tuple(sorted((i, j))))
    else:
        size = 2 * n
        vertices = lambda i, a: 2 * (i % n) + a
        edges = set()
        for i in range(n):
            for a in (0, 1):
                for j in (vertices(i + 1, a), vertices(i, 1 - a)):
                    edges.add(tuple(sorted((vertices(i, a), j))))
    adjacency = {i: set() for i in range(size)}
    for i, j in edges:
        adjacency[i].add(j)
        adjacency[j].add(i)
    assert all(len(a) == 3 for a in adjacency.values())
    return adjacency


def components(nodes, adjacency):
    remaining = set(nodes)
    answer = []
    while remaining:
        root = min(remaining)
        remaining.remove(root)
        cc = {root}
        frontier = [root]
        while frontier:
            for v in adjacency[frontier.pop()] & remaining:
                cc.add(v)
                remaining.remove(v)
                frontier.append(v)
        answer.append(cc)
    return answer


def boundary_sign(triangle, edge):
    tri = tuple(sorted(triangle))
    e = tuple(sorted(edge))
    assert set(e) <= set(tri)
    missing = next(i for i, v in enumerate(tri) if v not in e)
    return (-1) ** missing


def calculate(kind, n):
    G = graph(kind, n)
    T = sorted(set(tuple(sorted(neigh)) for neigh in G.values()))
    faces = {k: set() for k in (0, 1, 2)}
    for t in T:
        for k in (1, 2, 3):
            for face in combinations(t, k):
                faces[k - 1].add(face)
    V, E, F = (len(faces[d]) for d in (0, 1, 2))
    assert V == 2 * n
    edge_faces = defaultdict(list)
    for j, t in enumerate(T):
        for e in combinations(t, 2):
            edge_faces[e].append(j)
    assert max(map(len, edge_faces.values())) <= 2

    skeleton = defaultdict(set)
    for x, y in faces[1]:
        skeleton[x].add(y)
        skeleton[y].add(x)
    cc = components(set(x[0] for x in faces[0]), skeleton)

    B = {e for e, ff in edge_faces.items() if len(ff) == 1}
    boundary_adj = defaultdict(set)
    for a, b in B:
        boundary_adj[a].add(b)
        boundary_adj[b].add(a)
    BC = components(boundary_adj, boundary_adj) if B else []
    assert all(len(boundary_adj[v]) == 2 for v in boundary_adj)

    link_shapes = Counter()
    for v in G:
        link = [set(x for x in t if x != v) for t in T if v in t]
        link_edges = [tuple(sorted(p)) for p in link]
        link_vertices = set(x for p in link for x in p)
        deg = Counter(x for e in link_edges for x in e)
        if len(link_edges) == len(link_vertices) and set(deg.values()) == {2}:
            link_shapes['circle'] += 1
        elif len(link_edges) + 1 == len(link_vertices) and list(deg.values()).count(1) == 2 and all(d in (1,2) for d in deg.values()):
            link_shapes['interval'] += 1
        else:
            raise AssertionError(('bad link', kind, n, v, link_edges))
    # Since vertex links are intervals or circles and edge multiplicity <=2,
    # this is a compact triangulated 2-manifold (possibly disconnected).
    assert link_shapes['interval'] == len(boundary_adj)

    # Independently propagate orientations through the triangle dual graph.
    orientation = {}
    dual = defaultdict(list)
    for edge, fs in edge_faces.items():
        if len(fs) == 2:
            i, j = fs
            factor = -boundary_sign(T[i], edge) * boundary_sign(T[j], edge)
            dual[i].append((j, factor))
            dual[j].append((i, factor))
    orientable = True
    for start in range(len(T)):
        if start in orientation:
            continue
        orientation[start] = 1
        pending = [start]
        while pending:
            u = pending.pop()
            for v, factor in dual[u]:
                candidate = factor * orientation[u]
                if v not in orientation:
                    orientation[v] = candidate
                    pending.append(v)
                elif orientation[v] != candidate:
                    orientable = False

    # Ranks of mod-2 boundary maps for corroboration, using integer bitsets.
    basis = {}
    for triangle in T:
        x = 0
        for edge in combinations(triangle, 2):
            eidx = sorted(faces[1]).index(edge)
            x ^= 1 << eidx
        while x:
            leading = x.bit_length() - 1
            if leading in basis:
                x ^= basis[leading]
            else:
                basis[leading] = x
                break
    rank2 = len(basis)
    beta2 = F - rank2
    beta1 = E - V + len(cc) - rank2
    assert beta1 >= 0 and beta2 >= 0
    return dict(kind=kind, n=n, V=V, E=E, F=F, components=len(cc),
                chi=V-E+F, boundary_components=len(BC),
                boundary_cycles=sorted(map(len, BC)),
                orientable=orientable, beta1=beta1, beta2=beta2,
                link_shapes=dict(link_shapes))


def expected(kind, n):
    if kind == 'mobius':
        if n == 2:
            return dict(components=1,chi=2,boundary_components=0,beta1=0,beta2=1,orientable=True)
        if n == 3:
            return dict(components=2,chi=2,boundary_components=2,beta1=0,beta2=0,orientable=True)
        if n % 2 == 0:
            return dict(components=1,chi=0,boundary_components=2,beta1=1,beta2=0,orientable=True)
        return dict(components=2,chi=0,boundary_components=2,beta1=2,beta2=0,orientable=False)
    if n == 4:
        return dict(components=2,chi=4,boundary_components=0,beta1=0,beta2=2,orientable=True)
    if n % 2 == 0:
        return dict(components=2,chi=0,boundary_components=4,beta1=2,beta2=0,orientable=True)
    return dict(components=1,chi=0,boundary_components=2,beta1=1,beta2=0,orientable=True)


def main():
    count = 0
    for kind, n0 in [('mobius', 2), ('prism', 3)]:
        for n in range(n0, 31):
            result = calculate(kind, n)
            expected_results = expected(kind, n)
            for k, expected_value in expected_results.items():
                assert result[k] == expected_value, (kind, n, k, result[k], expected_value)
            if kind == 'mobius' and n >= 4:
                assert result['boundary_cycles'] == [n, n]
                assert result['link_shapes'] == {'interval': 2*n}
            if kind == 'prism' and n >= 5:
                assert result['boundary_cycles'] == ([n,n] if n % 2 else [n//2]*4)
                assert result['link_shapes'] == {'interval': 2*n}
            count += 1
    print('VERIFY_OK cases=%d mobius_n=2..30 prism_n=3..30 manifold_links=yes orientation=yes mod2_homology=yes' % count)


if __name__ == '__main__':
    main()
