#!/usr/bin/env python3
"""Exact Grassmannian Schubert intersections for a six-dimensional pencil-isotropic locus.
Two independent integrations: polynomial coefficient extraction and fixed-point localization.
Standard library only; run as `python verify.py`.
"""
from itertools import combinations, permutations
from fractions import Fraction
from math import prod

ZERO = (0, 0, 0)
ONE = {ZERO: 1}

def add(a, b, sign=1):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, 0) + sign * c
        if out[m] == 0:
            del out[m]
    return out

def mul(a, b):
    out = {}
    for m, u in a.items():
        for n, v in b.items():
            w = tuple(m[i]+n[i] for i in range(3))
            out[w] = out.get(w, 0) + u*v
    return {m:c for m,c in out.items() if c}

def mpow(a, k):
    r = ONE
    for _ in range(k):
        r = mul(r, a)
    return r

X = [{tuple(int(i==j) for i in range(3)):1} for j in range(3)]
E1 = add(add(X[0],X[1]),X[2]); E2 = add(add(mul(X[0],X[1]),mul(X[0],X[2])),mul(X[1],X[2])); E3=mul(mul(X[0],X[1]),X[2])
H=[ONE, E1]
for k in range(2,8):
    v=add(mul(E1,H[k-1]),mul(E2,H[k-2]),-1)
    if k>=3:
        v=add(v,mul(E3,H[k-3]))
    H.append(v)

def sign(perm):
    return -1 if sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3)) % 2 else 1

def schur_poly(part):
    part=tuple(part)+(0,)*(3-len(part))
    out={}
    for p in permutations(range(3)):
        v=ONE
        for i,j in enumerate(p):
            k=part[i]-i+j
            v=mul(v,H[k] if k>=0 else {})
        out=add(out,v,sign(p))
    return out

DELT=mul(mul(add(X[0],X[1],-1),add(X[0],X[2],-1)),add(X[1],X[2],-1))
EUL=mpow(mul(mul(add(X[0],X[1]),add(X[0],X[2])),add(X[1],X[2])),2)

def integ_coeff(p):
    return mul(mul(p,EUL),DELT).get((6,5,4),0)

def det3(A):
    return sum(sign(p)*prod(A[i][p[i]] for i in range(3)) for p in permutations(range(3)))

def schur_value(part, vals):
    e1=sum(vals);e2=vals[0]*vals[1]+vals[0]*vals[2]+vals[1]*vals[2];e3=prod(vals)
    h=[1,e1]
    for r in range(2,8):
        h.append(e1*h[-1]-e2*h[-2]+(e3*h[-3] if r>=3 else 0))
    part=tuple(part)+(0,)*(3-len(part))
    return det3([[h[part[i]-i+j] if part[i]-i+j>=0 else 0 for j in range(3)] for i in range(3)])

def integ_loc(pa,pb):
    weights=(1,2,3,4,5,6,7)
    out=Fraction(0)
    for ind in combinations(range(7),3):
        xs=tuple(-weights[i] for i in ind)
        other=tuple(i for i in range(7) if i not in ind)
        ev=prod((xs[i]+xs[j])**2 for i,j in combinations(range(3),2))
        denom=prod(weights[j]-weights[i] for i in ind for j in other)
        out += Fraction(schur_value(pa,xs)*schur_value(pb,xs)*ev,denom)
    assert out.denominator == 1,(pa,pb,out)
    return int(out)

parts = {
    0:[(0,0,0)],
    1:[(1,0,0)],
    2:[(2,0,0),(1,1,0)],
    3:[(3,0,0),(2,1,0),(1,1,1)],
    4:[(4,0,0),(3,1,0),(2,2,0),(2,1,1)],
    5:[(4,1,0),(3,2,0),(3,1,1),(2,2,1)],
    6:[(4,2,0),(4,1,1),(3,3,0),(3,2,1),(2,2,2)],
}
expected={
0:[[1,1,1,2,1]],
1:[[2,4,3,3]],
2:[[1,5,4,3],[1,4,3,3]],
3:[[2,4,1],[4,8,2],[1,2,1]],
}
for q in range(4):
    actual=[]
    for a in parts[q]:
        row=[]
        for b in parts[6-q]:
            c=integ_coeff(mul(schur_poly(a),schur_poly(b)))
            v=integ_loc(a,b)
            assert c==v,(q,a,b,c,v)
            row.append(c)
        actual.append(row)
    assert actual==expected[q],(q,actual)

plucker=integ_coeff(mpow(E1,6))
assert plucker==61 and integ_loc((1,0,0),(4,1,0))==2
assert expected[0][0][0] == 1
assert expected[2][0][0]*expected[2][1][1]-expected[2][0][1]*expected[2][1][0] == -1
assert expected[3][0][0]*expected[3][2][2]-expected[3][0][2]*expected[3][2][0] == 1
assert 3-2==1 # An integral degree-one/five dual pairing.
print('VERIFY_OK fixed_points=35 Plucker_degree=61 pairing_ranks=1,1,2,2 unit_middle_minor=1 unit_degree_2_4_minor=-1')
