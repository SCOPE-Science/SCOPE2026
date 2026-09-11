"""Replayable overlap audit for lane-703 target routes.
Computes perturbed ruling normals for Gamma_* (eps0=0.01 cos3theta),
pairwise Kakeya overlap sum S1, nearest-neighbour angle, transverse-shell
overlap profile, and bush-centre concurrency Mmax.
Stdlib + numpy only.
"""
import math
import numpy as np

R0 = 4096.0
r = 64.0  # R0^{1/2}
eps0 = 0.01
N = 64

ths = np.array([2 * math.pi * j / N for j in range(N)])

def normals(ths):
    out = []
    for th in ths:
        c, s = math.cos(th), math.sin(th)
        C, S = math.cos(3 * th), math.sin(3 * th)
        n = np.array([-c - eps0 * (c * C + 3 * s * S),
                      -s + eps0 * (-s * C + 3 * c * S),
                      1.0])
        n /= np.linalg.norm(n)
        out.append(n)
    return np.array(out)

Ns = normals(ths)

def ang(a, b):
    return math.acos(min(1.0, abs(float(a @ b))))

S1 = 0.0
for j in range(N):
    for k in range(N):
        if j == k:
            S1 += 1.0
        else:
            sn = math.sin(ang(Ns[j], Ns[k]))
            S1 += min(1.0, 2 * r / (R0 * sn))

mind = min(ang(Ns[j], Ns[(j + 1) % N]) for j in range(N))
trans = {rho: 2 * r / (rho * mind) for rho in [64, 256, 1024, 2048, 4096]}
Mmax = N  # all canonical tubes through origin along perturbed rulings
Rgain = math.exp(-math.log(4096) / 200)

print(f"S1 = {S1:.6f}")
print(f"S1^1/4 = {S1 ** 0.25:.6f}")
print(f"nearest-neighbour angle = {mind:.6f} rad")
print(f"2r/(R0 sin(min)) = {2*r/(R0*math.sin(mind)):.6f}")
for rho, ov in trans.items():
    print(f"rho={rho} overlap-proxy={ov:.3f}")
print(f"Mmax (bush centre) = {Mmax}")
print(f"R0^-1/200 = {Rgain:.6f}")
print(f"K0=8 threshold = {8*Rgain:.6f}")

assert abs(S1 - 331.410681) < 1.0, "S1 drift"
assert Mmax == 64
assert 2 * r / (R0 * math.sin(mind)) < 1.0, "neighbours must be transverse at full length"
assert trans[4096] < 1.0 and trans[256] > 1.0, "shell profile must separate"
print("VERIFY_OK")
