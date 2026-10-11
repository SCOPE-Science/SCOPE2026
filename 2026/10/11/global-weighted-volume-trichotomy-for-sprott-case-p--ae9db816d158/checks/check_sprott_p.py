#!/usr/bin/env python3
"""Exact algebraic checks for the Sprott case-P identities; no numerical simulations."""
from sympy import symbols, Matrix, exp, simplify, Rational

x, y, z, a, b, m = symbols('x y z a b m', real=True)
F = Matrix([a*y + z, -x + y*y, x + b*y])
coords = Matrix([x,y,z])
P = y+z
lie = lambda q: simplify(sum(F[i]*q.diff(coords[i]) for i in range(3)))
assert simplify(lie(P) - y*(y+b)) == 0
trace = sum(F[i].diff(coords[i]) for i in range(3))
assert simplify(trace-2*y) == 0
rho = exp(-2*P/b)
weighted = sum((rho*F[i]).diff(coords[i]) for i in range(3))
assert simplify(weighted/rho + 2*y*y/b) == 0
for state in (Matrix([0,0,0]), Matrix([b*b,-b,a*b])):
    assert all(simplify(f.subs(dict(zip(coords,state)))) == 0 for f in F)
assert simplify((-b*m)-m*m-(-m*(m+b)))==0
for par in ({a:Rational(27,10),b:1},{a:-4,b:-3},{a:0,b:Rational(2,5)}):
    assert simplify((weighted/rho+2*y*y/b).subs(par))==0
print('PASS: exact Sprott-P polynomial, weighted-divergence, equilibrium and stationary-algebra identities')
