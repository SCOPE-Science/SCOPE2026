#!/usr/bin/env python3
"""Standalone coefficient checks for the cyclic-factor doubling theorem.

Binary sequence is indexed from 1, and finite factor enumeration is
complete when the established paperfolding factor count 4*length is met.
No infinite theorem is inferred from these finite checks.
"""

def digits_formula(index):
    assert index >= 1
    odd_part = index // (index & -index)
    return 1 if odd_part % 4 == 1 else 0


def recursive_formula(index):
    assert index >= 1
    if index % 2 == 0:
        return recursive_formula(index // 2)
    return 1 if index % 4 == 1 else 0


def least_rotation(word):
    """Booth minimum rotation with the original length returned."""
    n = len(word)
    double = word + word
    i, j, k = 0, 1, 0
    while i < n and j < n and k < n:
        a = double[i + k]
        b = double[j + k]
        if a == b:
            k += 1
            continue
        if a > b:
            i += k + 1
            if i == j:
                i += 1
        else:
            j += k + 1
            if i == j:
                j += 1
        k = 0
    pos = min(i, j)
    return double[pos:pos + n]


def factors(sequence, size):
    return {sequence[i:i + size] for i in range(len(sequence) - size + 1)}


def necklace_count(factor_set, size):
    for word in factor_set:
        if size <= 12:
            assert least_rotation(word) == min(word[i:] + word[:i] for i in range(size))
    return len({least_rotation(w) for w in factor_set})


def run():
    size = 1 << 15
    a = bytes(digits_formula(i) for i in range(1, size + 1))
    b = bytes(recursive_formula(i) for i in range(1, size + 1))
    assert a == b
    assert not any(a[i:i+4] in (b'\x00\x01\x00\x01', b'\x01\x00\x01\x00')
                   for i in range(size - 3))
    checked = []
    for n in (8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 80, 96, 112, 128):
        lo = factors(a, n)
        hi = factors(a, 2*n)
        # By Allouche (1992), exactly 4*k factors exist for every k>=7.
        # These equalities certify completeness of this finite enumeration.
        assert len(lo) == 4*n, (n,len(lo))
        assert len(hi) == 8*n, (n,len(hi))
        cl = necklace_count(lo, n)
        ch = necklace_count(hi, 2*n)
        assert cl == ch, (n,cl,ch)
        checked.append((n,cl))
    # The threshold really excludes length 4.
    assert necklace_count(factors(a,4),4) == 3
    assert necklace_count(factors(a,8),8) == 4
    assert dict(checked)[12] == 16
    assert dict(checked)[20] == 28
    assert dict(checked)[28] == 40
    print('VERIFY_OK independent_paperfolding_recursion_32768_positions '
          'factor_exhaustiveness_via_4n 20_doubling_pairs_n_8_to_128 '
          'sharp_n4_exception counts_n12_16_n20_28_n28_40')
    for n, val in checked:
        print(f'cyclic_count({n})=cyclic_count({2*n})={val}')

if __name__ == '__main__':
    run()
