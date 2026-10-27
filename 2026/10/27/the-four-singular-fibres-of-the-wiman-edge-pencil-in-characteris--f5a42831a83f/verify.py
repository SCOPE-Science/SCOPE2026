"""Exact symbolic checks for Wiman--Edge plane-sextic specialization in characteristic 3.
Requires Python 3 and SymPy. Does not replace the geometric proof.
"""
import sympy as S

A,B,C,t=S.symbols('A B C t')
x,y,z,u,h=S.symbols('x y z u h')
U=A+B+C
V=A*B+B*C+C*A
D=(A-B)*(B-C)*(C-A)
F=S.expand(U*(V-U**2)+t*D)

def zero_mod3(expr,*variables):
    return S.Poly(S.expand(expr),*variables, modulus=3).is_zero

# The classical integral generators and the specialization identity.
Q=x**6+y**6+z**6+(x*x+y*y+z*z)*(x**4+y**4+z**4)-12*x*x*y*y*z*z
P=(x*x-y*y)*(y*y-z*z)*(z*z-x*x)
assert zero_mod3(Q-F.subs({A:x*x,B:y*y,C:z*z,t:0}),x,y,z)
assert zero_mod3(P-D.subs({A:x*x,B:y*y,C:z*z}),x,y,z)
assert zero_mod3(sum(S.diff(F, a) for a in (A,B,C))+U**2,A,B,C,t)
assert zero_mod3(F.subs({A:0,C:1})+(B-1)*(B*B+t*B-1),B,t)
# This last identity is modulo the exceptional parameter equation t^2+1=0.
nodecoef=S.rem(S.diff(F,A).subs({A:0,B:t,C:1})-t,t*t+1,t)
assert zero_mod3(nodecoef,t)

R=(V-U**2).subs({A:x*x,B:y*y,C:z*z})
L=(x+y+z)*(x+y-z)*(x-y+z)*(-x+y+z)
assert zero_mod3(R-L,x,y,z)

# At (1:1:1), use x=1+u, y=1+h-u, z=1. Degree-two part is -h^2;
# the degree-three restriction to the double tangent h=0 is t*u^3.
loc=S.Poly(S.expand(F.subs({A:(1+u)**2,B:(1+h-u)**2,C:1})),u,h,t)
part2=part3=S.Integer(0)
for (iu,ih,it),co in loc.terms():
    if iu+ih==2:part2+=co*u**iu*h**ih*t**it
    if iu+ih==3:part3+=co*u**iu*h**ih*t**it
assert zero_mod3(part2+h*h,u,h,t)
assert zero_mod3(part3.subs(h,0)-t*u**3,u,t)

# On x=0 at t^2=-1 the binary cubic is -(B-1)(B-t)^2;
# the transverse x^2 and tangent (B-t)^2 coefficients are both nonzero.
assert zero_mod3((B*B+t*B-1)-(B-t)**2+(t*t+1),B,t)

# The four fundamental points form a quadrangle in projective characteristic 3.
from itertools import combinations
pts=[(1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1)]
for tri in combinations(pts,3):
    assert S.det(S.Matrix(tri)) % 3 != 0

# The six intersections of four lines lie off U=0 and are all distinct.
lines=[S.Matrix([1,1,1]),S.Matrix([1,1,-1]),S.Matrix([1,-1,1]),S.Matrix([-1,1,1])]
points=[]
for a,b in combinations(lines,2):
    v=a.cross(b); vv=tuple(int(w)%3 for w in v)
    for c in vv:
        if c%3: inv=pow(c,-1,3);break
    vv=tuple(w*inv%3 for w in vv)
    assert sum(w*w for w in vv)%3 !=0
    points.append(vv)
assert len(set(points))==6
print('VERIFY_OK: characteristic-three identities, local cusp and node coefficients, four-point blowup, K5 geometry')
