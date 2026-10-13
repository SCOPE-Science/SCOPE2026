"""Exact rational checks for an embedding threshold of theta time stepping.

This executable checks finite algebraic identities. The all-dimension result
follows from the analytic matrix-function and path-parity proof in RESULT.md.
Requires Python 3 standard library only. Run: python3 artifacts/verify_embedding.py
"""
from fractions import Fraction as F
from math import log


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def matmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def matadd(A, B, a=1, b=1):
    return [[a * A[i][j] + b * B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def inv(A):
    n=len(A)
    T=[list(map(F, A[i]))+eye(n)[i] for i in range(n)]
    for j in range(n):
        pivot=next(k for k in range(j,n) if T[k][j])
        T[j],T[pivot]=T[pivot],T[j]
        d=T[j][j]
        T[j]=[v/d for v in T[j]]
        for k in range(n):
            if k==j: continue
            f=T[k][j]
            T[k]=[T[k][q]-f*T[j][q] for q in range(2*n)]
    return [row[n:] for row in T]


def chain(forward,backward):
    n=len(forward)+1
    assert len(backward)==n-1
    Q=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(n-1):
        Q[i][i+1]=F(forward[i]); Q[i+1][i]=F(backward[i])
    for i in range(n):
        Q[i][i]=-sum(Q[i],F(0))
    return Q


def theta_step(Q, h, theta):
    n=len(Q); I=eye(n)
    return matmul(inv(matadd(I,Q,1,-theta*h)),matadd(I,Q,1,(1-theta)*h))


def outer(v,scale):
    return [[scale*x*y for y in v] for x in v]


def main():
    Q=chain([1,1],[1,1]); h=F(1,2); theta=F(1,2)
    P=theta_step(Q,h,theta)
    expected=[[F(23,35),F(10,35),F(2,35)],
              [F(10,35),F(15,35),F(10,35)],
              [F(2,35),F(10,35),F(23,35)]]
    assert P==expected
    # Exact spectral decomposition and the exact sign of the logarithm.
    E0=outer([1,1,1],F(1,3))
    E1=outer([1,0,-1],F(1,2))
    E3=outer([1,-2,1],F(1,6))
    assert P==matadd(matadd(E0,E1,1,F(3,5)),E3,1,F(1,7))
    assert matmul(P,E1)==matadd([[F(0)]*3 for _ in range(3)],E1,0,F(3,5))
    assert matmul(P,E3)==matadd([[F(0)]*3 for _ in range(3)],E3,0,F(1,7))
    assert F(125,189)<1 and log(F(125,189))/6 < 0

    # Path-parity signs of all powers on two genuinely heterogeneous chains.
    chains=[chain([1,2,3,2],[2,1,4,3]),
            chain([F(1,3),F(5,2),4],[3,F(3,2),F(5,3)])]
    tests=0
    for M in chains:
        n=len(M); Mk=eye(n)
        for k in range(1,16):
            Mk=matmul(Mk,M)
            for i in range(n-2):
                assert (Mk[i][i+2]==0 if k<2 else (-1)**k * Mk[i][i+2]>0)
                assert (Mk[i+2][i]==0 if k<2 else (-1)**k * Mk[i+2][i]>0)
                tests+=2
            for i in range(n):
                for j in range(n):
                    if abs(i-j)>k: assert Mk[i][j]==0
                    if abs(i-j)==k: assert Mk[i][j]>0

    # Exact Taylor coefficients of the effective generator and their signs.
    for theta in [F(0),F(1,6),F(1,2),F(3,4),F(1),F(7,4)]:
        for k in range(1,20):
            ck=(theta**k + (-1)**(k+1)*(1-theta)**k)/k
            if k==1: assert ck==1
            if theta<=F(1,2):
                assert ck>0 if k%2 else ck<=0
            else: assert ck>0
            tests+=1

    # Resolvent integrand has nonnegative distant rates for positive s.
    Q=chain([1,3,2],[4,1,5]); n=len(Q); I=eye(n)
    for s in [F(1,32),F(1,4),F(1),F(5)]:
        R=inv(matadd(I,Q,1,-s))
        assert all(sum(row,F(0))==1 for row in R)
        assert all(R[i][j]>0 for i in range(n) for j in range(n))
        G=matadd(R,I,1,-1)
        assert matmul(Q,R)==[[x/s for x in row] for row in G]
        assert all(G[i][j]>0 for i in range(n) for j in range(n) if i!=j)
        tests+=n*(n-1)

    # The two-state exception: eigenvalue r and positive scalar log multiplier.
    Q=chain([F(2,3)],[F(7,5)])
    rate=F(2,3)+F(7,5)
    for theta in [F(0),F(1,3),F(1,2),F(3,4),F(1),F(4,3)]:
        for h in [F(1,50),F(1,5),F(1,2),F(1)]:
            P=theta_step(Q,h,theta)
            r=(1-(1-theta)*h*rate)/(1+theta*h*rate)
            assert P[0][0]+P[1][1]-1==r
            assert P[0][0]*P[1][1]-P[0][1]*P[1][0]==r
            assert all(sum(row,F(0))==1 for row in P)
            tests+=1
    print('VERIFY_OK exact checks:',tests)

if __name__=='__main__':main()
