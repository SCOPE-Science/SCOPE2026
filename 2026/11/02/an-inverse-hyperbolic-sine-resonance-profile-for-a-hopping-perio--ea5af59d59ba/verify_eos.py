"""Reproducible numerical diagnostics for the steep EOS period-three response.

Finite checks of residuals and asymptotics; they do not replace the proof.
Requires: mpmath (tested with Python 3).
"""
from mpmath import mp

mp.dps = 95


def diagnose(a_int, sigma_str):
    a = mp.mpf(a_int)
    sigma = mp.mpf(sigma_str)
    q = mp.exp(-a / 6)
    b = mp.mpf(1) / 3 + sigma * q

    def sigmoid(x):
        return 1 / (1 + mp.exp(-a * x))

    def f(x):
        return x + b - sigmoid(x)

    def h(z):
        x = -mp.mpf(1) / 2 + z / a
        return (f(f(f(x))) - x) / q

    z_lim = mp.asinh(3 * sigma / 2)
    z = mp.findroot(h, (z_lim - mp.mpf('0.02'), z_lim + mp.mpf('0.02')))
    orbit = [-mp.mpf(1) / 2 + z / a]
    orbit += [f(orbit[0])]
    orbit += [f(orbit[1])]
    assert abs(f(orbit[2]) - orbit[0]) < mp.mpf('1e-70')
    assert orbit[0] < orbit[1] < 0 < orbit[2]
    assert b - 1 < orbit[0] and orbit[2] < b

    df = [1 - a * sigmoid(x) * (1 - sigmoid(x)) for x in orbit]
    multiplier = mp.fprod(df)
    assert 0 < multiplier < 1

    # Exact parameter derivative: differentiate f^3 in b with x fixed.
    partial_b_f3 = 1 + df[2] * (1 + df[1])
    dx_db = partial_b_f3 / (1 - multiplier)
    z_limit = mp.asinh(3 * sigma / 2)
    slope_model = 3 / (2 * a * q * mp.cosh(z_limit))
    multiplier_model = 2 * a * q * mp.cosh(z_limit)

    # Exact rescaled-return Jacobian relation from the chain rule.
    assert mp.almosteq(mp.diff(h, z), (multiplier - 1) / (a * q),
                       rel_eps=mp.mpf('1e-65'), abs_eps=mp.mpf('1e-65'))
    # Convergence checks at finite, moderately large a.
    assert abs((1 - multiplier) / multiplier_model - 1) < mp.mpf('0.02')
    assert abs(dx_db / slope_model - 1) < mp.mpf('0.02')
    assert abs(z - z_limit) < 2000 * a * q
    return (float(abs(z - z_limit)), float(dx_db / slope_model),
            float((1 - multiplier) / multiplier_model))


if __name__ == '__main__':
    for a in [72, 96, 120]:
        for sigma in ['-2', '-0.5', '0', '0.5', '2']:
            err, slope_ratio, gap_ratio = diagnose(a, sigma)
            print(f'a={a:3d}, sigma={sigma:>4s}, phase_error={err:.9g}, '
                  f'slope_ratio={slope_ratio:.12f}, gap_ratio={gap_ratio:.12f}')
    print('PASS: 15 period-three residual, tangent, slope, and gap diagnostics')
