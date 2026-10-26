"""Independent finite-field checks for cycle evolution-algebra idempotents.

Run with Python 3 standard library: python check_idempotents.py.
"""
from itertools import product

IRREDUCIBLE = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}


def gf_mul(a, b, e):
    mod = IRREDUCIBLE[e]
    mask = (1 << e) - 1
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
        if a & (1 << e):
            a ^= mod
    return z & mask


def gf_square(a, e):
    return gf_mul(a, a, e)


def poly_mul(a, b):
    c = 0
    while b:
        if b & 1:
            c ^= a
        a <<= 1
        b >>= 1
    return c


def poly_pow(a, e):
    out = 1
    while e:
        if e & 1:
            out = poly_mul(out, a)
        e >>= 1
        a = poly_mul(a, a)
    return out


def poly_rem(a, b):
    if not b:
        raise ZeroDivisionError
    db = b.bit_length() - 1
    while a and a.bit_length() - 1 >= db:
        a ^= b << (a.bit_length() - 1 - db)
    return a


def poly_gcd(a, b):
    while b:
        a, b = b, poly_rem(a, b)
    return a


def polynomial_prediction(n, e):
    p = poly_pow(0b101, e) ^ (1 << e)
    d = poly_gcd((1 << n) | 1, p).bit_length() - 1
    return 1 << d


def binary_matmul(a, b, n):
    rows = []
    for ra in a:
        row = 0
        for j in range(n):
            if (ra >> j) & 1:
                row ^= b[j]
        rows.append(row)
    return rows


def binary_rank(rows, n):
    rows = rows[:]
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, len(rows)) if (rows[i] >> c) & 1), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        for k in range(len(rows)):
            if k != r and (rows[k] >> c) & 1:
                rows[k] ^= rows[r]
        r += 1
    return r


def binary_matrix_prediction(n, e):
    a = [((1 << ((i - 1) % n)) | (1 << ((i + 1) % n))) for i in range(n)]
    power = [(1 << i) for i in range(n)]
    for _ in range(e):
        power = binary_matmul(a, power, n)
    for i in range(n):
        power[i] ^= 1 << i
    return 1 << (n - binary_rank(power, n))


def brute_count(n, e):
    q = 1 << e
    squares = [gf_square(x, e) for x in range(q)]
    total = 0
    for v in product(range(q), repeat=n):
        if all((squares[v[(j - 1) % n]] ^ squares[v[(j + 1) % n]]) == v[j] for j in range(n)):
            total += 1
    return total


def main():
    matrix_tests = 0
    for e in range(1, 13):
        for n in range(3, 43):
            p = polynomial_prediction(n, e)
            q = binary_matrix_prediction(n, e)
            assert p == q, (n, e, p, q)
            assert p <= (1 << (2 * e)), (n, e, p)
            matrix_tests += 1
    enum_tests = 0
    for e, ns in [(1, range(3, 12)), (2, range(3, 8)), (3, range(3, 6)), (4, range(3, 5))]:
        for n in ns:
            p = polynomial_prediction(n, e)
            q = brute_count(n, e)
            assert p == q, (n, e, p, q)
            enum_tests += 1
    for n in range(3, 80):
        assert polynomial_prediction(n, 1) == (4 if n % 3 == 0 else 1)
        expect2 = (1 if n % 3 else (16 if n % 2 == 0 else 4))
        assert polynomial_prediction(n, 2) == expect2
        expect3 = 2 ** (2 * (n % 3 == 0) + 4 * (n % 5 == 0))
        assert polynomial_prediction(n, 3) == expect3, (n, expect3, polynomial_prediction(n, 3))
    period_tests = 0
    for e, period in {1: 3, 2: 6, 3: 15, 4: 12, 6: 30, 8: 24}.items():
        for n in range(3, 110):
            assert polynomial_prediction(n, e) == polynomial_prediction(n + period, e)
            assert (polynomial_prediction(n, e) == 2 ** (2 * e)) == (n % period == 0)
            period_tests += 1
    print('CYCLE_EVOLUTION_IDEMPOTENTS_OK', matrix_tests, 'matrix_pairs', enum_tests, 'direct_enumerations', period_tests, 'period_tests')


if __name__ == '__main__':
    main()
