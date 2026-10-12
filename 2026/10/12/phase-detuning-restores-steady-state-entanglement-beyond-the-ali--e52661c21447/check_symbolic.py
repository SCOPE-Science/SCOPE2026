"""Exact algebraic checks of the covariance invariant and scalar optimum identities."""
import sympy as s

a, h, u, v, w = s.symbols('a h u v w', real=True)
V = s.Matrix([
[a+h*u, h*v, 0, -h*w],
[h*v, a-h*u, -h*w, 0],
[0, -h*w, a+h*u, -h*v],
[-h*w, 0, -h*v, a-h*u]
])
assert s.factor(V[:2,:2].det()-(a*a-h*h*(u*u+v*v))) == 0
assert s.factor(V[:2,2:].det()+h*h*w*w) == 0
assert s.factor(V.det()-(a*a-h*h*(u*u+v*v+w*w))**2) == 0
m = s.symbols('m', positive=True)
chi2 = m*(1-m)
coef = 1-m*m
z2 = m/(1-m*m)
# Squared critical stationarity and critical objective identities.
assert s.factor(coef**2*z2-chi2*(1+coef*z2)) == 0
assert s.simplify((1+m)*(s.sqrt(1+m)-m/s.sqrt(1+m))**2-1) == 0
# Exact threshold polynomial discriminant (up to factor four).
b=s.symbols('b', positive=True)
disc = s.factor(b*b*chi2-(1-m)*(1-b*b))
assert s.factor(disc-(1-m)*(b*b*(1+m)-1)) == 0
print('SYMBOLIC_OK: covariance block and determinant identities; phase-optimum stationarity; threshold discriminant')
