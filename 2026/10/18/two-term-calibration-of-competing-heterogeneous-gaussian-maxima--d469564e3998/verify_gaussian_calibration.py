"""Numerical cross-checks for the Gaussian two-group winner expansion.

Requires Python 3, SciPy and NumPy. These checks supplement, rather than
replace, the analytical asymptotic proof in RESULT.md.
"""
import math
from scipy.integrate import quad
from scipy.stats import norm


def coefficients(r, C):
    assert r > 1 and C > 0
    h = (r - 1.0) / 2.0
    A = C * (4.0 * math.pi) ** h / math.sqrt(r)
    F = quad(lambda y: -math.expm1(-A * y ** r) * math.exp(-y), 0, 60,
             epsabs=1e-12)[0]
    H = quad(lambda y: A * y ** r * math.exp(-y - A * y ** r), 0, 60,
             epsabs=1e-12)[0]
    J = quad(lambda y: (A * y ** r * math.log(y) * math.exp(-y - A * y ** r))
             if y else 0., 0, 60, epsabs=1e-12)[0]
    return h, A, F, H, J


def expansion(n, r, C, d, e):
    L = math.log(n)
    h, A, F, H, J = coefficients(r, C)
    return F + ((d - h / 2) * H * math.log(L)
                + (e - (h / 2) * math.log(4 * math.pi)
                   + (r - 1 / r) / 2) * H - h * J) / L


def exact_probability(n, r, C, d, e):
    L = math.log(n)
    h = (r - 1) / 2
    correction = (d * math.log(L) + e) / L
    assert correction > -1
    m = int(math.floor(math.exp(math.log(C) + r * L - h * math.log(L)
                                + math.log1p(correction))))
    assert m >= 1 and n >= 100
    sigma = math.sqrt(r)

    def integrand(y):
        if y <= 0:
            return 0.0
        t = norm.isf(y / n)
        sf = norm.sf(sigma * t)
        win = -math.expm1(m * math.log1p(-sf))
        density = math.exp((n - 1) * math.log1p(-y / n))
        return win * density

    # For n>=100, Y=n*tail(max Z'_i) has P(Y>50)=(1-50/n)^n<=e^-50.
    return quad(integrand, 0, 50, epsabs=2e-12, limit=150)[0], m


def main():
    assertions = 0
    for r in [1.44, 2.0, 4.0]:
        h, A, F, H, J = coefficients(r, 1.0)
        assert 0 < F < 1 and H > 0 and math.isfinite(J)
        assertions += 1
        # Check equivalence to the source paper's Gumbel-integral representation.
        kappa = math.log(A) / r
        source_F = quad(lambda z: math.exp(-z - math.exp(-kappa) * z ** (1/r)),
                        0, 60, epsabs=1e-12)[0]
        assert abs(F - source_F) < 1e-11
        assertions += 1
        # Exact derivative wrt log C equals H.
        epsilon = 1e-4
        _, _, Fp, _, _ = coefficients(r, math.exp(epsilon))
        _, _, Fm, _, _ = coefficients(r, math.exp(-epsilon))
        assert abs((Fp - Fm) / (2 * epsilon) - H) < 2e-8
        assertions += 1
        e_star = h * J / H + (h / 2) * math.log(4 * math.pi) - (r - 1 / r) / 2
        d_star = h / 2
        errors_plain = []
        errors_calibrated = []
        for n in [10**6, 10**12, 10**24, 10**48]:
            p, m = exact_probability(n, r, 1.0, 0.0, 0.0)
            pcal, mcal = exact_probability(n, r, 1.0, d_star, e_star)
            pred = expansion(n, r, 1.0, 0.0, 0.0)
            L = math.log(n)
            bound = 1.5 * (math.log(L)**2) / L**2
            assert abs(p - pred) < bound, (r, n, p, pred, bound)
            assert abs(pcal - F) < bound, (r, n, pcal, F, bound)
            errors_plain.append(abs(p - F))
            errors_calibrated.append(abs(pcal - F))
            assertions += 2
        assert errors_calibrated[-1] < errors_plain[-1]
        assertions += 1
        print('r=',r,'F=',format(F,'.12g'),'H=',format(H,'.12g'),
              'J=',format(J,'.12g'),'d*=',format(d_star,'.12g'),
              'e*=',format(e_star,'.12g'),
              'last uncalibrated deviation=',format(errors_plain[-1],'.5g'),
              'last calibrated deviation=',format(errors_calibrated[-1],'.5g'))
    print('PASS:',assertions,'analytic consistency and finite-n quadrature assertions.')

if __name__ == '__main__':
    main()
