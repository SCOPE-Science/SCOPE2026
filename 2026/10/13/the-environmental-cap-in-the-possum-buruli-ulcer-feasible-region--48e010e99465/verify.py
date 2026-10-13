#!/usr/bin/env python3
from fractions import Fraction as F
import sympy as sp

# Symbolic top-face identities.
alphaE, muE, Km, H, Im = sp.symbols("alphaE muE Km H Im", positive=True)
Eprime = alphaE*Im - muE*H
Hstar = alphaE*Km/muE
Epub = alphaE/muE

assert sp.simplify(Eprime.subs({Im:Km,H:Hstar})) == 0
assert sp.simplify(Eprime.subs({Im:Km,H:Epub}) - alphaE*(Km-1)) == 0

# Exact source Table 1 parameters.
Lambda_m = F(2)
mu_m = F(1,365*60)
Lambda_v = F(5)
mu_v = F(1,14)
alpha_E = F(1,14)
mu_E = F(1,14)

K_m = Lambda_m/mu_m
K_v = Lambda_v/mu_v
E_pub = alpha_E/mu_E
H_star = alpha_E*K_m/mu_E

assert K_m == 43800
assert K_v == 70
assert E_pub == 1
assert H_star == 43800

# Boundary witness.
S_m,I_m,S_v,I_v,E = F(1),F(2),F(1),F(1),F(1)
assert S_m+I_m < K_m
assert S_v+I_v < K_v
assert E == E_pub

E_dot = alpha_E*I_m - mu_E*E
assert E_dot == F(1,14)
assert E_dot > 0

# Corrected top face is inward for the worst admissible I_m.
worst_corrected = alpha_E*K_m - mu_E*H_star
assert worst_corrected == 0

# Published top face would be inward uniformly iff K_m <= 1.
worst_published = alpha_E*K_m - mu_E*E_pub
assert worst_published == alpha_E*(K_m-1)
assert worst_published > 0

print("VERIFY_OK")
print("K_m", K_m)
print("K_v", K_v)
print("E_published", E_pub)
print("E_corrected", H_star)
print("witness_E_dot", E_dot)
