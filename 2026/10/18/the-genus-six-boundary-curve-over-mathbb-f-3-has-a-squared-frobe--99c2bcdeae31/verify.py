#!/usr/bin/env python3
"""Exact rational-place census and Weil polynomial for a characteristic-three Artin--Schreier curve.

Self-contained, standard-library-only: integer arithmetic in polynomial quotient fields.
The genus-six normalization and its four simple rational poles are proved
by the standard Artin--Schreier genus and ramification formulas.
"""
from itertools import product

P = 3
MODULI = {
    1: (0, 1),
    2: (1, 0, 1),
    3: (1, 0, 2, 1),
    4: (1, 0, 1, 1, 1),
    5: (1, 0, 0, 0, 2, 1),
    6: (1, 0, 0, 0, 1, 1, 1),
}
EXPECTED_COUNTS = (4, 10, 76, 82, 244, 670)
EXPECTED_WEIL = (1, 0, 0, 16, 0, 0, 118, 0, 0, 432, 0, 0, 729)


def mod_poly_rem(a, b):
    a = list(a)
    b = list(b)
    while len(a) >= len(b):
        c = a[-1] * pow(b[-1], -1, 3) % 3
        for i in range(len(b)):
            a[len(a) - len(b) + i] = (a[len(a) - len(b) + i] - c * b[i]) % 3
        while a and a[-1] == 0:
            a.pop()
    return a


def check_irreducible(poly):
    n = len(poly) - 1
    assert poly[-1] == 1 and (n == 1 or poly[0] != 0)
    for k in range(1, n // 2 + 1):
        for digits in product(range(3), repeat=k):
            if not any(digits):
                continue
            if not mod_poly_rem(poly, (*digits, 1)):
                return False
    return True


class Field:
    def __init__(self, poly):
        self.mod = tuple(poly)
        self.n = len(poly) - 1
        self.q = 3 ** self.n
        assert check_irreducible(poly)
        self.vec = [tuple((i // (3 ** j)) % 3 for j in range(self.n)) for i in range(self.q)]
        to_int = {v: i for i, v in enumerate(self.vec)}
        self.add = [[to_int[tuple((x[k] + y[k]) % 3 for k in range(self.n))]
                     for y in self.vec] for x in self.vec]
        self.neg = [to_int[tuple((-x[k]) % 3 for k in range(self.n))] for x in self.vec]
        self.mul = [[self._multiply(x, y, to_int) for y in self.vec] for x in self.vec]
        self.inv = [0] * self.q
        for x in range(1, self.q):
            inverses = [y for y in range(1, self.q) if self.mul[x][y] == 1]
            assert len(inverses) == 1
            self.inv[x] = inverses[0]
        self.fibre = [0] * self.q
        for y in range(self.q):
            y3 = self.power(y, 3)
            image = self.add[y3][self.neg[y]]
            self.fibre[image] += 1
        assert sorted(set(self.fibre)) == [0, 3]

    def _multiply(self, x, y, to_int):
        n = self.n
        vec = [0] * (2 * n - 1)
        for i in range(n):
            for j in range(n):
                vec[i + j] = (vec[i + j] + x[i] * y[j]) % 3
        for k in range(2 * n - 2, n - 1, -1):
            c = vec[k]
            for j in range(n):
                vec[k - n + j] = (vec[k - n + j] - c * self.mod[j]) % 3
        return to_int[tuple(vec[:n])]

    def power(self, x, m):
        acc = 1
        while m:
            if m & 1:
                acc = self.mul[acc][x]
            x = self.mul[x][x]
            m >>= 1
        return acc

    def trace(self, x):
        z = x
        total = 0
        for _ in range(self.n):
            total = self.add[total][z]
            z = self.power(z, 3)
        assert total in (0, 1, 2)
        return total

    def count(self):
        direct = 4  # exactly one totally ramified rational point over each of 0,+1,-1,infinity
        trace = 4
        poles = 0
        for x in range(self.q):
            denominator = self.add[self.power(x, 3)][self.neg[x]]
            if denominator == 0:
                poles += 1
                continue
            rhs = self.add[x][self.inv[denominator]]
            direct += self.fibre[rhs]
            trace += 3 * (self.trace(rhs) == 0)
            assert self.fibre[rhs] == 3 * (self.trace(rhs) == 0)
        assert poles == 3 and direct == trace
        return direct


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return tuple(c)


def main():
    counts = []
    for n, poly in MODULI.items():
        count = Field(poly).count()
        counts.append(count)
        assert count == EXPECTED_COUNTS[n - 1]
        print('extension degree', n, 'field cardinality', 3**n,
              'irreducible modulus', poly, 'point count', count)
    first = [1]
    for n in range(1, 7):
        numerator = sum(first[n - k] * (counts[k - 1] - (3**k + 1))
                        for k in range(1, n + 1))
        assert numerator % n == 0
        first.append(numerator // n)
    full = first + [3**(i - 6) * first[12 - i] for i in range(7, 13)]
    assert tuple(full) == EXPECTED_WEIL
    e = (1, -1, 3)
    surface = (1, 1, -2, 3, 9)
    factor = multiply(e, surface)
    assert multiply(factor, factor) == EXPECTED_WEIL
    # Integral irreducibility of u^4+u^3-2u^2+3u+9:
    # rational linear roots are impossible for a weight-one Weil polynomial;
    # if it has two rational quadratic factors, each factor has constant +/-3.
    # For constants (+3,+3), sums and products of middle coefficients
    # would be 1 and -8, requiring a root of t^2-t-8 (discriminant 33).
    # For constants (-3,-3), the u coefficient would be -3, not +3.
    assert 1**2 - 4*(-8) == 33
    # Direct count of E: v^2=u^3+u^2+2 over GF(3).
    e_points = 1 + sum((v*v - (u**3 + u*u + 2)) % 3 == 0
                       for u in range(3) for v in range(3))
    assert e_points == 3
    assert 4-e_points == 1  # trace of Frobenius
    assert sum(e) == 3 and sum(surface) == 12
    assert sum(EXPECTED_WEIL) == 1296
    print('full zeta numerator coefficients:', tuple(full))
    print('elliptic factor:', e, 'surface factor:', surface)
    print('Jacobian F3 cardinality:', sum(full))
    print('ALL EXACT CHECKS PASSED')


if __name__ == '__main__':
    main()
