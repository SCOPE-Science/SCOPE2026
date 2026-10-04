from fractions import Fraction as F


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def scale(c, A):
    return [[c * x for x in row] for row in A]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def inv(A):
    n = len(A)
    M = [list(A[i]) + eye(n)[i] for i in range(n)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[pivot] = M[pivot], M[col]
        q = M[col][col]
        M[col] = [x / q for x in M[col]]
        for r in range(n):
            if r == col:
                continue
            q = M[r][col]
            if q:
                M[r] = [M[r][j] - q * M[col][j] for j in range(2*n)]
    return [row[n:] for row in M]


def midpoint_square(Q, h):
    n = len(Q)
    I = eye(n)
    M = mul(add(I, scale(h/F(4), Q)), inv(add(I, scale(-h/F(4), Q))))
    return mul(M, M), M


def rows_stochastic(A):
    return all(sum(row) == 1 for row in A)


def nonnegative(A):
    return all(x >= 0 for row in A for x in row)


# Two-state projector formula, including one-way and strongly imbalanced chains.
for a, b in [(1, 0), (0, 3), (1, 1), (2, 5), (11, 2)]:
    s = F(a + b)
    Q = [[-F(a), F(a)], [F(b), -F(b)]]
    for h in [F(0), F(1, 7), F(1), F(4), F(17, 3), F(50)]:
        R, M = midpoint_square(Q, h)
        if s == 0:
            expected = eye(2)
        else:
            r = (1 - h*s/F(4)) / (1 + h*s/F(4))
            expected = [
                [(F(b) + r*r*F(a))/s, F(a)*(1-r*r)/s],
                [F(b)*(1-r*r)/s, (F(a) + r*r*F(b))/s],
            ]
        assert R == expected
        assert rows_stochastic(R)
        assert nonnegative(R)

# Intermediate-stage negativity can occur although the endpoint remains positive.
Q = [[F(-1), F(1)], [F(0), F(0)]]
R, M = midpoint_square(Q, F(5))
assert M[0][0] < 0 and R[0][0] > 0 and nonnegative(R)

# Three-state pure-birth witness and exact closed form.
Q3 = [[F(-1), F(1), F(0)], [F(0), F(-1), F(1)], [F(0), F(0), F(0)]]
for h in [F(0), F(1, 3), F(1), F(3), F(4), F(5), F(17, 2)]:
    R, _ = midpoint_square(Q3, h)
    d = h + 4
    expected = [
        [(h-4)**2/d**2, 16*h*(4-h)/d**3, 32*h*h/d**3],
        [F(0), (h-4)**2/d**2, 16*h/d**2],
        [F(0), F(0), F(1)],
    ]
    assert R == expected
    assert rows_stochastic(R)
    if h <= 4:
        assert nonnegative(R)
    else:
        assert R[0][1] < 0

print('VERIFY_OK')
