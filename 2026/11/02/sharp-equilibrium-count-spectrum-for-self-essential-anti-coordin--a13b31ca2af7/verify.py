"""Reproduce finite checks for the bipartite closed-neighborhood anti-threshold theorem.

Run with Python 3, no dependencies: python verify.py
The proof for arbitrary graph sizes is in RESULT.md; these are finite checks.
"""
from itertools import product
from math import floor


def zero_pairs_from_formula(left, right):
    a, b = len(left), len(right)
    pairs = []
    for i in range(a + 1):
        for j in range(b + 1):
            if (j + 1 not in left and i + 1 not in right
                    and i == sum(t >= j + 2 for t in left)
                    and j == sum(s >= i + 2 for s in right)):
                pairs.append((i, j))
    return pairs


def direct_fixed_points(left, right):
    """Enumerate binary profiles and apply the actual vertex update rule."""
    a, b = len(left), len(right)
    ans = []
    for bits in product((0, 1), repeat=a + b):
        z_left = sum(1 - v for v in bits[:a])
        z_right = sum(1 - v for v in bits[a:])
        updated = tuple(int(z_right + 1 - bits[i] >= left[i])
                        for i in range(a)) + tuple(
            int(z_left + 1 - bits[a + j] >= right[j])
            for j in range(b))
        if updated == bits:
            ans.append((z_left, z_right))
    return sorted(ans)


def construction(a, b, number):
    if number == 0:
        return (1,) * a, (1,) * b
    r = number - 1
    assert 2 * r <= min(a, b)
    L = tuple(t for h in range(1, r + 1) for t in (2 * h, 2 * h))
    R = tuple(t for h in range(1, r + 1) for t in (2 * h, 2 * h))
    return L + (0,) * (a - 2 * r), R + (0,) * (b - 2 * r)


profiles_checked = 0
raw_configs_checked = 0
maxima = {}
for a in range(1, 4):
    for b in range(1, 4):
        maximum = 0
        for L in product(range(b + 2), repeat=a):
            for R in product(range(a + 2), repeat=b):
                expected = zero_pairs_from_formula(L, R)
                actual = direct_fixed_points(L, R)
                if sorted(expected) != actual:
                    raise AssertionError((L, R, expected, actual))
                assert len(expected) <= min(a, b) // 2 + 1
                maximum = max(maximum, len(expected))
                profiles_checked += 1
                raw_configs_checked += 2 ** (a + b)
        maxima[(a, b)] = maximum
        assert maximum == min(a, b) // 2 + 1

constructed = 0
for a in range(1, 16):
    for b in range(1, 16):
        for k in range(min(a, b) // 2 + 2):
            L, R = construction(a, b, k)
            actual = zero_pairs_from_formula(L, R)
            assert len(actual) == k, (a, b, k, actual)
            if k:
                r = k - 1
                assert actual == [(2 * v, 2 * (r - v)) for v in range(r + 1)]
            else:
                assert actual == []
            constructed += 1

print('directly compared threshold assignments:', profiles_checked)
print('binary profiles examined:', raw_configs_checked)
print('spectrum constructions checked:', constructed)
print('exact small maxima:', sorted(maxima.items()))
print('PASS: all finite checks')
