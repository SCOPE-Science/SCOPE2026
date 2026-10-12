"""Independent finite-field verification for simultaneous incidence idempotents.

Run: python3 checker.py
No external dependencies. All field operations and incidence matrices are explicit.
"""
from itertools import product
from collections import Counter


def field(q):
    assert q in (2, 3, 4)
    if q != 4:
        add = lambda a, b: (a + b) % q
        mul = lambda a, b: (a * b) % q
    else:
        add = lambda a, b: a ^ b
        def mul(a, b):
            out = 0
            for i in range(2):
                for j in range(2):
                    if ((a >> i) & 1) and ((b >> j) & 1):
                        out ^= 1 << (i + j)
            if out & 4:
                out ^= 7  # t^2=t+1 modulo t^2+t+1
            return out
    return add, mul


def closure(n, edges):
    R = [[i == j for j in range(n)] for i in range(n)]
    for i, j in edges:
        R[i][j] = True
    for h in range(n):
        for i in range(n):
            for j in range(n):
                R[i][j] |= R[i][h] and R[h][j]
    return R


class Algebra:
    def __init__(self, n, edges, q):
        self.n, self.q = n, q
        self.add, self.mulfield = field(q)
        R = closure(n, edges)
        self.ints = [(i, j) for i in range(n) for j in range(i, n) if R[i][j]]
        self.loc = {p: s for s, p in enumerate(self.ints)}
        self.D = len(self.ints)
        self.pairs = [(i, j) for i, j in self.ints if i != j]
        self.product_keys = [
            [(self.loc[i, h], self.loc[h, j]) for h in range(i, j + 1)
             if (i, h) in self.loc and (h, j) in self.loc]
            for i, j in self.ints
        ]
        self.zero = (0,) * self.D
        self.one = tuple(1 if i == j else 0 for i, j in self.ints)

    def addmat(self, a, b):
        return tuple(self.add(x, y) for x, y in zip(a, b))

    def prod(self, a, b):
        return tuple(self._dot(a, b, ks) for ks in self.product_keys)

    def _dot(self, a, b, ks):
        val = 0
        for u, v in ks:
            val = self.add(val, self.mulfield(a[u], b[v]))
        return val

    def inverse_unipotent(self, u):
        # (1+z)^-1 = 1-z+z^2-... for nilpotent z.
        neg = (lambda a: (-a) % self.q) if self.q != 4 else (lambda a: a)
        z = tuple(self.add(u[i], neg(self.one[i])) for i in range(self.D))
        negz = tuple(neg(x) for x in z)
        inv = self.one
        powz = self.one
        for _ in range(1, self.n):
            powz = self.prod(powz, negz)
            inv = self.addmat(inv, powz)
        assert self.prod(u, inv) == self.one
        return inv

    def diag(self, vals):
        return tuple(vals[i] if i == j else 0 for i, j in self.ints)

    def commuting_idempotents_brute(self, k):
        universe = product(range(self.q), repeat=self.D)
        ids = [a for a in universe if self.prod(a, a) == a]
        result = set()
        for aa in product(ids, repeat=k):
            if all(self.prod(aa[i], aa[j]) == self.prod(aa[j], aa[i])
                   for i in range(k) for j in range(i + 1, k)):
                result.add(aa)
        return ids, result

    def chart_enumeration(self, k):
        result = set()
        ranks = Counter()
        for colors in product(range(1 << k), repeat=self.n):
            indexes = [self.loc[i, j] for i, j in self.pairs
                       if colors[i] != colors[j]]
            d = len(indexes)
            diag = [self.diag(tuple((c >> h) & 1 for c in colors)) for h in range(k)]
            for vals in product(range(self.q), repeat=d):
                u = list(self.one)
                for index, val in zip(indexes, vals):
                    u[index] = val
                u = tuple(u)
                inv = self.inverse_unipotent(u)
                tup = tuple(self.prod(self.prod(u, dh), inv) for dh in diag)
                assert all(self.prod(e, e) == e for e in tup)
                assert all(self.prod(tup[i], tup[j]) == self.prod(tup[j], tup[i])
                           for i in range(k) for j in range(i + 1, k))
                assert tup not in result, 'non-unique canonical chart'
                result.add(tup)
                ranks[tuple(sum((c >> h) & 1 for c in colors)
                            for h in range(k))] += 1
        return result, ranks

    def formula(self, k):
        ranks = Counter()
        for colors in product(range(1 << k), repeat=self.n):
            d = sum(colors[i] != colors[j] for i, j in self.pairs)
            ranks[tuple(sum((c >> h) & 1 for c in colors)
                        for h in range(k))] += self.q ** d
        return ranks


def fk_weighted_edge_subset(A, k):
    # Independent Fortuin--Kasteleyn edge-subset evaluation, with integral weights.
    m = len(A.pairs)
    total = 0
    for flags in product((0, 1), repeat=m):
        par = list(range(A.n))
        def root(x):
            while par[x] != x:
                x = par[x]
            return x
        for (i, j), selected in zip(A.pairs, flags):
            if selected:
                par[root(i)] = root(j)
        cc = len({root(x) for x in range(A.n)})
        z = sum(flags)
        total += (A.q ** (m-z)) * ((1-A.q) ** z) * ((1<<k) ** cc)
    return total


def check(name, n, edges, q, k):
    A = Algebra(n, edges, q)
    ids, brute = A.commuting_idempotents_brute(k)
    generated, rank_counts = A.chart_enumeration(k)
    expected = A.formula(k)
    assert brute == generated
    assert rank_counts == expected
    assert len(brute) == fk_weighted_edge_subset(A, k)
    print(name, q, k, 'idempotents', len(ids), 'tuples', len(brute))


if __name__ == '__main__':
    cases = [
        ('chain2', 2, [(0, 1)], 2, 3),
        ('chain2', 2, [(0, 1)], 3, 2),
        ('chain2', 2, [(0, 1)], 4, 2),
        ('chain3', 3, [(0, 1), (1, 2)], 2, 2),
        ('chain3', 3, [(0, 1), (1, 2)], 3, 2),
        ('fork', 3, [(0, 1), (0, 2)], 2, 2),
        ('fork', 3, [(0, 1), (0, 2)], 3, 2),
        ('diamond', 4, [(0, 1), (0, 2), (1, 3), (2, 3)], 2, 2),
        ('antichain', 3, [], 2, 2),
    ]
    for args in cases:
        check(*args)
    print('VERIFY_OK')
