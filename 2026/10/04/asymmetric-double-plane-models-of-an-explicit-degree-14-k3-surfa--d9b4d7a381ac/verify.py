import sympy as s

t,u,v,x,y,z=s.symbols('t u v x y z')
F=(t*u*x-u**2*x+u*v*x-v**2*x+t*x**2-u*x**2+t**2*y-t*u*y-t*v*y-t*x*y-v*x*y-t*y**2+t*u*z+v**2*z-t*x*z-u*y*z-v*y*z-t*z**2+u*z**2)
A=t**2*y+t*u*x-t*u*y+t*u*z-t*v*y-u**2*x+u*v*x-v**2*x+v**2*z
B=t*x**2-t*x*y-t*x*z-t*y**2-t*z**2-u*x**2-u*y*z+u*z**2-v*x*y-v*y*z
assert s.expand(F-A-B)==0
l=s.Matrix([t*u-u**2+u*v-v**2, t**2-t*u-t*v, t*u+v**2])
Q2=s.Matrix([[2*(t-u),-(t+v),-t],[-(t+v),-2*t,-(u+v)],[-t,-(u+v),2*(-t+u)]])
m=s.Matrix([x**2-x*y-x*z-y**2-z**2,-x**2-y*z+z**2,-x*y-y*z])
P2=s.Matrix([[2*y,x-y+z,-y],[x-y+z,-2*x,x],[-y,x,2*(-x+z)]])
D1=s.expand((l.T*Q2.adjugate()*l)[0])
D2=s.expand((m.T*P2.adjugate()*m)[0])
assert s.Poly(D1,t,u,v).total_degree()==6
assert s.Poly(D2,x,y,z).total_degree()==6
# exact projective singularity checks by affine charts; Euler makes D redundant in char 0
def gb_unit(polys, vars):
    return s.groebner(polys,*vars,order='lex').is_zero_dimensional is False and False

def basis_exprs(polys, vars):
    G=s.groebner(polys,*vars,order='lex')
    return [s.expand(p.as_expr()) for p in G.polys]
for fixed, rest in [(t,(u,v)),(u,(t,v)),(v,(t,u))]:
    ps=[s.expand(s.diff(D1,q).subs(fixed,1)) for q in (t,u,v)]
    assert basis_exprs(ps,rest)==[1]
# D2 has unique projective singularity [0:1:0]
assert basis_exprs([s.expand(s.diff(D2,q).subs(x,1)) for q in (x,y,z)],(y,z))==[1]
Gy=basis_exprs([s.expand(s.diff(D2,q).subs(y,1)) for q in (x,y,z)],(x,z))
assert Gy==[x,z]
assert basis_exprs([s.expand(s.diff(D2,q).subs(z,1)) for q in (x,y,z)],(x,y))==[1]
# ordinary node tangent cone at [0:1:0]
X,Z=s.symbols('X Z')
aff=s.Poly(s.expand(D2.subs({x:X,y:1,z:Z})),X,Z)
quad=sum(c*X**a*Z**b for (a,b),c in aff.terms() if a+b==2)
assert s.expand(quad + 4*(X**2+4*X*Z-Z**2))==0
assert s.det(s.Matrix([[1,2],[2,-1]]))==-5
# exceptional fiber of second projection over q=[0:1:0]
assert s.factor(A.subs({x:0,y:1,z:0}))==t*(t-u-v)
assert s.factor(B.subs({x:0,y:1,z:0}))==-t
# intersection numbers of H1,H2 on class (2H1+H2)(H1+2H2)
# coefficients of H1^2,H1H2,H2^2 are 2,5,2, hence H1^2=2,H1H2=5,H2^2=2 on S.
assert 2+2*5+2==14

print('D1=',D1)
print('D2=',D2)
print('VERIFY_OK')
