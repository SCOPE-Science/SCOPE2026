#!/usr/bin/env python3
"""Exact lattice-fan isomorphism certificate; requires SymPy."""
import itertools
import sympy as S

CONES = {(1,2,4),(2,3,4),(3,4,5),(4,5,6),(1,4,6),(1,6,7),
         (1,2,7),(2,3,7),(3,5,8),(5,6,8),(3,7,8),(6,7,8)}
TRI = {frozenset(c) for c in CONES}
a,b = S.symbols('a b')
def rays(z):
    return {1:S.Matrix([1,1,2]),2:S.Matrix([1,0,0]),
            3:S.Matrix([0,-1,0]),4:S.Matrix([0,0,-1]),
            5:S.Matrix([-1,z,z+1]),6:S.Matrix([0,1,0]),
            7:S.Matrix([0,0,1]),8:S.Matrix([-1,z+2,z+2])}

perms=[]
for p in itertools.permutations(range(1,9)):
    h=dict(enumerate(p,1))
    if {frozenset(h[i] for i in c) for c in TRI}==TRI:
        perms.append(h)
assert len(perms)==8, len(perms)
src,dst=rays(a),rays(b)
sol=[]
for h in perms:
    I=(1,2,4)
    A=S.Matrix.hstack(*[src[i] for i in I]);B=S.Matrix.hstack(*[dst[h[i]] for i in I])
    assert A.det() in (-1,1)
    U=S.simplify(B*A.inv())
    equations=[S.expand(x) for i in range(1,9) for x in (U*src[i]-dst[h[i]]) if x!=0]
    G=list(S.groebner(equations,a,b))
    sol.append((tuple(h[i] for i in range(1,9)),G,U))
expected={
 (1,2,3,4,5,6,7,8):[a-b],
 (5,8,7,6,1,4,3,2):[a+b+4],
}
assert len(sol)==8
for perm,G,U in sol:
    target=expected.get(perm,[S.Integer(1)])
    assert len(G)==len(target) and all(S.simplify(z-t)==0 for z,t in zip(G,target)),(perm,G)
reflection=next(U for h,G,U in sol if h==(5,8,7,6,1,4,3,2)).subs(b,-a-4)
assert S.simplify(reflection-S.Matrix([[-1,0,0],[-a-2,0,-1],[-a-2,-1,0]]))==S.zeros(3)
assert reflection.det()==1
assert (reflection.subs(a,-a-4)*reflection)==S.eye(3)
print('VERIFY_OK: eight simplicial automorphisms; only identity a=b and reflection a+b+4=0; det=1')
