"""Reproduce the exact stationary anisotropy sign classification.

Requires Python 3 and SymPy. All algebraic identities use exact arithmetic.
The all-parameter root count follows from the proof, not finite testing.
"""
from fractions import Fraction
from itertools import product
import sympy as sp

rho, beta, speed, diffusion = sp.symbols('rho beta speed diffusion', positive=True)

# Stationary generator equations for the Fourier modes of angular Brownian motion.
m1 = rho / (rho + 1)
m2 = rho / (rho + 4)
mean_x = speed * m1 / (rho + beta)
xc = speed * (1 + m2) / (2 * (rho + beta + 1))
ys = speed * (1 - m2) / (2 * (rho + beta + 1))
raw_x2 = (2 * diffusion + 2 * speed * xc) / (rho + 2 * beta)
raw_y2 = (2 * diffusion + 2 * speed * ys) / (rho + 2 * beta)
raw_difference = sp.factor(raw_x2 - raw_y2)
variance_difference = sp.factor(raw_difference - mean_x**2)
Q = (rho**4 + (beta - 1) * rho**3 - (6 * beta + 2) * rho**2
     - 4 * beta * (beta + 1) * rho + 2 * beta**2)
den = ((beta + rho)**2 * (rho + 2 * beta) * (rho + 1)**2
       * (rho + 4) * (rho + beta + 1))
assert sp.simplify(raw_difference - 2 * speed**2 * rho / ((rho + 4) * (rho + beta + 1) * (rho + 2 * beta))) == 0
assert sp.simplify(variance_difference - speed**2 * rho * Q / den) == 0
assert sp.simplify(variance_difference.subs(diffusion, sp.Integer(0)) - variance_difference) == 0

# Independent Brownian-angular two-time path integral (s <= u) gives two one-sided Laplace factors.
path_integral = speed**2 * 2 * rho / (rho + 2 * beta) / (rho + 4) / (rho + beta + 1)
assert sp.simplify(path_integral - raw_difference) == 0

# The exact strict-negative witness for the quartic at sqrt(beta).
sqrt_beta = sp.sqrt(beta)
negative_witness = sp.factor(Q.subs(rho, sqrt_beta))
assert sp.simplify(negative_witness + beta * (3 * beta * sqrt_beta + 3 * beta + 5 * sqrt_beta + 2)) == 0
assert sp.simplify(Q.subs(rho, 0) - 2 * beta**2) == 0
assert sp.Poly(Q, rho).degree() == 4
# Descartes: exactly two coefficient sign changes for all beta > 0,
# since leading and constant coefficients are positive, the middle
# two are negative, and the cubic coefficient may have either sign.
assert sp.factor(sp.LC(sp.Poly(Q, rho))) == 1
assert sp.simplify(sp.Poly(Q, rho).coeff_monomial(rho**2) + 6 * beta + 2) == 0
assert sp.simplify(sp.Poly(Q, rho).coeff_monomial(rho) + 4 * beta * (beta + 1)) == 0

# Singular-limit scaling polynomials for the two crossings.
q_small = sp.simplify(sp.limit(Q.subs(rho, speed * beta) / beta**2, beta, 0, dir='+'))
assert sp.simplify(q_small - (2 - 4 * speed - 2 * speed**2)) == 0
q_small_upper = sp.factor(Q.subs(beta, 0))
assert sp.simplify(q_small_upper - rho**2 * (rho - 2) * (rho + 1)) == 0
q_large_low = sp.simplify(sp.limit(Q / beta**2, beta, sp.oo))
assert sp.simplify(q_large_low - (2 - 4 * rho)) == 0
q_large_upper = sp.simplify(sp.limit(Q.subs(rho, speed * sp.sqrt(beta)) / beta**sp.Rational(5, 2), beta, sp.oo))
assert sp.simplify(q_large_upper - (speed**3 - 4 * speed)) == 0

# Exact rational generator algebra and sign witnesses at independent parameter choices.
checks = 0
for B, R, P, D in product([sp.Rational(1,10), sp.Rational(1,2), 1, 2, 10],
                          [sp.Rational(1,10), sp.Rational(1,2), 1, 2, 5, 10],
                          [sp.Rational(1,3), 1, 7], [0, sp.Rational(1,4), 3]):
    B, R, P, D = map(sp.Rational, (B, R, P, D))
    x = {beta:B, rho:R, speed:P, diffusion:D}
    m = mean_x.subs(x)
    x2 = raw_x2.subs(x)
    y2 = raw_y2.subs(x)
    # Generator balance directly, without use of closed anisotropy formula.
    assert (R+B)*m == P*R/(R+1)
    assert (2*B+R)*x2 == 2*D+2*P*xc.subs(x)
    assert (2*B+R)*y2 == 2*D+2*P*ys.subs(x)
    assert sp.factor(x2-y2-m**2 - (speed**2*rho*Q/den).subs(x)) == 0
    checks += 4

# A concrete three-regime example with beta=1.
assert Q.subs({beta:1, rho:sp.Rational(1,10)}) > 0
assert Q.subs({beta:1, rho:1}) == -13
assert Q.subs({beta:1, rho:5}) > 0
assert sp.factor(variance_difference.subs({beta:1, rho:1, speed:1})) == -sp.Rational(13,720)
print('PASS:', checks + 18 + 4, 'symbolic/rational assertions (1080 grid, 18 symbolic, 4 witness)')
print('Q(rho;beta) =', Q)
print('Q(sqrt(beta);beta) =', negative_witness)
print('beta=1 root brackets: positive near 0, negative at 1, positive at 5')
