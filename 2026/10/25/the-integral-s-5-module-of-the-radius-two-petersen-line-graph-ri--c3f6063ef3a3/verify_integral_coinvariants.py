#!/usr/bin/env python3
"""Independent integral S5-coinvariant lattice check with exact Smith form.
Run alongside verify_petersen_line_square.py; requires SymPy (tested 1.14).
"""
from itertools import product
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
from verify_petersen_line_square import blocks, group_action, sign_of_order

bvec=list(product((0,1),repeat=5)); lookup={v:i for i,v in enumerate(bvec)}
def induced_matrix(g):
    emap=group_action(g)
    M=Matrix.zeros(32,32)
    for col,v in enumerate(bvec):
        local=[]
        for c in range(5):
            source=blocks[c];destination=blocks[g[c]]
            u,w=emap[source[v[c]]],emap[source[2]]
            assert u in destination and w in destination
            components=[0,0,0]
            components[destination.index(u)]+=1
            components[destination.index(w)]-=1
            assert sum(components)==0
            local.append(components[:2])
        for target in bvec:
            a=sign_of_order(g)
            for c in range(5):a*=local[c][target[g[c]]]
            M[lookup[target],col]=a
    return M

I=Matrix.eye(32)
gens=[]
for i in range(4):
    g=list(range(5));g[i],g[i+1]=g[i+1],g[i]
    R=induced_matrix(g)
    assert R*R==I
    gens.append(R)
for i in range(4):
    for j in range(i+2,4):assert gens[i]*gens[j]==gens[j]*gens[i]
for i in range(3):assert gens[i]*gens[i+1]*gens[i]==gens[i+1]*gens[i]*gens[i+1]
A=Matrix.hstack(*(R-I for R in gens))
S=smith_normal_form(A,domain=ZZ)
invariants=[abs(int(S[i,i])) for i in range(32)]
assert sorted(invariants)==[0,0]+[1]*30
print('S5_GENERATORS',4,'COINVARIANT_RELATION_MATRIX',tuple(A.shape))
print('SMITH_NONZERO_UNIT_FACTORS',30,'SMITH_ZERO_FACTORS',2)
print('H4_S5_COINVARIANTS_IS_Z2',True)
print('VERIFY_OK_INTEGRAL_COINVARIANTS')
