#!/usr/bin/env python3
"""Exact algebraic checks for the period-two orbit theorem.

Requires SymPy. This tests polynomial identities and sample parameter points;
the universal root-count and stability arguments are in RESULT.md.
"""
import sympy as S

a, b, c, d, t = S.symbols('a b c d t', positive=True, finite=True)
half = S.Rational(1, 2)
c0 = half + b/4
C = d + 4*b/(1+b)**2
Q = (c-c0)*t**2 + a*t - C
m = 2/(1+b)
u, v = m-t/2, m+t/2

def F_at(x, y, sign):
    return S.Matrix([x+y, y-a*sign*y-x*y+b*x**2-c*y**2+d])

p = S.Matrix([u, t]); q = S.Matrix([v, -t])
assert (F_at(u, t, 1)-q-S.Matrix([0,-Q])).applyfunc(S.factor) == S.zeros(2,1)
assert (F_at(v, -t, -1)-p-S.Matrix([0,-Q])).applyfunc(S.factor) == S.zeros(2,1)


def J(x, y, sign):
    return S.Matrix([[1, 1], [-y+2*b*x, 1-a*sign-x-2*c*y]])

P = J(v, -t, -1)*J(u, t, 1)
alpha = (b-1)/(1+b)
h = 4*b/(1+b)
w = (1+b)*t
z = a+(2*c-half)*t
trace_formula = 1+2*h+alpha**2-z**2
det_formula = (alpha-h)**2-(w-z)**2
assert S.factor(S.trace(P)-trace_formula) == 0
assert S.factor(P.det()-det_formula) == 0
assert S.factor(1-S.trace(P)+P.det()-2*(1+b)*t*(a+2*(c-c0)*t)) == 0

# A rational parameter point with exactly two distinct period-two cycles.
values = {a:S.Integer(2), b:half, c:half, d:S.Rational(23,288)}
qq = S.factor(Q.subs(values))
assert S.factor(qq+(2*t-1)*(2*t-31)/32) == 0
for amplitude in [half, S.Rational(31,2)]:
    vals = {**values, t:amplitude}
    assert S.simplify(Q.subs(vals)) == 0
    assert F_at(u,t,1).subs(vals) == q.subs(vals)
    assert F_at(v,-t,-1).subs(vals) == p.subs(vals)
    matrix = P.subs(vals)
    tr, determinant = S.trace(matrix), matrix.det()
    schur = [S.factor(1-tr+determinant),
             S.factor(1+tr+determinant), S.factor(1-determinant)]
    if amplitude == half:
        assert schur == [S.Rational(45,16),S.Rational(35,144),S.Rational(17,36)]
    else:
        assert schur[0] == S.Rational(-1395,16)

# A valid positive-parameter double root where one multiplier equals +1.
fold_a, fold_b, fold_d = half, S.Rational(1,10), S.Rational(1,10)
fold_C = (C.subs({a:fold_a, b:fold_b, d:fold_d}))
fold_t = 2*fold_C/fold_a
fold_c = (c0 - fold_a**2/(4*fold_C)).subs({a:fold_a,b:fold_b})
fold_values = {a:fold_a,b:fold_b,c:fold_c,d:fold_d,t:fold_t}
assert fold_c > 0
assert S.factor(Q.subs(fold_values)) == 0
assert S.factor((1-S.trace(P)+P.det()).subs(fold_values)) == 0
assert S.factor(S.diff(Q,t).subs(fold_values)) == 0

# A valid positive-parameter zero-cycle regime.
none_values={a:S.Rational(1,100),b:S.Rational(1,10),
             c:S.Rational(1,4),d:S.Rational(1,10)}
disc=S.factor((a**2+4*(c-c0)*C).subs(none_values))
assert disc < 0

print('PERIOD_TWO_EXACT_IDENTITIES_AND_RATIONAL_EXAMPLES_OK')
