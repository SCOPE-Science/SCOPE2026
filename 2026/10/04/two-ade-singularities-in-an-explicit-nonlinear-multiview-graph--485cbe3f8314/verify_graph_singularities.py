import sympy as sp

x,y,z,t,X,Y,Z,A,B,C = sp.symbols('x y z t X Y Z A B C')

q1 = B*X**3 - A*Y*Z**2
q2 = C*X**2 - A*Y**2
q3 = B*X*Y - C*Z**2
q4 = C**2*X*Z**2 - A*B*Y**3
q5 = A*B**2*Y**4 - C**3*Z**4

# Exact elimination certificate for the graph ideal.
param_ideal = [X-x, Y-y, Z-z, A-x**3*t, B-y*z**2*t, C-x*y**2*t]
G = sp.groebner(param_ideal, x,y,z,t,X,Y,Z,A,B,C, order='lex')
elim = [sp.expand(p.as_expr()) for p in G.polys if not any(p.as_expr().has(v) for v in (x,y,z,t))]
assert len(elim) == 5
GB3 = sp.groebner([q1,q2,q3], X,Y,Z,A,B,C, order='lex')
for f in elim:
    assert sp.expand(GB3.reduce(f)[1]) == 0
for f in (q1,q2,q3):
    GE = sp.groebner(elim, X,Y,Z,A,B,C, order='lex')
    assert sp.expand(GE.reduce(f)[1]) == 0

# The elimination Groebner basis is q1,q2,q3 plus two S-polynomial completions.
assert sp.expand(q4 - (B*Y*q2 - C*X*q3)) == 0
# q5 is checked by exact ideal reduction.
assert sp.expand(GB3.reduce(q5)[1]) == 0

# Fiber over p=[0:0:1]: ideal in second factor is (C), hence P^1=[A:B:0].
p_sub = [sp.expand(f.subs({X:0,Y:0,Z:1})) for f in (q1,q2,q3)]
Gp = sp.groebner(p_sub, A,B,C, order='lex')
assert [sp.factor(p.as_expr()) for p in Gp.polys] == [C]

# Fiber over q=[0:1:0]: ideal in second factor is (A), hence P^1=[0:B:C].
q_sub = [sp.expand(f.subs({X:0,Y:1,Z:0})) for f in (q1,q2,q3)]
Gq = sp.groebner(q_sub, A,B,C, order='lex')
assert [sp.factor(p.as_expr()) for p in Gq.polys] == [A]

# Patch p, Z=B=1: exact local ideal equals (C-XY, X^3-AY).
pB = [sp.expand(f.subs({Z:1,B:1})) for f in (q1,q2,q3,q4,q5)]
GpB = sp.groebner(pB, X,Y,A,C, order='lex')
E_pB = sp.groebner([C-X*Y, X**3-A*Y], X,Y,A,C, order='lex')
for f in GpB.polys:
    assert sp.expand(E_pB.reduce(f.as_expr())[1]) == 0
for f in E_pB.polys:
    assert sp.expand(GpB.reduce(f.as_expr())[1]) == 0

# Singular point of X^3-AY is only the origin; this is standard A2 form uv-w^3.
hp = X**3-A*Y
gradp = [sp.diff(hp,v) for v in (X,A,Y)]
critp = sp.groebner(gradp, X,A,Y, order='lex')
assert [sp.factor(p.as_expr()) for p in critp.polys] == [X**2, A, Y]

# Other patch of first exceptional fiber, Z=A=1, is affine plane: Y=BX^3, C=B^2X^4.
pA = [sp.expand(f.subs({Z:1,A:1})) for f in (q1,q2,q3,q4,q5)]
GpA = sp.groebner(pA, Y,C,X,B, order='lex')
expected_pA = sp.groebner([Y-B*X**3, C-B**2*X**4], Y,C,X,B, order='lex')
for f in GpA.polys:
    assert sp.expand(expected_pA.reduce(f.as_expr())[1]) == 0
for f in expected_pA.polys:
    assert sp.expand(GpA.reduce(f.as_expr())[1]) == 0

# Patch q, Y=C=1: exact local ideal equals (A-X^2, XB-Z^2).
qC = [sp.expand(f.subs({Y:1,C:1})) for f in (q1,q2,q3,q4,q5)]
GqC = sp.groebner(qC, A,X,B,Z, order='lex')
E_qC = sp.groebner([A-X**2, X*B-Z**2], A,X,B,Z, order='lex')
for f in GqC.polys:
    assert sp.expand(E_qC.reduce(f.as_expr())[1]) == 0
for f in E_qC.polys:
    assert sp.expand(GqC.reduce(f.as_expr())[1]) == 0

# Singular point of XB-Z^2 is only the origin; this is standard A1 form uv-w^2.
hq = X*B-Z**2
gradq = [sp.diff(hq,v) for v in (X,B,Z)]
critq = sp.groebner(gradq, X,B,Z, order='lex')
assert [sp.factor(p.as_expr()) for p in critq.polys] == [X, B, Z]

# Other patch of second exceptional fiber, Y=B=1, is affine plane: X=CZ^2, A=C^3Z^4.
qB = [sp.expand(f.subs({Y:1,B:1})) for f in (q1,q2,q3,q4,q5)]
GqB = sp.groebner(qB, X,A,C,Z, order='lex')
expected_qB = sp.groebner([X-C*Z**2, A-C**3*Z**4], X,A,C,Z, order='lex')
for f in GqB.polys:
    assert sp.expand(expected_qB.reduce(f.as_expr())[1]) == 0
for f in expected_qB.polys:
    assert sp.expand(GqB.reduce(f.as_expr())[1]) == 0

print('VERIFY_OK')
