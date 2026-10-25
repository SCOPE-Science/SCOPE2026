#!/usr/bin/env python3
"""Exact count of norm-four E8 vectors and their classes modulo 2E8."""
from itertools import combinations, product
from collections import Counter


def norm_four_vectors_twice():
    """Returns tuples (2v_i) for all norm-four vectors of the standard E8."""
    vectors = []
    for i in range(8):
        for sign in (-1, 1):
            x = [0] * 8
            x[i] = 4 * sign
            vectors.append(tuple(x))
    for positions in combinations(range(8), 4):
        for signs in product((-1, 1), repeat=4):
            x = [0] * 8
            for pos, sign in zip(positions, signs):
                x[pos] = 2 * sign
            vectors.append(tuple(x))
    for special in range(8):
        for signs in product((-1, 1), repeat=8):
            x = tuple(sign * (3 if i == special else 1)
                      for i, sign in enumerate(signs))
            if sum(x) % 4 == 0:
                vectors.append(x)
    return vectors


def congruent_mod_twice_E8(u, v):
    """u and v encode twice the Euclidean coordinates of E8 vectors.

    (u-v)/4 belongs to E8 iff all its coordinates are integers
    with even sum, or all are half-integers with even sum.
    """
    difference = [a-b for a, b in zip(u,v)]
    residues = [d % 4 for d in difference]
    is_integer = all(r == 0 for r in residues)
    is_half_integer = all(r == 2 for r in residues)
    return (is_integer or is_half_integer) and sum(difference) % 8 == 0


def quad_mod_2(mask):
    """Quadratic form q(v)=||v||^2/2 modulo 2, in an E8 root basis.

    The seven chain edges plus an extra edge from vertex 2 to 7
    form the E8 Dynkin graph; Gram entries are 2 on the diagonal,
    -1 on edges and 0 elsewhere (determinant 1).
    """
    edges = ((0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (2,7))
    bits = [(mask >> i) & 1 for i in range(8)]
    return (sum(bits) + sum(bits[i]*bits[j] for i,j in edges)) % 2


def main():
    vec = norm_four_vectors_twice()
    assert len(vec)==2160 and len(set(vec))==2160
    assert all(sum(u*u for u in v)==16 for v in vec)
    representatives, sizes = [], []
    for v in vec:
        for i, r in enumerate(representatives):
            if congruent_mod_twice_E8(v, r):
                sizes[i] += 1
                break
        else:
            representatives.append(v)
            sizes.append(1)
    assert len(representatives) == 135, len(representatives)
    assert Counter(sizes) == {16: 135}, Counter(sizes)
    assert sum(quad_mod_2(mask) == 0 for mask in range(256)) == 136
    print('VERIFY_OK: 2160 norm-4 E8 vectors; 135 nonzero isotropic cosets; 16 vectors per coset; 136 isotropic cosets including zero')


if __name__ == '__main__':
    main()
