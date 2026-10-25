"""Finite checks for differential Hilbert weighted-Bergman matrix identities.

Only verifies finite moments and sample asymptotic trends; it is not an
infinite-dimensional proof. Requires Python 3 standard library only.
"""
import math


def weight(n, gamma):
    return math.exp(math.lgamma(gamma + 2) + math.lgamma(n + 1) - math.lgamma(n + gamma + 2))


def entry_squared(n, k, alpha, beta):
    return ((n + 1) / (n + k + 1)) ** 2 * weight(n, beta) / weight(k, alpha)


def phi(lam):
    return -math.expm1(-lam) / lam if lam != 0 else 1.0


def hs_square(N, alpha, lam):
    beta = alpha + 2 + lam / math.log(N)
    ws = [weight(k, alpha) for k in range(N + 1)]
    out = [weight(n, beta) for n in range(N + 1)]
    total = 0.0
    for n in range(N + 1):
        rowfactor = (n + 1) ** 2 * out[n]
        total += rowfactor * sum(1.0 / (ws[k] * (n + k + 1) ** 2) for k in range(N + 1))
    return total


def main():
    for g in [-0.75, -0.5, 0.25, 2.0]:
        for n in range(11):
            w_direct = (g + 1) * math.gamma(n + 1) * math.gamma(g + 1) / math.gamma(n + g + 2)
            assert math.isclose(weight(n, g), w_direct, rel_tol=1e-12)
    for alpha in [-0.75, -0.5, -0.2]:
        for n in range(8):
            for k in range(8):
                beta = alpha + 2.15
                coeff = (n + 1) / (n + k + 1)
                direct = coeff * coeff * weight(n, beta) / weight(k, alpha)
                assert math.isclose(entry_squared(n, k, alpha, beta), direct, rel_tol=1e-12)
        beta_integral = math.gamma(alpha + 2) * math.gamma(-alpha)
        assert beta_integral > 0
        constant = math.gamma(alpha + 4) * math.gamma(-alpha)
        assert math.isclose(constant, (alpha + 3) * (alpha + 2) * beta_integral)
    # A finite comparison: the absolute cutoff correction is negative and
    # grows much more slowly than the logarithmic leading term.
    alpha = -0.5
    L = math.log
    C = math.gamma(alpha + 4) * math.gamma(-alpha)
    for lam in [-1.0, 0.0, 1.0]:
        values = [hs_square(N, alpha, lam) for N in (60, 180, 450)]
        leading = [C * L(N) * phi(lam) for N in (60, 180, 450)]
        for v, a in zip(values, leading):
            assert v > 0 and math.isfinite(v)
            assert 0.1 < v / a < 1.5
        assert values[0] < values[1] < values[2]
    print("CHECK_OK: exact Bergman moments, gamma/beta constants, finite critical-window trends")


if __name__ == "__main__":
    main()
