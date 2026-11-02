"""Exact rational checks of the depth-two regular-tree Hilbert distortion construction.

Usage: python verify.py
Only uses the Python standard library. The analytical proof covers all integers
r,s >= 2; finite checks here reconstruct the proposed Gram matrix independently.
"""
from fractions import Fraction as F
from math import isqrt


def model(r, s):
    assert r >= 2 and s >= 2
    a, u = F(r - 1, r), F(s - 1, s)
    t = 2 * u
    yy = 8 - t
    B = a * yy + t
    D2 = B * B / (4 * a * yy)
    xx = D2 / a
    xy = B / (2 * a)
    assert xx * yy == xy * xy, (r, s)
    # Gram data: child vectors live in the centered r-simplex coordinates;
    # leaves add orthogonal centered s-simplex coordinates in each branch.
    vertices = [('root', 0, 0)] + [('child', i, 0) for i in range(r)] + [
        ('leaf', i, j) for i in range(r) for j in range(s)]

    def gram(p, q):
        kind1, i, j = p
        kind2, k, l = q
        if kind1 == 'root' or kind2 == 'root':
            return F(0)
        h = F(int(i == k)) - F(1, r)
        if kind1 == 'child' and kind2 == 'child':
            return xx * h
        if kind1 == 'leaf' and kind2 == 'leaf':
            return yy * h + (2 * (F(int(j == l)) - F(1, s)) if i == k else 0)
        return xy * h

    def graph_distance(p, q):
        if p == q:
            return 0
        k1, i, j = p
        k2, k, l = q
        if k1 == 'root':
            return 1 if k2 == 'child' else 2
        if k2 == 'root':
            return 1 if k1 == 'child' else 2
        if k1 == 'child' and k2 == 'child':
            return 2
        if k1 == 'leaf' and k2 == 'leaf':
            return 2 if i == k else 4
        return 1 if i == k else 3

    orbit = {}
    checked = 0
    touches_low = touches_high = False
    for idx, p in enumerate(vertices):
        for q in vertices[idx+1:]:
            dist = graph_distance(p, q)
            sq = gram(p, p) + gram(q, q) - 2 * gram(p, q)
            assert F(dist * dist) <= sq <= D2 * dist * dist, (r, s, p, q, sq, D2)
            if sq == dist * dist:
                touches_low = True
            if sq == D2 * dist * dist:
                touches_high = True
            # Identical distance orbit has identical Euclidean squared length.
            if p[0] == 'root' or q[0] == 'root':
                typ = 'root-'+(q[0] if p[0]=='root' else p[0])
            elif p[0] == q[0] == 'child':
                typ = 'child-child'
            elif p[0] == q[0] == 'leaf':
                typ = 'leaf-same' if p[1] == q[1] else 'leaf-different'
            else:
                typ = 'child-ownleaf' if p[1] == q[1] else 'child-otherleaf'
            if typ in orbit:
                assert sq == orbit[typ], (r, s, typ)
            else:
                orbit[typ] = sq
            checked += 1
    assert touches_low and touches_high
    assert len(orbit) == 7, (r, s, orbit)
    assert orbit['root-child'] == D2
    assert orbit['child-ownleaf'] == D2
    assert orbit['leaf-same'] == 4
    assert orbit['leaf-different'] == 16
    return checked, D2


def main():
    cases = checks = 0
    for r in range(2, 18):
        for s in range(2, 18):
            count, D2 = model(r, s)
            cases += 1
            checks += count
            assert F(1) < D2 < F(8, 3)
            if r == s == 2:
                assert D2 == F(81, 56)
    # This limit follows by substituting a,u -> 1 into the exact formula.
    assert (F(8) * F(8)) / (4 * F(6)) == F(8, 3)
    print(f'TREE_DEPTH2_CHECK_OK cases={cases} exact_pair_inequalities={checks} binary_depth2_squared_distortion=81/56 limiting_squared_distortion=8/3')


if __name__ == '__main__':
    main()
