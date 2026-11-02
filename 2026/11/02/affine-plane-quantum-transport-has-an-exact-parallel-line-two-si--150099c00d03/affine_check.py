#!/usr/bin/env python3
"""Independent finite-prime-order checks of incidence spectral-projector capture formulas."""
import numpy as np
from collections import Counter, defaultdict

def incidence(q):
    P=[(x,y) for x in range(q) for y in range(q)]
    L=[('v',b) for b in range(q)]+[(m,b) for m in range(q) for b in range(q)]
    B=np.zeros((q*q,q*(q+1)),dtype=float)
    for i,(x,y) in enumerate(P):
        for j,(m,b) in enumerate(L):
            B[i,j]=int((x==b) if m=='v' else ((y-m*x-b)%q==0))
    assert np.allclose(B@B.T,q*np.eye(q*q)+np.ones((q*q,q*q)))
    return P,L,B

def projectors(q,B):
    Q,L=B.shape
    s0=np.sqrt(q*(q+1));s1=np.sqrt(q);N=Q+L
    Ip=np.eye(Q); Il=np.eye(L)
    Jp=np.ones((Q,Q));Jl=np.ones((L,L));Jpl=np.ones((Q,L))
    U=Jp/Q; V=Jl/L; C=Jpl/np.sqrt(Q*L)
    X=Ip-U;Y=(B.T@B-Jl)/q;Z=(B-Jpl/q)/s1
    E={}
    for sg in (1,-1):
        E[sg*s0]=.5*np.block([[U,sg*C],[sg*C.T,V]])
        E[sg*s1]=.5*np.block([[X,sg*Z],[sg*Z.T,Y]])
    E[0]=np.block([[np.zeros((Q,Q)),np.zeros((Q,L))],[np.zeros((L,Q)),Il-V-Y]])
    A=np.block([[np.zeros((Q,Q)),B],[B.T,np.zeros((L,L))]])
    for lam,e in E.items():
        assert np.max(np.abs(A@e-lam*e)) <1e-11
        assert np.max(np.abs(e@e-e))<1e-11
    assert np.max(np.abs(sum(E.values())-np.eye(N)))<1e-11
    return A,E

def capture(E,a,b):
    N=next(iter(E.values())).shape[0]
    eta=np.zeros(N)
    dimensions=[]
    for e in E.values():
        W=e[:,[a,b]];G=W[[a,b],:]
        vals, vecs=np.linalg.eigh(G)
        keep=vals>1e-9
        dimensions.append(int(keep.sum()))
        if keep.any():
            K=vecs[:,keep]/np.sqrt(vals[keep])[None,:]
            U=W@K
            eta+=np.sum(U*U,axis=1)
    return eta,sum(dimensions),dimensions

def expected_dimension(q,a,b,Q,lines):
    if a<Q and b<Q:return 6
    if a<Q or b<Q:return 7
    l1,l2=lines[a-Q],lines[b-Q]
    parallel = (l1[0]==l2[0])
    return 7 if parallel else 8

def independent_eig(A,sinks):
    vals,U=np.linalg.eigh(A)
    blocks=[];used=np.zeros(len(vals),bool)
    for i,v in enumerate(vals):
        if used[i]:continue
        idx=np.where(np.abs(vals-v)<1e-7)[0]
        used[idx]=True
        W=U[:,idx]@(U[sinks,:][:,idx].T)
        G=W[sinks,:]
        eig,V=np.linalg.eigh(G)
        j=eig>1e-8
        if np.any(j):blocks.append(W@(V[:,j]/np.sqrt(eig[j])))
    P=sum((X@X.T for X in blocks),np.zeros_like(A))
    return np.diag(P),np.trace(P)

def run():
    count=0; cases=Counter(); largest=0; dim_mismatch=0; incident_checks=0
    for q in (3,5,7):
        pts,lines,B=incidence(q);A,E=projectors(q,B);Q=len(pts);N=A.shape[0]
        pairs=[(a,b) for a in range(N) for b in range(a+1,N)]
        if q>3:
            rng=np.random.default_rng(271828+q)
            idx=rng.choice(len(pairs),size=160 if q==5 else 96,replace=False)
            pairs=[pairs[i] for i in idx]
            # guarantee geometric types
            pairs += [(0,1),(0,Q),(Q,Q+1),(Q,Q+q),(Q,Q+q*q)]
            pairs=list(dict.fromkeys(pairs))
        for a,b in pairs:
            e,d,ds=capture(E,a,b)
            predicted=expected_dimension(q,a,b,Q,lines)
            assert d==predicted,(q,a,b,d,predicted,ds)
            assert np.min(e)>-1e-8 and np.max(e)<1+1e-8
            de,dt=independent_eig(A,[a,b])
            err=max(np.max(np.abs(de-e)),abs(dt-d))
            assert err<2e-8,(q,a,b,err)
            largest=max(largest,err);count+=1
            if a<Q and b>=Q and B[a,b-Q]>0.5:
                # Test the *whole* incidence-conditioned site histogram, not just its trace.
                actual=Counter(round(float(v),12) for v in e)
                predicted={round(1.,12):2,round(1/(q-1),12):2*(q-1),round(1/q,12):q,round(1/(q*(q-1)),12):2*q*(q-1)}
                assert actual==predicted,(q,a,b,actual,predicted)
                incident_checks+=1
            typ='PP' if b<Q else 'PL' if a<Q else 'LL-parallel' if lines[a-Q][0]==lines[b-Q][0] else 'LL-intersect'
            cases[(q,typ,d)]+=1
    print('projector-vs-full-eigendecomposition checked_pairs',count)
    print('maximum_absolute_error',format(largest,'.5g'))
    print('counts_by_type',sorted((q,t,d,n) for (q,t,d),n in cases.items()))
    print('incident_point_line_site_histograms',incident_checks)
    print('all_assertions_passed')
if __name__=='__main__':run()
