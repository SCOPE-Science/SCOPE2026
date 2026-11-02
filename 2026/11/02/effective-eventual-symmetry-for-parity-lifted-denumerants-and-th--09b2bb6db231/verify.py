"""Exact finite checks for parity-lifted denumerant thresholds.

All infinite conclusions require the algebraic arguments in RESULT.md.
Python 3 standard library only; run with `python verify.py`.
"""
from math import gcd


def denumerants(coins, bound):
    out = [0] * (bound + 1)
    out[0] = 1
    for coin in coins:
        for n in range(coin, bound + 1):
            out[n] += out[n - coin]
    return out


def direct_three(a, b, c, n):
    count = 0
    for x in range(n // a + 1):
        for y in range((n - a * x) // b + 1):
            if (n - a * x - b * y) % c == 0:
                count += 1
    return count


def sharp_spectrum():
    a, b, c = 3, 4, 7
    length = a * b * c
    h = denumerants((a, b, c), 500)
    bad = [n for n in range(length) if h[n + 1] < h[n]]
    assert bad == [0, 4, 7, 28], bad
    assert h[29] == 7 and h[30] == 8 and h[31] == 9
    for p, first, holes in [
        (0, 0, [1, 2, 5]),
        (1, 7, [8, 9]),
        (2, 14, []),
        (3, 18, []),
        (4, 21, []),
        (5, 24, []),
        (6, 27, []),
        (7, 28, [29]),
        (8, 31, []),
    ]:
        t = [j for j in range(500) if h[j] > p]
        assert t[0] == first, (p, t[0])
        assert [j for j in range(first, 500) if h[j] <= p] == holes, p
    d = denumerants((6, 7, 8), 1000)
    for p in range(101):
        present = [n for n, v in enumerate(d) if v > p]
        assert present, p
        ell = present[0]
        g = max(n for n, v in enumerate(d) if v <= p)
        genus = sum(1 for v in d if v <= p)
        assert ((2 * genus == ell + g + 1) == (p != 1)), p
    assert (14, 25, 21) == (
        min(n for n, v in enumerate(d) if v > 1),
        max(n for n, v in enumerate(d) if v <= 1),
        sum(v <= 1 for v in d),
    )
    assert (56, 65, 61) == (
        min(n for n, v in enumerate(d) if v > 7),
        max(n for n, v in enumerate(d) if v <= 7),
        sum(v <= 7 for v in d),
    )
    return 101


def samples():
    total = 0
    for a, b, c in [(3, 4, 7), (3, 4, 5), (2, 3, 5), (4, 7, 9), (5, 7, 11)]:
        assert min(a, b, c) >= 2
        assert gcd(a, b) == gcd(a, c) == gcd(b, c) == 1
        L = a * b * c
        h = denumerants((a, b, c), 4 * L + 50)
        A = denumerants((2 * a, 2 * b, c), 2 * L + 3 * c + 10)
        assert (L + a + b + c) % 2 == 0
        shift = (L + a + b + c) // 2
        for t in range(3 * L + 30):
            assert h[t + L] - h[t] == t + shift, (a, b, c, t)
            total += 1
        for t in range(min(L, 2 * L + 3 * c + 10)):
            assert h[t] == direct_three(a, b, c, t), (a, b, c, t)
            total += 1
        for t in range((len(A) - c) // 2):
            assert A[2 * t] == A[2 * t + c] == h[t], (a, b, c, t)
            total += 1
        delta_min = min(h[t + 1] - h[t] for t in range(L))
        J = max(0, 1 - delta_min)
        U = J * L
        P = max([0] + h[:U])
        assert all(h[t + 1] > h[t] for t in range(U, 3 * L + 30))
        for p in range(P, P + 10):
            u = next(t for t, val in enumerate(h) if val > p)
            assert u >= U
            assert all(val <= p for val in h[:u])
            assert all(val > p for val in h[u:])
            total += 1
    return total


if __name__ == '__main__':
    checks = samples()
    sym = sharp_spectrum()
    print(f'VERIFY_OK finite_identities={checks} spectrum_levels={sym} exceptional_level=1')
