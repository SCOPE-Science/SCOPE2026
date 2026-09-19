import sympy as sp

# Symbols
lam, H1, H2, H3 = sp.symbols('lam H1 H2 H3', positive=True)
kappa, p, eps = sp.symbols('kappa p eps', positive=True)

# 1. Critical-power (kappa=2) scale identity.
Hlam = lam**2 * H1 + lam**4 * H2 - lam**2 * H3
virial_k2 = sp.Eq(H3, H1 + 2*H2)  # from 2 H1 + 4 H2 - 2 H3 = 0
Hlam_stat = sp.expand(Hlam.subs(H3, virial_k2.rhs))
H1_stat = sp.expand(Hlam_stat.subs(lam, 1))
identity = sp.factor(Hlam_stat - H1_stat)
assert sp.simplify(identity - H2*(lam**2 - 1)**2) == 0

# 2. The nonlinear-gradient coefficient in Eq. (63) has sign p-1.
coeff = sp.factor(1 - 1/p)
assert coeff == (p - 1)/p

# 3. Exact sech integral ratio used for the first nonrelativistic correction.
a = sp.symbols('a', positive=True)
def J(x):
    # Integral over R of sech(z)^x tanh(z)^2 dz.
    return sp.gamma(sp.Rational(3, 2))*sp.gamma(x/2)/sp.gamma((x+3)/2)
ratio_general = sp.simplify(sp.expand_func(J(a+2)/J(a)))
assert ratio_general == a/(a+3)
ratio_kappa = sp.simplify(ratio_general.subs(a, 2/kappa))
assert ratio_kappa == 2/(3*kappa+2)

# 4. First-order Derrick threshold near kappa=2.
# eps = (m-omega)/(2m). To O(eps), H2/H1 is:
r = 2*eps*(p-1)/(p+1)*(kappa+1)/(3*kappa+2)
eta = sp.symbols('eta')
curv = (2-kappa) + (kappa+2)*r
near = sp.expand(curv.subs(kappa, 2+eta))
# Keep only total first order in eps and eta.
first = -eta + 3*eps*(p-1)/(p+1)
# Check by differentiating at (eps,eta)=(0,0).
linearized = (near.subs({eps:0,eta:0})
              + sp.diff(near, eps).subs({eps:0,eta:0})*eps
              + sp.diff(near, eta).subs({eps:0,eta:0})*eta)
assert sp.simplify(linearized-first) == 0

print('critical_scale_identity =', identity)
print('nonlinear_gradient_factor =', coeff)
print('sech_ratio =', ratio_kappa)
print('near_critical_curvature =', first)
print('critical_kappa = 2 + 3*eps*(p-1)/(p+1) + O(eps^2)')
