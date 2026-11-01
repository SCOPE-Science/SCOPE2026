#!/usr/bin/env python3
"""Finite checks for the geometric-reflection fixed spaces of Möbius-ladder independence complexes.

Uses only Python's standard library. The all-size proof is in RESULT.md.
"""
from collections import defaultdict


def mobius_edges(n):
    N = 2 * n
    return {tuple(sorted((u, v))) for u, v in
            ([(i, (i + 1) % N) for i in range(N)] +
             [(i, (i + n) % N) for i in range(n)])}


def reflection_graph(n, c):
    N = 2 * n
    edges = mobius_edges(n)
    orbit = lambda i: tuple(sorted({i, (c - i) % N}))
    orbits = {orbit(i) for i in range(N)}
    allowed = {o for o in orbits if len(o) == 1 or tuple(o) not in edges}
    quotient_edges = {frozenset({orbit(u), orbit(v)})
                      for u, v in edges if orbit(u) in allowed
                      and orbit(v) in allowed and orbit(u) != orbit(v)}
    return allowed, quotient_edges, orbit


def ladder_map(n, c):
    # Map ladder vertices (rail, column) to actual reflection orbits.
    if c == 0:
        m = (n + 1) // 2
        def representative(rail, j):
            return j if rail == 0 else n - j
    else:
        m = n // 2 - 1
        def representative(rail, j):
            return j + 2 if rail == 0 else n - 1 - j
    _, _, orbit = reflection_graph(n, c)
    return m, {(rail, j): orbit(representative(rail, j))
               for rail in (0, 1) for j in range(m)}


def verify_orbit_graph(n, c):
    allowed, qe, _ = reflection_graph(n, c)
    m, coordinates = ladder_map(n, c)
    assert len(coordinates) == len(allowed) == 2 * m
    assert len(set(coordinates.values())) == len(allowed)
    assert set(coordinates.values()) == allowed
    expected = set()
    for j in range(m):
        expected.add(frozenset((coordinates[0, j], coordinates[1, j])))
    for rail in (0, 1):
        for j in range(m - 1):
            expected.add(frozenset((coordinates[rail, j], coordinates[rail, j + 1])))
    assert qe == expected, (n, c, qe - expected, expected - qe)
    return m


def independent_faces(vertices, edges):
    vertices = list(vertices)
    adj = {v: set() for v in vertices}
    for e in edges:
        u, v = tuple(e)
        adj[u].add(v)
        adj[v].add(u)
    faces = defaultdict(list)
    def rec(i, chosen):
        if i == len(vertices):
            faces[len(chosen) - 1].append(frozenset(chosen))
            return
        rec(i + 1, chosen)
        v = vertices[i]
        if not adj[v].intersection(chosen):
            chosen.append(v)
            rec(i + 1, chosen)
            chosen.pop()
    rec(0, [])
    return faces


def gf2_rank(columns):
    pivots = {}
    for column in columns:
        x = column
        while x:
            pivot = x.bit_length() - 1
            if pivot in pivots:
                x ^= pivots[pivot]
            else:
                pivots[pivot] = x
                break
    return len(pivots)


def reduced_betti(faces):
    # Includes the augmented degree-minus-one group of rank one.
    dimensions = sorted(faces)
    assert dimensions and dimensions[0] == -1
    ranks = {}
    for d in dimensions:
        if d == -1:
            ranks[d] = 0
        else:
            preceding = {f: i for i, f in enumerate(faces[d - 1])}
            cols = []
            for f in faces[d]:
                bits = 0
                for v in f:
                    bits ^= (1 << preceding[f - {v}])
                cols.append(bits)
            ranks[d] = gf2_rank(cols)
    return {d: len(faces[d]) - ranks[d] - ranks.get(d + 1, 0)
            for d in dimensions if d >= 0
            and len(faces[d]) - ranks[d] - ranks.get(d + 1, 0) != 0}


def ambient_betti(n):
    vertices = tuple(range(2 * n))
    edges = frozenset(map(frozenset, mobius_edges(n)))
    return reduced_betti(independent_faces(vertices, edges))



