#!/usr/bin/env python3
from itertools import combinations, product
from collections import Counter

Q = 3
G = [
 [1,0,0,0,0,2,2,1,1,0,0,2,0,2,1,1,2,2,2,0,0,0,0,1],
 [0,1,0,2,0,1,0,0,2,0,2,1,1,0,2,1,2,1,0,2,2,2,2,1],
 [0,0,1,2,0,0,1,2,2,2,0,2,1,0,2,0,2,0,1,1,1,0,2,0],
 [0,0,0,0,1,1,1,1,2,2,2,2,1,1,1,1,0,0,0,0,0,1,1,1],
 [0,0,0,1,0,2,0,1,1,1,0,0,2,1,0,2,0,0,1,1,0,1,0,2],
 [0,0,0,0,0,0,1,2,1,1,0,1,1,1,0,1,2,2,0,2,1,1,0,2],
]
K, N = len(G), len(G[0])
EXPECTED_HISTS = {
 1:{12:16,13:35,14:54,15:50,16:63,17:48,18:42,19:27,20:24,21:4,22:1},
 2:{16:1,17:41,18:307,19:955,20:1721,21:2598,22:2716,23:2018,24:654},
 3:{19:3,20:150,21:1511,22:5577,23:12738,24:13901},
 4:{21:3,22:267,23:2361,24:8380},
 5:{23:24,24:340},
 6:{24:1},
}
EXPECTED_WD = {0:1,12:32,13:70,14:108,15:100,16:126,17:96,18:84,19:54,20:48,21:8,22:2}
EXPECTED_DUAL_TRIPLES = {
 (1,15,23):(1,2,1),
 (2,5,11):(1,1,1),
 (8,12,24):(1,2,1),
}
EXPECTED_UNIQUE_D2_ZERO = [1,2,9,10,14,15,22,23]

def rank(A):
    A=[row[:] for row in A]; m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]%Q),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        inv=pow(A[r][c]%Q,-1,Q); A[r]=[(x*inv)%Q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%Q:
                f=A[i][c]%Q
                A[i]=[(A[i][j]-f*A[r][j])%Q for j in range(n)]
        r+=1
        if r==m: break
    return r

def det(A):
    A=[row[:] for row in A]; d=1; m=len(A)
    for c in range(m):
        p=next((i for i in range(c,m) if A[i][c]%Q),None)
        if p is None: return 0
        if p!=c: A[c],A[p]=A[p],A[c]; d=(-d)%Q
        piv=A[c][c]%Q; d=d*piv%Q; inv=pow(piv,-1,Q)
        for i in range(c+1,m):
            f=A[i][c]*inv%Q
            for j in range(c,m): A[i][j]=(A[i][j]-f*A[c][j])%Q
    return d%Q

def matmul(A,B):
    return [[sum(x*y for x,y in zip(row,col))%Q for col in zip(*B)] for row in A]

def rref_subspaces(k,r):
    for pivs in combinations(range(k),r):
        pset=set(pivs)
        free=[(i,j) for i,p in enumerate(pivs) for j in range(p+1,k) if j not in pset]
        for vals in product(range(Q),repeat=len(free)):
            B=[[0]*k for _ in range(r)]
            for i,p in enumerate(pivs): B[i][p]=1
            for (i,j),v in zip(free,vals): B[i][j]=v
            yield B

def projective_key(col):
    if not any(col): return None
    t=next(x for x in col if x); inv=pow(t,-1,Q)
    return tuple((x*inv)%Q for x in col)

assert rank(G)==6
Gram=[[sum(G[i][t]*G[j][t] for t in range(N))%Q for j in range(K)] for i in range(K)]
assert det(Gram)==1

wd=Counter()
for a in product(range(Q), repeat=K):
    word=[sum(a[i]*G[i][j] for i in range(K))%Q for j in range(N)]
    wd[sum(x!=0 for x in word)] += 1
assert dict(sorted(wd.items())) == EXPECTED_WD

keys=[projective_key(tuple(G[i][j] for i in range(K))) for j in range(N)]
assert None not in keys and len(set(keys))==N

dual_triples={}
for S in combinations(range(N),3):
    for coeff in product((1,2),repeat=3):
        if coeff[0]!=1: continue
        if all(sum(coeff[t]*G[i][S[t]] for t in range(3))%Q==0 for i in range(K)):
            dual_triples[tuple(x+1 for x in S)] = coeff
            break
assert dual_triples == EXPECTED_DUAL_TRIPLES

hists={}; unique_d2_zero=None; total=0
for r in range(1,K+1):
    h=Counter(); minimizers=[]
    for B in rref_subspaces(K,r):
        BG=matmul(B,G)
        support=[j for j in range(N) if any(BG[i][j] for i in range(r))]
        s=len(support)
        # Independent support check using annihilation of the generator columns.
        zero_count=sum(all(sum(B[i][t]*G[t][j] for t in range(K))%Q==0 for i in range(r)) for j in range(N))
        assert s == N-zero_count
        h[s]+=1
        minimizers.append((s,B,support))
    got=dict(sorted(h.items()))
    assert got == EXPECTED_HISTS[r]
    total += sum(h.values())
    if r==2:
        m=min(h)
        best=[x for x in minimizers if x[0]==m]
        assert len(best)==1
        unique_d2_zero=[j+1 for j in range(N) if j not in best[0][2]]
assert total==56631
assert unique_d2_zero==EXPECTED_UNIQUE_D2_ZERO
hierarchy=tuple(min(EXPECTED_HISTS[r]) for r in range(1,K+1))
assert hierarchy==(12,16,19,21,23,24)
print('rank=6 gram_det=1')
print('weight_distribution='+repr(dict(sorted(wd.items()))))
print('hierarchy='+repr(hierarchy))
print('subspaces_checked=56631')
print('unique_d2_zero_coordinates='+repr(unique_d2_zero))
print('dual_weight_3_supports='+repr(sorted(dual_triples)))
print('VERIFY_OK')
