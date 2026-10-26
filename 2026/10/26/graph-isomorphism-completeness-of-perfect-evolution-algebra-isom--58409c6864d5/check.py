#!/usr/bin/env python3
"""Finite tests of algebra isomorphism versus cyclic-fiber relational isomorphism.

Uses prime fields and independent exhaustive permutations. No external dependencies.
"""
import itertools
import random
from collections import Counter


def det_nonzero(M, q):
    X=[list(row) for row in M]
    n=len(X)
    for i in range(n):
        pivot=next((r for r in range(i,n) if X[r][i]%q),None)
        if pivot is None: return False
        X[i],X[pivot]=X[pivot],X[i]
        inv=pow(X[i][i],-1,q)
        for r in range(i+1,n):
            a=X[r][i]*inv%q
            for s in range(i,n): X[r][s]=(X[r][s]-a*X[i][s])%q
    return True


def algebra_iso(A,B,q):
    n=len(A)
    for pi in itertools.permutations(range(n)):
        for cs in itertools.product(range(1,q),repeat=n):
            if all((A[i][j]*cs[j]-cs[i]*cs[i]*B[pi[i]][pi[j]])%q==0
                   for i in range(n) for j in range(n)):
                return True
    return False


def primitive(q):
    return next(g for g in range(1,q) if len({pow(g,k,q) for k in range(q-1)})==q-1)


def relations(M,q):
    n=len(M)
    g=primitive(q)
    nodes=[(i,t) for i in range(n) for t in range(1,q)]
    r1={((i,t),(i,g*t%q)) for i,t in nodes}
    r2={((i,t),(j,M[i][j]*t*t%q)) for i,t in nodes
        for j in range(n) if M[i][j]%q}
    return nodes,(r1,r2)


def graph_iso(A,B,q):
    vA,(s1,s2)=relations(A,q)
    vB,(t1,t2)=relations(B,q)
    m=len(vA)
    ai={v:i for i,v in enumerate(vA)}
    bi={v:i for i,v in enumerate(vB)}
    rA=[{(ai[a],ai[b]) for a,b in ss} for ss in (s1,s2)]
    rB=[{(bi[a],bi[b]) for a,b in ss} for ss in (t1,t2)]
    for perm in itertools.permutations(range(m)):
        if all({(perm[a],perm[b]) for a,b in ss}==tt
               for ss,tt in zip(rA,rB)):
            return True
    return False


def enumerate_GL(n,q):
    for vals in itertools.product(range(q),repeat=n*n):
        mat=tuple(tuple(vals[n*i:n*i+n]) for i in range(n))
        if det_nonzero(mat,q): yield mat


def check_case(n,q,max_pairs=None):
    mats=list(enumerate_GL(n,q))
    rng=random.Random(20261018+n*10+q)
    pairs=list(itertools.product(range(len(mats)),repeat=2))
    if max_pairs is not None and len(pairs)>max_pairs:
        pairs=rng.sample(pairs,max_pairs)
    yes=0
    for i,j in pairs:
        a=algebra_iso(mats[i],mats[j],q)
        b=graph_iso(mats[i],mats[j],q)
        assert a==b,(n,q,i,j,a,b)
        yes+=a
    print(f'q={q}, n={n}, matrices={len(mats)}, tested_pairs={len(pairs)}, isomorphic_pairs={yes}')


def incidence_matrix(n,edges,q):
    m=len(edges)
    size=n+m
    X=[[int(i==j) for j in range(size)] for i in range(size)]
    for k,(u,v) in enumerate(edges):
        X[u][n+k]=1
        X[v][n+k]=1
    assert det_nonzero(X,q)
    indeg=[sum(int(X[i][j]!=0) for i in range(size)) for j in range(size)]
    assert indeg[:n]==[1]*n and indeg[n:]==[3]*m
    return X


def check_incidence():
    for n in range(1,6):
        allpairs=list(itertools.combinations(range(n),2))
        for mask in range(1<<len(allpairs)):
            edges=[e for k,e in enumerate(allpairs) if mask>>k&1]
            for q in (2,3,5): incidence_matrix(n,edges,q)
        print(f'incidence encoding n={n}, simple_graphs={1<<len(allpairs)}')

if __name__=='__main__':
    check_case(2,2)
    check_case(2,3)
    check_case(3,2,max_pairs=1200)
    check_case(2,5,max_pairs=100)
    check_incidence()
    print('VERIFY_OK')
