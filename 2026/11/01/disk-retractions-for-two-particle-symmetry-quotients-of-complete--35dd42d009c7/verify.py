#!/usr/bin/env python3
"""Exact finite verification of two-particle complete-bipartite symmetry orbit models.

Run with Python 3: python verify.py
Requires only the standard library and the accompanying quotient_models.json.
"""
import collections
import itertools
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent


def all_nonempty_faces(vertices, edges):
    tris = set()
    for a, b in edges:
        for c, d in edges:
            corners = [('p', a, c), ('p', a, d), ('p', b, d), ('p', b, c)]
            center = ('c', edges.index((a, b)), edges.index((c, d)))
            for k in range(4):
                tris.add(tuple(sorted((center, corners[k], corners[(k + 1) % 4]))))
    one = {(u,) for u in vertices}
    two = {tuple(sorted(edge)) for tri in tris for edge in itertools.combinations(tri, 2)}
    return one | two | tris


def make_quotient(m, n, exchange_sides):
    assert m >= 2 and n >= 2 and (not exchange_sides or m == n)
    v = tuple(range(m + n))
    e = tuple((i, j) for i in range(m) for j in range(m, m + n))
    edge_id = {edge: i for i, edge in enumerate(e)}
    product_vertices = [('p', a, b) for a in v for b in v]
    product_vertices += [('c', i, j) for i in range(len(e)) for j in range(len(e))]
    full = all_nonempty_faces(product_vertices, e)
    diagonal_vertices = {('p', i, i) for i in v}
    diagonal_vertices |= {('c', i, i) for i in range(len(e))}
    diag_faces = {s for s in full if set(s) <= diagonal_vertices}
    assert collections.Counter(map(len, diag_faces)) == {1: m + n + m * n, 2: 2 * m * n}
    retained = {s for s in full if set(s).isdisjoint(diagonal_vertices)}
    assert all(tuple(sorted(t)) in retained for s in retained for k in range(1, len(s) + 1)
               for t in itertools.combinations(s, k))

    group = []
    for a in itertools.permutations(range(m)):
        for b in itertools.permutations(range(n)):
            for flip in ((False, True) if exchange_sides else (False,)):
                f = {i: (m + a[i] if flip else a[i]) for i in range(m)}
                f.update({m + j: (b[j] if flip else m + b[j]) for j in range(n)})
                for exchange_particles in (False, True):
                    group.append((f, exchange_particles))
    assert len(group) == 2 * math.factorial(m) * math.factorial(n) * (2 if exchange_sides else 1)

    def apply(g, vertex):
        permutation, flip_particles = g
        if vertex[0] == 'p':
            x, y = vertex[1:]
            if flip_particles:
                x, y = y, x
            return ('p', permutation[x], permutation[y])
        x, y = vertex[1:]
        if flip_particles:
            x, y = y, x
        a = tuple(sorted(permutation[z] for z in e[x]))
        b = tuple(sorted(permutation[z] for z in e[y]))
        return ('c', edge_id[a], edge_id[b])

    def act_simplex(g, simplex):
        return tuple(sorted(apply(g, t) for t in simplex))

    for simplex in retained:
        for g in group:
            assert act_simplex(g, simplex) in retained

    face_orbit = {}
    face_reps = []
    for face in sorted(retained, key=lambda s: (len(s), s)):
        if face not in face_orbit:
            identifier = len(face_reps)
            face_reps.append(face)
            for g in group:
                face_orbit[act_simplex(g, face)] = identifier
    assert len(face_orbit) == len(retained)

    # All nonempty strict inclusion chains, including vertex < triangle.
    chains = set()
    for top in retained:
        chains.add((top,))
        for size in range(1, len(top)):
            for sub in itertools.combinations(top, size):
                chains.add((sub, top))
        if len(top) == 3:
            for intermediate in itertools.combinations(top, 2):
                for vertex in itertools.combinations(intermediate, 1):
                    chains.add((vertex, intermediate, top))
    chain_orbits = set()
    for chain in chains:
        canonical = min(tuple(act_simplex(g, face) for face in chain) for g in group)
        chain_orbits.add(canonical)
    keyed_orbits = collections.Counter(tuple(face_orbit[face] for face in chain)
                                       for chain in chain_orbits)
    assert max(keyed_orbits.values()) == 1, 'Quotient would be a delta-complex, not the claimed simplicial complex.'
    quotient = {tuple(sorted(key)) for key in keyed_orbits}
    assert len(quotient) == len(chain_orbits)
    assert all(tuple(sorted(t)) in quotient for s in quotient for k in range(1, len(s) + 1)
               for t in itertools.combinations(s, k))
    return quotient, len(group), collections.Counter(map(len, retained)), collections.Counter(map(len, face_reps))


