#!/usr/bin/env python3
import math

lam = 10.0
dS = dV = dI = p = s = dE = k = sigma = c = h1 = dA = h2 = omega = 1.0
q = gamma = 1.0
dC, xi = 2.0, 1.0

Eb = s / dE
Db = dI + p * Eb
beta_c = dS * dV * Db / (k * lam)

def I_of_E(E):
    return (dE * E - s) * (h1 + E) / (c * E)

def D(E):
    return dI + p * E

def F(beta, E):
    I = I_of_E(E)
    return D(E) * (dS * dV / (beta * k) + (1.0 + dS * sigma / beta) * I)

def solve_E(beta):
    assert beta > beta_c
    lo = Eb
    hi = 2.0
    while F(beta, hi) <= lam:
        hi *= 2.0
    for _ in range(150):
        mid = (lo + hi) / 2.0
        if F(beta, mid) < lam:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0

IA = dA * dV * h2 / (omega * k)
b = dE * h1 - s - c * IA
disc = b * b + 4.0 * dE * s * h1
EA = (-b + math.sqrt(disc)) / (2.0 * dE)
DA = D(EA)
assert lam > DA * IA
beta_A = DA * dS * (dV + sigma * k * IA) / (k * (lam - DA * IA))
assert beta_A > beta_c

def equilibrium(beta):
    E = solve_E(beta)
    I = I_of_E(E)
    V = k * I / dV
    S = D(E) * (dV + sigma * k * I) / (beta * k)
    C = gamma * I / (dC - xi)
    A = 0.0
    return S, I, V, C, E, A

def residuals(beta, x):
    S,I,V,C,E,A = x
    return [
        lam - dS*S - beta*S*V/(1.0+sigma*V),
        beta*S*V/(1.0+sigma*V) - dI*I - p*E*I,
        k*I - dV*V - q*A*V,
        gamma*I + xi*C - dC*C,
        s + c*I*E/(h1+E) - dE*E,
        omega*V*A/(h2+A) - dA*A,
    ]

for beta in (0.5 * (beta_c + beta_A), 1.5 * beta_A):
    x = equilibrium(beta)
    assert max(abs(r) for r in residuals(beta, x)) < 1e-10
    rA = omega * x[2] / h2 - dA
    if beta < beta_A:
        assert rA < 0.0
    else:
        assert rA > 0.0

xA = equilibrium(beta_A)
assert abs(xA[1] - IA) < 1e-10
assert abs(omega * xA[2] / h2 - dA) < 1e-10

betas = [beta_c * 1.1, 0.5 * (beta_c + beta_A), beta_A, 2.0 * beta_A]
vals = [equilibrium(b) for b in betas]
assert all(vals[j][1] < vals[j+1][1] for j in range(len(vals)-1))
assert all(vals[j][2] < vals[j+1][2] for j in range(len(vals)-1))

print("VERIFY_OK")
