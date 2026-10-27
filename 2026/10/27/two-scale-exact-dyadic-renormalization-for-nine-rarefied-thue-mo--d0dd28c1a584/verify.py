#!/usr/bin/env python3
"""Exact finite matrix certificate and independent direct integer checks."""
from typing import List
N=9

def matmul(A,B):
    return [[sum(A[i][h]*B[h][j] for h in range(N)) for j in range(N)] for i in range(N)]

def times(A,v):
    return [sum(A[i][j]*v[j] for j in range(N)) for i in range(N)]

def prod_power(A,k):
    Q=[[int(i==j) for j in range(N)] for i in range(N)]
    for _ in range(k):Q=matmul(Q,A)
    return Q

B=[[0]*N for _ in range(N)]
for j in range(N):
    for r in (0,1):
        w=9*r+j
        B[j][w//2]+=1 if (w%2)==0 else -1

C=prod_power(B,6)
expected=[[3*int(i==j)+8*int(i%3==j%3)-3 for j in range(N)] for i in range(N)]
assert C==expected,(C,expected)
# Verify the spectral projectors exactly, no approximations.
Q=[[int(i%3==j%3) for j in range(N)] for i in range(N)]
assert matmul(Q,Q)==[[3*x for x in row] for row in Q]

v0=[1 if j.bit_count()%2==0 else -1 for j in range(N)]
v=v0
for k in range(1,19):
    v=times(B,v)
    assert sum(v)==0
    if k<=13:
        w=[sum(1 if (9*i+j).bit_count()%2==0 else -1 for i in range(1<<k)) for j in range(N)]
        assert w==v,(k,w,v)
    for m in (0,1,2,3):
        group=[sum(v[h] for h in range(j%3,N,3)) for j in range(N)]
        # 3^m v + (27^m-3^m)/3 Q v, exact integer numerator.
        numer=[3*(3**m)*v[j]+(27**m-3**m)*group[j] for j in range(N)]
        assert all(z%3==0 for z in numer)
        answer=[z//3 for z in numer]
        actual=v[:]
        for _ in range(6*m):actual=times(B,actual)
        assert answer==actual,(k,m,answer,actual)

# Two distinct scalar modes both occur already at k=1.
v1=times(B,v0)
g=[sum(v1[h] for h in range(j%3,N,3)) for j in range(N)]
assert any(x!=0 for x in g) and any(3*v1[j]!=g[j] for j in range(N))
# S(k+12)-30 S(k+6)+81 S(k)=0 is therefore minimal in 6-step shifts at k=1.
assert all(times(B,v0)[j]==[2,0,-2,2,-2,0,2,-2,0][j] for j in range(N))
print('VERIFIED: 9x9 exact matrix identity, independent direct sums k=1..13, all shifts k=1..18 and m=0..3, two nonzero modes')
