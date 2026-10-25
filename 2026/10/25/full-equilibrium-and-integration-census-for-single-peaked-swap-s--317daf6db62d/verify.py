"""Exact checks of cycle swap equilibria and the integration polynomial.
Run with Python 3, no third-party packages. The finite enumeration is a
consistency check, not an infinite proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb


def binom(a, b):
    return comb(a, b) if a >= 0 and 0 <= b <= a else 0


def is_integrated(colors, i):
    n = len(colors)
    return (colors[(i - 1) % n] != colors[i]
            or colors[(i + 1) % n] != colors[i])


def swap_equilibrium(colors):
    n = len(colors)
    current = [int(is_integrated(colors, i)) for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if colors[i] == colors[j]:
                continue
            swapped = list(colors)
            swapped[i], swapped[j] = swapped[j], swapped[i]
            if (int(is_integrated(swapped, i)) > current[i]
                and int(is_integrated(swapped, j)) > current[j]):
                return False
    return True


def polynomial_mul(A, B):
    result = Counter()
    for a, ca in A.items():
        for b, cb in B.items():
            result[a + b] += ca * cb
    return result


def short_compositions(total, k):
    """Numbers of k positive parts bounded by two, by sum min(part,2)."""
    v = binom(k, total - k)
    return Counter({total: v}) if v else Counter()


def all_compositions(total, k):
    """Numbers of all k positive parts, by sum min(part,2)."""
    poly = Counter()
    if total == k:
        poly[k] = 1
    for u in range(1, min(k, total - k) + 1):
        poly[k + u] = binom(k, u) * binom(total - k - 1, u - 1)
    return poly


def integration_polynomial(n, b):
    r = n - b
    assert 1 <= b <= r and n >= 3
    P = Counter()
    for k in range(1, b + 1):
        Bs, Rs = short_compositions(b, k), short_compositions(r, k)
        Ba, Ra = all_compositions(b, k), all_compositions(r, k)
        add1 = polynomial_mul(Bs, Ra)
        add2 = polynomial_mul(Ba, Rs)
        both = polynomial_mul(Bs, Rs)
        for j in set(add1) | set(add2) | set(both):
            P[j] += Fraction(n, k) * (add1[j] + add2[j] - both[j])
    assert all(v >= 0 and v.denominator == 1 for v in P.values())
    return {j: int(v) for j, v in P.items() if v}


def brute_polynomial(n, b):
    P = Counter()
    for choices in combinations(range(n), b):
        colors = [0] * n
        for j in choices:
            colors[j] = 1
        if swap_equilibrium(colors):
            P[sum(int(is_integrated(colors, i)) for i in range(n))] += 1
    return dict(P)


def exact_count(n, b):
    r = n - b
    return sum((Fraction(n, k) * (
        binom(k, b-k) * binom(r-1, k-1)
        + binom(b-1, k-1) * binom(k, r-k)
        - binom(k, b-k) * binom(k, r-k)))
        for k in range(1, b+1))


def main():
    tested = 0
    profiles = 0
    for n in range(3, 16):
        for b in range(1, n // 2 + 1):
            observed = brute_polynomial(n, b)
            predicted = integration_polynomial(n, b)
            assert observed == predicted, (n, b, observed, predicted)
            assert sum(predicted.values()) == exact_count(n, b)
            target = set(range(b + (b+1)//2 + 1, min(n,3*b) + 1))
            assert set(observed) == target, (n, b, target, observed)
            tested += 1
            profiles += binom(n,b)
    assert exact_count(6,3) == 14
    assert exact_count(8,4) == 46
    print('PASS: %d (n,b) parameters; %d labeled-vertex colorings independently tested' % (tested, profiles))
    print('PASS: exact equilibrium count, complete integration polynomial, contiguous spectrum')


if __name__ == '__main__':
    main()
