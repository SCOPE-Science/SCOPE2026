#!/usr/bin/env python3
import sympy as sp
from fractions import Fraction
x,y,z,r,k,a,b,c,k1,alpha,d1,d2=sp.symbols('x y z r k a b c k1 alpha d1 d2', nonzero=True)
P=a*x*z/(1+b*x+c*z)
fx=r*x*(1-x/k)-P
fy=k1*P-(alpha+d1)*y
fz=alpha*y-d2*z
Phi=x+y/k1+(alpha+d1)*z/(alpha*k1)
dPhi=sp.diff(Phi,x)*fx+sp.diff(Phi,y)*fy+sp.diff(Phi,z)*fz
C=(alpha+d1)*d2/(alpha*k1)
target=r*x*(1-x/k)-C*z
assert sp.simplify(dPhi-target)==0
sq=sp.expand((x-k/2)**2 + k*C*z/r-k**2/4)
assert sp.simplify(sq + (k/r)*target)==0
R=Fraction(4); K=Fraction(30); K1=Fraction(1,10); A=Fraction(1,10); D1=Fraction(2,25); D2=Fraction(1,20)
Cf=(A+D1)*D2/(A*K1)
coef=K*Cf/R
zmax=R*K/(4*Cf)
assert Cf==Fraction(9,10)
assert coef==Fraction(27,4)
assert zmax==Fraction(100,3)
print('VERIFY_OK')
