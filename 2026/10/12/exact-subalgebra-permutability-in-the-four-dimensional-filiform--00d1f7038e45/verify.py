#!/usr/bin/env python3
"""Independent finite-field subspace enumeration for a four-dimensional filiform Lie algebra.

Standard basis: x, y, z, w with [x,y]=z and [x,z]=w.
No external packages are required. Tests include the non-prime field of order four.
"""
from collections import Counter
from itertools import combinations, product

class Field:
    def __init__(self, size):
        assert size in (2, 3, 4, 5, 7)
        self.size = size

    def add(self, a, b):
        return a ^ b if self.size == 4 else (a + b) % self.size

    def neg(self, a):
        return a if self.size == 4 else (-a) % self.size

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        if self.size != 4:
            return (a * b) % self.size
        c = 0
        for i in range(2):
            for j in range(2):
                if ((a >> i) & (b >> j) & 1):
                    c ^= 1 << (i + j)
        if c & 8:
            c ^= 0b1110  # X^3 = X^2 + X in GF(2)[X]/(X^2+X+1)
        if c & 4:
            c ^= 0b111  # X^2 = X+1
        return c

    def inv(self, a):
        assert a != 0
        return next(b for b in range(1, self.size) if self.mul(a, b) == 1)


def rank(rows, F):
    a = [list(row) for row in rows if any(row)]
    r = 0
    for j in range(4):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        u = F.inv(a[r][j]); a[r] = [F.mul(u, x) for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][j]:
                c = a[i][j]
                a[i] = [F.sub(a[i][k], F.mul(c, a[r][k])) for k in range(4)]
        r += 1
        if r == len(a):
            break
    return r


def bracket(a, b, F):
    return (0, 0, F.sub(F.mul(a[0], b[1]), F.mul(a[1], b[0])),
            F.sub(F.mul(a[0], b[2]), F.mul(a[2], b[0])))


def subalgebras(F):
    spaces = []
    q = F.size
    for k in range(5):
        for pivots in combinations(range(4), k):
            free = [(i, j) for i in range(k)
                    for j in range(pivots[i]+1, 4) if j not in pivots]
            for values in product(range(q), repeat=len(free)):
                matrix = [[int(j == pivots[i]) for j in range(4)] for i in range(k)]
                for (i,j), val in zip(free, values):
                    matrix[i][j] = val
                if all(rank(matrix+[bracket(matrix[i], matrix[j], F)], F) == k
                       for i in range(k) for j in range(i)):
                    spaces.append(tuple(map(tuple, matrix)))
    return spaces


def label(space, F):
    qrank = rank([(v[0], v[1], 0, 0) for v in space], F)
    k = len(space)
    if qrank == 1:
        leader = next(v for v in space if v[0] or v[1])
        return ('X' if leader[0] else 'Y') + str(k-1)
    if qrank == 0 and k == 1:
        return 'Z1other' if space[0][2] else 'Z1center'
    return 'Z' + str(k) if qrank == 0 else 'whole'


def expected_failures(q):
    d = Counter()
    for a,b,c in [
        ('X0','X0',q**4*(q*q-1)),
        ('X0','X1',q**4*(q-1)),
        ('X1','X0',q**4*(q-1)),
        ('X1','X1',q**3*(q-1)),
        ('X0','Y0',q**5), ('Y0','X0',q**5),
        ('X0','Y1',q**4*(q+1)), ('Y1','X0',q**4*(q+1)),
        ('X1','Y0',q**4), ('Y0','X1',q**4),
        ('X1','Y1',q**3), ('Y1','X1',q**3),
        ('X0','Z1other',q**4), ('Z1other','X0',q**4),
    ]:
        d[(a,b)] = c
    return d


def verify(q):
    F = Field(q)
    for a in range(1, q):
        assert all(F.mul(a, F.add(b,c)) == F.add(F.mul(a,b),F.mul(a,c))
                   for b in range(q) for c in range(q))
    spaces = subalgebras(F)
    s = q**3+3*q*q+3*q+5
    assert len(spaces) == s, (q, len(spaces), s)
    fails = Counter()
    labels = [label(space,F) for space in spaces]
    for i,A in enumerate(spaces):
        for j,B in enumerate(spaces):
            sum_basis = list(A+B)
            r = rank(sum_basis,F)
            if any(rank(sum_basis+[bracket(u,v,F)],F) != r for u in A for v in B):
                fails[(labels[i], labels[j])] += 1
    assert fails == expected_failures(q), (q, fails, expected_failures(q))
    non = q**3*(q**3+6*q*q+4*q+1)
    assert sum(fails.values()) == non
    commute = 11*q**4+27*q**3+39*q*q+30*q+25
    assert len(spaces)**2 - sum(fails.values()) == commute
    print(f'q={q} subalgebras={s} nonpermutable_ordered={non} permutable_ordered={commute}')


if __name__ == '__main__':
    for order in (2,3,4,5,7):
        verify(order)
    print('VERIFY_OK')
