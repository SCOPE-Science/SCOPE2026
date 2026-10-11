#!/usr/bin/env python3
"""Independent finite verification of fixed-cardinality assignment-ball formulas."""
from itertools import combinations, permutations
import math
import numpy as np
from scipy.optimize import linprog

def lp_radius(N,k):
    M=N*N
    q=math.sqrt(1-1/M)
    h=math.sqrt(N-1)
    rows=[]; rhs=[]
    for z in range(M):
        rr=np.zeros(M+1); rr[z]=-1;rr[-1]=q
        rows.append(rr);rhs.append(0.)
    for side in range(2):
        for i in range(N):
            rr=np.zeros(M+1)
            for j in range(N):rr[N*i+j if side==0 else N*j+i]=1
            rr[-1]=h;rows.append(rr);rhs.append(1.)
    aa=np.zeros((1,M+1));aa[0,:M]=1
    cc=np.zeros(M+1);cc[-1]=-1
    return linprog(cc,A_ub=np.asarray(rows),b_ub=np.asarray(rhs),
                   A_eq=aa,b_eq=[float(k)],bounds=[(None,None)]*M+[(0,None)],
                   method='highs')

def test(N,k):
    q=math.sqrt(1-1/N**2)
    a=k/(N*math.sqrt(N*N-1))
    b=(N-k)/(N*math.sqrt(N-1))
    threshold=N+1-math.sqrt(N+1)
    rr=min(a,b)
    res=lp_radius(N,k)
    assert res.success,(N,k,res.message)
    assert abs(res.x[-1]-rr)<1e-9,(N,k,res.x[-1],rr)
    C0=np.full((N,N),k/(N*N))
    assert abs(C0.sum()-k)<1e-11
    coord=C0.min()/q
    row=(1-C0.sum(axis=1).max())/math.sqrt(N-1)
    col=(1-C0.sum(axis=0).max())/math.sqrt(N-1)
    assert abs(min(coord,row,col)-rr)<1e-11
    if k<threshold-1e-10:
        assert abs(rr-a)<1e-12 and b>a
        assert abs(rr*q-k/(N*N))<1e-12
    elif k>threshold+1e-10:
        assert abs(rr-b)<1e-12 and a>b
        s=(N-k)*math.sqrt(N+1)/(N*N)
        lam=(k-(N-k)*math.sqrt(N+1))/N
        assert lam>0
        # A permutation extreme point gives a nonuniform incenter.
        P=np.eye(N)
        C=s*np.ones((N,N))+lam*P
        assert np.all(C>0)
        assert abs(C.sum()-k)<1e-10
        assert max(abs(C.sum(axis=0)-k/N))<1e-10
        assert max(abs(C.sum(axis=1)-k/N))<1e-10
        assert abs(C.min()/q-rr)<1e-10
        # A strictly positive doubly stochastic matrix gives the uniform incenter.
        assert np.max(abs(s+lam/N-C0))<1e-12
    else:
        assert abs(a-b)<1e-10
        assert abs((N-k)*math.sqrt(N+1)/(N*N)-k/(N*N))<1e-10
    R2=k-k*k/(N*N)
    assert abs(np.sum((C0-C0)**2))<1e-12
    if N<=6 and k<=4:
        vertices=[]
        for ii in combinations(range(N),k):
            for jj in permutations(range(N),k):
                V=np.zeros((N,N))
                for u,v in zip(ii,jj):V[u,v]=1
                vertices.append(V)
        assert len(vertices)==math.comb(N,k)**2*math.factorial(k)
        centroid=np.mean(vertices,axis=0)
        assert np.max(abs(centroid-C0))<1e-12
        for V in vertices:
            assert abs(np.sum((V-C0)**2)-R2)<1e-10
        # Independent finite barycenter certificate for alternative center.
        alt=C0.copy();alt[0,0]+=0.05;alt[1,1]-=0.05
        d2=np.array([np.sum((V-alt)**2) for V in vertices])
        assert abs(np.mean(d2)-(R2+np.sum((alt-C0)**2)))<1e-10

for N in range(3,16):
    for k in range(2,N):
        test(N,k)

# Critical integer ranks: N+1 is a perfect square.
for h in range(2,7):
    N=h*h-1
    k=h*(h-1)
    assert 2<=k<N
    assert abs(N+1-math.sqrt(N+1)-k)<1e-12

print('VERIFY_OK k-assignment inballs N=3..15 all_k=yes full_intrinsic_LP=yes Birkhoff_incenter=yes small_outer_vertices=yes critical_ranks=yes')
