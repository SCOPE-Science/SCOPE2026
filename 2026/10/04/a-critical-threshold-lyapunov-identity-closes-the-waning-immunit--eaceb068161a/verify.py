#!/usr/bin/env python3
import sympy as sp

S, E, A, V = sp.symbols('S E A V', nonnegative=True)
beta, Sstar, eps = sp.symbols('beta Sstar eps', positive=True)
p, q, z1, z2, z3 = sp.symbols('p q z1 z2 z3', positive=True)
R0 = sp.symbols('R0', positive=True)

h = E + A + eps*V
Edot = beta*S*h - z1*E
Adot = p*E - z2*A
Vdot = q*E - z3*V
Ldot = sp.expand(Edot + beta*Sstar/z2*Adot + beta*eps*Sstar/z3*Vdot)

# Substitute the source reproduction-number identity.
# z1*R0 = beta*Sstar*(1 + p/z2 + q*eps/z3)
crit_relation = sp.solve(
    sp.Eq(z1*R0, beta*Sstar*(1+p/z2+q*eps/z3)), p
)[0]
expr = sp.simplify((Ldot - beta*(S-Sstar)*h - z1*(R0-1)*E).subs(p, crit_relation))
assert expr == 0

# Directly verify the R0 formula as printed.
Lam, mu = sp.symbols('Lam mu', positive=True)
source_R0 = beta*Lam/(mu*z1) + beta*Lam*p/(mu*z1*z2) + beta*Lam*q*eps/(mu*z1*z3)
compact_R0 = beta*(Lam/mu)/z1*(1+p/z2+q*eps/z3)
assert sp.simplify(source_R0-compact_R0) == 0

# Hospital/ICU determinant is positive: (alpha+gH+mu+delta)*(sigma+mu+delta)-alpha*sigma.
alpha, gH, delta, sigma = sp.symbols('alpha gH delta sigma', positive=True)
hdet = sp.expand((alpha+gH+mu+delta)*(sigma+mu+delta)-alpha*sigma)
positive_form = sp.expand(alpha*(mu+delta) + (gH+mu+delta)*(sigma+mu+delta))
assert sp.simplify(hdet-positive_form) == 0

# A concrete exact positive-parameter check at criticality confirms the zero eigenvalue of the E-A-V block.
vals = {Sstar:sp.Rational(10), z1:sp.Rational(3), z2:sp.Rational(2), z3:sp.Rational(5), p:sp.Rational(1), q:sp.Rational(1), eps:sp.Rational(1,2)}
bcrit = sp.simplify(vals[z1] / (vals[Sstar]*(1+vals[p]/vals[z2]+vals[q]*vals[eps]/vals[z3])))
M = sp.Matrix([
    [bcrit*vals[Sstar]-vals[z1], bcrit*vals[Sstar], bcrit*vals[eps]*vals[Sstar]],
    [vals[p], -vals[z2], 0],
    [vals[q], 0, -vals[z3]],
])
assert sp.simplify(M.det()) == 0

print('VERIFY_OK')
print('symbolic_identity', expr)
print('hospital_icu_determinant', hdet)
print('critical_beta_example', bcrit)
