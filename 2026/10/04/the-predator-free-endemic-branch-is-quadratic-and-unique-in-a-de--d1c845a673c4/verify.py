#!/usr/bin/env python3
import sympy as sp

y, r, alpha, nu, beta, K = sp.symbols('y r alpha nu beta K', positive=True)
x = nu*(alpha+y)/beta

# Predator-free equilibrium equations from the printed model.
eq_y = beta*x*y/(alpha+y) - nu*y
eq_x = r*x*(1-(x+y)/K) - beta*x*y/(alpha+y)
assert sp.simplify(eq_y) == 0

F = r*(alpha+y)*(beta*K-alpha*nu-(beta+nu)*y) - beta**2*K*y
reconstructed = sp.factor(eq_x * beta*K*(alpha+y) / x)
assert sp.expand(reconstructed - F) == 0
assert sp.Poly(F, y).degree() == 2

# Exact counterexample to the printed sufficient condition beta > nu*alpha.
subs_bad = {r:1, alpha:1, nu:1, beta:2, K:sp.Rational(2,5)}
F_bad = sp.factor(F.subs(subs_bad))
assert sp.simplify(F_bad + (15*y**2 + 24*y + 1)/5) == 0
assert subs_bad[beta] > subs_bad[nu]*subs_bad[alpha]
assert subs_bad[beta]*subs_bad[K] < subs_bad[alpha]*subs_bad[nu]
assert all(c < 0 for c in [sp.Rational(-15,5), sp.Rational(-24,5), sp.Rational(-1,5)])

# Exact feasible case and substitution.
subs_good = {r:1, alpha:1, nu:1, beta:2, K:1}
F_good = sp.expand(F.subs(subs_good))
assert sp.simplify(F_good - (1 - 6*y - 3*y**2)) == 0
y_star = -1 + 2*sp.sqrt(3)/3
x_star = sp.sqrt(3)/3
assert sp.simplify(F_good.subs(y, y_star)) == 0
assert y_star > 0
assert sp.simplify(x.subs(subs_good).subs(y, y_star) - x_star) == 0
assert sp.simplify(eq_y.subs(subs_good).subs({x: x_star, y: y_star})) == 0
assert sp.simplify(eq_x.subs(subs_good).subs({x: x_star, y: y_star})) == 0

# The threshold equals the infection invasion sign at (K,0,0).
invasion = beta*K/alpha - nu
assert sp.factor(invasion - nu*(beta*K/(alpha*nu)-1)) == 0

print('VERIFY_OK')
print('counterexample_polynomial', F_bad)
print('feasible_polynomial', F_good)
print('y_star', sp.simplify(y_star))
print('x_star', sp.simplify(x_star))
