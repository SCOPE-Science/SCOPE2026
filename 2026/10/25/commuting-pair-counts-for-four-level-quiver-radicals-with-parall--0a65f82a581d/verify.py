#!/usr/bin/env python3
"""Finite-field sanity checks for the four-level path radical count."""
from itertools import product
from math import prod


def rank_count(m, n, r, q):
    if r == 0: return 1
    return prod((q**m-q**i)*(q**n-q**i) for i in range(r)) // prod(q**r-q**i for i in range(r))

def formula(a,c,q):
    d=2*a+2*c+1+a*c
    z=sum(rank_count(a,4,r,q)*q**((4-r)*c) for r in range(min(a,4)+1))
    s = (q**(2*(a+c))
          + (q**a-1)*q**(2*(a+c)-c)
          + (q**c-1)*q**(2*(a+c)-a)
          + (q**a-1)*(q**c-1)*q**(a+c+1))
    return q**(2*a*c)*(z+(q*q-1)*s)

def rank_mod(cols,d,q):
    v=[[cols[j][i] % q for j in range(d)] for i in range(d)]
    rank=0
    for j in range(d):
        piv=next((i for i in range(rank,d) if v[i][j]), None)
        if piv is None: continue
        v[piv],v[rank]=v[rank],v[piv]
        inv=pow(v[rank][j],-1,q)
        v[rank]=[(x*inv)%q for x in v[rank]]
        for i in range(rank+1,d):
            if v[i][j]:
                f=v[i][j]
                v[i]=[(v[i][k]-f*v[rank][k])%q for k in range(d)]
        rank+=1
        if rank==d: break
    return rank

def direct(a,c,q):
    # q is prime in the direct finite-field check (2,3 only).
    d=2*a+2*c+1+a*c
    B=a; C=a+1; AB=C+c; BC=AB+a; ABC=BC+c
    mult={}
    for i in range(a):
        mult[(i,B)]=AB+i
        for j in range(c): mult[(i,BC+j)]=ABC+i*c+j
    for j in range(c): mult[(B,C+j)]=BC+j
    for i in range(a):
        for j in range(c): mult[(AB+i,C+j)]=ABC+i*c+j
    # For each x in J, ad_x : y->xy-yx is linear. Number of commuting y is q^(d-rank).
    total=0
    for x in product(range(q),repeat=d):
        columns=[]
        for j in range(d):
            col=[0]*d
            for i,z in enumerate(x):
                if not z:continue
                ij=mult.get((i,j)); ji=mult.get((j,i))
                if ij is not None:col[ij]+=z
                if ji is not None:col[ji]-=z
            columns.append(col)
        total+=q**(d-rank_mod(columns,d,q))
    return total

if __name__=='__main__':
    for a,c,q in [(1,1,2),(1,1,3),(2,1,2),(1,2,2),(2,2,2)]:
        val=direct(a,c,q); expected=formula(a,c,q)
        print(f"(a,c,q)=({a},{c},{q}), direct={val}, formula={expected}, equality={val==expected}")
        assert val==expected
    print('VERIFIED all finite checks')
