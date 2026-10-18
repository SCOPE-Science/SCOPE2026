"""Exact rational check of a periodic four-person donation-game threshold.
Run with Python 3; no third-party dependencies.
"""
from fractions import Fraction as F
from itertools import permutations

N = 4
EDGES = ((0, 1), (1, 2), (2, 3))  # L, M, R
PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
PI = (F(1, 6), F(1, 3), F(1, 3), F(1, 6))
P = [[F(0) for _ in range(N)] for _ in range(N)]
for a, b in EDGES:
    P[a][b] = F(1, len([1 for x, y in EDGES if a in (x, y)]))
    P[b][a] = F(1, len([1 for x, y in EDGES if b in (x, y)]))


def identity(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def mult(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def power(A, m):
    result = identity(len(A))
    for _ in range(m):
        result = mult(result, A)
    return result


def solve(A, B):
    n = len(A)
    cols = len(B[0])
    M = [[F(v) for v in A[i]] + [F(v) for v in B[i]] for i in range(n)]
    for j in range(n):
        k = next((k for k in range(j, n) if M[k][j]), None)
        assert k is not None, "singular matrix"
        M[j], M[k] = M[k], M[j]
        scale = M[j][j]
        M[j] = [z / scale for z in M[j]]
        for k in range(n):
            if k != j and M[k][j]:
                scale = M[k][j]
                M[k] = [a - scale * b for a, b in zip(M[k], M[j])]
    return [row[n:n+cols] for row in M]


def pair_index(i, j):
    if i == j:
        return None
    return PAIRS.index(tuple(sorted((i, j))))

# Two-lineage survival under ONE vertex update per unit time; idle probability 1/2.
Q = [[F(0) for _ in PAIRS] for _ in PAIRS]
for z, (i, j) in enumerate(PAIRS):
    Q[z][z] += F(1, 2)
    for k in range(N):
        a = pair_index(k, j)
        b = pair_index(i, k)
        if a is not None:
            Q[z][a] += P[i][k] / N
        if b is not None:
            Q[z][b] += P[j][k] / N

# Each row is the coefficient of b in the expected first-order selection drift.
V = (
    (F(-1, 48), F(0), F(1, 96), F(1, 96), F(0), F(0)),
    (F(1, 96), F(0), F(0), F(-1, 48), F(0), F(1, 96)),
    (F(0), F(0), F(1, 96), F(1, 96), F(0), F(-1, 48)),
)
W = (F(0), F(1, 96), F(0), F(0), F(1, 96), F(0))
zero = [[F(0)] for _ in PAIRS]
IminusQ3 = [[F(int(i == j)) - power(Q, 3)[i][j] for j in range(6)] for i in range(6)]
Z = solve(IminusQ3, [[F(1)] for _ in PAIRS])
ZT = [Z]
for r in range(1, 3):
    ZT.append(mult(power(Q, r), Z))

# Independent 14-state neutral voter chain and selection covariance calculation.
STATES = tuple(range(1, (1 << N) - 1))
SINDEX = {st: pos for pos, st in enumerate(STATES)}
H = len(STATES)
M = [[F(0) for _ in STATES] for _ in STATES]
GG_B = [[[F(0)] for _ in STATES] for _ in EDGES]
GG_C = [[[F(0)] for _ in STATES] for _ in EDGES]
for z, st in enumerate(STATES):
    x = [(st >> i) & 1 for i in range(N)]
    for i in range(N):
        for j in range(N):
            if not P[i][j]:
                continue
            newst = (st & ~(1 << i)) | (x[j] << i)
            if newst in SINDEX:
                M[z][SINDEX[newst]] += P[i][j] / N
    for e, (a, b) in enumerate(EDGES):
        for spec, G in ((0, GG_B), (1, GG_C)):
            # Payoff of each individual from the single active edge.
            fit = [F(0) for _ in range(N)]
            if spec == 0:
                fit[a], fit[b] = F(x[b]), F(x[a])
            else:
                fit[a], fit[b] = F(-x[a]), F(-x[b])
            drift = F(0)
            for i in range(N):
                mean_fit = sum((P[i][j] * fit[j] for j in range(N)), F(0))
                drift += (PI[i] / N) * sum(
                    (P[i][j] * (fit[j] - mean_fit) * (x[j] - x[i])
                     for j in range(N)), F(0))
            G[e][z] = [drift]

IminusM3 = [[F(int(i == j)) - power(M, 3)[i][j] for j in range(H)] for i in range(H)]
RM3 = solve(IminusM3, identity(H))
INITIAL = [[F(0) for _ in STATES]]
for i in range(N):
    INITIAL[0][SINDEX[1 << i]] += F(1, N)
    INITIAL[0][SINDEX[((1 << N) - 1) ^ (1 << i)]] += F(1, N)

EXPECTED = {
    (1, 0, 2): (F(12920, 259077), F(-4, 21), F(12337, 3230)),
    (1, 2, 0): (F(12920, 259077), F(-4, 21), F(12337, 3230)),
    (0, 2, 1): (F(1730, 37011), F(-4, 21), F(24674, 6055)),
    (2, 0, 1): (F(1730, 37011), F(-4, 21), F(24674, 6055)),
    (0, 1, 2): (F(11981, 259077), F(-4, 21), F(49348, 11981)),
    (2, 1, 0): (F(11981, 259077), F(-4, 21), F(49348, 11981)),
}
for order in permutations(range(3)):
    benefit = sum((sum((V[e][k] * ZT[r][k][0] for k in range(6)), F(0))
                   for r, e in enumerate(order)), F(0))
    cost = -sum((sum((W[k] * ZT[r][k][0] for k in range(6)), F(0))
                 for r in range(3)), F(0))
    threshold = -cost / benefit
    assert (benefit, cost, threshold) == EXPECTED[order], (order, benefit, cost, threshold)

    # The independent state-space derivative, computed without pair coalescence.
    direct = []
    for G in (GG_B, GG_C):
        value = F(0)
        for r, e in enumerate(order):
            w = mult(mult(mult(INITIAL, power(M, r)), RM3), G[e])
            value += w[0][0]
        direct.append(value)
    assert direct == [benefit, cost], (order, direct, benefit, cost)
    sign_at_four = 4 * benefit + cost
    if order[0] == 1:
        assert sign_at_four == F(2332, 259077)
    elif order[-1] == 1:
        assert sign_at_four == F(-908, 259077)
    else:
        assert sign_at_four == F(-1424, 259077)
    print(f"order={order} benefit={benefit} cost={cost} threshold={threshold} D'(4,1)={sign_at_four}")

# Isolated-edge hub-priority score equals half the sum of endpoint degrees.
assert [F(sum((P[i][j] > 0 for j in range(N))) + sum((P[j][i] > 0 for i in range(N))), 2)
        for i, j in EDGES] == [F(3, 2), F(2), F(3, 2)]
print("PASS: six exact periodic schedules, independent 6-pair and 14-state calculations")
