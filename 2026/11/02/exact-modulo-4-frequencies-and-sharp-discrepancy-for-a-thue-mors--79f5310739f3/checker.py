"""Finite exact certificate for the modulo-four Thue--Morse Fibonacci law.

Run with Python 3: python checker.py
The 128-dimensional matrices are never approximated or diagonalized numerically.
"""
from fractions import Fraction

SIGNS = (1, -1)
STATES = tuple((u, v) for u in range(4) for v in range(4))
IDENTITY = ((1, 0), (0, 1))

def matrix_for(sign):
    return ((sign % 4, 1), (1, 0))

def matrix_product(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in (0, 1)) % 4
                       for j in (0, 1)) for i in (0, 1))

def matrix_action(a, vector):
    return tuple(sum(a[i][j] * vector[j] for j in (0, 1)) % 4
                 for i in (0, 1))

def initial_vector():
    return {sign: {state: tuple(int(out == (sign * state[0] + state[1]) % 4)
                                for out in range(4))
                   for state in STATES} for sign in SIGNS}

def new_vector(current, products):
    return {sign: {state: tuple(x + y for x, y in zip(
        current[sign][state],
        current[-sign][matrix_action(products[sign], state)]))
                   for state in STATES} for sign in SIGNS}

def flat_vector(current):
    return tuple(current[sign][state][j]
                 for sign in SIGNS for state in STATES for j in range(4))

def run_transfer(levels=24):
    products = {sign: matrix_for(sign) for sign in SIGNS}
    current = initial_vector()
    all_vectors, all_products = [], []
    for level in range(levels):
        all_vectors.append(flat_vector(current))
        all_products.append(products.copy())
        next_c = new_vector(current, products)
        products = {sign: matrix_product(products[-sign], products[sign])
                    for sign in SIGNS}
        current = next_c
    return all_vectors, all_products

def polynomial_product(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            result[i+j] += c*d
    return result

def polynomial_remainder(numerator, denominator):
    p = [Fraction(x) for x in numerator]
    q = [Fraction(x) for x in denominator]
    while len(p) >= len(q):
        factor = p[-1] / q[-1]
        shift = len(p) - len(q)
        for j, qj in enumerate(q):
            p[shift+j] -= factor * qj
        while p and p[-1] == 0:
            p.pop()
    return p

def check_rational_series(sequence, numerator, denominator, max_level=23):
    for r in range(max_level):
        lhs = sum(denominator[k] * sequence[r-k]
                  for k in range(min(r, len(denominator)-1)+1))
        rhs = numerator[r] if r < len(numerator) else 0
        assert lhs == rhs, (r, lhs, rhs)

def main():
    vectors, products = run_transfer(24)
    # The block-product pair enters its four-cycle at level two.
    assert products[2] == products[6]
    assert products[3] == products[7]

    # Four exact 128-coordinate identities imply the recurrence at every
    # later level, by applying the same four-level linear transfer.
    for r in (3, 4, 5, 6):
        for i in range(128):
            assert (vectors[r+16][i] - 18*vectors[r+12][i]
                    + 49*vectors[r+8][i] - 288*vectors[r+4][i]
                    + 256*vectors[r][i]) == 0

    # Projection onto the eigenvalue 16 of the four-step transfer.
    # Only primitive starting pairs are needed for true recurrence blocks.
    for r in (3, 4, 5, 6):
        for sign_index, sign in enumerate(SIGNS):
            for state_index, (u,v) in enumerate(STATES):
                if not (u & 1 or v & 1):
                    continue
                for j, multiplier in enumerate((1, 2, 1, 2)):
                    pos = (sign_index * 16 + state_index) * 4 + j
                    projected = (vectors[r+12][pos] - 2*vectors[r+8][pos]
                                 + 17*vectors[r+4][pos] - 16*vectors[r][pos])
                    assert 6*projected == 3840 * 2**r * multiplier

    # The original sequence begins with virtual pair (h[-1],h[-2])=(1,-1).
    index = 4 * STATES.index((1, 3))
    A = [[vectors[r][index+j] for r in range(24)] for j in range(4)]
    for r in range(24):
        assert sum(A[j][r] for j in range(4)) == 2**r

    # Four generating functions, written for even/odd residue totals and
    # signed differences. Their denominators divide the universal
    # polynomial (1-16z^4)(1-z^4)(1-z^4+16z^8).
    even = [A[0][r] + A[2][r] for r in range(24)]
    odd = [A[1][r] + A[3][r] for r in range(24)]
    even_diff = [A[0][r] - A[2][r] for r in range(24)]
    odd_diff = [A[1][r] - A[3][r] for r in range(24)]
    totals_den = polynomial_product([1, 0, -1], [1, -2])
    check_rational_series(even, [1, -1, -1], totals_den)
    check_rational_series(odd, [0, 1], totals_den)
    check_rational_series(even_diff, [1, 1, 3, 2], [1, 0, 1])
    odd_den = polynomial_product([1, 0, 0, 0, -1], [1, 0, -3, 0, 4])
    odd_num = [0, 1, 0, -4, 0, 7, 4, 4, -4, -16, -16]
    check_rational_series(odd_diff, odd_num, odd_den)

    universal_den = polynomial_product(
        polynomial_product([1, 0, 0, 0, -16], [1, 0, 0, 0, -1]),
        [1, 0, 0, 0, -1, 0, 0, 0, 16])
    for den in (totals_den, [1, 0, 1], odd_den):
        assert not polynomial_remainder(universal_den, den)

    # A noncancelled pole at modulus 1/sqrt(2) makes the error sharp.
    special_factor = [1, 0, -3, 0, 4]
    remainder = polynomial_remainder(odd_num, special_factor)
    assert remainder == [Fraction(-1, 4), Fraction(-1, 4),
                         Fraction(7, 4), Fraction(7, 4)]
    # The remainder has roots -1 and +/-1/sqrt(7), none in the
    # zero set of 1-3z^2+4z^4.
    assert 1-3+4 != 0 and 1-Fraction(3,7)+Fraction(4,49) != 0

    # Independently compute the original recurrence on 0<=n<2^16.
    low, high = 0, 1
    brute = [1, 1, 0, 0]
    for n in range(2, 1 << 16):
        sign = 1 if n.bit_count() % 2 == 0 else -1
        low, high = high, (sign * high + low) % 4
        brute[high] += 1
    assert brute == [A[j][16] for j in range(4)]
    print('VERIFY_OK: 128-coordinate recurrence, spectral projector,')
    print('four rational identities, noncancellation, and 65,536 direct terms')
    print('dyadic_level_16_counts:', brute)

if __name__ == '__main__':
    main()
