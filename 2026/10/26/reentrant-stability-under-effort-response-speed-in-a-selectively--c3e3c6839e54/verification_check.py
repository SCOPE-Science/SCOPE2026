#!/usr/bin/env python3
"""Exact-rational verification for reentrant stability in a fishery model.

Requires SymPy; recreates the ODE, equilibrium, Jacobian and Hurwitz conditions.
No external input and no floating-point computations for proof assertions.
"""
from sympy import symbols, Rational, Integer, Matrix, eye, Poly, factor, sqrt, simplify

x,y,z,lam,rho = symbols('x y z lam rho', real=True)
a,d,e,q,m,p,c,m1,m2 = (Rational(21,2),Rational(21,2),Integer(13),Integer(6),Rational(1,2),Integer(1),Integer(1),Integer(1),Integer(1))
f = Matrix([
 x*(1-x)-a*x*y/(x+y),
 e*x*y/(x+y)-d*y-q*m*z*y/(m1*z+m2*y),
 rho*(p*q*m*y*z/(m1*z+m2*y)-c*z)
])
point = {x:Rational(31,52), y:Rational(31,1300), z:Rational(31,650)}
assert all(simplify(t.subs(point))==0 for t in f)
J=f.jacobian([x,y,z]).subs(point).applyfunc(factor)
J_expect=Matrix([[-Rational(281,1352),-Rational(13125,1352),0],[Rational(1,52),Rational(29,156),-Rational(1,3)],[0,4*rho/3,-2*rho/3]])
assert J==J_expect, (J,J_expect)
coeff=tuple(factor(t) for t in Poly((lam*eye(3)-J).det(),lam).all_coeffs())
expected=(Integer(1),(2704*rho+89)/4056,(3724*rho+1201)/8112,775*rho/4056)
assert all(simplify(u-v)==0 for u,v in zip(coeff,expected))
D=factor(coeff[1]*coeff[2]-coeff[3]); assert simplify(D-(10069696*rho**2-2707860*rho+106889)/32902272)==0
low=(Integer(676965)-sqrt(Integer(189196677289)))/Integer(5034848)
high=(Integer(676965)+sqrt(Integer(189196677289)))/Integer(5034848)
assert all(simplify(D.subs(rho,t))==0 for t in (low,high))
assert 0<low<Rational(1,20)<Rational(1,10)<high<Rational(1,4)
assert D.subs(rho,Rational(1,100))>0
assert D.subs(rho,Rational(1,10))<0
assert D.subs(rho,Integer(1))>0
assert D.diff(rho).subs(rho,low)<0 and D.diff(rho).subs(rho,high)>0
for rr in (Rational(1,100),Rational(1,10),Integer(1)):
  abc=[s.subs(rho,rr) for s in coeff[1:]]
  assert all(t>0 for t in abc)
  sign='stable' if D.subs(rho,rr)>0 else 'unstable'
  print('rho=',rr,'Delta=',D.subs(rho,rr),'label=',sign)
print('J=',J)
print('coefficients=',coeff)
print('Delta=',D)
print('critical rhos=',low,high)
print('PASS: exact equilibrium, Jacobian, cubic, quadratic roots, sign and transversality')
