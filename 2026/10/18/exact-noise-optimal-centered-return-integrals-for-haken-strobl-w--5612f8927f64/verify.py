#!/usr/bin/env python3
"""Finite independent checks for complete-bipartite Haken–Strobl resolvent."""
from fractions import Fraction as F
import numpy as np
from scipy.linalg import solve

def exact(a,b,g,J):
    n=a+b
    K=n*(n-1)-b
    R=n*(n-1)*(n-2)-b*n*n+4*b*b
    return F(K)*g/(2*b*J*J*n*(n-1))+F(R)/(2*g*n*(n-1))

def full_lindblad(a,b,g,J):
    n=a+b
    A=np.zeros((n,n))
    A[:a,a:]=1;A[a:,:a]=1
    H=float(J)*A
    # vec, column-major. -i[H,rho] = -i (I kron H - H^T kron I) vec(rho)
    L=-1j*(np.kron(np.eye(n),H)-np.kron(H.T,np.eye(n)))
    for i in range(n):
        for j in range(n):
            if i!=j: L[i+n*j,i+n*j]-=float(g)
    rho=np.zeros((n,n),dtype=complex);rho[0,0]=1
    centered=rho-np.eye(n)/n
    # Any trace-zero inverse can be computed by regularization of the stationarity mode.
    v=centered.reshape(n*n,order='F')
    trace_row=np.eye(n).reshape(n*n,order='F')
    projector=np.outer(np.eye(n).reshape(n*n,order='F')/n,trace_row)
    X=solve(-L+projector,v,assume_a='gen')
    return (n*X[0].real)/(n-1)

def internal_integrated_equations(a,b,g,J):
    n=a+b
    if a==1:
        P=F(n-1,2*b*J*n)
        W=F(1,g*n) if b>=2 else F(0)
        E=g*P/J+(b-1)*W
        X=F(b,n)*E
        assert X*n/F(n-1)==exact(a,b,g,J)
        return
    P=F(n-1,2*b*J*n);Q=F(-1,2*b*J*n)
    U=F(-(n-2),2*g*n);V=F(1,g*n);W=F(1,g*n)
    E=(g*P/J)-(a-1)*U+(b-1)*W
    F_=(g*Q/J)-U-(a-2)*V+(b-1)*W
    X=((n-1)*E-(a-1)*F_)/n
    assert X*n/F(n-1)==exact(a,b,g,J)

count=0
for a in range(1,6):
    for b in range(1,6):
        for g,J in [(F(1),F(1)),(F(2),F(1)),(F(3,2),F(5,3))]:
            x=exact(a,b,g,J)
            y=full_lindblad(a,b,g,J)
            assert abs(y-float(x))<1e-7*(1+abs(float(x))), (a,b,g,J,x,y)
            internal_integrated_equations(a,b,g,J)
            count+=2
for a,b in [(1,2),(1,5),(2,1),(2,3),(3,2),(4,5),(5,4)]:
    n=a+b;K=n*(n-1)-b;R=n*(n-1)*(n-2)-b*n*n+4*b*b
    assert R>0
    gamma=np.sqrt(b*R/K)
    opt=float(exact(a,b,F.from_float(gamma),F(1)))
    for factor in [0.5,0.8,1.2,2.0]:
        assert opt<float(exact(a,b,F.from_float(gamma*factor),F(1)))
        count+=1
print('VERIFY_OK',count,'full-Lindblad, rational symmetry and optimizer comparisons')
