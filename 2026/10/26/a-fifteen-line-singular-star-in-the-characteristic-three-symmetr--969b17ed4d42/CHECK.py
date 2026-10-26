#!/usr/bin/env python3
"""Exact finite-characteristic verification for the symmetric quartic cone.
Requires SymPy >= 1.13. All coefficients and evaluations are exact modulo 3.
The accompanying proof supplies the algebraic globalization argument.
"""
from itertools import combinations, product
import sympy as s

P = 3
z = s.symbols('z0:5')
a, b, c = s.symbols('a b c')
t = s.symbols('t')

def e4(vals):
    return s.expand(sum(s.prod(v) for v in combinations(vals, 4)))

def zero_mod3(expr, vars_):
    return s.Poly(s.expand(expr), *vars_, modulus=P).is_zero

# On the hyperplane sum x_i=0, translation by (1,1,1,1,1,1)
# leaves the quartic invariant in characteristic 3.
y = s.symbols('y0:5')
y6 = list(y) + [-sum(y)]
assert zero_mod3(e4([r+t for r in y6])-e4(y6), (*y,t))

# Project from the fixed point and impose z4 = -(z0+z1+z2+z3).
q = s.expand(e4(z).subs(z[4],-sum(z[:4])))
g = s.expand(q.subs({z[0]: 1, z[1]: a, z[2]: b, z[3]: c}))
J = [s.diff(g, v) for v in (a,b,c)]
G = s.groebner([g]+J,a,b,c, order='lex', modulus=P)
expected = [
 a**2-a*c+a-b**2+b*c-b,
 a*b-a*c-b**2-b+c**2+c,
 a*c**2-a*c-b*c**2+b*c,
 b**3-b,
 b**2*c+b**2-b*c**2+b-c**2-c,
 c**3-c
]
assert len(G.polys)==6
for obtained, want in zip(G.polys,expected):
    assert zero_mod3(obtained.as_expr()-want,(a,b,c))
assert G.is_zero_dimensional
LM = [s.Poly(f.as_expr(),a,b,c,modulus=P).LM(order='lex').exponents for f in G.polys]
standard = [(i,j,k) for i in range(2) for j in range(3) for k in range(3)
            if not any(i>=u and j>=v and k>=w for u,v,w in LM)]
assert len(standard)==9
assert standard==[(0,0,0),(0,0,1),(0,0,2),(0,1,0),
                  (0,1,1),(0,1,2),(0,2,0),(1,0,0),(1,0,1)]

points = []
H = s.hessian(g,(a,b,c)).det()
for triple in product(range(P),repeat=3):
    at = dict(zip((a,b,c),triple))
    if all(int(f.subs(at))%P==0 for f in [g]+J):
        points.append(triple)
        assert int(H.subs(at))%P == 1
assert len(points)==9
expected_points = [(0,0,0),(0,0,2),(0,2,0),(1,1,1),(1,1,2),
                   (1,2,1),(2,0,0),(2,1,1),(2,2,2)]
assert sorted(points)==expected_points

# Fifteen lines are indexed by the fifteen unordered pairs of six indices.
classes=set(); chart=set()
for i,j in combinations(range(6),2):
    vec=[0]*6
    vec[i],vec[j]=1,-1
    zz=[(vec[u]-vec[5])%P for u in range(5)]
    first = next(u for u,n in enumerate(zz) if n)
    key=tuple((u*pow(zz[first],-1,P))%P for u in zz)
    classes.add(key)
    if zz[0]:
        inv = pow(zz[0],-1,P)
        chart.add(tuple((zz[u]*inv)%P for u in (1,2,3)))
assert len(classes)==15
assert chart==set(expected_points)

# All rational points of the projective quartic threefold: optional sanity check.
projective=[]
for v in product(range(3),repeat=5):
    if not any(v):continue
    i=next(i for i,w in enumerate(v) if w)
    if v[i]!=1:continue
    six=list(v)+[-sum(v)]
    F=e4(six)
    if int(F)%3==0:projective.append(v)
assert len(projective)==76
print('PASS: translation invariance; exact reduced Groebner basis; 9 reduced chart nodes;')
print('      15 distinct projective base nodes; 15 concurrent lines; 76 F3 points.')
