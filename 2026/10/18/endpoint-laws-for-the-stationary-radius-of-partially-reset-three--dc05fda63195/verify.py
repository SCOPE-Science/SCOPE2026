"""Independent numerical cross-checks of stationary Fourier coefficients.

These finite precision checks corroborate, but do not prove, the analytic limits.
"""
import math
import numpy as np
from scipy.integrate import quad


def integral(c):
    assert 0 < c < 1
    indices = np.arange(max(100, int(math.ceil(22 / -math.log(c)))), dtype=float)
    powers = np.power(c, 2 * indices)
    def integrand(t):
        return t * t * math.exp(-float(np.log1p(powers * t * t).sum()))
    value, error = quad(integrand, 0, math.inf, epsabs=2e-10, epsrel=2e-10, limit=300)
    assert error < 1e-7
    return value


def coefficient(c):
    return (2 * (2 * c) ** 1.5 / (3 * math.pi)) * integral(c)


def run():
    count = 0
    for c in (0.005, 0.01, 0.02, 0.05, 0.1, 0.25, 0.5, 0.8, 0.9, 0.95, 0.98, 0.99):
        k = coefficient(c)
        assert k > 0 and math.isfinite(k)
        count += 1
    small = [(c, coefficient(c) / ((2 * math.sqrt(2) / 3) * math.sqrt(c)))
             for c in (0.005, 0.01, 0.02)]
    assert 0.95 < small[2][1] < small[1][1] < small[0][1] < 1
    count += 1
    large = [(c, coefficient(c) / ((4 / (3 * math.sqrt(math.pi))) * (1 - c) ** 1.5))
             for c in (0.95, 0.98, 0.99)]
    assert 0.97 < large[0][1] < large[1][1] < large[2][1] < 1
    count += 1
    for c in (0.2, 0.5, 0.8):
        # Correct invariant second moment from its generator.
        second = 3 / (c * (1 - c*c))
        # Sum of Gamma(2,sqrt(2c)) scalar lengths, as in the contrasting formula.
        scalar_second = 1 / (c * (1-c*c)) + 2 / (c * (1-c)**2)
        assert math.isclose(scalar_second - second, 4 / ((1-c)**2*(1+c)), rel_tol=1e-12)
        count += 1
        # Covariance of an independent vector-increment series.
        finite = sum(3 / c * c**(2*j) for j in range(100))
        assert math.isclose(finite, second, rel_tol=1e-12)
        count += 1
    c=0.5
    xi=1.3
    direct=math.prod(1/(1+(c**(2*j)*xi*xi/(2*c))) for j in range(100))
    log_form=math.exp(-sum(math.log1p(c**(2*j)*xi*xi/(2*c)) for j in range(100)))
    assert math.isclose(direct,log_form,rel_tol=1e-12)
    count += 1
    print(f"PASS: {count} numerical consistency assertions")
    print("K(0.5)=", coefficient(0.5))


if __name__ == '__main__':
    run()
