"""Standalone symbolic consistency checks for the stated Hankel asymptotic.

The maximization and the analytic-function existence argument are proved in RESULT.md.
"""
import sympy as S

alpha, c1, c2, c3, u = S.symbols('alpha c1 c2 c3 u', positive=True)
v = 1 - u
w1 = 2*c1/(1+alpha)
w2 = (2*c2 + alpha*w1**2)/(1+2*alpha)
w3 = (2*c3 + 3*alpha*w1*w2-alpha*w1**3)/(1+3*alpha)
a2 = w1
a3 = (w2+w1**2)/2
a4 = (w3+3*a2*a3-a2**3)/3
H = S.factor(a2*a4-a3**2)
assert S.simplify(S.limit(alpha**2*H,alpha,S.oo) - (16*c1*c3-9*c2**2)/36) == 0

A = 7*u**2
B = 14*u*v
C = v*(9+7*u)
xi = S.symbols('xi',real=True)
q = S.expand((A+C)**2+B**2+2*B*(A-C)*xi-4*A*C*xi**2)
assert S.factor(S.diff(q,xi).subs(xi,-1)-28*u*(1-u)*(28*u**2+20*u-9)) == 0
assert S.factor((A-B-C)-(28*u**2-12*u-9)) == 0
assert S.factor(S.diff(28*u**2-12*u-9,u).subs(u,S.Rational(3,14))) == 0
assert S.factor((28*u**2-12*u-9).subs(u,S.Rational(3,14))+S.Rational(72,7)) == 0
assert S.factor((A+C)**2*(1+B**2/(4*A*C))-16*(9-2*u)**2/(9+7*u)) == 0
assert S.simplify(S.diff(16*(9-2*u)**2/(9+7*u),u).subs(u,S.Rational(2,7))) < 0
assert S.simplify(16*(S.Rational(59,7))**2/11 < (S.Rational(72,7))**2)
assert S.simplify(S.Rational(72,7)/36-S.Rational(2,7)) == 0

# For the extremal two-point moment measure c_k=cos(k theta), cos(theta)^2=3/14.
r=S.sqrt(S.Rational(3,14))
cc1=r; cc2=2*r*r-1; cc3=4*r**3-3*r
assert S.simplify(16*cc1*cc3-9*cc2**2+S.Rational(72,7)) == 0
for t in (20,100,1000):
    numeric = float(abs(H.subs({alpha:t,c1:cc1,c2:cc2,c3:cc3}))*t*t)
    assert abs(numeric-2/7)<1.0/t, (t,numeric)
print('CHECK_OK: coefficient reduction, moment boundary, two regimes, extremal leading law')
