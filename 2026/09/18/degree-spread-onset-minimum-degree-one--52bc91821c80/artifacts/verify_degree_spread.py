"""Finite Erdős--Gallai verification for the degree-sequence constructions in RESULT.md."""

from bisect import bisect_right
from collections import Counter
from math import ceil


def erdos_gallai(seq):
    d = sorted(seq, reverse=True)
    n = len(d)
    if sum(d) % 2 or any(x < 0 or x >= n for x in d):
        return False
    pref = [0]
    for x in d:
        pref.append(pref[-1] + x)
    neg = [-x for x in d]
    for k in range(1, n + 1):
        j = max(k, bisect_right(neg, -k))
        rhs = k * (k - 1) + (j - k) * k + (pref[n] - pref[j])
        if pref[k] > rhs:
            return False
    return True


def window_number_one(seq):
    counts = Counter(seq)
    return max(counts[j] + counts[j + 1] for j in range(max(counts) + 1))


def extremal_sequence(d, n):
    assert d >= 2 and n >= 2 * d + 1 and (n * d) % 2 == 0

    if n < 3 * d:
        a = n - (2 * d - 1)
        seq = list(range(1, 2 * d))
        seq += [d - a + 1 + 2 * j for j in range(a)]
        return seq

    if n == 3 * d:
        seq = []
        for x in range(1, 2 * d, 2):
            seq += [x] * 3
        return seq

    if n < 4 * d - 2:
        a = n - (2 * d - 1)
        seq = list(range(1, 2 * d))
        if a % 2:
            q = (a - 1) // 2
            extra = list(range(d - q, d + q + 1))
        else:
            q = a // 2
            extra = [d - j for j in range(1, q + 1)]
            extra += [d + j for j in range(1, q + 1)]
        seq += extra
        return seq

    s = ceil(n / d)
    b = n - (s - 1) * d
    seq = []
    for x in range(1, 2 * d, 2):
        seq += [x] * (s - 1)
    seq += [d - b + 1 + 2 * j for j in range(b)]
    return seq


def main():
    checked = 0
    for d in range(2, 101):
        for n in range(2 * d + 1, 8 * d + 1):
            if (n * d) % 2:
                continue
            seq = extremal_sequence(d, n)
            assert len(seq) == n
            assert min(seq) == 1
            assert max(seq) == 2 * d - 1
            assert sum(seq) == n * d
            assert window_number_one(seq) == ceil(n / d)
            assert erdos_gallai(seq)
            checked += 1
    print(
        f"verified {checked} admissible pairs: "
        "d=2..100 and 2d+1 <= n <= 8d"
    )


if __name__ == "__main__":
    main()
