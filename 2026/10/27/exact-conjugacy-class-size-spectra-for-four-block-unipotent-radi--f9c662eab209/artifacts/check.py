#!/usr/bin/env python3
"""Independent centralizer-rank verification for radical groups of four-vertex path quivers.

All rows are computed by finite-field elimination on the path multiplication table,
not by the tensor-span formula. Works for prime fields.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def basis_paths(a, c):
    # Arrows 0,...,a-1 connect 0->1; arrow a connects 1->2;
    # arrows a+1,...,a+c connect 2->3.
    paths = [(i,) for i in range(a)] + [(a,)] + [(a+1+j,) for j in range(c)]
    paths += [(i,a) for i in range(a)] + [(a,a+1+j) for j in range(c)]
    paths += [(i,a,a+1+j) for i in range(a) for j in range(c)]
    idx = {p:i for i,p in enumerate(paths)}
    n = len(paths)
    table = []
    for i,p in enumerate(paths):
        for j,r in enumerate(paths):
            joined = p+r
            if joined in idx:
                table.append((i,j,idx[joined]))
    return paths, table


def rank_mod(matrix, q):
    if not matrix: return 0
    a = [row[:] for row in matrix]
    m, n = len(a), len(a[0]); pivot = 0
    for col in range(n):
        sel = next((row for row in range(pivot,m) if a[row][col]%q),None)
        if sel is None: continue
        a[pivot], a[sel] = a[sel], a[pivot]
        inv = pow(a[pivot][col], -1, q)
        a[pivot] = [(z*inv)%q for z in a[pivot]]
        for row in range(m):
            if row!=pivot and a[row][col]:
                coeff=a[row][col]
                a[row]=[(z-coeff*t)%q for z,t in zip(a[row],a[pivot])]
        pivot+=1
        if pivot==m: break
    return pivot


def direct_histogram(q, a, c):
    paths, table = basis_paths(a,c)
    n=len(paths); central=[i for i,p in enumerate(paths) if len(p)==3]
    varying=[i for i in range(n) if i not in central]
    hist=Counter(); checked=0
    for coeffs in product(range(q),repeat=len(varying)):
        x=[0]*n
        for i,t in zip(varying,coeffs): x[i]=t
        matrix=[[0]*n for _ in range(n)]
        for i,j,k in table:
            matrix[k][j]=(matrix[k][j]+x[i])%q
            matrix[k][i]=(matrix[k][i]-x[j])%q
        hist[rank_mod(matrix,q)]+=q**len(central)
        checked+=1
    return hist,checked


def formula_histogram(q,a,c):
    H=Counter()
    def ncount(d,i,z):
        if (i,z)==(0,0):return 1
        if (i,z)==(1,0):return q**d-1
        if (i,z)==(1,1):return q*(q**d-1)
        if (i,z)==(2,1):return (q**d-1)*(q**d-q)
        return 0
    for i,j,zu,zw in product(range(3),range(3),range(2),range(2)):
        count=ncount(a,i,zu)*ncount(c,j,zw)
        rank=int(bool(zu or zw))+i*c+a*j-i*j
        H[rank]+=q**(a*c)*count
    for zu,zw in product(range(2),repeat=2):
        ucount=(q**a-1) if zu else 1
        wcount=(q**c-1) if zw else 1
        span=0 if not (zu or zw) else (c if zu else 0)+(a if zw else 0)-int(bool(zu and zw))
        rank=a+c+span
        H[rank]+=q**(a*c)*(q-1)*q**(a+c)*ucount*wcount
    return +H


def make_product(x,y,table,q,n):
    out=[0]*n
    for i,j,k in table:
        out[k]=(out[k]+x[i]*y[j])%q
    return tuple(out)


def direct_burnside(q,a,c):
    paths,table=basis_paths(a,c)
    n=len(paths)
    els=list(product(range(q),repeat=n))
    cp=0
    for x in els:
        for y in els:
            if make_product(x,y,table,q,n)==make_product(y,x,table,q,n):cp+=1
    assert cp%len(els)==0
    return cp,cp//len(els)


def run():
    combos=[(2,1,1),(3,1,1),(5,1,1),(2,1,2),(3,1,2),(2,2,1),
            (2,2,2),(2,1,3),(2,2,3),(2,3,2)]
    total=0
    for q,a,c in combos:
        actual,m=direct_histogram(q,a,c)
        predicted=formula_histogram(q,a,c)
        assert actual==predicted,(q,a,c,actual,predicted)
        assert sum(actual.values())==q**(1+2*a+2*c+a*c)
        assert all(n%(q**r)==0 for r,n in actual.items())
        k=sum(n//q**r for r,n in actual.items())
        if (q,a,c) in [(2,1,1),(3,1,1),(2,1,2)]:
            pairs,k2=direct_burnside(q,a,c)
            assert k==k2,(q,a,c,k,k2)
        total+=m
        print('q=%d a=%d c=%d noncentral=%d group=%d ranks=%s classes=%d'%
              (q,a,c,m,sum(actual.values()), sorted(actual.items()),k))
    print('FOUR_VERTEX_QUIVER_CLASS_SPECTRA_CHECKS_PASSED cases=%d independent_adjoint_matrices=%d'%(len(combos),total))

if __name__=='__main__':run()
