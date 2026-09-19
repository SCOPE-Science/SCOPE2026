import math
import numpy as np


def root_x(kappa, iters=100):
    if kappa == 0:
        return 0.0
    lo, hi = 0.0, math.pi
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        val = mid * math.tan(0.5 * mid)
        if val < kappa:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def overlap_limit(kappa):
    x = root_x(kappa)
    if x == 0.0:
        return 1.0
    num = 2.0 * math.sin(0.5 * x) / x
    den = math.sqrt(0.5 + math.sin(x) / (2.0 * x))
    return num / den


def energy_limit(kappa):
    if kappa == 0.0:
        return 1.0
    x = root_x(kappa)
    j = 2.0 * (kappa - 1.0 + math.exp(-kappa)) / (kappa * kappa)
    lam = 2.0 * kappa / (kappa * kappa + x * x)
    return j / lam


def top_mode_direct(n, kappa):
    rho = 1.0 - kappa / n
    idx = np.arange(n)
    r = rho ** np.abs(idx[:, None] - idx[None, :])
    vals, vecs = np.linalg.eigh(r)
    v = vecs[:, -1]
    if np.sum(v) < 0:
        v = -v
    d = np.ones(n) / math.sqrt(n)
    return float(np.dot(v, d)), float(vals[-1] / n), float(d @ r @ d / vals[-1])


def exact_frequency_overlap(n, kappa):
    rho = 1.0 - kappa / n
    # Solve the exact first symmetric equation in x=N*omega:
    # tan(x/2) tan(x/(2N)) = (1-rho)/(1+rho).
    rhs = (1.0 - rho) / (1.0 + rho)
    lo, hi = 0.0, math.pi
    for _ in range(100):
        x = 0.5 * (lo + hi)
        val = math.tan(0.5 * x) * math.tan(x / (2.0 * n))
        if val < rhs:
            lo = x
        else:
            hi = x
    x = 0.5 * (lo + hi)
    omega = x / n
    s = math.sin(0.5 * n * omega) / math.sin(0.5 * omega)
    q = n / 2.0 + math.sin(n * omega) / (2.0 * math.sin(omega))
    return s / math.sqrt(n * q), x


print("Local-to-unity AR(1) KLT/DCT boundary-layer verification")
print("Columns: kappa, limit_overlap, exact_N2000_overlap, direct_N256_overlap, direct_N256_lambda/N, energy_ratio_N256, energy_limit")
for kappa in (0.1, 1.0, 5.0, 20.0):
    alim = overlap_limit(kappa)
    a2000, _ = exact_frequency_overlap(2000, kappa)
    ad, lamd, ed = top_mode_direct(256, kappa)
    print(f"{kappa:4.1f}  {alim:.12f}  {a2000:.12f}  {ad:.12f}  {lamd:.12f}  {ed:.12f}  {energy_limit(kappa):.12f}")

ainf = 2.0 * math.sqrt(2.0) / math.pi
angle = math.degrees(math.acos(ainf))
dist = math.sqrt(2.0 - 2.0 * ainf)
print(f"infinite-kappa overlap = {ainf:.12f}")
print(f"infinite-kappa principal angle (deg) = {angle:.12f}")
print(f"infinite-kappa sign-aligned row distance = {dist:.12f}")
print(f"small-kappa angle/kappa coefficient = {1.0/(6.0*math.sqrt(5.0)):.12f}")
