"""Independent finite-rank and simulation checks for the two-stack sketch theorem.
Scientific definitions only; no external services required.
"""
from collections import defaultdict, Counter
from itertools import product
from math import exp, log, factorial
from random import Random
import numpy as np


def predicted_nullity(r, edges):
    # Each edge: (left location, right location, sign in {+1,-1}).
    adj = [[] for _ in range(2*r)]
    for u, v, s in edges:
        adj[u].append((r+v, -s)); adj[r+v].append((u, -s))
    mark = [0]*(2*r); total = 0
    for src in range(2*r):
        if mark[src]: continue
        mark[src]=1; stack=[src]; nv=0; degrees=0; consistent=True
        while stack:
            u=stack.pop();nv+=1;degrees+=len(adj[u])
            for v,rel in adj[u]:
                expect=mark[u]*rel
                if mark[v]==0:
                    mark[v]=expect;stack.append(v)
                elif mark[v]!=expect: consistent=False
        e=degrees//2
        if e:
            total+=e-nv+int(consistent)
    return total


def matrix_nullity(r, edges):
    m=len(edges); A=np.zeros((2*r,m), dtype=np.float64)
    for j,(u,v,s) in enumerate(edges):
        A[u,j]=1.;A[r+v,j]=float(s)
    return m-int(np.linalg.matrix_rank(A, tol=1e-9))


def run():
    cases=0
    for r,k in [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(2,4),(3,2)]:
        atoms=[(u,v,s) for u in range(r) for v in range(r) for s in (-1,1)]
        for edges in product(atoms,repeat=k):
            a=predicted_nullity(r,edges);b=matrix_nullity(r,edges)
            assert a==b,(r,k,edges,a,b)
            cases+=1
    assert cases>5000
    # Confirm exact 2-edge rank-deficiency probability by complete enumeration.
    for r in range(1,6):
        atoms=[(u,v,s) for u in range(r) for v in range(r) for s in (-1,1)]
        nbad=sum(predicted_nullity(r,(a,b))>0 for a in atoms for b in atoms)
        assert nbad*2*r*r==len(atoms)**2,(r,nbad)
    print('Exhaustive small-matrix cases:',cases)
    print('Exact two-column singularity law: 1/(2r^2), r=1..5 verified')
    rng=Random(1729)
    for c in [0.5, 0.8]:
        for rho in [-1.0, 0.0, 0.5, 1.0]:
            lam=-(log(1-c*c)+log(1-rho*rho*c*c))/4
            for r in [80, 240]:
                trials=2500; count=Counter();m=int(c*r)
                for _ in range(trials):
                    es=[(rng.randrange(r), rng.randrange(r), 1 if rng.random()<(1+rho)/2 else -1) for j in range(m)]
                    count[predicted_nullity(r,es)]+=1
                p0=count[0]/trials;avg=sum(k*v for k,v in count.items())/trials
                assert abs(p0-exp(-lam)) < .13,(c,r,rho,p0,exp(-lam))
                assert abs(avg-lam) < .17,(c,r,rho,avg,lam)
                print(f'c={c}, rho={rho}, r={r}, P(full)={p0:.3f}, target={exp(-lam):.3f}, mean={avg:.3f}, Poisson={lam:.3f}')
    print('PASS')
if __name__=='__main__':run()
