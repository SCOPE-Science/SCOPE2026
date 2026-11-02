#!/usr/bin/env python3
"""Finite spectral and Krylov checks for two absorbing vertices on primitive distance-regular examples."""
import itertools, numpy as np, math
from collections import deque

def distance_matrix(adj):
    n=len(adj); D=np.full((n,n),n+1,dtype=int)
    for s in range(n):
        D[s,s]=0; queue=deque([s])
        while queue:
            u=queue.popleft()
            for v in np.flatnonzero(adj[u]):
                if D[s,v]>n:
                    D[s,v]=D[s,u]+1;queue.append(v)
    return D

def examples():
    n=7;A=np.zeros((n,n),dtype=int)
    for u in range(n): A[u,(u+1)%n]=A[u,(u-1)%n]=1
    yield 'odd-prime-cycle-C7',A
    n=10;A=np.zeros((n,n),dtype=int)
    verts=list(itertools.combinations(range(5),2))
    for i,U in enumerate(verts):
        for j,V in enumerate(verts): A[i,j]=int(not set(U).intersection(V))
    yield 'Petersen-KG(5,2)',A
    for n,k,name,rule in [(7,3,'Odd-graph-KG(7,3)','disjoint'),(8,3,'Johnson-J(8,3)','intersect2')]:
        verts=list(itertools.combinations(range(n),k))
        A=np.zeros((len(verts),len(verts)),dtype=int)
        for i,U in enumerate(verts):
            U=set(U)
            for j,V in enumerate(verts):
                if i!=j:A[i,j]=int((not U.intersection(V)) if rule=='disjoint' else (len(U.intersection(V))==k-1))
        yield name,A
    verts=list(itertools.product(range(3),repeat=3)); A=np.zeros((27,27),dtype=int)
    for i,U in enumerate(verts):
        for j,V in enumerate(verts): A[i,j]=int(sum(a!=b for a,b in zip(U,V))==1)
    yield 'Hamming-H(3,3)',A

def check(name,A):
    n=len(A); dist=distance_matrix(A); D=int(dist.max())
    eigs,U=np.linalg.eigh(A);groups=[]
    for i,e in enumerate(eigs):
        if not groups or abs(e-groups[-1][0])>1.e-7:groups.append([e,[i]])
        else:groups[-1][1].append(i)
    assert len(groups)==D+1,(name, groups, D)
    groups=groups[::-1] # valency (principal) first
    E=[U[:,idx]@U[:,idx].T for _,idx in groups]
    diag_err=max(abs(Ej.diagonal()-len(idx)/n).max() for Ej,(_,idx) in zip(E,groups))
    conn=[]
    for r in range(1,D+1):
        DD=(dist==r).astype(int)
        cc=distance_matrix(DD)
        conn.append(int(cc.max())<n+1)
    assert all(conn),(name,conn)
    max_probability_error=0; min_cosine_gap=1; tested=0; rank_min=n
    for u in range(n):
      for v in range(u+1,n):
        w=np.zeros((n,2));w[u,0]=w[v,1]=1
        B=[]; cols=[]
        for j,Ej in enumerate(E):
            F=Ej@w;G=F.T@F
            if j>0:
                cosine=G[0,1]/G[0,0]
                min_cosine_gap=min(min_cosine_gap,1-abs(cosine))
                assert abs(cosine)<1-1e-7,(name,u,v,j,cosine)
            B.append(F@np.linalg.pinv(G,rcond=1e-9)@F.T)
        P=sum(B)
        K=[];vects=w.copy()
        for h in range(D+1):
            K.append(vects);vects=A@vects
        Q,_=np.linalg.qr(np.concatenate(K,axis=1))
        # stable rank from singular-value decomposition of Krylov
        UK,s,VT=np.linalg.svd(np.concatenate(K,axis=1),full_matrices=False)
        rank=int((s>1e-7*s[0]).sum())
        rank_min=min(rank_min,rank)
        PK=UK[:,:rank]@UK[:,:rank].T
        max_probability_error=max(max_probability_error,np.max(abs(np.diag(P)-np.diag(PK))),np.max(abs(P-PK)))
        assert rank==2*D+1,(name,u,v,rank,D)
        assert abs(np.trace(P)-(2*D+1))<1e-7,(name,u,v,np.trace(P))
        assert max_probability_error<1e-7,(name,u,v,max_probability_error)
        tested+=1
    print(f'{name}: v={n}, diameter={D}, all_distance_graphs_connected={conn}, pairs_tested={tested}, bright_dimension={2*D+1}, average_capture={(2*D+1)/n:.12f}, min_cosine_gap={min_cosine_gap:.5e}, max_projector_error={max_probability_error:.3e}, diagonal_error={diag_err:.3e}')

def main():
    for name,A in examples():check(name,A)
    print('ALL FINITE TESTS PASSED')
if __name__=='__main__':main()
