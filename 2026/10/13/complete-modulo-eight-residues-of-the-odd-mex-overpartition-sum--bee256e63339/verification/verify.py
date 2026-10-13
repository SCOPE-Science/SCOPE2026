"""Exact small-case verification of the odd-mex overpartition residue law.

No dependencies beyond Python 3. The universal congruence uses an independent
formal-power-series proof provided with the theorem; these tests are finite.
"""
from math import isqrt

N = 400

def formula(n):
    if n == 0:
        return 1
    t = isqrt(n)
    is_square = t * t == n
    twice_square = n % 2 == 0 and isqrt(n // 2) ** 2 == n // 2
    return (2 * (-1 if n % 2 else 1)
            - (2 * (-1 if t % 2 else 1) if is_square else 0)
            + 4 * (isqrt(n - 1) + (n - 1) // 2 + int(twice_square))) % 8


def multiply_free(a, size):
    # Either no part of this size or any positive multiplicity with two
    # choices for overlining the first occurrence.
    b = a[:]
    for copies in range(1, N // size + 1):
        shift = copies * size
        for total in range(shift, N + 1):
            b[total] = (b[total] + 2 * a[total - shift]) % 8
    return b


def multiply_forced(a, size):
    # Must use this size, with two overlining choices.
    b = [0] * (N + 1)
    for copies in range(1, N // size + 1):
        shift = copies * size
        for total in range(shift, N + 1):
            b[total] = (b[total] + 2 * a[total - shift]) % 8
    return b


def direct_mex_series():
    # Reconstruct exact residues by conditioning on the first missing size.
    result = [0] * (N + 1)
    classes = 0
    j = 0
    while j * (2 * j + 1) <= N:
        missing = 2 * j + 1
        a = [1] + [0] * N
        for part in range(1, missing):
            a = multiply_forced(a, part)
        for part in range(missing + 1, N + 1):
            a = multiply_free(a, part)
        for n, c in enumerate(a):
            result[n] = (result[n] + missing * c) % 8
        classes += 1
        j += 1
    return result, classes


def direct_small(n):
    # Enumerate all ordinary partitions and multiply each by its number
    # of overline choices. This does not use generating-function products.
    total = 0
    def visit(remaining, largest, present, distinct):
        nonlocal total
        if remaining == 0:
            k = 1
            while k in present:
                k += 1
            if k % 2:
                total += k * (1 << distinct)
            return
        for part in range(min(largest, remaining), 0, -1):
            visit(remaining - part, part, present | {part},
                  distinct + (part not in present))
    visit(n, n, frozenset(), 0)
    return total


if __name__ == '__main__':
    coeffs, classes = direct_mex_series()
    assert len(coeffs) == N + 1
    for n in range(N + 1):
        assert coeffs[n] == formula(n), (n, coeffs[n], formula(n))
        if n > 0:
            assert (coeffs[n] == 0) == (isqrt(n) ** 2 == n), n
            assert coeffs[n] in (0, 2, 6), (n, coeffs[n])
    for n in range(0, 25):
        assert direct_small(n) % 8 == coeffs[n], (n, direct_small(n), coeffs[n])
    for limit in (100, 200, 400):
        count0 = sum(coeffs[n] == 0 for n in range(1, limit + 1))
        assert count0 == isqrt(limit)
        count2 = sum(coeffs[n] == 2 for n in range(1, limit + 1))
        count6 = sum(coeffs[n] == 6 for n in range(1, limit + 1))
        assert count0 + count2 + count6 == limit
        print('n<=%d: residues 0=%d, 2=%d, 6=%d' % (limit, count0, count2, count6))
    print('VERIFY_OK', 'N='+str(N), 'mex_classes='+str(classes),
          'direct_partitions_through=24')
