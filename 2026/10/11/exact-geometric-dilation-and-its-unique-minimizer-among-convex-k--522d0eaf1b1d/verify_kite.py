"""Numerical checks for geometric dilation of convex kite boundaries.

Run with Python 3: python verify_kite.py
The exact universal claims are proved analytically in RESULT.md.
"""
from math import atan, cos, hypot, pi, sin, tan, sqrt, isclose
from random import Random


def closed_formula(p, q, r):
    if p < r:
        p, r = r, p
    s, t = hypot(p, q), hypot(r, q)
    return max(s / q, hypot(q * (s + t), p * t + r * s) / (q * (p + r)))


def piecewise_direct(p, q, r):
    # An independent minimization of all piecewise-affine halving chords.
    s, t = hypot(p, q), hypot(r, q)
    H = s + t
    perimeter_times = [0.0, s, H, H + t, 2 * H]
    vertices = [(0., p), (q, 0.), (0., -r), (-q, 0.), (0., p)]

    def pos(u):
        u = max(0.0, min(2 * H, u))
        for j in range(4):
            if u <= perimeter_times[j + 1] + 1e-13:
                lam = (u - perimeter_times[j]) / (perimeter_times[j + 1] - perimeter_times[j])
                lam = max(0.0, min(1.0, lam))
                return tuple(vertices[j][i] * (1 - lam) + vertices[j + 1][i] * lam for i in (0, 1))
        raise AssertionError('parameter outside boundary')

    marks = sorted({0.0, H} | {z for c in perimeter_times for z in (c, c - H) if 0 <= z <= H})
    mind2 = float('inf')
    for a, b in zip(marks[:-1], marks[1:]):
        pa, qa, pb, qb = pos(a), pos(a + H), pos(b), pos(b + H)
        da = (pa[0] - qa[0], pa[1] - qa[1])
        db = (pb[0] - qb[0], pb[1] - qb[1])
        velocity = ((db[0] - da[0]) / (b - a), (db[1] - da[1]) / (b - a))
        norm2 = velocity[0] ** 2 + velocity[1] ** 2
        candidates = [a, b]
        if norm2 > 0:
            stationary = a - (da[0] * velocity[0] + da[1] * velocity[1]) / norm2
            candidates.append(max(a, min(b, stationary)))
        for u in candidates:
            w = (da[0] + velocity[0] * (u - a), da[1] + velocity[1] * (u - a))
            mind2 = min(mind2, w[0] ** 2 + w[1] ** 2)
    return H / sqrt(mind2)


def optimum_beta(alpha):
    def derivative(beta):
        return .5 * tan((alpha - beta) / 2) - 1 / tan(alpha + beta)
    if derivative(0.) >= 0:
        return 0.0
    lo, hi = 0., alpha
    for _ in range(80):
        mid = (lo + hi) / 2
        if derivative(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def root_parameters():
    def difference(alpha):
        beta = optimum_beta(alpha)
        return 1 / cos(alpha) - 2 * cos((alpha - beta) / 2) / sin(alpha + beta)
    lo, hi = pi / 4, pi / 3
    assert difference(lo) < 0 and difference(hi) > 0
    for _ in range(80):
        mid = (lo + hi) / 2
        if difference(mid) > 0:
            hi = mid
        else:
            lo = mid
    alpha = (lo + hi) / 2
    return alpha, optimum_beta(alpha)


def main():
    rng = Random(417913)
    max_deviation = 0.
    for _ in range(1000):
        p = 10 ** rng.uniform(-3, 3)
        q = 10 ** rng.uniform(-3, 3)
        r = 10 ** rng.uniform(-3, 3)
        exact = closed_formula(p, q, r)
        direct = piecewise_direct(p, q, r)
        deviation = abs(exact - direct) / max(1, abs(exact))
        max_deviation = max(max_deviation, deviation)
        assert isclose(exact, direct, rel_tol=8e-12, abs_tol=8e-12), (p, q, r, exact, direct)
    alpha, beta = root_parameters()
    p, q, r = tan(alpha), 1., tan(beta)
    opt = closed_formula(p, q, r)
    expected = 1 / cos(alpha)
    g = .5 * tan((alpha - beta) / 2) - 1 / tan(alpha + beta)
    assert pi / 4 < alpha < pi / 3 and 0 < beta < alpha
    assert abs(g) < 1e-12 and abs(opt - expected) < 1e-12
    # A finite grid is only a diagnostic, not a global minimization proof.
    for i in range(1, 210):
        a = (pi / 2) * i / 210
        for j in range(1, i + 1):
            b = a * j / i
            trial = max(1 / cos(a), 2 * cos((a - b) / 2) / sin(a + b))
            assert trial + 1e-11 >= opt
    print('VERIFY_OK')
    print('1000 independently minimized halving-chord configurations; max relative discrepancy', max_deviation)
    print('alpha', repr(alpha), 'beta', repr(beta))
    print('p/q', repr(p), 'r/q', repr(r), 'sharp dilation', repr(opt))
    print('grid test 21945 angle pairs (supplementary, non-exhaustive)')


if __name__ == '__main__':
    main()
