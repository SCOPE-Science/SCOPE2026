#!/usr/bin/env python3
"""Exact rational rank certificate for harmonic evaluation at truncated-octahedral vertices.
Uses only Python's standard library. Mathematical large-degree tail uses Bernstein's
Legendre inequality separately, not numerical enumeration.
"""
from fractions import Fraction as Q
from itertools import permutations, product

def vertices():
    return sorted({tuple(p) for a, b in product((-1, 1), (-2, 2)) for p in permutations((0, a, b))})

def antipodal_reps(points):
    reps, used = [], set()
    for p in points:
        if p not in used:
            reps.append(p)
            used.add(p)
            used.add(tuple(-x for x in p))
    assert len(reps) == 12
    return reps

def rank(A):
    A = [list(row) for row in A]
    n, m = len(A), len(A[0]); row = 0
    for col in range(m):
        pivot = next((r for r in range(row, n) if A[r][col]), None)
        if pivot is None:
            continue
        A[row], A[pivot] = A[pivot], A[row]
        p = A[row][col]
        for r in range(row + 1, n):
            if A[r][col]:
                q = A[r][col] / p
                for j in range(col, m):
                    A[r][j] -= q * A[row][j]
        row += 1
        if row == n:
            break
    return row

def dot(v, w):
    return sum(a * b for a, b in zip(v, w))

def legendre_table(stop):
    P0 = [Q(1) for j in range(-5, 6)]
    P1 = [Q(j, 5) for j in range(-5, 6)]
    yield 0, P0
    yield 1, P1
    for ell in range(1, stop):
        P2 = [((2*ell+1)*Q(j,5)*P1[j+5]-ell*P0[j+5]) / (ell+1) for j in range(-5,6)]
        yield ell+1, P2
        P0, P1 = P1, P2

def main():
    P = vertices()
    assert len(P) == 24 and all(sum(x*x for x in p)==5 for p in P)
    reps = antipodal_reps(P)
    dots = [[dot(v,w) for w in reps] for v in reps]
    assert set(t for r in dots for t in r) == set(range(-4,6)) - {-5}
    # Pairwise non-antipodal dot products are at most 4/5 in magnitude.
    assert all(abs(dots[i][j])<=4 for i in range(12) for j in range(12) if i!=j)
    exceptional = [1,3,5,6,9,9,10,12,11]
    for ell, table in legendre_table(128):
        G = [[table[dots[i][j]+5] for j in range(12)] for i in range(12)]
        r = rank(G)
        expected = exceptional[ell] if ell < 9 else 12
        assert r == expected, (ell,r,expected)
        if ell == 8:
            # degree-six cubic alternating harmonic H=(x²-y²)(y²-z²)(z²-x²)
            H = [((v[0]**2-v[1]**2)*(v[1]**2-v[2]**2)*(v[2]**2-v[0]**2)) for v in reps]
            assert all(abs(h)==12 for h in H)
            assert all(sum(G[i][j]*H[j] for j in range(12)) == 0 for i in range(12))
    # For ell>=129, Bernstein |P_ell(t)|<=sqrt(2/(pi*ell*sqrt(1-t²)))
    # and sqrt(1-t²)>=3/5 for off-diagonal t=i/5,
    # giving Gershgorin sum <= 11*sqrt(10/(3*pi*ell))<1.
    # Archimedes bound pi > 223/71 makes the comparison rational.
    assert 1210*71 < 3*223*129
    print('PASS: 24 antipodal vertices, 129 exact rational Gram ranks (ell 0..128),')
    print('      explicit degree-eight kernel, Bernstein/Gershgorin threshold ell>=129.')
    print('RANKS 0..8:', exceptional, 'and all ell>=9 have rank 12')

if __name__ == '__main__':
    main()
