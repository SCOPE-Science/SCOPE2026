#!/usr/bin/env python3
"""Exact finite support certificate for self-STFT on the Klein four group.
Uses integer arithmetic for all proof-critical steps; no external packages.
"""
from itertools import combinations
from collections import Counter

N = 4
Q = N*N
MOD = 65537

def parity(n):
    return n.bit_count() & 1

def sp(a,b):
    ax, ak = divmod(a,N)
    bx, bk = divmod(b,N)
    return parity((ax & bk)) ^ parity((ak & bx))

H = [[1 if not sp(a,b) else -1 for b in range(Q)] for a in range(Q)]
A = [[H[a][b] - (N if a==b else 0) for b in range(Q)] for a in range(Q)]

def rank_rows(cols):
    basis=[]
    row_indices=[]
    for rid,row in enumerate(A):
        vec=[row[j]%MOD for j in cols]
        for p,b in basis:
            if vec[p]:
                x=vec[p];vec=[(u-x*v)%MOD for u,v in zip(vec,b)]
        p=next((i for i,u in enumerate(vec) if u), None)
        if p is None:continue
        factor=pow(vec[p],-1,MOD);vec=[u*factor%MOD for u in vec]
        for i,(p0,b) in enumerate(basis):
            if b[p]:
                x=b[p];basis[i]=(p0,[(u-x*v)%MOD for u,v in zip(b,vec)])
        loc=next((i for i,(p0,b) in enumerate(basis) if p0>p),len(basis))
        basis.insert(loc,(p,vec))
        row_indices.append(rid)
        if len(row_indices)==len(cols):break
    return len(row_indices),row_indices

def det_int(B):
    """Bareiss exact determinant of an integer square matrix."""
    n=len(B)
    if not n:return 1
    C=[list(row) for row in B]
    sign=1; den=1
    for k in range(n-1):
        if C[k][k]==0:
            p=next((i for i in range(k+1,n) if C[i][k]),None)
            if p is None:return 0
            C[k],C[p]=C[p],C[k];sign=-sign
        pivot=C[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                x=C[i][j]*pivot-C[i][k]*C[k][j]
                assert x%den==0
                C[i][j]=x//den
            C[i][k]=0
        den=pivot
    return sign*C[n-1][n-1]

def kernel_cofactors(cols,rows):
    """For rank k-1, construct an exact kernel vector from (k-1)x(k-1) cofactors."""
    B=[[A[r][j] for j in cols] for r in rows]
    return [(-1)**i*det_int([[row[j] for j in range(len(cols)) if j!=i] for row in B]) for i in range(len(cols))]

def in_kernel(cols,v):
    return all(sum(row[j]*vv for j,vv in zip(cols,v))==0 for row in A)

lag=set()
for x,y in combinations(range(1,Q),2):
    if sp(x,y)==0:
        lag.add(frozenset((0,x,y,x^y)))
assert len(lag)==15
unions={L|K for L in lag for K in lag if len(L&K)==2}
assert len(unions)==45

rank_counts={}
full_positive={}
support_examples={}
for size in [4,5,6]:
    hist=Counter(); positive=set()
    for tail in combinations(range(1,Q),size-1):
        S=(0,)+tail
        r,rows=rank_rows(S)
        hist[r]+=1
        if r==size:
            continue
        if r==size-1:
            v=kernel_cofactors(S,rows)
            assert any(v)
            if not in_kernel(S,v):
                continue  # Complex rank is actually full.
            if (all(x>0 for x in v) or all(x<0 for x in v)):
                positive.add(frozenset(S)); support_examples[tuple(S)]=v
        elif size==6 and r==size-2:
            assert frozenset(S) in unions
            # Two independent indicator vectors in the exact kernel;
            # their positive sum has precisely the union as support.
            left,right=next((L,K) for L in lag for K in lag if L|K==frozenset(S) and len(L&K)==2)
            assert in_kernel(S,[int(j in left) for j in S])
            assert in_kernel(S,[int(j in right) for j in S])
            positive.add(frozenset(S))
        else:
            raise AssertionError((size,S,r))
    rank_counts[size]=hist
    full_positive[size]=positive
    print('size',size,'rank_mod65537_counts',dict(sorted(hist.items())), 'strict_positive_supports',len(positive))
assert full_positive[4]==lag
assert full_positive[5]==set()
assert full_positive[6]==unions
# For all rank-4 size-6 supports, kernel dimension is exactly two and generated
# by the two lagrangian indicator vectors: from mod-rank 4 and exact nullity >=2.
assert rank_counts[6][4]==45
print('lagrangian_planes',len(lag),'distinct_unions',len(unions))
print('PASS: exhaustive integer certificate; minimum 4, no 5, and 6 iff union of intersecting Lagrangian planes.')

# Explicit normalized 2-qubit vector (a,b,0,0) with a^2+b^2=1,
# a,b both nonzero and a^2 != b^2: select a=3/5,b=4/5.
# Its one-qubit Bloch x = 24/25, z = -7/25, y=0,
# and the other qubit's stabilizer is Z.
from fractions import Fraction
f = [Fraction(3,5), Fraction(4,5), Fraction(0), Fraction(0)]
w = []
for x in range(N):
    for k in range(N):
        amp = sum(f[t]*f[t^x]*(-1)**parity(k&t) for t in range(N))
        w.append(amp*amp)
assert {j for j,entry in enumerate(w) if entry} == frozenset((0,1,2,3,4,6))
assert [sum(H[u][v]*w[v] for v in range(Q)) for u in range(Q)] == [N*z for z in w]
print('EXAMPLE: f=(3/5,4/5,0,0); six nonzero ambiguity entries at {0,1,2,3,4,6}; exact symplectic Fourier eigenidentity PASS.')
