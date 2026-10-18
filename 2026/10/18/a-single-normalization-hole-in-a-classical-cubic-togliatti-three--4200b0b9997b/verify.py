#!/usr/bin/env python3
"""Exact finite consistency tests for a 12-monomial cubic toric embedding.

The all-degree saturation proof is mathematical and is given in RESULT.md.
This checker tests its finite combinatorial identities independently.
"""
from itertools import product, combinations_with_replacement, permutations
from math import comb


def det3(v, w, u):
    return v[0] * (w[1]*u[2]-w[2]*u[1]) - v[1]*(w[0]*u[2]-w[2]*u[0]) + v[2]*(w[0]*u[1]-w[1]*u[0])


def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def scaled(v,n):
    return tuple(n*x for x in v)


A = set()
for i,j in permutations(range(3),2):
    v=[0,0,0];v[i]=2;v[j]=1;A.add(tuple(v))
for i,j in combinations_with_replacement(range(3),2):
    v=[0,0,0];v[i]+=1;v[j]+=1;A.add(tuple(v))
assert len(A)==12
m=(1,1,1)
B = {p for p in product(range(3),repeat=3) if 2 <= sum(p) <= 3}
assert B-A=={m} and not (A-B)
assert abs(det3((-1,1,0),(-1,0,1),(0,1,0)))==1

A2 = {add(a,b) for a in A for b in A}
for p in B:
    assert add(p,m) in A2

# Central octahedron of a unit cube is four lattice-unimodular tetrahedra.
base=(1,0,0); other=(0,1,1)
cyclic=[(0,1,0),(1,1,0),(1,0,1),(0,0,1)]
for j in range(4):
    v,w=cyclic[j],cyclic[(j+1)%4]
    assert abs(det3(sub(other,base),sub(v,base),sub(w,base)))==1
# Sum 0..1 and sum 2..3 slices of a unit cube are unimodular tetrahedra.
assert abs(det3((1,0,0),(0,1,0),(0,0,1)))==1

S={(0,0,0)}
for d in range(1,9):
    S = {add(a,b) for a in S for b in A}
    P={p for p in product(range(2*d+1),repeat=3) if 2*d<=sum(p)<=3*d}
    expected=comb(3*d+3,3)-3*comb(d+2,3)-comb(2*d+2,3)
    assert len(P)==expected,(d,len(P),expected)
    assert P-S == ({m} if d==1 else set()),(d,P-S)
    assert S <= P
    print('degree',d,'R dimension',len(S),'normal dimension',len(P))

# Ehrhart h-star numerator 1+9t+6t^2.  Remove the unique degree-one hole.
for d in range(0,9):
    H=sum((1,9,6)[j]*comb(d-j+3,3) for j in range(min(d,2)+1))-(d==1)
    expected=1 if d==0 else comb(3*d+3,3)-3*comb(d+2,3)-comb(2*d+2,3)-(d==1)
    assert H==expected
print('Hilbert numerator: [1, 8, 10, -6, 4, -1]')
print('normalization quotient: one missing degree-one lattice monomial')
print('VERIFY_OK')
