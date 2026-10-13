"""Exact finite enumeration checks for the terminal reshuffling comparison.

Run with standard Python 3: python verify_rr_terminal.py.
This checker tests finite instances; the accompanying analytic proof covers all dimensions and horizons.
"""
from fractions import Fraction as F
from itertools import product, permutations


def sq(x):
    return x * x


def terminal_moment(n, k, curvature, step, centers, x0, reshuffle):
    """Directly enumerate sample choices, keeping exact rational state moments."""
    paths = list(permutations(range(n))) if reshuffle else list(product(range(n), repeat=n))
    path_count = len(paths)
    p = F(1, path_count)
    dist = {x0: F(1)}
    for _ in range(k):
        new = {}
        for x, mass in dist.items():
            for seq in paths:
                y = x
                for i in seq:
                    y -= step * curvature * (y - centers[i])
                new[y] = new.get(y, F(0)) + p * mass
        dist = new
    return sum(mass * sq(x - sum(centers, F(0)) / n) for x, mass in dist.items())


def exact_formula(n, k, curvature, step, centers, x0, reshuffle):
    mean = sum(centers, F(0)) / n
    variance = sum(sq(c - mean) for c in centers) / n
    t = step * curvature
    q = 1 - t
    s1 = sum((q ** j for j in range(n)), F(0))
    s2 = sum((q ** (2 * j) for j in range(n)), F(0))
    per_epoch = (t * t * variance * (n * s2 - s1 * s1) / (n - 1)
                 if reshuffle else t * t * variance * s2)
    return q ** (2 * n * k) * sq(x0 - mean) + per_epoch * sum((q ** (2 * n * j) for j in range(k)), F(0))


def check():
    tests = 0
    for n, ks in [(2, (1, 2, 3)), (3, (1, 2)), (4, (1,))]:
        centers = tuple(F(2 * j - n + 1, n + 1) for j in range(n))
        for curvature in [F(1), F(3, 2)]:
            for t in [F(1, 5), F(4, 5), F(1), F(5, 4), F(7, 4)]:
                eta = t / curvature
                for k in ks:
                    for rr in [True, False]:
                        x0 = F(1, 3)
                        a = terminal_moment(n, k, curvature, eta, centers, x0, rr)
                        b = exact_formula(n, k, curvature, eta, centers, x0, rr)
                        assert a == b, (n, k, t, rr, a, b)
                        tests += 1
                    # Formula sign compared to the direct two sampling schemes.
                    delta = exact_formula(n, k, curvature, eta, centers, F(1, 3), True) - exact_formula(n, k, curvature, eta, centers, F(1, 3), False)
                    assert (delta == 0 if t == 1 else ((delta < 0) == (t < 1)))
    # Two-curvature counterexample: one mode with q>0 and the other q<0.
    n = 2
    eig = [F(1), F(2)]
    eta = F(4, 5)
    for active in [0, 1]:
        diff = F(0)
        for r, lam in enumerate(eig):
            cs = (F(1), -F(1)) if r == active else (F(0), F(0))
            rr = exact_formula(n, 2, lam, eta, cs, F(1, 5), True)
            iid = exact_formula(n, 2, lam, eta, cs, F(1, 5), False)
            diff += lam * (rr - iid) / 2
        assert diff < 0 if active == 0 else diff > 0
        tests += 1
    # Explicit exact example of reversal with no initial error.
    n = 2
    cs = (F(1), -F(1))
    eta = F(3, 2)
    rr = exact_formula(n, 1, F(1), eta, cs, F(0), True)
    iid = exact_formula(n, 1, F(1), eta, cs, F(0), False)
    assert rr == F(81, 16) and iid == F(45, 16), (rr, iid)
    tests += 1
    print('VERIFY_OK', tests, 'exact-rational cases')


if __name__ == '__main__':
    check()
