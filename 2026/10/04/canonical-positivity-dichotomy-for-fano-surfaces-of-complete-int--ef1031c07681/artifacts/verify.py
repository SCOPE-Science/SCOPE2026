from itertools import combinations_with_replacement
from math import comb

def expected_r(k, ds):
    q = k + 1
    total = sum(comb(d + k, k) for d in ds)
    if (total + 2) % q:
        return None
    return k + (total + 2) // q

def B_value(k, r, ds):
    return sum(comb(d + k, k + 1) for d in ds) - r - 1

checked = 0
zeros = []

for k in range(1, 11):
    for m in range(1, 7):
        for ds in combinations_with_replacement(range(2, 13), m):
            r = expected_r(k, ds)
            if r is None:
                continue
            if r < 2 * k + m:
                continue
            delta = (k + 1) * (r - k) - sum(comb(d + k, k) for d in ds)
            assert delta == 2
            B = B_value(k, r, ds)
            assert B >= 0, (k, r, ds, B)
            if B == 0:
                zeros.append((k, r, ds))
            checked += 1

assert zeros == [(1, 5, (2, 2))]

# Symbolic inequalities used in the proof.
for q in range(2, 500):
    # m >= 3, all degrees at least 2.
    assert 3 * q * (q + 1) > 2 * (q * q + 2)

    # m = 2.
    assert q * (q + 1) >= q * q + 2
    assert (q * (q + 1) == q * q + 2) == (q == 2)

    # m = 1, degree at least 3.
    assert q * (q + 1) * (q + 2) > 3 * (q * q + 2)

print("VERIFY_OK", checked, zeros)
