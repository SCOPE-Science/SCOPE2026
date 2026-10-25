#!/usr/bin/env python3
"""Finite checks for a ladder perfect-matching homology character.

All computations use integer bit masks and the Python standard library.
Each graph edge is a simplicial vertex. The proof for all widths is
structural and independent of this finite checker.
"""
from collections import defaultdict


def perfect_matchings(n):
    """Enumerate all domino tilings of a two-row, n-column rectangle."""
    def visit(j):
        if j == n:
            yield 0
            return
        for tail in visit(j + 1):
            yield (1 << j) | tail
        if j + 1 < n:
            for tail in visit(j + 2):
                yield (1 << (n + j)) | (1 << (2 * n - 1 + j)) | tail
    return list(visit(0))


def faces_from_facets(facets):
    faces = {0}
    for facet in facets:
        subface = facet
        while subface:
            faces.add(subface)
            subface = (subface - 1) & facet
    return faces


def block_facets(n):
    assert n % 2 == 0
    facets = [0]
    for j in range(n // 2):
        i = 2 * j
        pair_rungs = (1 << i) | (1 << (i + 1))
        pair_rails = (1 << (n + i)) | (1 << (2 * n - 1 + i))
        facets = [old | choice for old in facets
                  for choice in (pair_rungs, pair_rails)]
    return facets


def automorphism(n, reverse_columns=False, swap_rows=False):
    order = 3 * n - 2
    perm = [None] * order
    for i in range(n):
        perm[i] = n - 1 - i if reverse_columns else i
    for t in range(2):
        for i in range(n - 1):
            old = n + t * (n - 1) + i
            new_t = 1 - t if swap_rows else t
            new_i = n - 2 - i if reverse_columns else i
            perm[old] = n + new_t * (n - 1) + new_i
    assert sorted(perm) == list(range(order))
    return perm


def reduced_lefschetz(faces, perm):
    """Alternating trace on oriented augmented simplicial chains."""
    value = -1  # The degree -1 augmented empty-face contribution.
    for face in faces:
        if face == 0:
            continue
        vertices = [i for i in range(len(perm)) if face & (1 << i)]
        images = [perm[i] for i in vertices]
        if set(images) != set(vertices):
            continue
        inversions = sum(a > b for j, a in enumerate(images)
                         for b in images[j + 1:])
        value += (-1) ** (len(vertices) - 1 + inversions)
    return value


def mod2_reduced_betti(faces):
    groups = defaultdict(list)
    for face in faces:
        if face:
            groups[face.bit_count() - 1].append(face)
    ranks = {}
    for dim in range(1, max(groups) + 1):
        row = {face: i for i, face in enumerate(groups[dim - 1])}
        pivots = {}
        for face in groups[dim]:
            column = 0
            x = face
            while x:
                bit = x & -x
                column ^= 1 << row[face - bit]
                x -= bit
            while column:
                p = column.bit_length() - 1
                if p in pivots:
                    column ^= pivots[p]
                else:
                    pivots[p] = column
                    break
        ranks[dim] = len(pivots)
    return {d:len(group)-ranks.get(d,0)-ranks.get(d+1,0)-(d==0)
            for d,group in groups.items() if len(group)-ranks.get(d,0)-ranks.get(d+1,0)-(d==0)}


def main():
    known_face_counts = {2: 6, 4: 60, 6: 546, 8: 4920, 10: 44286}
    for n in known_face_counts:
        faces = faces_from_facets(perfect_matchings(n))
        y_facets = block_facets(n)
        assert all(y in perfect_matchings(n) for y in y_facets)
        assert faces_from_facets(y_facets) <= faces
        assert len(faces) - 1 == known_face_counts[n]
        k, degree = n // 2, n // 2 - 1
        char_reverse = (-1) ** (k * (k - 1) // 2)
        for swap,reverse,expected in [(0,0,1),(1,0,1),
                                      (0,1,char_reverse),(1,1,char_reverse)]:
            perm = automorphism(n,reverse_columns=bool(reverse),swap_rows=bool(swap))
            L = reduced_lefschetz(faces,perm)
            assert L == (-1) ** degree * expected, (n,swap,reverse,L,expected)
        if n <= 8:
            assert mod2_reduced_betti(faces) == {degree:1}, n
        print(f'n={n}: faces={len(faces)-1}, block_facets={len(y_facets)}, '
              f'row_swap=+1, column_reversal={char_reverse:+d}, '
              f'characters_verified=yes')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
