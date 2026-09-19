import cmath
import math


def roots(gamma, h):
    a = 1.0 + 1j * gamma * h
    b = -(1.0 - 2j * h)
    c = -1j * h
    disc = b * b - 4.0 * a * c
    s = cmath.sqrt(disc)
    return ((-b + s) / (2.0 * a), (-b - s) / (2.0 * a))


def rho_direct(gamma, h):
    return max(abs(r) for r in roots(gamma, h))


def rho_closed(gamma, h):
    if gamma <= -1.0:
        u = math.sqrt(1.0 - 4.0 * (1.0 + gamma) * h * h)
        return math.sqrt((1.0 + u) / (gamma + 2.0 - gamma * u))
    hc = 1.0 / (2.0 * math.sqrt(1.0 + gamma))
    if h <= hc:
        u = math.sqrt(max(0.0, 1.0 - 4.0 * (1.0 + gamma) * h * h))
        return math.sqrt((1.0 + u) / (gamma + 2.0 - gamma * u))
    t = math.sqrt(4.0 * (1.0 + gamma) * h * h - 1.0)
    w = t / math.sqrt(1.0 + t * t)
    return 1.0 / math.sqrt(gamma + 2.0 - 2.0 * math.sqrt(gamma + 1.0) * w)


def check_gamma(gamma):
    hc = 1.0 / (2.0 * math.sqrt(1.0 + gamma))
    rmin = 1.0 / math.sqrt(gamma + 2.0)
    samples = [0.2 * hc, 0.7 * hc, hc, 1.3 * hc, 3.0 * hc]
    err = max(abs(rho_direct(gamma, h) - rho_closed(gamma, h)) for h in samples)
    left = rho_direct(gamma, 0.999 * hc)
    at = rho_direct(gamma, hc)
    right = rho_direct(gamma, 1.001 * hc)
    return hc, rmin, err, left, at, right


print("Exact-rate verification for p(r)=(1+i*gamma*h)r^2-(1-2ih)r-ih")
print()
for gamma in [0.0, 0.5, 1.0, 2.0, 3.0, 5.0]:
    hc, rmin, err, left, at, right = check_gamma(gamma)
    print(
        f"gamma={gamma:3.1f}  h_opt={hc:.12f}  "
        f"rho_min={rmin:.12f}  max_formula_error={err:.3e}  "
        f"rho(0.999h*)={left:.12f}  rho(h*)={at:.12f}  rho(1.001h*)={right:.12f}"
    )

print()
gamma = 1.0
hopt = 1.0 / (2.0 * math.sqrt(2.0))
stability_ceiling = 0.5
print(f"matched_skew_h_opt={hopt:.12f}")
print(f"matched_skew_rho_min={rho_direct(gamma, hopt):.12f}")
print(f"matched_skew_rho_at_0.499={rho_direct(gamma, 0.499):.12f}")
print(f"matched_skew_stability_ceiling={stability_ceiling:.12f}")

print()
for gamma in [-1.5, -2.0, -3.0, -5.0]:
    values = [rho_direct(gamma, h) for h in [1.0, 10.0, 100.0, 1000.0]]
    limit = 1.0 / math.sqrt(-gamma)
    print(
        f"gamma={gamma:4.1f}  rho(1,10,100,1000)="
        + ",".join(f"{x:.12f}" for x in values)
        + f"  predicted_limit={limit:.12f}"
    )
