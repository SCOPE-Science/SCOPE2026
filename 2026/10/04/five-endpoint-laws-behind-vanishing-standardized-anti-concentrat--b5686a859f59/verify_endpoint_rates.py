import mpmath as mp

mp.mp.dps = 80
YS = [mp.mpf("0.3"), mp.mpf("1"), mp.mpf("2.5")]


def gamma_exact(a, y):
    t = a + y * mp.sqrt(a)
    return mp.gammainc(a, t, mp.inf) / mp.gamma(a)


def gamma_asymptotic(a, y):
    return a * mp.log(1 / a) / 2 - a * (mp.log(y) + mp.euler)


def beta_exact(q, y):
    c = (q + y * mp.sqrt(q / (q + 2))) / (1 + q)
    return 1 - c**q


def beta_asymptotic(q, y):
    return q * mp.log(1 / q) / 2 - q * mp.log(y / mp.sqrt(2))


def pareto_exact(eps, y):
    r = 2 + eps
    return ((r - 1) / (r + y * mp.sqrt(r / eps)))**r


def lognormal_exact(sigma, y):
    z = sigma / 2 + mp.log(1 + y * mp.sqrt(mp.e**(sigma**2) - 1)) / sigma
    return mp.erfc(z / mp.sqrt(2)) / 2


def lognormal_asymptotic(sigma, y):
    return mp.e**(-sigma**2 / 2) / (y * sigma * mp.sqrt(2 * mp.pi))


def weibull_normalized_rate(a, y):
    mean = mp.gamma(1 + 1 / a)
    variance = mp.gamma(1 + 2 / a) - mean**2
    threshold = mean + y * mp.sqrt(variance)
    return a * threshold**a


for y in YS:
    a = mp.mpf("1e-6")
    assert abs(gamma_exact(a, y) / gamma_asymptotic(a, y) - 1) < mp.mpf("0.01")
    q = mp.mpf("1e-6")
    assert abs(beta_exact(q, y) / beta_asymptotic(q, y) - 1) < mp.mpf("0.01")
    eps = mp.mpf("1e-8")
    assert abs(pareto_exact(eps, y) / (eps / (2 * y**2)) - 1) < mp.mpf("0.01")
    sigma = mp.mpf("12")
    assert abs(lognormal_exact(sigma, y) / lognormal_asymptotic(sigma, y) - 1) < mp.mpf("0.02")
    a = mp.mpf("0.005")
    assert abs(weibull_normalized_rate(a, y) / (2 / mp.e) - 1) < mp.mpf("0.02")

print("VERIFY_OK")
