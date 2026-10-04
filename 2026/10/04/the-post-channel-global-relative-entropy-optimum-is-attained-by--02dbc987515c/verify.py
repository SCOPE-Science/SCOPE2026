import math


def h2(x: float) -> float:
    if x == 0.0 or x == 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def bell_weights(p: float):
    return (1.0 - p, p / 3.0, p / 3.0, p / 3.0)


def er_bell_depolarized(p: float) -> float:
    if not (0.0 <= p <= 0.75):
        raise ValueError("p outside the channel range")
    if p >= 0.5:
        return 0.0
    return 1.0 - h2(p)


p = 0.2
n = 4
kappa = 0.1
weights = bell_weights(p)
assert abs(sum(weights) - 1.0) < 1e-15
assert max(weights) == 1.0 - p
single = er_bell_depolarized(p)
identity_value = n * single
candidate_ceiling = identity_value * math.exp(-kappa * n)
assert single > 0.0
assert candidate_ceiling < identity_value

print(f"Bell weights at p={p}: {weights}")
print(f"single-pair E_R: {single:.16f} bits")
print(f"n={n} identity-LOCC value: {identity_value:.16f} bits")
print(f"candidate damped ceiling at kappa={kappa}: {candidate_ceiling:.16f} bits")
print("VERIFY_OK")
