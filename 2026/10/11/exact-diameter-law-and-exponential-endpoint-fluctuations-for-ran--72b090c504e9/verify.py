"""Independent finite checks for the cross-polytope section diameter formulas.

Only standard Python libraries are required. Finite tests do not establish the
large-dimension asymptotic theorem, whose justification is analytic.
"""
from math import erf, exp, pi, sqrt, isclose
from random import Random

rng = Random(20261010)


def analytic_diameter(absolute_normal):
    a = min(absolute_normal)
    b = max(absolute_normal)
    return 2.0 * sqrt(a * a + b * b) / (a + b)


def geometric_diameter(normal):
    """Find all crossed edges and exhaust all pairwise vertex distances."""
    n = len(normal)
    verts = []
    for i in range(n):
        for j in range(i + 1, n):
            for sign in (-1., 1.):
                p = [0.] * n
                ai, aj = abs(normal[i]), abs(normal[j])
                # The two signed endpoints must have normal coordinates of
                # opposite signs; edge crossing is an affine interpolation.
                p[i] = sign * (1.0 if normal[i] > 0 else -1.0) * aj / (ai + aj)
                p[j] = -sign * (1.0 if normal[j] > 0 else -1.0) * ai / (ai + aj)
                assert abs(sum(p[k] * normal[k] for k in range(n))) < 1e-9
                assert isclose(sum(abs(x) for x in p), 1.0, abs_tol=1e-12)
                verts.append(p)
    diam2 = max(sum((p[k] - q[k]) ** 2 for k in range(n))
                for p in verts for q in verts)
    return sqrt(diam2)


def cdf_integral(n, r, steps=12000):
    """Composite Simpson quadrature on a rigorously tail-controlled interval."""
    assert n >= 2 and 0 <= r <= 1
    upper = 11.0
    delta = upper / steps
    total = 0.0
    for k in range(steps + 1):
        y = k * delta
        h = sqrt(2.0 / pi) * exp(-y*y/2.0)
        H = erf(y / sqrt(2.0))
        Hr = erf(r * y / sqrt(2.0))
        v = n * h * max(0.0, H - Hr) ** (n - 1)
        weight = 1 if k in (0, steps) else (4 if k % 2 else 2)
        total += weight * v
    return total * delta / 3.0


def cdf_simulation(n, r, trials=30000):
    count = 0
    for _ in range(trials):
        a = [abs(rng.gauss(0, 1)) for i in range(n)]
        if min(a) >= r * max(a):
            count += 1
    return count / trials


def run():
    for n in (2, 3, 4, 7):
        for trial in range(16):
            normal = [rng.gauss(0., 1.) for _ in range(n)]
            d1 = geometric_diameter(normal)
            d2 = analytic_diameter([abs(x) for x in normal])
            assert isclose(d1, d2, rel_tol=1e-12, abs_tol=1e-12), (n, d1, d2)
    for n, r in ((2,.25),(3,.35),(4,.4),(8,.16)):
        exact = cdf_integral(n, r)
        approx = cdf_simulation(n, r)
        assert abs(exact - approx) < .02, (n, r, exact, approx)
        print('CDF', n, r, round(exact,8), round(approx,8))
    for n in (2,3,5):
        assert abs(cdf_integral(n,0) - 1.0) < 1e-7
        assert cdf_integral(n,1) == 0.0
    print('CROSSPOLYTOPE_DIAMETER_FINITE_CHECKS_OK')


if __name__ == '__main__':
    run()
