from math import comb, factorial, gcd
from fractions import Fraction


def degree_product(n, c):
    q = Fraction(1, 1)
    for j in range(c):
        q *= Fraction(factorial(n + j) * factorial(j),
                      factorial(n - c + j) * factorial(c + j))
    assert q.denominator == 1
    return q.numerator


def bareiss_det(a):
    a = [row[:] for row in a]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            s = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if s is None:
                return 0
            a[k], a[s] = a[s], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def degree_det(n, c):
    mat = []
    for i in range(1, c + 1):
        row = []
        for j in range(1, c + 1):
            k = c - i + j
            row.append(comb(n, k) if 0 <= k <= n else 0)
        mat.append(row)
    return bareiss_det(mat)


def factor(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def prime_support(n):
    return [p for p, _ in factor(n)]


formula_checks = 0
for n in range(2, 33):
    for c in range(1, n):
        assert degree_product(n, c) == degree_det(n, c)
        formula_checks += 1

classification_checks = 0
witness_checks = 0
for n in range(2, 121):
    degrees = [degree_product(n, c) for c in range(1, n)]
    g = 0
    for d in degrees:
        g = gcd(g, d)
    fac = factor(n)
    if len(fac) == 1:
        p, e = fac[0]
        assert g > 1
        assert set(prime_support(g)) == {p}
        assert all(d % p == 0 for d in degrees)
    else:
        assert g == 1
        for p, e in fac:
            c = p ** e
            d = degree_product(n, c)
            assert d % p != 0, (n, p, c, d)
            witness_checks += 1
    assert n % g == 0
    classification_checks += 1

print('VERIFY_OK', formula_checks, classification_checks, witness_checks)
