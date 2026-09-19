"""Verify collocation-resolution asymptotics for a hard-constrained smooth trial.

The trial u(x)=log(2)*x*(1-x) is exactly the paper's architecture with
raw network output identically zero.  The script computes the standard and
singularity-weighted strong residual losses on x_i=i/(N+1).
"""
import math
import numpy as np

A = math.log(2.0)
BETA = 1.0


def losses(N: int, alpha: float):
    x = np.arange(1, N + 1, dtype=np.float64) / (N + 1.0)
    u = A * x * (1.0 - x)
    residual = 2.0 * A - u ** (-alpha)
    standard = np.mean(residual * residual)
    weight = 1.0 + BETA * u ** (-alpha)
    weighted = np.mean(weight * residual * residual)
    return standard, weighted


print(f"A=log(2)={A:.15f}")
print("trial: u(x)=A*x*(1-x), beta=1")
print()

cases = [
    (1.0 / 3.0, "weighted critical: predicted L_w ~ (2/A) log N"),
    (0.5, "standard critical and weighted supercritical"),
    (0.6, "both supercritical"),
]
Ns = [2**k for k in (10, 12, 14, 16, 18, 20)]
for alpha, label in cases:
    print(f"alpha={alpha:.12g} -- {label}")
    prev = None
    for N in Ns:
        s, w = losses(N, alpha)
        slope_s = slope_w = float('nan')
        if prev is not None:
            N0, s0, w0 = prev
            slope_s = math.log(s / s0) / math.log(N / N0)
            slope_w = math.log(w / w0) / math.log(N / N0)
        extras = []
        if abs(alpha - 1.0/3.0) < 1e-14:
            extras.append(f"Lw/logN={w/math.log(N):.9f}")
        if abs(alpha - 0.5) < 1e-14:
            extras.append(f"Lstd/logN={s/math.log(N):.9f}")
            extras.append(f"Lw/sqrtN={w/math.sqrt(N):.9f}")
        if abs(alpha - 0.6) < 1e-14:
            extras.append(f"Lstd/N^0.2={s/N**0.2:.9f}")
            extras.append(f"Lw/N^0.8={w/N**0.8:.9f}")
        print(
            f"N={N:7d} Lstd={s:.9e} Lw={w:.9e} "
            f"slopes=({slope_s:.6f},{slope_w:.6f}) " + " ".join(extras)
        )
        prev = (N, s, w)
    print()

print("predicted critical constants")
print(f"2/A = {2.0/A:.12f}")
try:
    import mpmath as mp
    c = 2.0 * A**(-1.5) * float(mp.zeta(1.5))
    print(f"2*A^(-3/2)*zeta(3/2) = {c:.12f}")
except Exception:
    pass
