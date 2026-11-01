"""Symbolic checks of the asymmetric hyperbolic two-cap expansion.

Expands the independent cap contributions from exact hyperbolic formulas;
checks cancellations, fixed-area coefficients, and critical minimizer algebra.
"""
import sympy as sp

v,a=sp.symbols('v a',positive=True,real=True)
s=sp.sqrt(v); c=sp.sqrt(v+1)
A=v*(sp.cos(a)-1)+sp.sqrt(1+v*sp.sin(a)**2)-1
B=2*s*c*(sp.cos(a)-1)+s*sp.sin(a)*sp.atan(c*sp.tan(a))
a_series=sp.series(A,a,0,8).removeO().expand()
b_series=sp.series(B,a,0,8).removeO().expand()
assert sp.simplify(a_series.coeff(a,2))==0
assert sp.simplify(b_series.coeff(a,2))==0
assert sp.simplify(a_series.coeff(a,4)+v*(v+1)/8)==0
assert sp.simplify(a_series.coeff(a,6)-v*(v+1)*(3*v+1)/48)==0
assert sp.simplify(b_series.coeff(a,4)+s*c*(4*v+1)/12)==0
assert sp.simplify(b_series.coeff(a,6)-s*c*(36*v*v+22*v+1)/180)==0
fixed=sp.expand(b_series-(1+2*v)/(s*c)*a_series)
assert sp.simplify(fixed.coeff(a,4)-s*c*(1-2*v)/24)==0
assert sp.simplify(fixed.coeff(a,6)-s*c*(54*v*v+13*v-11)/720)==0
x=sp.symbols('x',nonnegative=True)
f=-sp.sqrt(3)*x*x/48+sp.pi*sp.sqrt(3)*x*x*x/80
root=sp.Rational(10,9)/sp.pi
assert sp.simplify(sp.diff(f,x).subs(x,root))==0
assert sp.simplify(sp.diff(f,x,2).subs(x,root)-sp.sqrt(3)/24)==0
assert sp.simplify(f.subs(x,root)+25*sp.sqrt(3)/(2916*sp.pi**2))==0
print('PASS: independent cap Taylor coefficients, exact fixed-area coefficients, unique onset critical point and value')
