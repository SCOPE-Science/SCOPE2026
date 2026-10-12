#!/usr/bin/env python3
import math

TARGET = 3.0 / math.log(2.0)

def quantities(d):
    x = float(d - 1)
    eta = 1.0 - d ** -2
    u = x ** (1.0 / 3.0) + x ** (-1.0 / 3.0)
    cstar = 2.0 / (u - 1.0) ** 2 - 1.0
    pstar = (1.0 - cstar) / (2.0 * eta)
    s = 3.0 * math.log2(u)
    kappa = (d * d - 1.0) / (d * (d - 2.0)) * math.log2(d - 1.0)
    p_left = (d - 2.0) ** 2 / (d * d - 1.0)
    witness = pstar * (s * eta - kappa)
    upper = math.log2(d) * (1.0 - d * math.log2(d) / ((d - 1.0) * s))
    return pstar, p_left, witness, upper

print("target", format(TARGET, ".12f"))
last_scaled = -1.0
for d in (10**3, 10**4, 10**6, 10**9):
    pstar, p_left, witness, upper = quantities(d)
    scaled_w = d ** (2.0 / 3.0) * witness
    scaled_u = d ** (2.0 / 3.0) * upper
    assert 0.0 < pstar < p_left < 1.0
    assert 0.0 <= witness <= upper + 1e-12
    assert scaled_w > last_scaled
    last_scaled = scaled_w
    print(d, "p*", format(pstar, ".12g"), "d^(2/3) witness", format(scaled_w, ".12g"), "d^(2/3) upper", format(scaled_u, ".12g"))
assert abs(last_scaled - TARGET) < 0.07
print("VERIFY_OK")
