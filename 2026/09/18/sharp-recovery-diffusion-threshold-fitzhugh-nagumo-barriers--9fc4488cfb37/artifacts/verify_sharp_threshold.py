from math import exp


def profile(x):
    if x < 0.0:
        return exp(x), exp(x)
    return 1.0, 0.0


def check_case(gamma, tilde_gamma, D):
    c0 = 1.0 / tilde_gamma
    worst_activator = float("inf")
    worst_recovery = float("inf")
    for x in (-8.0, -4.0, -1.0, -0.1, 0.1, 1.0):
        V, Vpp = profile(x)
        h = (1.0 + c0) * V
        activator_margin = h - c0 * V - Vpp
        recovery_margin = (gamma * c0 - 1.0) * V - D * c0 * Vpp
        worst_activator = min(worst_activator, activator_margin)
        worst_recovery = min(worst_recovery, recovery_margin)
    return worst_activator, worst_recovery


gamma = 2.0
tilde_gamma = 0.5
c0 = 1.0 / tilde_gamma
D_sharp = gamma - tilde_gamma
D_source = (gamma - tilde_gamma) / (1.0 + c0)

assert abs(D_sharp - 1.5) < 1e-15
assert abs(D_source - 0.5) < 1e-15
assert check_case(gamma, tilde_gamma, 1.4)[0] >= -1e-15
assert check_case(gamma, tilde_gamma, 1.4)[1] >= -1e-15
assert check_case(gamma, tilde_gamma, 1.6)[1] < 0.0

print(f"exact threshold: {D_sharp:.12g}")
print(f"source sufficient bound: {D_source:.12g}")
print(f"ratio: {D_sharp / D_source:.12g}")
for c0 in (2.0, 4.0, 10.0, 100.0):
    tilde_gamma = 1.0 / c0
    exact = gamma - tilde_gamma
    source = exact / (1.0 + c0)
    print(f"c0={c0:g}: exact/source={exact/source:.12g}")
