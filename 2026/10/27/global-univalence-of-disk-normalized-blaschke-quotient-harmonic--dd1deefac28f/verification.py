"""Exact symbolic identities for the harmonic convolution theorem."""
import sympy as S
x,y,z,w=S.symbols('x y z w', real=True)
D=1-x*x-x*y-y*y
Gamma=z*(z+x)*(1-y*z)/((1+x*z)*(z-y))
cm1=y*(x+y)*(1-y*y)/(1+x*y)
assert S.cancel(S.residue(Gamma,z,y)-cm1)==0
reg=S.cancel(Gamma-cm1/(z-y))
for n,expect in [(1,D/(1+x*y)),(2,-(1-x*x)*(x+y)/(1+x*y)),(3,x*(1-x*x)*(x+y)/(1+x*y))]:
 der=S.diff(reg,z,n).subs(z,0)/S.factorial(n)
 assert S.factor(der-expect)==0,(n,der,expect)
mu=(1-x*x)*(x+y)/D
nu=y*(x+y)*(1-y*y)/D
assert S.factor(mu-x-y*(1+x*y)/D)==0
r=x*x; s=y*y; d=mu**2-r
H=z+mu**2*z*z/(1-r*z)
G=nu**2*z/(1-s*z)
assert S.factor((H-H.subs(z,w))/(z-w)-(1+d*(z+w)-r*d*z*w)/((1-r*z)*(1-r*w)))==0
assert S.factor((G-G.subs(z,w))/(z-w)-nu**2/((1-s*z)*(1-s*w)))==0
Lambda=1-mu**2*(2+r)/(1+r)**2-nu**2/(1-s)**2
positive=(1-x*x)*(1+x+(x*x-x+2)*y)*(1-x-(x*x+x+2)*y)/((1+x*x)**2*D**2)
assert S.factor(Lambda-positive)==0
assert S.factor(D.subs(y,(1-x)/(3+x))-(1-x)*(1+x)*(x*x+5*x+8)/(3+x)**2)==0
for X,Y in [(S.Rational(1,2),S.Rational(1,10)),(S.Rational(10,11),S.Rational(1,44)),(S.Rational(99,100),S.Rational(1,500)),(S.Rational(1,3),S.Rational(0))]:
 assert Y<(1-X)/(3+X)
 assert S.factor(Lambda.subs({x:X,y:Y}))>0
print('PASS: exact Laurent coefficients, convolution divided differences, parameter positivity and gap factorization')
