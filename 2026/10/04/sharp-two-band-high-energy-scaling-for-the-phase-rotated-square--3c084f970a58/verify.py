#!/usr/bin/env python3
import math


def q_exact_from_x(n, ell, mu, x):
    N = n * math.pi / ell
    k = N + x / N
    s = math.sin(2.0 * mu)
    c = math.cos(2.0 * mu)
    t = k * ell
    st = math.sin(t)
    ct = math.cos(t)
    A = (
        -s * st * st * (1.0 + k ** 4)
        + s * (1.0 + 3.0 * math.cos(2.0 * t)) * k * k
        + 4.0 * c * st * ct * (k + k ** 3)
    )
    return -A / (2.0 * st * k * (k * k - 1.0))


def limit_x_edges(ell, mu):
    return [
        -2.0 * (1.0 / math.cos(mu) + math.tan(mu)) / ell,
        -2.0 * math.tan(mu / 2.0) / ell,
        2.0 * (1.0 / math.cos(mu) - math.tan(mu)) / ell,
        2.0 / (math.tan(mu / 2.0) * ell),
    ]


def limit_energy_edges(ell, mu):
    return [2.0 * x for x in limit_x_edges(ell, mu)]


def bisect(f, a, b, iterations=100):
    fa = f(a)
    fb = f(b)
    if fa == 0.0:
        return a
    if fb == 0.0:
        return b
    if fa * fb > 0.0:
        raise ValueError("root not bracketed")
    for _ in range(iterations):
        m = 0.5 * (a + b)
        fm = f(m)
        if fa * fm <= 0.0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5 * (a + b)


def exact_energy_edges(n, ell, mu):
    eps = -1.0 if n % 2 else 1.0
    x0s = limit_x_edges(ell, mu)
    q_limit_targets = [-2.0, 2.0, -2.0, 2.0]
    roots = []
    for x0, qlim in zip(x0s, q_limit_targets):
        target = eps * qlim
        width = max(0.1, 0.2 * abs(x0))
        f = lambda x: q_exact_from_x(n, ell, mu, x) - target
        for _ in range(20):
            a = x0 - width
            b = x0 + width
            if x0 < 0.0:
                b = min(b, 0.5 * x0)
            else:
                a = max(a, 0.5 * x0)
            try:
                xr = bisect(f, a, b)
                break
            except ValueError:
                width *= 1.5
        else:
            raise AssertionError("failed to bracket an edge")
        N = n * math.pi / ell
        k = N + xr / N
        roots.append(k * k - N * N)
    return roots


def central_secular_value(n, ell, mu):
    N = n * math.pi / ell
    return 4.0 * math.sin(2.0 * mu) * N * N


def check_case(ell, mu):
    predicted = limit_energy_edges(ell, mu)
    ns = [80, 160, 320]
    max_errors = []
    print("case ell=%.6f mu=%.12f" % (ell, mu))
    print("limit", " ".join("%.12f" % v for v in predicted))
    for n in ns:
        exact = exact_energy_edges(n, ell, mu)
        errors = [abs(a - b) for a, b in zip(exact, predicted)]
        maxerr = max(errors)
        max_errors.append(maxerr)
        assert central_secular_value(n, ell, mu) > 0.0
        assert all(exact[i] < exact[i + 1] for i in range(3))
        print("n=%d max_error=%.12g edges=%s" % (
            n,
            maxerr,
            " ".join("%.12f" % v for v in exact),
        ))
    # Second-order convergence: doubling n should reduce the leading error by about four.
    assert max_errors[1] < 0.30 * max_errors[0]
    assert max_errors[2] < 0.30 * max_errors[1]


def main():
    cases = [
        (1.7, 0.3),
        (2.3, math.pi / 4.0),
        (3.1, 1.2),
    ]
    for ell, mu in cases:
        check_case(ell, mu)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
