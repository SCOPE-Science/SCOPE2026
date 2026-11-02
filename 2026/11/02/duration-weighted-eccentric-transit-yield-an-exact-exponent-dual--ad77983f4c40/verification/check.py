"""Independent numerical checks for phase-integrated eccentric-transit yield.

Run with Python 3 standard library: python check.py
The analytic proof, not these finite evaluations, establishes the theorem.
"""
import math

PI = math.pi


def phase_moment(e, s, n=32768):
    """Midpoint integration on a uniform periodic phase grid."""
    assert 0 <= e < 1 and n > 0
    return math.fsum((1 + e * math.sin(2 * PI * (j + .5) / n)) ** s
                     for j in range(n)) / n


def yield_factor(e, alpha):
    d = 1 - e * e
    return d ** (alpha / 2 - 1) * phase_moment(e, 1 - alpha)


def direct_inclination_aggregate(e, alpha, nw=512, nb=256):
    """Independent two-dimensional quadrature of transit probability times duration power.

    Geometrical transit probability has a common small factor rho which cancels.
    Conditional normalized impact parameter b is uniform on [0,1].
    """
    d = 1 - e * e
    numerator = 0.0
    denominator = 0.0
    for k in range(nw):
        phase = 2 * PI * (k + .5) / nw
        x = 1 + e * math.sin(phase)
        for j in range(nb):
            b = (j + .5) / nb
            t0 = math.sqrt(1 - b * b)
            denominator += t0 ** alpha
            numerator += x / d * (t0 * math.sqrt(d) / x) ** alpha
    return numerator / denominator


def main():
    checks = 0
    for e in (0.1, 0.5, 0.85, 0.95):
        d = 1 - e * e
        for alpha in (0, 0.25, 0.5, 1, 1.25, 1.5, 1.75, 2, 2.5, 2.75, 3):
            y = yield_factor(e, alpha)
            z = yield_factor(e, 3 - alpha)
            assert abs(y - z) < 3e-11 * max(1, abs(y), abs(z)), (e, alpha, y, z)
            checks += 1
        assert abs(yield_factor(e, 0) - d ** -1) < 1e-11
        assert abs(yield_factor(e, 1) - d ** -0.5) < 1e-11
        assert abs(yield_factor(e, 2) - d ** -0.5) < 1e-11
        assert abs(yield_factor(e, 3) - d ** -1) < 1e-11
        checks += 4
        for alpha in (0, .5, 1, 2, 2.5, 3):
            assert yield_factor(e, 1.5) < yield_factor(e, alpha)
            checks += 1
        assert yield_factor(e, 1.5) > d ** (-.25)
        checks += 1
    assert abs(yield_factor(.5, 1.5) - 1.133293690137242467) < 2e-11
    checks += 1
    for e, alpha in ((.2, .5), (.5, 1.5), (.6, 2.5)):
        y_direct = direct_inclination_aggregate(e, alpha)
        y_theorem = yield_factor(e, alpha)
        assert abs(y_direct - y_theorem) < 8e-4, (e, alpha, y_direct, y_theorem)
        checks += 1
    print(f"PASS: {checks} numerical consistency assertions; finite checks do not prove identities")
    for e in (0.5, 0.9):
        d = 1 - e * e
        print(f"e={e:.1f}: exact-integral numerical Y_1.5={yield_factor(e,1.5):.15f}; "
              f"mean-duration proxy={d**(-.25):.15f}")


if __name__ == "__main__":
    main()
