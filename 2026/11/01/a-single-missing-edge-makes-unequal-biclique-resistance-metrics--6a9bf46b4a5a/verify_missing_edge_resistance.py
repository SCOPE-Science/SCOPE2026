"""Exact audit of the four-class formula for K_(m,n) with one missing edge.
Run: python verify_missing_edge_resistance.py  (requires SymPy and NumPy).
"""
import sympy as S
import numpy as np


def group_form(m,n):
    k=m*n*(m-1)*(n-1)
    s=S.Rational(m+n-1,m*n)
    w=[1,m-1,1,n-1]
    potentials=[m,0,1-n,1]
    side=[0,0,1,1]
    M=S.zeros(4)
    for i in range(4):
        for j in range(4):
            base=(S.Rational(2,n) if side[i]==side[j]==0 else
                  S.Rational(2,m) if side[i]==side[j]==1 else s)
            if i==j: M[i,j]=(1-S.Rational(1,w[i]))*base**2
            else:M[i,j]=(base+S.Rational((potentials[i]-potentials[j])**2,k))**2
    U=S.Matrix([[1,0,1],[-1,0,0],[0,1,-1],[0,-1,0]])
    return -U.T*M*U/2


def inverse_resistance(m,n):
    N=m+n
    L=S.zeros(N)
    for i in range(m):
        for j in range(n):
            if (i,j)==(0,0):continue
            u,v=i,m+j
            L[u,u]+=1; L[v,v]+=1; L[u,v]-=1;L[v,u]-=1
    Z=L[:N-1,:N-1].inv()
    R=S.zeros(N)
    for i in range(N):
        for j in range(i+1,N):
            z=(Z[i,i] if i<N-1 else 0)+(Z[j,j] if j<N-1 else 0)
            if i<N-1 and j<N-1:z-=2*Z[i,j]
            R[i,j]=R[j,i]=z
    return R


def P(s,t):
    return (6*s**4+29*s**3*t+36*s**3+33*s**2*t**2+154*s**2*t+72*s**2
           +14*s*t**3+125*s*t**2+265*s*t+48*s+2*t**4+28*t**3
           +116*t**2+146*t)

for m in range(2,7):
    for n in range(2,7):
        R=inverse_resistance(m,n)
        N=m+n
        k=m*n*(m-1)*(n-1)
        potentials=[m]+[0]*(m-1)+[1-n]+[1]*(n-1)
        for i in range(N):
            for j in range(i+1,N):
                if i<m and j<m:base=S.Rational(2,n)
                elif i>=m and j>=m:base=S.Rational(2,m)
                else:base=S.Rational(m+n-1,m*n)
                expected=base+S.Rational((potentials[i]-potentials[j])**2,k)
                assert R[i,j]==expected,(m,n,i,j)
        H=group_form(m,n)
        A=m*m*(m-n)+(n-2)*(m+1)
        B=n*n*(m-n)-(m-2)*(n+1)
        D=m*m*n*n*(m-1)**4*(n-1)**4
        assert H.det()==S.Rational(-4*A*B,D),(m,n,'det3')
        x,y=m-2,n-2
        assert H[:2,:2].det()==S.Rational(2*P(x+y,x*y),D),(m,n,'det2')
        assert H[0,0]>0
        J=S.eye(N)-S.ones(N)/N
        G=-J*R.multiply_elementwise(R)*J/2
        eig=np.linalg.eigvalsh(np.asarray(G.tolist(),dtype=float))
        negatives=int(np.sum(eig<-1e-8))
        zeros=int(np.sum(abs(eig)<1e-8))
        if m==n==2:expected=(0,3)
        elif m==n:expected=(0,1)
        else:expected=(1,1)
        assert (negatives,zeros)==expected,(m,n,negatives,zeros,expected)
    print('EXACT_OK m=',m,'n=2..6',flush=True)
print('ALL_DELETED_BICLIQUE_RESISTANCE_CHECKS_OK',flush=True)
