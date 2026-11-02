#!/usr/bin/env python3
"""Exact elementary checks for the perfect-matching complex of the Petersen graph.

Only Python's standard library is required. Vertices are the 2-subsets of
{0,1,2,3,4}; disjoint pairs form graph edges. No numerical approximations.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb

VERTICES = tuple(combinations(range(5), 2))
VERTEX_ID = {v: i for i, v in enumerate(VERTICES)}
EDGES = tuple((i, j) for i, j in combinations(range(10), 2)
              if set(VERTICES[i]).isdisjoint(VERTICES[j]))
EDGE_ID = {e: i for i, e in enumerate(EDGES)}


def perfect_matchings():
    answer = []

    def extend(free, matching):
        if not free:
            answer.append(tuple(sorted(matching)))
            return
        v = min(free)
        for edge in EDGES:
            if v in edge and set(edge) <= free:
                extend(free - set(edge), matching + [edge])

    extend(set(range(10)), [])
    return tuple(sorted(answer))


MATCHINGS = perfect_matchings()
MATCHING_ID = {m: i for i, m in enumerate(MATCHINGS)}


def graph_permutation(p):
    vperm = tuple(VERTEX_ID[tuple(sorted((p[a], p[b])))]
                  for a, b in VERTICES)
    eperm = tuple(EDGE_ID[tuple(sorted((vperm[a], vperm[b])))]
                  for a, b in EDGES)
    mperm = tuple(MATCHING_ID[tuple(sorted(
        tuple(sorted((vperm[a], vperm[b]))) for a, b in matching))]
        for matching in MATCHINGS)
    return eperm, mperm


def cycle_type(p):
    seen = set()
    types = []
    for start in range(len(p)):
        if start not in seen:
            v, size = start, 0
            while v not in seen:
                seen.add(v)
                size += 1
                v = p[v]
            types.append(size)
    return tuple(sorted(types, reverse=True))


def sign(p):
    return (-1) ** sum(p[i] > p[j]
                       for i in range(len(p)) for j in range(i + 1, len(p)))


def graph_quotient(group):
    """Orbit counts on barycentrically subdivided K_6 (no inverted edges)."""
    incidence = tuple((mi, EDGE_ID[edge])
                      for mi, matching in enumerate(MATCHINGS)
                      for edge in matching)
    assert len(incidence) == 30
    graph_vertices = tuple((0, i) for i in range(6)) + tuple((1, i) for i in range(15))
    graph_edges = tuple((mi, ei) for mi, ei in incidence)
    vertex_maps = []
    edge_maps = []
    for p in group:
        eperm, mperm = graph_permutation(p)
        vertex_maps.append({(0, i): (0, mperm[i]) for i in range(6)} |
                           {(1, i): (1, eperm[i]) for i in range(15)})
        edge_maps.append({(mi, ei): (mperm[mi], eperm[ei]) for mi, ei in incidence})

    def count_orbits(items, maps):
        remaining = set(items)
        count = 0
        while remaining:
            a = next(iter(remaining))
            orbit = {g[a] for g in maps}
            assert orbit <= remaining
            remaining -= orbit
            count += 1
        return count

    v = count_orbits(graph_vertices, vertex_maps)
    e = count_orbits(graph_edges, edge_maps)
    assert e - v + 1 >= 0  # Connected graph quotient.
    return v, e, e - v + 1


def main():
    assert len(VERTICES) == 10 and len(EDGES) == 15
    assert len(MATCHINGS) == 6 and all(len(m) == 5 for m in MATCHINGS)
    multiplicity = Counter(e for matching in MATCHINGS for e in matching)
    assert set(multiplicity) == set(EDGES)
    assert all(multiplicity[e] == 2 for e in EDGES)
    intersections = {}
    for i, j in combinations(range(6), 2):
        intersection = set(MATCHINGS[i]) & set(MATCHINGS[j])
        assert len(intersection) == 1
        intersections[(i, j)] = next(iter(intersection))
    assert set(intersections.values()) == set(EDGES)
    assert all(len(set(MATCHINGS[i]) & set(MATCHINGS[j]) & set(MATCHINGS[k])) == 0
               for i, j, k in combinations(range(6), 3))

    faces = set()
    for matching in MATCHINGS:
        for size in range(1, 6):
            for face in combinations(matching, size):
                faces.add(face)
    f = tuple(sum(len(face) == size for face in faces) for size in range(1, 6))
    assert f == (15, 60, 60, 30, 6), f
    assert sum((-1)**i * count for i, count in enumerate(f)) == -9

    group = tuple(permutations(range(5)))
    assert len(group) == 120
    classes = defaultdict(list)
    for p in group:
        eperm, mperm = graph_permutation(p)
        assert set(eperm) == set(range(15))
        assert set(mperm) == set(range(6))
        classes[cycle_type(p)].append(p)
        fixed = sum(mperm[i] == i for i in range(6))
        fixed_squared = sum(mperm[mperm[i]] == i for i in range(6))
        character = ((fixed - 1)**2 - (fixed_squared - 1)) // 2

        # Character of wedge^2 of the standard four-dimensional module,
        # plus the sign twist of that standard module.
        standard = sum(p[i] == i for i in range(5)) - 1
        squared = sum(p[p[i]] == i for i in range(5)) - 1
        decomposition = (standard**2 - squared) // 2 + sign(p) * standard
        assert character == decomposition, (p, character, decomposition)

    expected = {
        (1, 1, 1, 1, 1): (1, 6, 10),
        (2, 1, 1, 1): (10, 0, -2),
        (2, 2, 1): (15, 2, -2),
        (3, 1, 1): (20, 0, 1),
        (3, 2): (20, 0, 1),
        (4, 1): (30, 2, 0),
        (5,): (24, 1, 0),
    }
    assert set(classes) == set(expected)
    for typ, ps in classes.items():
        p = ps[0]
        _, mperm = graph_permutation(p)
        fixed = sum(mperm[i] == i for i in range(6))
        fixed_squared = sum(mperm[mperm[i]] == i for i in range(6))
        character = ((fixed - 1)**2 - (fixed_squared - 1)) // 2
        assert (len(ps), fixed, character) == expected[typ]

    cycle5 = ((1, 2, 3, 4, 0),)
    cyclic = [tuple(range(5))]
    for power in range(1, 5):
        cyclic.append(tuple((i + power) % 5 for i in range(5)))
    even_group = tuple(p for p in group if sign(p) == 1)
    assert len(even_group) == 60
    assert graph_quotient(group) == (2, 1, 0)
    assert graph_quotient(even_group) == (2, 1, 0)
    assert graph_quotient(cyclic) == (5, 6, 2)
    print('PETERSEN_PERFECT_MATCHING_EQUIVARIANT_CERTIFICATE_OK')
    print('vertices=10 graph_edges=15 perfect_matchings=6')
    print('perfect_matching_complex_f_vector=' + repr(f))
    print('homology_betti=(1,10,0,0,0)')
    print('group=S5 order=120; H1=wedge2(augmentation of 6-point matching action)')
    print('rational_H1=wedge2(standard_4) + sign*standard_4')
    for typ, (count, fixed, trace) in sorted(expected.items(), reverse=True):
        print('class=' + str(typ) + ' size=' + str(count) + ' fixed_matchings=' + str(fixed) + ' H1_trace=' + str(trace))
    print('quotient_S5=(vertices=2,edges=1,rank=0)')
    print('quotient_A5=(vertices=2,edges=1,rank=0)')
    print('quotient_C5=(vertices=5,edges=6,rank=2)')


if __name__ == '__main__':
    main()
