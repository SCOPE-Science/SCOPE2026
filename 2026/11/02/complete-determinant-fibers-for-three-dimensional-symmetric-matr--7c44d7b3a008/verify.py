#!/usr/bin/env python3
"""Exact independent enumeration for fixed-diagonal symmetric 3x3 determinant fibers.

Only standard-library integer arithmetic.  The quadratic-extension model for F_9
is F_3[t]/(t*t+1), with encoding a+3*b for a+b*t.
"""
from itertools import product


def prime_ops(p):
    return list(range(p)), lambda a, b: (a + b) % p, lambda a, b: (a * b) % p


def q9_ops():
    def add(a, b):
        return ((a % 3 + b % 3) % 3) + 3 * ((a // 3 + b // 3) % 3)

    def mul(a, b):
        aa, ab = a % 3, a // 3
        ba, bb = b % 3, b // 3
        return ((aa * ba - ab * bb) % 3) + 3 * ((aa * bb + ab * ba) % 3)

    return list(range(9)), add, mul


def count_and_check(elements, add, mul, diagonal_vectors, label):
    q = len(elements)
    minus_one = next(v for v in elements if add(v, 1) == 0)

    def neg(v):
        return mul(minus_one, v)

    squares = {mul(v, v) for v in elements if v}

    def chi(v):
        return 0 if not v else (1 if v in squares else -1)

    def determinant(a, b, c, x, y, z):
        # Direct Leibniz six-permutation expansion, with no use of the proof.
        pos = add(add(mul(mul(a, b), c), mul(mul(x, y), z)), mul(mul(x, y), z))
        negsum = add(add(mul(a, mul(z, z)), mul(b, mul(y, y))), mul(c, mul(x, x)))
        return add(pos, neg(negsum))

    fibers = 0
    matrices = 0
    for a, b, c in diagonal_vectors:
        counts = {v: 0 for v in elements}
        for x, y, z in product(elements, repeat=3):
            counts[determinant(a, b, c, x, y, z)] += 1
            matrices += 1
        k = (a != 0) + (b != 0) + (c != 0)
        abc = mul(mul(a, b), c)
        if k == 3:
            expected_zero = q * q + 1
        elif k == 2:
            expected_zero = q * q - q + 1
        elif k == 1:
            expected_zero = 2 * q * q - 2 * q + 1
        else:
            expected_zero = 3 * q * q - 3 * q + 1
        assert counts[0] == expected_zero, (label, (a,b,c), counts[0], expected_zero)
        fibers += 1
        for delta in elements[1:]:
            base = q * q + 1
            legendre = sum(chi(mul(neg(delta), t)) for t in (a, b, c))
            if k == 3:
                abc_minus_delta = add(abc, neg(delta))
                legendre += chi(mul(neg(delta), abc_minus_delta))
            legendre -= max(2 - k, 0)
            predicted = base + q * legendre
            assert predicted == counts[delta], (label, (a,b,c), delta, predicted, counts[delta])
            fibers += 1
    return fibers, matrices


def main():
    total_fibers = total_matrices = 0
    for p in (3, 5, 7, 11):
        elems, add, mul = prime_ops(p)
        f, m = count_and_check(elems, add, mul, product(elems, repeat=3), 'F_' + str(p))
        total_fibers += f
        total_matrices += m
    elems, add, mul = q9_ops()
    points = [0, 1, 2, 3, 4, 5, 8]
    diagonals = [(0,0,0), (0,0,1), (0,1,1), (1,1,1),
                 (3,4,5), (0,3,4), (2,3,8), (1,2,8)]
    f, m = count_and_check(elems, add, mul, diagonals, 'F_9')
    total_fibers += f
    total_matrices += m
    print('VERIFY_OK prime_fields=3,5,7,11 extension_field=9'
          ' determinant_fibers={} independent_matrices={}'
          ' singular_and_nonzero_cases=yes'.format(total_fibers, total_matrices))


if __name__ == '__main__':
    main()
