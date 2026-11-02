"""Numerical and exact finite checks for one weighted complete-tripartite edge.
Usage: python verify_weighted_tripartite_edge.py (requires numpy).
Finite checks corroborate, rather than establish, the universal proof.
"""
import math
import numpy as np
from fractions import Fraction


def complete_adjacency(n):
    N = 3*n
    B=np.fromfunction(lambda i,j: (i//n != j//n).astype(int),(N,N),dtype=int)
    return B


def ttop(n,eta):
    b=3*n*n+(3*n-2)*eta
    return (b+math.sqrt(b*b-36*n*n*(n-1)*eta))/(6*n)


def gram_basis(n):
    N=3*n
    X=np.vstack([np.eye(N-1),-np.ones((1,N-1))])
    return np.linalg.qr(X, mode='reduced')[0]


def critical(n,t):
    lo=0.0
    hi=math.log2(n/(n-1))
    for _ in range(85):
        p=(lo+hi)/2
        a=2**p
        eta=math.expm1(p*math.log(t))/math.expm1(p*math.log(2))
        T=ttop(n,eta)
        # F(p)=2^p -(2^p-1)*T
        if a-(a-1)*T>0:lo=p
        else:hi=p
    return (lo+hi)/2


def run():
    num=0
    for n in range(2,21):
        B=complete_adjacency(n)
        Q=gram_basis(n)
        E=np.zeros_like(B,dtype=float)
        E[0,n]=E[n,0]=1
        for t in (1.05,1.2,1.5,1.85,2.0):
            p=critical(n,t)
            assert 0<p<math.log2(n/(n-1))
            a=2**p; b=t**p
            eta=(b-1)/(a-1)
            T=ttop(n,eta)
            compressed=Q.T@(B-eta*E)@Q
            eig=np.linalg.eigvalsh(compressed)
            assert abs(eig[0]+T)<1e-9
            assert eig[1]-eig[0]>1e-4
            D=a*(np.ones_like(B)-np.eye(3*n))+(1-a)*B+(b-1)*E
            Deig=np.linalg.eigvalsh(Q.T@D@Q)
            assert abs(Deig[-1])<2e-9
            assert Deig[-2]<-1e-4
            for c in (0.80,1.20):
                q=c*p
                aa=2**q; bb=t**q
                Dq=aa*(np.ones_like(B)-np.eye(3*n))+(1-aa)*B+(bb-1)*E
                top=np.linalg.eigvalsh(Q.T@Dq@Q)[-1]
                assert (top<0 if c<1 else top>0)
            num+=1
    print('FULL_WEIGHTED_METRIC_THRESHOLD_AND_SIMPLE_KERNEL_OK',num)

    count=0
    for n in range(2,15):
        B=complete_adjacency(n)
        E=np.zeros_like(B)
        E[0,n]=E[n,0]=1
        for eta in [Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)]:
            f=[((3*i+7*j)%11)-5 for j,i in enumerate(range(3*n-1))]
            f.append(-sum(f))
            sums=[sum(f[i*n:(i+1)*n]) for i in range(3)]
            lhs=sum(Fraction(f[i]*f[j])*(int(B[i,j])-eta*int(E[i,j])) for i in range(3*n) for j in range(3*n))
            rhs= -sum(v*v for v in sums)-2*eta*f[0]*f[n]
            assert lhs==rhs
            count+=1
    print('EXACT_RATIONAL_WEIGHTED_QUADRATIC_FORM_OK',count)

    for t in (1.15,1.5,1.95,2.0):
        target=math.log(t)/(3*math.log(2)**2)
        for n in (200,1000,2500):
            p=critical(n,t)
            q=math.log2(n/(n-1))
            # Direct subtraction at large n is acceptable for these finite diagnostics.
            assert abs(n**3*(q-p)-target)<0.02,(n,t,n**3*(q-p),target)
    print('CUBIC_WEIGHTED_EDGE_SENSITIVITY_OK')
    print('ALL_WEIGHTED_TRIPARTITE_EDGE_CHECKS_OK')


if __name__=='__main__':run()
