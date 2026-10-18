#!/usr/bin/env python3
"""Direct deterministic checks of the critical DGDA step law in real arithmetic."""
from math import sqrt, isclose
from cmath import sqrt as csqrt
from fractions import Fraction


def mul(A,B):
    return [[sum(A[i][t]*B[t][j] for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def adj(A):
    return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]

def power(A,k):
    o=[[complex(i==j) for j in range(len(A))] for i in range(len(A))]
    for _ in range(k):
        o=mul(o,A)
    return o

def opnorm_sq_2(A):
    H=mul(adj(A), A)
    tr=(H[0][0]+H[1][1]).real
    det=(H[0][0]*H[1][1]-H[0][1]*H[1][0]).real
    return (tr+sqrt(max(0,tr*tr-4*det)))/2

B=[[.5-1j,.5],[.5,.5]]
lam=(1-1j)/2
N=[[B[i][j]-lam*(i==j) for j in range(2)] for i in range(2)]
assert all(abs(v)<1e-13 for row in mul(N,N) for v in row)
assert abs(opnorm_sq_2(N)-1)<1e-13
count=2
for k in range(0,41):
    P=power(B,k)
    v=2**(-k)*(1+k*k+k*sqrt(k*k+2))
    actual=opnorm_sq_2(P)
    assert isclose(v,actual,rel_tol=2e-11,abs_tol=1e-11), (k,v,actual)
    W=[sum(P[i][j] for j in range(2)) for i in range(2)]
    # Synchronized starting state (z,z), normalized z=1
    assert abs(abs(W[0])**2-(k+1)**2/(2**k))<1e-10
    assert abs((abs(W[0])**2+abs(W[1])**2)/(2)-(1+k+k*k)/(2**k))<1e-10
    assert abs(W[0]-(k+1)*lam**k)<1e-10
    count+=4
assert 3*sqrt(11)>4*sqrt(6)
assert all((2*k*k+2)/(2**k)<=34/16 for k in range(4,200))
assert all(((k+1)**2)/(2**k)<=Fraction(9,4) for k in range(0,200))
count+=3
# Real 4x4 isometric complexification of one scalar bilinear game, comparing powers via norm of explicit vector.
T=[[.5,1,.5,0],[-1,.5,0,.5],[.5,0,.5,0],[0,.5,0,.5]]
for z0 in [(1.,0.),(.6,-.8)]:
    x=[z0[0],z0[1],z0[0],z0[1]]
    for k in range(20):
        expected=(k+1)**2/(2**k)*(z0[0]**2+z0[1]**2)
        assert abs(x[0]**2+x[1]**2-expected)<1e-10,(k,x,expected)
        x=[sum(T[i][j]*x[j] for j in range(4)) for i in range(4)]
        count+=1
print(f'PASS: {count} deterministic identities; exact Jordan and peak arguments are in RESULT.md')
