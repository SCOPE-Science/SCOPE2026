#!/usr/bin/env python3
"""Exact integer checks for the parity and local charts of cycle-root fans.
Works without third-party dependencies; it checks finite cases, not the infinite proof.
"""
from itertools import product, combinations
from math import comb


def determinant(A):
    # Fraction-free Bareiss exact determinant, matrix as rows.
    A=[list(row) for row in A]
    n=len(A)
    if n==0:
        return 1
    sign=1
    den=1
    for k in range(n-1):
        if A[k][k]==0:
            p=next((i for i in range(k+1,n) if A[i][k]),None)
            if p is None:
                return 0
            A[k],A[p]=A[p],A[k]
            sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num % den == 0
                A[i][j]=num//den
            A[i][k]=0
        den=pivot
    return sign*A[-1][-1]


def test(n):
    d=n-1
    ray=[tuple(1 if i==j else 0 for i in range(d)) for j in range(d)]
    ray.append(tuple(-1 for _ in range(d)))
    rays=ray+ [tuple(-a for a in v) for v in ray]
    # Enumerate ternary candidates of the polar |u_i|<=1, |sum u_i|<=1.
    # An interior cube-edge point is a vertex only if it activates a slab wall.
    verts=[]
    for u in product((-1,0,1), repeat=d):
        s=sum(u)
        if abs(s)>1:
            continue
        zero=u.count(0)
        if zero==0 or (zero==1 and abs(s)==1):
            verts.append(u)
    expected = comb(n,n//2) if n%2==0 else comb(n-1,(n-1)//2) + (n-1)*2*comb(n-2,(n-1)//2)
    assert len(verts)==expected, (n,len(verts),expected)
    non_simple=0
    for u in verts:
        got=[v for v in rays if sum(x*y for x,y in zip(u,v))==1]
        assert all(sum(x*y for x,y in zip(u,v))<=1 for v in rays)
        if n%2==1:
            assert len(got)==d
            mat=[[v[i] for v in got] for i in range(d)]
            assert abs(determinant(mat))==1
        else:
            assert len(got)==n
            non_simple+=1
            # Every d-element subfamily of this circuit is an integral basis.
            for subset in combinations(got,d):
                mat=[[v[i] for v in subset] for i in range(d)]
                assert abs(determinant(mat))==1
            # Unique primitive dependence is balanced: coefficients ±1.
            coeff=[]
            for v in got:
                j=next(i for i,w in enumerate(ray) if v==w or v==tuple(-a for a in w))
                coeff.append(1 if v==ray[j] else -1)
            assert sum(coeff)==0
            assert all(sum(c*v[i] for c,v in zip(coeff,got))==0 for i in range(d))
            assert coeff.count(1)==coeff.count(-1)==n//2
    if n%2==0:
        r=n//2
        # Purely semigroup-theoretic check: every balanced exponent vector
        # of degrees <=3 is a sum of r-by-r rank-one matrix generators.
        pos={x for x in product(range(4),repeat=r) if sum(x)<=3}
        for a in pos:
            for b in pos:
                if sum(a)!=sum(b):
                    continue
                i=list(a)
                j=list(b)
                pairs=[]
                for ai,ac in enumerate(i):
                    pairs.extend([ai]*ac)
                for bj,bc in enumerate(j):
                    j[bj]=bc
                cols=[]
                for bj,bc in enumerate(j):
                    cols.extend([bj]*bc)
                assert len(pairs)==len(cols)==sum(a)
                M=[[0]*r for _ in range(r)]
                for ii,jj in zip(pairs,cols):
                    M[ii][jj]+=1
                assert tuple(map(sum,M))==a
                assert tuple(sum(M[ii][jj] for ii in range(r)) for jj in range(r))==b
        assert non_simple==comb(2*r,r)
        print('n=%d dimension=%d singular_fixed=%d rank_one_matrix=%dx%d multiplicity=%d'%(n,d,non_simple,r,r,comb(2*r-2,r-1)))
    else:
        assert non_simple==0
        print('n=%d dimension=%d smooth_fixed=%d singular_fixed=0'%(n,d,len(verts)))

if __name__=='__main__':
    for n in range(3,11):
        test(n)
    print('VERIFY_OK')
