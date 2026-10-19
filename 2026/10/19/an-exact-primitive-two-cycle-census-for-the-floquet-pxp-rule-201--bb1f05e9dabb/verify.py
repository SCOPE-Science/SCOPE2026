"""Exact, stdlib-only checks of a two-cycle transfer-matrix formula.

Run: python3 verify.py
The code is deliberately independent of symbolic-algebra libraries.
"""

FORBIDDEN = {"00000", "00001", "01001", "01010", "10000", "10010"}


def gate(a, c):
    return (1 - a) * (1 - c)


def local_condition(bits):
    a, b, c, d, e = bits
    old = gate(b, d)
    left = b ^ gate(a, c)
    right = d ^ gate(c, e)
    return old == gate(left, right)


def transfer():
    mat = [[0] * 16 for _ in range(16)]
    for four in range(16):
        a, b, c, d = ((four >> i) & 1 for i in (3, 2, 1, 0))
        for e in (0, 1):
            if local_condition((a, b, c, d, e)):
                nxt = ((four << 1) & 15) | e
                mat[four][nxt] += 1
    return mat


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matmul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def charpoly_coeffs(a):
    """Faddeev--LeVerrier, integer arithmetic with exact divisions."""
    n = len(a)
    b = eye(n)
    coeffs = [1]
    for k in range(1, n + 1):
        c = matmul(a, b)
        numerator = -trace(c)
        assert numerator % k == 0
        ck = numerator // k
        coeffs.append(ck)
        for i in range(n):
            c[i][i] += ck
        b = c
    return coeffs


def direct_f(state, n):
    value = state
    for parity in (0, 1):
        nxt = value
        for site in range(parity, n, 2):
            left = (value >> ((site - 1) % n)) & 1
            right = (value >> ((site + 1) % n)) & 1
            if left == 0 and right == 0:
                nxt ^= (1 << site)
        value = nxt
    return value


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def check():
    observed = {format(k, '05b') for k in range(32)
                if not local_condition(tuple((k >> i) & 1 for i in (4, 3, 2, 1, 0)))}
    assert observed == FORBIDDEN, (observed, FORBIDDEN)
    matrix = transfer()
    # z^8 (z^2+1)(z^6-z^5-z^4-z^2-z+1)
    polynomial = [1, -1, -1, 0, -1, -1, 1]  # sextic, descending
    a = [0] * 9
    for k, value in enumerate(polynomial):
        a[k] += value
        a[k + 2] += value
    expected = a + [0] * 8
    actual = charpoly_coeffs(matrix)
    assert actual == expected, (actual, expected)
    print('For every five-bit window, forbidden patterns:', sorted(observed))
    print('Characteristic polynomial coefficients, degrees 16..0:', actual)
    assert sum(sum(row) for row in matrix) == 26
    powers = eye(16)
    for n in range(1, 19):
        powers = matmul(powers, matrix)
        if n % 2 or n < 4:
            continue
        fixed_two = trace(powers)
        fixed_one = lucas(n // 2) ** 2
        if n <= 16:
            exhaustive_one = 0
            exhaustive_two = 0
            forbidden_avoidance = 0
            for state in range(1 << n):
                first = direct_f(state, n)
                second = direct_f(first, n)
                exhaustive_one += first == state
                exhaustive_two += second == state
                good = all(local_condition(tuple((state >> ((i + off) % n)) & 1
                                                     for off in (-2, -1, 0, 1, 2)))
                           for i in range(n))
                forbidden_avoidance += good
                assert (second == state) == good
            assert (exhaustive_one, exhaustive_two, forbidden_avoidance) == (
                fixed_one, fixed_two, fixed_two)
        assert fixed_two >= fixed_one and (fixed_two - fixed_one) % 2 == 0
        print('n={}, Fix(F)={}, Fix(F^2)={}, primitive 2-cycles={}'.format(
            n, fixed_one, fixed_two, (fixed_two - fixed_one) // 2))
    print('All exact transfer, polynomial, and independent orbit checks passed.')


if __name__ == '__main__':
    check()
