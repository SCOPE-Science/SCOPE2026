#!/usr/bin/env python3
"""Independent direct finite-field row-space check of maximal abelian subspaces."""
from itertools import combinations, product
from math import floor

def rref_planes(n,k,q):
    for piv in combinations(range(n),k):
        free=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
        for values in product(range(q),repeat=len(free)):
            mat=[[0]*n for _ in range(k)]
            for i,j in enumerate(piv): mat[i][j]=1
            for (i,j),a in zip(free,values):mat[i][j]=a
            yield mat

def bracket_zero(M,n,q):
    k=len(M)
    return all((M[a][j]*M[b][(j+1)%n]-M[b][j]*M[a][(j+1)%n])%q==0 for a in range(k) for b in range(a+1,k) for j in range(n))

def count(n,q):
    k=n//2
    count=0; total=0
    for M in rref_planes(n,k,q):
        total+=1
        count+=bracket_zero(M,n,q)
    predicted=2 if n%2==0 else n*q
    assert count==predicted, (n,q,count,predicted)
    print(f'n={n} q={q} k={k} total_Gr={total} abelian={count} predicted={predicted}')

if __name__=='__main__':
    for n,q in [(4,2),(4,3),(4,5),(5,2),(5,3),(5,5),(6,2),(6,3),(7,2)]:count(n,q)
    print('VERIFY_OK_CYCLE_MAXIMAL_ABELIAN')
