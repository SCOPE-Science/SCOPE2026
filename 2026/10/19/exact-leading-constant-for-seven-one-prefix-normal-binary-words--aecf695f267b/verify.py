#!/usr/bin/env python3
"""Exact rational-volume certificate for seven-one prefix-normal binary words.

Standard-library only.  All cone, face, determinant and volume decisions
are exact rational/integer arithmetic.  The final factor enumeration is
independent of the gap characterization.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import factorial, gcd, comb
from functools import reduce

DIM = 6


def det(A):
    n = len(A)
    if n == 0:
        return Q(1)
    B = [[Q(x) for x in row] for row in A]
    sign, previous = 1, Q(1)
    for k in range(n - 1):
        if B[k][k] == 0:
            i = next((i for i in range(k + 1, n) if B[i][k]), None)
            if i is None:
                return Q(0)
            B[k], B[i] = B[i], B[k]
            sign = -sign
        pivot = B[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                B[i][j] = (B[i][j] * pivot - B[i][k] * B[k][j]) / previous
            B[i][k] = 0
        previous = pivot
    return sign * B[n - 1][n - 1]


def rank(A):
    if not A:
        return 0
    M = [[Q(x) for x in row] for row in A]
    p = 0
    for j in range(len(M[0])):
        if p == len(M):
            break
        i = next((i for i in range(p, len(M)) if M[i][j]), None)
        if i is None:
            continue
        M[p], M[i] = M[i], M[p]
        v = M[p][j]
        for k in range(j, len(M[0])):
            M[p][k] /= v
        for i in range(p + 1, len(M)):
            v = M[i][j]
            if v:
                for k in range(j, len(M[0])):
                    M[i][k] -= v * M[p][k]
        p += 1
    return p


def inverse(A):
    n = len(A)
    M = [[Q(x) for x in row] + [Q(i == j) for j in range(n)]
         for i, row in enumerate(A)]
    for j in range(n):
        pivot_row = next(k for k in range(j, n) if M[k][j])
        M[j], M[pivot_row] = M[pivot_row], M[j]
        v = M[j][j]
        M[j] = [x / v for x in M[j]]
        for k in range(n):
            if k != j and M[k][j]:
                v = M[k][j]
                M[k] = [M[k][i] - v * M[j][i] for i in range(2 * n)]
    return [r[n:] for r in M]


def inequalities():
    rows = []
    for i in range(DIM):
        row = [0] * DIM
        row[i] = 1
        rows.append(tuple(row))
    for k in range(1, DIM):
        for j in range(1, DIM - k + 1):
            row = [0] * DIM
            for h in range(k):
                row[j+h] += 1
                row[h] -= 1
            rows.append(tuple(row))
    assert len(rows) == 21
    return rows


def extreme_rays(rows):
    rays = set()
    for ix in combinations(range(len(rows)), DIM-1):
        A = [rows[i] for i in ix]
        v = [(-1)**j * int(det([row[:j] + row[j+1:] for row in A]))
             for j in range(DIM)]
        if not any(v):
            continue
        assert all(sum(a * b for a, b in zip(row, v)) == 0 for row in A)
        evaluations = [sum(a * b for a, b in zip(row, v)) for row in rows]
        if all(e >= 0 for e in evaluations):
            pass
        elif all(e <= 0 for e in evaluations):
            v = [-x for x in v]
        else:
            continue
        g = reduce(gcd, v)
        rays.add(tuple(x // g for x in v))
    return sorted(rays)

RAYS_EXPECTED = [
    (0,0,0,0,0,1), (0,0,0,0,1,0), (0,0,0,1,0,0),
    (0,0,1,0,0,1), (0,0,1,0,1,0), (0,0,1,1,0,0),
    (0,1,0,1,0,1), (0,1,0,1,1,0), (0,1,1,0,1,1),
    (0,1,1,0,2,0), (0,1,1,1,0,1), (0,2,1,1,1,1),
    (0,2,1,1,2,0), (1,1,1,1,1,1)
]


def exact_volume(rays):
    # The cross-section sum(s_i)=1 is a 5-polytope with these vertices.
    pts = [tuple(Q(x, sum(v)) for x in v) for v in rays]
    face_cache = {}

    def facets(face):
        face = tuple(sorted(face))
        if face in face_cache:
            return face_cache[face]
        ps = [pts[i] for i in face]
        p0 = ps[0]
        differences = [[a-b for a, b in zip(p, p0)] for p in ps[1:]]
        dimension = rank(differences)
        if dimension == 0:
            face_cache[face] = ()
            return ()
        basis = []
        for v in differences:
            if rank(basis + [v]) > len(basis):
                basis.append(v)
            if len(basis) == dimension:
                break
        # Rational coordinate chart for this affine face.
        cols = next(c for c in combinations(range(DIM), dimension)
                    if det([[b[i] for i in c] for b in basis]))
        inv = inverse([[b[i] for i in cols] for b in basis])
        coords = []
        for p in ps:
            d = [p[i] - p0[i] for i in cols]
            coords.append(tuple(sum(d[i] * inv[i][j]
                                    for i in range(dimension))
                                for j in range(dimension)))
        all_facets = set()
        for ids in combinations(range(len(face)), dimension):
            q = [coords[i] for i in ids]
            D = [[q[i][j] - q[0][j] for j in range(dimension)]
                 for i in range(1, dimension)]
            normal = [(-1)**j * det([row[:j] + row[j+1:] for row in D])
                      for j in range(dimension)]
            if not any(normal):
                continue
            sides = [sum(normal[j] * (p[j]-q[0][j])
                         for j in range(dimension)) for p in coords]
            if (any(x > 0 for x in sides) and any(x < 0 for x in sides)) \
               or not any(sides):
                continue
            subface = tuple(face[i] for i, x in enumerate(sides) if not x)
            assert len(subface) >= dimension
            all_facets.add(subface)
        result = tuple(sorted(all_facets))
        face_cache[face] = result
        return result

    total = Q(0)
    simplex_count = 0

    def visit(face, centers):
        nonlocal total, simplex_count
        barycenter = tuple(sum(pts[i][j] for i in face) / len(face)
                           for j in range(DIM))
        centers = centers + (barycenter,)
        children = facets(face)
        if not children:
            assert len(face) == 1 and len(centers) == DIM
            total += abs(det(centers)) / factorial(DIM)
            simplex_count += 1
        else:
            for child in children:
                visit(child, centers)

    visit(tuple(range(len(rays))), ())
    assert len(face_cache) == 155
    assert simplex_count == 2184
    return total, len(face_cache), simplex_count


def prefix_normal(s):
    pref = [0]
    for c in s:
        pref.append(pref[-1] + c)
    for k in range(1, len(s) + 1):
        for i in range(1, len(s) - k + 1):
            if pref[i+k]-pref[i] > pref[k]:
                return False
    return True


def brute_counts(n):
    if n < 7:
        return 0
    count = 0
    for indices in combinations(range(n), 7):
        seq = [0] * n
        for i in indices:
            seq[i] = 1
        count += prefix_normal(seq)
    return count


def gap_counts(n, rows):
    if n < 7:
        return 0
    budget = n-7
    count = 0
    def rec(part):
        nonlocal count
        if len(part) == DIM:
            count += all(sum(a*b for a,b in zip(row,part)) >= 0 for row in rows)
            return
        for x in range(budget - sum(part) + 1):
            rec(part + [x])
    rec([])
    return count


def main():
    rows=inequalities()
    rays=extreme_rays(rows)
    assert rays == RAYS_EXPECTED, ('rays', rays)
    vol, nf, ns=exact_volume(rays)
    assert vol==Q(289,2488320), ('volume',vol)
    # Two independent finite descriptions of prefix normality.
    checked={}
    for n in range(7,18):
        direct=brute_counts(n)
        gaps=gap_counts(n,rows)
        assert direct==gaps,(n,direct,gaps)
        checked[n]=direct
    print('VERIFIED_EXACT_VOLUME',vol)
    print('RAYS',len(rays),'FACES',nf,'SIMPLEX_FLAGS',ns)
    print('EXACT_FINITE_COUNTS',checked)
    print('ASYMPTOTIC a_7(n) = 289/2488320 n^6 + O(n^5)')

if __name__=='__main__':main()
