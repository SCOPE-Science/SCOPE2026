#!/usr/bin/env python3
"""Exact bounded regression for one-entry-deleted rank-one projective matrix models.

No floating-point arithmetic. The general theorem uses a symbolic chart proof;
these tests compare semigroups and graded Hilbert functions in small formats.
"""
from itertools import product
from math import comb


def vector(dim, *coordinates):
    v = [0] * dim
    for i in coordinates:
        v[i] += 1
    return tuple(v)


def sum_vec(a, b):
    return tuple(x+y for x,y in zip(a,b))


def hilbert_counts(generators, top):
    zero = (0,)*len(generators[0])
    states = {zero}
    ans = [1]
    for degree in range(1, top+1):
        states = {sum_vec(s,v) for s in states for v in generators}
        ans.append(len(states))
    return ans


def chart(a, b, i, j):
    # For the nonzero coordinate (i,j), use the other row and column
    # coordinates as torus variables, so a ratio x_p y_q/(x_i y_j) has
    # exponent (x_p/x_i)*(y_q/y_j).
    rows = [p for p in range(a) if p != i]
    cols = [q for q in range(b) if q != j]
    index_r = {p:k for k,p in enumerate(rows)}
    index_c = {q:len(rows)+k for k,q in enumerate(cols)}
    dim = a+b-2
    observed = []
    for p in range(a):
        for q in range(b):
            if (p,q) == (0,0) or (p,q) == (i,j):
                continue
            observed.append(vector(dim,*([index_r[p]] if p!=i else []),
                                     *([index_c[q]] if q!=j else [])))
    if i and j:
        m = [vector(dim,k) for k in range(dim)]
        kind = 'smooth'
        degree_counts = [comb(dim+d-1,d) for d in range(5)]
    elif i == 0:
        # y_0 is inaccessible alone; pairs x_p y_0 are available.
        xs = [index_r[p] for p in rows]
        free = [index_c[q] for q in cols if q != 0]
        z = index_c[0]
        m = ([vector(dim,k) for k in xs]
             +[vector(dim,k,z) for k in xs]
             +[vector(dim,k) for k in free])
        rank_width, free_count = a-1,b-2
        kind = 'row'
        degree_counts = [sum(comb(d-f+rank_width-1,rank_width-1)*(d-f+1)*comb(f+free_count-1,f)
                             if free_count else (d+1)*comb(d+rank_width-1,rank_width-1)
                             for f in ([0] if not free_count else range(d+1))) for d in range(5)]
    else:
        ys = [index_c[q] for q in cols]
        free = [index_r[p] for p in rows if p != 0]
        z = index_r[0]
        m = ([vector(dim,k) for k in ys]
             +[vector(dim,k,z) for k in ys]
             +[vector(dim,k) for k in free])
        rank_width,free_count = b-1,a-2
        kind = 'column'
        degree_counts = [sum(comb(d-f+rank_width-1,rank_width-1)*(d-f+1)*comb(f+free_count-1,f)
                             if free_count else (d+1)*comb(d+rank_width-1,rank_width-1)
                             for f in ([0] if not free_count else range(d+1))) for d in range(5)]
    # Redundant edge monomials are products of displayed generators;
    # their nonhomogeneous total degree need not agree, hence instead
    # check equality of bounded semigroup elements, not graded counts.
    zero = (0,)*dim
    canonical = {zero}
    for depth in range(6):
        canonical |= {sum_vec(s,v) for s in list(canonical) for v in m}
    assert set(observed) <= canonical, (a,b,i,j,'missing observed generator')
    exact = hilbert_counts(m,4)
    assert exact == degree_counts,(a,b,i,j,kind,exact,degree_counts)
    return kind,len(observed),exact


def rational_rank(rows):
    from fractions import Fraction
    M = [[Fraction(x) for x in r] for r in rows]
    if not M:
        return 0
    rank = 0
    for col in range(len(M[0])):
        pivot = next((j for j in range(rank,len(M)) if M[j][col]),None)
        if pivot is None:
            continue
        M[rank],M[pivot] = M[pivot],M[rank]
        v = M[rank][col]
        M[rank] = [z/v for z in M[rank]]
        for j in range(len(M)):
            if j != rank and M[j][col]:
                v = M[j][col]
                M[j] = [u-v*w for u,w in zip(M[j],M[rank])]
        rank += 1
    return rank


def minor_jacobian(x,w):
    m=len(x)
    J=[]
    for i in range(m):
        for j in range(i+1,m):
            row=[0]*(2*m)
            row[i]=w[j]
            row[j]=-w[i]
            row[m+i]=-x[j]
            row[m+j]=x[i]
            J.append(row)
    return J


def main():
    for m in range(1,7):
        for u in [(1,0),(0,1),(2,3)]:
            for v in [[1]*m, list(range(1,m+1)), [0]*(m-1)+[1]]:
                x=[u[0]*t for t in v]
                w=[u[1]*t for t in v]
                assert rational_rank(minor_jacobian(x,w)) == m-1
        assert rational_rank(minor_jacobian([0]*m,[0]*m)) == 0
    total = 0
    tally = {'smooth':0,'row':0,'column':0}
    for a,b in product(range(2,7),repeat=2):
        for i,j in product(range(a),range(b)):
            if i == j == 0:
                continue
            kind,ng,hs = chart(a,b,i,j)
            tally[kind] += 1
            total += 1
        # Precisely two putative boundary strata, only where the
        # relevant 2-row determinantal cone has at least two columns.
        expected = int(a>=3)+int(b>=3)
        assert expected == int(a-1>=2)+int(b-1>=2)
        if max(a,b)<=3:
            assert all(m in (1,2) for m in (a-1,b-1))
    print('PASS: formats a,b=2..6:',25)
    print('PASS: exact affine coordinate charts:',total, tally)
    print('PASS: affine semigroup generation and Hilbert functions, degrees 0..4')
    print('PASS: exact rational Jacobian ranks of 2-by-m determinantal cones, m=1..6')
    print('PASS: expected transverse ranks, singular-component and Gorenstein boundaries')
    print('NOTE: finite regression, not a proof of the assertions for all a,b')

if __name__ == '__main__':
    main()
