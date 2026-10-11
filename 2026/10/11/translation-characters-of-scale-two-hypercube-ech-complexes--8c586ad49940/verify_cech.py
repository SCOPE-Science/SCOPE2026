#!/usr/bin/env python3
"""Reproduce translation Lefschetz characters on radius-one hypercube Cech nerves.

The simplicial complex has one maximal simplex, the closed graph-neighborhood
of each binary vertex. The program independently enumerates oriented faces,
computes signed fixed-simplex traces, and checks mod-two boundary ranks.
"""
from itertools import combinations
from math import comb


def build_faces(n):
    faces = set()
    for v in range(1 << n):
        star = [v] + [v ^ (1 << i) for i in range(n)]
        for size in range(1, n + 2):
            for s in combinations(star, size):
                faces.add(tuple(sorted(s)))
    return tuple(tuple(sorted(x for x in faces if len(x) == k))
                 for k in range(1, n + 2))


def permutation_sign(image):
    return -1 if sum(x > y for i, x in enumerate(image)
                     for y in image[i + 1:]) % 2 else 1


def lefschetz(faces, g):
    ans = 0
    invariant = []
    for degree, group in enumerate(faces):
        for face in group:
            trans = tuple(v ^ g for v in face)
            if set(trans) == set(face):
                order = [face.index(x) for x in trans]
                sign = permutation_sign(order)
                ans += (-1) ** degree * sign
                invariant.append((face, degree, sign))
    return ans, invariant


def gf2_rank(rows):
    pivots = {}
    for x in rows:
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return len(pivots)


def boundary_rank(faces_lo, faces_hi):
    pos = {f: i for i, f in enumerate(faces_lo)}
    rows = [0] * len(faces_lo)
    for j, face in enumerate(faces_hi):
        for i in range(len(face)):
            rows[pos[face[:i] + face[i + 1:]]] ^= 1 << j
    return gf2_rank(rows)


def beta(n):
    return (1 << (n - 2)) * (n * n - 3 * n + 4) - 1


def multiplicity(n, k):
    return comb(n, 2) if k == 0 else comb(n, 2) + 1 - k * (n + 1 - k)


def run():
    for n in range(2, 8):
        faces = build_faces(n)
        actual = {g: lefschetz(faces, g) for g in range(1 << n)}
        for g, (L, inv) in actual.items():
            if not g:
                assert L == 1 + beta(n), (n, g, L, beta(n))
            else:
                wt = g.bit_count()
                assert L == ((1 << (n - 1)) if wt in (1, 2) else 0), (n, g, L)
                if wt <= 2:
                    assert len(inv) == (1 << (n - 1))
                    assert all(d == 1 and sign == -1 for _, d, sign in inv)
                else:
                    assert not inv
        # Check every one-dimensional translation character, not just its weight orbit.
        for x in range(1 << n):
            k = x.bit_count()
            m = multiplicity(n, k)
            assert m >= 0, (n, x, k, m)
            s = sum((-1) ** ((g & x).bit_count()) * (L - 1)
                    for g, (L, _) in actual.items())
            assert s == (1 << n) * m, (n, x, k, s, m)
        assert sum(comb(n, k) * multiplicity(n, k)
                   for k in range(n + 1)) == beta(n)
        fvec = [len(group) for group in faces]
        if n <= 5:
            ranks = [boundary_rank(faces[k - 1], faces[k])
                     for k in range(1, len(faces))]
            betti = [fvec[i] - (ranks[i - 1] if i else 0)
                     - (ranks[i] if i < len(ranks) else 0)
                     for i in range(len(faces))]
            assert betti == [1, 0, beta(n)] + [0] * (n - 2), (n, betti)
            print('n=', n, 'faces=', fvec, 'boundary_ranks=', ranks,
                  'betti_F2=', betti, 'translation_lefschetz=OK',
                  'Fourier=OK')
        else:
            print('n=', n, 'faces=', fvec, 'translation_lefschetz=OK',
                  'Fourier=OK')
    for n in range(2, 14):
        assert sum(comb(n, k) * multiplicity(n, k)
                   for k in range(n + 1)) == beta(n)
    print('ALL_CECH_CHECKS_PASSED')


if __name__ == '__main__':
    run()
