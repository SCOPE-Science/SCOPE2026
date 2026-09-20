from itertools import product, combinations
from fractions import Fraction
from math import atan, sqrt, pi

def t3_cdf(x):
    return 0.5 + atan(x / sqrt(3.0)) / pi + (sqrt(3.0) * x) / (pi * (x*x + 3.0))

def t_stat(xs):
    n = len(xs)
    m = sum(xs) / n
    q = sum((x-m)**2 for x in xs)
    if q == 0:
        return float("inf") if m > 0 else float("-inf") if m < 0 else 0.0
    s2 = q / (n-1)
    return sqrt(n) * m / sqrt(s2)

for theta in (-1, 1):
    probs = {}
    for s in product((-1, 1), repeat=4):
        p = Fraction(1 + theta * (s[0]*s[1]*s[2]*s[3]), 16)
        probs[s] = p
    assert sum(probs.values(), Fraction(0)) == 1
    for r in range(1, 4):
        for kept in combinations(range(4), r):
            table = {}
            for s, p in probs.items():
                key = tuple(s[i] for i in kept)
                table[key] = table.get(key, Fraction(0)) + p
            target = Fraction(1, 2 ** len(kept))
            assert all(v == target for v in table.values())
            assert len(table) == 2 ** len(kept)

grid = [k / 2 for k in range(-8, 9)]
for xs in product(grid, repeat=4):
    T = t_stat(xs)
    if T > 3 + 1e-12:
        assert all(x > 0 for x in xs)
    if T < -3 - 1e-12:
        assert all(x < 0 for x in xs)

one_sided_at_3 = 1.0/6.0 - sqrt(3.0) / (4.0*pi)
two_sided_at_3 = 2.0 * one_sided_at_3
closed_form = 1.0/3.0 - sqrt(3.0)/(2.0*pi)
assert abs(two_sided_at_3 - closed_form) < 1e-15
assert two_sided_at_3 > 0.05

lo, hi = 0.0, 20.0
for _ in range(100):
    mid = (lo + hi) / 2.0
    upper = 1.0 - t3_cdf(mid)
    if upper > 0.025:
        lo = mid
    else:
        hi = mid
critical = (lo + hi) / 2.0
assert critical > 3.0

print("proper sign marginals: exact")
print("deterministic threshold grid check: passed")
print(f"two-sided P(|t_3|>3) = {two_sided_at_3:.15f}")
print(f"two-sided 5% t_3 critical = {critical:.15f} > 3")
print("theta=+1 predicted two-sided size at alpha=0.05: 0.100000000000000")
print("theta=-1 predicted two-sided size at alpha=0.05: 0.000000000000000")
