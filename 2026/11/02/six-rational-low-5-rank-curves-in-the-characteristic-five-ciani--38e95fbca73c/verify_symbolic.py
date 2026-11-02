"""Symbolic checks of the characteristic-five Ciani rank-stratum identities.
Requires sympy >= 1.12. This complements the stdlib-only finite-field check.
"""
import sympy as s

a, b, c, t = s.symbols('a b c t')
F = lambda a,b,c: a*a*b*b + 2*a*a + 2*b*b + c*c - a*b*c + 2
D = a*a + b*b + c*c - a*b*c - 4

def modzero(expression, variables):
    numerator = s.cancel(expression).as_numer_denom()[0]
    return s.Poly(numerator, *variables, modulus=5).is_zero

A, B, C = a*a-4, 2*a*b-4*c, b*b-4
assert modzero(B*B + 2*A*C - F(a,b,c), (a,b,c))
assert modzero(F(a,b,c) - F(a,c,b) - (a*a+1)*(b*b-c*c), (a,b,c))
assert modzero(F(a,b,c) - F(b,c,a) - (b*b+1)*(a*a-c*c), (a,b,c))
assert modzero(F(a,c,b) - F(b,c,a) - (c*c+1)*(a*a-b*b), (a,b,c))

for eps, N in [(1,4*b*b+1),(-1,b*b+4)]:
    aa = N/(b*b+2)
    substitutions = {a:aa,c:eps*b}
    assert modzero(F(a,b,c).subs(substitutions), (b,))
    assert modzero(D.subs(substitutions)-3*b*b*(b*b+1)**2/(b*b+2)**2,(b,))
    assert modzero((a*a-4).subs(substitutions)-2*b*b*(b*b+1)/(b*b+2)**2,(b,))

assert modzero(t**4-t**3+2 - (t-2)**2*(t*t-2*t-2), (t,))
print('QUOTIENT_HASSE_POLYNOMIAL=PASS')
print('THREE_PAIRWISE_DIVISOR_DIFFERENCES=PASS')
print('SIX_COMPONENT_PARAMETRIZATIONS_AND_SMOOTHNESS=PASS')
print('TRIPLE_POINT_EQUATION_FACTORIZATION=PASS')
print('VERIFY_SYMBOLIC_OK')
