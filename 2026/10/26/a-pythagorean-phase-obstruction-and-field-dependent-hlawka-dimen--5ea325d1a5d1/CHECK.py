"""Independent arithmetic checks for the two-coordinate Hornich--Hlawka witness.

These finite checks corroborate numerical identities; the proof of the universal
claim is analytical and appears in RESULT.md.
"""
from math import isclose


def norm(v, p):
    if p == float("inf"):
        return max(abs(t) for t in v)
    return sum(abs(t) ** p for t in v) ** (1 / p)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def gap(p):
    x, y, z = (1 + 0j, 1 + 0j), (1 + 0j, -1 + 0j), (-1 + 0j, 4j / 3)
    left = norm(x, p) + norm(y, p) + norm(z, p) + norm(add(add(x, y), z), p)
    right = norm(add(x, y), p) + norm(add(y, z), p) + norm(add(x, z), p)
    return left - right


def analytic_gap(p):
    if p == float("inf"):
        return -2 / 3
    return (2 / 3) * (3 * 2 ** (1 / p) + (3 ** p + 4 ** p) ** (1 / p) - 8)


assert 3 * 2 ** (1 / 3) + 91 ** (1 / 3) > 8
assert 3 * 2 ** (1 / 4) + 337 ** (1 / 4) < 8
for p in (2, 3, 3.5, 3.6, 4, 5, 10, 100, float("inf")):
    assert isclose(gap(p), analytic_gap(p), abs_tol=2e-12)
assert gap(3) > 0 and gap(4) < 0
assert gap(float("inf")) < 0
lo, hi = 3.0, 4.0
for _ in range(90):
    mid = (lo + hi) / 2
    if analytic_gap(mid) > 0:
        lo = mid
    else:
        hi = mid
print("root estimate:", (lo + hi) / 2)
print("gap at exponent 4:", gap(4))
print("gap at infinity:", gap(float("inf")))
print("all independent numerical checks passed")
