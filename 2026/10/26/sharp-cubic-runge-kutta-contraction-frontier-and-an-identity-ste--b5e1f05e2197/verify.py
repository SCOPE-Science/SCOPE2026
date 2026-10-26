"""Exact symbolic checks for a cubic Runge--Kutta contraction boundary.

All identities are over the rational polynomial ring and do not use sampled
approximations as certificates for universal assertions.
"""
import sympy as sp

a,b,h,beta=sp.symbols('a b h beta', positive=True, real=True)
L=sp.Matrix([[0,-a],[a,-b]])
P=sp.eye(2)+h*L+sp.Rational(1,2)*h*h*L*L+beta*h**3*L**3
D=sp.expand(P.T*P-sp.eye(2))
tr=sp.factor(sp.trace(D)); det=sp.factor(D.det())
assert sp.simplify(sp.expand(det).coeff(h,4)-a*a*b*b*(1-4*beta))==0
assert sp.simplify(sp.expand(det).coeff(h,5)-a*a*b*(8*a*a*beta-a*a-b*b)/2)==0
assert sp.simplify(sp.diff(tr,h).subs(h,0)+2*b)==0
Pedge=sp.simplify(P.subs({beta:sp.Rational(1,4),b:a}))
assert Pedge.subs(h,2/a)==sp.eye(2)
tr_edge=sp.factor(tr.subs({beta:sp.Rational(1,4),b:a}))
det_edge=sp.factor(det.subs({beta:sp.Rational(1,4),b:a}))
x=sp.symbols('x', real=True)
assert sp.simplify(tr_edge.subs(h,x/a)-x*(x-2)*(x*x-2*x+2)*(x*x+2*x+4)/8)==0
assert sp.simplify(det_edge.subs(h,x/a)-x**6*(x-2)**2*(x**4+16)/256)==0
# Exact rational reentrant contraction certificate.
Q=sp.simplify(P.subs({beta:sp.Rational(1,4),a:1,b:sp.Rational(11,10),h:1}))
assert Q == sp.Matrix([[sp.Rational(31,40),-sp.Rational(201,400)],[sp.Rational(201,400),sp.Rational(889,4000)]])
E=Q.T*Q-sp.eye(2)
assert sp.trace(E)==-sp.Rational(13519479,16000000)
assert E.det()==sp.Rational(1269,50000)
# Imaginary-axis modulus of the marginal polynomial.
y=sp.symbols('y',real=True)
z=sp.I*y
R=lambda z:1+z+z*z/2+z**3/4
assert sp.simplify(sp.expand_complex(R(z)*R(-z)-1)-y**4*(y*y-4)/16)==0
print('Exact polynomial identities, a=b threshold, and rational reentrant certificate: PASS')
print('R(a=b, h=2/a)=I, determinant and trace factorizations: PASS')
print('R(a=1,b=11/10,h=1) =',Q)
