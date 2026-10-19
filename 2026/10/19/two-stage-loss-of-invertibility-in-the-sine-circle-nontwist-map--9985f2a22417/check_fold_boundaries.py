"""Reproduce finite checks for exact fold boundaries of a sine-circle map.

Requires only Python 3 standard library. Numerical checks supplement, but do not
replace, the analytic root-count and asymptotic proofs.
"""
from math import sqrt, pi, sin, cos, asin, isclose


def thresholds(b, omega):
    assert b > 0
    r = abs(omega) / b
    q = sqrt(r * r + 8)
    um = (r - q) / 4
    M = (r - um) * sqrt(1 - um * um)
    up = (r + q) / 4
    small = (up - r) * sqrt(max(0, 1 - up * up)) if r < 1 else 0.0
    a_first = 1 / (4 * pi * b * b * M)
    a_second = 1 / (4 * pi * b * b * small) if r < 1 else float('inf')
    return a_first, a_second, M, small


def derivative(t, a, b, omega):
    return 1 + 4 * pi * a * b * cos(t) * (omega - b * sin(t))


def zeros_by_brackets(a, b, omega, grid=48000):
    """Simple-zero count away from thresholds; sign changes on fine mesh."""
    vals = [derivative(2 * pi * j / grid, a, b, omega) for j in range(grid)]
    count = sum(vals[j] * vals[(j + 1) % grid] < 0 for j in range(grid))
    if min(abs(v) for v in vals) < 1e-7:
        # Choose only strict-phase parameters with a safety gap.
        raise AssertionError('numerical test too close to a derivative zero grid node')
    return count


def predicted_count(a, b, omega):
    f, s, _, _ = thresholds(b, omega)
    if a < f:
        return 0
    if abs(omega) < 1e-14:
        return 4
    if abs(omega) < b and a > s:
        return 4
    return 2


def main():
    tests = 0
    cases = [
        (1.0, 0.0), (1.0, 0.1), (1.0, 0.25), (1.0, 0.5),
        (1.0, 0.75), (1.0, 0.99), (1.0, 1.0), (1.0, 1.5),
        (0.75, 0.2), (2.0, -0.9), (0.5, 0.05)
    ]
    for b, omega in cases:
        a1, a2, M, m = thresholds(b, omega)
        assert a1 > 0
        # At a threshold both the lift derivative and its first phase
        # derivative vanish (the emerging simple zeros form a pair).
        r = abs(omega) / b
        q = sqrt(r * r + 8)
        um = (r - q) / 4
        primary_angle = pi - asin(um) + (pi if omega < 0 else 0)
        assert abs(derivative(primary_angle, a1, b, omega)) < 1e-11
        assert abs(2 * um * um - r * um - 1) < 1e-12
        tests += 2
        if r < 1:
            up = (r + q) / 4
            secondary_angle = asin(up) + (pi if omega < 0 else 0)
            assert abs(derivative(secondary_angle, a2, b, omega)) < 1e-11
            assert abs(2 * up * up - r * up - 1) < 1e-12
            tests += 2
        if 0 < abs(omega) < b:
            assert 0 < m < M and a2 > a1
            for multiplier, expected in [(0.7, 0), (1.3, 2)]:
                a = a1 * multiplier
                if a >= a2:
                    continue
                assert zeros_by_brackets(a, b, omega) == expected
                tests += 1
            assert zeros_by_brackets((a1 + a2) / 2, b, omega) == 2
            tests += 1
            assert zeros_by_brackets(a2 * 1.25, b, omega) == 4
            tests += 1
        else:
            assert zeros_by_brackets(a1 * 0.7, b, omega) == 0
            tests += 1
            assert zeros_by_brackets(a1 * 1.25, b, omega) == (4 if omega == 0 else 2)
            tests += 1
        for t in (0.17, 1.1, 2.85, 4.33):
            a = a1 * 1.17
            x = t / (2 * pi)
            step = 1e-6
            def lift(z):
                return z + a * (1 - (omega - b * sin(2 * pi * z))**2)
            approximation = (lift(x + step) - lift(x - step)) / (2 * step)
            assert isclose(approximation, derivative(t, a, b, omega), abs_tol=2e-9)
            tests += 1
        if abs(omega) < b:
            q = sqrt((abs(omega)/b)**2 + 8)
            r = abs(omega)/b
            uplus = (r+q)/4
            uminus = (r-q)/4
            assert abs(2*uplus*uplus-r*uplus-1)<1e-12
            assert abs(2*uminus*uminus-r*uminus-1)<1e-12
            tests += 2
    # Secondary threshold has a 3/2 power divergence near |Omega|=b.
    b = 1.3
    target = 3*sqrt(6)/(16*pi*b*b)
    for epsilon in [1e-2, 1e-3, 1e-4, 1e-5]:
        a2 = thresholds(b, b*(1-epsilon))[1]
        ratio = a2 * epsilon**1.5
        assert abs(ratio/target-1) < 4*epsilon
        tests += 1
    print(f'PASS: {tests} finite consistency checks')


if __name__ == '__main__':
    main()
