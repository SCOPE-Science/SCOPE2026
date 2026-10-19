#!/usr/bin/env python3
"""Finite reproducibility checks for an optimal Laplacian gap on pendant coronas.

Requires numpy, networkx and sympy. These checks supplement, not replace,
the mathematical proof. Run: python sunlet_transitive_check.py
"""
import math
import numpy as np
import networkx as nx
import sympy as sp

checked = 0

def assert_close(x, y, tol=5e-9):
    global checked
    if not math.isclose(float(x), float(y), rel_tol=tol, abs_tol=tol):
        raise AssertionError((x, y))
    checked += 1


def graphs():
    for n in range(3, 11):
        yield f'cycle_{n}', nx.cycle_graph(n)
    for n in range(2, 9):
        yield f'complete_{n}', nx.complete_graph(n)
    for d in range(2, 6):
        yield f'cube_{d}', nx.convert_node_labels_to_integers(nx.hypercube_graph(d))
    for n in range(2, 8):
        yield f'biclique_{n}', nx.convert_node_labels_to_integers(nx.complete_bipartite_graph(n,n))
    yield 'petersen', nx.petersen_graph()


def mats(G):
    G=nx.convert_node_labels_to_integers(G)
    n=G.number_of_nodes(); E=list(G.edges());m=len(E)
    inc=[]
    for i,j in E:
        v=np.zeros(n);v[i]=1;v[j]=-1;inc.append(v)
    return n,m,E,np.asarray(inc)


def theta_graph_spectrum(n,E,weights):
    L=np.zeros((2*n,2*n))
    for (i,j),w in zip(E,weights[:len(E)]):
        for u,v,sgn in ((i,i,1),(j,j,1),(i,j,-1),(j,i,-1)):
            L[u,v]+=sgn*w
    for i,weight in enumerate(weights[len(E):]):
        L[i,i]+=weight;L[n+i,n+i]+=weight
        L[i,n+i]-=weight;L[n+i,i]-=weight
    return np.linalg.eigvalsh(L)[1],L

rng=np.random.default_rng(132546)
for name,G in graphs():
    n,m,E,C=mats(G)
    L0=C.T@C
    eig=np.linalg.eigvalsh(L0)
    mu=eig[1]
    # All graph families have vertex and edge transitivity; verify projector
    P=np.zeros((n,n))
    U=np.linalg.eigh(L0)[1]
    rnk=int(np.sum(np.isclose(eig,mu,atol=1e-8)))
    for k in range(n):
        if abs(eig[k]-mu)<1e-8:
            P+=np.outer(U[:,k],U[:,k])
    assert_close(np.max(np.diag(P)),np.min(np.diag(P)),1e-7)
    ldg=np.einsum('ei,ij,ej->e',C,P,C)
    assert_close(np.max(ldg),np.min(ldg),1e-7)
    for t in (0.035,0.4,1,3,20):
        B=1.7+0.12*n
        rho=m*t/(n*mu)
        r=math.sqrt(rho)
        opt=B/(n*(1+2*r+2*r*r))
        a=opt*(2+1/r)/mu
        b=opt*(1+r)
        assert_close(m*t*a+n*b,B)
        gap,L=theta_graph_spectrum(n,E,np.r_[np.full(m,a),np.full(n,b)])
        assert_close(gap,opt,1e-8)
        assert_close(np.sum(L,axis=0).max(),0.0,1e-8)
        assert_close(np.linalg.eigvalsh(a*L0)[1],a*mu,1e-8)
        # Individual asymmetric assignments respect the exact upper bound
        for k in range(24):
            vec=rng.gamma(1.1,size=m+n)
            scale=B/(t*sum(vec[:m])+sum(vec[m:]))
            v=vec*scale
            alt_gap,_=theta_graph_spectrum(n,E,v)
            if alt_gap>opt+5e-8:
                raise AssertionError((name,t,alt_gap,opt))
            checked+=1
        # Small rank-one and pairwise directional perturbations
        for k in range(4):
            vec=np.r_[np.full(m,a),np.full(n,b)]
            j=int(rng.integers(0,m+n)); l=int(rng.integers(0,m+n))
            if j==l: continue
            costs=np.r_[np.full(m,t),np.ones(n)]
            eps=min(vec[j],vec[l])*0.03
            vec[j]+=eps
            vec[l]-=eps*costs[j]/costs[l]
            if vec[l]<0: continue
            alt_gap,_=theta_graph_spectrum(n,E,vec)
            if alt_gap>opt+5e-8:
                raise AssertionError(('local',name,t,alt_gap,opt))
            checked+=1

# Exact rational confirmations of the spectral quadratic and prices.
for n,mu in [(2,2),(3,3),(4,2),(6,1)]:
    m=n if n>=3 else 1
    for r in (sp.Rational(1,3), sp.Rational(1,2),sp.Rational(1),sp.Rational(3,2),sp.Rational(3)):
        t=sp.Rational(n*mu,m)*r*r
        B=sp.Rational(13,7)
        lam=B/(n*(1+2*r+2*r*r))
        a=lam*(2+1/r)/mu
        b=lam*(1+r)
        assert sp.simplify(m*t*a+n*b-B)==0
        assert sp.simplify(lam*lam-(a*mu+2*b)*lam+a*mu*b)==0
        checked+=2

print('PASS',checked,'finite assertions across vertex-and-edge-transitive families')
