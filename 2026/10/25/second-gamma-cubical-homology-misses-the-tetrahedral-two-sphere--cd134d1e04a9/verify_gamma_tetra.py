#!/usr/bin/env python3
"""Finite integral certificate for second Gamma-cubical homology of four triple hyperedges.
Run: python3 verify_gamma_tetra.py gamma_tetra_certificate.json
Uses Python's exact integers, no external packages.
"""
import json, sys
from collections import defaultdict
from itertools import product

CERT = sys.argv[1] if len(sys.argv)>1 else 'gamma_tetra_certificate.json'
with open(CERT,encoding='utf-8') as stream:
    data=json.load(stream)
assert data['schema_version']==1 and data['vertices']==[0,1,2,3]
selected=data['selected_cubes']
assert len(selected)==219

# A cube is ordered by bit-index: 00, 10, 01, 11 in dimension two.
def face(cube,n,coordinate,fixed):
    result=[]
    for smaller in range(1<<(n-1)):
        source=(smaller&((1<<coordinate)-1)) | ((smaller>>coordinate)<<(coordinate+1)) | (fixed<<coordinate)
        result.append(cube[source])
    return tuple(result)

def nondegenerate(cube,n):
    return all(any(cube[i]!=cube[i^(1<<j)] for i in range(1<<n)) for j in range(n))

def valid_three(cube):
    return all(len({cube[i]} | {cube[i^(1<<j)] for j in range(3)})<=3 for i in range(8))

basis1=[c for c in product(range(4),repeat=2) if nondegenerate(c,1)]
basis2=[c for c in product(range(4),repeat=4) if nondegenerate(c,2)]
index1={t:i for i,t in enumerate(basis1)}
index2={t:i for i,t in enumerate(basis2)}
assert len(basis1)==12 and len(basis2)==228

def cubical_boundary(cube,n,index):
    out=defaultdict(int)
    for j in range(n):
        for fixed in (0,1):
            sub=face(cube,n,j,fixed)
            if sub in index:
                out[index[sub]]+=((-1)**(j+1))*(1 if fixed==0 else -1)
    return {i:v for i,v in out.items() if v}

# Differential has the exact signed convention, tested on generators.
def boundary1(cube):
    return {cube[0]:-1,cube[1]:1} if cube[0]!=cube[1] else {}
def composition_zero(cube):
    d3=cubical_boundary(cube,3,index2)
    comp=defaultdict(int)
    for j,coef in d3.items():
        for k,v in cubical_boundary(basis2[j],2,index1).items():
            comp[k]+=coef*v
    return all(v==0 for v in comp.values())

# The selected 219 actual cube boundaries have a unimodular pivot projection.
pivot_vectors={}
used=set()
for position,record in enumerate(selected):
    cube=tuple(record['cube'])
    row=record['pivot']
    assert len(cube)==8 and set(cube)<=set(range(4))
    assert nondegenerate(cube,3) and valid_three(cube)
    assert cube not in used and row not in pivot_vectors
    used.add(cube)
    assert composition_zero(cube)
    residual=cubical_boundary(cube,3,index2)
    for old_row in pivot_vectors:
        if old_row not in residual:continue
        coef=residual.pop(old_row)
        for j,c in pivot_vectors[old_row].items():
            if j==old_row:continue
            residual[j]=residual.get(j,0)-coef*c
            if not residual[j]:del residual[j]
    assert all(old_row not in residual for old_row in pivot_vectors), (position,row,"prior-pivot-reappeared")
    assert residual.get(row) in (-1,1),(position,row,residual.get(row))
    sign=residual[row]
    pivot_vectors[row]={j:sign*c for j,c in residual.items()}
assert len(pivot_vectors)==219

# Directly verify that the 2-boundary has rational rank exactly nine:
# nine explicit linearly independent relations, and d1 has rank three.
# Only the 2-boundaries of four two-color backtracks and five triangles
# are needed to certify rank; choose them via ordinary exact elimination.
def rank_integer_columns(cols):
    piv={}
    for col in cols:
        residual={j:__import__('fractions').Fraction(v) for j,v in col.items()}
        for row in sorted(piv):
            if row not in residual:continue
            coefficient=residual.pop(row)
            for j,val in piv[row].items():
                if j==row:continue
                residual[j]=residual.get(j,0)-coefficient*val
                if not residual[j]:del residual[j]
        if residual:
            row=min(residual)
            val=residual[row]
            piv[row]={j:c/val for j,c in residual.items()}
    return len(piv)

d2=[cubical_boundary(c,2,index1) for c in basis2]
assert rank_integer_columns(d2)==9
for cube in basis2:
    composite=defaultdict(int)
    for i,c in cubical_boundary(cube,2,index1).items():
        for vertex,v in boundary1(basis1[i]).items():composite[vertex]+=c*v
    assert all(v==0 for v in composite.values())
assert rank_integer_columns([boundary1(c) for c in basis1])==3

# Exhaustive independent census (the certificate proof needs only the 219 cubes).
census=0
for t in product(range(4),repeat=8):
    if nondegenerate(t,3) and valid_three(t):census+=1
assert census==32868
# Integral logic: C2 has rank 228; ker(d2) rank 228-9=219.
# The 219 verified boundaries form a primitive direct summand of C2,
# as each elimination uses coefficient +1 or -1. Their span equals ker(d2).
print('VERIFY_OK C1=12 C2=228 C3=32868 d1rank=3 d2rank=9 primitive_d3_rank=219 H2Gamma=0')
