from fractions import Fraction
from math import exp


def phi(u, q):
    n = len(q)
    return sum(u ** (1.0 - x) for x in q) - (n - 1) * u


def dphi(u, q):
    n = len(q)
    return sum((1.0 - x) * u ** (-x) for x in q) - (n - 1)


def invert_phi(y, q, steps=100):
    lo, hi = 0.0, 1.0
    for _ in range(steps):
        mid = (lo + hi) / 2.0
        if phi(mid, q) < y:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def elementary_from_power_sums(power_sums):
    # Newton identities: k e_k = sum_{i=1}^k (-1)^(i-1) e_{k-i} p_i.
    e = [Fraction(1)]
    for k in range(1, len(power_sums) + 1):
        rhs = sum((1 if i % 2 else -1) * e[k - i] * power_sums[i - 1]
                  for i in range(1, k + 1))
        e.append(rhs / k)
    return e


def polynomial_from_roots(roots):
    coeff = [Fraction(1)]
    for r in roots:
        nxt = [Fraction(0)] * (len(coeff) + 1)
        for j, c in enumerate(coeff):
            nxt[j] += c
            nxt[j + 1] -= c * r
        coeff = nxt
    return coeff


# Exact three-component example: lambda=(1,2,4), normalized q=(1,2,4)/7.
q_exact = [Fraction(1, 7), Fraction(2, 7), Fraction(4, 7)]
alpha = [1 - q for q in q_exact]
power_sums = [sum(a ** r for a in alpha) for r in range(1, 4)]
e = elementary_from_power_sums(power_sums)
newton_poly = [Fraction(1)] + [((-1) ** k) * e[k] for k in range(1, 4)]
expected_poly = polynomial_from_roots(alpha)
assert newton_poly == expected_poly

# Baseline-free elimination: S2(t) = Phi(S1(t)).
q_float = [float(q) for q in q_exact]
for t in [0.05, 0.2, 0.7, 1.3]:
    s1 = exp(-7.0 * t)
    s2_direct = exp(-6.0 * t) + exp(-5.0 * t) + exp(-3.0 * t) - 2.0 * exp(-7.0 * t)
    s2_transform = phi(s1, q_float)
    assert abs(s2_direct - s2_transform) < 2e-14

# Every admissible Phi is strictly increasing on (0,1).
for q in ([0.1, 0.2, 0.3, 0.4], [0.05, 0.15, 0.8], [0.5, 0.5]):
    for u in [0.02, 0.1, 0.3, 0.7, 0.95]:
        assert dphi(u, q) > 0.0

# A second-failure marginal alone can be reproduced with a different component count
# and different normalized hazards by changing the unknown baseline.
q_alt = [0.1, 0.2, 0.3, 0.4]
for t in [0.05, 0.2, 0.7, 1.3]:
    target = exp(-6.0 * t) + exp(-5.0 * t) + exp(-3.0 * t) - 2.0 * exp(-7.0 * t)
    b_alt = invert_phi(target, q_alt)
    assert 0.0 < b_alt < 1.0
    assert abs(phi(b_alt, q_alt) - target) < 2e-14

print("Exact Newton reconstruction polynomial:", newton_poly)
print("Baseline-free three-rate identity: verified at 4 points")
print("Strict monotonicity of Phi: verified for 3 distinct hazard profiles")
print("Second-marginal nonidentifiability: reproduced with 4 components")
print("All verification checks passed")
