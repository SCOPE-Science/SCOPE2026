#!/usr/bin/env python3
"""Exact checks for point counts on the quadratic-character plane-curve family.

No external packages or external data are required. Polynomial arithmetic is
performed over the rationals; field enumeration covers prime and extension
fields using explicit irreducible binomials.
"""
from fractions import Fraction


def add(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, Fraction(0)) + v
    return {k: v for k, v in c.items() if v}


def neg(a):
    return {k: -v for k, v in a.items()}


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    c = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            key = (i + k, j + l)
            c[key] = c.get(key, Fraction(0)) + x * y
    return {k: v for k, v in c.items() if v}


def power(a, n):
    out = {(0, 0): Fraction(1)}
    for _ in range(n):
        out = mul(out, a)
    return out


def scale(a, x):
    return {k: v * x for k, v in a.items() if v * x}


def symbolic_verification():
    one = {(0, 0): Fraction(1)}
    q = {(1, 0): Fraction(1)}
    z = {(0, 1): Fraction(1)}
    iz = {(0, -1): Fraction(1)}
    alpha = scale(add(z, iz), Fraction(1, 2))
    beta = scale(sub(z, iz), Fraction(1, 2))
    qm1 = sub(q, one)
    f0 = add(one, mul(qm1, alpha))
    u = sub(one, alpha)
    q2 = power(q, 2)
    core = add(power(f0, 4), mul(qm1, sub(power(u, 4), mul(q2, power(beta, 4)))))
    core_plus = add(power(f0, 4), mul(qm1, add(add(power(u, 4), scale(mul(q, mul(power(u, 2), power(beta, 2))), 6)), mul(q2, power(beta, 4)))))
    hminus = {(i, j): v for (i, j), v in core.items() if j == 0}
    hplus = {(i, j): v for (i, j), v in core_plus.items() if j == 0}
    # Character orthogonality says q*N_aff is the constant Laurent coefficient.
    predicted_minus = scale(mul(q, add(one, mul(qm1, scale(add(sub(power(q, 2), scale(q, 4)), scale(one, 11)), Fraction(3, 8))))), 1)
    predicted_plus = mul(q, add(one, scale(mul(qm1, power(qm1, 2)), Fraction(3, 8))))
    assert hminus == predicted_minus, (hminus, predicted_minus)
    assert hplus == predicted_plus, (hplus, predicted_plus)
    print('FORMAL_LAURENT_COEFFICIENT_IDENTITIES_PASS')


class FiniteField:
    def __init__(self, p, n=1, c=0):
        self.p, self.n, self.c = p, n, c
        self.q = p ** n
        self.elems = [tuple((i // (p ** j)) % p for j in range(n)) for i in range(self.q)]
        self.index = {a: i for i, a in enumerate(self.elems)}
        self.zero = 0
        self.one = self.index[(1,) + (0,) * (n - 1)]
        self.minus = self.index[((p - 1),) + (0,) * (n - 1)]
        self.chis = [self._character(i) for i in range(self.q)]

    def add(self, a, b):
        x = self.elems[a]
        y = self.elems[b]
        return self.index[tuple((x[k] + y[k]) % self.p for k in range(self.n))]

    def mul(self, a, b):
        x = self.elems[a]
        y = self.elems[b]
        z = [0] * (2 * self.n - 1)
        for i in range(self.n):
            for j in range(self.n):
                z[i + j] += x[i] * y[j]
        for k in range(2 * self.n - 2, self.n - 1, -1):
            z[k - self.n] += z[k] * self.c
        return self.index[tuple(z[i] % self.p for i in range(self.n))]

    def pow(self, a, n):
        r = self.one
        while n:
            if n & 1:
                r = self.mul(r, a)
            a = self.mul(a, a)
            n //= 2
        return r

    def _character(self, a):
        if a == self.zero:
            return 0
        t = self.pow(a, (self.q - 1) // 2)
        assert t in (self.one, self.minus), (self.q, a, t)
        return 1 if t == self.one else -1


def point_count(field):
    q = field.q
    ch = field.chis
    add = field.add
    one = field.one
    count = 0
    for x in range(q):
        for y in range(q):
            s = add(add(x, y), one)
            if ch[s] + ch[x] + ch[y] + 1 == 0:
                count += 1
    for x in range(q):
        if ch[add(x, one)] + ch[x] + 1 == 0:
            count += 1
    if ch[one] + ch[one] == 0:
        count += 1
    # Coordinate-axis x=0, with z=1, y arbitrary, and [0:1:0].
    axis = sum(ch[add(y, one)] + ch[y] + 1 == 0 for y in range(q))
    axis += int(ch[one] + ch[one] == 0)
    return count, axis


def expected(q):
    if q % 4 == 1:
        assert 3 * (q - 1) ** 2 % 8 == 0
        return 3 * (q - 1) ** 2 // 8, 0
    assert q % 4 == 3
    assert 3 * (q * q - 4 * q + 11) % 8 == 0
    return 3 * (q * q - 4 * q + 11) // 8, 1


if __name__ == '__main__':
    symbolic_verification()
    for p in [5, 7, 11, 13, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, 103]:
        field = FiniteField(p)
        got = point_count(field)
        assert got == expected(p), (p, got, expected(p))
        print(f'F_{p}_POINTS_{got[0]}_AXIS_{got[1]}_PASS')
    for p, n, c in [(5, 2, 2), (7, 2, 3), (11, 2, 2), (7, 3, 2)]:
        field = FiniteField(p, n, c)
        got = point_count(field)
        assert got == expected(p ** n), (p, n, got)
        print(f'F_{p ** n}_POINTS_{got[0]}_AXIS_{got[1]}_PASS')
    print('BLOCKING_CURVE_POINT_COUNT_FORMAL_AND_EXTENSION_FIELD_PASS')
