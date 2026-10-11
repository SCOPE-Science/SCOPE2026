"""Exact algebraic consistency checks for the classical three-dimensional Rössler system.

Run with: python check_identity.py
Requires SymPy. Analytical sign, compactness and LaSalle arguments are in RESULT.md.
"""
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
a, b, c, p = sp.symbols('a b c p', real=True)
X, Y, Z = x - a*p, y + p, z - p
f = (-y-z, x+a*y, b+z*(x-c))
V = (X*X+Y*Y)/2 + z-p-p*sp.log(z/p)
dV = sum(sp.diff(V, u)*fu for u,fu in zip((x,y,z),f))
claimed = a*Y*Y+(a*p-c)*Z*Z/z
residual = sp.factor(dV-claimed)
assert sp.simplify(residual-(a*p*p-c*p+b)*Z/z)==0
assert sp.simplify(residual.subs(b,c*p-a*p*p))==0
assert all(sp.simplify(v)==0 for v in (
    f[0].subs({x:a*p,y:-p,z:p}),
    f[1].subs({x:a*p,y:-p,z:p}),
    f[2].subs({x:a*p,y:-p,z:p,b:c*p-a*p*p})
))
assert sp.simplify((f[0]-(-Y-Z)))==0
assert sp.simplify(f[1]-(X+a*Y))==0
assert sp.simplify((f[2]-(z*X+(a*p-c)*Z)).subs(b,c*p-a*p*p))==0
# Algebraic spot checks are not a proof of the quantified global stability theorem.
for aa,bb,cc in ((0,1,3),(-1,2,3),(-sp.Rational(1,2),4,5),(-5,1,1)):
    roots=[sp.N(r,30) for r in sp.solve(aa*p*p-cc*p+bb,p)] if aa else [sp.Rational(bb,cc)]
    pos=[r for r in roots if r.is_real and r>0]
    assert len(pos)==1
    assert sp.N(aa*pos[0]-cc)<0
print('PASS: exact equilibrium, translated vector field, entropy derivative, and sign samples')
