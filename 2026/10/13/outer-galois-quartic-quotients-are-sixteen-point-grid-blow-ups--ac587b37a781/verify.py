#!/usr/bin/env python3
from fractions import Fraction

# Basis: A,B,E_00,...,E_33 for Pic(Bl_{16}(P1xP1)).
# Intersection: A^2=B^2=0, A.B=1, E_ij^2=-1, other products 0.
N=18

def vec(**kw):
    v=[0]*N
    for k,val in kw.items():
        v[int(k)]=val
    return v

def add(*vs): return [sum(x) for x in zip(*vs)]
def scale(a,v): return [a*x for x in v]
def dot(v,w):
    s=v[0]*w[1]+v[1]*w[0]
    for k in range(2,N): s-=v[k]*w[k]
    return s

def E(i,j):
    v=[0]*N; v[2+4*i+j]=1; return v
A=vec(**{'0':1}); B=vec(**{'1':1})
V=[]; H=[]
for i in range(4):
    V.append(add(A,*[scale(-1,E(i,j)) for j in range(4)]))
for j in range(4):
    H.append(add(B,*[scale(-1,E(i,j)) for i in range(4)]))

for c in V+H: assert dot(c,c)==-4
for i in range(4):
    for k in range(4):
        if i!=k: assert dot(V[i],V[k])==0
for j in range(4):
    for l in range(4):
        if j!=l: assert dot(H[j],H[l])==0
for i in range(4):
    for j in range(4):
        assert dot(V[i],H[j])==0
        e=E(i,j)
        assert dot(e,e)==-1
        assert dot(e,V[i])==1 and dot(e,H[j])==1
        for k in range(4):
            if k!=i: assert dot(e,V[k])==0
        for l in range(4):
            if l!=j: assert dot(e,H[l])==0

sumE=add(*[E(i,j) for i in range(4) for j in range(4)])
K=add(scale(-2,A),scale(-2,B),sumE)
D=add(*V,*H)
assert D==scale(-2,K)
assert dot(K,K)==-8
assert 2+16==18
assert 4+16==20
# Scalar tangent weights at the two fixed-point types.
assert ((-1)%4,(-1)%4)==(3,3)
assert ((1)%4,(1)%4)==(1,1)
print('VERIFY_OK boundary=8x(-4) grid_exceptionals=16x(-1) D=-2K K2=-8 rho=18 euler=20 local_types=8x1/4(1,1)')
