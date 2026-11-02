#!/usr/bin/env python3
"""Exact symbolic verification of a three-phase gradient-curvature obstruction."""
import sympy as s
t=s.symbols('t0:3', real=True)
f=(3+2*sum(s.cos(t[i]-t[j]) for i in range(3) for j in range(i+1,3)))/9
g=s.Matrix([s.diff(f,x) for x in t]);H=s.hessian(f,t)
for i in range(3):
    drift=sum(s.sin(t[j]-t[i]) for j in range(3))/3
    assert s.trigsimp(drift-s.Rational(3,2)*g[i])==0
p={t[0]:0,t[1]:s.pi/2,t[2]:2*s.pi/3}
G=s.simplify(g.subs(p)); Q=s.simplify(H.subs(p)*G)
assert G == s.Matrix([2+s.sqrt(3),-1,-1-s.sqrt(3)])/9
assert Q == s.Matrix([3+2*s.sqrt(3),-3,-2*s.sqrt(3)])/81
assert s.simplify(f.subs(p)) == (2+s.sqrt(3))/9
assert s.simplify(G.cross(Q)) == -(3+s.sqrt(3))*s.ones(3,1)/729
print('PASS: drift gradient normalization, exact witness, Hessian-vector product, nonzero cross product')
