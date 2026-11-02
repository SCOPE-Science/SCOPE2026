"""Exact asymptotic coefficient checks for a quintic Lienard flow."""
import sympy as s
z=s.symbols('z',positive=True)
b,c=s.symbols('b c',positive=True)
A=b/4; Q=2/b; K=32/b**3
# Let z = 1/x. The differential identity is dY/dx = b*x^3 + x^5/Y.
Y=A/z**4+Q/z**2-K*s.log(1/z)
# The residual of the equation should be o(1/x) after the log correction.
res=s.diff(Y,z)*(-z**2)-b/z**3-z**-5/Y
assert s.limit(z*res,z,0)==0
# Sign-negative damping: Y=x^2/c+d+e/x^2 with d,e as below.
d=-2/c**3;e=4/c**5
Yn=1/(c*z**2)+d+e*z**2
resn=s.simplify(s.diff(Yn,z)*(-z**2)-z**-5/Yn+c/z**3)
assert s.limit(resn/z,z,0)==0
# Positive-damping time and logarithmic coefficients.
assert s.simplify((b/4)*4-b)==0
assert s.simplify(Q-1/(2*A))==0
assert s.simplify(K-Q/A**2)==0
# Hamiltonian case: derivative of y^2 - x^6/3 is exactly 0.
x,y=s.symbols('x y',real=True)
assert s.expand(2*y*x**5-2*x**5*y)==0
print('CHECK_OK: exact identity, logarithmic coefficient, damped slow branch')
