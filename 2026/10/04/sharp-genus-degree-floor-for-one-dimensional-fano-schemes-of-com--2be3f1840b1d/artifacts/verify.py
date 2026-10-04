from itertools import combinations_with_replacement
from math import comb

def expected_n(k, ds):
    q = k + 1
    T = sum(comb(d + k, k) for d in ds)
    if (T + 1) % q:
        return None
    return k + (T + 1) // q

def B_value(k, n, ds):
    return sum(comb(d + k, k + 1) for d in ds) - n - 1

checked = 0
equalities = []

for k in range(1, 13):
    for r in range(1, 7):
        for ds in combinations_with_replacement(range(2, 13), r):
            n = expected_n(k, ds)
            if n is None or n < 4:
                continue
            delta = (k + 1) * (n - k) - sum(comb(d + k, k) for d in ds)
            assert delta == 1
            B = B_value(k, n, ds)
            assert B >= 2, (k, n, ds, B)
            if B == 2:
                equalities.append((k, n, ds))
            checked += 1

assert equalities == [(1, 6, (2, 2, 2))]

# Classical calibration examples from the source.
assert B_value(1, 4, (4,)) == 5
assert 1 + B_value(1, 4, (4,)) * 320 // 2 == 801

assert B_value(1, 5, (2, 3)) == 3
assert 1 + B_value(1, 5, (2, 3)) * 180 // 2 == 271

assert B_value(1, 6, (2, 2, 2)) == 2
assert 1 + B_value(1, 6, (2, 2, 2)) * 128 // 2 == 129

# Symbolic threshold checks used by the proof.
for q in range(2, 100):
    # r >= 3
    assert 3 * q * (q + 1) >= 2 * (q + 1) ** 2
    if q > 2:
        assert 3 * q * (q + 1) > 2 * (q + 1) ** 2

    # r = 2, at least one degree >= 3
    lhs_two = q * (q + 1) * (2 * q + 7)
    rhs_two = 6 * (q + 1) ** 2
    assert lhs_two > rhs_two

for q in range(3, 100):
    lhs_one = q * (q + 1) * (q + 2)
    rhs_one = 3 * (q + 1) ** 2
    assert lhs_one > rhs_one

print("VERIFY_OK", checked, equalities)
