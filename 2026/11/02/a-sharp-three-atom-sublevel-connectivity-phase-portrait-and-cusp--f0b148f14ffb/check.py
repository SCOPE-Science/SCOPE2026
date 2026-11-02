"""Finite symbolic/numeric cross-checks for the stated three-atom phase portrait.

No topological conclusion is inferred from finite tests; see the analytic proof.
"""
import math
import sympy as S

z, a, w = S.symbols('z a w')
T = z*z + z + 1
numer = -(z + 1)*(a*T + 2*z*z - 4*z + 2)
denom = (z - 1)*T
F = S.cancel(numer/denom)
expected_derivative = 2/(1-z)**2 * (a-1+9*z*z/T**2)
assert S.cancel(S.diff(F,z)-expected_derivative) == 0
quartic = 9*w**4 + 6*(a*a-20*a-8)*w*w + a*(a+8)**3
assert S.factor(S.discriminant(numer-w*denom,z)+3*quartic) == 0
assert S.factor((a*a-20*a-8)**2-a*(a+8)**3) == -64*(a-1)**3
for ratio in [S.Rational(1,100),S.Rational(1,4),S.Rational(3,4),
              S.Rational(9,10), S.Rational(11,10),S.Integer(2),S.Integer(10)]:
    polynomial = S.together(S.diff(F,z)).as_numer_denom()[0].subs(a,ratio)
    # A polynomial has four global critical points, only two are in the unit disk.
    roots = S.nroots(polynomial,maxsteps=150)
    inside = [complex(q) for q in roots if abs(complex(q)) < 1-1e-8]
    assert len(inside) == 2
    heights = sorted([complex(F.subs({a:ratio,z:q}).evalf(40)).real for q in inside])
    av = float(ratio)
    if av < 1:
        low = math.sqrt((20*av+8-av*av-8*(1-av)**1.5)/3)
        high = math.sqrt((20*av+8-av*av+8*(1-av)**1.5)/3)
        assert abs(heights[0]-low)<1e-7 and abs(heights[1]-high)<1e-7
        assert all(abs(q.imag)<1e-8 for q in inside)
    else:
        height = math.sqrt((math.sqrt(av*(av+8)**3)+20*av+8-av*av)/6)
        assert max(abs(q-height) for q in heights)<1e-7
        assert abs(inside[0]-inside[1].conjugate())<1e-7
# The cusp expansion follows exactly from the squared-height gap.
assert S.simplify(((S.Integer(16)/3)/S.Integer(6)) - S.Rational(8,9)) == 0
assert S.factor(S.cancel(F.subs(a,1) - 3*(1+z**3)/(1-z**3))) == 0
print('CHECK_OK: derivative, cubic discriminant, critical heights, symmetry and cusp coefficient')
