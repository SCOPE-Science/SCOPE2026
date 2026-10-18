"""Exact rational-inertia certificate for the kayak-paddle line-graph classification.

Run: python3 verify_kayak.py
Only Python's standard library is used. All spectral signs are exact rationals.
"""
from fractions import Fraction

# For p<=q from 3 to 6, each pair gives (signature,nullity) for odd and even bridge lengths.
BASE = {
    (3, 3): ((-2, 1), (-2, 0)),
    (3, 4): ((-1, 1), (-1, 2)),
    (3, 5): ((-1, 0), ( 0, 0)),
    (3, 6): ((-2, 0), (-1, 0)),
    (4, 4): (( 0, 3), ( 0, 2)),
    (4, 5): (( 1, 1), ( 0, 1)),
    (4, 6): (( 0, 1), (-1, 1)),
    (5, 5): (( 1, 0), ( 0, 0)),
    (5, 6): (( 0, 0), (-1, 0)),
    (6, 6): ((-1, 0), (-1, 1)),
}


def kayak_edges(p, q, r):
    assert p >= 3 and q >= 3 and r >= 1
    edges = [(i, (i+1)%p) for i in range(p)]
    edges += [(p+i, p+(i+1)%q) for i in range(q)]
    path = [0] + list(range(p+q, p+q+r-1)) + [p]
    edges += list(zip(path, path[1:]))
    n = p+q+r-1
    assert len(edges) == p+q+r
    assert len({tuple(sorted(e)) for e in edges}) == len(edges)
    return n, edges


def inertia_exact(matrix):
    """Sylvester inertia by symmetric rational congruences with 1x1/2x2 pivots."""
    a = [[Fraction(z) for z in row] for row in matrix]
    positive = negative = zero = 0
    while a:
        n = len(a)
        k = next((i for i in range(n) if a[i][i]), None)
        if k is not None:
            if k:
                a[0], a[k] = a[k], a[0]
                for row in a:
                    row[0], row[k] = row[k], row[0]
            pivot = a[0][0]
            positive += int(pivot > 0)
            negative += int(pivot < 0)
            a = [[a[i][j] - a[i][0]*a[0][j]/pivot
                  for j in range(1, n)] for i in range(1, n)]
        else:
            pair = next(((i, j) for i in range(n) for j in range(i+1, n)
                         if a[i][j]), None)
            if pair is None:
                zero += n
                break
            i, j = pair
            permutation = [i, j] + [k for k in range(n) if k not in pair]
            a = [[a[ii][jj] for jj in permutation] for ii in permutation]
            coupling = a[0][1]
            positive += 1
            negative += 1
            a = [[a[ii][jj] -
                  (a[ii][0]*a[1][jj] + a[ii][1]*a[0][jj])/coupling
                  for jj in range(2, n)] for ii in range(2, n)]
    return positive, zero, negative


def line_graph_matrix(p, q, r):
    _, edges = kayak_edges(p, q, r)
    m = len(edges)
    return [[int(i != j and bool(set(edges[i]) & set(edges[j])))
             for j in range(m)] for i in range(m)]


def shifted_signless_matrix(p, q, r):
    n, edges = kayak_edges(p, q, r)
    a = [[0]*n for _ in range(n)]
    for i, j in edges:
        a[i][i] += 1
        a[j][j] += 1
        a[i][j] += 1
        a[j][i] += 1
    for i in range(n):
        a[i][i] -= 2
    return a


def predicted_inertia(p, q, r):
    pp = 3+(p-3)%4
    qq = 3+(q-3)%4
    pair = min(pp, qq), max(pp, qq)
    signature, nullity = BASE[pair][(r+1)%2]
    m = p+q+r
    assert (m-nullity+signature)%2 == 0
    return ((m-nullity+signature)//2, nullity,
            (m-nullity-signature)//2)


def check():
    # Check every base entry twice: 20 direct line-adjacency calculations and
    # 20 independently assembled shifted-signless-Laplacian calculations.
    base_count = 0
    for (p,q), (odd,even) in BASE.items():
        for r, expected in [(1,odd),(2,even)]:
            direct = inertia_exact(line_graph_matrix(p,q,r))
            u,z,v = inertia_exact(shifted_signless_matrix(p,q,r))
            assert direct == (u,z,v+1), (p,q,r,direct,(u,z,v+1))
            assert (direct[0]-direct[2],direct[1]) == expected, (p,q,r,direct,expected)
            assert direct == predicted_inertia(p,q,r)
            base_count += 1
    # Exact larger-parameter checks are supplemental to the proved subdivisions.
    extended_count = 0
    for p in range(3,18):
        for q in range(p,18):
            for r in range(1,12):
                u,z,v = inertia_exact(shifted_signless_matrix(p,q,r))
                assert (u,z,v+1) == predicted_inertia(p,q,r), (p,q,r,u,z,v)
                extended_count += 1
    print('BASE_CASES_EXACT',base_count)
    print('EXTENDED_CASES_EXACT',extended_count)
    print('ALL_CHECKS_PASS')


if __name__ == '__main__':
    check()
