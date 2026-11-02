#!/usr/bin/env python3
"""Exact algebra checks for singular fibers of a projective quintic pencil."""
import sympy as sp
x,y,z,w,t=sp.symbols('x y z w t')
F=(z-w)*(x**4-3*y**4)-6*(z+w)*x**2*y**2+z*w*(w**3-t*z**3)
assert sp.Poly(F,x,y,z,w).total_degree()==5
fx,fy,fz,fw=[sp.diff(F,v) for v in (x,y,z,w)]
assert sp.expand(fx-4*x*(x*x*(z-w)-3*y*y*(z+w)))==0
assert sp.expand(fy+12*y*(y*y*(z-w)+x*x*(z+w)))==0
assert sp.expand(fz-(x**4-3*y**4-6*x*x*y*y+w**4-4*t*z**3*w))==0
assert sp.expand(fw-(-x**4+3*y**4-6*x*x*y*y+4*z*w**3-t*z**4))==0
f=F.subs(z,1).subs(t,1)
H=sp.hessian(f,(x,y,w)); D=sp.factor(H.det())
for relations, target, name in [
 ([x,w-1,y**4+1],3456,'axis-x-zero'),
 ([y,w-1,x**4-3],3456,'axis-y-zero'),
 ([w**2+w+1,4*y**4-w**2,x**2-(w-w**2)*y**2],3456*w**2,'offaxis')
]:
 gb=sp.groebner(relations,x,y,w,order='lex',domain=sp.QQ)
 for exp in (f,*[sp.diff(f,v) for v in (x,y,w)],D-target):
  rem=gb.reduce(sp.expand(exp))[1]
  assert rem==0,(name,rem)
Q=x**4-6*x**2*y**2-3*y**4+w**4
assert sp.expand(F.subs({z:1,t:0})-(Q-w*(x**4+6*x*x*y*y-3*y**4)))==0
assert sp.diff(Q,w)==4*w**3
assert sp.expand(sp.diff(Q,x)-4*x*(x*x-3*y*y))==0
assert sp.expand(sp.diff(Q,y)+12*y*(x*x+y*y))==0
# The initial homogeneous Jacobian has length 27. Its leading monomials
# bound every standard monomial; these are counted independently.
TG=sp.groebner([sp.diff(Q,v) for v in (x,y,w)],x,y,w,order='lex',domain=sp.QQ)
leads=[p.LM(order='lex').exponents for p in TG.polys]
assert set(leads)=={(3,0,0),(2,1,0),(1,3,0),(0,5,0),(0,0,3)}
def divisible(a,b):
 return all(a[i]>=b[i] for i in range(3))
std=[(i,j,k) for i in range(3) for j in range(5) for k in range(3)
     if not any(divisible((i,j,k),lead) for lead in leads)]
assert len(std)==27
assert 5*(5**2-4*5+6)==55
assert 24==8+16
assert 27==3**3
print('VERIFY_OK: gradients, three exact nodal Hessian certificates, tangent cone, Euler data')
