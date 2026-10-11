#!/usr/bin/env python3
import sympy as s

x,y,z,alpha,eps,iota=s.symbols('x y z alpha eps iota', nonzero=True)
xd=y
yd=-x-y*z
zd=alpha*(y**2-1-eps*z)
Q=z-(y**2-1)/eps
Qdot=s.expand(s.diff(Q,x)*xd+s.diff(Q,y)*yd+s.diff(Q,z)*zd)
expected=-alpha*eps*Q+s.Rational(2,1)*y*(x+y*z)/eps
assert s.simplify(Qdot-expected)==0
on_null=s.factor(Qdot.subs(z,(y**2-1)/eps))
assert s.simplify(on_null-2*y*(eps*x+y**3-y)/eps**2)==0

# Slow graph z = iota*h1 + iota**2*h2 + O(iota**3).
h1=y**2-1
h2=2*x*y/alpha
h=iota*h1+iota**2*h2
xd_i=y
yd_i=-x-y*h
# invariance equation: h_x xdot + h_y ydot = alpha*(h1-h)/iota
lhs=s.diff(h,x)*xd_i+s.diff(h,y)*yd_i
rhs=alpha*(iota*(y**2-1)-h)/iota
res=s.series(s.expand(lhs-rhs),iota,0,2).removeO()
assert s.simplify(res)==0

# Averaged radial field from E'=-iota(y^4-y^2)+O(iota^2).
r,t=s.symbols('r t', positive=True, real=True)
ycirc=-r*s.sin(t)
avg_y2=s.integrate(ycirc**2,(t,0,2*s.pi))/(2*s.pi)
avg_y4=s.integrate(ycirc**4,(t,0,2*s.pi))/(2*s.pi)
assert s.simplify(avg_y2-r**2/s.Integer(2))==0
assert s.simplify(avg_y4-3*r**4/s.Integer(8))==0
f=s.simplify((avg_y2-avg_y4)/r)
assert s.simplify(f-r*(4-3*r**2)/8)==0
rstar=2/s.sqrt(3)
assert s.simplify(f.subs(r,rstar))==0
assert s.simplify(s.diff(f,r).subs(r,rstar)+1)==0
print('VERIFY_OK')
