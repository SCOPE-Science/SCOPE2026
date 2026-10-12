#!/usr/bin/env python3
import math
from scipy.integrate import solve_ivp

mu0 = 2.0
mu1 = 4.0
mu2 = 3.0
alpha = 1.0
S0 = 4.0
A0 = mu0*S0

def theta(I):
    return 1.0/(1.0 + 0.5*I)

theta0 = 1.0
theta1 = -0.5
K = theta0*mu1/mu0 - S0*theta1*alpha/mu2
assert abs(K - 8.0/3.0) < 1e-14

def rhs(t, y):
    S,E,I = y
    return [
        A0 - theta(I)*S*E - mu0*S,
        theta(I)*S*E - mu1*E,
        alpha*E - mu2*I,
    ]

sol = solve_ivp(
    rhs, (0.0, 2.0e5), [3.7, 0.08, 0.03],
    rtol=2e-10, atol=1e-12, max_step=40.0
)
S,E,I = sol.y[:, -1]
t = sol.t[-1]

vals = [t*E, t*I, t*(S0-S)]
targets = [1.0/K, (alpha/mu2)/K, (mu1/mu0)/K]

for got, target in zip(vals, targets):
    assert abs(got-target)/max(1.0,abs(target)) < 0.01

print("VERIFY_OK")
print("K", K)
print("scaled_state", vals)
print("target_state", targets)
