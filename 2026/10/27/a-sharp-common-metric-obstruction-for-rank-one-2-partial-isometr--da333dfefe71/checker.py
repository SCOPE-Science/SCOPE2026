"""Reproduce exact finite-dimensional identities and sample the rank-one metric threshold.

No external dependencies. The proof of the universal theorem is in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt

# Exact real quadratic field Q(sqrt(7)).
def a(q=0, r=0): return (F(q), F(r))
def plus(x, y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0], -x[1])
def mul(x, y): return (x[0]*y[0]+7*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def smul(q, x): return (F(q)*x[0], F(q)*x[1])
def mm(X, Y): return [[plus(mul(X[i][0],Y[0][j]),mul(X[i][1],Y[1][j])) for j in range(2)] for i in range(2)]
def transpose(X): return [[X[j][i] for j in range(2)] for i in range(2)]
def madd(X, Y): return [[plus(X[i][j],Y[i][j]) for j in range(2)] for i in range(2)]
def mscale(q, X): return [[smul(q,X[i][j]) for j in range(2)] for i in range(2)]
def mneg(X): return mscale(-1, X)
Z=a(); one=a(1)
I=[[one,Z],[Z,one]]
T=[[a(0,F(1,2)),Z],[a(F(3,2)),Z]]
Tstar=transpose(T)
T2=mm(T,T)
beta=madd(madd(mm(transpose(T2),T2),mneg(mscale(2,mm(Tstar,T)))),I)
S=madd(mscale(2,Tstar),mneg(mm(mm(Tstar,Tstar),T)))
P=mm(S,T)
Q=mm(T,S)
assert beta==[[Z,Z],[Z,one]]
assert mm(T,beta)==[[Z,Z],[Z,Z]]
assert S==[[a(0,-1),a(3)],[Z,Z]]
assert P==[[one,Z],[Z,Z]]
assert Q==[[a(F(-7,2)),a(0,F(3,2))],[a(0,F(-3,2)),a(F(9,2))]]
assert mm(P,P)==P and mm(Q,Q)==Q
assert mm(mm(T,S),T)==T and mm(mm(S,T),S)==S
assert Q[0][1] == neg(Q[1][0]) and Q[0][1] != Z
# Every positive metric satisfying GP=P*G is diagonal; GQ=Q*G
# would force g11 * positive = g22 * negative, impossible.

def mm_float(X,Y):return [[sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def trans_float(X):return [[X[j][i] for j in range(2)] for i in range(2)]
N=0
for x in [0.5,0.51,0.7,0.9,1.,1.1,1.5,1.9,1.999,2.,2.1,3.,4.,10.]:
    c=sqrt(2*x-1)/x
    s=abs(x-1)/x
    TT=[[sqrt(x)*c,0.],[sqrt(x)*s,0.]]
    TS=mm_float(TT,[[sqrt(x)*(2-x)*c,2*sqrt(x)*s],[0.,0.]])
    if x<2:
        G=[[2-x,0.],[0.,2.]]
        GX=mm_float(G,TS)
        assert max(abs(GX[i][j]-GX[j][i]) for i in range(2) for j in range(2)) < 2.e-13
        assert 2-x>0
    else:
        assert c*s > 1.e-8
        assert TS[0][1]>0 and TS[1][0]<=0
    N+=1
print('PASS: exact Q(sqrt(7)) identities; rank-one metric threshold sampled in',N,'cases')
