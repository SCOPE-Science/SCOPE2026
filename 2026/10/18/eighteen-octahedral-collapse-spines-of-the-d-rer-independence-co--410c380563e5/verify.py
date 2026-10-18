#!/usr/bin/env python3
"""Exact verifier for octahedral spines in the Dürer graph independence complex.

Usage: python3 verify.py octahedral_spines.json
Only Python's standard library is needed.
"""
import itertools
import json
import sys
from collections import Counter


def edge_set():
    e = set()
    for i in range(6):
        e.add(tuple(sorted((i, (i + 1) % 6))))
        e.add((i, i + 6))
        e.add(tuple(sorted((6 + i, 6 + (i + 2) % 6))))
    return e


def perm_sign(seq):
    return (-1) ** sum(seq[i] > seq[j]
                       for i in range(len(seq)) for j in range(i + 1, len(seq)))


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        certificate = json.load(f)
    assert certificate['schema_version'] == 1
    assert certificate['graph'] == 'GP(6,2)'
    edges = edge_set()
    assert len(edges) == 18
    # Independent sets are recovered without trusting the certificate.
    faces = {}
    for mask in range(1, 1 << 12):
        if all(not (mask >> a & 1 and mask >> b & 1) for a, b in edges):
            faces[mask] = mask.bit_count() - 1
    assert Counter(faces.values()) == {0: 12, 1: 48, 2: 74, 3: 36}
    facets = [m for m in faces if not any(
        m != other and m & other == m for other in faces)]
    assert len(facets) == 36 and all(m.bit_count() == 4 for m in facets)
    # Classify every induced triple of disjoint graph edges on six vertices.
    core_sets = []
    for vs in itertools.combinations(range(12), 6):
        six = set(vs)
        induced = [(a, b) for a, b in edges if a in six and b in six]
        if len(induced) == 3 and len(set().union(*(set(e) for e in induced))) == 6:
            core_sets.append(vs)
    assert len(core_sets) == 18
    assert len(certificate['cores']) == 18
    assert sorted(tuple(row['vertices']) for row in certificate['cores']) == core_sets
    for entry in certificate['cores']:
        vertices = tuple(entry['vertices'])
        vmask = sum(1 << v for v in vertices)
        target = {m for m in faces if not m & ~vmask}
        # Boundary of octahedron: 6 vertices, 12 edges and 8 triangles.
        assert Counter(faces[m] for m in target) == {0: 6, 1: 12, 2: 8}
        current = set(faces)
        assert len(entry['pairs']) == 72
        for pair in entry['pairs']:
            assert len(pair) == 2
            lower, upper = pair
            assert isinstance(lower, int) and isinstance(upper, int)
            assert 0 < lower < (1 << 12) and 0 < upper < (1 << 12)
            assert lower in current and upper in current
            assert lower not in target and upper not in target
            assert upper.bit_count() == lower.bit_count() + 1
            assert (upper & lower) == lower
            # The lower face must have exactly one proper remaining coface.
            strict_cofaces = [m for m in current if m != lower and m & lower == lower]
            assert strict_cofaces == [upper], (vertices, lower, upper, strict_cofaces)
            current.remove(lower)
            current.remove(upper)
        assert current == target
    # The labelled D6 action preserves every graph edge and all 170 faces.
    permutations = []
    for a in range(6):
        for reflection in (0, 1):
            p = tuple((a + (-i if reflection else i)) % 6 for i in range(6))
            p += tuple(6 + (a + (-i if reflection else i)) % 6 for i in range(6))
            assert {tuple(sorted((p[u], p[v]))) for u, v in edges} == edges
            permutations.append((a, reflection, p))
    assert len({p for _, _, p in permutations}) == 12
    # Two D6 orbits of six-vertex octahedral cores.
    unseen = set(core_sets)
    orbit_sizes = []
    while unseen:
        one = next(iter(unseen))
        orbit = {tuple(sorted(p[j] for j in one)) for _, _, p in permutations}
        assert orbit <= set(core_sets)
        orbit_sizes.append(len(orbit))
        unseen -= orbit
    assert sorted(orbit_sizes) == [6, 12]
    # Full graph automorphism group is D6: the six u-vertices lie in no
    # graph triangle; the six v-vertices lie in the two graph triangles.
    # Every graph automorphism restricts to an automorphism of the u-cycle
    # (at most twelve), and the unique spokes determine its action on v.
    triangle_participants = set().union(*(
        set(triple) for triple in itertools.combinations(range(12), 3)
        if all(tuple(sorted(e)) in edges for e in itertools.combinations(triple, 2))))
    assert triangle_participants == set(range(6, 12))
    # Signed augmented Lefschetz numbers equal H2 traces because
    # all 18 certified collapses imply reduced integral homology Z in degree 2.
    signatures = []
    for a, ref, p in permutations:
        lf = -1  # empty simplex is degree -1 in the reduced chain complex
        for face, dim in faces.items():
            verts = tuple(i for i in range(12) if face >> i & 1)
            images = tuple(p[i] for i in verts)
            if set(images) == set(verts):
                index_order = tuple(verts.index(x) for x in images)
                lf += (-1) ** dim * perm_sign(index_order)
        assert lf == (-1) ** (a + ref), (a, ref, lf)
        signatures.append((a, ref, lf))
    assert len(signatures) == 12
    print('VERIFY_OK: F_VECTOR_12_48_74_36, CORES_18, COLLAPSES_1296, ORBITS_6_12, DIHEDRAL_CHARACTER')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python3 verify.py octahedral_spines.json')
    main(sys.argv[1])
