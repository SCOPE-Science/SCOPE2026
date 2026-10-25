#!/usr/bin/env python3
"""Reproduce exact quartic matrix distances and sample fixed-trace identities."""
import random
import math

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def tr(A):
    return A[0][0]+A[1][1]
def fourth(A,B):
    return tr(mul(mul(mul(A,A),A),A))+tr(mul(mul(mul(B,B),B),B))-2*tr(mul(mul(mul(A,B),A),B))
def dot(u,v):
    return sum(a*b for a,b in zip(u,v))
def dist2(x,y,t):
    v=[a-b for a,b in zip(x,y)]
    w=[a+b for a,b in zip(x,y)]
    return 2*dot(v,v)*(4*t*t+dot(w,w))
A=[[2,2],[2,2]]
B=[[2,0],[0,1]]
C=[[2,0],[0,0]]
assert fourth(A,C)==240 and fourth(A,B)==201 and fourth(B,C)==1
assert 19*19>201
R=random.Random(20261020)
for k in range(5000):
    t=R.uniform(.2,4)
    pts=[]
    for _ in range(3):
        z=[R.uniform(-1,1) for j in range(3)]
        l=math.sqrt(dot(z,z))
        factor=t*R.random()/l
        pts.append([factor*u for u in z])
    x,y,z=pts
    def pauli(v):
        return [[t+v[2],v[0]-1j*v[1]],[v[0]+1j*v[1],t-v[2]]]
    direct=fourth(pauli(x),pauli(y))
    formula=dist2(x,y,t)
    assert abs(direct-formula)<=1e-9*(1+formula)
    # Exact two-by-two trace-four formula from Pauli multiplication:
    # for tI+u.sigma, the Pauli polynomial trace identities reduce to dist2.
    lhs=math.sqrt(dist2(x,z,t))
    rhs=math.sqrt(dist2(x,y,t))+math.sqrt(dist2(y,z,t))
    assert lhs<=rhs+1e-11*(1+lhs+rhs)
print('PASS: three integer squared distances, strict inequality, 5000 triangle diagnostics')
