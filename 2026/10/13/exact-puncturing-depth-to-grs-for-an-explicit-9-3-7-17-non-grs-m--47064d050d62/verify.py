#!/usr/bin/env python3
from itertools import combinations

P = 17
S = (0, 2, 3, 4, 5, 7, 9, 10, 16)
EXPECTED_SIX = {
    (0, 2, 3, 5, 7, 9),
    (0, 2, 4, 5, 10, 16),
    (0, 2, 4, 7, 9, 10),
    (0, 3, 4, 7, 10, 16),
    (0, 3, 5, 9, 10, 16),
    (4, 5, 7, 9, 10, 16),
}


def inv(a):
    return pow(a % P, -1, P)


def rref(a):
    a = [[x % P for x in row] for row in a]
    m = len(a)
    n = len(a[0]) if m else 0
    pivots = []
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        z = inv(a[r][c])
        a[r] = [(z*x) % P for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                z = a[i][c]
                a[i] = [(a[i][j] - z*a[r][j]) % P for j in range(n)]
        pivots.append(c)
        r += 1
        if r == m:
            break
    return a, pivots


def rank(a):
    return len(rref(a)[1])


def point(t):
    return (1, pow(t, 3, P), pow(t, 4, P))


def quadrow(t):
    x, y, z = point(t)
    return (x*x % P, y*y % P, z*z % P, x*y % P, x*z % P, y*z % P)


def null_vector(a):
    rr, piv = rref(a)
    free = [j for j in range(len(a[0])) if j not in piv]
    assert len(free) == 1
    f = free[0]
    v = [0]*len(a[0])
    v[f] = 1
    for i, c in enumerate(piv):
        v[c] = (-rr[i][f]) % P
    return tuple(v)

# Independent MDS check: every three displayed columns are independent.
points = {t: point(t) for t in S}
for triple in combinations(S, 3):
    assert rank([points[t] for t in triple]) == 3, triple

rank_census = {}
grs_subsets = {}
for m in range(5, 10):
    rc = {}
    good = []
    for T in combinations(S, m):
        r = rank([quadrow(t) for t in T])
        rc[r] = rc.get(r, 0) + 1
        if r < 6:
            good.append(T)
    rank_census[m] = rc
    grs_subsets[m] = good

assert rank_census == {
    5: {5: 126},
    6: {6: 78, 5: 6},
    7: {6: 36},
    8: {6: 9},
    9: {6: 1},
}
assert set(grs_subsets[6]) == EXPECTED_SIX
assert len(grs_subsets[5]) == 126
assert not grs_subsets[7] and not grs_subsets[8] and not grs_subsets[9]

print('MDS_TRIPLE_CHECKS', len(list(combinations(S, 3))))
print('CONIC_RANK_CENSUS', rank_census)
print('SIX_POINT_GRS_SURVIVORS')
for T in sorted(EXPECTED_SIX):
    q = null_vector([quadrow(t) for t in T])
    deleted = tuple(t for t in S if t not in T)
    print(' survive', T, 'delete', deleted, 'conic_coefficients', q)
print('MINIMUM_PUNCTURES_TO_GRS', 3)
print('GRS_TRIPLE_DELETIONS', 6)
print('ALL_FOUR_DELETIONS_GRS', len(grs_subsets[5]))
print('VERIFY_OK')
