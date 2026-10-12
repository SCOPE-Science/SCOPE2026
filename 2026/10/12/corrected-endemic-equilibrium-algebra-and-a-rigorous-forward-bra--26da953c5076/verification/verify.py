#!/usr/bin/env python3
Pi = 40.0
d = 0.01
lam = 0.000025
c = 0.5
mu = 0.15
delta = 0.01
q = 0.02
r1 = 0.002
h = 0.03
r2 = 0.023
r3 = 0.02
omega = 0.003
gamma = 0.0025
theta = 0.015

A0 = omega / theta

def B0(A):
    return d + delta + (q + r1) * A

def B1(A):
    return d + delta + (h + r2) * A

def B2(A):
    return d + delta + r3 * A

def L(A):
    return 1.0 + q*A/B1(A) + h*q*A*A/(B1(A)*B2(A))

def IofA(A):
    return (theta*A - omega) / (gamma * L(A))

def SofA(A, la):
    return (1.0 + c*A) * (mu + d) * B0(A) / (mu * la)

def psi(A, la):
    return Pi - d*SofA(A, la) - (mu + d) * B0(A) * IofA(A) / mu

lambda_c = d * (1.0 + c*A0) * (mu + d) * B0(A0) / (mu * Pi)
R0 = lam / lambda_c
R0_formula = lam * Pi * mu / (
    d * (1.0 + c*A0) * (mu + d) * B0(A0)
)
assert abs(R0 - R0_formula) < 1e-14
assert R0 > 1.0

lo = A0
hi = 2.0
while psi(hi, lam) > 0.0:
    hi *= 2.0
for _ in range(160):
    mid = 0.5 * (lo + hi)
    if psi(mid, lam) > 0.0:
        lo = mid
    else:
        hi = mid
A = 0.5 * (lo + hi)
I = IofA(A)
Q = q*A*I/B1(A)
H = h*A*Q/B2(A)
E = B0(A)*I/mu
S = SofA(A, lam)
R = A*(r1*I + r2*Q + r3*H)/d

res = [
    Pi - lam*S*I/(1.0 + c*A) - d*S,
    lam*S*I/(1.0 + c*A) - (mu + d)*E,
    mu*E - B0(A)*I,
    q*A*I - B1(A)*Q,
    h*A*Q - B2(A)*H,
    A*(r1*I + r2*Q + r3*H) - d*R,
    omega + gamma*(I + Q + H) - theta*A,
]
assert max(abs(x) for x in res) < 1e-10

I_src = mu * (Pi - d*S) / (
    (1.0 + c*A) * (mu + d) * B0(A)
)
source_residual = Pi - lam*S*I_src/(1.0 + c*A) - d*S
predicted_residual = (Pi - d*S) * c*A/(1.0 + c*A)
assert source_residual > 0.0
assert abs(source_residual - predicted_residual) < 1e-12
assert abs(I - mu*(Pi-d*S)/((mu+d)*B0(A))) < 1e-10

C0 = d * (mu + d) / mu
d_product = c*B0(A0) + (1.0 + c*A0)*(q + r1)
psi_lambda = Pi / lambda_c
Iprime0 = theta / (gamma * L(A0))
psi_A = -C0 * d_product / lambda_c - ((mu+d)/mu)*B0(A0)*Iprime0
assert psi_lambda > 0.0
assert psi_A < 0.0
assert -psi_lambda/psi_A > 0.0

print("VERIFY_OK")
print("R0", format(R0, ".12f"))
print("A_star", format(A, ".12f"))
print("I_star", format(I, ".12f"))
print("I_source", format(I_src, ".12f"))
print("source_residual", format(source_residual, ".12f"))
