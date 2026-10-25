#!/usr/bin/env python3
"""Independent finite checks for two-surplus binary de Bruijn circles."""
from collections import Counter, defaultdict
from fractions import Fraction


def count_necklaces(k):
    n = (1 << k) + 2
    groups = defaultdict(set)
    for bits in range(1 << n):
        word = tuple((bits >> i) & 1 for i in range(n))
        frequencies = Counter(tuple(word[(i + j) % n] for j in range(k)) for i in range(n))
        if len(frequencies) != (1 << k):
            continue
        extra = tuple(sorted(mer for mer, count in frequencies.items() for _ in range(count - 1)))
        representative = min(word[i:] + word[:i] for i in range(n))
        groups[extra].add(representative)
    return {tuple(''.join(map(str, mer)) for mer in extra): len(words)
            for extra, words in groups.items()}


def determinant(matrix):
    n = len(matrix)
    a = [row[:] for row in matrix]
    denom = 1
    sign = 1
    for j in range(n - 1):
        if a[j][j] == 0:
            swap = next((r for r in range(j + 1, n) if a[r][j] != 0), None)
            if swap is None:
                return 0
            a[j], a[swap] = a[swap], a[j]
            sign = -sign
        pivot = a[j][j]
        for i in range(j + 1, n):
            for h in range(j + 1, n):
                value = a[i][h] * pivot - a[i][j] * a[j][h]
                assert value % denom == 0
                a[i][h] = value // denom
            a[i][j] = 0
        denom = pivot
    return sign * a[-1][-1]


def tree_ratio(k):
    n = 1 << (k - 1)
    lap = [[0] * n for _ in range(n)]
    for u in range(n):
        for bit in (0, 1):
            v = ((u << 1) & (n - 1)) | bit
            lap[u][u] += 1
            lap[u][v] -= 1
    alternating = sum((i % 2) << (k - 2 - i) for i in range(k - 1))
    other = alternating ^ (n - 1)
    aug = [row[:] for row in lap]
    aug[alternating][alternating] += 1
    aug[other][other] += 1
    aug[alternating][other] -= 1
    aug[other][alternating] -= 1
    original = determinant([r[:-1] for r in lap[:-1]])
    changed = determinant([r[:-1] for r in aug[:-1]])
    return Fraction(changed, original)


def predicted(k):
    baseline = 1 << ((1 << (k - 1)) - k)
    ratio = Fraction(5, 3) + Fraction((-1) ** k, 3 * (1 << (k - 2)))
    alt = baseline * ratio
    assert alt.denominator == 1
    zero = '0' * k
    one = '1' * k
    a = ''.join('01'[i % 2] for i in range(k))
    b = ''.join('10'[i % 2] for i in range(k))
    return {(zero, zero): baseline, (zero, one): baseline,
            (one, one): baseline, tuple(sorted((a, b))): int(alt)}


def main():
    for k in (2, 3, 4):
        actual = count_necklaces(k)
        expected = predicted(k)
        assert actual == expected, (k, actual, expected)
        print('EXHAUSTIVE', k, len(actual), sum(actual.values()), 'OK')
    for k in range(2, 8):
        computed = tree_ratio(k)
        expected = Fraction(5, 3) + Fraction((-1) ** k, 3 * (1 << (k - 2)))
        assert computed == expected, (k, computed, expected)
        print('MATRIX_TREE', k, str(computed), 'OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
