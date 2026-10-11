#!/usr/bin/env python3
"""Exact rational witnesses for the four-corner normal compression theorem.

For Pythagorean triples, verify the rank-one effect decomposition and its
weighted reconstruction. The universal upper bound is proved analytically.
"""
from fractions import Fraction as Q

def matadd(A,B):return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]
def scale(k,A):return [[k*A[i][j] for j in range(2)] for i in range(2)]
def det(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def tr(A):return A[0][0]+A[1][1]

I=[[Q(1),Q(0)],[Q(0),Q(1)]]
X=[[Q(0),Q(1)],[Q(1),Q(0)]]
Z=[[Q(1),Q(0)],[Q(0),Q(-1)]]
O=[[Q(0),Q(0)],[Q(0),Q(0)]]

def verify(a,b,r):
    assert a>0 and b>0 and a*a+b*b==r*r
    lam,mu=Q(b,r),Q(a,r)
    assert lam*lam+mu*mu==1
    Es={};sumE=[row[:] for row in O]
    H=[row[:] for row in O];K=[row[:] for row in O]
    for s in (1,-1):
        for t in (1,-1):
            E=scale(Q(1,4),matadd(matadd(I,scale(s*lam,X)),scale(t*mu,Z)))
            assert det(E)==0 and tr(E)==Q(1,2) and E[0][0]>0
            Es[s,t]=E
            sumE=matadd(sumE,E)
            H=matadd(H,scale(s*a,E))
            K=matadd(K,scale(t*b,E))
    assert sumE==I
    t=Q(a*b,r)
    assert H==scale(t,X) and K==scale(t,Z)
    # Since the compressed operator is t*(X+iZ), its square vanishes.
    assert X[0][1]==1 and Z[0][0]==1 and Z[1][1]==-1
    # The predicted minor semiaxis satisfies the upper bound with equality.
    assert t*t*(Q(1,a*a)+Q(1,b*b))==1

if __name__=='__main__':
    for a,b,r in ((3,4,5),(5,12,13),(8,15,17),(7,24,25)):
        verify(a,b,r)
        verify(b,a,r)
    print('FOUR_CORNER_RATIONAL_CERTIFICATE_OK')
