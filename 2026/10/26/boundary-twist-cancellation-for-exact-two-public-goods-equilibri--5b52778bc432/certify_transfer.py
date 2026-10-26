#!/usr/bin/env python3
"""Exact symbolic transfer-matrix certificate for cubic prism/Mobius public-goods fixed points.

Requires Python 3 and SymPy. All identities are over the polynomial ring Z[z,t].
"""
from itertools import product
from math import comb
import sympy as S

z,t=S.symbols('z t')
pairs=list(product((0,1), repeat=2))
states=[(a,b) for a in pairs for b in pairs]
state_id={v:i for i,v in enumerate(states)}
flip=lambda q:(q[1],q[0])
twist=lambda v:(flip(v[0]),flip(v[1]))
T=S.zeros(16)
for i,(left,center) in enumerate(states):
    for right in pairs:
        is_fixed=all(center[k] == int(left[k]+right[k]+center[1-k] == 2) for k in (0,1))
        if is_fixed:
            T[i,state_id[(center,right)]]=z**sum(center)

# The row-exchange involution commutes with the transfer matrix.
assert all(T[i,j]==T[state_id[twist(states[i])],state_id[twist(states[j])]]
           for i in range(16) for j in range(16))
fixed=[];pair_orbits=[];used=set()
for st in states:
    if st in used:continue
    other=twist(st)
    used.update((st,other))
    (fixed if st==other else pair_orbits).append(st if st==other else (st,other))
assert len(fixed)==4 and len(pair_orbits)==6
basis_plus=S.zeros(16,10)
basis_minus=S.zeros(16,6)
for k,st in enumerate(fixed):basis_plus[state_id[st],k]=1
for k,(st,other) in enumerate(pair_orbits):
    basis_plus[state_id[st],4+k]=1
    basis_plus[state_id[other],4+k]=1
    basis_minus[state_id[st],k]=1
    basis_minus[state_id[other],k]=-1

def restrict(B):
    out=S.zeros(B.cols)
    transported=T*B
    for row in range(B.cols):
        pivot=next(j for j in range(16) if B[j,row]!=0)
        for col in range(B.cols):
            out[row,col]=S.expand(transported[pivot,col]/B[pivot,row])
    assert B*out==transported
    return out
A=restrict(basis_plus);B=restrict(basis_minus)
plus_expected=t**3*(t-z)*(t**2-z**3)*(t**4-t**3-z**4)
minus_expected=t**3*(t-z)*(t**2+z**3)
assert S.expand(A.charpoly(t).as_expr()-plus_expected)==0
assert S.expand(B.charpoly(t).as_expr()-minus_expected)==0
# Distinct eigenspace traces encode the untwisted and crossed edge identifications.
for n in range(3,10):
    bulk=sum(S.Integer(n)*S.binomial(n-3*j,j)*z**(4*j)/(n-3*j)
             for j in range(n//4+1))
    expect_M=bulk+(4*z**(3*n//2) if n%4==2 else 0)
    expect_C=bulk+2*z**n+(4*z**(3*n//2) if n%4==0 else 0)
    an=S.trace(A**n); bn=S.trace(B**n)
    assert S.expand(an-bn-expect_M)==0
    assert S.expand(an+bn-expect_C)==0
print('PASS exact polynomial characteristic identities on 10D and 6D invariant subspaces')
print('PASS twisted and untwisted traces for n=3,...,9')
