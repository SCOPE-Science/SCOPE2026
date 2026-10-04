from math import erf, exp, lgamma, log, sqrt


def _betacf(a, b, x):
    max_iter = 300
    eps = 3.0e-14
    fpmin = 1.0e-300
    qab = a + b
    qap = a + 1.0
    qam = a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < fpmin:
        d = fpmin
    d = 1.0 / d
    h = d
    for m in range(1, max_iter + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) <= eps:
            return h
    raise RuntimeError("incomplete-beta continued fraction did not converge")


def betainc(a, b, x):
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    bt = exp(lgamma(a + b) - lgamma(a) - lgamma(b) + a * log(x) + b * log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * _betacf(a, b, x) / a
    return 1.0 - bt * _betacf(b, a, 1.0 - x) / b


def t_cdf(x, nu):
    if x == 0.0:
        return 0.5
    y = nu / (nu + x * x)
    tail = 0.5 * betainc(nu / 2.0, 0.5, y)
    return 1.0 - tail if x > 0 else tail


def normal_cdf(x):
    return 0.5 * (1.0 + erf(x / sqrt(2.0)))


def central_t(z, nu):
    return 2.0 * t_cdf(z, nu) - 1.0


if __name__ == "__main__":
    n = 10
    N = 100
    z = 1.96
    nu_star = min(n - 1, N - 1)
    nu = n + N - 2
    floor = central_t(z, nu_star)
    ceiling = central_t(z, nu)
    nominal = 2.0 * normal_cdf(z) - 1.0
    balance_variance_ratio = N * (N - 1) / (n * (n - 1))
    w = (balance_variance_ratio / N) / (balance_variance_ratio / N + 1.0 / n)
    assert abs(floor - 0.9183555945395834) < 5e-13
    assert abs(ceiling - 0.9474279305425579) < 5e-13
    assert abs(nominal - 0.9500042097035590) < 5e-13
    assert abs(w - (N - 1) / (N + n - 2)) < 1e-15
    assert floor < ceiling < nominal
    print(f"floor={floor:.16f}")
    print(f"ceiling={ceiling:.16f}")
    print(f"nominal={nominal:.16f}")
    print(f"balance_variance_ratio={balance_variance_ratio:.16f}")
    print("VERIFY_OK")
