"""Exact cellular verification of the D5 quotient of Hom(C5,K4).

Run: python verify_pentagon_four_color_quotient.py
Requires: sympy. Cells are products of simplices with the standard
lexicographic orientation on each factor. All calculations are integral.
"""
from collections import Counter, defaultdict
from itertools import product
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

N = 5
Q = 4

# Every D5 element acts on the *positions*, leaving the colors untouched.
perms = []
for a in range(N):
    for b in (1, -1):
        p = tuple((a + b * i) % N for i in range(N))
        if p not in perms:
            perms.append(p)
assert len(perms) == 10


def act(cell, p):
    ans = [None] * N
    for i in range(N):
        ans[p[i]] = cell[i]
    return tuple(ans)


def action_sign(cell, p):
    """Koszul sign from permuting simplex-product factors."""
    d = [x.bit_count() - 1 for x in cell]
    swaps = sum(d[i] * d[j] for i in range(N)
                for j in range(i + 1, N) if p[i] > p[j])
    return -1 if swaps & 1 else 1


def boundary(cell):
    result = defaultdict(int)
    shift = 0
    for i, mask in enumerate(cell):
        colors = [a for a in range(Q) if mask & (1 << a)]
        if len(colors) > 1:
            for j, col in enumerate(colors):
                face = list(cell)
                face[i] &= ~(1 << col)
                result[tuple(face)] += (-1) ** (shift + j)
        shift += len(colors) - 1
    return {c: a for c, a in result.items() if a}


cells = [c for c in product(range(1, 1 << Q), repeat=N)
         if all(not (c[i] & c[(i + 1) % N]) for i in range(N))]
by_dimension = defaultdict(list)
for c in cells:
    by_dimension[sum(m.bit_count() - 1 for m in c)].append(c)
assert sorted(by_dimension) == [0, 1, 2, 3]
assert tuple(map(lambda d: len(by_dimension[d]), range(4))) == (240, 780, 840, 300)

# There is no cell with nontrivial dihedral stabilizer.
for c in cells:
    assert len({act(c, p) for p in perms}) == 10

# Verify the orientation rule is an actual group action on cellular chains.
for c in cells:
    for p in perms:
        gc = act(c, p)
        gsign = action_sign(c, p)
        left = {f: gsign * k for f, k in boundary(gc).items()}
        right = defaultdict(int)
        for f, k in boundary(c).items():
            right[act(f, p)] += k * action_sign(f, p)
        assert left == {f: k for f, k in right.items() if k}, (c, p)


def canonical(cell):
    options = sorted((act(cell, p), action_sign(cell, p)) for p in perms)
    assert len({x for x, _ in options}) == 10
    return options[0]


representatives = {
    d: sorted({canonical(c)[0] for c in by_dimension[d]})
    for d in range(4)
}
assert tuple(len(representatives[d]) for d in range(4)) == (24, 78, 84, 30)

matrices = {}
smith = {}
for d in (1, 2, 3):
    top = representatives[d]
    low = representatives[d - 1]
    low_index = {c: i for i, c in enumerate(low)}
    entries = [[0] * len(top) for _ in low]
    for j, cell in enumerate(top):
        for face, coeff in boundary(cell).items():
            rep, eps = canonical(face)
            entries[low_index[rep]][j] += coeff * eps
    matrices[d] = Matrix(entries)

    diagonal = smith_normal_form(matrices[d], domain=ZZ)
    smith[d] = tuple(sorted(abs(int(diagonal[i, i]))
                            for i in range(min(diagonal.rows, diagonal.cols))
                            if diagonal[i, i]))
    assert matrices[d].rank() == len(smith[d])

assert matrices[1] * matrices[2] == Matrix.zeros(24, 84)
assert matrices[2] * matrices[3] == Matrix.zeros(78, 30)
assert smith[1] == (1,) * 23
assert smith[2] == (1,) * 54 + (4,)
assert smith[3] == (1,) * 29

# H1 has torsion Z/4, since im(d1) is free and rank(H1)=0.
# H2 has rank 84-55-29=0 and is torsion-free as a subgroup of a free group.
# H3 has rank 30-29=1 and is free.
assert (78 - len(smith[1]) - len(smith[2]),
        84 - len(smith[2]) - len(smith[3]),
        30 - len(smith[3])) == (0, 0, 1)
print('COUNTS_ORIGINAL_CELLS=(240,780,840,300)')
print('COUNTS_QUOTIENT_CELLS=(24,78,84,30)')
for d in (1, 2, 3):
    print(f'SMITH_d{d}={dict(sorted(Counter(smith[d]).items()))}')
print('INTEGRAL_HOMOLOGY=(Z,Z/4,0,Z)')
print('PENTAGON_FOUR_COLOR_DIHEDRAL_QUOTIENT_VERIFIED')
