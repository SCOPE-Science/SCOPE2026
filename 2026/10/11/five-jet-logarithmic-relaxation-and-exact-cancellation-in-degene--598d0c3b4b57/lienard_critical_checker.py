"""Exact algebra for the critical slow branch of a damped Lienard equation.

Requires SymPy >= 1.10. Numeric dynamics are independent of this checker.
"""
import sympy as sp
x, a, b, c, d = sp.symbols('x a b c d', nonzero=True, real=True)
A, B = sp.symbols('A B')
h = A*x**3+B*x**5
residual = sp.expand(sp.diff(h,x)*h + (a+b*x**2)*h + c*x**3 + d*x**5)
coeff3 = sp.expand(residual).coeff(x,3)
coeff5 = sp.expand(residual).coeff(x,5)
sol = sp.solve([coeff3,coeff5],[A,B], dict=True)
assert len(sol)==1
assert sp.simplify(sol[0][A]+c/a)==0
assert sp.simplify(sol[0][B]+d/a-b*c/a**2+3*c**2/a**3)==0
alpha = c/a
beta = sol[0][B]
gamma = sp.factor(-beta/alpha)
assert sp.simplify(gamma-(d/c-b/a+3*c/a**2))==0
# The curve F=0 is invariant precisely on the logarithm-cancellation locus.
v = sp.symbols('v')
F = v+alpha*x**3
field_F = sp.diff(F,x)*v + sp.diff(F,v)*(-(a+b*x**2)*v-c*x**3-d*x**5)
cofactor = -(a+(b-3*alpha)*x**2)
assert sp.simplify(field_F-cofactor*F-(alpha*b-3*alpha**2-d)*x**5)==0
b_star = a*d/c+3*c/a
assert sp.simplify(gamma.subs(b,b_star))==0
assert sp.simplify((field_F-cofactor*F).subs(b,b_star))==0
# For b=b_star: F'=-(a+a*d*x^2/c)F along every solution.
assert sp.simplify(cofactor.subs(b,b_star)+a+a*d*x**2/c)==0
# Sign-changing logarithmic drift with admissible positive parameters.
assert gamma.subs({a:1,b:0,c:1,d:0})==3
assert gamma.subs({a:1,b:3,c:1,d:0})==0
assert gamma.subs({a:1,b:6,c:1,d:0})==-3
print('CHECK_OK')
