"""Exact finite checks for normal-cone angle formulas of cubical binary nestohedra.

Only uses Python's standard library. Run: python VERIFY.py
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import factorial


@lru_cache(None)
def shapes(n):
    if n == 1:
        return (None,)
    return tuple((left, right) for a in range(1, n)
                 for left in shapes(a) for right in shapes(n-a))


def nleaves(t):
    return 1 if t is None or isinstance(t, int) else nleaves(t[0]) + nleaves(t[1])


def label(t, base=0):
    if t is None:
        return base
    left, right = t
    return label(left, base), label(right, base + nleaves(left))


def support(t, scores, w_rule):
    if isinstance(t, int):
        return t, (), (0,) * len(scores), 0
    wa, ba, xa, ha = support(t[0], scores, w_rule)
    wb, bb, xb, hb = support(t[1], scores, w_rule)
    bit = 0 if scores[wa] > scores[wb] else 1
    win = wa if bit == 0 else wb
    weight = w_rule(t)
    x = list(map(sum, zip(xa, xb)))
    x[win] += weight
    return win, (bit, ba, bb), tuple(x), ha + hb + weight * scores[win]


def probabilities(t):
    if isinstance(t, int):
        return {(): Fraction(1)}
    left, right = t
    pl, pr = probabilities(left), probabilities(right)
    a, b = nleaves(left), nleaves(right)
    out = {}
    for il, al in pl.items():
        for ir, ar in pr.items():
            out[(0, il, ir)] = Fraction(a, a+b) * al * ar
            out[(1, il, ir)] = Fraction(b, a+b) * al * ar
    return out


def collision(t):
    if isinstance(t, int):
        return Fraction(1)
    left, right = t
    a, b = nleaves(left), nleaves(right)
    return (Fraction(a*a+b*b, (a+b)*(a+b)) *
            collision(left) * collision(right))


def perfect(k):
    if k == 0:
        return None
    return (perfect(k-1), perfect(k-1))


def leaves(t):
    if isinstance(t, int):
        return (t,)
    return leaves(t[0]) + leaves(t[1])


def internal(t):
    if isinstance(t, int):
        return ()
    return (t,) + internal(t[0]) + internal(t[1])


for n in range(2, 7):
    for shape in shapes(n):
        t = label(shape)
        p = probabilities(t)
        counts = Counter()
        signature_to_vertex = {}
        vertices = set()
        for perm in permutations(range(n)):
            # Uniform random permutation ranks reproduce isotropic Gaussian ranks.
            _, signature, vertex, value = support(t, perm,
                      lambda node: 1 + (nleaves(node) % 3))
            assert value == sum((1 + (nleaves(node) % 3)) *
                                max(perm[i] for i in leaves(node))
                                for node in internal(t))
            counts[signature] += 1
            if signature in signature_to_vertex:
                assert signature_to_vertex[signature] == vertex
            else:
                signature_to_vertex[signature] = vertex
                vertices.add(vertex)
        assert len(counts) == len(vertices) == 2 ** (n-1)
        assert all(Fraction(counts[sig], factorial(n)) == p[sig]
                   for sig in p)
        assert sum((v*v for v in p.values()), Fraction(0)) == collision(t)
    print('exhaustive rank and vertex checks passed:', n, 'leaves,',
          len(shapes(n)), 'plane tree shapes')


for n in range(2, 9):
    vals = [(collision(label(sh)), sh) for sh in shapes(n)]
    for c, sh in vals:
        excess = c * 2 ** (n-1)
        assert excess == 1 or excess >= Fraction(10, 9)
        if excess == 1:
            assert n & (n-1) == 0
        if excess == Fraction(10, 9):
            assert n % 3 == 0 and (n//3) & (n//3-1) == 0
    if n == 6:
        smallest = min(c for c, sh in vals)
        assert smallest == Fraction(5, 144)
        assert all((nleaves(sh[0]), nleaves(sh[1])) in {(2, 4), (4, 2)}
                   for c, sh in vals if c == smallest)
    print('all-tree angle-gap check passed:', n, 'leaves')


def dyadic_graft(t, depth):
    if t is None:
        return perfect(depth)
    return dyadic_graft(t[0], depth), dyadic_graft(t[1], depth)


dyadic = ((None, None), ((None, None), (None, None)))
root_balanced = ((None, (None, None)), (None, (None, None)))
for depth in range(6):
    a = collision(label(dyadic_graft(dyadic, depth)))
    b = collision(label(dyadic_graft(root_balanced, depth)))
    n = 6 * 2 ** depth
    assert a == Fraction(10, 9) * Fraction(1, 2 ** (n-1))
    assert b == Fraction(100, 81) * Fraction(1, 2 ** (n-1))
    assert b/a == Fraction(10, 9)
print('dyadic equality and comparison checks passed')
print('ALL VERIFICATIONS PASSED')
