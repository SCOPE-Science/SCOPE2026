"""Supplementary finite consistency checks for an arithmetic endpoint extremizer theorem.

The theorem's universal assertions are established by the accompanying proof;
these finite checks exercise its arithmetic formulas and examples.
"""
import cmath
import math
import random
from functools import reduce


def root_order(indices):
    assert indices and all(isinstance(n, int) and n > 0 for n in indices)
    n0 = indices[0]
    return reduce(math.gcd, [2 * n0] + [n - n0 for n in indices[1:]])


def extended_gcd(a, b):
    if not b:
        return abs(a), (1 if a > 0 else -1), 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def certificate(indices):
    n0 = indices[0]
    frequencies = sorted({s * n for n in indices for s in (-1, 1)})
    diffs = [m - n0 for m in frequencies if m != n0]
    d = 0
    coefs = []
    for v in diffs:
        g, x, y = extended_gcd(d, v)
        coefs = [x * a for a in coefs] + [y]
        d = g
    assert d == root_order(indices)
    assert sum(a * v for a, v in zip(coefs, diffs)) == d
    return d, diffs, coefs


def mu_hat(thetas, coeffs, k):
    return sum(a * cmath.exp(-1j * k * t) for t, a in zip(thetas, coeffs))


def unit(z):
    return z / abs(z)


def angular_distance(x, y):
    return abs((x - y + math.pi) % (2 * math.pi) - math.pi)


def test_extremizers():
    rng = random.Random(20260927)
    cases = [(1,), (1, 2), (1, 3), (2, 4), (2, 6), (3, 6, 9), (3, 5), (4, 10, 16), (2, 3, 7)]
    assert [root_order(s) for s in cases] == [2, 1, 2, 2, 4, 3, 2, 2, 1]
    for S in cases:
        d, diffs, coeff = certificate(S)
        n0 = S[0]
        for _ in range(15):
            shift = rng.uniform(-math.pi, math.pi)
            phase = cmath.exp(1j * rng.uniform(-math.pi, math.pi))
            masses = [rng.random() for _ in range(d)]
            total = sum(masses)
            masses = [p / total for p in masses]
            angles = [shift + 2 * math.pi * j / d for j in range(d)]
            values = [phase * cmath.exp(1j * n0 * x) * p for x, p in zip(angles, masses)]
            for n in S:
                assert abs(abs(mu_hat(angles, values, n)) - 1) < 1e-12
                assert abs(abs(mu_hat(angles, values, -n)) - 1) < 1e-12
    return len(cases) * 15


def test_quantitative_bound():
    rng = random.Random(200027)
    trials = 0
    for S in [(1,), (1, 2), (1, 3), (2, 6), (3, 6, 9), (4, 10, 16)]:
        d, diffs, bezout = certificate(S)
        B = sum(abs(a) for a in bezout)
        n0 = S[0]
        freqs = sorted({s * n for n in S for s in (-1, 1)})
        for _ in range(30):
            shift = rng.uniform(-math.pi, math.pi)
            phase = cmath.exp(1j * rng.uniform(-math.pi, math.pi))
            masses = [rng.random() for _ in range(d)]
            total = sum(masses)
            masses = [x / total for x in masses]
            angles = [shift + 2 * math.pi * j / d + rng.uniform(-0.03, 0.03) for j in range(d)]
            phases = [phase * cmath.exp(1j * n0 * a) * cmath.exp(1j * rng.uniform(-0.02, 0.02)) for a in angles]
            values = [u * m for u, m in zip(phases, masses)]
            deficit = max(0.0, max(2 - abs(mu_hat(angles, values, n)) - abs(mu_hat(angles, values, -n)) for n in S))
            assert deficit < 0.5
            c = {m:unit(mu_hat(angles, values, m)) for m in freqs}
            lam = [c[n0] * c[n0].conjugate() if diff == 0 else c[n0 + diff] * c[n0].conjugate() for diff in diffs]
            target = math.prod(v ** a for v, a in zip(lam, bezout))
            target_theta = -cmath.phase(target) / d
            coset = [target_theta + 2 * math.pi * j / d for j in range(d)]
            dist_l2 = math.sqrt(sum(m * min(angular_distance(t, e) for e in coset) ** 2 for m, t in zip(masses, angles)))
            phase_l2 = math.sqrt(sum(m * abs(u - c[n0] * cmath.exp(1j * n0 * t)) ** 2 for m, u, t in zip(masses, phases, angles)))
            assert phase_l2 <= math.sqrt(2 * deficit) + 1e-9
            assert dist_l2 <= math.pi * math.sqrt(2) * B / d * math.sqrt(deficit) + 1e-9
            trials += 1
    return trials


def test_sharp_exponent():
    for S in [(1,), (1, 2), (1, 3), (2, 6), (3, 6, 9)]:
        nmax = max(S)
        d = root_order(S)
        for h in (0.01 / nmax, 0.003 / nmax, 0.001 / nmax):
            eps = max(2 - 2 * math.cos(n * h / 2) for n in S)
            assert abs(eps / h**2 - nmax**2 / 4) / (nmax**2 / 4) < 1e-3
            # The best shifted d-coset is centered between the two nearby atoms.
            assert h < math.pi / d
            rms = h / 2
            assert rms / math.sqrt(eps) > 0.9 / nmax
    return 15


if __name__ == '__main__':
    a = test_extremizers()
    b = test_quantitative_bound()
    c = test_sharp_exponent()
    print(f'PASS: {a} exact-support checks, {b} quantitative checks, {c} sharpness checks')
