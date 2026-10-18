"""Exact symbolic verification for the Han--Kwak threefold chart.
Requires Python 3 and SymPy. No probabilistic or floating-point tests.
"""
import sympy as S

u, t, v, a, b, z = S.symbols('u t v a b z')
P, Q, R = S.symbols('P Q R')
H = 1 + b*b*v
F = a*(u-b*v*v) + u*u + v**3
G = t*H + u*v+b*v**3-a*b*b*v*v
J2 = -a*a*b*b*v*v+a*b*b*t*v+2*a*b*v**3+a*t-b*t*v*v+t*u-v**4
J4 = a*a*b*b*v**3-2*a*b*b*t*v*v-2*a*b*v**4-a*t*v+b*b*t*t*v+2*b*t*v**3+t*t+v**5
f1 = t*(b*v*v-u)-u*u*v
f2 = a*(b*v*v-u)-v**3-u*u
param = {u:Q/(P*R), t:Q**2/(P*R),v:1/R,
         a:(P*P+Q*Q*R)/(P*R),b:(R+Q*R*R)/(P*R)}
for polynomial in [F,G,J2,J4,f1,f2]:
    assert S.factor(polynomial.subs(param, simultaneous=True)) == 0
# Exact elimination certificate: saturation of the parametric elimination ideal by v.
GB = S.groebner([f1,f2,z*v-1],z,u,t,v,a,b,order='lex')
nonz = [g.as_expr() for g in GB.polys if not g.as_expr().has(z)]
assert len(nonz) == 4
GB2 = S.groebner([F,G,J2,J4],u,t,v,a,b,order='lex')
for h in nonz:
    assert GB2.reduce(h)[1] == 0
GB3 = S.groebner(nonz,u,t,v,a,b,order='lex')
for h in [F,G,J2,J4]:
    assert GB3.reduce(h)[1] == 0
# Where H is a unit, the two extra equations follow from F and G.
GBh = S.groebner([F,G,z*H-1],z,u,t,v,a,b,order='lex')
for h in [J2,J4]:
    assert GBh.reduce(h)[1] == 0
# The singular support of F on H != 0 is u=v=a=0.
assert S.factor(F.subs({u:0,v:0,a:0})) == 0
assert [S.diff(F,x) for x in (u,v,a,b)] == [a+2*u,3*v**2-2*a*b*v,u-b*v**2,-a*v*v]
# On H=0 the equations imply the following; b != 0 and b^3*u != 1.
special={v:-1/b**2,a:-u-1/b**3,t:b*u*u/(b**3*u-1)}
assert S.factor(G.subs({v:-1/b**2,a:-u-1/b**3})) == 0
j2_spec = S.factor(J2.subs({v:-1/b**2,a:-u-1/b**3}))
assert S.factor(j2_spec - (b**3*t*u-b*u*u-t)/b**3)==0
jac = S.Matrix([[S.diff(f,x) for x in (u,t)] for f in (F,J2)])
det = S.factor(jac.det().subs(special))
assert S.factor(det-(b**3*u-1)**2/b**6) == 0
# Formal A2 coordinate: W = u-b*v^2, U=a+u+b*v^2;
# exact identity F=U W+v^3 H.
W=u-b*v*v
U=a+u+b*v*v
assert S.expand(F-U*W-v**3*H)==0
print('VERIFY_OK: parameter identities, saturation, local equations, H=0 smoothness, formal A2 type')
