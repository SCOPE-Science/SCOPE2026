#!/usr/bin/env python3
"""Finite-size numerical consistency checks for two-site quantum absorption on Hamming graphs."""
from itertools import product, combinations
from math import comb
import numpy as np
from scipy.linalg import expm

def adjacency(q,d):
    vertices=list(product(range(q),repeat=d)); N=len(vertices)
    A=np.zeros((N,N),dtype=float)
    for i,u in enumerate(vertices):
        for j,v in enumerate(vertices):
            if sum(a!=b for a,b in zip(u,v))==1: A[i,j]=1
    return vertices,A

def kah(q,d,k,h):
    return sum((-1)**j*(q-1)**(k-j)*comb(h,j)*comb(d-h,k-j)
               for j in range(max(0,k-d+h),min(k,h)+1))

def predicted(q,d,h):
    if q==2 and h==d:return d+1
    if q==2:return 2*d
    return 2*d+1

def formula_eta(q,d,u,v,x):
    h=sum(a!=b for a,b in zip(u,v)); a=sum(i!=j for i,j in zip(x,u)); b=sum(i!=j for i,j in zip(x,v)); N=q**d
    ans=0.
    for k in range(d+1):
        B=comb(d,k)*(q-1)**k
        K=kah(q,d,k,h); ka=kah(q,d,k,a); kb=kah(q,d,k,b)
        if B==abs(K):
            ans+=ka*ka/(N*B)
        else:
            ans+=(B*(ka*ka+kb*kb)-2*K*ka*kb)/(N*(B*B-K*K))
    return ans

def run():
    count=0; vals=[]
    cases=[(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3),(4,1),(4,2)]
    for q,d in cases:
        vs,A=adjacency(q,d); N=len(vs); u=vs[0]
        eigvals=[d*(q-1)-q*k for k in range(d+1)]
        evecs=[]
        for k,ev in enumerate(eigvals):
            # exact spectral projector as polynomial in graph adjacency; floats okay here
            P=np.eye(N)
            for j,ev2 in enumerate(eigvals):
                if j!=k:P=P@(A-ev2*np.eye(N))/(ev-ev2)
            evecs.append(P)
        for h in range(1,d+1):
            v=tuple([1]*h+[0]*(d-h)); vid=vs.index(v)
            cols=[]
            for P in evecs:
                cols.extend([P[:,0],P[:,vid]])
            M=np.column_stack(cols)
            rank=np.linalg.matrix_rank(M,tol=1e-7)
            assert rank==predicted(q,d,h),(q,d,h,rank)
            Q=M@np.linalg.pinv(M)
            proj=np.real(np.diag(Q))
            assert abs(proj.sum()-rank)<1e-7
            for i,x in enumerate(vs):
                f=formula_eta(q,d,u,v,x)
                assert abs(f-proj[i])<1e-7,(q,d,h,x,f,proj[i])
                count+=1
            if q==2 and h==d:
                for i,x in enumerate(vs):
                    a=sum(t!=w for t,w in zip(x,u))
                    assert abs(proj[i]-1/comb(d,a))<1e-7
            if q==2 and h==1:
                for i,x in enumerate(vs):
                    a=sum(t!=w for t,w in zip(x[1:],u[1:]))
                    assert abs(proj[i]-1/comb(d-1,a))<1e-7
            vals.append((q,d,h,rank,round(rank/N,8)))
    # finite-absorption direct propagator in a case with a dark state
    q,d=3,2
    vs,A=adjacency(q,d)
    u=vs[0]; v=(1,0); vid=vs.index(v)
    H=A.astype(complex)-.5j*np.diag([1.3 if i==0 else .7 if i==vid else 0 for i in range(len(vs))])
    U=expm(-1j*H*900)
    predicted_survival=1-(2*d+1)/len(vs)
    surv=np.linalg.norm(U,'fro')**2/len(vs)
    assert abs(surv-predicted_survival)<2e-7,(surv,predicted_survival)
    print('PASS',len(cases),'parameter families,',len(vals),'two-detector distance cases,',count,'spectral projection site comparisons')
    print('Direct non-Hermitian propagation average survival:',surv,'expected',predicted_survival)
    for x in vals:print(x)
if __name__=='__main__':run()
