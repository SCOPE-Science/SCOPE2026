"""Exact rational verification of a sector-multiplier switching construction."""
from fractions import Fraction as F

Z = F(0)
O = F(1)
A = [
    [Z, Z, Z, F(1, 3)],
    [Z, Z, F(1, 2), F(4, 9)],
    [F(3, 4), Z, Z, Z],
    [Z, Z, Z, Z],
]


def multiply(X, Y):
    return [[sum((X[i][k] * Y[k][j] for k in range(len(Y))), Z)
             for j in range(len(Y[0]))] for i in range(len(X))]


def identity(n):
    return [[O if i == j else Z for j in range(n)] for i in range(n)]


def solve(M, b):
    n = len(M)
    T = [M[i][:] + [b[i]] for i in range(n)]
    for k in range(n):
        r = next(i for i in range(k, n) if T[i][k] != 0)
        T[k], T[r] = T[r], T[k]
        d = T[k][k]
        T[k] = [x / d for x in T[k]]
        for i in range(n):
            if i != k:
                c = T[i][k]
                T[i] = [T[i][j] - c * T[k][j] for j in range(n + 1)]
    return [T[i][-1] for i in range(n)]


def polynomial_evaluate(coeffs, t):
    return sum((c * t**i for i, c in enumerate(coeffs)), Z)


powers = [identity(4)]
for k in range(1, 5):
    powers.append(multiply(powers[-1], A))
assert powers[4] == [[Z] * 4 for _ in range(4)]
assert all(sum(A[i][j] for i in range(4)) < O for j in range(4))
coefficients = [
    [sum(powers[k][i][j] for i in range(4)) for k in range(4)]
    for j in range(4)
]
assert coefficients == [
    [O, F(3, 4), F(3, 8), Z],
    [O, Z, Z, Z],
    [O, F(1, 2), Z, Z],
    [O, F(7, 9), F(1, 4), F(1, 8)],
]
expected_diff = [Z, F(1, 36), F(-1, 8), F(1, 8)]
assert [coefficients[3][i] - coefficients[0][i] for i in range(4)] == expected_diff
for t in [F(1, 6), F(1, 2), F(5, 6)]:
    scores = [polynomial_evaluate(v, t) for v in coefficients]
    desired_winner = 3 if t != F(1, 2) else 0
    assert all(scores[desired_winner] > scores[j] for j in range(4) if j != desired_winner)
for t in [F(1, 3), F(2, 3)]:
    scores = [polynomial_evaluate(v, t) for v in coefficients]
    assert scores[0] == scores[3] > scores[2] > scores[1]

B = [[A[i][j] + F(1, 1000) for j in range(4)] for i in range(4)]
assert all(B[i][j] > 0 for i in range(4) for j in range(4))
assert max(sum(B[i][j] for i in range(4)) for j in range(4)) == F(1759, 2250)
assert max(sum(B[i][j] for i in range(4)) for j in range(4)) < O
margins = []
for t, winner in [(F(1, 6), 3), (F(1, 2), 0), (F(5, 6), 3)]:
    Q = [[(O if i == j else Z) - t * B[j][i] for j in range(4)] for i in range(4)]
    scores = solve(Q, [O] * 4)
    margin = min(scores[winner] - scores[j] for j in range(4) if j != winner)
    assert margin > 0
    margins.append(margin)
assert margins == [F(6000, 3453491), F(2000, 1149013), F(6000, 687631)]
print('VERIFY_OK nilpotence_degree=4 crossings=(1/3,2/3) positive_matrix_winners=(4,1,4) exact_margins=' + str(margins))
