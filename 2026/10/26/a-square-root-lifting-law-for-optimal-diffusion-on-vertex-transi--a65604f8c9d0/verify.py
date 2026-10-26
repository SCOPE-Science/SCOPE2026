#!/usr/bin/env python3
"""Standalone reproducibility checks for a weighted corona spectral-budget identity.

Requires Python 3, sympy, numpy and networkx. Numerical sampling is supplementary
and is not a proof of the global optimization statement.
"""
import math
import random
import networkx as nx
import numpy as np
import sympy as sp


def symbolic_checks():
    N,M,g,c,d,q,lam = sp.symbols('N M g c d q lam', positive=True)
    z = sp.symbols('z', positive=True)
    # z^2 = M*c/(N*g*d); all symbolic formulae can be represented
    # rationally in z using M*c=N*g*d*z*z.
    x = lam/g*(q+1+q/z)
    y = lam*(1+z)
    budget = (M*c*x + N*q*d*y).subs(M*c,N*g*d*z*z)
    den = (N*q*d + M*c*(q+1)/g + 2*q*sp.sqrt(M*N*c*d/g))
    rational_den = N*d*(q + (q+1)*z*z + 2*q*z)
    assert sp.simplify(budget-lam*rational_den)==0
    poly=sp.expand(lam*lam-(g*x+(q+1)*y)*lam+g*x*y)
    assert sp.simplify(poly)==0
    # Cost minimization: C/lambda=A*(q+1+q/(u-1))+D*u.
    A,D,u=sp.symbols('A D u', positive=True)
    cost=A*(q+1+q/(u-1))+D*u
    assert sp.simplify(sp.diff(cost,u,2)-2*A*q/(u-1)**3)==0
    assert sp.simplify(sp.diff(cost,u).subs(u,1+sp.sqrt(A*q/D)))==0
    print('SYMBOLIC budget, characteristic polynomial, convexity: PASS')



def symbolic_lifting_checks():
    beta, N, d, q, r, z = sp.symbols('beta N d q r z', positive=True)
    # Encode z = sqrt(beta*N*d), with beta*N*d = z*z.
    a = r*(q+1+q*z)
    y = r*(1+1/z)
    W=a/beta
    total=sp.expand(W+N*q*d*y)
    expected=r*((q+1)/beta+N*q*d+2*q*sp.sqrt(N*d/beta))
    total_rational=sp.expand(total.subs(N*d,z*z/beta))
    expected_rational=r/beta*(q+1+q*z*z+2*q*z)
    assert sp.simplify(total_rational-expected_rational)==0
    assert sp.simplify(r*r-(a+(q+1)*y)*r+a*y)==0
    u=sp.symbols('u',positive=True)
    target=(q+1)/beta+q/(beta*(u-1))+N*q*d*u
    assert sp.simplify(sp.diff(target,u).subs(u,1+1/sp.sqrt(beta*N*d)))==0
    assert sp.simplify(sp.diff(target,u,2)-2*q/(beta*(u-1)**3))==0
    print('GENERAL LIFTING SYMBOLIC IDENTITIES: PASS')

def build_laplacian(core, q, x, y):
    n=len(core)
    nodes=list(core.nodes())
    lab={v:i for i,v in enumerate(nodes)}
    L=np.zeros((n*(q+1),n*(q+1)))
    for u,v in core.edges():
        i,j=lab[u],lab[v]
        L[i,i]+=x;L[j,j]+=x;L[i,j]-=x;L[j,i]-=x
    for i in range(n):
        for z in range(q):
            j=n+i*q+z
            L[i,i]+=y;L[j,j]+=y;L[i,j]-=y;L[j,i]-=y
    return L


