#!/usr/bin/env python3
"""Independent finite-field checks for simultaneous zero-products in split octonions.

No external packages. Zorn multiplication is implemented directly, and the
rank of the complete 16-by-8 left/right multiplication matrix is computed
from scratch for each element. F4 is the field F2[t]/(t*t+t+1).
"""
from collections import Counter
from itertools import product


class Field:
    def __init__(self, q):
        self.q = q
        if q == 4:
            self.add = lambda a, b: a ^ b
            def multiply(a, b):
                ans = 0
                while b:
                    if b & 1:
                        ans ^= a
                    b >>= 1
                    a <<= 1
                    if a & 4:
                        a ^= 7  # t^2 + t + 1
                return ans
            self.mul = multiply
        else:
            self.add = lambda a, b: (a + b) % q
            self.mul = lambda a, b: (a * b) % q
        self.neg = lambda a: next(b for b in range(q) if self.add(a, b) == 0)
        self.sub = lambda a, b: self.add(a, self.neg(b))
        self.inverse = {a: next(b for b in range(1, q) if self.mul(a, b) == 1)
                        for a in range(1, q)}

    def dot(self, a, b):
        s = 0
        for u, v in zip(a, b):
            s = self.add(s, self.mul(u, v))
        return s

    def cross(self, a, b):
        s = self.sub
        m = self.mul
        return (s(m(a[1], b[2]), m(a[2], b[1])),
                s(m(a[2], b[0]), m(a[0], b[2])),
                s(m(a[0], b[1]), m(a[1], b[0])))

    def multiply_octonion(self, x, y):
        a, u1, u2, u3, v1, v2, v3, b = x
        c, s1, s2, s3, t1, t2, t3, d = y
        u, v, s, t = (u1, u2, u3), (v1, v2, v3), (s1, s2, s3), (t1, t2, t3)
        add, sub, mul = self.add, self.sub, self.mul
        ct, cs = self.cross(v, t), self.cross(u, s)
        return (add(mul(a, c), self.dot(u, t)),
                *(sub(add(mul(a, s[i]), mul(d, u[i])), ct[i]) for i in range(3)),
                *(add(add(mul(c, v[i]), mul(b, t[i])), cs[i]) for i in range(3)),
                add(mul(b, d), self.dot(v, s)))

    def norm(self, x):
        return self.sub(self.mul(x[0], x[7]), self.dot(x[1:4], x[4:7]))

    def trace(self, x):
        return self.add(x[0], x[7])

    def rank(self, a):
        a = [list(row) for row in a]
        rows, cols, r = len(a), len(a[0]), 0
        add, mul, neg = self.add, self.mul, self.neg
        for j in range(cols):
            pivot = next((i for i in range(r, rows) if a[i][j] != 0), None)
            if pivot is None:
                continue
            a[r], a[pivot] = a[pivot], a[r]
            inv = self.inverse[a[r][j]]
            a[r] = [mul(inv, z) for z in a[r]]
            for i in range(r + 1, rows):
                if a[i][j]:
                    factor = neg(a[i][j])
                    a[i] = [add(u, mul(factor, v)) for u, v in zip(a[i], a[r])]
            r += 1
        return r


def verify(q):
    f = Field(q)
    E = [tuple(int(j == i) for j in range(8)) for i in range(8)]
    counts = Counter()
    total = 0
    for x in product(range(q), repeat=8):
        columns = [f.multiply_octonion(x, e) + f.multiply_octonion(e, x) for e in E]
        nullity = 8 - f.rank(zip(*columns))
        if x == (0,) * 8:
            label, predicted = 'zero', 8
        elif f.norm(x) != 0:
            label, predicted = 'nonsingular-norm', 0
        elif f.trace(x) != 0:
            label, predicted = 'isotropic-nonzero-trace', 1
        else:
            label, predicted = 'isotropic-zero-trace', 3
        if nullity != predicted:
            raise AssertionError((q, x, label, nullity, predicted))
        counts[label] += 1
        total += q ** nullity
    predicted_counts = {
        'zero': 1,
        'nonsingular-norm': q**8-(q**7+q**4-q**3),
        'isotropic-zero-trace': q**6-1,
        'isotropic-nonzero-trace': q**7-q**6+q**4-q**3,
    }
    assert dict(counts) == predicted_counts, (q, counts, predicted_counts)
    polynomial = q**9 + 3*q**8 - 2*q**7 + q**5 - 2*q**4
    assert total == polynomial, (q, total, polynomial)
    print(f'q={q} exhaustive_first_factors={q**8} kernel_classes={dict(counts)} total={total} OK')


if __name__ == '__main__':
    for q in (2, 3, 4):
        verify(q)
    print('SPLIT_OCTONION_BIDIRECTIONAL_ZERO_PRODUCTS_OK 3 FULL_FIELDS')
