#!/usr/bin/env python3
"""Exact rational checks of the local derived-Hodge d1 block for truncated polynomial rings.

For A=Q[t]/(t^m), the two-term model of wedge^p L_A for p>=1 is
A (degree -p) --m*t^(m-1)--> A (degree -p+1).
The nontrivial horizontal d1 blocks are derivatives from (t) to
A/(t^(m-1)), and at p=0 from A to A/(t^(m-1)).
These finite checks illustrate, but do not prove, the Euler-homotopy theorem.
"""
from fractions import Fraction

def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    nrows=len(a); ncols=len(a[0]) if a else 0
    r=0
    for c in range(ncols):
        pivot = next((i for i in range(r,nrows) if a[i][c]), None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        scale=a[r][c]
        a[r]=[v/scale for v in a[r]]
        for i in range(nrows):
            if i != r and a[i][c]:
                f=a[i][c]
                a[i]=[a[i][j]-f*a[r][j] for j in range(ncols)]
        r +=1
    return r

def check(m,p):
    assert m>=2 and p>=0
    # Domain basis: 1,t,...,t^(m-1) when p=0;
    # t,...,t^(m-1) when p>=1.
    exps = list(range(0 if p==0 else 1,m))
    # Codomain basis 1,...,t^(m-2) for all p.
    mat = [[(j if j-1==i else 0) for j in exps] for i in range(m-1)]
    r=rank(mat)
    assert r == m-1, (m,p,r)
    assert (len(exps)-r) == (1 if p==0 else 0)
    # Vertical differential t^(m-1) from A to A has rank one.
    vert = [[m if (j==0 and i==m-1) else 0
             for j in range(m)] for i in range(m)]
    assert rank(vert)==1
    return 1

def main():
    tests=sum(check(m,p) for m in range(2,18) for p in range(0,14))
    print('VERIFY_OK', tests, 'exact local E1 blocks checked')

if __name__=='__main__':main()
