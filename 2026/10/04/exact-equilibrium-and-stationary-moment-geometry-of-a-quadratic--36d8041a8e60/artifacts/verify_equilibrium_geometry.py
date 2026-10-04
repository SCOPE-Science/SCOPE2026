#!/usr/bin/env python3
import sympy as sp

a,b,c,d,e,f,g = sp.symbols('a b c d e f g', positive=True)
x,y,lam,q = sp.symbols('x y lam q', real=True)
A = b*e + c*d
Delta = sp.sqrt(a**2*e**2 + 4*A*c*f)
xp = (-a*e + Delta)/(2*A)
xm = (-a*e - Delta)/(2*A)
P = A*x**2 + a*e*x - c*f
assert sp.simplify(P.subs(x,xp)) == 0
assert sp.simplify(P.subs(x,xm)) == 0

J = sp.Matrix([[0,0,g],[2*d*x,2*e*y,0],[-a-2*b*x,2*c*y,0]])
char = sp.expand((lam*sp.eye(3)-J).det())
expected = sp.expand(lam**3 - 2*e*y*lam**2 + g*(a+2*b*x)*lam - 2*g*y*(a*e+2*A*x))
assert sp.simplify(char-expected) == 0

# Routh-Hurwitz obstruction at the lower-y positive-x equilibrium.
bracket = sp.factor(e*(a+2*b*xp)-Delta)
assert sp.simplify(bracket - c*d*(a*e-Delta)/A) == 0

# Stationary variance factorization.
meanx = (c*f-A*q)/(a*e)
variance = sp.factor(q-meanx**2)
factorized = sp.factor(A**2/(a**2*e**2)*(q-xp**2)*(xm**2-q))
assert sp.simplify(variance-factorized) == 0

# Source parameter set.
subs = {a:4,b:1,c:1,d:1,e:1,f:4,g:1}
xpv = sp.simplify(xp.subs(subs))
xmv = sp.simplify(xm.subs(subs))
y2v = sp.simplify(((f-d*xp**2)/e).subs(subs))
assert sp.simplify(xpv-(sp.sqrt(3)-1)) == 0
assert sp.simplify(xmv-(-sp.sqrt(3)-1)) == 0
assert sp.simplify(y2v-2*sp.sqrt(3)) == 0
ypv = sp.sqrt(2*sp.sqrt(3))
Jp = J.subs(subs).subs({x:xpv,y:ypv})
roots = sp.nroots(sp.expand((lam*sp.eye(3)-Jp).det()), n=20, maxsteps=100)
printed_residual = sp.N((x**2+y**2-4).subs({x:sp.Rational(7321,10000),y:sp.Rational(34641,10000)}),15)

print('A =', A)
print('Delta =', Delta)
print('equilibrium_polynomial_verified = True')
print('characteristic_polynomial_verified = True')
print('routh_bracket =', bracket)
print('variance_factorization_verified = True')
print('source_x_plus =', xpv)
print('source_x_minus =', xmv)
print('source_y_squared =', y2v)
print('source_y_abs_decimal =', sp.N(ypv,15))
print('source_corrected_eigenvalues =', ', '.join(str(sp.N(r,12)) for r in roots))
print('printed_coordinate_equation2_residual =', printed_residual)
print('VERIFY_OK')
