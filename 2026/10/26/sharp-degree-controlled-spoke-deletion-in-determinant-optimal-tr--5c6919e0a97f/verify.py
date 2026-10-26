"""Numerical and rational reconstruction checks for tree-cone D-optimal allocations.

Usage: python verify.py
Dependencies: Python 3, numpy, sympy (for exact rational tests).
"""
from fractions import Fraction
from itertools import combinations
import math
import random
import numpy as np
import sympy as sp


def tree_from_prufer(seq):
    n = len(seq) + 2
    degree = [1] * n
    for x in seq:
        degree[x] += 1
    result = []
    for x in seq:
        leaf = next(i for i in range(n) if degree[i] == 1)
        result.append((leaf, x))
        degree[leaf] -= 1
        degree[x] -= 1
    u,v = (i for i in range(n) if degree[i] == 1)
    return result + [(u, v)]


def distances(n, edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v);adj[v].append(u)
    d=np.zeros((n,n),dtype=int)
    for root in range(n):
        q=[root]
        seen={root}
        for u in q:
            for v in adj[u]:
                if v not in seen:
                    seen.add(v);d[root,v]=d[root,u]+1;q.append(v)
        assert len(q)==n
    return d


def candidate(n, edges, t, B=1.):
    deg=np.zeros(n,dtype=int)
    for u,v in edges:deg[u]+=1;deg[v]+=1
    if t>=2.:
        return np.ones(n)*B/n, np.zeros(n-1),0.
    rho=1-t/2.
    spokes=(B/n)*(1-(deg-1)*rho)/(1+rho)
    rims=np.ones(n-1)*(B/n)*rho/(1-rho*rho)
    return spokes,rims,rho


def laplacian_grounded(n,edges,spokes,rims):
    M=np.diag(spokes.copy())
    for (u,v),w in zip(edges,rims):
        M[u,u]+=w;M[v,v]+=w;M[u,v]-=w;M[v,u]-=w
    return M


def checks(n,edges,t,B=1.,tol=4e-8):
    s,x,rho=candidate(n,edges,t,B)
    assert s.min()>=-tol
    assert x.min()>=-tol
    assert abs(s.sum()+t*x.sum()-B)<tol
    M=laplacian_grounded(n,edges,s,x)
    C=np.power(rho,distances(n,edges)) if rho>0 else np.eye(n)
    cov=np.linalg.inv(M)
    assert np.max(np.abs(cov-(n/B)*C))<tol
    d=np.linalg.det(M)
    assert abs(d-((B/n)**n)/(1-rho*rho)**(n-1))<tol*max(1,d)
    assert np.linalg.eigvalsh(M).min()>0
    gsp=np.diag(cov)
    gedge=np.array([cov[u,u]+cov[v,v]-2*cov[u,v] for u,v in edges])
    assert np.max(np.abs(gsp-n/B))<tol
    assert np.max(np.abs(gedge-t*n/B))<tol if t<=2 else np.all(gedge<=t*n/B+tol)
    return d


def rational_exact(n,edges,t):
    tt=sp.Rational(t.numerator,t.denominator);B=sp.Integer(1)
    deg=[0]*n
    for u,v in edges:deg[u]+=1;deg[v]+=1
    rho=max(sp.Rational(0),1-tt/2)
    if tt>=2:
        spokes=[sp.Rational(1,n)]*n
        rims=[sp.Integer(0)]*(n-1)
    else:
        spokes=[(1-(d-1)*rho)/(n*(1+rho)) for d in deg]
        rims=[rho/(n*(1-rho*rho))]*(n-1)
    assert min(spokes)>=0
    M=sp.diag(*spokes)
    for (u,v),w in zip(edges,rims):
        M[u,u]+=w;M[v,v]+=w;M[u,v]-=w;M[v,u]-=w
    C=sp.Matrix([[rho**int(a) for a in row] for row in distances(n,edges)])
    assert M*C==sp.eye(n)/n
    assert M.det()==sp.Rational(1,n)**n/(1-rho*rho)**(n-1)
    assert sum(spokes)+tt*sum(rims)==1
    return True


def random_competitor(n,edges,t,B,rng):
    w=np.array([rng.expovariate(1.) for _ in range(2*n-1)])
    w=w*(B/(w[:n].sum()+t*w[n:].sum()))
    return laplacian_grounded(n,edges,w[:n],w[n:])


def main():
    rng=random.Random(20261024)
    num=0;exact=0;competitors=0;threshold=0
    ts=[0.11,0.25,0.5,0.75,1.,1.25,1.5,1.8,1.99,2.,2.5,4.]
    trees=[]
    for n in range(2,11):
        trees.append((n,[(i,i+1) for i in range(n-1)]))
        if n>=3:trees.append((n,[(0,j) for j in range(1,n)]))
        for _ in range(8):
            trees.append((n,tree_from_prufer([rng.randrange(n) for _ in range(n-2)])))
    for n,edges in trees:
        degree=[0]*n
        for u,v in edges:degree[u]+=1;degree[v]+=1
        cutoff=0 if max(degree)<=2 else 2*(max(degree)-2)/(max(degree)-1)
        for t in ts:
            if t<cutoff-1e-10:
                s,_,_=candidate(n,edges,t)
                assert min(s)<0
                threshold+=1
                continue
            B=float(n+3)/7
            d=checks(n,edges,t,B)
            num+=1
            for _ in range(4):
                Z=random_competitor(n,edges,t,B,rng)
                assert np.linalg.det(Z)<=d*(1+3e-8)
                competitors+=1
    for n,edges,tsub in [
        (3,[(0,1),(1,2)],[Fraction(1,2),Fraction(1),Fraction(2)]),
        (5,[(0,1),(1,2),(2,3),(3,4)],[Fraction(1,3),Fraction(3,2)]),
        (5,[(0,1),(0,2),(0,3),(0,4)],[Fraction(3,2),Fraction(2)]),
        (6,[(0,1),(0,2),(0,3),(3,4),(3,5)],[Fraction(5,3),Fraction(7,3)])
    ]:
        for t in tsub:
            assert rational_exact(n,edges,t)
            exact+=1
    print(f'PASS: {num} candidate covariance/cost/KKT/determinant checks; {competitors} numerical feasible competitors; {exact} exact-rational matrix identities; {threshold} below-threshold candidate infeasibility checks.')
    print('Finite computations corroborate the analytic tree-covariance and convexity proof; they do not establish the theorem alone.')

if __name__=='__main__':main()
