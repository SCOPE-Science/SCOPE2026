import sympy as sp

S, Sb, I, Q = sp.symbols('S Sb I Q', positive=True)
St, It = sp.symbols('St It', nonnegative=True)
beta, d1, d2 = sp.symbols('beta d1 d2', positive=True)

Sdot = d1*Sb - d1*S - beta*S*I
Idot = beta*St*It - I*Q/(1+I) - d2*I
phi_dot = (1-Sb/S)*Sdot
delay_dot = beta*(S*I-St*It)
W0_dot = sp.factor(phi_dot + Idot + delay_dot)
target = -d1*(S-Sb)**2/S + (beta*Sb-d2)*I - I*Q/(1+I)
assert sp.simplify(W0_dot-target) == 0
critical = sp.factor(W0_dot.subs(d2, beta*Sb))
critical_target = -d1*(S-Sb)**2/S - I*Q/(1+I)
assert sp.simplify(critical-critical_target) == 0
print('VERIFY_OK')
