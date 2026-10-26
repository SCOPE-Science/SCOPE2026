"""Exact-rational tests for a two-state Padé transition calculation.

The infinitely-many-parameter theorem is established analytically; this code
checks polynomial identities and independently reconstructs rational matrices.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def inv2(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert d>0
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]


def pade_from_matrix(a,b,h):
    Q=[[-a,a],[b,-b]]
    H=[[h*Q[i][j] for j in range(2)] for i in range(2)]
    HH=matmul(H,H)
    N=[[F(int(i==j))+H[i][j]/3 for j in range(2)] for i in range(2)]
    D=[[F(int(i==j))-F(2,3)*H[i][j]+HH[i][j]/6 for j in range(2)] for i in range(2)]
    return matmul(inv2(D),N)


def pade_s(s):
    return (6-2*s)/(s*s+4*s+6)


def projected(a,b,h):
    l=a+b
    r=pade_s(h*l)
    pi1=b/l
    pi2=a/l
    return [[pi1+r*pi2,pi2*(1-r)], [pi1*(1-r),pi2+r*pi1]]


def positivity_by_quadratic(a,b,h):
    l=a+b
    m=min(a,b)/l
    s=h*l
    return m*s*s+(6*m-2)*s+6>=0


count=0
for a,b,h in product([F(1,37),F(1,10),F(1),F(2),F(9),F(19),F(42)],
                     [F(1,23),F(1,2),F(1),F(4),F(13),F(31)],
                     [F(i,11) for i in range(0,77)]+[F(1,333),F(50),F(500)]):
    P=pade_from_matrix(a,b,h)
    X=projected(a,b,h)
    assert P==X
    assert all(sum(row)==1 for row in P)
    assert (all(v>=0 for row in P for v in row))==positivity_by_quadratic(a,b,h)
    r=pade_s(h*(a+b))
    assert -1<r<=1
    P2=matmul(P,P)
    # Every double step is a stochastic transition even when a single step is not.
    assert all(x>=0 for row in P2 for x in row)
    if h>0: assert all(x>0 for row in P2 for x in row)
    count+=1

# Critical identity from exact formulas, and a nontrivial rational witness.
a,b=F(19),F(1)
for h in [F(0),F(1,5),F(1),F(3,2),F(2)]:
    P=pade_from_matrix(a,b,h)
    assert (P[0][0]>=0)==(h<=F(1,5) or h>=F(3,2))
assert pade_from_matrix(a,b,F(1,5))==pade_from_matrix(a,b,F(3,2))
assert pade_from_matrix(a,b,F(1))[0][0]==-F(4,243)

mc=(2-sqrt(3))/3
scrit=3+3*sqrt(3)
rcrit=float(pade_s(scrit))
assert abs(rcrit+mc/(1-mc))<1e-13
assert abs((9*mc*mc-12*mc+1))<1e-13
assert abs(float(pade_s(F(3)))+0)<1e-14
assert abs(float(pade_s(F(1))) - F(4,11))<1e-14
print('PASS:',count,'direct 2x2 exact matrix reconstructions, mass/positivity, two-step checks; exact witness and critical constants')
