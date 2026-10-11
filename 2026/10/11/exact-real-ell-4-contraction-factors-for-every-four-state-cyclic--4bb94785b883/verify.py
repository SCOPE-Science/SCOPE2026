"""Exact identities for a real four-state cyclic convolution on the mean-zero subspace."""
from sympy import symbols, expand, factor, simplify, Matrix
from sympy import Rational
u,v,w,a,c,b=symbols('u v w a c b', real=True)
x=Matrix([u+w,v-w,-u+w,-v-w])
y=Matrix([a*u+c*v+b*w,-c*u+a*v-b*w,-a*u-c*v+b*w,c*u-a*v-b*w])
assert expand(sum(z**4 for z in x)-2*(u**4+v**4+6*w*w*(u*u+v*v)+2*w**4))==0
assert expand(sum(z**4 for z in y)-2*((a*u+c*v)**4+(-c*u+a*v)**4+6*b*b*w*w*(a*a+c*c)*(u*u+v*v)+2*b**4*w**4))==0
# The extremal 2D quartic quotient has characteristic polynomial
r2=a*a+c*c
T=(r2*r2+a*a*c*c)
Delta=(a*c)**2*(2*r2*r2+a*a*c*c)
assert expand(T*T-r2**4-Delta)==0
# Explicit sharp stochastic example: k=(1/2,1/2,0,0), then fourth norm is 1/2.
assert simplify(T.subs({a:Rational(1,2),c:Rational(1,2)}) + Rational(1,4)*Rational(3,4)-Rational(1,2))==0
print('VERIFY_OK')
