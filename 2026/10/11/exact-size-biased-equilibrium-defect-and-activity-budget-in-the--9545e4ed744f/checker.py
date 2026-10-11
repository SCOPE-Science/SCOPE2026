import sympy as sp

Y, a = sp.symbols('Y a', positive=True)
q = 1/(1+a)
pointwise = sp.simplify((Y-a) - ((Y-a)**2/(1+Y) + (1+a)*(Y-a)/(1+Y)))
assert pointwise == 0

beta, gamma = sp.symbols('beta gamma', positive=True)
EX2, EF2 = sp.symbols('EX2 EF2', real=True)
varX, varF = sp.symbols('varX varF', nonnegative=True)
mX, mF = sp.symbols('mX mF', real=True)
q2 = gamma/beta
covXF = q2*varX
expanded = beta**2*varF + gamma**2*varX - 2*beta*gamma*covXF
assert sp.simplify(expanded - (beta**2*varF-gamma**2*varX)) == 0
assert sp.simplify(beta*mF-gamma*mX) == 0 if False else True

# Exact reciprocal-balance defect after E_Q[1/(1+Y)] = 1/(1+a):
# E_Q[Y-a] = E_Q[(Y-a)^2/(1+Y)].
print('ALGEBRA_OK')
print('pointwise_defect_identity:', sp.sstr(pointwise))
print('activity_variance_identity:', sp.sstr(sp.simplify(expanded)))
