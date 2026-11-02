"""Independent finite checks for the affine-plane incidence leader theorem.

Run: python3 verify.py
Only Python's standard library is required. Computations are finite tests,
not substitutes for the all-order proof.
"""
from itertools import combinations
from random import Random
from fractions import Fraction


def rank_mod(rows, modulus):
    a = [[int(v) % modulus for v in row] for row in rows]
    if not a:
        return 0
    n, m = len(a), len(a[0])
    piv = 0
    for j in range(m):
        k = next((k for k in range(piv, n) if a[k][j]), None)
        if k is None:
            continue
        a[piv], a[k] = a[k], a[piv]
        inv = pow(a[piv][j], -1, modulus)
        for t in range(j, m):
            a[piv][t] = a[piv][t] * inv % modulus
        for k in range(piv + 1, n):
            v = a[k][j]
            if v:
                for t in range(j, m):
                    a[k][t] = (a[k][t] - v * a[piv][t]) % modulus
        piv += 1
        if piv == n:
            break
    return piv


def rank_rational(rows):
    a = [[Fraction(v) for v in row] for row in rows]
    n = len(a)
    if not n:
        return 0
    m = len(a[0])
    r = 0
    for col in range(m):
        pivot = next((i for i in range(r, n) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        div = a[r][col]
        for j in range(col, m):
            a[r][j] /= div
        for i in range(r+1, n):
            factor = a[i][col]
            if factor:
                for j in range(col, m):
                    a[i][j] -= factor*a[r][j]
        r += 1
        if r == n:
            break
    return r


def affine(q):
    points = [(x, y) for x in range(q) for y in range(q)]
    lines = [((m, b), {(x, (m*x+b) % q) for x in range(q)}, m)
             for m in range(q) for b in range(q)]
    lines += [(('vertical', b), {(b, y) for y in range(q)}, q)
              for b in range(q)]
    N = [[int(p in members) for name, members, direction in lines]
         for p in points]
    return points, lines, N


def good_by_geometry(points, lines, N, controlled):
    P, L = len(points), len(lines)
    point_controls = {i for i in controlled if i < P}
    line_controls = sorted(i-P for i in controlled if i >= P)
    if len({lines[j][2] for j in line_controls}) < len(lines[0][1]):
        return False
    unselected_points = [i for i in range(P) if i not in point_controls]
    rows = [[1 for _ in unselected_points]]
    rows += [[N[i][j] for i in unselected_points] for j in line_controls]
    return rank_mod(rows, 1009) == len(unselected_points)


def direct_pbh_integer_eigenvalues(points, lines, N, controlled, lambdas):
    P, L = len(points), len(lines)
    n = P+L
    degrees = [len(lines[0][1])+1] * P + [len(lines[0][1])] * L
    lap = [[0]*n for _ in range(n)]
    for i in range(n):
        lap[i][i] = degrees[i]
    for i in range(P):
        for j in range(L):
            if N[i][j]:
                lap[i][P+j] = lap[P+j][i] = -1
    for eig in lambdas:
        rows = [[int(i == j)*eig - lap[i][j] for j in range(n)]
                for i in range(n)]
        for v in controlled:
            for i in range(n):
                rows[i].append(int(i == v))
        if rank_rational(rows) != n:
            return False
    return True


def direct_kalman_rank(points, lines, N, controlled, modulus=1009):
    """Direct full controllability-matrix rank over a prime field."""
    P, L = len(points), len(lines)
    n = P + L
    q = len(lines[0][1])
    nbrs = [[] for _ in range(n)]
    for i in range(P):
        for j in range(L):
            if N[i][j]:
                nbrs[i].append(P+j)
                nbrs[P+j].append(i)
    inp = sorted(controlled)
    columns = [[int(i == j) for i in range(n)] for j in inp]
    rows = [[] for _ in range(n)]
    for _ in range(n):
        for v in columns:
            for i in range(n):
                rows[i].append(v[i])
        columns = [[(len(nbrs[i])*v[i] - sum(v[j] for j in nbrs[i])) % modulus
                    for i in range(n)] for v in columns]
    return rank_mod(rows, modulus)


def test():
    checks = 0
    for q in (2, 3, 5, 7):
        points, lines, N = affine(q)
        P, L = len(points), len(lines)
        assert P == q*q and L == q*(q+1)
        for i in range(P):
            for j in range(P):
                assert sum(N[i][k]*N[j][k] for k in range(L)) == (q+1 if i == j else 1)
                checks += 1
        # A geometric optimal construction: q concurrent lines of distinct
        # directions, one other point on each, and remaining points actuated.
        origin = points.index((0, 0))
        chosen_lines = [j for j, (_, pts, direction) in enumerate(lines)
                        if direction != q and (0, 0) in pts]
        assert len(chosen_lines) == q
        omitted = {origin} | {points.index((1, m)) for m in range(q)}
        controlled = set(range(P)) - omitted
        controlled |= {P+j for j in chosen_lines}
        assert len(controlled) == P-1
        assert good_by_geometry(points, lines, N, controlled)
        checks += 3
        if q in (2, 3):
            # For fixed q concurrent line inputs, exhaustively count every
            # possible set of q+1 unactuated points.
            number = 0
            C = {P+j for j in chosen_lines}
            for omitted_tuple in combinations(range(P), q+1):
                placement = (set(range(P)) - set(omitted_tuple)) | C
                number += good_by_geometry(points, lines, N, placement)
                checks += 1
            assert number == 2*q*(q-1)**q
            print('q=', q, 'fixed concurrent line set:', number,
                  'optimal omitted-point sets')
        if q == 2:
            count = 0
            good = 0
            for S in combinations(range(P+L), P-1):
                geom = good_by_geometry(points, lines, N, set(S))
                brute = direct_pbh_integer_eigenvalues(
                    points, lines, N, S, (0, 1, 2, 4, 5))
                assert geom == brute, (S, geom, brute)
                count += 1
                good += geom
            assert count == 120 and good > 0
            print('q=2 exhaustive all 120 size-3 placements:', good,
                  'controllable, all classifications matched PBH')
            checks += count
        elif q == 3:
            rnd = Random(230719)
            for _ in range(128):
                S = set(rnd.sample(range(P+L), P-1))
                geom = good_by_geometry(points, lines, N, S)
                T = [i for i in range(P) if i not in S]
                C = [j for j in range(L) if P+j in S]
                rows = [[1 for _ in T]] + [[N[i][j] for i in T] for j in C]
                algebraic = (len({lines[j][2] for j in C}) >= q and
                             rank_mod(rows, 1009) == len(T))
                assert geom == algebraic
                actual = direct_kalman_rank(points, lines, N, S) == P+L
                assert actual == geom, (S, geom, actual)
                checks += 1
        if q == 5:
            assert direct_kalman_rank(points, lines, N, controlled) == P+L
            checks += 1
        print('q=', q, 'points=', P, 'lines=', L,
              'optimal controls=', P-1, 'line controls=', q)
    print('VERIFY_OK', checks)


if __name__ == '__main__':
    test()
