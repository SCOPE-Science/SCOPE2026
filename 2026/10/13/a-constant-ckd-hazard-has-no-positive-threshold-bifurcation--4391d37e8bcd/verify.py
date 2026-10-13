#!/usr/bin/env python3
import sympy as sp

Lam, lam, mu, zeta, muk, gamma, muh = sp.symbols(
    'Lambda lambda_k mu zeta_k mu_k gamma_h mu_h', positive=True
)
phi = zeta + muk + mu
psi = gamma + muh + mu
Delta = sp.expand(phi*psi - gamma*zeta)
assert sp.expand(Delta - (zeta*(muh+mu) + (muk+mu)*(gamma+muh+mu))) == 0

Sstar = Lam/(lam+mu)
Istar = lam*Lam*psi/((lam+mu)*Delta)
Hstar = zeta*Istar/psi

# Check equilibrium identities for the printed CKD-only system.
f1 = sp.expand(Lam - (lam+mu)*Sstar)
f2 = sp.simplify(lam*Sstar + gamma*Hstar - phi*Istar)
f3 = sp.simplify(zeta*Istar - psi*Hstar)
assert f1 == 0 and f2 == 0 and f3 == 0

# Exact characteristic polynomial of the homogeneous affine system.
r = sp.symbols('r')
M = sp.Matrix([[-(lam+mu), 0, 0], [lam, -phi, gamma], [0, zeta, -psi]])
char = sp.factor(M.charpoly(r).as_expr())
expected = sp.expand((r+lam+mu)*(r**2 + (phi+psi)*r + Delta))
assert sp.expand(char-expected) == 0

# The source's C_k=1 value is a positive lambda_k; it cannot be a bifurcation.
C = lam*Lam*(psi+zeta)/(mu*Delta)
lamcrit = sp.simplify(mu*Delta/(Lam*(psi+zeta)))
assert sp.simplify(C.subs(lam, lamcrit)-1) == 0
Icrit = sp.factor(Istar.subs(lam, lamcrit))
assert sp.simplify(Icrit - Lam*psi/(Delta + Lam*(psi+zeta))) == 0
# At lambda_crit the true characteristic polynomial has nonzero constant term.
constcrit = sp.factor(expected.subs({r:0, lam:lamcrit}))
assert constcrit != 0

# Exact monotonicity of the equilibrium burden with respect to the constant hazard.
dI = sp.factor(sp.diff(Istar, lam))
dH = sp.factor(sp.diff(Hstar, lam))
assert sp.simplify(dI - Lam*psi*mu/(Delta*(lam+mu)**2)) == 0
assert sp.simplify(dH - Lam*zeta*mu/(Delta*(lam+mu)**2)) == 0

print('VERIFY_OK')
print('Delta =', Delta)
print('characteristic =', char)
print('I(lambda_crit) =', Icrit)
print('dI/dlambda =', dI)
print('dH/dlambda =', dH)
