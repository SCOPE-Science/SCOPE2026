"""Supplementary numerical checks for continuous-spiral support geometry.

This is not a proof of the infinite-dimensional numerical-range theorem.
Run: python verify_spiral.py
"""
import math

PI = math.pi


def crossing(k):
    assert k > 0.0
    phi = math.atan(k)
    c = 1.0 / math.sqrt(1.0 + k * k)
    def gap(theta):
        return math.cos(theta) - c * math.exp(-k * (theta - phi))
    lo, hi = 1.5 * PI, 2.0 * PI
    assert gap(lo) < 0 < gap(hi)
    for _ in range(90):
        mid = (lo + hi) * 0.5
        if gap(mid) < 0:
            lo = mid
        else:
            hi = mid
    theta = (lo + hi) * 0.5
    return phi, theta, c, c * math.exp(-k * (theta - phi))


def exact_support(k, theta):
    phi = math.atan(k)
    c = 1.0 / math.sqrt(1 + k * k)
    candidate = theta - phi
    if candidate < 0:
        candidate += 2 * PI
    return max(math.cos(theta), c * math.exp(-k * candidate))


def spectral_support_grid(k, theta, samples=40000):
    # Because every extra full turn is suppressed, x in [0,2*pi] suffices.
    return max(math.exp(-k * (2 * PI * j / samples))
               * math.cos((2 * PI * j / samples) - theta)
               for j in range(samples + 1))


def run():
    for k in (0.01, 0.1, 0.5, 1.0, 2.0, 5.0):
        phi, theta_star, c, radius = crossing(k)
        assert phi < theta_star < 2.0 * PI
        assert 1.5 * PI < theta_star < 2.0 * PI
        assert 0.0 < radius < 1.0
        assert abs(math.cos(theta_star) - radius) < 5e-14
        angles = [2.0 * PI * j / 251 for j in range(252)]
        angles.extend([phi, theta_star, (phi + theta_star) / 2])
        for theta in angles:
            formula = exact_support(k, theta)
            direct = spectral_support_grid(k, theta, 4000)
            assert abs(formula - direct) < 3e-5, (k, theta, formula, direct)
        sampled_min = min(exact_support(k, t) for t in angles)
        assert radius <= sampled_min + 1e-12
        assert abs(radius - sampled_min) < 2e-9
        print(f'k={k:.3g}; tangent angle={theta_star:.12g}; radius={radius:.12g}')
    print('PASS: six parameter regimes; support and radius checks')


if __name__ == '__main__':
    run()
