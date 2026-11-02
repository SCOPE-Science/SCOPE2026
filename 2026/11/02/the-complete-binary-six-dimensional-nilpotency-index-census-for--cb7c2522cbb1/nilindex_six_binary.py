#!/usr/bin/env python3
"""Exact finite census of nilpotency indices for six-dimensional binary evolution algebras.

Enumerates every strictly upper triangular 6-by-6 structure matrix over GF(2).
The index is the least k for which E^k=0, with E^1=E and
E^k=sum(E^i E^(k-i): 1 <= i < k). No third-party dependencies.
"""
from collections import Counter
from hashlib import sha256

N = 6
MAX_INDEX = (1 << (N - 1)) + 1
EXPECTED = {
    2: 1, 3: 1329, 4: 574, 5: 9760, 6: 352, 7: 1584,
    8: 96, 9: 11648, 10: 64, 11: 192, 13: 512, 17: 5632, 33: 1024,
}


def matrix_from_mask(mask):
    """Coefficients ordered (0,1),(0,2),...,(0,5),(1,2),...,(4,5)."""
    rows = [0] * N
    bit = 0
    for i in range(N):
        for j in range(i + 1, N):
            if mask & (1 << bit):
                rows[i] |= 1 << j
            bit += 1
    assert bit == 15
    return rows


def multiply_bits(x, y, rows):
    """Evolution-algebra multiplication in GF(2)^6."""
    z = 0
    common = x & y
    while common:
        low = common & -common
        z ^= rows[low.bit_length() - 1]
        common ^= low
    return z


def independent_basis(generators):
    """Basis via highest-set-bit Gaussian elimination."""
    pivots = [0] * N
    for word in generators:
        z = word
        while z:
            lead = z.bit_length() - 1
            if pivots[lead]:
                z ^= pivots[lead]
            else:
                pivots[lead] = z
                break
    return tuple(x for x in pivots if x)


def first_zero_power(rows):
    """Compute all E^k by the defining recursive sum of subspace products."""
    spaces = [(), tuple(1 << j for j in range(N))]
    for k in range(2, MAX_INDEX + 1):
        gens = []
        for i in range(1, k // 2 + 1):
            j = k - i
            if j >= len(spaces):
                continue
            for x in spaces[i]:
                for y in spaces[j]:
                    gens.append(multiply_bits(x, y, rows))
        basis = independent_basis(gens)
        if not basis:
            return k
        spaces.append(basis)
    raise AssertionError('exceeds theoretical upper bound')


def span_via_closure(generators):
    """An independent GF(2) span implementation, using closure under XOR."""
    members = {0}
    for w in generators:
        if w not in members:
            members.update({v ^ w for v in tuple(members)})
    # Derive a basis by retaining generators that enlarge the subgroup.
    # We use a separate, deterministic insertion algorithm.
    B = []
    generated = {0}
    for w in generators:
        if w not in generated:
            B.append(w)
            generated.update({v ^ w for v in tuple(generated)})
    assert generated == members
    return tuple(B)


def second_multiplication(a, b, rows):
    """Compute from all six coordinate products (no bitwise intersection)."""
    vector = 0
    for k in range(N):
        if ((a >> k) % 2) * ((b >> k) % 2):
            vector = vector ^ rows[k]
    return vector


def independent_index(rows):
    """Second exhaustive computation, with a distinct span and product routine."""
    spaces = {1: tuple(1 << j for j in range(N))}
    for degree in range(2, MAX_INDEX + 1):
        images = []
        for a in range(1, degree):
            b = degree - a
            if a not in spaces or b not in spaces:
                continue
            for v in spaces[a]:
                for w in spaces[b]:
                    images.append(second_multiplication(v, w, rows))
        B = span_via_closure(images)
        if len(B) == 0:
            return degree
        spaces[degree] = B
    raise AssertionError('exceeds bound')


def run():
    counts = Counter()
    first_example = {}
    all_indices = bytearray()
    for m in range(1 << 15):
        rows = matrix_from_mask(m)
        a = first_zero_power(rows)
        b = independent_index(rows)
        assert a == b, ('independent methods disagree', m, a, b)
        assert 2 <= a <= MAX_INDEX
        counts[a] += 1
        first_example.setdefault(a, m)
        all_indices.append(a)
    assert dict(counts) == EXPECTED, (dict(counts), EXPECTED)
    assert sum(counts.values()) == 32768
    assert counts[33] == 2 ** 10
    # Maximal nilindex occurs iff all 5 successive superdiagonal entries are 1.
    for m in range(1 << 15):
        rows = matrix_from_mask(m)
        adjacent = all((rows[i] >> (i + 1)) & 1 for i in range(N - 1))
        assert (all_indices[m] == 33) == bool(adjacent)
    print('COUNTS', sorted(counts.items()))
    print('FIRST_MASK_WITNESSES', sorted(first_example.items()))
    print('INDEX_VECTOR_SHA256', sha256(all_indices).hexdigest())
    print('TWO_INDEPENDENT_RECURRENCES_VERIFIED', len(all_indices))
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
