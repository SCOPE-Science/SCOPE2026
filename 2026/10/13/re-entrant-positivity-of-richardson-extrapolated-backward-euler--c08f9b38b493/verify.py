from fractions import Fraction as F


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def matsub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matscale(c, A):
    return [[c * x for x in row] for row in A]


def inv(A):
    n = len(A)
    M = [row[:] + eye(n)[i] for i, row in enumerate(A)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[pivot] = M[pivot], M[col]
        d = M[col][col]
        M[col] = [x / d for x in M[col]]
        for r in range(n):
            if r == col:
                continue
            q = M[r][col]
            if q:
                M[r] = [M[r][j] - q * M[col][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def generator(n):
    Q = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        Q[i][i] = F(-1)
        Q[i][i + 1] = F(1)
    return Q


def richardson(n, h):
    I = eye(n)
    Q = generator(n)
    full = matsub(I, matscale(h, Q))
    half = matsub(I, matscale(h / 2, Q))
    B1 = inv(full)
    Bh = inv(half)
    two_half = matmul(Bh, Bh)
    return matsub(matscale(F(2), two_half), B1)


def poly(x):
    return x**5 + 18*x**4 + 52*x**3 + 48*x**2 + 2*x - 12


M = richardson(5, F(1, 4))
assert all(sum(row) == 1 for row in M)
assert M[0][4] == F(-7799, 36905625)
assert M[0] == [F(316,405), F(3484,18225), F(7252,273375), F(83804,36905625), F(-7799,36905625)]
assert all(M[i][j] >= 0 for i in range(5) for j in range(5) if (i, j) != (0, 4))

M1 = richardson(5, F(1))
assert all(sum(row) == 1 for row in M1)
assert all(x >= 0 for row in M1 for x in row)
assert M1[0][4] == F(109, 3888)

assert poly(F(3959, 10000)) < 0
assert poly(F(99, 250)) > 0

for n in (2, 3, 4, 5):
    Z = richardson(n, F(0))
    assert Z == eye(n)

print('VERIFY_OK')
