#!/usr/bin/env python3
"""Independent finite graph test of a representation-type classification for face algebras.
Requires numpy. The unrestricted theorem is proved mathematically, not by enumeration.
"""
import itertools
import random
import numpy as np


def components(n, edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    seen=set(); ret=[]
    for s in range(n):
        if s in seen:continue
        todo=[s];seen.add(s);comp=[]
        while todo:
            v=todo.pop();comp.append(v)
            for w in adj[v]:
                if w not in seen: seen.add(w);todo.append(w)
        ret.append(comp)
    return ret


def is_acyclic(n, edges):
    out=[[] for _ in range(n)]; degree=[0]*n
    for u,v in edges:out[u].append(v);degree[v]+=1
    todo=[v for v in range(n) if degree[v]==0];count=0
    while todo:
        v=todo.pop();count+=1
        for w in out[v]:
            degree[w]-=1
            if degree[w]==0:todo.append(w)
    return count==n


def expected(n, edges):
    ins=[0]*n;outs=[0]*n
    for u,v in edges:outs[u]+=1;ins[v]+=1
    fork=0
    for comp in components(n,edges):
        if all(ins[v]<=1 and outs[v]<=1 for v in comp):continue
        if len(comp)==3 and sum(ins[v] for v in comp)==2 and (
            max(ins[v] for v in comp)==2 or max(outs[v] for v in comp)==2
        ):
            fork+=1;continue
        return 'wild'
    return 'tame' if fork else 'finite'


def actual(n, edges):
    # Symmetric Cartan matrix 2I - adjacency of the Kronecker-square quiver.
    A=np.zeros((n*n,n*n),dtype=float)
    for (u,v),(x,y) in itertools.product(edges,repeat=2):
        i=u*n+x; j=v*n+y
        A[i,j]+=1;A[j,i]+=1
    mineigen=float(np.linalg.eigvalsh(2*np.eye(n*n)-A)[0])
    if mineigen < -1.e-7:return 'wild'
    if mineigen < 1.e-7:return 'tame'
    return 'finite'


def run():
    tested=0
    for n in range(1,5):
        pairs=list(itertools.combinations(range(n),2))
        for options in itertools.product([0,1,-1],repeat=len(pairs)):
            edges=[(a,b) if x==1 else (b,a) for (a,b),x in zip(pairs,options) if x]
            if not is_acyclic(n,edges):continue
            pred,got=expected(n,edges),actual(n,edges)
            assert pred==got,(n,edges,pred,got)
            tested+=1
    rng=random.Random(716203)
    for n in [5,6]:
        for _ in range(140):
            perm=list(range(n));rng.shuffle(perm)
            edges=[(perm[i],perm[j]) for i in range(n) for j in range(i+1,n) if rng.random()<0.34]
            pred,got=expected(n,edges),actual(n,edges)
            assert pred==got,(n,edges,pred,got)
            tested+=1
    # Distinct oriented 3-vertex forks: same orientation gives affine D4,
    # opposite gives affine A3, independently of any other components.
    forks={'+':[(0,1),(0,2)],'-':[(1,0),(2,0)]}
    for x,y in itertools.product('+-',repeat=2):
        edges=forks[x]+[(u+3,v+3) for u,v in forks[y]]
        assert actual(6,edges)=='tame'
        assert expected(6,edges)=='tame'
        tested+=1
    # Separately audit the two affine shapes in the four ordered fork products.
    for x,y in itertools.product('+-',repeat=2):
        A=forks[x]; B=forks[y]
        edges=[(u*3+r,v*3+s) for u,v in A for r,s in B]
        cs=components(9,edges)
        large=[cc for cc in cs if len(cc)>1]
        assert len(large)==1 and len(large[0])==(5 if x==y else 4)
        assert len(edges)==4
    # Multi-arrow boundary: a doubled arrow creates four arrows in the square.
    assert expected(2,[(0,1),(0,1)])=='wild'
    assert actual(2,[(0,1),(0,1)])=='wild'
    tested+=1
    print(f'VERIFY_OK {tested} acyclic quivers; Cartan inertia, four affine fork products and parallel-arrow boundary')

if __name__=='__main__':run()
