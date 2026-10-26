#!/usr/bin/env python3
"""Reproducible finite-dimensional checks for single-node Poisson-reset linear phase networks.
No external data; run: python verify_reset_graph.py (requires numpy)."""
import numpy as np

def calc(edges,n,root,c,lam,omega):
    L=np.zeros((n,n))
    for i,j in edges:
        L[i,i]+=1; L[j,j]+=1; L[i,j]-=1;L[j,i]-=1
    e=np.eye(n)[root]
    P=np.outer(e,e); J=np.eye(n)-P
    m=np.linalg.solve(c*L+lam*P,omega)
    # M_ij equation: c(L C+C L)+lam(C-J C J)= (Omega**2/lam)*P.
    M=c*(np.kron(np.eye(n),L)+np.kron(L,np.eye(n)))+lam*(np.eye(n*n)-np.kron(J,J))
    C=np.linalg.solve(M,(sum(omega)**2/lam*P).reshape(-1)).reshape(n,n)
    return L,m,C

def check():
    graphs=[(2,[(0,1)]),(3,[(0,1),(1,2)]),(4,[(0,1),(0,2),(0,3)]),
      (5,[(0,1),(1,2),(2,3),(3,4)]), (6,[(0,1),(1,2),(1,3),(3,4),(3,5)]),
      (7,[(0,1),(1,2),(2,3),(3,4),(2,5),(5,6)])]
    checks=0
    for n,edges in graphs:
        for root in (0,n-1):
            c=1.3
            w=np.array([(-1)**i*(i+0.8) for i in range(n)],float)
            w2=w +np.arange(n,dtype=float)-np.mean(np.arange(n))
            L,m,C=calc(edges,n,root,c,3.4,w)
            _,m2,C2=calc(edges,n,root,c,3.4,w2)
            Om=sum(w)
            assert abs(sum(w2)-Om)<1e-10
            assert np.max(np.abs(C-C2))<1e-10;checks+=1
            assert np.allclose(c*L@m+3.4*m[root]*np.eye(n)[root],w,atol=1e-10);checks+=1
            assert np.isclose(m[root],Om/3.4,atol=1e-10);checks+=1
            ground=np.delete(np.delete(L,root,0),root,1)
            others=[i for i in range(n) if i!=root]
            shift=np.zeros(n);shift[others]=np.linalg.solve(c*ground,w[others])
            assert np.allclose(m,shift+Om/3.4,atol=1e-10);checks+=1
            assert np.min(np.linalg.eigvalsh(C))>-1e-9;checks+=1
            if abs(Om)>1e-5:
                assert np.min(C)>0;checks+=1
            wzero=w-np.mean(w)
            _,mz,Cz=calc(edges,n,root,c,3.4,wzero)
            assert np.max(np.abs(Cz))<1e-10;checks+=1
            # strong reset cubic suppression, per non-reset block
            aa=-L[others,root]
            B=L[np.ix_(others,others)]
            expect=np.linalg.solve(np.kron(np.eye(n-1),B)+np.kron(B,np.eye(n-1)),(2*c*Om*Om*np.outer(aa,aa)).reshape(-1)).reshape(n-1,n-1)
            for rate in (1000.,10000.):
                _,_,Cv=calc(edges,n,root,c,rate,w)
                assert abs(Cv[root,root]*rate**2 / Om**2 -1)<0.03;checks+=1
                err=np.max(np.abs(Cv[np.ix_(others,others)]*rate**3-expect))
                assert err < 0.12*max(1,np.max(abs(expect))), (n,root,rate,err,expect)
                checks+=1
            if n==2:
                lam=3.4
                exact_rr=Om**2*(lam+c)/(lam**2*(lam+3*c))
                exact_mm=Om**2*c/(lam**2*(lam+3*c))
                assert np.isclose(C[root,root],exact_rr);checks+=1
                assert np.isclose(C[others[0],others[0]],exact_mm);checks+=1
    # pathwise affine shift: same shocks and same initial universal perturbation
    n=4;edges=[(0,1),(1,2),(2,3)];root=0;c=1.1
    L,m,C=calc(edges,n,root,c,2.3,np.array([.7,-.2,.1,1.3]))
    q1=np.array([.7,-.2,.1,1.3]);q2=np.array([-.1,.9,.7,.4])
    assert abs(sum(q1)-sum(q2))<1e-10
    B=np.delete(np.delete(L,root,0),root,1)
    base1=np.r_[0.,np.linalg.solve(c*B,q1[1:])]
    base2=np.r_[0.,np.linalg.solve(c*B,q2[1:])]
    from scipy.linalg import expm
    z=np.array([.2,.1,-.3,.4])
    for dt in (.017,.34,.089,.12):
        # exact for deterministic test: use augmented exp
        H=np.zeros((n+1,n+1));H[:n,:n]=-c*L;H[:n,-1]=q1
        H2=H.copy();H2[:n,-1]=q2
        F=expm(H*dt);F2=expm(H2*dt)
        x=base1+z; y=base2+z
        dx=F[:n,:n]@x+F[:n,-1]
        dy=F2[:n,:n]@y+F2[:n,-1]
        assert np.allclose(dx-base1,dy-base2,atol=1e-12);checks+=1
        z=dx-base1
        z[root]=0.
    print('PASS',checks,'independent checks; examples: root covariance and cubic distant-node covariance')

if __name__=='__main__':check()
