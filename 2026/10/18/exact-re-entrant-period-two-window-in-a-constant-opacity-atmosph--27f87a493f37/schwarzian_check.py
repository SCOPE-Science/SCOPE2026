#!/usr/bin/env python3
"""High-precision differential check of the opacity map's Schwarzian identity.

Requires mpmath. These sample checks supplement an all-parameter calculus proof.
"""
import mpmath as mp
mp.mp.dps = 50

samples = [
    ("2", "4", "0"),
    ("3", "30", "0.25"),
    ("3", "30", "1"),
    ("8", "20", "0.15"),
    ("1.05", "120", "2"),
]
for gs, ps, xs in samples:
    gamma, p2, x = map(mp.mpf, (gs, ps, xs))
    a, b = 1 + 1 / gamma, 1 - 1 / gamma
    h = lambda v: (a + b * mp.exp(-gamma * v)) ** (-mp.mpf(1) / 4)
    f = lambda v: mp.exp(-p2 * h(v))
    f1, f2, f3 = (mp.diff(f, x, k) for k in (1, 2, 3))
    numerical = f3 / f1 - mp.mpf(3) / 2 * (f2 / f1) ** 2
    u = mp.exp(-gamma * x)
    r = b * u / (a + b * u)
    hp = (b * gamma / 4) * u / (a + b * u) ** (mp.mpf(5) / 4)
    analytical = gamma ** 2 * (-mp.mpf(1) / 2 + mp.mpf(15) / 32 * r ** 2) - p2 ** 2 * hp ** 2 / 2
    assert abs(numerical - analytical) / (1 + abs(numerical)) < mp.mpf('1e-44')
    assert numerical < 0
print('PASS 5 high-precision Schwarzian-identity comparisons')
