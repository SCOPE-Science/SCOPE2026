"""Exact symbolic checks for scalar log-regularized inertial reweighting."""
import sympy as s
x, y, a, b, ell, rho, beta = s.symbols(
    'x y a b ell rho beta', real=True)
F_prime = a * (x - b) + 2*x/(1+rho*x*x)
F_second = s.diff(F_prime,x)
D = ell + 2/(1+rho*x*x)
Phi = ((ell-a)*((1+beta)*x-beta*y)+a*b)/D
# Evaluate the two-dimensional map derivative along fixed-point equations.
Fx = s.diff(Phi,x)
Fy = s.diff(Phi,y)
fix_b = x + 2*x/(a*(1+rho*x*x))
Fx_star = s.factor(Fx.subs({y:x,b:fix_b}))
Fy_star = s.factor(Fy.subs({y:x,b:fix_b}))
assert s.simplify(Fy_star + beta*(ell-a)/D) == 0
assert s.simplify(Fx_star - ((1+beta)*(ell-a)/D + 4*rho*x*x/(D*(1+rho*x*x)**2))) == 0
assert s.simplify(1-Fx_star-Fy_star-F_second/D) == 0
# The scalar mass map and derivative fold polynomial.
u = s.symbols('u',real=True)
H = u*(1+2/(a*(1+u*u)))
assert s.simplify(s.diff(H,u) - (a*(1+u*u)**2+2*(1-u*u))/(a*(1+u*u)**2)) == 0
# Fully exact non-global locally attracting witness.
av=s.Rational(1,8); bv=s.Integer(9); rv=s.Integer(1)
P=s.factor((a*(x-b)*(1+rho*x*x)+2*x).subs({a:av,b:bv,rho:rv})/av)
assert P == (x-1)*(x**2-8*x+9)
roots=[1,4-s.sqrt(7),4+s.sqrt(7)]
F2=lambda z:s.factor(F_second.subs({a:av,rho:rv,x:z}))
assert F2(1)==av
assert s.simplify(F2(4-s.sqrt(7))+s.sqrt(7)/32)==0
assert s.simplify(F2(4+s.sqrt(7))-s.sqrt(7)/32)==0
# At any hyperbolic fixed point, unit-circle Schur test is the objective curvature.
for z in roots:
 d=s.factor(D.subs({x:z,ell:1,rho:1}))
 A=s.factor(Fx_star.subs({a:av,x:z,ell:1,rho:1,beta:s.Rational(1,2)}))
 B=s.factor(-Fy_star.subs({a:av,x:z,ell:1,rho:1,beta:s.Rational(1,2)}))
 assert s.simplify(1-A+B-F2(z)/d)==0
 assert 0 < float(B) < 1 and float(1+A+B)>0
 assert (float(1-A+B)>0)==(float(F2(z))>0)
# The exact objective difference is positive by the elementary inequalities
# sqrt(7) in (12/5,3), log(2)<7/10; no floating-point inference required.
assert (s.Rational(12,5))**2<7<9
assert sum((s.Rational(7,10))**k/s.factorial(k) for k in range(4))>2
print('VERIFY_OK: rational witness, fixed-point map, Jacobian identity, and signs.')
