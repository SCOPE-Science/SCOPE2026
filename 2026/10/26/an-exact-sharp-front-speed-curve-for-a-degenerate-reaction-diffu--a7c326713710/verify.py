import sympy as sp

u, beta, lam, k, c = sp.symbols("u beta lam k c", real=True)
D = u + beta*u**2
hprime = u + k*u**2
bracket = sp.expand(sp.diff(D, u)*(1-u) - D)
residual = sp.expand(lam**2*bracket - lam*(c-hprime) + u)

# Coefficient equations for a positive exponential front.
coefficients = [sp.expand(residual).coeff(u, j) for j in range(3)]
assert sp.simplify(coefficients[0] - (lam**2-lam*c)) == 0
assert sp.simplify(coefficients[1] - (lam**2*(2*beta-2)+lam+1)) == 0
assert sp.simplify(coefficients[2] - (-3*beta*lam**2+lam*k)) == 0

lam_beta = (1+sp.sqrt(9-8*beta))/(4*(1-beta))
k_beta = 3*beta*lam_beta
assert sp.simplify(2*(1-beta)*lam_beta**2-lam_beta-1) == 0
assert sp.simplify(residual.subs({c:lam, lam:lam_beta, k:k_beta})) == 0

# Conservative flux D(U) U' - h(U) vanishes at U=0.
h = u**2/2 + k*u**3/3
assert sp.simplify(D.subs(u, 0)) == 0
assert sp.simplify(h.subs(u, 0)) == 0

# Exact sample: beta=1/2 gives lambda=(1+sqrt(5))/2.
lam_half = sp.simplify(lam_beta.subs(beta, sp.Rational(1,2)))
assert sp.simplify(lam_half - (1+sp.sqrt(5))/2) == 0
assert sp.simplify(k_beta.subs(beta, sp.Rational(1,2)) - sp.Rational(3,2)*lam_half) == 0

print("SYMBOLIC_RESIDUAL_ZERO")
print("PARAMETER_RELATION_ZERO")
print("WEAK_FLUX_MATCH_OK")
print("SAMPLE_BETA_HALF_OK")
