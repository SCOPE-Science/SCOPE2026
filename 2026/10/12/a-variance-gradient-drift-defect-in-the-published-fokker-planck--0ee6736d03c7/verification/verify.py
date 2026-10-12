#!/usr/bin/env python3
"""Exact algebraic replay for the Fokker–Planck forward-form comparison."""
import sympy as sp

S, I, t = sp.symbols('S I t', real=True)
alpha, beta, gamma, delta, eta, v, B = sp.symbols('alpha beta gamma delta eta v B', real=True)
q = sp.Rational(1,50)*(1-alpha)**2
D_S = q*S**2*I**2
D_I = q*S**2*I**2
F_S = B-(1-alpha)*beta*S*I-(v+delta)*S
F_I = (1-alpha)*beta*S*I-(gamma+eta+delta)*I

b_S = F_S-sp.diff(D_S,S)
b_I = F_I-sp.diff(D_I,I)
c_pub = sp.diff(b_S,S)+sp.diff(b_I,I)
correct_b_S = F_S-sp.diff(D_S,S)/2
correct_b_I = F_I-sp.diff(D_I,I)/2
correct_c = sp.diff(correct_b_S,S)+sp.diff(correct_b_I,I)
assert sp.simplify(correct_b_S-(F_S-sp.diff(D_S,S)/2)) == 0
assert sp.simplify(correct_b_I-(F_I-sp.diff(D_I,I)/2)) == 0
assert sp.simplify(correct_c-c_pub-(sp.diff(D_S,S,2)+sp.diff(D_I,I,2))/2) == 0

# A genuinely nonconstant positive polynomial test state density.
f = 1+S*I+S**2+I**3
L6 = (sp.diff(F_S*f,S)+sp.diff(F_I*f,I)
      -(sp.diff(D_S*f,S,2)+sp.diff(D_I*f,I,2))/2)
L8 = (b_S*sp.diff(f,S)+b_I*sp.diff(f,I)+c_pub*f
      -(sp.diff(D_S*sp.diff(f,S),S)+sp.diff(D_I*sp.diff(f,I),I))/2)
expected_defect = -(sp.diff(sp.diff(D_S,S)*f,S)+sp.diff(sp.diff(D_I,I)*f,I))/2
assert sp.simplify(L8-L6-expected_defect) == 0

# The alternative equation is exactly the forward generator for a shifted Ito drift.
Lmodified = (sp.diff(correct_b_S*f,S)+sp.diff(correct_b_I*f,I)
      -(sp.diff(D_S*f,S,2)+sp.diff(D_I*f,I,2))/2)
assert sp.simplify(L8-Lmodified) == 0
assert sp.simplify((correct_b_S-F_S)+q*S*I**2) == 0
assert sp.simplify((correct_b_I-F_I)+q*S**2*I) == 0
assert sp.simplify((correct_b_S-F_S)+(correct_b_I-F_I)+q*S*I*(S+I)) == 0

# Even with constant variance, the source's extra 1/2 in (9) is consequential.
f0 = 1+S-2*t
phi = S*(1-S)*I*(1-I)
assert sp.diff(f0,t)+2*sp.diff(f0,S) == 0
assert sp.diff(f0,S,2)+sp.diff(f0,I,2) == 0
weak_pub_integrand = sp.diff(f0,t)*phi + sp.Rational(1,2)*2*sp.diff(f0,S)*phi + sp.Rational(1,2)*(sp.diff(f0,S)*sp.diff(phi,S)+sp.diff(f0,I)*sp.diff(phi,I))
weak_correct_integrand = sp.diff(f0,t)*phi + 2*sp.diff(f0,S)*phi + sp.Rational(1,2)*(sp.diff(f0,S)*sp.diff(phi,S)+sp.diff(f0,I)*sp.diff(phi,I))
assert sp.integrate(weak_correct_integrand,(S,0,1),(I,0,1)) == 0
assert sp.integrate(weak_pub_integrand,(S,0,1),(I,0,1)) == -sp.Rational(1,36)

print('VERIFY_OK')
