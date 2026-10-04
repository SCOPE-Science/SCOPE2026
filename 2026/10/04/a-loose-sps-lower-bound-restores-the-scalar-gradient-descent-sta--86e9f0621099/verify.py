import math


def sps_step(a, c, alpha, x):
    if x == 0.0:
        return 0.0
    g = a * x
    f = 0.5 * a * x * x
    tau = min(alpha, (f + c) / (g * g))
    return x - tau * g


def delta_sps(a, c, alpha, x):
    if x == 0.0:
        return 0.0
    g = a * x
    f = 0.5 * a * x * x
    tau = min(alpha, (f + c) / (g * g))
    return tau * (1.0 - tau / (2.0 * alpha)) * g * g


def normalized_map(q, y):
    if y == 0.0:
        return 0.0
    if q <= 0.5 + 1.0 / (y * y):
        return (1.0 - q) * y
    return 0.5 * y - 1.0 / y


def close(a, b, tol=5e-12):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def main():
    a = 3.0
    c = 5.0

    # Original update and normalized map agree.
    for q in (0.2, 0.8, 1.7, 2.0, 3.5):
        alpha = q / a
        for y in (-7.0, -1.1, -0.4, 0.4, 1.1, 7.0):
            x = y * math.sqrt(c / a)
            xp = sps_step(a, c, alpha, x)
            yp = xp * math.sqrt(a / c)
            assert close(yp, normalized_map(q, y))

    # Exact cycle and stability-index formula.
    xstar = math.sqrt(2.0 * c / (3.0 * a))
    for q in (2.0, 2.5, 10.0):
        alpha = q / a
        x1 = sps_step(a, c, alpha, xstar)
        x2 = sps_step(a, c, alpha, x1)
        assert close(x1, -xstar)
        assert close(x2, xstar)
        expected_delta = 4.0 * c / 3.0 * (1.0 - 1.0 / q)
        assert close(delta_sps(a, c, alpha, xstar), expected_delta)
        assert close(0.5 * a * xstar * xstar, c / 3.0)

    # Representative subcritical trajectories converge.
    for q in (0.1, 0.75, 1.2, 1.9, 1.99):
        alpha = q / a
        for x0 in (-1e4, -7.0, -0.1, 0.1, 7.0, 1e4):
            x = x0
            for _ in range(20000):
                if abs(x) < 1e-150:
                    break
                x = sps_step(a, c, alpha, x)
            assert abs(x) < 1e-70 or abs(x) < 1e-10 * max(1.0, abs(x0))

    # Algebraic branch boundary used in the proof.
    u = 2.0 / 3.0
    assert close(3.0 * u * u + 4.0 * u - 4.0, 0.0)

    print('VERIFY_OK')


if __name__ == '__main__':
    main()
