#!/usr/bin/env python3
"""Symbolic checks for Lorenz-84 balance identities used in the record."""
import sympy as sp

x,y,z,a,b,F,G=sp.symbols('x y z a b F G', real=True)
R=y**2+z**2
fx=a*(F-x)-R
fy=(x-1)*y-b*x*z+G
fz=b*x*y+(x-1)*z
U=F-x
E=(x**2+y**2+z**2)/2

checks={}
checks['U_identity_residual']=sp.simplify(-fx-(R-a*U))
Edot=sp.diff(E,x)*fx+sp.diff(E,y)*fy+sp.diff(E,z)*fz
checks['energy_identity_residual']=sp.factor(Edot-(-a*x**2-R+a*F*x+G*y))
Rdot=sp.diff(R,y)*fy+sp.diff(R,z)*fz
checks['eddy_identity_residual']=sp.factor(Rdot-(2*(x-1)*R+2*G*y))
div=sp.diff(fx,x)+sp.diff(fy,y)+sp.diff(fz,z)
checks['divergence_residual']=sp.simplify(div-(2*x-a-2))
m,m2=sp.symbols('m m2', real=True)
ER=a*(F-m)
EXR=a*(F*m-m2)
cov=sp.expand(EXR-m*ER)
checks['covariance_identity_residual']=sp.expand(cov+a*(m2-m**2))
for name,val in checks.items():
    print(f'{name} = {sp.simplify(val)}')
assert all(sp.simplify(v)==0 for v in checks.values())
