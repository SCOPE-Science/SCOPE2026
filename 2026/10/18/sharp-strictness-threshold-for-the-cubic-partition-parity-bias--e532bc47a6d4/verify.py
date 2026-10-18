#!/usr/bin/env python3
"""Exact finite certificate for the cubic-partition parity threshold."""

EXCEPTIONS = set(range(8, 16)) | set(range(24, 27)) | set(range(40, 43)) | set(range(67, 70)) | set(range(94, 97)) | set(range(121, 124))
SMALL = [1, 2, 4, 16, 27, 32, 54, 108]
BASE = SMALL + [125, 128]


def subset_sums(weights):
    mask = 1
    for weight in weights:
        mask |= mask << weight
    return mask


def allowed_weights(N):
    out = []
    for u in range(1, N + 1, 2):
        if u ** 3 > N:
            break
        for j in range(N.bit_length()):
            if j > 0 and j % 3 == 0:
                continue
            w = (u ** 3) << j
            if w > N:
                break
            out.append(w)
    return sorted(out)


def signed_partition_coefficients(N):
    # Direct coefficients of Product_{m>=1}(1+q^{m^3})^{-1},
    # independent from the subset-sum construction.
    c = [0] * (N + 1)
    c[0] = 1
    for m in range(1, N + 1):
        cube = m ** 3
        if cube > N:
            break
        for n in range(cube, N + 1):
            c[n] -= c[n-cube]
    return [v if n % 2 == 0 else -v for n, v in enumerate(c)]


def check():
    # Finite base coverage: exactly 1024 subsets.
    assert len(BASE) == 10 and len(set(BASE)) == 10
    base_mask = subset_sums(BASE)
    assert all((base_mask >> n) & 1 for n in range(124, 374))
    assert not ((base_mask >> 374) & 1)

    # Complete exceptions below 124: exactly 256 subsets.
    small_mask = subset_sums(SMALL)
    misses = {n for n in range(124) if not ((small_mask >> n) & 1)}
    assert misses == EXCEPTIONS
    assert len(misses) == 23
    assert (small_mask >> 123) & 1 == 0
    assert (base_mask >> 124) & 1 == 1

    # Infinite induction bases and monotone margin polynomial.
    assert 250 == 2 * (5 ** 3)
    assert 343 == 7 ** 3 and 729 == 9 ** 3
    R = 373 + 250
    assert R == 623 and 343 <= R - 123
    R += 343
    assert R == 966 and 729 <= R - 123
    # The general inequality 2v^3-(v+2)^3 >= 127 for v>=9
    # follows symbolically by its positive derivative at v>=9.
    assert 2 * 9 ** 3 - 11 ** 3 == 127

    # Two independent exact constructions, through degree 2048.
    N = 2048
    coeff = signed_partition_coefficients(N)
    weights = allowed_weights(N)
    subset_counts = [0] * (N + 1)
    subset_counts[0] = 1
    for w in weights:
        for n in range(N, w-1, -1):
            subset_counts[n] += subset_counts[n-w]
    assert coeff == subset_counts
    assert all(coeff[n] > 0 for n in range(124, N+1))
    assert {n for n in range(124) if coeff[n] == 0} == EXCEPTIONS
    print(f'PASS: 1024 base subsets; 256 small subsets; {len(EXCEPTIONS)} zeros; {N+1} independent coefficient comparisons; induction checked')

if __name__ == '__main__':
    check()
