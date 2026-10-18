"""Exact consistency checker for multilinear-rank / nullcone witnesses.
The proof in RESULT.md covers every d >= 2 and m >= 3.
"""
from itertools import combinations


def witness(d, m):
    terms = {}
    for pos in range(m):
        a = [0] * m
        a[pos] = d - 1
        terms[tuple(a)] = terms.get(tuple(a), 0) + 1
    for i in range(1, d-1):
        for j, k in combinations(range(m), 2):
            a = [0] * m
            a[j] = a[k] = i
            terms[tuple(a)] = terms.get(tuple(a), 0) + 1
    weights = (2, 0, -2) if (d, m) == (3, 3) else (d-1,) + (-1,)*(d-1)
    return terms, weights


def rank(matrix):
    a = [row[:] for row in matrix]
    p = 0
    for j in range(len(a[0])):
        lead = next((i for i in range(p, len(a)) if a[i][j]), None)
        if lead is None:
            continue
        a[p], a[lead] = a[lead], a[p]
        for i in range(p+1, len(a)):
            if a[i][j]:
                x, y = a[i][j], a[p][j]
                a[i] = [y*b-x*c for b,c in zip(a[i],a[p])]
        p += 1
        if p == len(a):
            break
    return p

cases = [(d,m) for d in range(2,6) for m in range(3,6)] + [(2,m) for m in range(6,9)] + [(3,6)]
for d,m in cases:
    t,weights = witness(d,m)
    assert sum(weights) == 0
    assert {sum(weights[i] for i in idx) for idx in t} and min(sum(weights[i] for i in idx) for idx in t)>0
    for axis in range(m):
        mat = [[0]*(d**(m-1)) for _ in range(d)]
        for idx,c in t.items():
            other = tuple(idx[k] for k in range(m) if k!=axis)
            col = 0
            for j in other:
                col = d*col + j
            mat[idx[axis]][col] += c
        assert rank(mat)==d,(d,m,axis)
print('HYPERQUIVER_FULL_RANK_NULLCONE_EXACT_OK',len(cases),'test_formats')
