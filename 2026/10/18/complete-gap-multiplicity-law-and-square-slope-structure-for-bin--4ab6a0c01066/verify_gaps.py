#!/usr/bin/env python3
"""Exact independent checks for the binary inclusion-exclusion gap histogram.

No third-party modules are required. The direct route enumerates polynomial
coefficients through the finite generating-function product; the predicted
route uses only circular interval arithmetic and floor sums.
"""
from collections import Counter
from math import gcd


def predicted(a, b):
    assert 2 <= a < b and gcd(a, b) == 1
    h, r = divmod(b, a)
    u = pow(r, -1, a)
    ans = Counter()
    for D in range(2, a + 1):
        if D == a:
            delta, H = 0, 1
        else:
            positions = sorted(u * j % a for j in range(D + 1))
            t = (u * D) % a
            if t == positions[1]:
                delta, H = t, a - positions[-1]
                assert H == positions[2] - t
            elif t == positions[-1]:
                delta, H = a - t, t - positions[-2]
                assert H == positions[1]
            else:
                continue
        assert H >= 1 and delta + 2 * H - 2 <= a - 2
        extra = sum(
            ((delta + j + H) * r // a) - ((delta + j) * r // a)
            for j in range(H)
        )
        ans[D - 1] = 2 * (h * H * H + extra)
    return ans


def directly_from_polynomial(a, b):
    """Compute Q_ab via its finite generating function, not Apéry thresholds."""
    degree = (a - 1) * (b - 1)
    representation = [0] * (degree + 1)
    for x in range(0, degree + 1, a):
        for n in range(x, degree + 1, b):
            representation[n] += 1
    assert max(representation) == 1
    coeff = [representation[0]]
    coeff.extend(representation[n] - representation[n - 1]
                 for n in range(1, degree + 1))
    assert coeff[0] == coeff[-1] == 1
    assert all(c in (-1, 0, 1) for c in coeff)
    assert coeff == coeff[::-1]
    positions = [n for n, c in enumerate(coeff) if c]
    return Counter(y - x for x, y in zip(positions, positions[1:]))


def check_triangular_insertion():
    """Independently count arcs in nested residue sets for the critical lemma."""
    for a in range(2, 28):
        for r in range(1, a):
            if gcd(a, r) != 1:
                continue
            u = pow(r, -1, a)
            for D in range(2, a + 1):
                if D == a:
                    delta, width = 0, 1
                else:
                    P = sorted((u * v) % a for v in range(D + 1))
                    t = (u * D) % a
                    if t == P[1]:
                        delta, width = t, a - P[-1]
                    elif t == P[-1]:
                        delta, width = a - t, t - P[-2]
                    else:
                        delta, width = 0, 0
                for j in range(a - 1):
                    points = sorted((i * r) % a for i in range(j + 1))
                    cyclic_gaps = [v - w for w, v in zip(points, points[1:])]
                    cyclic_gaps.append(a + points[0] - points[-1])
                    observed = cyclic_gaps.count(D)
                    expected = sum(1 for x in range(width)
                                   for y in range(width)
                                   if j == delta + x + y)
                    assert observed == expected, (a, r, D, j, observed, expected)


def run():
    check_triangular_insertion()
    checked = 0
    for a in range(2, 55):
        for b in range(a + 1, 125):
            if gcd(a, b) != 1:
                continue
            lhs = predicted(a, b)
            rhs = directly_from_polynomial(a, b)
            assert lhs == rhs, (a, b, lhs, rhs)
            checked += 1
    # A larger, different quotient and residue range.
    for a in (61, 67, 71, 79, 83, 97, 101, 127):
        for r in (1, 2, 3, a // 2, a - 3, a - 2, a - 1):
            if 0 < r < a and gcd(a, r) == 1:
                for h in (1, 3, 7):
                    b = h * a + r
                    assert predicted(a, b) == directly_from_polynomial(a, b)
                    checked += 1
    for a, b, expected in (
        (3, 5, {1: 4, 2: 2}),
        (5, 7, {1: 12, 2: 2, 4: 2}),
        (5, 11, {1: 4, 2: 4, 3: 4, 4: 4}),
        (7, 17, {1: 20, 2: 20, 3: 4, 6: 4}),
    ):
        assert predicted(a, b) == expected
    print(f"VERIFIED: {checked} coprime pairs; exact coefficient gaps and square-slope formula")


if __name__ == '__main__':
    run()
