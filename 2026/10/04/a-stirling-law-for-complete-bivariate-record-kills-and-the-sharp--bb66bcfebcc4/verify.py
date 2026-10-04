from fractions import Fraction
from math import factorial


def stirling_row(m):
    row = [0] * (m + 1)
    row[0] = 1
    for n in range(1, m + 1):
        nxt = [0] * (m + 1)
        for k in range(1, n + 1):
            nxt[k] = row[k - 1] + (n - 1) * row[k]
        row = nxt
    return row


def harmonic(m):
    return sum((Fraction(1, j) for j in range(1, m + 1)), Fraction(0))


def C(n, k):
    return Fraction(stirling_row(n - 1)[k], n * n * factorial(n - 1))

for n in range(2, 30):
    vals = [C(n, k) for k in range(1, n)]
    assert sum(vals, Fraction(0)) == Fraction(1, n * n)
    assert C(n, 1) == Fraction(1, n * n * (n - 1))
    if n >= 3:
        assert C(n, 2) == Fraction(1, n * n * (n - 1)) * harmonic(n - 2)
    assert C(n, n - 1) == Fraction(1, n * factorial(n))

published = {
    2: [Fraction(1, 4)],
    3: [Fraction(1, 18), Fraction(1, 18)],
    4: [Fraction(1, 48), Fraction(1, 32), Fraction(1, 96)],
    5: [Fraction(1, 100), Fraction(11, 600), Fraction(1, 100), Fraction(1, 600)],
}
for n, row in published.items():
    assert [C(n, k) for k in range(1, n)] == row

print("VERIFY_OK")
