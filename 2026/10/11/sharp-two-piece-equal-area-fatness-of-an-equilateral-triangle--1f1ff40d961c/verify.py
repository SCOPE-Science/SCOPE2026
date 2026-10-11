#!/usr/bin/env python3
"""Check algebra in the analytic equilateral two-piece fatness proof.

Requires SymPy. Numerical samples are sanity checks, not an infinite proof.
"""
import sympy as S

t=S.symbols('t', positive=True)
u=1/(2*t)
h=S.sqrt(3)/2
c=(3+S.sqrt(3))/2
L2=t*t+u*u-t*u

assert S.simplify(L2-S.Rational(3,4)*t*t-(t-1/t)**2/4)==0
assert S.simplify((2+h)*t-u-c*(2*t-1)-
    (1-t)*((1+h)*t-S.Rational(1,2))/t)==0
assert S.simplify(S.sqrt(3)/(4*c)-(S.sqrt(3)-1)/4)==0
for numerator in range(72,101):
    tv=S.Rational(numerator,100)
    uv=S.Rational(1,2)/tv
    if tv<1/S.sqrt(2):
        continue
    Lv=S.sqrt(tv*tv+uv*uv-tv*uv)
    bound=S.N(S.sqrt(3)*(tv-S.Rational(1,2))/
              (2*(2*tv-uv+Lv)),40)
    optimum=S.N((S.sqrt(3)-1)/4,40)
    assert float(bound)<=float(optimum)+1e-13
    if tv<1:
        assert float(bound)<float(optimum)-1e-10
print('EQUAL_AREA_TRIANGLE_IDENTITIES_OK')
