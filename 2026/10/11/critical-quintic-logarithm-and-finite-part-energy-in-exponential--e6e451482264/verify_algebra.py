"""Reproducible exact coefficient identities; the analytic proof is separate."""
import sympy as s

q, beta, c, alpha = s.symbols('q beta c alpha', positive=True)
d = -beta / (q + 1)
e = beta**2 * q / (2*c*(q+1)**2)
assert s.simplify(2*c*d + 2*beta*c/(q+1)) == 0
assert s.simplify(d*d + 2*c*e - beta**2/(q+1)) == 0
assert s.simplify(2*beta*e.subs(q, 3) - 3*beta**3/(16*c)) == 0
log_coefficient = s.simplify(-beta * e.subs(q,3) / c)
assert s.simplify(log_coefficient.subs(c, s.sqrt(alpha/3)) + 9*beta**3/(32*alpha)) == 0
C = s.simplify((s.Symbol('K')-2*d.subs(q,3)*e.subs(q,3))/(2*c))
assert s.simplify(C - s.Symbol('K')/(2*c) - 3*beta**3/(128*c**2)) == 0
print('PASS: symbolic universal coefficients, quintic logarithm, and finite-part constant conversion')