def boundary_and_links(simplices):
    vertices = {t[0] for t in simplices if len(t) == 1}
    edges = {t for t in simplices if len(t) == 2}
    triangles = {t for t in simplices if len(t) == 3}
    triangle_degrees = collections.Counter(tuple(x for x in t if x != v)
                                           for t in triangles for v in t)
    assert all(triangle_degrees[e] in (1, 2) for e in edges)
    assert len(triangle_degrees) == len(edges)
    boundary = {e for e in edges if triangle_degrees[e] == 1}
    graph = collections.defaultdict(set)
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    reached = {min(vertices)}
    while True:
        extended = reached | set().union(*(graph[x] for x in reached))
        if extended == reached:
            break
        reached = extended
    assert reached == vertices
    for v in vertices:
        link_edges = {tuple(x for x in t if x != v) for t in triangles if v in t}
        link_vertices = {u for e in link_edges for u in e}
        assert link_vertices == graph[v]
        degree = collections.Counter(u for e in link_edges for u in e)
        assert all(degree[u] in (1, 2) for u in link_vertices)
        assert sum(degree[u] == 1 for u in link_vertices) in (0, 2)
        seen = {next(iter(link_vertices))}
        while True:
            extended = seen | {u for edge in link_edges if any(w in seen for w in edge) for u in edge}
            if extended == seen:
                break
            seen = extended
        assert seen == link_vertices
    boundary_graph = collections.defaultdict(set)
    for a, b in boundary:
        boundary_graph[a].add(b)
        boundary_graph[b].add(a)
    assert all(len(v) == 2 for v in boundary_graph.values())
    seen = {min(boundary_graph)}
    while True:
        extended = seen | set().union(*(boundary_graph[x] for x in seen))
        if extended == seen:
            break
        seen = extended
    assert seen == set(boundary_graph)
    assert len(vertices) - len(edges) + len(triangles) == 1
    return len(boundary)


def check_collapses(simplices, pairs):
    remaining = set(simplices)
    for small, large in pairs:
        small, large = tuple(small), tuple(large)
        assert small in remaining and large in remaining
        assert len(large) == len(small) + 1 and set(small) < set(large)
        all_cofaces = {f for f in remaining if set(small) < set(f)}
        assert all_cofaces == {large}, (small, large, all_cofaces)
        remaining.remove(small)
        remaining.remove(large)
    assert len(remaining) == 1 and len(next(iter(remaining))) == 1
    return len(pairs)


def run():
    records = json.loads((HERE / 'quotient_models.json').read_text(encoding='utf-8'))
    for key in ('balanced', 'unbalanced'):
        data = records[key]
        m, n = data['representative']
        group_sides = (key == 'balanced')
        q, order, orig, num_face_orbits = make_quotient(m, n, group_sides)
        expected = {tuple(simplex) for simplex in data['simplices']}
        assert q == expected
        assert [orig[k] for k in (1, 2, 3)] == data['retained_face_counts']
        assert [num_face_orbits[k] for k in (1, 2, 3)] == data['face_orbit_counts']
        assert [sum(len(face) == k for face in q) for k in (1, 2, 3)] == data['quotient_face_counts']
        boundary_edges = boundary_and_links(q)
        assert boundary_edges == data['boundary_edges']
        collapses = check_collapses(q, data['collapse_pairs'])
        assert collapses == data['collapse_count']
        print(f'{key.upper()}_VERIFY_OK: group={order}; quotient_faces={data["quotient_face_counts"]}; '
              f'boundary_edges={boundary_edges}; collapses={collapses}')
    # Independent representative sizes, checking stability of face-orbit counts
    # and quotient face numbers under changing the cardinalities of each part.
    for m, n in ((3, 3), (3, 4)):
        key = 'balanced' if m == n else 'unbalanced'
        d = records[key]
        q, order, _, face_orbits = make_quotient(m, n, m == n)
        assert [face_orbits[k] for k in (1, 2, 3)] == d['face_orbit_counts']
        assert [sum(len(t) == k for t in q) for k in (1, 2, 3)] == d['quotient_face_counts']
        assert boundary_and_links(q) == d['boundary_edges']
        print(f'STABILITY_{m}_{n}_OK: group={order}; quotient_faces={d["quotient_face_counts"]}')
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    run()
