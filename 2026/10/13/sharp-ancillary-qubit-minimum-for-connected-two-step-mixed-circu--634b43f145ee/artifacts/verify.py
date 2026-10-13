"""Exact-rational-free GF(2) verification of a four-regular circulant rank theorem."""
from math import gcd


def valuation2(a):
    assert a > 0
    i = 0
    while a % 2 == 0:
        a //= 2
        i += 1
    return i


def predicted_kernel(n, a, b):
    assert n % 2 == 0 and 0 < a < b < n
    t, m = valuation2(n), n
    m >>= t
    u, v = b - a, a + b
    h, k = min(1 << t, 1 << valuation2(u)), min(1 << t, 1 << valuation2(v))
    f, g = gcd(m, u), gcd(m, v)
    z = gcd(f, g)
    return (f - z) * h + (g - z) * k + z * min(1 << t, (1 << valuation2(u)) + (1 << valuation2(v)))


def gf2_rank(bits):
    rows = list(bits)
    rank = 0
    n = len(rows)
    for col in range(n):
        pivot = next((i for i in range(rank, n) if (rows[i] >> col) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(rank + 1, n):
            if (rows[i] >> col) & 1:
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def matrix_rows(n, a, b):
    return [sum(1 << ((i + d) % n) for d in (a, -a, b, -b)) for i in range(n)]


def admissible(n, a, b):
    return gcd(n, gcd(a, b)) == 1 and len({a % n, -a % n, b % n, -b % n}) == 4


def check(up_to=72):
    count = 0
    for n in range(6, up_to + 1, 2):
        target = (n - 2) // 4
        mn = n
        for a in range(1, n):
            for b in range(a + 1, n):
                if not admissible(n, a, b):
                    continue
                rows = matrix_rows(n, a, b)
                predicted = n - predicted_kernel(n, a, b)
                actual = gf2_rank(rows)
                assert actual == predicted and actual % 2 == 0, (n, a, b, predicted, actual)
                e = actual // 2
                assert e >= target, (n, a, b, e, target)
                mn = min(mn, e)
                count += 1
        exemplar = (1, n // 2 - 1)
        assert admissible(n, *exemplar)
        assert gf2_rank(matrix_rows(n, *exemplar)) // 2 == target
        assert mn == target, (n, mn, target)
    print(f"VERIFY_OK n=6..{up_to}_even connected_step_pairs={count} exact_GF2_rank_and_cyclic_kernel_agree=true minimum_and_witness=true")


if __name__ == '__main__':
    check()
