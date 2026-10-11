"""Standalone arithmetic checks supporting the period-asymptotic derivation.
Requires Python 3 and SymPy. Analytic convergence is proved in the accompanying result.
"""
import sympy as S
x,y,b,d,z,r=S.symbols('x y b d z r',real=True)
A=(1-x*x)*(1+b*x)
B=(1-y*y)*(1+d*y)
P=-A*y
Q=B*x
assert S.simplify((x/A)*P+(y/B)*Q)==0
assert S.simplify((1/r-1)*r/((1-r*r)*(1+z*r))-1/((1+r)*(1+z*r)))==0
assert S.simplify(1/((1+r)*(1+z*r)) - (1/(1-z))/(1+r) + (z/(1-z))/(1+z*r))==0
primitive=(S.log(1+r)-S.log(1+z*r))/(1-z)
assert S.simplify(S.diff(primitive,r)-1/((1+r)*(1+z*r)))==0
assert S.simplify(primitive.subs(r,1)-primitive.subs(r,0)-(S.log(2)-S.log(1+z))/(1-z))==0
print('CHECK_OK')
