"""Exact monodromy verification for an inverse-square-root two-step oscillator.

Requires SymPy. Computation is rational in beta and v, reduced using
v**2 = 6*beta*(beta-1)/(beta**2+1).
"""
import sympy as s

beta, v = s.symbols("beta v", real=True, positive=True)
xi = 6*beta*(beta-1)/(beta**2+1)
tau = 2*v*(1-v**2/s.Integer(6))

def phase_matrix(h, first_velocity, last_velocity):
    fundamental_initial = s.Matrix([
        [first_velocity, 1],
        [h, first_velocity/s.Integer(4)],
    ])
    fundamental_final = s.Matrix([
        [last_velocity, 1-s.Rational(3,4)*tau*last_velocity],
        [h, last_velocity/s.Integer(4)-s.Rational(3,4)*tau*h],
    ])
    return fundamental_final * fundamental_initial.inv()

positive = phase_matrix(1, -v, v)
negative = phase_matrix(-beta, v, -v)
M = negative*positive

def modulo_orbit(expr):
    numerator, denominator = s.cancel(expr).as_numer_denom()
    polynomial_relation = s.Poly(v**2-xi, v)
    n = s.rem(s.Poly(numerator, v), polynomial_relation).as_expr()
    d = s.rem(s.Poly(denominator, v), polynomial_relation).as_expr()
    return s.factor(s.cancel(n/d))

trace = modulo_orbit(s.trace(M))
det = modulo_orbit(M.det())
entry21 = modulo_orbit(M[1,0])
expected_trace = -2*(17*beta**4-38*beta**2+17)/(beta**2+1)**2
expected_entry21 = -6*v*(beta**2-1)/(beta**2+1)
assert s.simplify(trace-expected_trace) == 0
assert s.simplify(det-1) == 0
assert s.simplify(entry21-expected_entry21) == 0
assert s.simplify(trace-2+36*(beta**2-1)**2/(beta**2+1)**2) == 0
assert s.simplify(trace+2+16*(beta**2-2)*(2*beta**2-1)/(beta**2+1)**2) == 0
print('trace =', s.factor(trace))
print('determinant =', det)
print('entry (2,1) =', entry21)
print('trace-2 =', s.factor(trace-2))
print('trace+2 =', s.factor(trace+2))
print('All exact algebraic checks passed.')
