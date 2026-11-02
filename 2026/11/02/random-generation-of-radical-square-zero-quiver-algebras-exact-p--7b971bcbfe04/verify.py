"""Direct enumeration of small finite quiver algebras and their generating tuples.

Uses multiplication closure rather than the structural criterion in the theorem.
All arithmetic and all test cases are self-contained.
"""
from itertools import product
from math import prod


class Field:
    def __init__(self, q):
        assert q in (2, 3, 4)
        self.q = q

    def add(self, x, y):
        return (x ^ y) if self.q == 4 else (x + y) % self.q

    def neg(self, x):
        return x if self.q == 4 else (-x) % self.q

    def mul(self, x, y):
        if self.q != 4:
            return (x * y) % self.q
        # F_4 = F_2[t]/(t^2+t+1), with 2 representing t.
        p = 0
        for i in range(2):
            for j in range(2):
                if (x >> i) & (y >> j) & 1:
                    p ^= 1 << (i + j)
        if p & 8:
            p ^= 0b1110
        if p & 4:
            p ^= 0b111
        return p

    def inv(self, x):
        assert x
        return next(y for y in range(1, self.q) if self.mul(x, y) == 1)


def rank(rows, field):
    if not rows:
        return 0
    a = [list(row) for row in rows]
    r = 0
    for col in range(len(a[0])):
        pivot = next((j for j in range(r, len(a)) if a[j][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = field.inv(a[r][col])
        a[r] = [field.mul(inv, x) for x in a[r]]
        for j in range(len(a)):
            if j != r and a[j][col]:
                c = a[j][col]
                a[j] = [field.add(x, field.neg(field.mul(c, y)))
                        for x, y in zip(a[j], a[r])]
        r += 1
    return r


def multiplication(x, y, vertices, arrows, field):
    out = [field.mul(x[i], y[i]) for i in range(vertices)]
    for t, (u, w) in enumerate(arrows):
        out.append(field.add(field.mul(x[u], y[vertices + t]),
                             field.mul(x[vertices + t], y[w])))
    return tuple(out)


def generates(elements, vertices, arrows, field):
    dim = vertices + len(arrows)
    identity = tuple([1] * vertices + [0] * len(arrows))
    basis = [identity]
    for x in elements:
        if rank(basis + [x], field) > len(basis):
            basis.append(x)
    while True:
        extra = []
        for b in basis:
            for x in elements:
                for z in (multiplication(b, x, vertices, arrows, field),
                          multiplication(x, b, vertices, arrows, field)):
                    if rank(basis + extra + [z], field) > len(basis) + len(extra):
                        extra.append(z)
        if not extra:
            return len(basis) == dim
        basis.extend(extra)


def predicted_count(vertices, arrows, q, k):
    multiplicities = {}
    for u, w in arrows:
        multiplicities[u, w] = multiplicities.get((u, w), 0) + 1
    result = prod(q ** k - i for i in range(vertices))
    for (u, w), r in multiplicities.items():
        if u == w:
            result *= prod(q ** k - q ** j for j in range(r))
        else:
            result *= q ** r * prod(q ** (k - 1) - q ** j for j in range(r))
    return result


def run():
    cases = [
        (1, [], 2, 1), (1, [(0, 0)], 2, 1),
        (1, [(0, 0), (0, 0)], 2, 2),
        (2, [], 2, 1), (2, [(0, 1)], 2, 1),
        (2, [(0, 1)], 2, 2), (2, [(0, 1), (0, 1)], 2, 2),
        (2, [(0, 1), (0, 1)], 2, 3),
        (2, [(0, 1), (1, 0)], 2, 2),
        (2, [(0, 0), (1, 1)], 2, 2),
        (2, [(0, 0), (0, 1)], 2, 2),
        (2, [(0, 0), (1, 1), (0, 1)], 2, 2),
        (2, [(0, 0), (0, 1), (1, 0)], 2, 2),
        (3, [(0, 1), (1, 2)], 2, 2),
        (3, [(0, 1), (1, 2)], 2, 3),
        (2, [(0, 1)], 3, 2), (2, [(0, 0)], 3, 2),
        (2, [(0, 1)], 4, 2), (2, [(0, 0)], 4, 2),
    ]
    for vertices, arrows, q, k in cases:
        field = Field(q)
        dim = vertices + len(arrows)
        all_elements = product(range(q), repeat=dim)
        total = sum(generates(elems, vertices, arrows, field)
                    for elems in product(all_elements, repeat=k))
        wanted = predicted_count(vertices, arrows, q, k)
        assert total == wanted, (vertices, arrows, q, k, total, wanted)
    print('VERIFY_OK', len(cases), 'exhaustive finite-field cases')


if __name__ == '__main__':
    run()
