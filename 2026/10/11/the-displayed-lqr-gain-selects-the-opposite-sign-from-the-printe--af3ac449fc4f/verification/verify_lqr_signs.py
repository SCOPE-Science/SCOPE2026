from fractions import Fraction as F

A = [
    [F(1), F(0), F(0), F(0)],
    [F(-10), F(0), F(1), F(0)],
    [F(0), F(0), F(0), F(1)],
    [F(0), F(1), F(0), F(0)],
]
P = [[F(x) for x in row] for row in [
    ["13.9065", "-4.1415", "-0.2871", "-0.1351"],
    ["-4.1415", "9.1334", "0.4281", "0.5049"],
    ["-0.2871", "0.4281", "10.0164", "0.5123"],
    ["-0.1351", "0.5049", "0.5123", "10.0244"],
]]
N = 4
I = [[F(i == j) for j in range(N)] for i in range(N)]

def add(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(N)] for i in range(N)]

def sub(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(N)] for i in range(N)]

def scale(c, X):
    return [[c * X[i][j] for j in range(N)] for i in range(N)]

def mul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(N)) for j in range(N)] for i in range(N)]

def tr(X):
    return sum(X[i][i] for i in range(N))

def transpose(X):
    return [[X[j][i] for j in range(N)] for i in range(N)]

def maxabs(X):
    return max(abs(v) for row in X for v in row)

def charpoly(M):
    B = [row[:] for row in I]
    coeff = [F(1)]
    for k in range(1, N + 1):
        MB = mul(M, B)
        ck = -tr(MB) / F(k)
        coeff.append(ck)
        B = add(MB, scale(ck, I))
    assert all(v == 0 for row in B for v in row)
    return coeff

def quartic_hurwitz(coeff):
    assert coeff[0] == 1 and len(coeff) == 5
    a1, a2, a3, a4 = coeff[1:]
    d2 = a1 * a2 - a3
    d3 = a1 * a2 * a3 - a3 * a3 - a1 * a1 * a4
    return (all(v > 0 for v in (a1, a2, a3, a4)), d2, d3)

AtP = mul(transpose(A), P)
PA = mul(P, A)
P2 = mul(P, P)
Q = scale(F(100), I)
standard = add(sub(add(AtP, PA), P2), Q)
printed = add(sub(add(AtP, PA), Q), P2)
assert maxabs(standard) == F(1789, 2000000)
assert maxabs(printed) == F(5532161073, 25000000)

M_stable = sub(A, P)
M_literal = add(A, P)
cp_stable = charpoly(M_stable)
cp_neg_literal = charpoly(scale(F(-1), M_literal))

expected_stable = [
    F(1), F(420807, 10000), F(214029003, 312500),
    F(5075824905837459, 1000000000000),
    F(143551090592111890521, 10000000000000000),
]
expected_neg_literal = [
    F(1), F(440807, 10000), F(410950381, 625000),
    F(3923873869437459, 1000000000000),
    F(76212541773651250521, 10000000000000000),
]
assert cp_stable == expected_stable
assert cp_neg_literal == expected_neg_literal

pos1, d21, d31 = quartic_hurwitz(cp_stable)
pos2, d22, d32 = quartic_hurwitz(cp_neg_literal)
assert pos1 and d21 > 0 and d31 > 0
assert pos2 and d22 > 0 and d32 > 0

print("standard_residual_max", maxabs(standard), float(maxabs(standard)))
print("printed_residual_max", maxabs(printed), float(maxabs(printed)))
print("stable_charpoly", cp_stable)
print("stable_hurwitz", d21, d31)
print("negative_literal_charpoly", cp_neg_literal)
print("negative_literal_hurwitz", d22, d32)
print("VERIFY_OK")
