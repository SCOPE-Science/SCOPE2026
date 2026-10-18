#!/usr/bin/env python3
"""Exact rational certificate for the triangle-area map of a right 4-simplex.
Requires sympy. Run: python checker.py
"""
from itertools import combinations
from sympy import Matrix, Rational, Symbol, factor, simplify, eye

edges = tuple(combinations(range(5), 2))
faces = tuple(combinations(range(5), 3))
xs = tuple(Symbol('q'+str(i)) for i in range(len(edges)))
edge_to_x = dict(zip(edges, xs))
base = {edge_to_x[e]: Rational(1, 2) if 0 in e else Rational(1) for e in edges}

def face_squared_area(i,j,k):
    u, v, w = edge_to_x[(i,j)], edge_to_x[(i,k)], edge_to_x[(j,k)]
    return (2*(u*v+v*w+w*u)-u*u-v*v-w*w)/16

F = Matrix([face_squared_area(*tr) for tr in faces])
F0 = F.subs(base)
assert list(F0) == [Rational(1,16)]*6 + [Rational(3,16)]*4
J = F.jacobian(xs).subs(base)
U = Matrix([0,0,0,0, 0,1,-1,-1,1,0])
V = Matrix([0,0,0,0, 1,0,-1,-1,0,1])
A = Matrix([0,1,-1,-1,1,0,0,0,0,0])
B = Matrix([1,0,-1,-1,0,1,0,0,0,0])
assert J*U == Matrix.zeros(10,1)
assert J*V == Matrix.zeros(10,1)
assert (A.T*J) == Matrix.zeros(1,10)
assert (B.T*J) == Matrix.zeros(1,10)
rows = (0,1,2,3,6,7,8,9)
cols = (0,1,2,3,4,5,6,7)
assert J.extract(rows, cols).det() == -Rational(1,4194304)
assert J.rank() == 8

s,t = Symbol('s',real=True), Symbol('t',real=True)
sub = {xs[k]: base[xs[k]] + s*U[k] + t*V[k] for k in range(10)}
dF = F.subs(sub)-F0
qa, qb = factor((A.T*dF)[0]), factor((B.T*dF)[0])
assert qa == t*(2*s+t)/8
assert qb == s*(s+2*t)/8
assert simplify(qa**2+qb**2 -(s*s+t*t)**2/192
                -(s*s+3*s*t+t*t)**2/96) == 0

# The entire small kernel path lies in the open Euclidean edge-length domain.
def gram(x):
    ed = dict(zip(edges,x))
    return Matrix([[(ed[(0,i)] if i == j else
                    (ed[(0,i)] + ed[(0,j)] - ed[tuple(sorted((i,j)))])/2)
                    for j in range(1,5)] for i in range(1,5)])
for r in [Rational(1,16),-Rational(1,16)]:
    q = [base[xs[k]] + r*U[k] for k in range(10)]
    G = gram(q)
    assert all(G[:k,:k].det()>0 for k in range(1,5))
    assert F.subs(dict(zip(xs,q))) != F0
    assert (F.subs(dict(zip(xs,q))) - F0) == (r*r)*(F.subs({xs[k]:base[xs[k]]+U[k] for k in range(10)}) - F0)
print('PASS: base areas; rank-eight minor; two kernel and cokernel bases;')
print('      exact projected quadratic forms and coercivity identity;')
print('      positive-definite Gram examples and sharp quadratic scale.')
