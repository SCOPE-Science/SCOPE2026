import cmath
import math

def det4(M):
    A=[list(map(complex,row)) for row in M]
    d=1+0j
    for i in range(4):
        p=max(range(i,4),key=lambda r:abs(A[r][i]))
        if abs(A[p][i])<1e-14:
            return 0j
        if p!=i:
            A[i],A[p]=A[p],A[i]
            d*=-1
        piv=A[i][i]
        d*=piv
        for r in range(i+1,4):
            f=A[r][i]/piv
            for c in range(i+1,4):
                A[r][c]-=f*A[i][c]
    return d

def matrix(beta,eta,kd,lam):
    s=eta*lam
    a=(1-beta)*kd*lam
    return [[1-s+a,-a,beta,kd*beta],
            [1,0,0,0],
            [-s,0,beta,0],
            [(1-beta)*lam,-(1-beta)*lam,0,beta]]

def determinant(beta,eta,kd,lam,z):
    M=matrix(beta,eta,kd,lam)
    return det4([[(z if i==j else 0)-M[i][j] for j in range(4)] for i in range(4)])

def factor(beta,eta,kd,lam,z):
    s=eta*lam
    q=beta+(1-beta)*kd*lam
    return z*(z-beta)*(z*z-(1+q-s)*z+q)

def roots(beta,eta,kd,lam):
    s=eta*lam
    q=beta+(1-beta)*kd*lam
    T=1+q-s
    d=cmath.sqrt(T*T-4*q)
    return (T+d)/2,(T-d)/2

for beta in (0.0,0.2,0.7,0.95):
    for lam in (0.3,1.0,4.0):
        for kd in (0.0,0.05,0.2):
            if kd*lam>=0.95:
                continue
            eta=0.23
            for z in (0.2,-0.7,1.3,0.4+0.9j,-1.1+0.3j):
                lhs=determinant(beta,eta,kd,lam,z)
                rhs=factor(beta,eta,kd,lam,z)
                assert abs(lhs-rhs)<2e-10*(1+abs(rhs))

for beta in (0.0,0.3,0.8,0.97):
    for lam in (0.5,1.0,3.0):
        for kdlam in (0.0,0.2,0.8):
            kd=kdlam/lam
            q=beta+(1-beta)*kdlam
            ceiling=2*(1+q)
            for frac in (0.01,0.3,0.9,0.999999):
                eta=frac*ceiling/lam
                r1,r2=roots(beta,eta,kd,lam)
                assert max(abs(r1),abs(r2),beta)<1+1e-10
            eta=1.000001*ceiling/lam
            r1,r2=roots(beta,eta,kd,lam)
            assert max(abs(r1),abs(r2),beta)>1

for beta in (0.1,0.6,0.9):
    L=5.0
    kd=0.7/L
    rhs=2*(1+beta+(1-beta)*kd*L)
    for frac in (0.4,0.99):
        eta=frac*rhs/L
        for j in range(1,501):
            lam=L*j/500
            r1,r2=roots(beta,eta,kd,lam)
            assert max(abs(r1),abs(r2),beta)<1+1e-10
    eta=1.001*rhs/L
    r1,r2=roots(beta,eta,kd,L)
    assert max(abs(r1),abs(r2),beta)>1

for beta in (0.0,0.25,0.8):
    lam=2.0
    for kdlam in (0.0,0.2,0.7):
        kd=kdlam/lam
        q=beta+(1-beta)*kdlam
        lo=(1-math.sqrt(q))**2
        hi=(1+math.sqrt(q))**2
        for s in (lo,(lo+hi)/2,hi):
            eta=s/lam
            r1,r2=roots(beta,eta,kd,lam)
            full=max(abs(r1),abs(r2),beta)
            assert abs(full-math.sqrt(q))<1e-6

print("verification passed")
