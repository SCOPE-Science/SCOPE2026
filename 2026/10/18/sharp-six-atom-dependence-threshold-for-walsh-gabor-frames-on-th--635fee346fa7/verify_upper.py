"""Exact structural certificate for the universal six-column dependence."""
from itertools import combinations, permutations
from collections import defaultdict

SIZE = 8
SUPPORT = [(2, 2), (2, 4), (6, 3), (6, 4), (7, 0), (7, 1)]
# Each B_j is specified by (row, column, entry).
SPARSE_B = [
    [(0,3,1), (1,2,-1), (4,7,-1), (5,6,1)],
    [(0,5,1), (1,4,1), (2,7,-1), (3,6,-1),
     (4,1,-1), (5,0,-1), (6,3,1), (7,2,1)],
    [(2,1,1), (3,0,-1), (6,5,-1), (7,4,1)],
]

def pauli(x, y):
    p = [[0] * SIZE for _ in range(SIZE)]
    for t in range(SIZE):
        p[t][t ^ x] = -1 if (t & y).bit_count() & 1 else 1
    return p

def sparse_matrix(entries):
    b = [[0] * SIZE for _ in range(SIZE)]
    for row, col, value in entries:
        assert b[row][col] == 0
        b[row][col] = value
    return b

def mult_bt_p(b, p):
    return [[sum(b[k][i] * p[k][j] for k in range(SIZE))
             for j in range(SIZE)] for i in range(SIZE)]

bs = [sparse_matrix(entries) for entries in SPARSE_B]
for b in bs:
    for x, y in SUPPORT:
        m = mult_bt_p(b, pauli(x, y))
        assert all(m[i][j] + m[j][i] == 0
                   for i in range(SIZE) for j in range(SIZE))

ones = [1] * SIZE
w = [[sum(b[i][j] * ones[j] for j in range(SIZE)) for b in bs]
     for i in range(3)]
# Explicit nonzero minor proves the three null vectors are generically independent.
assert w == [[1, 1, 0], [-1, 1, 0], [0, -1, 1]]
assert w[0][0] * (w[1][1] * w[2][2] - w[1][2] * w[2][1]) - w[0][1] * (w[1][0] * w[2][2] - w[1][2] * w[2][0]) == 2

# Independent coefficient-wise determinant check (all 28 maximal minors of
# the eight-by-six matrix, all 720 terms per determinant, all degree-six monomials).
for rows in combinations(range(SIZE), 6):
    coefficients = defaultdict(int)
    for permutation in permutations(range(6)):
        parity = sum(permutation[i] > permutation[j]
                     for i in range(6) for j in range(i + 1, 6))
        sign = -1 if parity & 1 else 1
        # Three bits per exponent suffice because the total degree is six.
        monomial = 0
        for i, index in enumerate(permutation):
            x, y = SUPPORT[index]
            t = rows[i]
            if (t & y).bit_count() & 1:
                sign = -sign
            monomial += 1 << (3 * (t ^ x))
        coefficients[monomial] += sign
    assert all(v == 0 for v in coefficients.values()), rows
print("PASS: 18 exact skew-symmetry identities, independent three-dimensional left kernel, 28 identically zero six-by-six minors.")
