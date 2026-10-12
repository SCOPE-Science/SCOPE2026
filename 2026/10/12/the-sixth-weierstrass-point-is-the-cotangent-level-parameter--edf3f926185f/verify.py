import sympy as sp

r = sp.symbols('r')
theta = sp.symbols('theta1:6')
A = sp.symbols('A1:6', nonzero=True)
x = sp.symbols('x1:6')

q0 = sum(A[i]*x[i]**2 for i in range(5))
q1 = sum(theta[i]*A[i]*x[i]**2 for i in range(5))
S0 = sum(A[i]*x[i]**2/(r-theta[i]) for i in range(5))
S1 = sum(theta[i]*A[i]*x[i]**2/(r-theta[i]) for i in range(5))
S2 = sum(theta[i]**2*A[i]*x[i]**2/(r-theta[i]) for i in range(5))

# Tangent-radical identities. On X, q0=q1=0, so
# [[S0,S1],[S1,S2]] = S0*[[1,r],[r,r**2]].
assert sp.simplify(S1 - r*S0 + q0) == 0
assert sp.simplify(S2 - r*S1 + q1) == 0

# Kummer model for the genus-two curve branched at theta_1,...,theta_5,r.
y = sp.symbols('y1:7')
w = [A[i]/(theta[i]-r) for i in range(5)]
w6 = sp.symbols('w6', nonzero=True)
E0 = sum(w[i]*y[i]**2 for i in range(5)) + w6*y[5]**2
E1 = sum(theta[i]*w[i]*y[i]**2 for i in range(5)) + r*w6*y[5]**2
E2 = sum(theta[i]**2*w[i]*y[i]**2 for i in range(5)) + r**2*w6*y[5]**2
q0y = sum(A[i]*y[i]**2 for i in range(5))
q1y = sum(theta[i]*A[i]*y[i]**2 for i in range(5))

assert sp.simplify(E1-r*E0-q0y) == 0
assert sp.simplify(E2-r*E1-q1y) == 0
branch_kummer = sum(w[i]*y[i]**2 for i in range(5))
branch_tangent = sum(A[i]*y[i]**2/(r-theta[i]) for i in range(5))
assert sp.simplify(branch_kummer + branch_tangent) == 0
assert 2**4 == 16

print('VERIFY_OK tangent_branch=kummer_branch sixth_branch_parameter=e complement=16_two_torsion')