def subgroup_quotient(n, a, b=None):
    """Directly form actual vertex orbits of the subgroup of the dihedral group."""
    N = 2 * n
    unseen = set(range(N))
    vertex_orbit = {}
    all_orbits = set()
    while unseen:
        seed = next(iter(unseen))
        orbit = {seed}
        frontier = [seed]
        while frontier:
            v = frontier.pop()
            successors = [(v + a) % N]
            if b is not None:
                successors.append((b - v) % N)
            for w in successors:
                if w not in orbit:
                    orbit.add(w)
                    frontier.append(w)
        o = tuple(sorted(orbit))
        all_orbits.add(o)
        unseen -= orbit
        for v in orbit:
            vertex_orbit[v] = o
    orig = mobius_edges(n)
    forbidden = {vertex_orbit[u] for u, v in orig
                 if vertex_orbit[u] == vertex_orbit[v]}
    permitted = all_orbits - forbidden
    quotient_edges = {frozenset((vertex_orbit[u], vertex_orbit[v]))
                      for u, v in orig if vertex_orbit[u] != vertex_orbit[v]
                      and vertex_orbit[u] in permitted
                      and vertex_orbit[v] in permitted}
    return permitted, quotient_edges, vertex_orbit


def verify_subgroup(n, a, b=None):
    from math import gcd
    d = gcd(2 * n, a)
    V, E, vertex_orbit = subgroup_quotient(n, a, b)
    if n % d == 0:
        assert len(V) == len(E) == 0, (n, a, b, 'expected empty')
        return 'empty'
    assert d % 2 == 0
    if b is None:
        expected_vertices = {vertex_orbit[j] for j in range(d)}
        expected_edges = set()
        for j in range(d):
            expected_edges.add(frozenset((vertex_orbit[j], vertex_orbit[(j+1)%d])))
            expected_edges.add(frozenset((vertex_orbit[j], vertex_orbit[(j+d//2)%d])))
        assert V == expected_vertices and E == expected_edges, (n, a, 'cyclic')
        return 'mobius_' + str(d)
    m = d // 2
    residue_good, residue_edges, _ = reflection_graph(m, b % d)
    projected_vertices = {vertex_orbit[o[0]] for o in residue_good}
    projected_edges = {frozenset(vertex_orbit[o[0]] for o in edge) for edge in residue_edges}
    assert len(projected_vertices) == len(residue_good)
    assert V == projected_vertices and E == projected_edges, (n, a, b, 'dihedral')
    if b % 2:
        rung_count = max(0, m // 2 - 1)
    else:
        rung_count = (m + 1) // 2
    assert len(V) == 2 * rung_count
    if rung_count:
        verify_orbit_graph(m, b % 2)
    return 'ladder_' + str(rung_count)

def main():
    for n in range(4, 121):
        assert verify_orbit_graph(n, 0) == (n + 1) // 2
        assert verify_orbit_graph(n, 1) == n // 2 - 1
    print('ORBIT_GRAPH_OK n=4..120, both reflection classes')
    for n in range(4, 19):
        for c in (0, 1):
            V, E, _ = reflection_graph(n, c)
            m = verify_orbit_graph(n, c)
            predicted = {(m - 1) // 2: 1}
            actual = reduced_betti(independent_faces(V, E))
            assert actual == predicted, (n, c, actual, predicted)
    print('FIXED_HOMOLOGY_OK n=4..18, both classes, exact augmented GF(2) boundaries')
    for n in range(4, 10):
        actual = ambient_betti(n)
        if n % 4 == 2:
            predicted = {n // 2 - 1: 3}
        elif n % 4 == 0:
            predicted = {n // 2 - 1: 1}
        else:
            predicted = {((n - 1) // 2 if n % 4 == 1 else (n - 3) // 2): 1}
        assert actual == predicted, (n, actual, predicted)
    print('AMBIENT_HOMOLOGY_OK n=4..9, source homology dimensions corroborated')
    assert verify_orbit_graph(3, 0) == 2
    assert verify_orbit_graph(3, 1) == 0
    print('LOW_BOUNDARY_OK n=3, one S^0 and one empty fixed space')
    cases = 0
    for n in range(4, 25):
        for d in range(1, 2*n+1):
            if (2*n) % d:
                continue
            a = d if d < 2*n else 0
            verify_subgroup(n, a)
            cases += 1
            for b in range(d):
                verify_subgroup(n, a, b)
                cases += 1
    for n in range(4, 14):
        for a in range(2*n):
            verify_subgroup(n, a)
            cases += 1
            for b in range(2*n):
                verify_subgroup(n, a, b)
                cases += 1
    print(f'ALL_SUBGROUPS_OK {cases} direct subgroup orbit-graph comparisons')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
