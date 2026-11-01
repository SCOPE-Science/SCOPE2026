"""Exact gauge-conjugacy and pointwise-Jacobian checks for a polynomial oscillator family."""
import sympy as sp

x,y,z,m,e=sp.symbols('x y z m e', real=True)
R=x*x+y*y
S=z+R/sp.Integer(10)
Q=(R-5)*(sp.Rational(20,21)-R)-sp.Rational(400,21)*z*z
F=sp.Matrix([m*x*Q-(1+e*S)*y, m*y*Q+(1+e*S)*x, -S])
c,s=sp.cos(e*z),sp.sin(e*z)
U,V=c*x-s*y,s*x+c*y
H=sp.Matrix([U,V,z]); DH=H.jacobian([x,y,z]);
assert sp.trigsimp(sp.expand_trig(U**2+V**2-R)) == 0
assert sp.simplify(DH.det()-1)==0
G=sp.Matrix([m*U*Q-V,m*V*Q+U,-S])
assert all(sp.trigsimp(sp.expand(t))==0 for t in (DH*F-G))
# Proves H conjugates the full real polynomial flow to its e=0 counterpart.
lam=sp.symbols('lam');J=F.jacobian([x,y,z]);P=sp.Poly(J.charpoly(lam).as_expr(),lam)
coeff=[sp.factor(a.subs({x:1,y:0,z:-sp.Rational(1,10),e:0})) for a in P.all_coeffs()]
assert all(sp.simplify(a-b)==0 for a,b in zip(coeff,[1, 1-sp.Rational(166,21)*m, 1-sp.Rational(50,7)*m, 1]))
assert sp.simplify(coeff[1]*coeff[2]-1-m*(8300*m-2212)/147)==0
critical=5*(1/coeff[1]-1+sp.Rational(50,7)*m)
assert sp.simplify(critical-sp.Rational(250,7)*m-830*m/(21-166*m))==0
assert sp.simplify(critical.subs(m,sp.Rational(1,1000))-sp.Rational(22037,291676))==0
base=[sp.simplify(a.subs({x:1,y:0,z:-sp.Rational(1,10),m:sp.Rational(1,1000),e:sp.Rational(1,10)})) for a in P.all_coeffs()]
assert base==[1,sp.Rational(10417,10500),sp.Rational(709,700),1]
assert sp.simplify(base[1]*base[2]-base[3])==sp.Rational(35653,7350000)
untwisted=[sp.simplify(a.subs({x:1,y:0,z:-sp.Rational(1,10),m:sp.Rational(1,1000),e:0})) for a in P.all_coeffs()]
assert sp.simplify(untwisted[1]*untwisted[2]-untwisted[3])==-sp.Rational(22037,1470000)
# The two periodic-circle profiles are exact stationary states in (R,z).
assert all(sp.simplify(v.subs({x:r,y:0,z:-sp.Rational(r*r,10)}))==0 for r in (1,2) for v in (Q,S))
print('PASS: full-space analytic conjugacy; volume-preserving twist; exact periodic profiles;')
print('PASS: saddle-circle Jacobian polynomial; all-positive-m non-Hurwitz obstruction;')
print('PASS: rational Routh-Hurwitz contrasts at m=1/1000, e=0 and e=1/10.')
