"""Reproducible exact symbolic checks for the two-state Dirichlet transition theorem.
Requires Python 3 and SymPy. These checks supplement the analytic proof.
"""
from fractions import Fraction
import sympy as S
s, r = S.symbols('s r', real=True)
a, b = s*(1-r), s*r
J = S.det(S.Matrix([[S.diff(a,s), S.diff(a,r)], [S.diff(b,s), S.diff(b,r)]]))
assert S.simplify(J - s) == 0  # determinant equals s
assert S.simplify((b/(a+b))-r) == 0
assert S.simplify(1-a-b-(1-s)) == 0
assert S.integrate(s,(s,0,1)) == S.Rational(1,2)
assert S.integrate(2-s,(s,1,2)) == S.Rational(1,2)
assert S.integrate(S.Rational(1,2)/(1-r)**2,(r,0,S.Rational(1,2)))==S.Rational(1,2)
assert S.integrate(S.Rational(1,2)/r**2,(r,S.Rational(1,2),1))==S.Rational(1,2)
var = S.integrate(s/12,(s,0,1)) + S.integrate((2-s)**3/(12*s**2),(s,1,2))
assert S.simplify(var-(S.Rational(3,4)-S.log(2)))==0
mixed=S.integrate((1-s)*s/12,(s,0,1)) + S.integrate((1-s)*(2-s)**3/(12*s**2),(s,1,2))
assert S.simplify(mixed-(S.Rational(7,6)-S.Rational(5,3)*S.log(2)))==0
odds=S.factor((1-s/2)**2/((1-s/4)*(1-3*s/4)))
assert S.simplify(S.diff(odds,s).subs(s,S.Rational(1,2)))!=0
for i in range(1,39):
    for j in range(1,39):
        u,v=Fraction(i,40), Fraction(j,40)
        ss=u+v; rr=v/ss; lam=1-ss
        assert (ss*rr,ss*(1-rr))==(v,u)
        assert Fraction(0)<rr<Fraction(1)
        if lam>=0:
            assert Fraction(0)<rr<Fraction(1)
        else:
            assert (ss-1)/ss<rr<Fraction(1,1)/ss
print('PASS: Jacobian, exact normalizations, stationary moments, mixed moment, nonuniform-family separation, and 1,444 rational cases.')
