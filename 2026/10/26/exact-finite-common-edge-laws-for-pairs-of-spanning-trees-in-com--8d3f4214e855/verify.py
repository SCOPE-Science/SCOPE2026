"""Reproduce the finite exact checks for the common-edge law on K_{3,n}.

Only the Python standard library is required. This tests, rather than replaces,
the general core-decomposition proof.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations


def add(a, b):
    c = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return c


def mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def power(a, n):
    ans = [F(1)]
    for _ in range(n):
        ans = mul(ans, a)
    return ans


def times(c, a):
    return [c * x for x in a]


def shift(a, k):
    return [F(0)] * k + list(a)


def law(n):
    """Exact coefficients of E[t^X], independently of tree enumeration."""
    assert n >= 4
    p, q = [F(2, 3), F(1, 3)], [F(1, 3), F(2, 3)]
    p2, q2 = power(p, 2), power(q, 2)
    middle = mul(p2, add(add([F(0), F(0), F(1)],
                             times(4, shift(q, 2))),
                         times(F(1, 3), [0, 0, 3, 2, 1])))
    # Here middle = p^2 [t^2 + 4t^2q + (t^4+2t^3+3t^2)/3].
    pieces = [
        times((n-1)*(n-2)*(n-3), power(q, 4)),
        times(F(2*(n-1)*(n-2), 3), mul([F(0), F(7), F(2)], mul(q2, p))),
        times(n-1, middle),
        mul(shift(power(p, 3), 3), [F(1)]),
    ]
    poly = []
    for x in pieces:
        poly = add(poly, x)
    poly = times(F(1, n**3), poly)
    return mul(power(p, n-4), poly)


def trees(n):
    """Direct spanning-tree enumeration, with no reference to the formula."""
    edges = [(i, 3+j) for i in range(3) for j in range(n)]
    out = []
    for pick in combinations(range(3*n), n+2):
        parent = list(range(3+n))
        def root(i):
            while parent[i] != i:
                i = parent[i]
            return i
        for e in pick:
            i, j = edges[e]
            ri, rj = root(i), root(j)
            if ri == rj:
                break
            parent[ri] = rj
        else:
            out.append(sum(1 << j for j in pick))
    return out


def main():
    total_pairs = 0
    for n in (4, 5):
        ts = trees(n)
        assert len(ts) == n*n*3**(n-1)
        counts = Counter((s & t).bit_count() for s in ts for t in ts)
        total_pairs += len(ts)**2
        expected = law(n)
        observed = [F(counts[k], len(ts)**2) for k in range(len(expected))]
        assert observed == expected, (n, observed, expected)
        disjoint = 9*n*(n-1)*(n-2)*(n-3)*6**(n-4)
        assert counts[0] == disjoint
        print('EXHAUSTIVE_OK', 'n=', n, 'trees=', len(ts), 'pairs=', len(ts)**2,
              'intersection_counts=', dict(sorted(counts.items())))
    for n in range(4, 41):
        f = law(n)
        assert sum(f) == 1 and all(x >= 0 for x in f)
        assert sum(i*x for i, x in enumerate(f)) == F((n+2)**2, 3*n)
        mean = sum(i*x for i, x in enumerate(f))
        assert sum((i-mean)**2*x for i, x in enumerate(f)) == F(2*(n-1)*(n*n+n+1), 9*n*n)
        assert f[0] == F((n-1)*(n-2)*(n-3), 81*n**3) * F(2, 3)**(n-4)
    print('VERIFY_OK', 'exhaustive_pairs=', total_pairs, 'additional_rational_laws=', 37)


if __name__ == '__main__':
    main()
