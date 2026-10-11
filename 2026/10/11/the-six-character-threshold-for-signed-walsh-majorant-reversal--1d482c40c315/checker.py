"""Exact finite verification of Walsh sign-majorant classification."""
from itertools import combinations
from math import comb


def affine_rank(support):
    pivot = {}
    for u in support[1:]:
        z = u ^ support[0]
        while z:
            b = z.bit_length() - 1
            if b in pivot:
                z ^= pivot[b]
            else:
                pivot[b] = z
                break
    return len(pivot)


def moment_numerator(d, support, signs):
    """Sum of absolute cubes over the group, entirely in integers."""
    total = 0
    for x in range(1 << d):
        value = sum(s * (-1 if (x & k).bit_count() % 2 else 1)
                    for k, s in zip(support, signs))
        total += abs(value) ** 3
    return total


def verify():
    # All ternary coefficient vectors on the three-dimensional Boolean cube.
    # For each fixed nonempty support, compare with the positive idempotent.
    small_supports = 0
    for support_size in range(1, 9):
        for support in combinations(range(8), support_size):
            positive = moment_numerator(3, support, (1,) * support_size)
            for negmask in range(1 << support_size):
                signs = tuple(-1 if negmask >> j & 1 else 1
                              for j in range(support_size))
                assert moment_numerator(3, support, signs) <= positive
            small_supports += 1
    assert small_supports == 255

    # Exhaust every support of size <=5 containing frequency zero in F_2^4.
    # Translation invariance reduces an arbitrary support to one containing 0.
    low_cases = 0
    for k in range(1, 6):
        for tail in combinations(range(1, 16), k - 1):
            support = (0,) + tail
            positive = moment_numerator(4, support, (1,) * k)
            for mask in range(1 << (k - 1)):
                signs = (1,) + tuple(-1 if mask >> j & 1 else 1
                                      for j in range(k - 1))
                assert moment_numerator(4, support, signs) <= positive
            low_cases += 1
    assert low_cases == sum(comb(15, k - 1) for k in range(1, 6))

    # Six-point supports: the exact iff-criterion, including exact gap 3.
    supports = 0
    violating_supports = 0
    violating_signs = 0
    for tail in combinations(range(1, 16), 5):
        support = (0,) + tail
        positive = moment_numerator(4, support, (1,) * 6)
        six_circuit = affine_rank(support) == 4 and not (
            support[0] ^ support[1] ^ support[2] ^ support[3]
            ^ support[4] ^ support[5])
        saw_violating = False
        for mask in range(1 << 5):
            signs = (1,) + tuple(-1 if mask >> j & 1 else 1
                                  for j in range(5))
            signed = moment_numerator(4, support, signs)
            violation = signed > positive
            assert violation == (six_circuit and mask.bit_count() % 2 == 1)
            if violation:
                assert (positive, signed) == (16 * 21, 16 * 24)
                violating_signs += 1
                saw_violating = True
        if saw_violating:
            violating_supports += 1
        supports += 1
    assert supports == 3003
    assert violating_supports == 168
    assert violating_signs == 2688
    print('PASS: F_2^3: 255 nonempty support masks, all signings')
    print('PASS: F_2^4: %d support masks of sizes 1-5, all signings' % low_cases)
    print('PASS: F_2^4: %d six-support masks, 32 signings each' % supports)
    print('PASS: strict reversal iff affine six-circuit and odd signs')
    print('PASS: 168 support masks and 2688 signed cases; exact M3 = 21 and 24')


if __name__ == '__main__':
    verify()
