"""Exact moment checks for random moving-average feedback; no simulations needed."""
from fractions import Fraction as Q
import itertools
import numpy as np

def one(m,a,v,rho,tau=Q(1)):
    a,v,rho,tau=map(Q,(a,v,rho,tau))
    den=m-(m-1)*a
    r=a/den
    S=[[Q(1) if i==j else r for j in range(m)] for i in range(m)]
    F=a*a/den+v/Q(m)*(1+(m-1)*rho*r)
    def K(P):
        T=[[Q(0) for j in range(m)] for i in range(m)]
        for i in range(m):
            for j in range(m):
                if i and j: T[i][j]=P[i-1][j-1]
                elif i or j:
                    k=(i or j)-1
                    T[i][j]=a/Q(m)*sum(P[t][k] for t in range(m))
                else:
                    T[i][j]=a*a/Q(m*m)*sum(sum(row) for row in P)+v/Q(m*m)*sum(P[s][t]*(Q(1) if s==t else rho) for s in range(m) for t in range(m))
        return T
    T=K(S)
    for i in range(m):
        for j in range(m):
            assert T[i][j]-S[i][j]== (F-1 if i==j==0 else 0)
    vmax=Q(m)*(1-a)*(m+a)/(m-(m-1)*a*(1-rho))
    assert (F<1)==(v<vmax)
    if F<1:
        u=tau/(1-F)
        P=[[u*z for z in row] for row in S]
        KP=K(P)
        for i in range(m):
            for j in range(m):
                assert P[i][j]-KP[i][j]==(tau if i==j==0 else 0)
        B=np.zeros((m,m));B[0,:]=float(a)/m;B[1:,:-1]=np.eye(m-1)
        cov=np.array([[float(v)*(1 if i==j else float(rho))/m**2 for j in range(m)] for i in range(m)])
        E=np.zeros((m*m,m*m))
        E+=np.kron(B,B)
        for i in range(m):
            for j in range(m):
                E[0,i*m+j]+=cov[i,j]
        eig=max(abs(np.linalg.eigvals(E)))
        assert eig<1+1e-8,(m,a,v,rho,eig)
    return 1

count=0
for m in range(2,8):
    rhovals=[Q(1),Q(0),-Q(1,m-1), Q(1,3), Q(1,2)]
    avals=[-Q(m)+Q(1,2),-Q(m,2),-Q(1,2),Q(0),Q(1,4),Q(3,4)]
    for a,rho in itertools.product(avals,rhovals):
        vmax=Q(m)*(1-a)*(m+a)/(m-(m-1)*a*(1-rho))
        for mult in [Q(0),Q(1,4),Q(3,4),Q(99,100),Q(1),Q(3,2)]:
            count+=one(m,a,vmax*mult,rho)
assert count==6*6*5*6
# Sharp distinction at the two extremal correlations.
for m in range(2,9):
    for a in [-Q(m-1,2),Q(1,3)]:
        def cap(rho):return Q(m)*(1-a)*(m+a)/(m-(m-1)*a*(1-rho))
        assert cap(-Q(1,m-1))==m+a
        assert cap(Q(1))==(1-a)*(m+a)
        assert (cap(-Q(1,m-1))>cap(1)) == (a>0)
print('PASS:',count,'exact symbolic-state covariance checks, additional extremal checks')
