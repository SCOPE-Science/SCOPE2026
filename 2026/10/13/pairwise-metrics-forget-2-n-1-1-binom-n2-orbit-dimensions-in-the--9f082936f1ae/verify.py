#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from math import comb


def cuts(n):
    # One representative of each nontrivial unordered split: nonempty U not containing n-1.
    if n <= 1:
        return []
    out=[]
    for mask in range(1, 1 << (n-1)):
        out.append(frozenset(i for i in range(n-1) if mask >> i & 1))
    return out


def edge_rows(n):
    return list(combinations(range(n),2))


def crosses(U,i,j):
    return (i in U) ^ (j in U)


def matrix(n):
    cs=cuts(n); es=edge_rows(n)
    return [[1 if crosses(U,i,j) else 0 for U in cs] for i,j in es],cs,es


def rank_q(A):
    if not A: return 0
    a=[[Fraction(x) for x in row] for row in A]
    r=0; cols=len(a[0])
    for c in range(cols):
        piv=next((i for i in range(r,len(a)) if a[i][c]),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        z=a[r][c]
        a[r]=[x/z for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                z=a[i][c]
                a[i]=[x-z*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a): break
    return r


def mul(A,v):
    return [sum(a*x for a,x in zip(row,v)) for row in A]


def semidiversity(n, weights):
    cs=cuts(n)
    def delta(A):
        A=set(A)
        return sum(w for U,w in zip(cs,weights)
                   if A & set(U) and A - set(U))
    return delta

checks=0
for n in range(1,9):
    A,cs,es=matrix(n)
    m=(1 << (n-1))-1 if n>=1 else 0
    q=comb(n,2)
    assert len(cs)==m
    checks+=1
    r=rank_q(A)
    assert r==q,(n,r,q)
    checks+=1
    assert m-r == (1 << (n-1))-1-comb(n,2)
    checks+=1
    if n>=3:
        # Every edge unit vector lies in the cut span via
        # 2 e_ij = c_{i}+c_{j}-c_{ij}; complements represent the same cut.
        idx={U:k for k,U in enumerate(cs)}
        def rep(S):
            S=set(S)
            if n-1 in S: S=set(range(n))-S
            return frozenset(S)
        for epos,(i,j) in enumerate(es):
            v=[0]*m
            for coeff,S in [(1,{i}),(1,{j}),(-1,{i,j})]:
                R=rep(S)
                if R: v[idx[R]] += coeff
            y=mul(A,v)
            target=[0]*q; target[epos]=2
            assert y==target,(n,(i,j),y,target)
            checks+=1

# Four-point hidden direction: singleton cuts versus 2+2 cuts.
n=4
A,cs,es=matrix(n)
idx={U:k for k,U in enumerate(cs)}
v=[0]*len(cs)
# singleton cuts {0},{1},{2},{3}; {3} is represented by complement {0,1,2}
for S in [{0},{1},{2},{0,1,2}]: v[idx[frozenset(S)]] += 1
# 2+2 cuts; choose the representatives not containing point 3
for S in [{0,1},{0,2},{1,2}]: v[idx[frozenset(S)]] -= 1
assert mul(A,v)==[0]*6
checks+=1
assert sum(v)==1  # every nontrivial cut crosses the full four-point set
checks+=1

base=[2]*len(cs)
w1=base
w2=[a+b for a,b in zip(base,v)]
assert min(w2)>0
checks+=1
D1=semidiversity(4,w1); D2=semidiversity(4,w2)
for i,j in es:
    assert D1({i,j})==D2({i,j})
    checks+=1
assert D2(set(range(4)))-D1(set(range(4)))==1
checks+=1
# Full subset values are not identical, so the L1 diversities are distinct.
assert any(D1(S)!=D2(S) for r in range(3,5) for S in combinations(range(4),r))
checks+=1

print(f'VERIFY_OK {checks} exact assertions')
