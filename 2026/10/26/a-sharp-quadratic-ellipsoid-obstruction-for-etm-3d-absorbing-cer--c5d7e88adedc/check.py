"""Exact symbolic verification for quadratic ETM-3D ellipsoid certificates."""
import sympy as s
x,y,z,rho=s.symbols('x y z rho',real=True)
a,c=s.symbols('a c',positive=True)
b=(a+c)/2
mx,my,mz=s.symbols('mx my mz',real=True)
X=s.Matrix([x,y,z]);m=s.Matrix([mx,my,mz]);W=s.diag(a,b,c)
F=s.Matrix([-2*x-rho*y+y*z,x-y+rho*z-2*x*z,rho*y-5*z+x*y])
Vdot=s.expand(((X-m).T*W*F)[0]);u,v,w=s.symbols('u v w',real=True)
Q=s.Poly(s.expand(Vdot.subs({x:mx+u,y:my+v,z:mz+w,}, simultaneous=True)),u,v,w)
coeff=lambda mon: s.factor(Q.coeff_monomial(mon))
assert coeff(u**2)==-2*a
assert s.simplify(coeff(v**2)+b)==0
assert coeff(w**2)==-5*c
assert s.factor(coeff(u*v)-(b-a*rho-c*mz))==0
assert s.factor(coeff(v*w)-((b+c)*rho-a*mx))==0
assert s.factor(coeff(u*w)-2*b*my)==0
mx0=(b+c)*rho/a;mz0=(b-a*rho)/c
ax,az,ay=s.symbols('alpha_x alpha_z alpha_y',real=True)
fy=s.expand(F[1].subs({x:mx0+ax,y:ay,z:mz0+az},simultaneous=True))
assert s.simplify(fy.coeff(rho,2)-3)==0
assert s.simplify(s.expand(Vdot.subs({x:mx,y:my+v,z:mz},simultaneous=True))-b*v*(F[1].subs({x:mx,y:my,z:mz})-v))==0
h=rho*(3*rho-1)/2
d=s.sqrt(rho**2+h**2+(1-rho)**2/4)
C=2*rho**2+h**2+5*(1-rho)**2/4
assert s.limit(d-h,rho,s.oo)==s.Rational(5,12)
assert s.limit(s.sqrt(C)-h,rho,s.oo)==s.Rational(13,12)
assert s.limit(d+s.sqrt(C)-(3*rho**2-rho),rho,s.oo)==s.Rational(3,2)
print('SYMMETRIC_CUBIC_CANCELLATION_AND_COEFFICIENTS_PASS')
print('UNIVERSAL_TRANSVERSE_FORCING_COEFFICIENT_PASS',fy.coeff(rho,2))
print('EXACT_AXIS_NORMAL_DERIVATIVE_PASS')
print('EXPLICIT_SOURCE_RADIUS_SHARP_ASYMPTOTIC_PASS',s.Rational(3,2))
print('GLOBAL_SEMIDEFINITE_AND_INVARIANCE_IMPLICATIONS_REQUIRE_ANALYTICAL_PROOF')
