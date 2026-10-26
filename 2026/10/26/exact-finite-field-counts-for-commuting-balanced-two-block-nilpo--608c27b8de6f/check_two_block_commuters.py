"""Exact arithmetic checks for an enumerated finite-field centralizer stratum.

Run: python3 check_two_block_commuters.py
Only prime fields are enumerated; the published proof applies to all prime powers.
"""
import itertools
from math import gcd


def mm(A, B, p):
    h = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(h)) % p
             for j in range(h)] for i in range(h)]


def power(A, n, p):
    h = len(A)
    P = [[int(i == j) for j in range(h)] for i in range(h)]
    while n:
        if n % 2:
            P = mm(P, A, p)
        A = mm(A, A, p)
        n //= 2
    return P


def formula(n, q, p):
    g1, g2 = gcd(n, q - 1), gcd(n, q + 1)
    assert (g1 + g2) % 2 == 0
    t = q - (g1 + g2) // 2 + (n % p != 0)
    assert t >= 0
    return (q - 1) ** 2 * t * q ** (4 * n - 8)


def twobytwo_count(n, p):
    count = 0
    for a, b, c, d in itertools.product(range(p), repeat=4):
        if (a * d - b * c) % p:
            if power([[a, b], [c, d]], n, p)[0][0] == 0:
                count += 1
    return count


def rank(M, p):
    rows = [r[:] for r in M]
    h = len(rows)
    s = 0
    for j in range(h):
        k = next((i for i in range(s, h) if rows[i][j]), None)
        if k is None:
            continue
        rows[s], rows[k] = rows[k], rows[s]
        inv = pow(rows[s][j], -1, p)
        rows[s] = [(z * inv) % p for z in rows[s]]
        for i in range(s + 1, h):
            c = rows[i][j]
            if c:
                rows[i] = [(x - c * y) % p for x, y in zip(rows[i], rows[s])]
        s += 1
    return s


def commuting_matrix(n, p, a, d, b, c):
    # Basis is 1,t,...,t^n of the long summand, followed by
    # 1,t,...,t^(n-2) of the short summand.
    long, short = n + 1, n - 1
    h = 2 * n
    Y = [[0] * h for _ in range(h)]
    for j in range(long):
        for k in range(j, long):
            Y[k][j] = a[k - j]
        for k in range(j, short):
            Y[long + k][j] = c[k - j]
    for j in range(short):
        for k in range(j + 2, long):
            Y[k][long + j] = b[k - j - 2]
        for k in range(j, short):
            Y[long + k][long + j] = d[k - j]
    return Y


def exhaustive_full_matrix(n, p):
    total = p ** (4 * n - 4)
    seen = 0
    for coeff in itertools.product(range(p), repeat=4 * n - 4):
        a = (0,) + coeff[:n]
        d = (0,) + coeff[n:2*n - 2]
        b = coeff[2*n - 2:3*n - 3]
        c = coeff[3*n - 3:]
        Y = commuting_matrix(n, p, a, d, b, c)
        if rank(Y, p) == 2 * n - 2:
            if not any(z for row in power(Y, n, p) for z in row):
                seen += 1
    expected = formula(n, p, p)
    assert seen == expected, (n, p, total, seen, expected)
    return n, p, total, seen


def main():
    prime_field_tests = 0
    for p in (2, 3, 5, 7, 11):
        for n in (3, 4, 5, 6, 7, 8, 12, 15):
            observed = twobytwo_count(n, p)
            predicted = (p - 1) ** 2 * (
                p - (gcd(n, p - 1) + gcd(n, p + 1)) // 2
                + (n % p != 0))
            assert observed == predicted, (n, p, observed, predicted)
            prime_field_tests += 1
    direct_tests = [exhaustive_full_matrix(n, p) for n, p in
                    ((3, 2), (3, 3), (4, 2))]
    print('TWO_BLOCK_COUNT_OK')
    print('2x2 exhaustive cases:', prime_field_tests)
    print('Full centralizer exhaustive cases:', direct_tests)

if __name__ == '__main__':
    main()
