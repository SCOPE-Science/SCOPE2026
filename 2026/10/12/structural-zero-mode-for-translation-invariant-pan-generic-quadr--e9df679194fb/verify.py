from fractions import Fraction


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def rank_q(A):
    B = [[Fraction(x) for x in row] for row in A]
    m, n = len(B), len(B[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if B[i][c]), None)
        if pivot is None:
            continue
        B[r], B[pivot] = B[pivot], B[r]
        p = B[r][c]
        B[r] = [x / p for x in B[r]]
        for i in range(m):
            if i != r and B[i][c]:
                q = B[i][c]
                B[i] = [B[i][j] - q * B[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def qvalue(a, b, c, x, y):
    ax = matvec(a, x)
    by = matvec(b, y)
    cy = matvec(c, y)
    return sum(x[i] * ax[i] for i in range(4)) + sum(x[i] * by[i] for i in range(4)) + sum(y[i] * cy[i] for i in range(4))

I = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
a = I
b = [[-2 if i == j else 0 for j in range(4)] for i in range(4)]
c = [
    [3, 0, -4, 2],
    [0, 3, 2, -4],
    [-4, 2, 3, 0],
    [2, -4, 0, 3],
]
Delta = [[c[i][j] - I[i][j] for j in range(4)] for i in range(4)]
u = [1, 1, 1, 1]

# M has off-diagonal blocks b/2 = -I.
M = []
for i in range(4):
    M.append(a[i] + [-I[i][j] for j in range(4)])
for i in range(4):
    M.append([-I[i][j] for j in range(4)] + c[i])

assert matvec(M, u + u) == [0] * 8
assert matvec(Delta, u) == [0] * 4

H = [
    [1, 1, 1, 1],
    [1, -1, 1, -1],
    [1, 1, -1, -1],
    [1, -1, -1, 1],
]
expected = [0, -4, 4, 8]
for v, lam in zip(H, expected):
    assert matvec(Delta, v) == [lam * t for t in v]

assert rank_q(M) == 7
assert qvalue(a, b, c, [1, 0, 0, 0], [0, 0, 0, 0]) == 1
v = [1, -1, 1, -1]
assert qvalue(a, b, c, v, v) == -16

print('VERIFY_OK rank=7 spectrum=-4,0,4,8 positive=1 negative=-16')
