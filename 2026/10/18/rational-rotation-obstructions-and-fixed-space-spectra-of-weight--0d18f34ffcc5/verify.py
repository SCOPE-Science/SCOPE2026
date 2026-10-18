#!/usr/bin/env python3
"""Exact finite-field enumerator for weighted cyclic evolution-algebra automorphisms.
Only standard-library Python is required. Cross-checks use direct matrices and ranks.
"""
from collections import Counter
from math import gcd


class Field:
    # The monic polynomial coefficients are constant-term first.
    def __init__(self, p, polynomial):
        self.p = p
        self.poly = polynomial
        self.e = len(polynomial) - 1
        self.q = p ** self.e
        assert polynomial[-1] == 1

    def components(self, x):
        return [(x // (self.p ** i)) % self.p for i in range(self.e)]

    def value(self, terms):
        return sum((v % self.p) * self.p ** i for i, v in enumerate(terms))

    def add(self, a, b):
        return self.value([x + y for x, y in zip(self.components(a), self.components(b))])

    def neg(self, a):
        return self.value([-x for x in self.components(a)])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        ac, bc = self.components(a), self.components(b)
        v = [0] * (2 * self.e - 1)
        for i, ai in enumerate(ac):
            for j, bj in enumerate(bc):
                v[i + j] += ai * bj
        for i in range(len(v) - 1, self.e - 1, -1):
            c = v[i] % self.p
            for j in range(self.e):
                v[i - self.e + j] -= c * self.poly[j]
        return self.value(v[:self.e])

    def power(self, a, n):
        assert n >= 0
        r = 1
        while n:
            if n & 1:
                r = self.mul(r, a)
            a = self.mul(a, a)
            n //= 2
        return r

    def inv(self, a):
        assert a != 0
        return self.power(a, self.q - 2)


def fixed_dimension(field, c, shift):
    n = len(c)
    f = field
    # Explicit Gaussian elimination for phi-I over the field, independent
    # of the cycle-product formula in the theoretical proof.
    mat = [[0] * n for _ in range(n)]
    for j in range(n):
        mat[(j + shift) % n][j] = c[j]
    for i in range(n):
        mat[i][i] = f.sub(mat[i][i], 1)
    rank = 0
    for col in range(n):
        pivot = next((row for row in range(rank, n) if mat[row][col] != 0), None)
        if pivot is None:
            continue
        mat[pivot], mat[rank] = mat[rank], mat[pivot]
        inv = f.inv(mat[rank][col])
        mat[rank] = [f.mul(x, inv) for x in mat[rank]]
        for row in range(n):
            if row == rank:
                continue
            a = mat[row][col]
            if a:
                mat[row] = [f.sub(x, f.mul(a, y)) for x, y in zip(mat[row], mat[rank])]
        rank += 1
    return n - rank


def brute(field, n, t):
    f = field
    lam = [1] * (n - 1) + [t]
    counts = Counter()
    for s in range(n):
        for first in range(1, f.q):
            c = [first]
            for i in range(n - 1):
                ratio = f.mul(lam[(i+s) % n], f.inv(lam[i]))
                c.append(f.mul(ratio, f.mul(c[-1], c[-1])))
            if f.mul(lam[n - 1], c[0]) != f.mul(lam[(n-1+s) % n], f.mul(c[-1], c[-1])):
                continue
            counts[fixed_dimension(f, c, s)] += 1
    return +counts


def formula(field, n, t):
    M, N = field.q - 1, 2**n - 1
    d = gcd(M, N)
    out = Counter()
    for s in range(n):
        g = gcd(n, s)
        H = N // (2**g - 1)
        J = (2**s - 1) // (2**g - 1)
        b = gcd(M, H)
        A = d if field.power(t, (2**s - 1) * (M // d)) == 1 else 0
        B = b if field.power(t, J * (M // b)) == 1 else 0
        assert B <= A
        out[0] += A - B
        out[g] += B
    return +out


def verify():
    # The extension moduli have been chosen irreducible over their prime fields.
    fields = [(2, [0, 1]), (3, [0, 1]), (5, [0, 1]),
              (7, [0, 1]), (11, [0, 1]), (13, [0, 1]),
              (19, [0, 1]), (31, [0, 1]), (43, [0, 1]),
              (2, [1, 1, 1]),       # F_4: z^2+z+1
              (2, [1, 1, 0, 1]),    # F_8: z^3+z+1
              (3, [1, 0, 1]),       # F_9: z^2+1
              (2, [1, 1, 0, 0, 1])] # F_16: z^4+z+1
    cases = 0
    for p, mod in fields:
        F = Field(p, mod)
        for n in range(2, 8 if F.q <= 13 else 7):
            for t in range(1, F.q):
                predicted = formula(F, n, t)
                observed = brute(F, n, t)
                assert predicted == observed, (F.q, n, t, predicted, observed)
                cases += 1
    F = Field(43, [0, 1])
    assert F.power(3, 7) == 37
    assert formula(F, 6, 37) == Counter({0: 62, 6: 1})
    assert brute(F, 6, 37) == Counter({0: 62, 6: 1})
    assert (43**6 - 1) % 63 == 0
    print('VERIFY_OK', cases, 'independent finite-field configurations')


if __name__ == '__main__':
    verify()
