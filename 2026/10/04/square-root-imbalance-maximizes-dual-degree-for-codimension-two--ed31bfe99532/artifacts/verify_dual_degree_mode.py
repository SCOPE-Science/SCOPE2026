#!/usr/bin/env python3
from math import isqrt


def direct_degree(d: int, e: int) -> int:
    x, y = d - 1, e - 1
    return d * e * (x**3 + x**2*y + x*y**2 + y**3)


def factor_degree(q: int, s: int) -> int:
    num = q * (((q + 2)**2 - s**2) * (q**2 + s**2))
    assert num % 8 == 0
    return num // 8


def admissible_s(q: int):
    return list(range(q % 2, q - 1, 2))


def bidegree(q: int, s: int):
    x = (q - s) // 2
    y = (q + s) // 2
    return x + 1, y + 1


def predicted_tie_q(q: int) -> bool:
    # q = 2 k(k+1), k >= 2.
    if q % 2:
        return False
    m = q // 2
    k = (isqrt(1 + 4*m) - 1) // 2
    return k >= 2 and k * (k + 1) == m


comparisons = 0
for q in range(2, 2001):
    vals = []
    for s in admissible_s(q):
        d, e = bidegree(q, s)
        assert d >= 2 and d <= e and d + e - 2 == q and e - d == s
        a = direct_degree(d, e)
        b = factor_degree(q, s)
        assert a == b
        vals.append((a, s, d, e))
        comparisons += 1

    top = max(v[0] for v in vals)
    maxs = [v for v in vals if v[0] == top]
    target = 2 * (q + 1)
    mind = min(abs(s*s - target) for s in admissible_s(q))
    closest = [s for s in admissible_s(q) if abs(s*s - target) == mind]
    assert [v[1] for v in maxs] == closest
    assert (len(maxs) == 2) == predicted_tie_q(q)
    assert len(maxs) in (1, 2)

    if predicted_tie_q(q):
        # Recover k and the two closed-form maximizing bidegrees.
        m = q // 2
        k = (isqrt(1 + 4*m) - 1) // 2
        got = {(v[2], v[3]) for v in maxs}
        expected = {(k*k + 1, (k + 1)**2), (k*k, (k + 1)**2 + 1)}
        assert got == expected

# Hand checks used in the writeup.
assert direct_degree(2, 2) == 16
assert direct_degree(2, 4) == 320
assert direct_degree(3, 3) == 288
q = 12
mx = max(direct_degree(*bidegree(q, s)) for s in admissible_s(q))
assert direct_degree(5, 9) == mx == direct_degree(4, 10)

print(f"VERIFY_OK q=2..2000 admissible_pairs={comparisons} first_tie_q=12")
