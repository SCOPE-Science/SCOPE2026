#!/usr/bin/env python3
"""Exact signed-Lefschetz character verification for width-three grid tiling complexes.

Requires only the accompanying verify_three_row_perfect_matching.py and Python stdlib.
Run both files from the same directory: python verify_reflection_characters.py
"""
from verify_three_row_perfect_matching import ordered_grid_edges, perfect_matchings, generated_complex

EXPECTED = {
    2: ((19, 3, 11, 3), (0, 0, 0, 0), (0, 0, 0, 0)),
    4: ((494, 16, 42, 20), (-1, 1, -1, 1), (1, -1, 1, -1)),
    6: ((12374, 72, 286, 80), (1, -1, -1, 1), (1, -1, -1, 1)),
    8: ((309479, 313, 1097, 515), (-2, 0, 0, -2), (2, 0, 0, 2)),
}


def reflection_permutation(n, rowswap, colswap, edges):
    edge_index = {tuple(sorted(e)): i for i, e in enumerate(edges)}
    perm = []
    for edge in edges:
        mapped = []
        for u in edge:
            row, column = divmod(u, n)
            rr = 2-row if rowswap else row
            cc = n-1-column if colswap else column
            mapped.append(rr*n+cc)
        perm.append(edge_index[tuple(sorted(mapped))])
    assert sorted(perm) == list(range(len(edges)))
    assert all(perm[perm[i]] == i for i in range(len(edges)))
    return perm


def reduced_lefschetz(faces, perm):
    # A nonempty invariant oriented simplex with k vertices contributes
    # (-1)^(k-1) times the orientation sign of the induced permutation.
    # The augmentation contributes an extra -1 in reduced Lefschetz number.
    num_fixed = 0
    result = -1
    for face in faces:
        if face == 0:
            continue
        original = [i for i in range(len(perm)) if face & (1 << i)]
        images = [perm[i] for i in original]
        if set(original) != set(images):
            continue
        num_fixed += 1
        inversions = sum(x > y for j, x in enumerate(images) for y in images[j+1:])
        result += (-1 if (len(original) - 1 + inversions) % 2 else 1)
    return num_fixed, result


def verify(n):
    edges = ordered_grid_edges(n)
    facets = perfect_matchings(n, edges)
    faces = generated_complex(facets)
    signatures = []
    for h, v in ((False, False), (True, False), (False, True), (True, True)):
        perm = reflection_permutation(n, h, v, edges)
        signatures.append(reduced_lefschetz(faces, perm))
    fixed_counts = tuple(x for x, _ in signatures)
    lefschetz = tuple(x for _, x in signatures)
    d = n//2-1
    homology_character = tuple(((-1) ** d) * t for t in lefschetz)
    assert (fixed_counts, lefschetz, homology_character) == EXPECTED[n], (n, signatures)
    # Fourier inversion on the Klein four-group gives irreducible
    # multiplicities. The four one-dimensional characters are
    # (1, sign_h, sign_v, sign_h*sign_v).
    irrep_multiplicities = []
    for sh, sv in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        numerator = sum(a*b for a,b in zip(homology_character, (1, sh, sv, sh*sv)))
        assert numerator % 4 == 0
        multiplicity = numerator//4
        assert multiplicity >= 0
        irrep_multiplicities.append(multiplicity)
    assert sum(irrep_multiplicities) == homology_character[0]
    print('n=%d fixed_nonempty=%r reduced_lefschetz=%r homology_character=%r multiplicities_(++, -+, +-, --)=%r'
          % (n, fixed_counts, lefschetz, homology_character, tuple(irrep_multiplicities)))


if __name__ == '__main__':
    for n in (2, 4, 6, 8):
        verify(n)
    print('VERIFICATION_OK 16 exact signed fixed-simplex sums')
