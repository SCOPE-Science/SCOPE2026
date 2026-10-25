"""Exact rational-polytope verification of a five-symbol cat-map law.

Run with Python 3 using only the standard library: python verify.py
All arithmetic determining the answer uses fractions.Fraction, not floating point.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
from math import floor

FORMS = ((1, 0), (0, 1), (-1, 3), (-3, 8), (-8, 21))
SQUARE = ((Q(0), Q(0)), (Q(1), Q(0)), (Q(1), Q(1)), (Q(0), Q(1)))


def clip(poly, a, b, c, keep_le):
    """Exact intersection of a convex polygon with a*u+b*v <=/>= c."""
    if not poly:
        return ()
    vertices = []
    old = poly[-1]
    oldval = a * old[0] + b * old[1] - c
    for new in poly:
        newval = a * new[0] + b * new[1] - c
        oldok = oldval <= 0 if keep_le else oldval >= 0
        newok = newval <= 0 if keep_le else newval >= 0
        if oldok != newok:
            t = oldval / (oldval - newval)
            vertices.append((old[0] + t * (new[0] - old[0]),
                             old[1] + t * (new[1] - old[1])))
        if newok:
            vertices.append(new)
        old, oldval = new, newval
    return tuple(v for j, v in enumerate(vertices)
                 if j == 0 or v != vertices[j - 1])


def area(poly):
    if len(poly) < 3:
        return Q(0)
    return abs(sum(a[0] * b[1] - b[0] * a[1]
                   for a, b in zip(poly, poly[1:] + poly[:1]))) / 2


def exact_partition(forms):
    """Return probabilities of every sign word, with all boundary cuts exact.

    The interiors of the output polygons are disjoint and cover the square:
    each refinement intersects a polygon with all strips
    k <= 2(a*u+b*v) <= k+1 that can meet its interior.
    """
    states = [(SQUARE, ())]
    polygon_counts = []
    for a, b in forms:
        refined = []
        for polygon, word in states:
            vals = [2 * (a * x + b * y) for x, y in polygon]
            for k in range(floor(min(vals)), floor(max(vals)) + 1):
                cut = clip(polygon, 2 * a, 2 * b, Q(k), False)
                cut = clip(cut, 2 * a, 2 * b, Q(k + 1), True)
                if len(cut) >= 3 and area(cut) > 0:
                    refined.append((cut, word + ((1 if k % 2 == 0 else -1),)))
        states = refined
        assert sum(area(poly) for poly, _ in states) == 1
        polygon_counts.append(len(states))
    table = defaultdict(lambda: Q(0))
    for polygon, word in states:
        table[word] += area(polygon)
    return dict(table), polygon_counts


def validate_symmetry():
    # Half-lattice translations kill all nonempty moments whose vector
    # sum mod 2 is nonzero. Global inversion kills every odd moment.
    assert [tuple(t % 2 for t in form) for form in FORMS] == [
        (1, 0), (0, 1), (1, 1), (1, 0), (0, 1)]
    for m in range(1, 6):
        for inds in combinations(range(5), m):
            parity = tuple(sum(FORMS[j][axis] for j in inds) % 2
                           for axis in range(2))
            if m == 4 and inds == (0, 1, 3, 4):
                assert parity == (0, 0)
            elif m % 2 == 0 and m != 0:
                # All other 4-subsets (but not necessarily all pairs)
                # are killed by half-translation, unless m=2.
                if m == 4:
                    assert parity != (0, 0)
    # Pairwise independence is from the surjective torus homomorphism
    # defined by any two nonparallel integer linear forms.
    for i, j in combinations(range(5), 2):
        a, b = FORMS[i]
        c, d = FORMS[j]
        assert a * d - b * c != 0


def run():
    validate_symmetry()
    law, counts = exact_partition(FORMS)
    assert counts == [2, 4, 16, 56, 168], counts
    assert len(law) == 32 and sum(law.values()) == 1
    for word in product((-1, 1), repeat=5):
        product4 = word[0] * word[1] * word[3] * word[4]
        expected = (Q(1) + Q(product4, 21)) / 32
        assert law[word] == expected, (word, law[word], expected)
    assert {v for v in law.values()} == {Q(11, 336), Q(5, 168)}
    assert sum(Q(word[0] * word[1] * word[3] * word[4]) * prob
               for word, prob in law.items()) == Q(1, 21)
    # Independent partition of just the exceptional four time positions:
    law4, counts4 = exact_partition((FORMS[0], FORMS[1], FORMS[3], FORMS[4]))
    assert counts4 == [2, 4, 44, 156], counts4
    assert sum(Q(word[0] * word[1] * word[2] * word[3]) * prob
               for word, prob in law4.items()) == Q(1, 21)
    # Marginalize the full five-block certificate over any four consecutive
    # positions and verify exact, not approximate, fair independence.
    for start in (0, 1):
        for subword in product((-1, 1), repeat=4):
            assert sum(prob for word, prob in law.items()
                       if word[start:start+4] == subword) == Q(1, 16)
    print("VERIFY_OK: exact five-block distribution for all 32 words;")
    print("conditional fourth-order moment 1/21; all four-block marginals iid;")
    print("exact rational polygon counts full=[2,4,16,56,168], four=[2,4,44,156];")
    print("positive pattern mass 11/336 and negative pattern mass 5/168.")


if __name__ == "__main__":
    run()
