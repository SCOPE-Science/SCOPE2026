#!/usr/bin/env python3
from itertools import combinations, product
from collections import deque, Counter
from math import comb

def vertices(d,k):
    out=[]
    for S in combinations(range(d),k):
        for signs in product((-1,1), repeat=k):
            v=[0]*d
            for i,s in zip(S,signs):
                v[i]=s
            out.append(tuple(v))
    return out

def neighbors(v):
    occ=[i for i,x in enumerate(v) if x]
    empty=[i for i,x in enumerate(v) if not x]
    for i in occ:
        for j in empty:
            for s in (-1,1):
                w=list(v)
                w[i]=0
                w[j]=s
                yield tuple(w)

def formula(u,v):
    k=sum(x!=0 for x in u)
    if u==v:
        return 0
    a=sum(x!=0 and x==y for x,y in zip(u,v))
    r=sum(x!=0 and y!=0 for x,y in zip(u,v))
    return k-a if r<k else k-a+1

def shell_formula(d,k,j):
    if j==0:
        return 1
    z=0
    if 1<=j<=k:
        z += comb(k,j)*sum(
            comb(j,c)*comb(d-k,c)*(2**c)
            for c in range(1,min(j,d-k)+1)
        )
    if 2<=j<=k+1:
        z += comb(k,j-1)
    return z

cases=0
ordered_pairs=0
for d in range(2,8):
    for k in range(1,d):
        V=vertices(d,k)
        assert len(V)==(2**k)*comb(d,k)
        index={v:i for i,v in enumerate(V)}
        A=[[] for _ in V]
        for i,v in enumerate(V):
            ns=list(neighbors(v))
            assert len(ns)==2*k*(d-k)
            A[i]=[index[w] for w in ns]
        first_shell=None
        maxdist=0
        for s,u in enumerate(V):
            D=[-1]*len(V)
            D[s]=0
            q=deque([s])
            while q:
                x=q.popleft()
                for y in A[x]:
                    if D[y]<0:
                        D[y]=D[x]+1
                        q.append(y)
            assert -1 not in D
            for t,v in enumerate(V):
                assert D[t]==formula(u,v), (d,k,u,v,D[t],formula(u,v))
            maxdist=max(maxdist,max(D))
            ordered_pairs += len(V)
            if s==0:
                first_shell=Counter(D)
        assert maxdist==k+1
        for j in range(k+2):
            assert first_shell[j]==shell_formula(d,k,j), (d,k,j,first_shell[j],shell_formula(d,k,j))
        assert sum(first_shell.values())==len(V)
        cases += 1
print(f"VERIFY_OK cube-cross-polytope metric cases={cases} ordered_pairs={ordered_pairs} max_d=7")
