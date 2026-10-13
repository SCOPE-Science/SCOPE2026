#!/usr/bin/env python3
"""Exact-rational checks for two-period incremental momentum on scalar quadratics."""
from fractions import Fraction as F
from itertools import product

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def checks(a,b,beta,eta):
    U=1+beta
    A=[[U-eta*a,-beta],[F(1),F(0)]]
    B=[[U-eta*b,-beta],[F(1),F(0)]]
    P=matmul(B,A)
    tr=P[0][0]+P[1][1]
    det=P[0][0]*P[1][1]-P[0][1]*P[1][0]
    assert det == beta*beta
    assert tr == (U-eta*a)*(U-eta*b)-2*beta
    C=U*(a+b)/(a*b)
    Delta=U*U*(a-b)**2-4*a*b*(1-beta)**2
    j1=1-tr+det
    j2=1+tr+det
    assert j1==eta*a*b*(C-eta)
    assert j2==a*b*(eta-C/2)**2-Delta/(4*a*b)
    interval = 0<eta<C and (Delta<0 or (eta-C/2)**2>Delta/(4*a*a*b*b))
    assert (j1>0 and j2>0 and det<1)==interval
    for eta_res in (U/a,U/b):
        Ares=[[U-eta_res*a,-beta],[F(1),F(0)]]
        Bres=[[U-eta_res*b,-beta],[F(1),F(0)]]
        Pres=matmul(Bres,Ares)
        assert Pres[0][0]+Pres[1][1]==-2*beta
        assert Pres[0][0]*Pres[1][1]-Pres[0][1]*Pres[1][0]==beta*beta
        assert checks_simple_res(eta_res,a,b,beta)
    return interval

def checks_simple_res(eta,a,b,beta):
    return 0<eta<(1+beta)*(a+b)/(a*b) and ((1+beta-eta*a)*(1+beta-eta*b)+(1-beta)**2)>0

count=0
for ai,bi,betai,j in product((1,2,3,5,9),(1,2,3,5,9),(F(0),F(1,4),F(1,2),F(3,4)),range(1,51)):
    checks(F(ai),F(bi),betai,F(j,20));count+=1
assert checks(F(9),F(1),F(1,2),F(3,2))
assert not checks(F(9),F(1),F(1,2),F(1,2))
a,b,beta,eta=F(9),F(1),F(1,2),F(3,2)
A=[[1+beta-eta*a,-beta],[F(1),F(0)]]
B=[[1+beta-eta*b,-beta],[F(1),F(0)]]
P=matmul(B,A)
assert P==[[F(-1,2),F(0)],[F(-12),F(-1,2)]]
assert sum(P[i][i] for i in range(2)) == -1
print('VERIFY_OK',count,'exact rational cases plus resonances; explicit stable/unstable witnesses')
