#!/usr/bin/env python3
"""Finite-field controls for the off-diagonal Gram three-vector critical-value theorem.

These finite checks do not replace the all-dimensional algebraic proof.
"""
from itertools import product

def dot(x, y, p):
    return sum(a*b for a,b in zip(x,y)) % p

def rank_mod(mat, p):
    a = [list(row) for row in mat]
    nr, nc = len(a), len(a[0])
    r = 0
    for c in range(nc):
        pivot = next((j for j in range(r, nr) if a[j][c] % p), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(v*inv)%p for v in a[r]]
        for j in range(nr):
            if j != r and a[j][c]:
                z = a[j][c]
                a[j] = [(a[j][l]-z*a[r][l])%p for l in range(nc)]
        r += 1
        if r == nr:
            break
    return r

def check_rank_three_vectors(M, p):
    observed = set()
    checked = 0
    for xs in product(range(p), repeat=3*M):
        vs = [xs[i*M:(i+1)*M] for i in range(3)]
        v1,v2,v3=vs
        target = (dot(v1,v2,p),dot(v1,v3,p),dot(v2,v3,p))
        rows = (
            tuple(v2) + tuple(v1) + (0,)*M,
            tuple(v3) + (0,)*M + tuple(v1),
            (0,)*M + tuple(v3) + tuple(v2),
        )
        observed_critical = rank_mod(rows,p)<3
        rank_columns = rank_mod(vs,p)
        predicted_critical = rank_columns <= 1 and any(all(entry == 0 for entry in v) for v in vs)
        # For rank one a,b,c nonzero, all three targets are nonzero.
        if observed_critical != predicted_critical:
            raise AssertionError((M,p,vs,target,observed_critical,predicted_critical))
        if observed_critical:
            if sum(x!=0 for x in target)>1:
                raise AssertionError(('critical target outside axes',vs,target))
            observed.add(target)
        checked += 1
    expected = {(0,0,0)} | {(a,0,0) for a in range(1,p)} | {(0,a,0) for a in range(1,p)} | {(0,0,a) for a in range(1,p)}
    assert observed==expected, (observed,expected)
    return checked

def verify_local_rank(M, p):
    # The normal equation on a nonzero target axis is sum_{i=2}^M x_i y_i.
    # Its Hessian in (x_2,...,x_M,y_2,...,y_M) is [[0,I],[I,0]].
    n=M-1
    h=[([0]*n+[int(i==j) for j in range(n)] if i<n
        else [int(i-n==j) for j in range(n)]+[0]*n)
       for i in range(2*n)]
    assert rank_mod(h,p)==2*n

if __name__=='__main__':
    n=check_rank_three_vectors(3,3)
    assert n == 3**9
    for M in range(3,9):
        verify_local_rank(M,3)
    print('GRAM_DISCRIMINANT_EXACT_OK; frames=',n)
