from fractions import Fraction
from itertools import product
from math import comb


def raney_count(r, b):
    n = (r + 1) * b + r
    num = r * comb(n, b)
    assert num % n == 0
    return num // n


def formula(d, kappa, r):
    if d < r:
        return Fraction(0, 1)
    m = (d - r) // (r + 1)
    ans = Fraction(0, 1)
    for b in range(m + 1):
        n = (r + 1) * b + r
        ans += Fraction(raney_count(r, b) * (kappa ** b), (kappa + 1) ** n)
    return ans


def brute_probability(d, kappa, r):
    p = Fraction(1, kappa + 1)
    s = Fraction(kappa, kappa + 1)
    ans = Fraction(0, 1)
    for path in product((1, -r), repeat=d):
        total = 0
        hit = False
        for step in path:
            total += step
            if total >= r:
                hit = True
                break
        if hit:
            plus = sum(step == 1 for step in path)
            minus = d - plus
            ans += (p ** plus) * (s ** minus)
    return ans


def direct_first_hit_count(r, b):
    n = (r + 1) * b + r
    target_plus = r * (b + 1)
    count = 0
    for neg_positions in __import__('itertools').combinations(range(n), b):
        neg = set(neg_positions)
        total = 0
        ok = True
        for j in range(n):
            total += -r if j in neg else 1
            if j < n - 1 and total >= r:
                ok = False
                break
        if ok and total == r:
            count += 1
    assert target_plus == n - b
    return count


def smaller_root(kappa, r):
    p = 1.0 / (kappa + 1)
    s = kappa / (kappa + 1)
    def g(x):
        return p + s * (x ** (r + 1)) - x
    x_min = (1.0 / ((r + 1) * s)) ** (1.0 / r)
    lo, hi = 0.0, x_min
    assert g(lo) > 0 and g(hi) < 0
    for _ in range(200):
        mid = (lo + hi) / 2
        if g(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


for r in range(1, 4):
    for b in range(0, 4):
        assert direct_first_hit_count(r, b) == raney_count(r, b)

for kappa, r in [(2, 1), (2, 2), (3, 2), (2, 3)]:
    for d in range(1, 10):
        assert brute_probability(d, kappa, r) == formula(d, kappa, r)
        if d < r:
            assert formula(d, kappa, r) == 0
        if d >= 2 and d not in {(r + 1) * b + r for b in range(20)}:
            assert formula(d, kappa, r) == formula(d - 1, kappa, r)

examples = [(10, 1, 0.1), (5, 2, 0.029179606750063095), (2, 5, 0.004172949295476599)]
for kappa, r, target in examples:
    f = smaller_root(kappa, r)
    val = f ** r
    assert abs(val - target) < 5e-14
    if r == 1:
        assert abs(val - 1.0 / (kappa * r)) < 5e-14
    else:
        assert val < 1.0 / (kappa * r)

print('VERIFY_OK')
