"""Exact finite-state checks for the two-anchor coordination-design result.

Run using Python 3.9+; requires only the standard library.
The infinite parameter statements are established analytically in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

PAW = [(0, 3), (1, 2), (1, 3), (2, 3)]


def weight_on_graph(edges, n, u, v):
    z = F(0)
    for bits in product((0, 1), repeat=n):
        n00 = sum(bits[a] == bits[b] == 0 for a, b in edges)
        n11 = sum(bits[a] == bits[b] == 1 for a, b in edges)
        z += u ** n00 * v ** n11
    return z


def pinned_core(edges, n, a, b, u, v):
    c = {(0, 0): F(0), (0, 1): F(0), (1, 0): F(0), (1, 1): F(0)}
    for bits in product((0, 1), repeat=n):
        n00 = sum(bits[i] == bits[j] == 0 for i, j in edges)
        n11 = sum(bits[i] == bits[j] == 1 for i, j in edges)
        c[(bits[a], bits[b])] += u ** n00 * v ** n11
    return c


def two_anchor_partition(c, L, s, u, v):
    A, B = 1 + u, 1 + v
    return (c[(0, 0)] * A ** L + c[(1, 1)] * B ** L
            + c[(0, 1)] * A ** s * B ** (L - s)
            + c[(1, 0)] * B ** s * A ** (L - s))


def H(t):
    return 2*t**6 - 2*t**4 - 9*t**3 - 5*t**2 - 3*t + 1


def check():
    tested = 0
    # This graph is the triangle on vertices 1,2,3 with a pendant vertex 0.
    # a=3 is its degree-three vertex, and b=0 its degree-one vertex.
    for t in (F(3, 2), F(2), F(3), F(4)):
        u, v = t, t*t
        c = pinned_core(PAW, 4, 3, 0, u, v)
        T0 = u**3 + 2*u + v
        T1 = v**3 + 2*v + u
        assert c[(0, 1)] == T0
        assert c[(1, 0)] == T1
        assert c[(0, 0)] == u*T0
        assert c[(1, 1)] == v*T1
        for L in (1, 2, 3, 4, 5):
            for s in range(L + 1):
                edges = PAW + [(3, 4 + i) for i in range(s)] \
                            + [(0, 4 + i) for i in range(s, L)]
                direct = weight_on_graph(edges, 4 + L, u, v)
                reduced = two_anchor_partition(c, L, s, u, v)
                assert direct == reduced, (t, L, s)
                tested += 1
        c0 = two_anchor_partition(c, 4, 0, u, v)
        c1 = two_anchor_partition(c, 4, 1, u, v)
        assert c0-c1 == -t*t*(t-1)**2*H(t)
        assert (c1 < c0) if t <= 2 else (c0 < c1)
        tested += 1
    # A distinct, non-clique core checks the general two-anchor reduction.
    ed = [(0, 1), (1, 2), (2, 3), (1, 3), (3, 4)]
    c = pinned_core(ed, 5, 1, 4, F(2), F(4))
    for s in range(4):
        edges = ed + [(1, 5+i) for i in range(s)] \
                   + [(4, 5+i) for i in range(s, 3)]
        assert weight_on_graph(edges, 8, F(2), F(4)) == two_anchor_partition(c, 3, s, F(2), F(4))
        tested += 1
    assert H(F(0)) > 0 and H(F(1)) < 0 and H(F(2)) < 0 and H(F(3)) > 0
    lo, hi = 2.0, 3.0
    for _ in range(75):
        mid = (lo + hi) / 2
        if H(mid) < 0:
            lo = mid
        else:
            hi = mid
    print('Exact partition comparisons:', tested)
    print('Unique root above 1 within:', lo, hi)
    print('All exact finite checks passed.')


if __name__ == '__main__':
    check()
