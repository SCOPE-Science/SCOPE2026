"""Standalone exact-arithmetic checks for sharp clipping-bias support bound.
Run: python verify.py   (Python 3.9+; standard library only)
The general upper bound and global convergence are analytical proofs, not
certified by these finite checks.
"""
from fractions import Fraction
from random import Random


def signed_weights(m):
    assert m >= 3
    v = [Fraction(0)] + [Fraction((-1) ** (i - 1)) for i in range(1, m)] + [Fraction(0)]
    slopes = [v[i + 1] - v[i] for i in range(m)] + [Fraction(0)]
    w = [slopes[i - 1] - slopes[i] for i in range(1, m + 1)]
    return w, v


def clip(z, cap):
    return max(-cap, min(z, cap))


def make_law(m):
    w, v = signed_weights(m)
    total = sum(map(abs, w))
    return [(i if w[i - 1] > 0 else -i, abs(w[i - 1]) / total) for i in range(1, m + 1)], total, v


def drift(law, x, cap):
    return sum((p * clip(x + z, cap) for z, p in law), Fraction(0))


def root_float(law, cap):
    def d(x):
        return sum(float(p) * min(cap, max(-cap, x + z)) for z, p in law)
    lo, hi = -max(abs(z) for z, _ in law) - cap, max(abs(z) for z, _ in law) + cap
    for _ in range(85):
        mid = (lo + hi) / 2
        if d(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


for m in range(3, 81):
    law, total, v = make_law(m)
    assert total == 4 * m - 5 and total % 2 == 1
    assert len(law) == m and all(p > 0 for _, p in law)
    assert sum((p for _, p in law), Fraction(0)) == 1
    assert sum((z * p for z, p in law), Fraction(0)) == 0
    for i in range(m + 1):
        assert drift(law, Fraction(0), Fraction(i)) == v[i] / total, (m, i)
    for i in range(1, m - 1):
        c = Fraction(2 * i + 1, 2)
        assert drift(law, Fraction(0), c) == 0, (m, i)
        c1 = Fraction(4 * i + 1, 4)
        c2 = Fraction(4 * i + 3, 4)
        left = drift(law, Fraction(0), c1)
        right = drift(law, Fraction(0), c2)
        assert left * right < 0, (m, i)
        if m <= 12:
            assert root_float(law, float(c1)) * float(left) < 0
            assert root_float(law, float(c2)) * float(right) < 0
    assert drift(law, Fraction(0), Fraction(m)) == 0
    assert drift(law, Fraction(0), Fraction(3 * m, 2)) == 0

# The m=3 example: (+1,-2,+3) with probabilities (3,3,1)/7.
law, _, _ = make_law(3)
assert law == [(1, Fraction(3, 7)), (-2, Fraction(3, 7)), (3, Fraction(1, 7))]
assert drift(law, Fraction(0), Fraction(1)) == Fraction(1, 7)
assert drift(law, Fraction(0), Fraction(2)) == Fraction(-1, 7)
assert drift(law, Fraction(0), Fraction(3, 2)) == 0

rng = Random(1337)
for _ in range(2000):
    m = rng.randrange(3, 30)
    law, _, _ = make_law(m)
    c = rng.uniform(0.1, m + 2)
    a, b = sorted((rng.uniform(-m - 2, m + 2), rng.uniform(-m - 2, m + 2)))
    da = sum(float(p) * min(c, max(-c, a + z)) for z, p in law)
    db = sum(float(p) * min(c, max(-c, b + z)) for z, p in law)
    assert 0 <= db - da + 1e-12 <= (b - a) + 1e-12

print('VERIFY_OK exact_family_m=3..80; all_midpoint_zeros; signs; unique_root_diagnostics; random_monotone_lipschitz=2000')
