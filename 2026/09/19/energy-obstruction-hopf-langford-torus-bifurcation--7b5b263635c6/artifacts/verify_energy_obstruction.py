import sympy as sp

# Exact reduced variables for the Hopf-Langford-type system.
alpha, mu, gamma, beta = sp.symbols('alpha mu gamma beta', real=True, nonzero=True)
w, v = sp.symbols('w v', positive=True, real=True)
s = alpha - mu
T = mu - 2*gamma*s
R2 = s*(mu/gamma - s)

# In w=r**gamma and y=z-s, the amplitude equation is
# w' = v, v' = T v + gamma**2 R2 w - gamma**2 w**(1+2/gamma).
force = gamma**2*R2*w - gamma**2*w**(1 + 2/gamma)

# Energy identity. Differentiate E along the first-order system by the chain rule.
Vprime = -force
# It is enough to verify dE/dt using V' without choosing a branch for the antiderivative.
dEdt = sp.expand(v*(T*v + force) + Vprime*v)
assert sp.simplify(dEdt - T*v**2) == 0

# Exact nonzero periodic circle in the original 3D flow has z=s and r^2=R2.
# Its transverse amplitude Jacobian has exact trace T and determinant 2 gamma R^2.
R = sp.symbols('R', positive=True, real=True)
J = sp.Matrix([[0, R], [-2*gamma*R, T]])
assert sp.simplify(sp.trace(J) - T) == 0
assert sp.simplify(J.det() - 2*gamma*R**2) == 0

# The time-P map of (w,v) has constant Jacobian determinant exp(T P),
# because the planar divergence is exactly T.
planar_divergence = sp.diff(v, w) + sp.diff(T*v + force, v)
assert sp.simplify(planar_divergence - T) == 0

# The first-integral condition in Vassilev-Nikolov (Axioms 2025), after mapping
# their parameters alpha_A=mu-alpha, eta=1, delta=gamma, is exactly T=0.
alpha_A = mu - alpha
VN_condition = 2*alpha_A*gamma + mu
assert sp.simplify(VN_condition - T) == 0

# Expansion of the exact critical surface mu = 2 gamma alpha/(1+2 gamma).
eps = sp.symbols('eps', real=True)
a1, a2, g0, g1, g2, mu2 = sp.symbols('a1 a2 g0 g1 g2 mu2', real=True)
alpha_eps = a1*eps + a2*eps**2
gamma_eps = g0 + g1*eps + g2*eps**2
mu_exact = sp.series(2*gamma_eps*alpha_eps/(1+2*gamma_eps), eps, 0, 3).removeO()
c1 = sp.expand(mu_exact).coeff(eps, 1)
c2 = sp.expand(mu_exact).coeff(eps, 2)
expected_c1 = 2*a1*g0/(1+2*g0)
expected_mu1_correction = 2*a2*g0/(1+2*g0) + 2*a1*g1/(1+2*g0)**2 - mu2
assert sp.simplify(c1 - expected_c1) == 0
assert sp.simplify((c2 - mu2) - expected_mu1_correction) == 0

# Source Example 2 at epsilon=10^-3.
e = sp.Rational(1, 1000)
a_ex = e + sp.Rational(1,100)*e**2
b_ex = sp.Rational(1,10) + sp.Rational(443,100)*e + sp.Rational(1,25)*e**2
g_ex = -1 - e + sp.Rational(1,25)*e**2
m_ex = sp.Rational(399317,100000)*e + sp.Rational(1,25)*e**2
s_ex = sp.simplify(a_ex - m_ex)
R2_ex = sp.simplify(s_ex*(m_ex/g_ex - s_ex))
T_ex = sp.simplify((1+2*g_ex)*m_ex - 2*g_ex*a_ex)
det_ex = sp.simplify(2*g_ex*R2_ex)

# Source Eq. (9), evaluated at the Example-2 leading values gamma0=-1, omega=1/10.
pi = sp.pi
gamma0 = sp.Integer(-1)
omega = sp.Rational(1,10)
ell_source_eq9 = ((4*pi**2-2)*gamma0**2 + 3*(4*pi**2-1)*gamma0 + pi**2)/(16*omega**2)
ell_example_claim = (49*pi**2-11)/144

print('energy_identity_residual =', sp.simplify(dEdt - T*v**2))
print('reduced_divergence_minus_T =', sp.simplify(planar_divergence - T))
print('VN_integrability_condition_minus_T =', sp.simplify(VN_condition - T))
print('exact_critical_leading_coefficient =', sp.simplify(c1))
print('exact_mu1_O(eps)_correction =', sp.simplify(c2-mu2))
print('example2_alpha =', sp.N(a_ex, 16))
print('example2_beta =', sp.N(b_ex, 16))
print('example2_gamma =', sp.N(g_ex, 16))
print('example2_mu =', sp.N(m_ex, 16))
print('example2_R2 =', sp.N(R2_ex, 16))
print('example2_T =', sp.N(T_ex, 16))
print('example2_transverse_determinant =', sp.N(det_ex, 16))
print('source_eq9_at_gamma0_minus1_omega_point1 =', sp.N(ell_source_eq9, 16))
print('example2_claimed_ell =', sp.N(ell_example_claim, 16))
print('all_symbolic_checks_passed = True')
