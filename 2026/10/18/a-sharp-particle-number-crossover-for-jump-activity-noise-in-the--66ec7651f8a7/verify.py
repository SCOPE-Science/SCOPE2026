#!/usr/bin/env python3
"""Exact rational consistency checks for a two-site inclusion-process activity formula."""
from fractions import Fraction as F


def solve(A,b):
    n=len(b)
    M=[[F(v) for v in row]+[F(b[i])] for i,row in enumerate(A)]
    for c in range(n):
        p=next((i for i in range(c,n) if M[i][c]),None)
        assert p is not None
        M[c],M[p]=M[p],M[c]
        fac=M[c][c]
        M[c]=[a/fac for a in M[c]]
        for i in range(n):
            if i==c:continue
            fac=M[i][c]
            if fac:M[i]=[u-fac*v for u,v in zip(M[i],M[c])]
    return [row[-1] for row in M]


def check(n,d):
    b=[(n-k)*(d+k) for k in range(n+1)]
    a=[k*(d+n-k) for k in range(n+1)]
    Q=[[F(0) for _ in range(n+1)] for _ in range(n+1)]
    for k in range(n+1):
        if k<n:Q[k][k+1]=b[k]
        if k>0:Q[k][k-1]=a[k]
        Q[k][k]=-a[k]-b[k]
    w=[F(1)]
    for k in range(n):w.append(w[-1]*b[k]/a[k+1])
    W=sum(w);pi=[z/W for z in w]
    assert all(sum(pi[i]*Q[i][j] for i in range(n+1))==0 for j in range(n+1))
    q=[a[k]+b[k] for k in range(n+1)]
    mu=sum(pi[k]*q[k] for k in range(n+1))
    assert mu==F(n)*d*(n+2*d)/(2*d+1)
    L=[[-Q[i][j] for j in range(n+1)] for i in range(n+1)]
    rhs=[z-mu for z in q]
    L[-1]=pi[:];rhs[-1]=F(0)
    h=solve(L,rhs)
    assert all(sum(Q[i][j]*h[j] for j in range(n+1))==mu-q[i] for i in range(n+1))
    raw=sum(pi[i]*(sum(Q[i][j]*h[j] for j in range(n+1) if i!=j)) for i in range(n+1))
    nu=mu+2*raw
    fano=1+F((n-1))*(n+2*d+1)/((2*d+1)**2*(2*d+3))
    assert nu==mu*fano,(n,d,nu,mu*fano)
    assert sum(pi[i]*(F(2*i-n,2)**2) for i in range(n+1))==F(n)*(n+2*d)/(4*(2*d+1))
    for k in range(n+1):
        xx=F(2*k-n,2)
        lx2=sum(Q[k][j]*(F(2*j-n,2)**2) for j in range(n+1))
        assert lx2==d*n+F(n*n,2)-(4*d+2)*xx**2
    return (mu,nu)

if __name__=='__main__':
    count=0
    for n in range(1,10):
        for d in [F(1,5),F(1,2),F(2,3),F(1),F(5,3),F(3)]:
            check(n,d)
            count+=1
    print('PASS:',count,'exact rational stationary, generator, Poisson and activity-variance tests')
