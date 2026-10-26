#!/usr/bin/env python3
"""Symbolic Pfaffian certificate for the coadjoint rank boundaries of T_4."""
from itertools import combinations
from functools import lru_cache
import sympy as sp

pos=[(i,j) for i in range(4) for j in range(i,4)]
off=[(i,j) for i,j in pos if i<j]
a,b,c,d,e,f=sp.symbols('a b c d e f')
lam=dict(zip(off,[a,b,c,d,e,f]))
M=sp.Matrix(10,10,lambda u,v:(lam.get((pos[u][0],pos[v][1]),0) if pos[u][1]==pos[v][0] else 0)-(lam.get((pos[v][0],pos[u][1]),0) if pos[v][1]==pos[u][0] else 0))
@lru_cache(None)
def pf(I):
    if not I:return sp.Integer(1)
    return sp.factor(sum((-1)**(j+1)*M[I[0],I[j]]*pf(I[1:j]+I[j+1:]) for j in range(1,len(I))))
Delta=b*e-c*d
Q=a*e+b*f
expected={sp.expand(Delta*x) for x in (c*c,a*c,b*c,c*e,c*f,Q)}
actual={sp.expand(pf(I)) for I in combinations(range(10),8)}-{0}
assert all(x in expected or -x in expected for x in actual)
assert all(x in actual or -x in actual for x in expected)
for k,expected_forms in ((6,(c**3,b*b*e,b*b*f,a*e*e)),(4,(b*b,e*e))):
    forms={sp.expand(pf(I)) for I in combinations(range(10),k)}
    for x in expected_forms:
        assert x in forms or -x in forms,(k,x)
print('VERIFY_OK_BOREL4_SYMBOLIC_PFAFFIANS')
