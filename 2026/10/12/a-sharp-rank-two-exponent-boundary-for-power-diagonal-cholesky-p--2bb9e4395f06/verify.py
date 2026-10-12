#!/usr/bin/env python3
"""Exact-arithmetic reproducibility checks for the power-diagonal pivot theorem."""
from fractions import Fraction as Q

def block_gain(m,t,beta):
    t=Q(t)
    return (t**(beta+2)+m**3)/(t**beta+m)

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def check_matrix(A,beta):
    n=len(A); d=[A[i][i] for i in range(n)]
    assert all(x>0 for x in d)
    sq=lambda M: sum(x*x for row in M for x in row)
    S=sq(A); den=sum(x**beta for x in d); residual=Q(0)
    for i in range(n):
        col=[A[j][i] for j in range(n)]
        B=[[A[j][k]-col[j]*col[k]/d[i] for k in range(n)] for j in range(n)]
        residual+=d[i]**beta*sq(B)/den
    return residual, S

def run():
    m=100;t=8;b=5
    g=block_gain(m,t,b)
    expected=Q(t*t+m*m)-g
    target=Q(m,m+1)*(t*t+m*m)
    assert g==Q(86032,913)
    assert expected==Q(9102400,913)
    assert target==Q(1006400,101)
    assert expected-target==Q(499200,92213)>0
    nchecked=0
    for m in (2,3,5,10):
        for t in (Q(1,3),Q(1),Q(3,2),Q(2),Q(3),Q(5),Q(11)):
            S=t*t+m*m
            for beta in (0,1,2,3,4):
                # The rank-two identity can be checked without instantiating huge matrices.
                E=(t**beta*m*m+m*t*t)/(t**beta+m)
                assert E==S-block_gain(m,t,beta)
                if beta<=4:assert E<=Q(m,m+1)*S
                nchecked+=1
            y=t*t
            p=y**3-m*y**2-y+m**3
            assert p>0
            assert block_gain(m,t,4)-S/Q(m+1)==m*p/((m+1)*(y*y+m))
    # Small exact PSD and PD matrices test the actual downdate identity.
    matrices=[
      [[Q(2),Q(1)],[Q(1),Q(2)]],
      [[Q(3),Q(0),Q(1)],[Q(0),Q(2),Q(1)],[Q(1),Q(1),Q(3)]],
      [[Q(5),Q(1,2)],[Q(1,2),Q(3)]],
      [[Q(1),Q(1),Q(0)],[Q(1),Q(1),Q(0)],[Q(0),Q(0),Q(2)]],
    ]
    for A in matrices:
        n=len(A)
        for beta in (0,1,2):
            E,S=check_matrix(A,beta)
            assert E<=Q(n-1,n)*S
            nchecked+=1
    for m in (2,3,5):
        for t in (Q(1,2),Q(2),Q(4)):
            A=[[Q(0) for _ in range(m+1)] for _ in range(m+1)]
            A[0][0]=t
            for i in range(1,m+1):
                for j in range(1,m+1):A[i][j]=Q(1)
            for beta in (0,1,2,3,4):
                E,S=check_matrix(A,beta)
                assert E==S-block_gain(m,t,beta)
                nchecked+=1
    print('VERIFY_OK',nchecked,'exact checks')
if __name__=='__main__': run()
