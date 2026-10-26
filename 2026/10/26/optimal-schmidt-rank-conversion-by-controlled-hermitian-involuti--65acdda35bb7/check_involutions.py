#!/usr/bin/env python3
"""Finite consistency checks for the constructive Hermitian Schmidt-rank reachability theorem.
Requires numpy. No finite computation is used as proof of the all-dimensional theorem.
"""
import math
import numpy as np


def controlled_reflection(m, n, p, q):
    assert 1 <= p <= min(m,n) and 1 <= q <= min(m,n)
    x=np.zeros((m,n),complex)
    a=np.arange(1,p+1,dtype=float)
    a/=np.linalg.norm(a)
    for j in range(p): x[j,j]=a[j]
    P=[]; V=[]
    if q <= p:
        t=(p+q-1)//q
        groups=[list(range(q))]
        tail=list(range(q,p))
        groups.extend([tail[i:i+q] for i in range(0,len(tail),q)])
        assert len(groups)==t
        for r,G in enumerate(groups):
            Q=np.zeros((m,m),complex)
            if r==0:
                G=G+list(range(p,m))
            for j in G: Q[j,j]=1
            W=np.eye(n,dtype=complex)
            if r>0:
                for j,src in enumerate(groups[r]):
                    dst=groups[0][j]
                    W[src,src]=W[dst,dst]=0
                    W[src,dst]=W[dst,src]=1
            P.append(Q);V.append(W)
    else:
        t=(q+p-1)//p
        groups=[list(range(p))]
        extra=q-p
        for r in range(1,t):
            group=list(range(min(p,extra)))
            groups.append(group)
            extra-=len(group)
        assert extra==0
        positions={a: [a] for a in range(p)}
        idx=p
        targets={}
        for r in range(1,t):
            for a in groups[r]:
                positions[a].append(idx)
                targets[(r,a)]=idx
                idx+=1
        assert idx==q
        evec={}
        for a in range(p):
            coords=positions[a]
            v=len(coords)
            if v==1:
                H=np.eye(1)
            else:
                h=np.ones(v)/np.sqrt(v)
                e=np.eye(v)[0]
                u=h-e
                H=np.eye(v)-2*np.outer(u,u)/np.dot(u,u)
            for i,r in enumerate([r for r,G in enumerate(groups) if a in G]):
                w=np.zeros(m,complex)
                w[coords]=H[:,i]
                evec[(r,a)]=w
            z=sum([evec[(r,a)] for r,G in enumerate(groups) if a in G])/math.sqrt(v)
            assert np.allclose(z,np.eye(m)[a],atol=1e-12)
        for r,G in enumerate(groups):
            Q=np.zeros((m,m),complex)
            for a in G:
                v=evec[(r,a)]
                Q+=np.outer(v,v.conj())
            if r==0: Q+=np.eye(m)-sum((np.outer(w,w.conj()) for w in evec.values()),start=np.zeros((m,m),complex))
            W=np.eye(n,dtype=complex)
            if r>0:
                for a in G:
                    dst=targets[(r,a)]
                    W[a,a]=W[dst,dst]=0
                    W[a,dst]=W[dst,a]=1
            P.append(Q); V.append(W)
    U=sum([np.kron(Q,W) for Q,W in zip(P,V)],start=np.zeros((m*n,m*n),complex))
    return U,x,t


def numerical_rank(A):
    s=np.linalg.svd(A,compute_uv=False)
    return int(np.sum(s>1e-8))


def osr(U,m,n):
    return numerical_rank(U.reshape(m,n,m,n).transpose(0,2,1,3).reshape(m*m,n*n))


def run():
    cases=0
    for m,n in [(d,d) for d in range(1,9)]+[(3,5),(5,3),(4,6),(6,4)]:
        for p in range(1,min(m,n)+1):
            for q in range(1,min(m,n)+1):
                U,X,t=controlled_reflection(m,n,p,q)
                y=(U@X.ravel()).reshape(m,n)
                assert np.allclose(U,U.conj().T,atol=1e-10),(m,n,p,q,'herm')
                assert np.allclose(U@U,np.eye(m*n),atol=1e-10),(m,n,p,q,'involution')
                assert numerical_rank(y)==q,(m,n,p,q,'q rank')
                assert osr(U,m,n)==t,(m,n,p,q,'osr',osr(U,m,n),t)
                assert t==math.ceil(max(p/q,q/p))
                cases+=1
    print(f'PASS {cases} dimensions/ranks; reflection, Schmidt rank, and exact OSR each.')

if __name__=='__main__':
    run()
