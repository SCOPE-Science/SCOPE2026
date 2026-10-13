#!/usr/bin/env python3
"""Independent RREF enumeration of small finite-field subalgebras and ideals.
For the tensor-two nilpotent algebra with basis V and V tensor V.
Uses only Python's standard library. Run: python3 checker.py
"""
from collections import Counter
from itertools import combinations, product
from math import prod


def gauss(N, K, q):
    if K < 0 or K > N:
        return 0
    if K == 0 or K == N:
        return 1
    top = prod(q**(N-i)-1 for i in range(K))
    bot = prod(q**(K-i)-1 for i in range(K))
    assert top % bot == 0
    return top // bot


def predicted(n, q, ideals=False):
    h = Counter()
    N = n*n
    for r in range(n+1):
        d = (2*n*r-r*r) if ideals else r*r
        for z in range(d, N+1):
            h[(r,z)] += gauss(n,r,q)*gauss(N-d,z-d,q)*q**(r*(N-z))
    return h


def rref_spaces(d, q):
    for k in range(d+1):
        for pivots in combinations(range(d),k):
            free = [(i,j) for i,p in enumerate(pivots)
                    for j in range(p+1,d) if j not in pivots]
            for vals in product(range(q), repeat=len(free)):
                B = [[0]*d for _ in range(k)]
                for i,p in enumerate(pivots):
                    B[i][p] = 1
                for (i,j),v in zip(free,vals):
                    B[i][j] = v
                yield pivots, B


def belongs(v, pivots, B, q):
    a = list(v)
    for p,row in zip(pivots,B):
        c = a[p]
        if c:
            for j in range(p,len(a)):
                a[j] = (a[j]-c*row[j])%q
    return not any(a)


def rank(matrix, q):
    if not matrix:
        return 0
    B = [list(row) for row in matrix]
    nr, nc = len(B),len(B[0]); rank=0
    for j in range(nc):
        piv = next((i for i in range(rank,nr) if B[i][j]%q),None)
        if piv is None:
            continue
        B[piv],B[rank] = B[rank],B[piv]
        inv = pow(B[rank][j], -1,q)
        B[rank] = [inv*x%q for x in B[rank]]
        for i in range(nr):
            if i!=rank and B[i][j]:
                mul = B[i][j]
                B[i] = [(x-mul*y)%q for x,y in zip(B[i],B[rank])]
        rank += 1
        if rank==nr:break
    return rank


def mul(a,b,n,q):
    d=n+n*n
    return [0]*n + [(a[i]*b[j])%q for i in range(n) for j in range(n)]


def brute(n,q):
    d=n+n*n
    sub,ide = Counter(),Counter()
    checked = 0
    for piv,B in rref_spaces(d,q):
        checked += 1
        r=rank([row[:n] for row in B],q)
        z=len(B)-r
        is_sub=all(belongs(mul(a,b,n,q),piv,B,q) for a in B for b in B)
        is_ideal=all(belongs(mul(a,unit,n,q),piv,B,q) and belongs(mul(unit,a,n,q),piv,B,q)
                for a in B for unit in [[int(i==j) for i in range(d)] for j in range(n)])
        if is_sub:sub[(r,z)]+=1
        if is_ideal:ide[(r,z)]+=1
        if is_ideal and not is_sub:raise AssertionError('ideal not subalgebra')
    return sub,ide,checked


def test():
    for n,q in [(1,2),(1,3),(2,2),(2,3)]:
        got_s,got_i,ambient=brute(n,q)
        exp_s,exp_i=predicted(n,q),predicted(n,q,True)
        assert got_s==exp_s,(n,q,'sub',got_s,exp_s)
        assert got_i==exp_i,(n,q,'ideal',got_i,exp_i)
        print('EXHAUSTIVE_OK',f'n={n}',f'q={q}',f'all_spaces={ambient}',
            f'subalgebras={sum(got_s.values())}',f'ideals={sum(got_i.values())}')
    print('VERIFY_OK')

if __name__=='__main__':test()
