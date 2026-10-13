#!/usr/bin/env python3
import math

H = 4_890_000.0
mu = 0.0003548
alpha = 1.0
eps = 0.0149
mu1 = mu + alpha + eps
omega = 0.33 * 7.0
K = 1.0
sigma = 1.155
beta_c = 4.095e-7 / 1.45
beta_h = 1.024e-7 / 1.45
xi = 1.25 / H
zeta = 0.125

def kfun(g):
    return xi*xi * zeta / math.sqrt(zeta*zeta + (g*H*xi)**2)

def phi(g):
    k = kfun(g)
    if k*H <= beta_h:
        return beta_h*H - 0.5*k*H*H
    return beta_h*beta_h/(2.0*k)

g0 = beta_c*H/(omega*K)
k0 = kfun(g0)
phi0 = phi(g0)
F0 = phi0 + g0*sigma
margin = mu1 - F0

# Source deterministic R0 reconstructed from its two transmission routes.
R0 = (beta_h*H + beta_c*H*sigma/(omega*K)) / mu1
Rstar0 = R0 * mu1/(mu1 + 0.5*k0*H*H)
Rstar_low = R0 * mu1/(mu1 + 0.5*xi*xi*H*H)

assert abs(g0 - 0.5978369905956113) < 1e-12
assert abs(k0 - 1.0780213764790616e-14) < 1e-24
assert abs(phi0 - 0.2164463976312683) < 1e-12
assert abs(F0 - 0.9069481217691993) < 1e-12
assert abs(margin - 0.1083066782308007) < 1e-12
assert abs(R0 - 1.0202728384556509) < 1e-12
assert abs(Rstar0 - 0.9053382105026572) < 1e-12
assert abs(Rstar_low - 0.5765845415785831) < 1e-12
assert beta_h/k0 > H
assert F0 < mu1
assert Rstar_low < 1.0 < R0

# Broad monotonicity consistency check.
gs = [10**(-8 + i*0.02) for i in range(651)]
ks = [kfun(g) for g in gs]
Fs = [phi(g)+g*sigma for g in gs]
assert all(ks[i+1] < ks[i] for i in range(len(ks)-1))
assert all(Fs[i+1] > Fs[i] for i in range(len(Fs)-1))

print("VERIFY_OK")
print("g0", g0)
print("k0", k0)
print("phi0", phi0)
print("F0", F0)
print("mu1", mu1)
print("margin", margin)
print("R0", R0)
print("Rstar_g0", Rstar0)
print("Rstar_lower_limit", Rstar_low)
