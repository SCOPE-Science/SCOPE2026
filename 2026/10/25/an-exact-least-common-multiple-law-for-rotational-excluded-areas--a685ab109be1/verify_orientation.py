"""Independent convex-hull checks for an exact two-regular-polygon excluded-area formula."""
import math
import numpy as np
from scipy.spatial import ConvexHull


def exact_profile(n, m, r, s, theta):
    g = math.gcd(n, m)
    ell = n * m // g
    center = 0.0 if (n // g) % 2 else math.pi / ell
    step = 2.0 * math.pi / ell
    offset = math.pi / n - theta - math.pi - center
    distance = abs((offset + step / 2.0) % step - step / 2.0)
    area_n = n * r * r * math.sin(2.0 * math.pi / n) / 2.0
    area_m = m * s * s * math.sin(2.0 * math.pi / m) / 2.0
    amplitude = (2.0 * g * r * s * math.sin(math.pi / n)
                 * math.sin(math.pi / m) / math.sin(math.pi / ell))
    return area_n + area_m + amplitude * math.cos(distance)


def hull_area(n, m, r, s, theta):
    angle_n = 2.0 * math.pi * np.arange(n) / n
    angle_m = 2.0 * math.pi * np.arange(m) / m + theta + math.pi
    v = r * np.column_stack((np.cos(angle_n), np.sin(angle_n)))
    w = s * np.column_stack((np.cos(angle_m), np.sin(angle_m)))
    points = (v[:, None, :] + w[None, :, :]).reshape(-1, 2)
    return ConvexHull(points).volume


def main():
    rng = np.random.default_rng(20260620)
    pairs = [(3, 3), (3, 4), (4, 4), (3, 5), (3, 6), (4, 6),
             (6, 8), (12, 18), (9, 11), (5, 15), (15, 20),
             (10, 14), (8, 17)]
    max_err = 0.0
    trials = 0
    for n, m in pairs:
        g = math.gcd(n, m)
        ell = n * m // g
        t_star = 0.0 if (n // g) % 2 else math.pi / ell
        theta_max = math.pi / n - math.pi - t_star
        theta_min = theta_max + math.pi / ell
        angles = list(rng.uniform(-2.0 * math.pi, 2.0 * math.pi, size=40))
        angles += [theta_max, theta_min, theta_max + 2.0 * math.pi / ell]
        for theta in angles:
            r, s = 0.7, 1.3
            got = hull_area(n, m, r, s, theta)
            expected = exact_profile(n, m, r, s, theta)
            error = abs(got - expected)
            max_err = max(max_err, error)
            assert error < 3e-12, (n, m, theta, got, expected, error)
            trials += 1
        # Independent trapezoidal orientation mean test over a complete period.
        uniform = np.linspace(theta_max, theta_max + 2 * math.pi / ell,
                              1001)
        mean_integral = np.trapezoid(
            np.array([exact_profile(n, m, .7, 1.3, t) for t in uniform]),
            uniform) / (2 * math.pi / ell)
        an = n * .7**2 * math.sin(2 * math.pi / n) / 2
        am = m * 1.3**2 * math.sin(2 * math.pi / m) / 2
        perimeter_n = 2 * n * .7 * math.sin(math.pi / n)
        perimeter_m = 2 * m * 1.3 * math.sin(math.pi / m)
        assert abs(mean_integral - (an + am + perimeter_n * perimeter_m /
                                    (2 * math.pi))) < 3e-6
    print(f"PASS: {trials} hull area comparisons, maximum absolute error {max_err:.3e}")
    print("PASS: 13 independent uniform-orientation mean comparisons")

if __name__ == '__main__':
    main()
