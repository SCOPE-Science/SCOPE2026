"""Reproducible numerical consistency checks for a spectral irradiation model.

Run with Python 3.9 or later. Only the Python standard library is needed.
Finite numerical checks do not substitute for the analytical proof.
"""

import math
import random

ROOT3 = math.sqrt(3.0)


def pq(tau, bands):
    p = math.fsum(j * (lam * lam - 3.0) * math.exp(-lam * tau)
                  for lam, j in bands if lam > ROOT3)
    q = math.fsum(j * (3.0 - lam * lam) * math.exp(-lam * tau)
                  for lam, j in bands if lam < ROOT3)
    return p, q


def t4(tau, s, tint, bands):
    a = .75 * tint**4 * (2.0 / 3.0 + tau)
    b = .75 * s * math.fsum(j * (2.0 / 3.0 + 1.0 / lam
                                   + (lam / 3.0 - 1.0 / lam)
                                   * math.exp(-lam * tau))
                               for lam, j in bands)
    return a + b


def four_d_t4(tau, s, tint, bands):
    p, q = pq(tau, bands)
    return 3.0 * tint**4 + s * (q - p)


def root_if_present(s, tint, bands):
    b = 3.0 * tint**4
    p0, q0 = pq(0.0, bands)
    if s * (p0 - q0) <= b:
        return None
    lo, hi = 0.0, 1.0
    while four_d_t4(hi, s, tint, bands) <= 0.0:
        hi *= 2.0
        if hi > 2.0**30:
            raise AssertionError('root not bracketed')
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if four_d_t4(mid, s, tint, bands) > 0.0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2.0


def near(x, y, *, atol=1e-8, rtol=1e-7):
    return abs(x-y) <= atol + rtol*max(abs(x), abs(y))


def test_derivative():
    rng = random.Random(20261024)
    for _ in range(5000):
        bands = [(rng.uniform(.12, 7.0), rng.uniform(.01, 7.0))
                 for _ in range(rng.randint(1, 9))]
        tau = rng.uniform(0.03, 4.5)
        s = rng.uniform(.1, 8.0)
        tint = rng.uniform(.5, 3.0)
        h = 0.00001
        numerical = 4.0*(t4(tau+h, s, tint, bands)
                         - t4(tau-h, s, tint, bands))/(2.0*h)
        analytic = four_d_t4(tau, s, tint, bands)
        assert near(numerical, analytic, atol=1e-7, rtol=3e-7)
    print('5000 derivative finite-difference comparisons: PASS')


def test_shapes():
    rng = random.Random(19930416)
    count_roots = 0
    for _ in range(3000):
        bands = [(rng.uniform(.08, 6.5), rng.uniform(.1, 4.0))
                 for _ in range(rng.randint(1, 8))]
        tint = rng.uniform(.2, 1.5)
        s = rng.uniform(.1, 10.0)
        rt = root_if_present(s, tint, bands)
        f0 = four_d_t4(0.0, s, tint, bands)
        if rt is None:
            assert f0 >= -1e-9
            assert all(four_d_t4(tau, s, tint, bands)>-1e-9
                       for tau in (0.01, .1, .3, .7, 1, 2, 4, 8, 16))
        else:
            count_roots += 1
            assert f0 < 0
            assert four_d_t4(rt*.5, s, tint, bands) < 0
            assert four_d_t4(rt+1.0, s, tint, bands) > 0
            assert abs(four_d_t4(rt, s, tint, bands))<1e-9
    print('3000 randomized profile classifications: PASS; inversions:',count_roots)


def test_limits():
    # A high-opacity absorption band with or without a transparent band.
    both = [(3.0, 10.0), (1.0, 2.0)]
    pure = [(3.0, 10.0)]
    critical = 3.0 / 56.0
    terminal = math.log(15.0)/2.0
    assert root_if_present(critical, 1.0, both) is None
    assert root_if_present(critical*(1.0-1e-7), 1.0, both) is None
    assert near(root_if_present(1.0, 1.0, both), 0.848000916459738, atol=2e-12)
    assert near(root_if_present(1000.0, 1.0, both), 1.352576932763925, atol=2e-12)
    p = 60.0 * math.exp(-3.0*terminal)
    q = 4.0 * math.exp(-terminal)
    fp = -3.0*p+q
    for s in (1000.0, 1e4, 1e5, 1e6):
        tau = root_if_present(s, 1.0, both)
        assert 0 < tau < terminal
        assert near((terminal-tau)*s, 3.0/(-fp), rtol=.005)
    for s in (1.0, 10, 1000, 1e6):
        tau = root_if_present(s, 1.0, pure)
        assert near(tau, math.log(20.0*s)/3.0, atol=2e-12)
    print('Exact two-band values, saturation and logarithmic limits: PASS')
    print('critical irradiation:', critical)
    print('finite saturation depth:',terminal)
    print('finite depth at irradiation 1:',root_if_present(1.,1.,both))
    print('finite depth at irradiation 1000:',root_if_present(1000.,1.,both))
    print('single absorption band depth at irradiation 1000:',root_if_present(1000.,1.,pure))


def test_two_band_crossover():
    high, low, b = 3.0, 1.0, 3.0
    a, c = 60.0, 4.0
    rng = random.Random(519829)
    for _ in range(1000):
        eps = 10.0**rng.uniform(-6.0, 0.0)
        critical = b/(a-eps*c)
        s = critical * 10.0**rng.uniform(.01, 6.0)
        tau = root_if_present(s, 1.0, [(3.0, 10.0), (1.0, 2.0*eps)])
        assert tau is not None
        tau_inf = math.log(a/(eps*c))/(high-low)
        k = a*math.exp(-high*tau_inf)
        xi = s*k/b
        y = tau_inf-tau
        assert y > 0
        lhs = math.exp(high*y)-math.exp(low*y)
        assert near(lhs, 1.0/xi, rtol=1e-7, atol=1e-8)
    print('1000 exact two-band crossover-identity comparisons: PASS')


if __name__ == '__main__':
    test_derivative()
    test_shapes()
    test_limits()
    test_two_band_crossover()
