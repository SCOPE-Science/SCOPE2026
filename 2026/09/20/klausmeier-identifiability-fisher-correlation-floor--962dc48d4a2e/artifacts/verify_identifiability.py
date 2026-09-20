import sympy as sp

# Symbols and vector field
a, m, w, n = sp.symbols('a m w n', positive=True)
x = sp.symbols('x', positive=True)
wdot = a - w - w*n**2
ndot = n*(w*n - m)

# Differential identities whose time integrals recover a and m.
assert sp.simplify(wdot + w*(1+n**2) - a) == 0
assert sp.simplify(ndot/n - w*n + m) == 0

# Positive-equilibrium inverse map and its Jacobian.
Psi = sp.Matrix([w*(1+n**2), w*n])
J = Psi.jacobian([w, n])
detJ = sp.factor(J.det())
assert sp.simplify(detJ - w*(1-n**2)) == 0

# Positive equilibria: the source's same-sign displayed pairing is not an equilibrium;
# the cross pairing is exact.
Delta = sp.sqrt(a**2 - 4*m**2)
wplus = (a + Delta)/2
wminus = (a - Delta)/2
nplus = (a + Delta)/(2*m)
nminus = (a - Delta)/(2*m)
assert sp.simplify(wminus*nplus - m) == 0
assert sp.simplify(wplus*nminus - m) == 0
same_plus = sp.factor(sp.simplify(wplus*nplus - m))
same_minus = sp.factor(sp.simplify(wminus*nminus - m))

# Ideal equilibrium-only Gaussian Fisher geometry.
# At equilibrium w=m/n, parameter covariance is proportional to J J^T.
Jeq = sp.simplify(J.subs(w, m/n))
C = sp.simplify(Jeq * Jeq.T)
Caa = sp.factor(C[0,0])
Cmm = sp.factor(C[1,1])
Cam = sp.factor(C[0,1])
rho2 = sp.factor(Cam**2/(Caa*Cmm))
one_minus_rho2 = sp.factor(1-rho2)
expected_h = m**2*(n**2-1)**2 / (((1+n**2)**2+4*m**2)*(n**4+m**2))
assert sp.simplify(one_minus_rho2 - expected_h) == 0

# Sharp correlation floor on the stable positive branch n>1.
hx = sp.factor(expected_h.subs(n, sp.sqrt(x)))
dhx = sp.diff(hx, x)
num, den = sp.fraction(sp.factor(dhx))
expected_num = -2*m**2*(x-1)*(2*m**2+x**2+x)*(x**2-2*x-1-2*m**2)
assert sp.simplify(num/expected_num) == 1
xstar = 1 + sp.sqrt(2*(1+m**2))
hstar = sp.factor(sp.simplify(hx.subs(x, xstar)))
expected_hstar = m**2/(9*m**2 + 12*sp.sqrt(2)*sp.sqrt(1+m**2) + 17)
assert sp.simplify(hstar - expected_hstar) == 0

# Expected Fisher determinant for M observations of variance sigma^2.
M, sigma = sp.symbols('M sigma', positive=True)
S = sp.simplify(Jeq.inv())
Fisher = sp.simplify((M/sigma**2) * S.T*S)
detF = sp.factor(Fisher.det())
expected_detF = (M/sigma**2)**2 / ((m/n)**2*(n**2-1)**2)
assert sp.simplify(detF - expected_detF) == 0

# Numerical value used in the source paper.
mval = sp.Rational(9,20)
xstar_val = sp.N(xstar.subs(m,mval), 30)
nstar_val = sp.N(sp.sqrt(xstar).subs(m,mval), 30)
astar_val = sp.N((m*(sp.sqrt(xstar)+1/sp.sqrt(xstar))).subs(m,mval), 30)
rho_min_val = sp.N(sp.sqrt(1-expected_hstar).subs(m,mval), 30)

print('trajectory_a_identity_residual =', sp.simplify(wdot + w*(1+n**2) - a))
print('trajectory_m_identity_residual =', sp.simplify(ndot/n - w*n + m))
print('inverse_map_det =', detJ)
print('cross_pair_residual_1 =', sp.simplify(wminus*nplus-m))
print('cross_pair_residual_2 =', sp.simplify(wplus*nminus-m))
print('same_sign_plus_residual =', same_plus)
print('same_sign_minus_residual =', same_minus)
print('one_minus_rho_squared =', one_minus_rho2)
print('d_dx_numerator =', num)
print('x_star =', xstar)
print('one_minus_rho_min_squared =', hstar)
print('det_fisher =', detF)
print('m = 0.45')
print('x_star_numeric =', xstar_val)
print('n_star_numeric =', nstar_val)
print('a_star_numeric =', astar_val)
print('rho_min_numeric =', rho_min_val)
print('all_symbolic_checks_passed = True')
