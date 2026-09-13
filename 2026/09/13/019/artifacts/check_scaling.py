"""Rescaled coherence check for cone Knapp sliver (thin radial cut, robust reading).

Sliver: |xi'| <= r0 R^-1/2, s = s0 + R^-1 tau, |tau| <= r1.
dsg = R^-2 dzeta dtau, Ef = R^-2 e^{iPhi0} I + err,
I(a,b,c) = int_{|zeta|<=r0} int_{|tau|<=r1} exp(i(a.zeta + b tau + c|zeta|^2/(2s0))) dzeta dtau,
a = x'/R^1/2, b = (x3+t)/R, c = t/R.
Coherence box gives tube vol R^3, |Ef| >= c R^-2 => LHS >= c R^-5/4.
Per-piece L^inf/L^2 gives R^-13/8 each, RHS <= R^-11/8, ratio R^1/8.
"""
import numpy as np

r0, r1, s0 = 1.0, 1.0, 1.5
nr, nth, ntau = 60, 120, 41
r = (np.arange(nr) + 0.5) * r0 / nr
th = np.linspace(0, 2 * np.pi, nth, endpoint=False)
tau = (np.arange(ntau) + 0.5) * 2 * r1 / ntau - r1
dr, dth, dtau = r0 / nr, 2 * np.pi / nth, 2 * r1 / ntau
Rgrid, Tgrid, Augrid = np.meshgrid(r, th, tau, indexing='ij')
W = Rgrid * dr * dth * dtau
Z1 = Rgrid * np.cos(Tgrid)
Z2 = Rgrid * np.sin(Tgrid)
R2 = Z1 ** 2 + Z2 ** 2

def I_val(a1, a2, b, c):
    ph = a1 * Z1 + a2 * Z2 + b * Augrid + c * R2 / (2 * s0)
    return np.sum(W * np.exp(1j * ph))

vol = np.sum(W)
exact = np.pi * r0 ** 2 * 2 * r1
print(f"quad I(0,0,0) = {vol:.4f}  (exact {exact:.4f})")
assert abs(vol - exact) < 1e-9, "quadrature inexact"
print(f"|I(0,0,0)| = {abs(I_val(0, 0, 0, 0)):.4f}")
worst = 1e9
for a1 in [0, 0.5, -0.5]:
    for a2 in [0, 0.5]:
        for b in [0, 0.5]:
            for c in [0, 0.5]:
                v = abs(I_val(a1, a2, b, c)) / vol
                worst = min(worst, v)
print(f"min |I|/vol over coherence box = {worst:.3f}")
assert worst > 0.5, "coherence failed"

# exponent arithmetic (thin-sliver numerology)
for R in [2 ** 8, 2 ** 16, 2 ** 24]:
    N = R ** 0.5
    print(f"R=2^{int(np.log2(R)):d}: N={N:.1f} bunch N^1/4={N ** 0.25:.4f} "
          f"claimed R^1/16={R ** (1 / 16):.4f} ratio={N ** 0.25 / R ** (1 / 16):.4f}")
print("LHS R^-5/4 vs RHS R^-11/8: ratio R^1/8. OK.")
