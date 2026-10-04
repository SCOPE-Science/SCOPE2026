#!/usr/bin/env python3
import math
import numpy as np
from scipy.optimize import brentq
from scipy.linalg import expm, eigvals
from scipy.integrate import quad

pi = 0.5
Lambda = 10.0
mu = 1.0
delta = 1.0
beta_b = 10.0
beta_v = 10.0
sigma1 = sigma2 = sigma3 = 1.0

eta1 = 0.1
jump_rate = 1.0

mu1 = mu + sigma1**2/2.0 + jump_rate*(eta1-math.log1p(eta1))
mu2 = mu + sigma2**2/2.0
mu3 = mu + sigma3**2/2.0

Rtilde = Lambda/(mu3+delta) * (
    (1.0-pi)*beta_b/mu1 + pi*beta_v/mu2
)
assert Rtilde > 1.0

def incidence(I):
    return I/(1.0+I)

def Sstar(I):
    return (1.0-pi)*Lambda/(mu1 + beta_b*incidence(I))

def Vstar(I):
    return pi*Lambda/(mu2 + beta_v*incidence(I))

def root_eq(I):
    return (beta_b*Sstar(I)+beta_v*Vstar(I))/(1.0+I) - (mu3+delta)

Istar = brentq(root_eq, 1e-12, 100.0)
S = Sstar(Istar)
V = Vstar(Istar)

l11 = mu1 + beta_b*incidence(Istar)
l22 = mu2 + beta_v*incidence(Istar)
l13 = beta_b*Istar/(1.0+Istar)**2
l23 = beta_v*Istar/(1.0+Istar)**2
l31 = beta_b*S/(1.0+Istar)
l32 = beta_v*V/(1.0+Istar)
l33 = (beta_b*S+beta_v*V)*Istar/(1.0+Istar)**2

A = np.array([
    [-l11, 0.0, -l13],
    [0.0, -l22, -l23],
    [l31, l32, -l33],
], dtype=float)

ev = eigvals(A)
assert np.max(np.real(ev)) < 0.0

h1 = math.log1p(eta1)
e1 = np.array([1.0, 0.0, 0.0])

def fourth_integrand(s):
    propagated = float(e1 @ expm(A*s) @ e1)
    return jump_rate*(h1*propagated)**4

# The tail is negligible on this stable witness.
k4_main, err = quad(fourth_integrand, 0.0, 20.0, epsabs=1e-14, epsrel=1e-11, limit=300)
k4_tail, err2 = quad(fourth_integrand, 20.0, 80.0, epsabs=1e-16, epsrel=1e-10, limit=300)
k4 = k4_main + k4_tail
assert k4 > 2.0e-6
assert k4 < 2.5e-6

true_jump_var = jump_rate*h1*h1
source_jump_var = 2.0*jump_rate*(eta1-math.log1p(eta1))
assert abs(true_jump_var-source_jump_var) > 2.0e-4

print("VERIFY_OK")
print("mu1", repr(mu1))
print("Rtilde", repr(Rtilde))
print("Sstar", repr(S))
print("Vstar", repr(V))
print("Istar", repr(Istar))
print("eigvals", [complex(x) for x in ev])
print("kappa4_e1", repr(k4))
print("true_jump_variance_rate", repr(true_jump_var))
print("source_jump_replacement", repr(source_jump_var))
