#!/usr/bin/env python3
"""Symbolic checks for sharp tails of the degenerate mKdV--Burgers shock."""
import sympy as sp

mu, kappa, s, y = sp.symbols('mu kappa s y', positive=True)
a2, a3 = sp.symbols('a2 a3')
v = a2*y**2 + a3*y**3
res = sp.expand(kappa*v*sp.diff(v, y) + mu*v - (3*s*y**2 - y**3))
sol_a2 = sp.simplify(sp.solve(sp.Eq(res.coeff(y, 2), 0), a2)[0])
sol_a3 = sp.simplify(sp.solve(sp.Eq(res.subs(a2, sol_a2).coeff(y, 3), 0), a3)[0])

# If X=1/y, then X'=v/y^2=a2+a3/X+O(X^-2), so the log coefficient is a3/a2.
log_coeff = sp.simplify(sol_a3/sol_a2)
expected_log_coeff = -sp.Rational(1, 3)/s - 6*kappa*s/mu**2

lam_minus = sp.simplify((mu-sp.sqrt(mu**2-36*kappa*s**2))/(2*kappa))
lam_plus = sp.simplify((mu+sp.sqrt(mu**2-36*kappa*s**2))/(2*kappa))
charpoly = lambda lam: sp.expand(kappa*lam**2-mu*lam+9*s**2)

kcrit = mu**2/(36*s**2)
lamcrit = 18*s**2/mu
D = sp.symbols('D')
critical_poly = sp.expand(kcrit*D**2-mu*D+9*s**2)
critical_factor = sp.expand(kcrit*(D-lamcrit)**2)

print('center-manifold v(y) coefficients')
print('a2 =', sol_a2)
print('a3 =', sol_a3)
print('residual y^2 =', sp.simplify(res.subs({a2:sol_a2,a3:sol_a3}).coeff(y,2)))
print('residual y^3 =', sp.simplify(res.subs({a2:sol_a2,a3:sol_a3}).coeff(y,3)))
print()
print('reciprocal-tail logarithmic coefficient')
print('a3/a2 =', log_coeff)
print('matches expected =', sp.simplify(log_coeff-expected_log_coeff) == 0)
print()
print('upstream characteristic roots')
print('P(lambda_minus) =', sp.simplify(charpoly(lam_minus)))
print('P(lambda_plus)  =', sp.simplify(charpoly(lam_plus)))
print()
print('critical factorization')
print('difference =', sp.simplify(critical_poly-critical_factor))
print('lambda_c =', lamcrit)
print()
# Numerical sanity values for mu=s=1.
for kval in [sp.Rational(1,72), sp.Rational(1,36)]:
    vals = {mu:1, s:1, kappa:kval}
    lm = lam_minus.subs(vals) if kval < sp.Rational(1,36) else lamcrit.subs({mu:1,s:1})
    ell = (-expected_log_coeff).subs(vals)  # positive magnitude d in X=A xi-d log xi+...
    print(f'kappa={kval}: upstream_rate={sp.N(lm,12)}, reciprocal_log_magnitude={sp.N(ell,12)}')
