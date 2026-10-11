"""Exact symbolic checks for identities used in the proof."""
import sympy as sp
t = sp.symbols("t", positive=True)
A = (1+t**3)**(-sp.Rational(1,3))
r = 1/(1+t**2)
F = 3*t*(1+t**3)**(sp.Rational(2,3))/(1+t**2)**2 + (1-t**6)/(1+t**2)**3
assert sp.simplify((A-t**2*r)**3 + (t*A+r)**3 - (1+F)) == 0
H = (t**7 + 2*t**5*(1+t**3)**(sp.Rational(1,3)) - 2*t**5
     + 3*t**4 - 3*t**3 + 2*t**2
     + 2*t*(1+t**3)**(sp.Rational(1,3)) - 1)
factor = -3*H/((t+1)**(sp.Rational(1,3))*(1+t**2)**4*(t**2-t+1)**(sp.Rational(1,3)))
assert sp.simplify(sp.factor(sp.diff(F,t))/factor) == 1
alpha = 2**(-sp.Rational(1,3))
assert sp.simplify((alpha+sp.Rational(1,2))**3+(alpha-sp.Rational(1,2))**3
                   -(1+3/2**(sp.Rational(4,3)))) == 0
print("all symbolic identities verified")
