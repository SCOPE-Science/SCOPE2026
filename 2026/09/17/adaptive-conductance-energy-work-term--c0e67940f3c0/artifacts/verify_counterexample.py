from math import exp

# Nominal values used in the source paper's energy experiment / model code.
a = 1.2
b = 1.5
C = 1.0
alpha_G = 0.30
lambda_G = 0.10
tau_G = 5.0
k_sigma = 3.0
x = 1.49


def f(v):
    return a * v * (v * v - b * b)


def sigma(v):
    return 1.0 / (1.0 + exp(-k_sigma * v))


# Two-cell antisymmetric state V=(-x,x), with no GRN/external/wound forcing.
# This G makes both voltage derivatives exactly zero analytically.
G = 0.5 * a * (b * b - x * x)
V1, V2 = -x, x
V1_dot = (-f(V1) + G * (V2 - V1)) / C
V2_dot = (-f(V2) + G * (V1 - V2)) / C

# Adaptive conductance law with R=epsilon=0.
G_dot = (alpha_G * sigma(V1) * sigma(V2) - lambda_G * G) / tau_G

# Correct chain-rule contribution from the changing conductance.
E_dot = -C * (V1_dot * V1_dot + V2_dot * V2_dot) + 0.5 * G_dot * (V1 - V2) ** 2

print(f"G={G:.15f}")
print(f"V1_dot={V1_dot:.15e}")
print(f"V2_dot={V2_dot:.15e}")
print(f"G_dot={G_dot:.15e}")
print(f"E_dot={E_dot:.15e}")

assert abs(V1_dot) < 1e-12
assert abs(V2_dot) < 1e-12
assert G_dot > 0.0
assert E_dot > 0.0