def test_family():
    cases=[('triangle', nx.complete_graph(3)),
           ('complete5',nx.complete_graph(5)),
           ('cycle4',nx.cycle_graph(4)),
           ('cycle7',nx.cycle_graph(7)),
           ('cube3',nx.hypercube_graph(3)),
           ('petersen',nx.petersen_graph()),
           ('biclique3',nx.complete_bipartite_graph(3,3)),
           ('octahedron',nx.octahedral_graph())]
    rng=random.Random(79304)
    tests=0
    random_budgets=0
    for name,G in cases:
        n=G.number_of_nodes();m=G.number_of_edges()
        L0=nx.laplacian_matrix(G).toarray().astype(float)
        gap=float(np.linalg.eigvalsh(L0)[1])
        assert gap>0
        for q in (1,2,4):
          for (cost_core,cost_leaf,B) in ((1.0,1.0,1.0), (2.0,0.3,11.0),(0.25,4.0,3.5)):
            D=n*q*cost_leaf + m*cost_core*(q+1)/gap + 2*q*math.sqrt(m*n*cost_core*cost_leaf/gap)
            lam=B/D
            x=lam/gap*(q+1+q*math.sqrt(n*gap*cost_leaf/(m*cost_core)))
            y=lam*(1+math.sqrt(m*cost_core/(n*gap*cost_leaf)))
            assert abs(m*cost_core*x+n*q*cost_leaf*y-B)<=1e-10*max(1,B)
            L=build_laplacian(G,q,x,y)
            eig=np.linalg.eigvalsh(L)
            assert abs(eig[1]-lam)<=1e-8*max(1,lam), (name,q,eig[1],lam)
            # All positive base and private-leaf edges.
            assert x>0 and y>0
            tests+=1
            if n*(q+1)<=28:
              for _ in range(15):
                raw=[rng.uniform(.01,1) for _ in range(m+n*q)]
                scale=B/(cost_core*sum(raw[:m])+cost_leaf*sum(raw[m:]))
                Lr=np.zeros_like(L)
                nodes=list(G.nodes());lab={v:i for i,v in enumerate(nodes)}
                for a,(u,v) in enumerate(G.edges()):
                    i,j=lab[u],lab[v];w=raw[a]*scale
                    Lr[i,i]+=w;Lr[j,j]+=w;Lr[i,j]-=w;Lr[j,i]-=w
                for i in range(n):
                  for k in range(q):
                    j=n+i*q+k;w=raw[m+i*q+k]*scale
                    Lr[i,i]+=w;Lr[j,j]+=w;Lr[i,j]-=w;Lr[j,i]-=w
                random_gap=np.linalg.eigvalsh(Lr)[1]
                assert random_gap <=lam+1e-8*max(1,lam), (name,q,random_gap,lam)
                random_budgets+=1
    print('FULL SPECTRA:',tests,'PASS')
    print('RANDOM ASYMMETRIC ALLOCATIONS:',random_budgets,'PASS (non-exhaustive)')

if __name__=='__main__':
    symbolic_checks()
    symbolic_lifting_checks()
    test_family()


def test_non_edge_transitive_prisms():
    # Cartesian prisms are vertex-transitive but their base edges form two orbits
    # for s>=5. The triangle prism is also vertex transitive and non-edge transitive.
    checked=0
    for s in (3,5,7):
        N=2*s
        alpha=4*math.sin(math.pi/s)**2
        for (c1,c2,d,B) in ((1.,2.,.7,5.),(2.,.3,1.5,12.)):
            W=2*s*c1/alpha+s*c2/2
            beta=1/W
            for q in (1,2,3):
                D=(q+1)/beta+N*q*d+2*q*math.sqrt(N*d/beta)
                lam=B/D
                core_gap=lam*(q+1+q*math.sqrt(beta*N*d))
                a=core_gap/alpha
                b=core_gap/2
                y=lam*(1+1/math.sqrt(beta*N*d))
                G=nx.cartesian_product(nx.cycle_graph(s),nx.path_graph(2))
                nodes=list(G.nodes());lab={v:i for i,v in enumerate(nodes)}
                L=np.zeros((N*(q+1),N*(q+1)))
                total_core=0.0
                for u,v in G.edges():
                    w=a if u[1]==v[1] else b
                    c=c1 if u[1]==v[1] else c2
                    total_core+=c*w
                    i,j=lab[u],lab[v]
                    L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
                for i in range(N):
                  for k in range(q):
                    j=N+i*q+k
                    L[i,i]+=y;L[j,j]+=y;L[i,j]-=y;L[j,i]-=y
                assert abs(total_core+N*q*d*y-B)<1e-8
                spec=np.linalg.eigvalsh(L)
                assert abs(spec[1]-lam)<1e-8,(s,q,lam,spec[1])
                checked+=1
    print('PRISM TWO-ORBIT COST CASES:',checked,'PASS')

if __name__=='__main__':
    test_non_edge_transitive_prisms()
