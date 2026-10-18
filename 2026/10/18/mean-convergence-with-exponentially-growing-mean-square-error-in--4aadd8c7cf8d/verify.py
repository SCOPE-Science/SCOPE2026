#!/usr/bin/env python3
"""Exact arithmetic certificates for the stated EControl counterexample."""
from fractions import Fraction as F

def mat(rows): return [[F(z) for z in row] for row in rows]
def mul(X,Y): return [[sum(X[i][k]*Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]
def add(X,Y): return [[X[i][j]+Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
def sub(X,Y): return [[X[i][j]-Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
def smul(a,X): return [[a*z for z in row] for row in X]
def T(X):return [list(row) for row in zip(*X)]
def eye(n):return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def det(X):
    if len(X)==1:return X[0][0]
    if len(X)==2:return X[0][0]*X[1][1]-X[0][1]*X[1][0]
    return sum((-1)**j*X[0][j]*det([row[:j]+row[j+1:] for row in X[1:]]) for j in range(len(X)))
def minors(X):return [det([row[:k] for row in X[:k]]) for k in (1,2,3)]
s=F(1,10)
A=mat([[1,-s,0],[0,1,0],[1,-1,1]])
def B(eta):return mat([[1-s,0,-s*eta],[1,0,eta],[0,0,1-eta]])
def avgadj(Q,eta):return smul(F(1,2),add(mul(mul(T(A),Q),A),mul(mul(T(B(eta)),Q),B(eta))))
W=smul(F(1,10**6),mat([[341000,-347500,171200],[-347500,366200,-148500],[171200,-148500,247000]]))
H=sub(avgadj(W,F(1)),smul(F(13,10),W))
Q=smul(F(1,9),mat([[1840,-1658,570],[-1658,1781,-452],[570,-452,395]]))
R=smul(F(1,99),mat([[1160,-112,10],[-112,212,7],[10,7,218]]))
M=smul(F(1,2),add(A,B(F(1))))
assert minors(W)==[F(341,1000),F(82359,20000000),F(27082717,62500000000)]
assert minors(H)==[F(6071,200000),F(1260269,40000000000),F(282727743,10**15)]
assert sub(Q,avgadj(Q,F(1,2)))==eye(3)
assert minors(Q)==[F(1840,9),F(528076,81),F(108358000,729)]
assert sub(R,mul(mul(T(M),R),M))==eye(3)
assert minors(R)==[F(1160,99),F(7072,297),F(15544,297)]
v0=mat([[1],[1],[0]])
assert mul(mul(T(v0),W),v0)==[[F(61,5000)]]
assert sum(W[i][i] for i in range(3))==F(4771,5000)
print('PASS: six exact matrix identities / definiteness certificates and initial norm')
