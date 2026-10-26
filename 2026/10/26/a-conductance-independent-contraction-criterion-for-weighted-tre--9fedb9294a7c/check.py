"""Reproducible finite diagnostics for the weighted-tree BV heat criterion.

The algebraic proof is in RESULT.md; this script is not an infinite certificate.
Only the Python standard library is needed.
"""
from fractions import Fraction as F
from itertools import product
from collections import deque
from random import Random


def tree_from_prufer(seq):
    n = len(seq) + 2
    degrees = [1]*n
    for u in seq: degrees[u] += 1
    edges=[]
    for u in seq:
        v=next(v for v in range(n) if degrees[v]==1)
        edges.append((u,v)); degrees[v]-=1; degrees[u]-=1
    a,b=[v for v in range(n) if degrees[v]==1]
    edges.append((a,b))
    return edges


def is_tree_path_or_claw(n,edges):
    deg=[0]*n
    for u,v in edges: deg[u]+=1;deg[v]+=1
    return max(deg)<=2 or (n==4 and sorted(deg)==[1,1,1,3])


def criterion(edges,n,masses,w):
    degree_w=[F(0)]*n
    for (u,v),we in zip(edges,w):degree_w[u]+=we;degree_w[v]+=we
    return [w[e]*(1/masses[u]+1/masses[v]) - ((degree_w[u]-w[e])/masses[u] +(degree_w[v]-w[e])/masses[v]) for e,(u,v) in enumerate(edges)]


def build_q(edges,n,masses,c,w):
    m=len(edges); Q=[[F(0) for _ in range(m)] for _ in range(m)]
    for e,(u,v) in enumerate(edges):
        Q[e][e]=-c[e]*(1/masses[u]+1/masses[v])
        for f,(a,b) in enumerate(edges):
            if e==f:continue
            common=set((u,v)).intersection((a,b))
            if common:
                node=next(iter(common))
                se=(1 if node==v else -1)
                sf=(1 if node==b else -1)
                Q[f][e]=-F(se*sf)*c[e]*w[f]/(w[e]*masses[node])
    return Q


def lognorm(q):
    return max(q[j][j]+sum(abs(q[i][j]) for i in range(len(q)) if i!=j) for j in range(len(q)))


def mm(a,b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def mat_exp_approx(q,t,order=8):
    n=len(q)
    eye=[[float(i==j) for j in range(n)] for i in range(n)]
    a=[[float(q[i][j])*float(t) for j in range(n)] for i in range(n)]
    cur=[r[:] for r in eye]; out=[r[:] for r in eye]
    for k in range(1,order+1):
        cur=mm(cur,a)
        for i in range(n):
            for j in range(n):
                cur[i][j]/=k; out[i][j]+=cur[i][j]
    return out


def colnorm(a):
    return max(sum(abs(a[i][j]) for i in range(len(a))) for j in range(len(a)))


def verify():
    enumerated=0; weighted=0; rng=Random(223311)
    # Every labeled tree through seven vertices, including the exceptional 3-star.
    for n in range(2,8):
        for seq in product(range(n),repeat=max(0,n-2)):
            ed=tree_from_prufer(seq)
            unit=[F(1)]*(n-1)
            slopes=criterion(ed,n,[F(1)]*n,unit)
            good=all(s>=0 for s in slopes)
            if good!=is_tree_path_or_claw(n,ed):
                raise AssertionError(('classification',n,seq,ed,slopes))
            enumerated+=1
    # Rational random weights and two independent slope formulas; small-time semigroup.
    for trial in range(150):
        n=rng.randrange(2,9)
        ed=tree_from_prufer([rng.randrange(n) for _ in range(n-2)])
        masses=[F(rng.randrange(1,6),rng.randrange(1,6)) for _ in range(n)]
        c=[F(rng.randrange(1,6),rng.randrange(1,6)) for _ in ed]
        w=[F(rng.randrange(1,6),rng.randrange(1,6)) for _ in ed]
        q=build_q(ed,n,masses,c,w)
        local=criterion(ed,n,masses,w)
        for e in range(len(ed)):
            slope=q[e][e]+sum(abs(q[f][e]) for f in range(len(ed)) if f!=e)
            if slope !=-c[e]/w[e]*local[e]:
                raise AssertionError(('formula',trial,e,slope,local[e]))
        mu=float(lognorm(q));t=1e-7
        observed=(colnorm(mat_exp_approx(q,t))-1)/t
        if abs(observed-mu)>0.003:
            raise AssertionError(('asymptotic',trial,observed,mu))
        weighted+=1
    print('PASS: exactly',enumerated,'labeled-tree classifications;')
    print('PASS:',weighted,'weighted rational generator identities and small-time tests.')
    print('Finite checks are diagnostics, not a proof of the universal theorem.')

if __name__=='__main__': verify()
