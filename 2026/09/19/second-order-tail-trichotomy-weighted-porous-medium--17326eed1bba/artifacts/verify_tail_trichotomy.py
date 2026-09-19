import sympy as sp

m, p, sigma, N = sp.symbols('m p sigma N', positive=True)
c = sp.symbols('c', positive=True)

D = sigma*(m-1) + 2*(p-1)
alpha = (sigma+2)/D
beta = (m-p)/D
a = sigma/(p-1)
delta = sp.simplify(a*(m-1) + 2)
h = sp.simplify(1/beta)
lam = sp.simplify(a*m)

# Leading absorption-transport balance, with c**(p-1)=1/(p-1).
assert sp.simplify(alpha + beta*a - 1/(p-1)) == 0
assert sp.simplify(delta - D/(p-1)) == 0
assert sp.simplify(h - D/(m-p)) == 0

# The two stable exponents exchange order exactly at m=2p-1.
rate_difference = sp.factor(delta-h)
expected_rate_difference = sp.factor(D*(m-2*p+1)/((p-1)*(m-p)))
assert sp.simplify(rate_difference-expected_rate_difference) == 0

# Radial diffusion of c*xi**(-a*m), divided by c*xi**(-a).
d = sp.simplify(c**(m-1)*lam*(lam-N+2))
linear_factor = sp.simplify(-1 + beta*delta)
assert sp.simplify(linear_factor - (m-2*p+1)/(p-1)) == 0

B_diff = sp.simplify(-d/linear_factor)
B_expected = sp.simplify((p-1)*d/(2*p-1-m))
assert sp.simplify(B_diff-B_expected) == 0

# At m=2p-1, xi^(-delta) is resonant.  L[B xi^-delta log xi] = -beta B xi^-delta.
mres = 2*p-1
beta_res = sp.simplify(beta.subs(m, mres))
delta_res = sp.simplify(delta.subs(m, mres))
d_res = sp.simplify(d.subs(m, mres))
B_log = sp.simplify(d_res/beta_res)
B_log_expected = sp.simplify(2*(sigma+1)*d_res)
assert sp.simplify(beta_res - 1/(2*(sigma+1))) == 0
assert sp.simplify(delta_res - 2*(sigma+1)) == 0
assert sp.simplify(B_log-B_log_expected) == 0

# Center-manifold coordinate cross-check for the subresonant forced coefficient.
x0 = sp.simplify(m*c**(m-1)/alpha)
q = sp.simplify(h*a*(a-N+h))
V_over_X = sp.simplify(q/(h-delta))
# With T=Z-gamma0=V-h*a*X and Z=gamma0*(1+eps)^(p-1),
# eps = T / ((p-1)*gamma0) + higher order, gamma0=1/(alpha*(p-1)).
gamma0 = 1/(alpha*(p-1))
B_center = sp.simplify((V_over_X-h*a)*x0/((p-1)*gamma0))
assert sp.simplify(B_center-B_expected) == 0

# Resonant center-manifold cross-check: V ~ q*x0*nu*exp(-delta*nu).
q_res = sp.simplify(q.subs(m, mres))
x0_res = sp.simplify(x0.subs(m, mres))
gamma0_res = sp.simplify(gamma0.subs(m, mres))
B_center_log = sp.simplify(q_res*x0_res/((p-1)*gamma0_res))
assert sp.simplify(B_center_log-B_log) == 0

# Harmonic cancellation: if a*m=N-2, the diffusion forcing coefficient vanishes.
assert sp.simplify(d.subs(N, lam+2)) == 0

print('leading_balance: PASS')
print('rate_threshold_m_eq_2p_minus_1: PASS')
print('subresonant_coefficient: PASS')
print('resonant_log_coefficient: PASS')
print('center_manifold_cross_checks: PASS')
print('harmonic_cancellation: PASS')
print('all_symbolic_checks_passed = True')
