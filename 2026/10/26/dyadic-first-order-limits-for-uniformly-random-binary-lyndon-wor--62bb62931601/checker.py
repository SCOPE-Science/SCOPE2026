"""Exact small-size and finite-sampling checks for random binary Lyndon words.

No external dependencies.  The finite computations do not prove asymptotic laws.
"""
from collections import Counter
from itertools import product
import random


def mobius(n):
    factors = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            factors += 1
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors += 1
    return (-1) ** factors


def lyndon_count(n):
    return sum(mobius(d) * (2 ** (n // d)) for d in range(1, n + 1) if n % d == 0) // n


def booth(bits):
    n = len(bits)
    s = bits + bits
    i, j, k = 0, 1, 0
    while i < n and j < n and k < n:
        x, y = s[i + k], s[j + k]
        if x == y:
            k += 1
            continue
        if x > y:
            i += k + 1
        else:
            j += k + 1
        if i == j:
            j += 1
        k = 0
    return min(i, j)


def main():
    total_words = 0
    total_lyndon = 0
    table = []
    for n in range(2, 17):
        count = 0
        histogram = Counter()
        for data in product((0, 1), repeat=n):
            total_words += 1
            seq = bytes(data)
            if booth(seq) != 0 or seq in (seq + seq)[1:-1]:
                continue
            count += 1
            total_lyndon += 1
            assert seq[0] == 0 and seq[-1] == 1
            cyclic = seq + seq
            maximum = max(
                next((t for t in range(n) if cyclic[j + t] == 1), n)
                for j in range(n) if seq[j] == 0 and seq[(j - 1) % n] == 1
            )
            first = next(t for t in range(n) if seq[t] == 1)
            assert first == maximum
            if n >= 5:
                histogram[seq[-4:]] += 1
        assert count == lyndon_count(n), (n, count, lyndon_count(n))
        if n >= 9:
            assert len(histogram) == 8
        if n >= 5:
            table.append((n, count, min(histogram.values()), max(histogram.values())))

    rng = random.Random(2610)
    samples = 15000
    empirical = {}
    for n in (128, 512, 2048):
        counts = Counter()
        prefix_five_zeros = 0
        for _ in range(samples):
            raw = bytes(rng.randrange(2) for _ in range(n))
            i = booth(raw)
            rotated = raw[i:] + raw[:i]
            counts[rotated[-4:]] += 1
            prefix_five_zeros += (rotated[:5] == b'\0' * 5)
        assert set(counts) == {bytes((a, b, c, 1)) for a, b, c in product((0, 1), repeat=3)}
        empirical[n] = {
            'prefix_00000_frequency': round(prefix_five_zeros / samples, 4),
            'min_suffix4_frequency': round(min(counts.values()) / samples, 4),
            'max_suffix4_frequency': round(max(counts.values()) / samples, 4),
        }
    print('LYNDON_EXACT_OK', total_words, total_lyndon, len(table))
    print('TERMINAL_TABLE_LAST4', table[-4:])
    print('SAMPLED_TERMINAL_DISTRIBUTIONS', empirical)


if __name__ == '__main__':
    main()
