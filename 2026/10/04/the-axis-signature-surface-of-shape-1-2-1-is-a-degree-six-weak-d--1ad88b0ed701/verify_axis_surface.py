#!/usr/bin/env python3
import sympy as s

# Source parameters and projective coordinates.
a,b,c = s.symbols('a b c')
X = s.symbols('X0:7')
forms = [(a+c)**3, a**2*b, a*b*c, a*b**2, b*c**2, b**2*c, b**3]

graph = [X[i]-forms[i] for i in range(7)]
G = s.groebner(graph, a,b,c,*X, order='lex')
elim = [s.expand(p.as_expr()) for p in G.polys if not (p.as_expr().has(a) or p.as_expr().has(b) or p.as_expr().has(c))]

expected = [
 X[0]*X[3]-X[1]**2-3*X[1]*X[2]-3*X[2]**2-X[2]*X[4],
 X[0]*X[5]-X[1]*X[2]-3*X[2]**2-3*X[2]*X[4]-X[4]**2,
 X[0]*X[6]-X[1]*X[3]-3*X[2]*X[3]-3*X[3]*X[4]-X[4]*X[5],
 X[1]*X[4]-X[2]**2,
 X[1]*X[5]-X[2]*X[3],
 X[1]*X[6]-X[3]**2,
 X[2]*X[5]-X[3]*X[4],
 X[2]*X[6]-X[3]*X[5],
 X[4]*X[6]-X[5]**2,
]
assert len(elim) == 9
# Compare ideals by mutual exact Groebner reduction.
GE = s.groebner(expected, *X, order='grevlex')
for f in elim:
    assert GE.reduce(f)[1] == 0
GI = s.groebner(elim, *X, order='grevlex')
for f in expected:
    assert GI.reduce(f)[1] == 0
for f in expected:
    assert s.expand(f.subs(dict(zip(X, forms)))) == 0

# x0=1: eliminate x3,x5,x6 and verify every remaining relation is a multiple
# of x1*x4-x2^2.
x1,x2,x4 = s.symbols('x1 x2 x4')
x3 = x1**2 + 3*x1*x2 + 3*x2**2 + x2*x4
x5 = x1*x2 + 3*x2**2 + 3*x2*x4 + x4**2
x6 = s.expand(x1*x3 + 3*x2*x3 + 3*x3*x4 + x4*x5)
baseA1 = x1*x4-x2**2
relsA1 = [
 x1*x4-x2**2,
 x1*x5-x2*x3,
 x1*x6-x3**2,
 x2*x5-x3*x4,
 x2*x6-x3*x5,
 x4*x6-x5**2,
]
GA1 = s.groebner([baseA1], x1,x2,x4, order='grevlex')
for f in relsA1:
    assert GA1.reduce(s.expand(f))[1] == 0
# Unique singularity of uv-w^2 is the origin.
assert s.Matrix([s.diff(baseA1,v) for v in (x1,x2,x4)]).subs({x1:0,x2:0,x4:0}) == s.zeros(3,1)

# x1=1: x4=x2^2, x5=x2*x3, x6=x3^2 and the residual equation is x0*x3-(1+x2)^3.
x0,x2b,x3b = s.symbols('x0 x2b x3b')
subsB = {X[0]:x0, X[1]:1, X[2]:x2b, X[3]:x3b, X[4]:x2b**2, X[5]:x2b*x3b, X[6]:x3b**2}
residual = s.expand(x0*x3b-(1+x2b)**3)
GB = s.groebner([residual], x0,x2b,x3b, order='grevlex')
for f in expected:
    rr = s.expand(f.subs(subsB))
    assert GB.reduce(rr)[1] == 0
# A2 singularity at x0=0, x2=-1, x3=0.
gradB = [s.diff(residual,v) for v in (x0,x2b,x3b)]
assert all(g.subs({x0:0,x2b:-1,x3b:0}) == 0 for g in gradB)

# x6=1 chart is A^2 with coordinates x3=a/b, x5=c/b.
u,v=s.symbols('u v')
chart6 = {X[0]:(u+v)**3, X[1]:u**2, X[2]:u*v, X[3]:u, X[4]:v**2, X[5]:v, X[6]:1}
for f in expected:
    assert s.expand(f.subs(chart6)) == 0

# Jacobian rank drops from codimension 4 to 3 at the two claimed points.
J = s.Matrix([[s.diff(f,z) for z in X] for f in expected])
P = dict(zip(X,[1,0,0,0,0,0,0]))
Q = dict(zip(X,[0,1,-1,0,1,0,0]))
assert J.subs(P).rank() == 3
assert J.subs(Q).rank() == 3

# Intersection lattice: H^2=1, Ei^2=-1 and all other basis pairings zero.
# Vectors are coefficients of (H,E1,E2,E3).
def dot(u,v):
    return u[0]*v[0] - sum(u[i]*v[i] for i in range(1,4))
Kminus = (3,-1,-1,-1)
C0=(1,-1,-1,-1)
C1=(0,1,-1,0)
C2=(0,0,1,-1)
assert [dot(C,C) for C in (C0,C1,C2)] == [-2,-2,-2]
assert [dot(Kminus,C) for C in (C0,C1,C2)] == [0,0,0]
assert dot(C1,C2) == 1
assert dot(C0,C1) == 0 and dot(C0,C2) == 0
assert dot(Kminus,Kminus) == 6

print('VERIFY_OK')
