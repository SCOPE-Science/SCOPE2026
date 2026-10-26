"""Reproducible exact and floating-point checks for the three-constraint arrow family.

Requires only the Python standard library for rational symbolic identities;
NumPy is used only for optional independent matrix eigenvalue replay.
"""
from fractions import Fraction as F
from itertools import permutations
from math import sqrt


def determinant3(A):
    a,b,c=A[0];d,e,f=A[1];g,h,i=A[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def matrices(t,s,p):
    r=((F(1),F(0),F(0)),(t,s,F(0)),(t,F(0),s))
    q=[r[i] for i in p]
    G=[[sum(u*v for u,v in zip(a,b)) for b in q] for a in q]
    det=determinant3(G)
    assert det>0
    S=(F(1), 1-G[0][1]**2, det/(1-G[0][1]**2))
    T=sum(G[i][i]/S[i] for i in range(3))
    U=sum((G[i][i]*G[j][j]-G[i][j]**2)/(S[i]*S[j]) for i in range(3) for j in range(i+1,3))
    V=det/(S[0]*S[1]*S[2])
    assert V==1
    return G,S,(T,U,V)


def main():
    examples=((2,1),(3,1),(3,2),(4,3),(5,2),(5,1),(10,1))
    exact_checks=0
    for m,n in examples:
        t=F(m*m-n*n,m*m+n*n)
        s=F(2*m*n,m*m+n*n)
        assert 0<t<1 and t*t+s*s==1
        y=t*t; d=1-y
        Ta=1+2/d; Ua=Ta
        Tb=Ta; Ub=Ta-y*y/d
        Tc=Ta+y*y/(d*(1+y)); Uc=Ub
        for p in permutations(range(3)):
            _,S,(T,U,V)=matrices(t,s,p)
            expected = ((Ta,Ua) if p[0]==0 else (Tb,Ub) if p[1]==0 else (Tc,Uc))
            assert (T,U)==expected, (t,p,T,U,expected)
            exact_checks+=1
    print('exact rational coefficient checks:',exact_checks)

    import numpy as np
    samples=(0.05,0.2,0.6,0.9,0.99,0.9999)
    numeric_checks=0
    for t in samples:
        s=sqrt(1-t*t)
        r=np.array([[1.,0.,0.],[t,s,0.],[t,0.,s]])
        maxima={}
        for p in permutations(range(3)):
            q=r[list(p),:]
            G=q@q.T
            S=[1.,1.-G[0,1]**2,float(np.linalg.det(G))/(1.-G[0,1]**2)]
            assert min(S)>0
            W=q/np.sqrt(S)[:,None]
            H=W@W.T
            eig=np.linalg.eigvalsh(H)
            positive=(1.+np.sqrt(1.+4*eig))/2.
            Q=np.block([[np.eye(3),W.T],[W,np.zeros((3,3))]])
            actual=np.linalg.eigvalsh(Q)
            predicted=np.sort(np.r_[positive,(1.-np.sqrt(1.+4*eig))/2.])
            assert np.allclose(predicted, actual, rtol=1.e-7, atol=1.e-8)
            maxima[p]=eig[-1]
            numeric_checks+=1
        A=maxima[(0,1,2)]; B=maxima[(1,0,2)]; C=maxima[(1,2,0)]
        assert A<B<C,(t,A,B,C)
        assert np.isclose(maxima[(0,2,1)],A)
        assert np.isclose(maxima[(2,0,1)],B)
        assert np.isclose(maxima[(2,1,0)],C)
        print('t=',t,'top singular squares:',A,B,C)
    print('independent numerical full-matrix spectral checks:',numeric_checks)
    t=0.9999; s=sqrt(1-t*t); r=np.array([[1.,0.,0.],[t,s,0.],[t,0.,s]])
    z=[]
    for p in ((0,1,2),(1,2,0)):
        q=r[list(p)]; G=q@q.T; d=1-G[0,1]**2;S=[1,d,np.linalg.det(G)/d]
        W=q/np.sqrt(S)[:,None]
        z.append(np.linalg.eigvalsh(W@W.T)[-1])
    print('large-coupling ratio:',z[1]/z[0], 'limit:',1.25)

if __name__=='__main__':
    main()
