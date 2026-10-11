"""Numerical diagnostics for the analytic lattice-free ellipse phase theorem.

The infinite-domain proof is in RESULT.md; these checks are supplementary.
Only Python's standard library is used.
"""
import math


def perimeter(a: float, b: float, steps: int = 20000) -> float:
    assert 0 < b <= a and steps % 2 == 0
    h = (math.pi / 2) / steps
    def integrand(k):
        th = k * h
        return math.hypot(a * math.sin(th), b * math.cos(th))
    total = integrand(0) + integrand(steps)
    total += 4 * sum(integrand(j) for j in range(1, steps, 2))
    total += 2 * sum(integrand(j) for j in range(2, steps, 2))
    return 4 * total * h / 3


def dperimeter_da(a: float, b: float, steps: int = 20000) -> float:
    h = (math.pi / 2) / steps
    def integrand(k):
        th = k * h
        s = math.sin(th)
        return a * s * s / math.hypot(a * s, b * math.cos(th))
    total = integrand(0) + integrand(steps)
    total += 4 * sum(integrand(j) for j in range(1, steps, 2))
    total += 2 * sum(integrand(j) for j in range(2, steps, 2))
    return 4 * total * h / 3


def square_lattice_free_axis_ellipse(cx: float, cy: float, a: float, b: float):
    k = math.ceil(abs(cx) + a + 2)
    for x in range(-k, k + 1):
        for y in range(-k, k + 1):
            if ((x - cx) / a) ** 2 + ((y - cy) / b) ** 2 < 1 - 1e-12:
                return False
    return True


def check():
    rho = 1 / math.sqrt(2)
    for b in (0.08, 0.2, 0.49, rho):
        for ratio in (1, 1.0001, 1.02, 1.2, 2, 5, 50):
            a = ratio * b
            p = perimeter(a, b)
            dp = dperimeter_da(a, b)
            assert p >= 4 * a - 1e-9
            assert dp < 4 + 1e-10
            assert p - 4 * a <= (2 * math.pi - 4) * b + 1e-9
            if ratio > 1:
                assert p - 4 * a < (2 * math.pi - 4) * b - 1e-9
            for lam in (4, 4.5, 5.8, 2 * math.pi, 7.0):
                assert p - lam * a <= (2 * math.pi - lam) * b + 1e-9
    assert abs(perimeter(rho, rho) - 2 * math.pi * rho) < 1e-10
    assert square_lattice_free_axis_ellipse(0.5, 0.5, rho, rho)
    for a in (1.0, 5.0, 20.0):
        b = 0.49
        assert square_lattice_free_axis_ellipse(0.0, 0.5, a, b)
        assert perimeter(a, b) >= 4 * a
    print('VERIFY_OK: 28 axis pairs, five parameters, attained square-lattice sharp disk and free-strip ellipses.')


if __name__ == '__main__':
    check()
