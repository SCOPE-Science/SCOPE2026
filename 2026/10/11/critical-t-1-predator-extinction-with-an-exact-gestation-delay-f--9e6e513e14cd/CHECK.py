#!/usr/bin/env python3
"""Exact symbolic checks for a delayed three-species food-chain threshold theorem.
Requires SymPy. The long-time convergence proof is analytic in RESULT.md.
"""
import sympy as s
x, y, z, xp, yp, zp = s.symbols('x y z xp yp zp', positive=True)
r, k, b, a, alpha, m, beta, theta, v, p, q, eta, e, tau = s.symbols(
    'r k b a alpha m beta theta v p q eta e tau', positive=True)
f = r*x/(1+k*y)-b*x-a*x**2-alpha*x*y/(x+m*y)
g = beta*xp*yp/(xp+m*yp)-beta*y-theta*y*z/(v+p*y+q*z)
Pprime = g + beta*(y-yp)
expect = -beta*m*yp**2/(xp+m*yp)-theta*y*z/(v+p*y+q*z)
assert s.simplify(Pprime-expect) == 0
# First-order center variable and delay-shift expansion; unknown quadratic derivative d2.
X, eps = s.symbols('X eps', positive=True)
c1, d2 = s.symbols('c1 d2', real=True)
y_p = eps - tau*d2*eps**2
x_p = X + c1*eps
production = beta*x_p*y_p/(x_p+m*y_p)
quadratic = s.expand(s.series(production-beta*eps-d2*eps**2, eps, 0, 3).removeO()).coeff(eps,2)
sol = s.solve(quadratic,d2)
assert len(sol) == 1
assert s.simplify(sol[0] + beta*m/(X*(1+beta*tau))) == 0
# Strictly positive coexistence-absence counterexample above the conversion threshold.
param = {r:s.Rational(9,2),k:1,b:1,a:1,alpha:s.Rational(1,2),m:1,
         beta:2,theta:1,v:1,p:1,q:1,eta:1,e:1}
f2 = beta*x*y/(x+m*y)-y-theta*y*z/(v+p*y+q*z)
f3 = eta*y*z/(v+p*y+q*z)-e*z
fs = s.Matrix([f,f2,f3])
stationary = s.simplify(fs.subs(param).subs({x:1,y:1,z:0}))
assert stationary == s.zeros(3,1)
J = s.simplify(fs.jacobian([x,y,z]).subs(param).subs({x:1,y:1,z:0}))
assert J[:2,:2] == s.Matrix([[-s.Rational(7,8),-s.Rational(5,4)],
                             [s.Rational(1,2),-s.Rational(1,2)]])
assert J[2,2] == -s.Rational(1,2)
assert s.trace(J[:2,:2]) == -s.Rational(11,8)
assert J[:2,:2].det() == s.Rational(17,16)
print('CHECK_OK exact energy identity, quadratic coefficient, and sharpness example')
