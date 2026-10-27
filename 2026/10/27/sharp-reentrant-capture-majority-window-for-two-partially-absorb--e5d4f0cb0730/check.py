"""Independent direct-resolvent and numerical spot checks for two reactive point sinks.

The analytic inequalities in RESULT.md, not this finite numerical test, prove
its assertions over all positive parameters.
"""
import math


def odds_closed(A, B, t):
    if t == 0:
        return B * (1 + A) / (A * (1 + 2 * B))
    q = math.exp(-t)
    return (B / A) * q * (2 * t + A * (1 - q * q)) / (
        2 * t + B * (1 - q ** 4)
    )


def odds_resolvent(A, B, t):
    """Solve two-sink killed-resolvent system, without using odds_closed."""
    q = math.exp(-t)
    c = 1 / (2 * t)
    m11 = 1 + A * c
    m22 = 1 + B * c
    m12 = B * c * q ** 3
    m21 = A * c * q ** 3
    h1 = c * q
    h2 = c * q * q
    det = m11 * m22 - m12 * m21
    u1 = (h1 * m22 - h2 * m12) / det
    u2 = (m11 * h2 - m21 * h1) / det
    assert det > 0 and u1 > 0 and u2 > 0
    return B * u2 / (A * u1)


def threshold(B, t):
    q = math.exp(-t)
    return 2 * B * t * q / (2 * t + B * (1 - q) * (1 + q ** 3))


def bisect_crossing(A, B, lo, hi):
    f0 = odds_closed(A, B, lo) - 1
    f1 = odds_closed(A, B, hi) - 1
    assert f0 * f1 < 0
    for _ in range(75):
        mid = (lo + hi) / 2
        if (odds_closed(A, B, mid) - 1) * f0 > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def run():
    for A in [0.2, 0.7, 1.1, 3.0, 12.0]:
        for B in [0.1, 0.9, 1.01, 2, 100]:
            for t in [0.02, 0.1, 0.4, 1, 2, 4, 10]:
                x = odds_closed(A, B, t)
                y = odds_resolvent(A, B, t)
                assert math.isclose(x, y, rel_tol=3e-12), (A, B, t, x, y)
                assert (x > 1) == (A < threshold(B, t))
    for B in [0.05, 0.25, 0.5, 0.9, 1.0]:
        assert all(threshold(B, j / 100) < B / (1 + B)
                   for j in range(1, 1001))
    for B in [1.01, 1.05, 1.1, 2, 10, 100]:
        assert max(threshold(B, j / 1000) for j in range(1, 1001)) > B / (1 + B)
    A, B = 11 / 10, 100
    assert odds_closed(A, B, 0) < 1
    assert odds_closed(A, B, math.log(2)) > 1
    assert odds_closed(A, B, 5) < 1
    small_cross = bisect_crossing(A, B, 0, math.log(2))
    large_cross = bisect_crossing(A, B, math.log(2), 5)
    print('Matrix cross-checks: 175/175 exact-model parameter cases matched.')
    print('Witness odds at r=0, t=ln 2 and t=5:',
          odds_closed(A, B, 0), odds_closed(A, B, math.log(2)),
          odds_closed(A, B, 5))
    print('Two witnessed dimensionless crossing roots:',small_cross,large_cross)
    print('Numerical tests do not replace the analytic universal proof.')


if __name__ == '__main__':
    run()
