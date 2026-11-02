"""Exact four-round first-order types of biaffine incidence graphs.

Uses five ordered-pair orbit representatives per starting vertex, a group
symmetry of the Desarguesian examples. It is a finite verification, not a
proof for all nets; the latter uses the incidence axioms in RESULT.md.
"""
from time import monotonic


def field(q):
    if q in (2, 3, 5, 7, 11, 13):
        return lambda a, b: (a+b) % q, lambda a, b: (a*b) % q
    if q in (4, 8, 16):
        polynomial = {4: 0b111, 8: 0b1011, 16: 0b10011}[q]
        def multiply(a, b):
            result = 0
            while b:
                if b & 1:
                    result ^= a
                b >>= 1
                a <<= 1
                if a & q:
                    a ^= polynomial
            return result
        return lambda a, b: a ^ b, multiply
    if q == 9:
        def add(a, b):
            return (a%3+b%3)%3 + 3*((a//3+b//3)%3)
        def multiply(a, b):
            return (a%3*b%3-a//3*(b//3))%3 + 3*((a%3*(b//3)+a//3*(b%3))%3)
        return add, multiply
    raise ValueError(q)


def neighbors(q):
    add, multiply = field(q)
    negative = {x: next(y for y in range(q) if add(x, y) == 0) for x in range(q)}
    half = q*q
    adj = [0]*(2*half)
    for x in range(q):
        for y in range(q):
            p = x*q+y
            for m in range(q):
                b = add(y, negative[multiply(x, m)])
                l = half+m*q+b
                adj[p] |= 1 << l
                adj[l] |= 1 << p
    assert all(a.bit_count() == q for a in adj)
    return adj


def rank_four_type(q, colored):
    adj = neighbors(q)
    size = len(adj)
    half = size // 2
    universe = (1 << size) - 1
    points = (1 << half) - 1
    lines = universe ^ points

    def atomic(vertices):
        pair_data = tuple((int(vertices[i] == vertices[j]),
                           int(bool(adj[vertices[i]] & (1 << vertices[j]))))
                          for i in range(len(vertices))
                          for j in range(i+1, len(vertices)))
        return (tuple(int(x >= half) for x in vertices), pair_data) if colored else pair_data

    def triple_type(a, b, c):
        vertices = (a, b, c)
        available = universe & ~((1 << a) | (1 << b) | (1 << c))
        profiles = set()
        choices = ((0, points), (1, lines)) if colored else ((0, universe),)
        for side, side_mask in choices:
            for pattern in range(8):
                matching = available & side_mask
                for i, v in enumerate(vertices):
                    matching &= adj[v] if pattern & (1 << i) else universe & ~adj[v]
                if matching:
                    profiles.add((side, pattern) if colored else pattern)
        # Fourth choices equal to a prior selected vertex are determined by
        # the atomic diagram of the triple, and need not be stored separately.
        return atomic(vertices), frozenset(profiles)

    def pair_type(a, b):
        return atomic((a, b)), frozenset(triple_type(a, b, c) for c in range(size))

    def singleton_type(a):
        # Equal, parallel, intersecting, incident, anti-incident representatives.
        representatives = ([0, 1, q, half, half+1] if a == 0
                           else [half, half+1, half+q, 0, 1])
        return atomic((a,)), frozenset(pair_type(a, b) for b in representatives)

    return frozenset(singleton_type(a) for a in ([0, half] if colored else [0]))


def main():
    orders = (2, 3, 4, 5, 7, 8, 9, 11, 13, 16)
    raw = {q: rank_four_type(q, False) for q in orders}
    colored = {q: rank_four_type(q, True) for q in orders}
    for q in orders:
        assert (q == 2) == (raw[q] == raw[2])
        assert (q >= 3) == (raw[q] == raw[3])
        assert (q == 2) == (colored[q] == colored[2])
        assert (q == 3) == (colored[q] == colored[3])
        assert (q >= 4) == (colored[q] == colored[4])
        print('ORDER', q, 'VERTICES', 2*q*q,
              'PURE_CLASS', 0 if q == 2 else 1,
              'COLORED_CLASS', 0 if q == 2 else 1 if q == 3 else 2)
    print('RANK4_ORBIT_TYPES_OK')


if __name__ == '__main__':
    main()
