#!/usr/bin/env python3
import sympy as sp

rho, alpha, beta, mu, sigma = sp.symbols("rho alpha beta mu sigma", positive=True)
S, L, E, I, R = sp.symbols("S L E I R", nonnegative=True)
delta, gamma, a = sp.symbols("delta gamma a", positive=True)
H = E + I

Sdot = mu*rho + sigma*rho*R - alpha*S*H - mu*S
Ldot = mu*(1-rho) + sigma*(1-rho)*R - beta*L*H - mu*L
q = S/rho - L/(1-rho)
qdot = sp.simplify(Sdot/rho - Ldot/(1-rho))
target_qdot = -(mu + beta*H)*q - (alpha-beta)*H*S/rho
assert sp.simplify(qdot - target_qdot) == 0

a0 = alpha*rho + beta*(1-rho)
decomp = a0*(S+L) + (alpha-beta)*rho*(1-rho)*q
assert sp.simplify(alpha*S + beta*L - decomp) == 0

A = sp.Matrix([[a-delta-mu, a], [delta, -gamma-mu]])
det_target = (delta+mu)*(gamma+mu) - a*(gamma+mu+delta)
assert sp.simplify(A.det() - det_target) == 0

aa = sp.Rational(1,5)
bb = sp.Rational(1,10)
rr = sp.Rational(3,10)
dd = sp.Rational(3,20)
gg = sp.Rational(4,5)
mm = sp.Rational(1,200)

a0_num = aa*rr + bb*(1-rr)
R0 = sp.simplify(a0_num * (1/(dd+mm) + dd/((dd+mm)*(gg+mm))))
assert a0_num == sp.Rational(13,100)
assert R0 < 1

S0 = sp.Rational(9,10)
L0 = 0
E0 = sp.Rational(1,10)
I0 = 0
actual = sp.simplify((aa*S0 + bb*L0 - dd - mm)*E0 + (aa*S0 + bb*L0)*I0)
claimed = sp.simplify((a0_num - dd - mm)*E0 + a0_num*I0)

assert actual == sp.Rational(1,400)
assert claimed == -sp.Rational(1,400)

print("VERIFY_OK")
print("a0", a0_num)
print("R0", float(R0))
print("actual_Edot", actual, float(actual))
print("claimed_bound_Edot", claimed, float(claimed))
