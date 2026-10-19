"""Exact symbolic checks for a nonlinear epidemic-adherence equilibrium theorem.

Requires Python 3.10+ and SymPy. Run: python check.py
"""
import sympy as sp
x=sp.symbols('x', real=True); z=sp.Symbol('z')
Q=lambda p,q=1: sp.Rational(p,q)
mu,delta,gamma,beta=Q(1,10),Q(9,10),Q(1),Q(33,10)
a,e,kap,c,xi,eps=Q(9,10),Q(1,10),Q(1),Q(503,300),Q(800,297),Q(1,100)
b=(1-a*x)*(1-e*x)
E=Q(1,2)*(1-Q(1)/(3*b))
S=(gamma+mu)/(beta*b)
alpha=-c+a*xi*beta*E*(1-e*x)+kap*(2*x-1)
poly=1440*x*x-409*x+10
assert sp.simplify(alpha-poly/(100*(9*x-10)))==0
assert sp.discriminant(poly,x)==109681
for low,high in [(Q(27,1000),Q(28,1000)),(Q(257,1000),Q(258,1000))]:
 assert poly.subs(x,low)*poly.subs(x,high)<0
 assert sp.simplify((3*b-1).subs(x,high))>0
rlo=(409-sp.sqrt(109681))/2880
rhi=(409+sp.sqrt(109681))/2880
assert  Q(27,1000)<rlo<Q(28,1000)
assert Q(257,1000)<rhi<Q(258,1000)
assert sp.simplify(sp.diff(alpha,x).subs(x,rlo))>0
assert sp.simplify(sp.diff(alpha,x).subs(x,rhi))<0
h=eps*x*(1-x)
J=sp.Matrix([
[-(mu+delta)-beta*b*E,-(delta+gamma+mu),-beta*sp.diff(b,x)*S*E],
[beta*b*E,0,beta*sp.diff(b,x)*S*E],
[0,h*a*xi*beta*(1-e*x),h*(2*kap-a*e*xi*beta*E)]])
A=mu+delta+beta*b*E; B=delta+gamma+mu; C=beta*b*E
u=-beta*sp.diff(b,x)*S*E
v=h*a*xi*beta*(1-e*x)
w=h*(2*kap-a*e*xi*beta*E)
cc1=A-w
cc2=B*C-A*w+u*v
cc3=(mu+delta)*u*v-B*C*w
coeff=sp.Poly(J.charpoly(z).as_expr(),z).all_coeffs()
assert sp.simplify(coeff[1]-cc1)==0
assert sp.simplify(coeff[2]-cc2)==0
assert sp.simplify(coeff[3]-cc3)==0
assert sp.simplify(cc3+B*C*h*sp.diff(alpha,x))==0
assert sp.simplify(cc1*cc2-cc3-(A*B*C-A*A*w+A*w*w+u*v*(C-w)))==0
assert alpha.subs(x,0)==-Q(1,100)
assert (b.subs(x,1)*3)==Q(27,100)
assert c-kap==Q(203,300)
# Rigorous inequalities valid on 0<x<13/50 at an endemic equilibrium:
assert b.subs(x,Q(13,50))>Q(7,10)
assert Q(33,10)*Q(7,10)*Q(1,4)==Q(231,400)
assert 2*Q(231,400)-Q(53,20)*Q(1,200)>0
assert 2*Q(231,400)-Q(53,20)**2*Q(1,200)>0
print('PASS: algebraic reduction, two rational root brackets, derivative signs, exact Jacobian identities, Routh bounds')
print('adherence roots:',[sp.N(r,15) for r in (rlo,rhi)])
print('prevalence roots:',[sp.N(E.subs(x,r),15) for r in (rlo,rhi)])
