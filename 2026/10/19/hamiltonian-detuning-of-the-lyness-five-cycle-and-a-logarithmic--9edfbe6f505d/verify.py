"""Standalone exact algebra and independent numerical checks for a positive Lyness-map detuning theorem."""
import sympy as s
x,y,a=s.symbols('x y a', positive=True)
V=lambda A,X,Y:(1+X)*(1+Y)*(A+X+Y)/(X*Y)
F=lambda A,X,Y:(Y,(A+Y)/X)
X,Y=x,y
for _ in range(5): X,Y=F(a,X,Y)
assert s.cancel(X.subs(a,1)-x)==0
assert s.cancel(Y.subs(a,1)-y)==0
H=V(1,x,y)
U=s.cancel(x*y*s.diff(H,y)/H)
W=s.cancel(-x*y*s.diff(H,x)/H)
assert s.factor(s.diff(X,a).subs(a,1)-U)==0
assert s.factor(s.diff(Y,a).subs(a,1)-W)==0
p,q=F(a,x,y)
assert s.factor(V(a,p,q)-V(a,x,y))==0
assert s.factor(s.diff(p,x)*s.diff(q,y)-s.diff(p,y)*s.diff(q,x)-p*q/(x*y))==0
assert s.factor(s.diff(H,x)*U+s.diff(H,y)*W)==0
phi=(1+s.sqrt(5))/2
rcrit=s.simplify(H.subs({x:phi,y:phi}))
assert s.simplify(rcrit-(11+5*s.sqrt(5))/2)==0
u,v=s.symbols('u v', real=True)
Hs=s.log(1+s.exp(u))+s.log(1+s.exp(v))+s.log(1+s.exp(u)+s.exp(v))-u-v
Hess=s.hessian(Hs,(u,v)).subs({u:s.log(phi),v:s.log(phi)})
assert s.simplify(s.det(Hess)-(25-11*s.sqrt(5))/2)==0
vertices=[(-1,0),(0,-1),(1,0),(1,1),(0,1)]
doubled=sum(vertices[i][0]*vertices[(i+1)%5][1]-vertices[i][1]*vertices[(i+1)%5][0] for i in range(5))
assert doubled==5
# Numerical central derivative consistency at the unique fixed point:
import math
for e in [1e-3,1e-4,1e-5]:
 aa=1+e
 q=(1+math.sqrt(1+4*aa))/2
 trace=1/q
 # F_a matrix [[0,1],[-1,1/q]]; clockwise positive rotation near equilibrium.
 rho=math.acos(trace/2)/(2*math.pi)
 fd=(rho-.2)/e
 expected=math.sqrt((25-11*math.sqrt(5))/2)/(10*math.pi)
 assert abs(fd-expected)<1e-3
print('VERIFY_OK')
