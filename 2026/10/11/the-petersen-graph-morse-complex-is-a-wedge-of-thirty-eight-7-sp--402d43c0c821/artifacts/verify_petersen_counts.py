"""Independent exact face-count certificate for the Petersen Morse complex."""
from math import comb

vertices = tuple(range(10))
edges = sorted({tuple(sorted((i, (i + 1) % 5))) for i in range(5)} |
               {tuple(sorted((i, i + 5))) for i in range(5)} |
               {tuple(sorted((5 + i, 5 + (i + 2) % 5))) for i in range(5)})
assert len(edges) == 15
laplacian = [[0] * 10 for _ in vertices]
for i, j in edges:
    laplacian[i][i] += 1
    laplacian[j][j] += 1
    laplacian[i][j] -= 1
    laplacian[j][i] -= 1

def exact_det(matrix):
    """Fraction-free Bareiss determinant on square integer matrices."""
    a = [row.copy() for row in matrix]
    n = len(a)
    den = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, n) if a[j][k]), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = pivot * a[i][j] - a[i][k] * a[k][j]
                assert num % den == 0
                a[i][j] = num // den
        for i in range(k + 1, n):
            a[i][k] = 0
        den = pivot
    return sign * a[-1][-1]

# A degree-nine polynomial is fixed by its values at any ten distinct arguments.
for t in range(10):
    m = [[(1 if i == j else 0) + t * laplacian[i][j] for j in vertices] for i in vertices]
    assert exact_det(m) == (1 + 2 * t) ** 5 * (1 + 5 * t) ** 4
coeffs = [sum(comb(5, i) * 2 ** i * comb(4, k - i) * 5 ** (k - i)
              for i in range(max(0, k - 4), min(5, k) + 1)) for k in range(10)]
assert coeffs == [1, 30, 390, 2880, 13305, 39882, 77640, 94800, 66000, 20000]
print('INDEPENDENT_ROOTED_FOREST_COUNT_OK', coeffs)
