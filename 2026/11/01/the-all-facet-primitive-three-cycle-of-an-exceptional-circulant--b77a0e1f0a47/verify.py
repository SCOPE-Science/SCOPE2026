#!/usr/bin/env python3
"""Reconstruct the primitive top cycle of a small circulant independence complex.

Only Python's standard library is required. All counts are recomputed from
independent sets, and the finite-rank checks use bit-vector Gaussian elimination.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import gcd

N = 16
STEPS = {1, 4, 8}
SEEDS = (
    (0, 2, 5, 7),
    (0, 2, 5, 11),
    (0, 2, 7, 9),
    (0, 2, 7, 13),
    (0, 3, 6, 9),
)
WEIGHTS = (1, -1, 2, -1, 1)


def edge(a, b):
    return min((a - b) % N, (b - a) % N) in STEPS


def simplices(k):
    return [t for t in combinations(range(N), k)
            if all(not edge(a, b) for a, b in combinations(t, 2))]


def oriented_action(face, shift=0, reflect=False):
    raw = [((-v if reflect else v) + shift) % N for v in face]
    inversions = sum(raw[i] > raw[j] for i in range(len(raw))
                     for j in range(i + 1, len(raw)))
    return tuple(sorted(raw)), (-1) ** inversions


def rotation_orbit_chain(seed):
    result = Counter()
    for t in range(N):
        face, sign = oriented_action(seed, shift=t)
        result[face] += sign
    return {f: v for f, v in result.items() if v}


def boundary(chain):
    result = Counter()
    for face, coeff in chain.items():
        for i in range(len(face)):
            result[face[:i] + face[i + 1:]] += coeff * (-1) ** i
    return {f: v for f, v in result.items() if v}


def rank_binary(columns):
    basis = {}
    for col in columns:
        while col:
            pivot = col.bit_length() - 1
            if pivot in basis:
                col ^= basis[pivot]
            else:
                basis[pivot] = col
                break
    return len(basis)


def rank_of_boundary(lower, higher):
    lookup = {face: j for j, face in enumerate(lower)}
    columns = []
    for f in higher:
        v = 0
        for i in range(len(f)):
            v ^= 1 << lookup[f[:i] + f[i + 1:]]
        columns.append(v)
    return rank_binary(columns)


def main():
    faces = [simplices(k) for k in range(1, 5)]
    assert [len(x) for x in faces] == [16, 80, 144, 80]
    assert not simplices(5)
    assert len(set(SEEDS)) == 5
    orbit_chains = [rotation_orbit_chain(seed) for seed in SEEDS]
    assert all(len(x) == 16 for x in orbit_chains)
    assert len(set().union(*(set(x) for x in orbit_chains))) == 80
    assert all(set(x).issubset(set(faces[3])) for x in orbit_chains)
    z = Counter()
    for w, orbit in zip(WEIGHTS, orbit_chains):
        for f, a in orbit.items():
            z[f] += w * a
    assert len(z) == 80 and all(z[f] for f in faces[3])
    assert Counter(abs(z[f]) for f in faces[3]) == {1: 64, 2: 16}
    assert gcd(*z.values()) == 1
    assert not boundary(z)
    ranks = [rank_of_boundary(faces[i - 1], faces[i]) for i in range(1, 4)]
    assert ranks == [15, 65, 79]
    # The nonzero integral top cycle forces rational rank of d3 <= 79.
    # The mod-two rank 79 forces rational rank of d3 >= 79.
    assert len(faces[3]) - ranks[2] == 1
    # The full dihedral action fixes the oriented integral generator.
    for reflect in (False, True):
        for shift in range(N):
            image = Counter()
            for face, coeff in z.items():
                new_face, sign = oriented_action(face, shift, reflect)
                image[new_face] += sign * coeff
            assert image == z, (reflect, shift)
    incidences = defaultdict(list)
    for f in faces[3]:
        for i in range(4):
            incidences[f[:i] + f[i + 1:]].append(abs(z[f]))
    pattern = Counter(tuple(sorted(v)) for v in incidences.values())
    assert pattern == {(1, 1): 96, (1, 1, 2): 32, (2, 2): 16}
    # Check the compact nine-orbit boundary certificate.
    remaining = set(faces[2]); tri_reps = []
    while remaining:
        rep = min(remaining)
        orbit = {oriented_action(rep, t)[0] for t in range(N)}
        assert len(orbit) == N
        tri_reps.append(rep)
        remaining.difference_update(orbit)
    assert len(tri_reps) == 9
    assert tri_reps == [(0, 2, 5), (0, 2, 7), (0, 2, 9),
                        (0, 2, 11), (0, 2, 13), (0, 3, 6),
                        (0, 3, 9), (0, 3, 10), (0, 5, 10)]
    table = [[boundary(orb).get(rep, 0) for orb in orbit_chains]
             for rep in tri_reps]
    assert table == [
        [-1, -1, 0, 0, 0],
        [1, 0, -1, -1, 0],
        [0, 0, 0, 0, 0],
        [-1, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, -1, -1],
        [0, -1, 0, 1, 0],
    ]
    assert all(sum(a * b for a, b in zip(row, WEIGHTS)) == 0
               for row in table)
    print("f-vector (excluding empty face):", tuple(map(len, faces)))
    print("mod-two boundary ranks:", tuple(ranks))
    print("rotation tetrahedron orbits:", tuple(SEEDS))
    print("primitive orbit coefficients:", tuple(WEIGHTS))
    print("primitive top-cycle coefficient magnitudes:", dict(sorted(Counter(abs(v) for v in z.values()).items())))
    print("triangle incidence patterns:", dict(sorted(pattern.items())))
    print("dihedral elements fixing integral top cycle: 32/32")
    print("top integral homology: Z; no proper tetrahedral support carries nonzero H3")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
