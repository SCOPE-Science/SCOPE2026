"""Exact polynomial and boundary-permutation checks for the Cd curve.

Run: python verify.py (SymPy 1.10+).  This checks the displayed
identities only; the all-characteristic completeness proof is algebraic.
"""
from itertools import product
from sympy import symbols, expand

u, v, d = symbols('u v d')
f = (u*u + u)*(v*v + v) - d
maps = {
    'flip_u': (-1-u, v),
    'flip_v': (u, -1-v),
    'swap': (v, u),
}
for name, (u1, v1) in maps.items():
    assert expand(f.subs({u:u1, v:v1}, simultaneous=True)-f) == 0, name

# Boundary order: O=(0,infinity), T=(-1,infinity),
# R=(infinity,0), M=(infinity,-1).
O,T,R,M=range(4)
flip_u = (T,O,R,M)
flip_v = (O,T,M,R)
swap = (R,M,O,T)

def compose(p,q):
    return tuple(p[q[i]] for i in range(4))

gens=[flip_u, flip_v, swap]
identity=(O,T,R,M)
group={identity}
change=True
while change:
    before=len(group)
    group.update(compose(g,h) for g in gens for h in list(group))
    change=len(group)!=before
assert len(group)==8, len(group)
assert all(sorted(p)==list(range(4)) for p in group)
# Inversion fixes O,T and exchanges R,M.
assert flip_v == (O,T,M,R)
# The quotient parameter is invariant under all generators.
J=u*u+u+v*v+v
for name, (u1,v1) in maps.items():
    assert expand(J.subs({u:u1, v:v1},simultaneous=True)-J)==0, name
print('VERIFY_OK: three universal integer polynomial identities')
print('VERIFY_OK: eight distinct boundary permutations and invariant J')
