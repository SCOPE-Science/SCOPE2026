"""Reproducible checks: fastest symmetric mixing on H Cartesian K_s.

Run: python fmmc_clique_layers_verify.py
Requires numpy, scipy, networkx, sympy. No network access.
"""
import itertools
import random
import numpy as np
import networkx as nx
from scipy.optimize import linprog
import sympy as sp

rng=random.Random(2607)
checks={'matrix_spectra':0,'linear_programs':0,'asymmetric_tests':0,
        'cycle_parity_tests':0,'johnson_spectra':0,'exact_rational':0}

def analyze(H,s):
    H=nx.convert_node_labels_to_integers(H)
    n=len(H);d=H.degree(0)
    assert nx.is_connected(H) and all(deg==d for _,deg in H.degree())
    L=nx.laplacian_matrix(H,nodelist=list(range(n))).toarray().astype(float)
    e=np.linalg.eigvalsh(L)
    alpha,beta=e[1],e[-1]
    M=max(beta+2*alpha,2*d+2*alpha*(s-1)/s)
    x=2/M;y=2*alpha/(s*M);mu=1-2*alpha/M
    assert x>0 and y>0 and d*x+(s-1)*y<=1+1e-10
    r=linprog([0,0,1],A_ub=[[-alpha,0,-1],[0,-s,-1],[beta,s,-1],[d,s-1,0]],
              b_ub=[-1,-1,1,1],bounds=[(0,None),(0,None),(0,None)],method='highs')
    assert r.success and np.allclose(r.x,[x,y,mu],atol=2e-8)
    checks['linear_programs']+=1
    if n*s<=80:
        K=np.full((s,s),-1.);np.fill_diagonal(K,s-1.)
        LH=np.kron(L,np.eye(s)); LK=np.kron(np.eye(n),K)
        P=np.eye(n*s)-x*LH-y*LK
        assert np.max(np.abs(P.sum(axis=1)-1))<1e-9
        assert np.min(P)>-1e-10
        ew=np.linalg.eigvalsh(P)
        assert abs(ew[-1]-1)<1e-9 and abs(np.max(abs(ew[:-1]))-mu)<2e-8
        checks['matrix_spectra']+=1
        # A second family of non-orbit-constant feasible matrices.
        if n*s<=42:
            edges=[]
            for u,v in H.edges():
                for j in range(s):edges.append((s*u+j,s*v+j))
            for u in range(n):
                for a in range(s):
                    for b in range(a):edges.append((s*u+a,s*u+b))
            for k in range(8):
                weights=[rng.random()+0.1 for _ in edges]
                outgoing=np.zeros(n*s)
                for (u,v),w in zip(edges,weights):outgoing[u]+=w;outgoing[v]+=w
                bound=outgoing.max()*1.2
                R=np.eye(n*s)
                for (u,v),w in zip(edges,weights):
                    w/=bound
                    R[u,u]-=w;R[v,v]-=w;R[u,v]+=w;R[v,u]+=w
                eps=rng.uniform(0.1,0.9)
                Q=eps*R+(1-eps)*P
                eq=np.linalg.eigvalsh(Q)
                assert np.max(abs(eq[:-1])) >= mu-2e-8
                checks['asymmetric_tests']+=1
    return alpha,beta,d,x,y,mu

for n in range(3,16):
    for s in (2,3,5,7,8,9,12):
        a,b,d,x,y,mu=analyze(nx.cycle_graph(n),s)
        h=1-d*x-(s-1)*y
        if n%2==0:assert h>1e-10
        elif n==3:
            assert (h>1e-10)==(s<6)
            if s==2 or s==3 or s==5 or s==7 or s==8 or s==9 or s==12:pass
        else:assert (h>1e-10)==(s<=7)
        checks['cycle_parity_tests']+=1

for n in range(4,9):
    combinations=list(itertools.combinations(range(n),2))
    J=nx.Graph();J.add_nodes_from(range(len(combinations)))
    for i,A in enumerate(combinations):
        for j,B in enumerate(combinations[:i]):
            if len(set(A)&set(B))==1:J.add_edge(i,j)
    for s in (2,3,4,6):
        a,b,d,x,y,mu=analyze(J,s)
        assert abs(a-n)<1e-8 and abs(b-(2*n-2))<1e-8
        assert d==2*(n-2)
        checks['johnson_spectra']+=1
for s in (2,3,4,5,7):
    analyze(nx.petersen_graph(),s)
    analyze(nx.complete_graph(5),s)
    analyze(nx.complete_bipartite_graph(3,3),s)

for n in range(4,14):
    a=sp.Integer(n); b=sp.Integer(2*n-2); d=sp.Integer(2*n-4)
    for s in range(2,11):
        ss=sp.Integer(s)
        M=sp.Max(b+2*a,2*d+2*a*(ss-1)/ss)
        x=2/M;y=2*a/(ss*M);mu=1-2*a/M
        assert d*x+(ss-1)*y<=1
        assert 1-a*x==mu and 1-ss*y==mu
        assert b*x+ss*y-1<=mu
        checks['exact_rational']+=1
print('PASS',checks)
