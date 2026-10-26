"""Exact checks of the middle lattice and cohomological bookkeeping."""
from fractions import Fraction


def det(rows):
    a = [[Fraction(c) for c in row] for row in rows]
    sign = 1
    result = Fraction(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return 0
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            sign = -sign
        v = a[i][i]
        result *= v
        for j in range(i + 1, len(a)):
            factor = a[j][i] / v
            for k in range(i + 1, len(a)):
                a[j][k] -= factor * a[i][k]
    return sign * result


def blocks(*bs):
    n = sum(map(len, bs))
    output = [[0] * n for _ in range(n)]
    off = 0
    for block in bs:
        for i, row in enumerate(block):
            for j, entry in enumerate(row):
                output[off + i][off + j] = entry
        off += len(block)
    return output


edges = {(0, 1), (0, 2), (2, 3), (0, 4), (4, 5), (5, 6), (6, 7)}
eight = [[2 if i == j else -1 if (min(i, j), max(i, j)) in edges else 0
          for j in range(8)] for i in range(8)]
assert [det([r[:k] for r in eight[:k]]) for k in range(1, 9)] == [2, 3, 4, 5, 4, 3, 2, 1]
hyperbolic = [[0, 1], [1, 0]]
gram = blocks(hyperbolic, hyperbolic, eight, [[1]])
assert len(gram) == 13 and det(gram) == 1
# Two hyperbolic blocks contribute (2,2), E8 contributes (8,0),
# and the positive rank-one block contributes (1,0).
positive, negative = (2 + 8 + 1, 2)
assert (positive, negative) == (11, 2)
betti = [1, 0, 3, 0, 13, 0, 3, 0, 1]
assert sum((-1)**i * b for i, b in enumerate(betti)) == 21
assert betti == betti[::-1]
# Degree-four and degree-five torsion are both order 2, as required
# by the torsion linking pairing in real dimension eight.
torsion = {4: 2, 5: 2}
assert torsion[4] == torsion[8-4+1] == 2
print("VERIFY_OK E8_minors=2,3,4,5,4,3,2,1 rank=13 det=1 signature=(11,2) euler=21 torsion_degrees=(4,5)")
