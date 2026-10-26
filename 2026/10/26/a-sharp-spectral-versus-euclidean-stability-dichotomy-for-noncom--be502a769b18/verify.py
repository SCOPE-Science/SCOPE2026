#!/usr/bin/env python3
"""Reproduce the exact 2x2 certificate and sample the sharp bounds.

Requires only the Python standard library. Finite checks do not replace the proof.
"""
from fractions import Fraction as Q
from math import exp, log, sqrt


def mul(A, B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]


def norm_sq_2(M):
    a,b=M[0]; c,d=M[1]
    tr=a*a+b*b+c*c+d*d
    det=(a*d-b*c)**2
    return (tr+sqrt(max(0.,tr*tr-4*det)))/2

# All entries below are exactly rational because the step is log(2).
H=[[Q(4),Q(0)],[Q(0),Q(1)]]
K=[[Q(4),-Q(9,5)],[-Q(9,5),Q(1)]]
W=[[Q(15,64),Q(0)],[Q(0),Q(1,2)]]
S=[[int(i==j)-v for j,v in enumerate(row)] for i,row in enumerate(mul(W,K))]
assert S==[[Q(1,16),Q(27,64)],[Q(9,10),Q(1,2)]]
assert H[0][0]*H[1][1]>0
assert K[0][0]>0 and K[0][0]*K[1][1]-K[0][1]**2==Q(19,25)
D=[[2*H[i][j]-K[i][j] for j in range(2)] for i in range(2)]
assert D[0][0]>0 and D[0][0]*D[1][1]-D[0][1]**2==Q(19,25)
v=[Q(1),Q(1)]
y=[sum(S[i][j]*v[j] for j in range(2)) for i in range(2)]
quot=sum(z*z for z in y)/Q(2)
assert y==[Q(31,64),Q(7,5)]
assert quot==Q(224729,204800)>1
print('EXACT rational nonexpansion counterexample:',quot)

count=0
for kap in [1.,1.1,1.5,2.,4.,8.,25.,100.]:
    for h in [0.001,0.1,0.5,1.,2.,5.,25.]:
        for eta in [0.0,0.3,0.7,0.9,0.99,0.999]:
            d1=-__import__('math').expm1(-kap*h)
            d2=-__import__('math').expm1(-h)
            S0=[[1-d1,eta*d1/sqrt(kap)],[eta*d2*sqrt(kap),1-d2]]
            frobsq=norm_sq_2(S0)
            assert frobsq<=kap+1e-11,(kap,h,eta,frobsq)
            # K is H^1/2 [[1,-eta],[-eta,1]] H^1/2.
            # Both K and 2H-K are SPD when 0<=eta<1.
            # Check K-norm via B=K^1/2 W K^1/2 by trace/determinant
            tr=(d1+d2)
            det=d1*d2*(1-eta*eta)
            lamhi=(tr+sqrt(max(0.,tr*tr-4*det)))/2
            lamlo=(tr-sqrt(max(0.,tr*tr-4*det)))/2
            assert -1e-12<lamlo and lamhi<2+1e-12
            assert max(abs(1-lamlo),abs(1-lamhi))<=1+1e-11
            count+=1
print('PASS',count,'deterministic SPD parameter checks, in addition to exact rational certificate')
