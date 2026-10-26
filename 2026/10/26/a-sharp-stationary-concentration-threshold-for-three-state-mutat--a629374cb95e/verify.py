#!/usr/bin/env python3
"""Exact-rational consistency tests for three-state no-holding spectral identities."""
from fractions import Fraction as F
from itertools import product
from math import isclose, sqrt


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def determinant(P):
    return P[0][1]*P[1][2]*P[2][0]+P[0][2]*P[1][0]*P[2][1]


def construct(pi, J):
    L = [1-2*x for x in pi]
    Fij = [[F(0)] * 3 for _ in range(3)]
    for a,b,k in [(0,1,2),(1,2,0),(2,0,1)]:
        Fij[a][b]=(L[k]+J)/2
        Fij[b][a]=(L[k]-J)/2
    return [[Fij[i][j]/pi[i] for j in range(3)] for i in range(3)]


def test():
    count=0
    for N in range(7,36):
        for a in range(1,N):
            for b in range(1,N-a):
                c=N-a-b
                pi=[F(a,N),F(b,N),F(c,N)]
                if min(pi)<=0 or max(pi)>=F(1,2):
                    continue
                U=pi[0]*pi[1]*pi[2]
                L=[1-2*x for x in pi]
                G=U-L[0]*L[1]*L[2]
                p=max(pi); Jmax=1-2*p
                assert G>=0
                assert Jmax*Jmax-G == (4-9*p)*U/p
                for w in [-1,F(-1,2),F(0),F(1,2),F(1)]:
                    J=Jmax*w
                    P=construct(pi,J)
                    assert all(P[i][i]==0 for i in range(3))
                    assert all(P[i][j]>=0 for i in range(3) for j in range(3))
                    assert all(sum(P[i])==1 for i in range(3))
                    assert all(sum(pi[i]*P[i][j] for i in range(3))==pi[j] for j in range(3))
                    det=determinant(P)
                    assert det==(L[0]*L[1]*L[2]+J*J)/(4*U)
                    delta=1-4*det
                    assert delta==(G-J*J)/U
                    # Characteristic polynomial: (z-1)(z^2+z+det P).
                    assert P[0][0]+P[1][1]+P[2][2]==0
                    trP2=sum(matmul(P,P)[i][i] for i in range(3))
                    assert trP2==2-2*det
                    count+=11
                Rstar = .5 if p<=F(4,9) else (1+sqrt(9-4/float(p)))/2
                candidates=[-float(Jmax), float(Jmax)]
                if G<=Jmax**2:
                    candidates.extend([-sqrt(float(G)), sqrt(float(G))])
                rbest=float('inf')
                for j in candidates:
                    detval=float((L[0]*L[1]*L[2]+F.from_float(j*j))/(4*U))
                    disc=1-4*detval
                    rr=(1+sqrt(disc))/2 if disc>=0 else sqrt(detval)
                    rbest=min(rr,rbest)
                assert abs(rbest-Rstar)<1e-7, (pi, Jmax, rbest, Rstar)
                count+=2
    return count

if __name__=='__main__':
    print('Exact spectral identities and boundaries:',test(),'checks passed')
