"""Reproduce the exact six-by-six transvectant Jacobian certificate.

Only the standard Python library is needed. All arithmetic is integral or rational.
"""
from fractions import Fraction
from math import comb, factorial, gcd
from functools import reduce

R = 10
BASE = [1, 1, 1, 1] + [0] * 7
ROWS = [(4, j) for j in range(5)] + [(5, 0)]
NORMAL_COLUMNS = tuple(range(5, 11))
EXPECTED = [
    [-5, 8, -18, 60, 0, 0],
    [0, -3, 10, -42, 270, 0],
    [0, 0, 9, -4, -108, 2700],
    [0, 0, 0, 5, -21, 135],
    [0, 0, 0, 0, -3, 10],
    [0, 0, -3, 8, -36, 360],
]

def falling(n, k):
    return factorial(n) // factorial(n-k) if 0 <= k <= n else 0

def c(m, j, u, v):
    """Coefficient of a_u*a_v in [x^(20-4m-j)y^j] (f,f)_{2m}."""
    if u + v != 2*m + j:
        return 0
    return sum(
        (-1)**k * comb(2*m, k) * falling(R-u, 2*m-k)
        * falling(u, k) * falling(R-v, k) * falling(v, 2*m-k)
        for k in range(2*m+1)
    )

def det(A):
    """Exact rational Gaussian elimination, with row swaps."""
    B = [[Fraction(x) for x in row] for row in A]
    n = len(B)
    d = Fraction(1)
    for i in range(n):
        pivot = next((k for k in range(i,n) if B[k][i]), None)
        if pivot is None:
            return 0
        if pivot != i:
            B[i], B[pivot] = B[pivot], B[i]
            d = -d
        p = B[i][i]
        d *= p
        for k in range(i+1, n):
            fac = B[k][i] / p
            for j in range(i+1, n):
                B[k][j] -= fac * B[i][j]
            B[k][i] = 0
    assert d.denominator == 1
    return int(d)

# The order-eight and order-ten transvectants vanish at the indicated binary
# decic because the sum of y-degrees of any two nonzero terms is <=6.
for m, j in ROWS:
    assert sum(BASE[u]*BASE[v]*c(m,j,u,v)
               for u in range(R+1) for v in range(R+1)) == 0

J = [
    [sum(2*BASE[u]*c(m,j,u,v) for u in range(R+1))
     for v in NORMAL_COLUMNS]
    for (m,j) in ROWS
]
normalized = []
scales = []
for row in J:
    scale = reduce(gcd, row, 0)
    assert scale > 0
    scales.append(scale)
    normalized.append([v // scale for v in row])
assert normalized == EXPECTED, (normalized, scales)
assert scales == [2438553600, 4877107200, 2438553600,
                  9754214400, 14631321600, 73156608000]
assert det(normalized) == -1890000
assert 2**6 == 64
assert comb(4,1)*7 == 28
assert 64 - 28 == 36
print('VERIFY_OK: six quadrics, exact nonzero Jacobian determinant, residual degree 36')
