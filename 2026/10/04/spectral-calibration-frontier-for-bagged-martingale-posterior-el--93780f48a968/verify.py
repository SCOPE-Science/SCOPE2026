import math


def normal_pdf(z):
    return math.exp(-0.5 * z * z) / math.sqrt(2.0 * math.pi)


def normal_cdf(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def simpson(f, a, b, n=20000):
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for k in range(1, n):
        total += (4.0 if k % 2 else 2.0) * f(a + k * h)
    return total * h / 3.0


def cdf_weighted_q(x):
    # Q = Z1^2 + (1/4) Z2^2.
    if x <= 0.0:
        return 0.0
    zmax = 2.0 * math.sqrt(x)
    def integrand(z2):
        rem = x - 0.25 * z2 * z2
        if rem <= 0.0:
            return 0.0
        return normal_pdf(z2) * (2.0 * normal_cdf(math.sqrt(rem)) - 1.0)
    return simpson(integrand, -zmax, zmax)


def quantile_weighted(p):
    lo, hi = 0.0, 20.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if cdf_weighted_q(mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    alpha = 0.05
    q_q = quantile_weighted(1.0 - alpha)
    # Chi-square with two degrees of freedom is exponential with rate 1/2.
    q_chi2 = -2.0 * math.log(alpha)
    tau = q_q / q_chi2
    assert abs(tau - 0.6917708845) < 5e-7, tau
    assert 0.25 < tau < 1.0
    tau_all_contrasts = 1.0
    assert tau < tau_all_contrasts

    # Proportional covariance mismatch: all spectral weights agree.
    rho = 0.5
    a = 1.0 / (1.0 + rho)
    assert abs(a - (2.0 / 3.0)) < 1e-15
    # Then Q = a * chi-square_d, so the exact ellipsoid scale is a,
    # and every contrast has posterior/sampling variance ratio one after scaling.
    assert abs(a * (1.0 + rho) - 1.0) < 1e-15
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
