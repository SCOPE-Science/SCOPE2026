#!/usr/bin/env python3
import sympy as sp

# Source and target coordinates.
x,y,z,w,t = sp.symbols('x y z w t')
X,Y,Z,W,A,B,C,D = sp.symbols('X Y Z W A B C D')

# Graph of ([x:y:z:w],[x*y^2:x*w^2:y*z*w:z^2*w]).
rels = [
    X-x, Y-y, Z-z, W-w,
    A-x*y**2*t,
    B-x*w**2*t,
    C-y*z*w*t,
    D-z**2*w*t,
]
G = sp.groebner(rels, x,y,z,w,t,X,Y,Z,W,A,B,C,D, order='lex')
elim = [sp.expand(p.as_expr()) for p in G.polys
        if not (p.as_expr().free_symbols & {x,y,z,w,t})]
assert len(elim) == 8

# Three relations used in the affine chart proof really belong to the exact kernel.
needed = [D*Y-C*Z, D*W*X-B*Z**2, C**2*X-A*D*W]
for q in needed:
    rem = sp.groebner(elim, X,Y,Z,W,A,B,C,D, order='lex').reduce(q)[1]
    assert sp.expand(rem) == 0

# Dehomogenize the exact graph kernel at X=D=1.
chart_vars = [Y,W,C,Z,A,B]
chart_polys = [sp.expand(f.subs({X:1,D:1})) for f in elim]
chart_polys = [f for f in chart_polys if f != 0]
chart_gb = sp.groebner(chart_polys, *chart_vars, order='lex')
model_gb = sp.groebner([
    Y-C*Z,
    W-B*Z**2,
    C**2-A*B*Z**2,
], *chart_vars, order='lex')
assert [sp.expand(p.as_expr()) for p in chart_gb.polys] == [sp.expand(p.as_expr()) for p in model_gb.polys]

# Hypersurface model R = QQ[Z,A,B,C]/(C^2-A*B*Z^2).
f = C**2-A*B*Z**2
assert sp.factor(f) == f

# The integral element T=C/Z is not already in R: C is nonzero modulo (Z,f).
remC = sp.groebner([f,Z], C,A,B,Z, order='lex').reduce(C)[1]
assert sp.expand(remC) == C

# Normalization candidate S = QQ[Z,A,B,T]/(T^2-A*B), C=Z*T.
T = sp.symbols('T')
g = T**2-A*B
assert sp.expand(f.subs(C,Z*T)) == sp.expand(Z**2*g)
# S is singular only on A=B=T=0 (with Z free), hence regular in codimension one.
partials_g = [sp.diff(g,v) for v in (Z,A,B,T)]
assert partials_g == [0, -B, -A, 2*T]

# Jacobian of R: set-theoretic singular locus is V(Z,C) union V(A,B,C).
partials_f = [sp.diff(f,v) for v in (Z,A,B,C)]
assert partials_f == [-2*A*B*Z, -B*Z**2, -A*Z**2, 2*C]
# Representative checks for the two strata.
assert all(sp.expand(q.subs({Z:0,C:0})) == 0 for q in [f]+partials_f)
assert all(sp.expand(q.subs({Z:1,A:0,B:0,C:0})) == 0 for q in [f]+partials_f)
# Away from Z=0 the change T=C/Z gives the A1 equation T^2=A*B.
assert sp.expand((f/Z**2).subs(C,Z*T)) == g

# Conductor inclusion checks: Z*T=C and C*T=Z*A*B in the normalization.
assert sp.expand(Z*T - C).subs(C,Z*T) == 0
assert sp.expand(C*T - Z*A*B).subs(C,Z*T).subs(T**2,A*B) == 0

print('VERIFY_OK')
print('elimination_generators=', len(elim))
print('chart_equation=', str(f))
print('normalization_equation=', str(g))
