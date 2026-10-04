#!/usr/bin/env python3
from fractions import Fraction

def dot(u,v):
    return sum(a*b for a,b in zip(u,v))

def matvec(B,z):
    return [sum(B[i][j]*z[j] for j in range(len(z))) for i in range(len(B))]

def q(B,z):
    return dot(matvec(B,z),z)

def Q(B,z1,z2):
    return q(B,z1)+q(B,z2)

B0=[[0,0],[0,0]]
assert Q(B0,[1,0],[0,0])==0

K=[[0,-1],[1,0]]
for z in ([1,0],[0,1],[2,-3],[5,7]):
    assert q(K,z)==0

Bi=[[1,0],[0,-1]]
e1=[1,0]
e2=[0,1]
assert q(Bi,e1)==1
assert q(Bi,e2)==-1
assert Q(Bi,e1,e2)==0

Bc=[[2,0],[0,1]]
for z in ([1,0],[0,1],[2,-3],[-5,4]):
    assert q(Bc,z)>=dot(z,z)

for n in (1,2,5,10,100,1000):
    denominator=Fraction(1,n)
    numerator=Fraction(1,1)
    assert numerator/denominator==n

print("VERIFY_OK")
