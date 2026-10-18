#!/usr/bin/env python3
"""Independent, exact finite checks for star-sphere retractions in N(L(K_n)).

Uses only the Python standard library. The infinite-family proof is mathematical;
the tested finite instances are consistency checks, not its logical substitute.
"""
from itertools import combinations


def edges(n):
    return list(combinations(range(n), 2))


def neighborhoods(n):
    ee = edges(n)
    return [frozenset(f for f in ee if f != e and len(set(e) & set(f)) == 1)
            for e in ee]


def retraction(n, i):
    remainder = [a for a in range(n) if a != i]
    anchors = tuple(remainder[:3])
    assert len(anchors) == 3
    def f(e):
        if i in e:
            return e
        c = next(c for c in anchors if c not in e)
        return tuple(sorted((i, c)))
    return f


def verify_retractions(n):
    ee = edges(n)
    facets = neighborhoods(n)
    assert len(facets) == len(ee)
    for i in range(n):
        spokes = frozenset(e for e in ee if i in e)
        assert len(spokes) == n - 1
        f = retraction(n, i)
        # All faces map into the proper-subset boundary of the spoke simplex.
        for facet in facets:
            images = frozenset(f(e) for e in facet)
            assert images < spokes
        # Every proper spoke subset is a face, the full spoke set is not.
        for omission in spokes:
            assert any((spokes - {omission}) <= facet for facet in facets)
        assert not any(spokes <= facet for facet in facets)
        assert all(f(e) == e for e in spokes)
        for j in range(n):
            if j == i:
                continue
            other = frozenset(e for e in ee if j in e)
            image = frozenset(f(e) for e in other)
            # The other fundamental sphere lands in a simplex of <=4 vertices.
            assert len(image) <= 4 < n - 1
            assert any(image <= facet for facet in facets)
    return True


def faces_by_cardinality(n):
    by_k = {}
    for facet in neighborhoods(n):
        ff = sorted(facet)
        for k in range(1, len(ff) + 1):
            by_k.setdefault(k, set()).update(
                tuple(c) for c in combinations(ff, k))
    return {k: sorted(v) for k, v in by_k.items()}


def boundary_binary_basis(upper, lower, lowest_pivot=False):
    index = {s: j for j, s in enumerate(lower)}
    pivots = {}
    for simplex in upper:
        col = 0
        for t in range(len(simplex)):
            col ^= 1 << index[simplex[:t] + simplex[t + 1:]]
        while col:
            p = (col & -col).bit_length() - 1 if lowest_pivot else col.bit_length() - 1
            if p in pivots:
                col ^= pivots[p]
            else:
                pivots[p] = col
                break
    return pivots


def verify_seven():
    F = faces_by_cardinality(7)
    assert [len(F[k]) for k in sorted(F)] == [
        21, 210, 1190, 3780, 5187, 4410, 2520, 945, 210, 21]
    b4 = boundary_binary_basis(F[5], F[4])
    b5 = boundary_binary_basis(F[6], F[5])
    # Verify exact ranks again with the opposite pivot convention.
    assert len(boundary_binary_basis(F[5], F[4], True)) == len(b4)
    assert len(boundary_binary_basis(F[6], F[5], True)) == len(b5)
    assert (len(b4), len(b5)) == (2534, 2646)
    assert len(F[5]) - len(b4) - len(b5) == 7
    # Independently verify that the seven spoke boundaries survive modulo 2.
    F4index = {s: j for j, s in enumerate(F[5])}
    basis = dict(b5)
    ee = edges(7)
    for i in range(7):
        spokes = tuple(sorted(e for e in ee if i in e))
        chain = 0
        for j in range(len(spokes)):
            face = spokes[:j] + spokes[j+1:]
            chain ^= 1 << F4index[face]
        while chain:
            p = chain.bit_length() - 1
            if p in basis:
                chain ^= basis[p]
            else:
                basis[p] = chain
                break
        assert len(basis) == len(b5) + i + 1
    return len(F[5]), len(b4), len(b5), len(basis)-len(b5)


def sign(seq):
    inversions = sum(a > b for i, a in enumerate(seq) for b in seq[i+1:])
    return (-1) ** inversions


def verify_orientation(n):
    perms = []
    for i in range(n - 1):
        p = list(range(n))
        p[i], p[i+1] = p[i+1], p[i]
        perms.append(p)
    perms.append(list(range(1, n)) + [0])
    for p in perms:
        for i in range(n):
            image_order = [p[j] for j in range(n) if j != i]
            degree = sign(image_order)
            assert degree == sign(p) * ((-1) ** (i + p[i]))
    return len(perms) * n


def main():
    for n in range(7, 12):
        assert verify_retractions(n)
    f4, r4, r5, rank = verify_seven()
    assert verify_orientation(7) == 49
    print("Simplicial retractions and off-diagonal null maps: PASS for n=7..11")
    print("Signed S_7 star-boundary action: PASS for seven generating permutations")
    print("T_7: C_4 = %d, rank(d_4 mod 2) = %d, rank(d_5 mod 2) = %d" %
          (f4, r4, r5))
    print("T_7: dim H_4(F_2) = 7; independent star classes = %d" % rank)


if __name__ == '__main__':
    main()
