"""Exact, dependency-free certificate for a cyclic shift covering of F_2^28.

Coordinates of a binary polynomial are represented by low-to-high bits.
This program verifies every orbit of a nine-dimensional quotient, not a
random sample of the original twenty-eight-dimensional space.
"""

MODULUS = 0x2E7  # (t^3+t+1)^3
FUNCTIONALS = (0x020, 0x1B0, 0x179, 0x0E1)
# (least orbit representative, orbit size, first exponent into the kernel)
ORBIT_CERTIFICATE = (
    (0, 1, 0), (1, 28, 1), (3, 28, 1), (5, 28, 23),
    (7, 28, 6), (9, 28, 21), (11, 14, 10), (13, 28, 4),
    (15, 28, 9), (19, 28, 23), (21, 28, 5), (25, 28, 9),
    (27, 28, 5), (29, 14, 7), (31, 28, 14), (33, 28, 7),
    (35, 28, 16), (37, 28, 10), (49, 14, 12), (65, 28, 0),
    (69, 7, 0), (83, 14, 9),
)


def polynomial_multiply(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
    return result


def polynomial_remainder(a, modulus):
    while a.bit_length() >= modulus.bit_length():
        a ^= modulus << (a.bit_length() - modulus.bit_length())
    return a


def multiply_by_t_mod(s):
    val = s << 1
    if val & (1 << 9):
        val ^= MODULUS
    assert 0 <= val < (1 << 9)
    return val


def vanishes(s):
    return all(((mask & s).bit_count() & 1) == 0 for mask in FUNCTIONALS)


def binary_rank(rows):
    pivots = {}
    for x in rows:
        while x:
            pivot = x.bit_length()
            if pivot in pivots:
                x ^= pivots[pivot]
            else:
                pivots[pivot] = x
                break
    return len(pivots)


def main():
    f = (1 << 3) | (1 << 1) | 1
    assert polynomial_multiply(polynomial_multiply(f, f), f) == MODULUS
    assert polynomial_remainder((1 << 28) | 1, MODULUS) == 0
    assert binary_rank(FUNCTIONALS) == 4

    # Check the induced 28-dimensional row masks independently by reduction.
    residues = [polynomial_remainder(1 << j, MODULUS) for j in range(28)]
    rows28 = tuple(sum((((mask & residue).bit_count() & 1) << j)
                       for j, residue in enumerate(residues))
                   for mask in FUNCTIONALS)
    assert rows28 == (0x0A882A20, 0x0922B9B0, 0x0E90E779, 0x0976F8E1)
    assert binary_rank(rows28) == 4
    assert sum(vanishes(s) for s in range(1 << 9)) == 1 << 5

    # Independent complete orbit partition of all 512 quotient states.
    unseen = set(range(1 << 9))
    observed = []
    while unseen:
        start = min(unseen)
        state = start
        orbit = []
        while state in unseen:
            orbit.append(state)
            unseen.remove(state)
            state = multiply_by_t_mod(state)
        assert state == start
        hit_positions = [j for j, v in enumerate(orbit) if vanishes(v)]
        assert hit_positions
        observed.append((start, len(orbit), hit_positions[0]))
    assert tuple(observed) == ORBIT_CERTIFICATE
    assert len(observed) == 22
    assert sum(length for _, length, _ in observed) == (1 << 9)

    # Verify shift covariance on the 28 standard coordinate vectors.
    for j in range(28):
        assert multiply_by_t_mod(residues[j]) == residues[(j + 1) % 28]

    # A second coverage check tests all states, not just representatives.
    for s in range(1 << 9):
        v = s
        for _ in range(28):
            if vanishes(v):
                break
            v = multiply_by_t_mod(v)
        else:
            raise AssertionError(f'Uncovered quotient state: {s}')
    print('CYCLICALLY_COVERING_28_VERIFY_OK')
    print('orbit_count=22 quotient_states=512 kernel_states=32 rank=4')
    print('row_masks_28=' + ','.join(f'{r:07x}' for r in rows28))


if __name__ == '__main__':
    main()
