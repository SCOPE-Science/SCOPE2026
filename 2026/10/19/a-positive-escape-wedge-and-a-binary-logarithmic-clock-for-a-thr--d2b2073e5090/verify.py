"""Finite numerical diagnostics for the lagged-flux Chialvo escape theorem.

Run: python verify.py
Requires: mpmath. This checks sample trajectories, not the infinite-time proof.
"""

from mpmath import mp

mp.dps = 80
S = mp.mpf
PARAMETERS = [
    ('.5', '.4', '.89', '-.44', '.5', '.1', '.1', '.1', '.2'),
    ('.8', '.1', '-2', '-5', '.1', '0', '1', '.05', '.9'),
    ('.2', '2', '1.2', '100', '3', '2', '.02', '2', '0'),
]

for sample, item in enumerate(PARAMETERS, start=1):
    a, b, c, k0, k, alpha, beta, k1, k2 = map(S, item)
    K = k1 / (1 + k2)
    B = S(9) * k * beta * K * K / 4
    A = 3 * k * beta * k1 * k1
    Phi = mp.sqrt(S(5) / (3 * k * beta))
    R = max(S(2), abs(k0) + 2, Phi / K + 2, mp.sqrt(S(10) / B) + 2)
    Y = max(S(0), c / (1 - a))
    assert (1 - a) * Y >= c
    assert 3 * k * beta * Phi**2 > 4
    assert B * R**2 > 9
    x, y, phi = R + 1, Y - 1, None
    phi = (Phi + K * x) / 2
    x_hist, y_hist, phi_hist = [x], [y], [phi]

    for n in range(12):
        assert x > R and y < Y and Phi < phi < K * x
        x_next = x**2 * mp.exp(y - x) + k0 + k * x * (alpha + 3 * beta * phi**2)
        y_next = a * y - b * x + c
        phi_next = k1 * x - k2 * phi
        assert x_next > 3 * x
        assert x_next > R and y_next < Y and Phi < phi_next < K * x_next
        if n >= 1:
            assert x_next >= B * x * x_hist[-2]**2
        x, y, phi = x_next, y_next, phi_next
        x_hist.append(x)
        y_hist.append(y)
        phi_hist.append(phi)

    for n in (9, 10, 11):
        flux_ratio = phi_hist[n] / x_hist[n - 1]
        recovery_ratio = y_hist[n] / x_hist[n - 1]
        recurrence_ratio = x_hist[n + 1] / (A * x_hist[n] * x_hist[n - 1]**2)
        assert mp.almosteq(flux_ratio, k1, rel_eps=S('1e-10'))
        assert mp.almosteq(recovery_ratio, -b, rel_eps=S('1e-10'))
        assert mp.almosteq(recurrence_ratio, 1, rel_eps=S('1e-10'))
    heights = [mp.log(x_hist[n]) / 2**n for n in (9, 10, 11)]
    assert all(v > 0 and mp.isfinite(v) for v in heights)
    print(f'example {sample}: cone and lag ratios checked, finite heights:',
          ', '.join(mp.nstr(v, 13) for v in heights))

print('PASS: 3 parameter choices; 36 invariant-cone steps; 9 lag-ratio triplets.')
