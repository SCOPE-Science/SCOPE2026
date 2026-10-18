"""Exhaustive finite-field checks of complete-graph evolution idempotents.

Standalone Python 3 script; no third-party packages required.
This checks exact finite instances, not the general proof.
"""
from itertools import product
from math import comb


class Field:
    def __init__(self, p, degree=1, nonsquare=None):
        assert degree in (1, 2)
        self.p, self.degree = p, degree
        self.q = p ** degree
        if degree == 2 and p != 2:
            if nonsquare is None:
                nonsquare = next(a for a in range(1, p)
                                 if pow(a, (p - 1) // 2, p) == p - 1)
            self.nu = nonsquare
        self.add = [[self._add(a, b) for b in range(self.q)]
                    for a in range(self.q)]
        self.mul = [[self._mul(a, b) for b in range(self.q)]
                    for a in range(self.q)]

    def _add(self, x, y):
        p = self.p
        if self.degree == 1:
            return (x + y) % p
        return ((x % p + y % p) % p
                + p * ((x // p + y // p) % p))

    def _mul(self, x, y):
        p = self.p
        if self.degree == 1:
            return x * y % p
        a, b, c, d = x % p, x // p, y % p, y // p
        if p == 2:  # omega^2 + omega + 1 = 0
            return ((a * c + b * d) % p
                    + p * ((a * d + b * c + b * d) % p))
        return ((a * c + self.nu * b * d) % p
                + p * ((a * d + b * c) % p))


def predicted(p, f, n):
    assert n >= 2
    if p == 2:
        return 2 ** (n - 1) if n % 2 or f % 2 else 2 ** n
    if (n - 1) % p == 0:
        z = sum(comb(n, k) for k in range(n + 1)
                if (2 * k - n) % p == 0)
        return (2 ** n - z) // 2
    extra = int((n + 1) % p == 0)
    total = 0
    for k in range(n + 1):
        delta = ((2 * k - n) ** 2 - (n * n - 1)) % p
        character = 0 if delta == 0 else (1 if f % 2 == 0 else
                                          (1 if pow(delta, (p-1)//2, p) == 1 else -1))
        total += comb(n, k) * (1 + character - extra)
    assert total % 2 == 0
    return extra + total // 2


def actual(field, n):
    q = field.q
    add, mul = field.add, field.mul
    count = 0
    for xs in product(range(q), repeat=n):
        squares = [mul[v][v] for v in xs]
        s = 0
        for t in squares:
            s = add[s][t]
        if all(add[x][mul[x][x]] == s for x in xs):
            count += 1
    return count


def main():
    cases = []
    for p in (2, 3, 5, 7, 11):
        for n in range(2, 8):
            if p ** n <= 50000:
                cases.append((p, 1, n))
    for p, nmax in ((2, 6), (3, 5), (5, 4), (7, 3)):
        for n in range(2, nmax + 1):
            if p ** (2*n) <= 500000:
                cases.append((p, 2, n))
    for p, degree, n in cases:
        field = Field(p, degree)
        got = actual(field, n)
        expected = predicted(p, degree, n)
        assert got == expected, (p, degree, n, got, expected)
        print(f'GF({p}^{degree}), n={n}: {got} idempotents')
    print(f'VERIFY_OK: {len(cases)} exact finite-field idempotent censuses')


if __name__ == '__main__':
    main()
