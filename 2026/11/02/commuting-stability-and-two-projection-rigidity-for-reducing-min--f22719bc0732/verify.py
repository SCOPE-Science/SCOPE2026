"""Finite exact and numerical checks for projection-mixture identities.
Analytic statements about infinite-dimensional operators are established in the proof, not by this script.
"""
from fractions import Fraction as F
from math import sin,sqrt

N=0

def check(assertion):
    global N
    assert assertion
    N+=1

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def sub(A,B):
    return [[A[i][j]-B[i][j] for j in range(2)] for i in range(2)]

angles=[(F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(8,17),F(15,17)),(F(1),F(0)),(F(0),F(1))]
weights=[F(1,9),F(2,7),F(1,2),F(5,7),F(8,9)]
P=[[F(1),F(0)],[F(0),F(0)]]
for c,s in angles:
    Q=[[c*c,c*s],[c*s,s*s]]
    check(mul(Q,Q)==Q)
    D=sub(P,Q)
    DD=mul(D,D)
    check(DD==[[s*s,F(0)],[F(0),s*s]])
    for t in weights:
        A=[[t*P[i][j]+(1-t)*Q[i][j] for j in range(2)] for i in range(2)]
        check(A[0][0]+A[1][1]==1)
        check(A[0][0]*A[1][1]-A[0][1]*A[1][0] == t*(1-t)*s*s)
        left=sub(mul(A,A),A)
        check(left==[[-t*(1-t)*DD[i][j] for j in range(2)] for i in range(2)])

for tau in (1e-1,1e-2,1e-3):
    for t in (.1,.25,.5,.75,.9):
        previous=1.
        for n in range(1,70):
            sn=sin(tau*2.**(-n))
            z=4*t*(1-t)*sn*sn
            lower=(2*t*(1-t)*sn*sn)/(1+sqrt(1-z))
            check(0<lower<previous)
            previous=lower
print('Finite verification assertions passed:',N)
