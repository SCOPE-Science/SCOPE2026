#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

EXPECTED_ORIGIN = {3: 17, 4: 150, 5: 1872}
EXPECTED_ALL = {3: 34, 4: 480, 5: 9984}


def inverse(A):
    n = len(A)
    M = [[Fraction(A[i][j]) for j in range(n)] +
         [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return None
        if p != c:
            M[c], M[p] = M[p], M[c]
        pivot = M[c][c]
        M[c] = [x / pivot for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [M[r][j] - f * M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]


def determinant(A):
    n = len(A)
    M = [[Fraction(x) for x in row] for row in A]
    det = Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return Fraction(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            det = -det
        pivot = M[c][c]
        det *= pivot
        for r in range(c+1, n):
            if M[r][c] != 0:
                f = M[r][c] / pivot
                for j in range(c+1, n):
                    M[r][j] -= f * M[c][j]
                M[r][c] = 0
    return det


def gram(points):
    base = points[0]
    vecs = [[p[k] - base[k] for k in range(len(base))] for p in points[1:]]
    return [[sum(vecs[i][k] * vecs[j][k] for k in range(len(base)))
             for j in range(len(vecs))] for i in range(len(vecs))]


def nonobtuse(points):
    H = inverse(gram(points))
    if H is None:
        return False
    n = len(H)
    if any(H[i][j] > 0 for i in range(n) for j in range(n) if i != j):
        return False
    if any(sum(H[i], Fraction(0)) < 0 for i in range(n)):
        return False
    return True


def cube_vertices(d):
    return [tuple((m >> k) & 1 for k in range(d)) for m in range(1 << d)]


def census(d):
    cube = cube_vertices(d)
    tet_ok = {}
    for face in combinations(range(1 << d), 4):
        tet_ok[face] = nonobtuse([cube[i] for i in face])

    local_origin = 0
    global_failures = 0
    for choice in combinations(range(1, 1 << d), d):
        ids = (0,) + choice
        if not all(tet_ok[tuple(sorted(face))] for face in combinations(ids, 4)):
            continue
        pts = [cube[i] for i in ids]
        H = inverse(gram(pts))
        if H is None:
            continue
        local_origin += 1
        if not nonobtuse(pts):
            global_failures += 1

    assert local_origin == EXPECTED_ORIGIN[d], (d, local_origin)
    assert global_failures == 0, (d, global_failures)
    all_count_num = local_origin * (1 << d)
    assert all_count_num % (d + 1) == 0
    all_count = all_count_num // (d + 1)
    assert all_count == EXPECTED_ALL[d], (d, all_count)
    return sum(tet_ok.values()), len(tet_ok), local_origin, all_count


def witness_check():
    V = [
        (0,0,0,0,0,0),
        (1,1,0,0,0,1),
        (1,0,1,0,1,1),
        (0,0,1,1,0,1),
        (0,1,1,0,1,0),
        (0,1,0,1,1,1),
        (1,1,1,1,0,0),
    ]
    G_expected = [
        [3,2,1,1,2,2],
        [2,4,2,2,2,2],
        [1,2,3,1,2,2],
        [1,2,1,3,2,2],
        [2,2,2,2,4,2],
        [2,2,2,2,2,4],
    ]
    H_expected = [
        [Fraction(1),Fraction(-1,2),Fraction(1,2),Fraction(1,2),Fraction(-1,2),Fraction(-1,2)],
        [Fraction(-1,2),Fraction(3,4),Fraction(-1,2),Fraction(-1,2),Fraction(1,4),Fraction(1,4)],
        [Fraction(1,2),Fraction(-1,2),Fraction(1),Fraction(1,2),Fraction(-1,2),Fraction(-1,2)],
        [Fraction(1,2),Fraction(-1,2),Fraction(1,2),Fraction(1),Fraction(-1,2),Fraction(-1,2)],
        [Fraction(-1,2),Fraction(1,4),Fraction(-1,2),Fraction(-1,2),Fraction(3,4),Fraction(1,4)],
        [Fraction(-1,2),Fraction(1,4),Fraction(-1,2),Fraction(-1,2),Fraction(1,4),Fraction(3,4)],
    ]
    G = gram(V)
    H = inverse(G)
    assert G == G_expected
    assert H == H_expected
    assert determinant(G) == 64
    assert not nonobtuse(V)
    tetra = sum(nonobtuse([V[i] for i in face]) for face in combinations(range(7), 4))
    assert tetra == 35
    pos = [(i+1,j+1) for i in range(6) for j in range(i+1,6) if H[i][j] > 0]
    neg_rows = [i+1 for i in range(6) if sum(H[i], Fraction(0)) < 0]
    assert pos == [(1,3),(1,4),(2,5),(2,6),(3,4),(5,6)]
    assert neg_rows == [2,5,6]
    return tetra, pos, neg_rows


def main():
    for d in (3,4,5):
        nt, total, local0, allc = census(d)
        print(f'd={d} nonobtuse_tetra_subsets={nt}/{total} local_origin={local0} all_binary={allc} global_failures=0')
    tetra, pos, neg = witness_check()
    print(f'd=6 witness_nonobtuse_tetrahedra={tetra}/35 gram_det=64 positive_offdiag={pos} negative_row_sums={neg}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
