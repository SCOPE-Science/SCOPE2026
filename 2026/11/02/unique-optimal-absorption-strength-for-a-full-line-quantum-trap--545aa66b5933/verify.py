#!/usr/bin/env python3
"""Reproduce exact absorption integrals, optimizer, and independent finite-time checks.
Dependencies: mpmath, numpy, scipy; invoke `python verify.py`.
"""
import math
import mpmath as mp
import numpy as np
from scipy.integrate import quad
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply

mp.mp.dps = 55

def q_band(J, eta):
    return (eta / mp.pi) * mp.quad(
        lambda w: 1 / (eta + mp.sqrt(4 * J * J - w * w)) ** 2,
        [-2 * J, 0, 2 * J],
    )

def q_out(J, eta, m):
    return (4 * eta * J / mp.pi) * mp.quad(
        lambda u: mp.exp(-2 * m * u) * mp.sinh(u)
        / (eta ** 2 + 4 * J ** 2 * mp.sinh(u) ** 2),
        [0, 1, mp.inf],
    )

def q_band_closed(a):
    if abs(a - 1) < mp.mpf('1e-30'):
        return 2 / (3 * mp.pi)
    if a < 1:
        k = mp.sqrt(1 - a * a)
        return 2 * a * (mp.atanh(k) - k) / (mp.pi * k ** 3)
    k = mp.sqrt(a * a - 1)
    return 2 * a * (k - mp.acos(1 / a)) / (mp.pi * k ** 3)

def critical(k):
    return (3 - 2 * k * k) * (mp.atanh(k) - k) - k ** 3

# Positive coefficients beyond the single negative fifth-order coefficient
for m in range(3, 80):
    c = mp.mpf(2 * m - 5) / ((2 * m - 1) * (2 * m + 1))
    assert c > 0
assert critical(mp.mpf('.75')) < 0 < critical(mp.mpf('.81'))

kstar = mp.findroot(critical, (mp.mpf('.75'), mp.mpf('.81')))
astar = mp.sqrt(1 - kstar**2)
assert abs(critical(kstar)) < mp.mpf('1e-45')
assert abs(2 * astar - mp.mpf('1.225741123666203284523450349692')) < mp.mpf('1e-28')
assert abs(q_band_closed(astar) - mp.mpf('0.222796320563446058885933877582')) < mp.mpf('1e-28')

# Independently integrate over the spectral band and in the closed form.
for J, eta in [(mp.mpf('1'), mp.mpf('0.5')), (mp.mpf('1'), mp.mpf('1')),
               (mp.mpf('1'), mp.mpf('2')), (mp.mpf('2'), mp.mpf('3'))]:
    b = q_band(J, eta)
    assert abs(b - q_band_closed(eta / (2 * J))) < mp.mpf('1e-45')
    for m in [0, 1, 3, 7]:
        assert 0 < b < b + q_out(J, eta, m) < 1
    for m in [2, 4, 8]:
        assert q_out(J, eta, m-1) > q_out(J, eta, m) > 0

# High-distance two-term Watson law, checked without relying on a truncated series.
for J, eta in [(mp.mpf('1'), mp.mpf('1')), (mp.mpf('2'), mp.mpf('3'))]:
    c2 = J / (mp.pi * eta)
    c4 = J / (4 * mp.pi * eta) - 6 * J**3 / (mp.pi * eta**3)
    for m in [30, 60, 100]:
        rem = q_out(J, eta, m) - c2 / m**2 - c4 / m**4
        assert abs(rem) < 40 / m**6

# An independent finite-volume Schrödinger calculation at fixed time.
N, J_f, eta_f, t = 501, 1.0, float(2 * astar), 85.0
H = diags([np.full(N-1, J_f), np.full(N-1, J_f)], [-1, 1],
          shape=(N, N), dtype=np.complex128, format='lil')
H[N//2, N//2] = -1j * eta_f
H = H.tocsr()
band_float = float(q_band(mp.mpf('1'), mp.mpf(str(eta_f))))
for m in [0, 1, 5, 10]:
    psi = np.zeros(N, dtype=complex)
    psi[N//2 + m] = 1
    after = expm_multiply(-1j * t * H, psi)
    observed_loss = 1 - np.vdot(after, after).real
    predicted_loss = band_float + float(q_out(mp.mpf('1'), mp.mpf(str(eta_f)), m))
    assert 0 < predicted_loss - observed_loss < .002

# Independent frequency-domain quadrature: 2 eta/(2pi) times spectral norm squared.
for m in [0, 2, 5]:
    eta, J = 1.0, 1.0
    inside = (eta / np.pi) * quad(
        lambda w: 1 / (eta + np.sqrt(4 * J**2 - w*w))**2,
        -2*J, 2*J, epsabs=1e-12)[0]
    outside = (2*eta / np.pi) * quad(
        lambda w:
         np.exp(-2*m*np.arccosh(w/(2*J))) /
         (eta**2 + w*w - 4*J*J),
         2*J, np.inf, epsabs=1e-12)[0]
    exact = float(q_band(mp.mpf('1'), mp.mpf('1')) + q_out(mp.mpf('1'),mp.mpf('1'),m))
    assert abs(inside + outside - exact) < 1e-10

print('PASS: band/exterior spectral quadratures, exact closed form,')
print('      strict distance decrease, two-term asymptotics, optimizer,')
print('      and independent finite-time Schrödinger dynamics')
print('critical coupling eta/J =', mp.nstr(2 * astar, 34))
print('maximal distant-source absorption =', mp.nstr(q_band_closed(astar), 34))
