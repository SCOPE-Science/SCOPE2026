from fractions import Fraction
import sympy as sp

x, m, d, c, w = sp.symbols('x m d c w', positive=True)
point_lhs = m/(d+m) - x/(d+x)
point_rhs = -d*(x-m)/(d+m)**2 + d*(x-m)**2/((d+m)**2*(d+x))
assert sp.simplify(point_lhs-point_rhs) == 0

u = c*d/(w-c)
# Denote Q = E[(x-m)^2/(d+x)]. Averaging the point identity gives
# h(m)-h(u) = d*Q/(d+m)^2.
Q = sp.symbols('Q', nonnegative=True)
lhs = m-u
rhs = (d+u)/(d+m)*Q
balance_equation = sp.Eq(d*(m-u)/((d+m)*(d+u)), d*Q/(d+m)**2)
sol = sp.solve(balance_equation, m-u, dict=False)
assert len(sol) == 1
assert sp.simplify(sol[0]-rhs) == 0

source_u = Fraction(7,10)*20/(Fraction(2,1)-Fraction(7,10))
assert source_u == Fraction(140,13)
assert float(source_u) > 10.7692 and float(source_u) < 10.7693

# h is strictly increasing for d>0.
hprime = sp.diff(x/(d+x), x)
assert sp.simplify(hprime - d/(d+x)**2) == 0

print('point_identity=OK')
print('defect_rearrangement=OK')
print('source_u2_star=', source_u)
print('monotonicity=OK')
print('VERIFY_OK')
