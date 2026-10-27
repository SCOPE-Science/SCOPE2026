#!/usr/bin/env python3
"""Exact symbolic checks for a two-community directed-contact replicator."""
import sympy as sp

a,b,R,p,K,w11,u,v,w22=sp.symbols('a b R p K w11 u v w22', positive=True)
e=b/(a+b)
f=a/(a+b)
kap=p*(1-p)*K
A0=R*f*u+a
B0=R*e*v+b
X0=R*e*u+b
Y0=R*f*v+a
g1=e*(e*w11+f*u)
g2=f*(e*v+f*w22)
C=sp.Matrix([[-A0,X0],[Y0,-B0]])
L=C-kap*sp.Matrix([g1,g2])*sp.Matrix([[1,1]])
assert all(sp.cancel(q)==0 for q in C*sp.Matrix([e,f]))
assert sp.cancel(C.det())==0
assert sp.cancel(L.trace()+A0+B0+kap*(g1+g2))==0
assert sp.cancel(L.det()-kap*((B0+Y0)*g1+(A0+X0)*g2))==0

eta,s1,s2=sp.symbols('eta s1 s2')
W=sp.Matrix([[10,1],[5,1]])
alpha=beta=sp.Rational(1,20)
h=[eta,1-eta]
x=[s1,s2]
z=[h[i]-x[i] for i in range(2)]
y=s1+s2
rA=sp.Rational(3,2)-y
rB=sp.Rational(1,2)+y
F=[sum(W[i,j]*(z[i]*x[j]*rA-x[i]*z[j]*rB) for j in range(2)) for i in range(2)]
ODE=sp.Matrix([-alpha*eta+beta*(1-eta),
               beta*s2-alpha*s1+F[0],
               alpha*s1-beta*s2+F[1]])
pt={eta:sp.Rational(1,2),s1:sp.Rational(1,4),s2:sp.Rational(1,4)}
assert ODE.subs(pt)==sp.zeros(3,1)
J=sp.simplify(ODE.jacobian([eta,s1,s2]).subs(pt))
Jexpected=sp.Matrix([[-sp.Rational(1,10),0,0],
                     [sp.Rational(1,2),-sp.Rational(77,40),-sp.Rational(33,40)],
                     [-sp.Rational(5,2),sp.Rational(9,5),-sp.Rational(33,10)]])
assert J==Jexpected
l=sp.symbols('l')
poly=sp.factor(J.charpoly(l).as_expr())
expected=(l+sp.Rational(1,10))*(l*l+sp.Rational(209,40)*l+sp.Rational(627,80))
assert sp.simplify(poly-expected)==0
assert sp.Rational(209,40)**2-4*sp.Rational(627,80)==-sp.Rational(6479,1600)
print('PASS: general identities and exact oscillatory witness')
