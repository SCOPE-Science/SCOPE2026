#!/usr/bin/env python3
"""Exact finite verification for the order-8 Sidon-seed completion claim."""
from itertools import combinations

P = 73
SEED = frozenset((1, 2, 4, 8))
SINGER = tuple(sorted(pow(2, j, P) for j in range(9)))
EXPECTED_EQUIVALENT_FOURSETS = {
    (1, 2, 4, 8),
    (2, 4, 8, 16),
    (4, 8, 16, 32),
    (8, 16, 32, 64),
    (16, 32, 55, 64),
    (32, 37, 55, 64),
    (1, 37, 55, 64),
    (1, 2, 4, 37),
    (1, 2, 37, 55),
}


def affine_signature(points):
    """Complete invariant for a 4-set under x -> u*x+v over F_73."""
    points = tuple(points)
    candidates = []
    for x in points:
        for y in points:
            if x == y:
                continue
            inv = pow((y - x) % P, -1, P)
            candidates.append(tuple(sorted(((z - x) * inv) % P for z in points)))
    return min(candidates)


def main():
    assert len(SINGER) == 9 and len(set(SINGER)) == 9
    assert SEED <= set(SINGER)
    assert affine_signature(SEED) == (0, 1, 3, 7)

    # The PDS condition: the 9*8 ordered nonzero differences are all residues 1..72.
    differences = [((x - y) % P) for x in SINGER for y in SINGER if x != y]
    assert len(differences) == P - 1
    assert len(set(differences)) == P - 1
    assert set(differences) == set(range(1, P))

    # Count the entire affine orbit and the affine stabilizer of the Singer set.
    orbit = {}
    transformations_containing_seed = []
    for u in range(1, P):
        for v in range(P):
            image = frozenset((u * x + v) % P for x in SINGER)
            orbit.setdefault(image, []).append((u, v))
            if SEED <= image:
                transformations_containing_seed.append((u, v, image))
    assert len(orbit) == 584
    assert {len(fiber) for fiber in orbit.values()} == {9}
    assert len(transformations_containing_seed) == 9
    containing_images = {image for _, _, image in transformations_containing_seed}
    assert containing_images == {frozenset(SINGER)}

    # Independent orbit-intersection check: enumerate all 126 four-subsets of SINGER.
    equivalent_foursets = {
        tuple(sorted(C))
        for C in combinations(SINGER, 4)
        if affine_signature(C) == affine_signature(SEED)
    }
    assert len(list(combinations(SINGER, 4))) == 126
    assert equivalent_foursets == EXPECTED_EQUIVALENT_FOURSETS
    assert equivalent_foursets == {
        tuple(sorted((pow(2, j, P) * x) % P for x in SEED))
        for j in range(9)
    }

    # The seed has no nonidentity affine automorphism.
    seed_stabilizer = [
        (u, v)
        for u in range(1, P)
        for v in range(P)
        if frozenset((u * x + v) % P for x in SEED) == SEED
    ]
    assert seed_stabilizer == [(1, 0)]

    print("PDS_DIFFERENCES_OK: 72 distinct nonzero residues")
    print("AFFINE_ORBIT_OK: 584 distinct PDSs; stabilizer size 9")
    print("SEED_CONTAINMENT_OK: 9 transformations, 1 distinct PDS")
    print("FOURSET_SIGNATURE_OK: 9 of 126 subsets; all are 2^j*SEED")
    print("SEED_AFFINE_STABILIZER_OK: identity only")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
