"""Exact projective coordinate checks for the two exceptional incidence types.
Sympy is used only for rational polynomial identities and Q(sqrt(-3)).
"""
import sympy as s
v=s.symbols('v')
u=2-v; w=-v
chord=lambda a,b:s.Matrix([1,-(a+b),a*b])
S=[chord(u,v),chord(v,w),chord(w,u)]
T=[s.Matrix([1,0,0]),s.Matrix([1,-2,1]),s.Matrix([0,0,1])]
P=[S[i].cross(T[i]) for i in range(3)]
d=s.factor(s.det(s.Matrix.hstack(*P)))
assert s.expand(d-4*(2*v-1)*(v*v-v+1))==0
assert s.rem(d,v*v-v-1,v)==16*v-8
assert s.gcd(d,v*v-v-1)==1
print('THREE_TANGENTS_FOUR_SECANTS_COLLINEARITY_IMPOSSIBLE_OK')

z=s.symbols('z',nonzero=True)
w=(-1+s.sqrt(-3))/2
assert s.simplify(w*w+w+1)==0
points=[z,1/z,w*z,w*w/z,w*w*z,w/z]
lines=[chord(points[i],points[(i+1)%6]) for i in range(6)]
R=[lines[i].cross(lines[i+3]) for i in range(3)]
A=s.Matrix([1,0,-w*w])
for r in R:
    assert s.simplify(s.expand(A.dot(r)))==0
# The Pascal line is non-tangent to the parametrized conic X=t^2,Y=t,Z=1,
# as t^2-w^2 has distinct roots +w and -w in characteristic zero.
assert w!=0
print('HEXAGON_PASCAL_LINE_NON_TANGENT_OK')
