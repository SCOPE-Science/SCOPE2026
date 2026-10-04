#!/usr/bin/env python3
from itertools import combinations

def crown(n):
    # vertices 0..n-1 are a_i, n..2n-1 are b_i
    edges=[(i,n+j) for i in range(n) for j in range(n) if i!=j]
    adj=[set() for _ in range(2*n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    return edges,adj

def all_pairs_dist(adj):
    N=len(adj); D=[]
    for s in range(N):
        d=[-1]*N; d[s]=0; q=[s]
        for u in q:
            for v in adj[u]:
                if d[v]<0:
                    d[v]=d[u]+1; q.append(v)
        assert all(x>=0 for x in d)
        D.append(d)
    return D

def resolves(S,edges,D):
    seen=set()
    for u,v in edges:
        code=tuple(min(D[s][u],D[s][v]) for s in S)
        if code in seen: return False
        seen.add(code)
    return True

def predicted_basis(S,n):
    if len(S)!=n-1: return False
    hit=[]
    for i in range(n):
        c=(i in S)+((n+i) in S)
        hit.append(c)
    return hit.count(0)==1 and hit.count(1)==n-1 and hit.count(2)==0

subset_checks=basis_checks=distance_formula_checks=0
for n in range(3,9):
    edges,adj=crown(n); D=all_pairs_dist(adj)
    # Check closed distance formula to every edge.
    for i,j in [(i,j) for i in range(n) for j in range(n) if i!=j]:
        e=(i,n+j)
        for k in range(n):
            da=min(D[k][e[0]],D[k][e[1]])
            db=min(D[n+k][e[0]],D[n+k][e[1]])
            assert da==(0 if k==i else 2 if k==j else 1)
            assert db==(0 if k==j else 2 if k==i else 1)
            distance_formula_checks+=2
    # No resolving set below n-1; all size n-1 sets match claimed classification.
    for r in range(n-1):
        for S in combinations(range(2*n),r):
            assert not resolves(S,edges,D)
            subset_checks+=1
    actual=[]
    for S in combinations(range(2*n),n-1):
        ok=resolves(S,edges,D)
        pred=predicted_basis(S,n)
        assert ok==pred
        subset_checks+=1
        if ok: actual.append(S)
    assert len(actual)==n*(2**(n-1))
    basis_checks+=len(actual)
print(f"VERIFY_OK n_range=3..8 subset_checks={subset_checks} basis_checks={basis_checks} distance_formula_checks={distance_formula_checks} max_order=16")
