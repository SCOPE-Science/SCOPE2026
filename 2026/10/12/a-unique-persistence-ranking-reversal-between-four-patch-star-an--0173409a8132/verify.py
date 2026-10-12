"""Exact reconstruction of four-node extinction times; Python 3 standard library only."""
from fractions import Fraction

STAR = ((0, 1), (0, 2), (0, 3))
PATH = ((0, 1), (1, 2), (2, 3))


def same(a, b):
    a, b = list(a), list(b)
    while a and a[-1] == 0:
        a.pop()
    while b and b[-1] == 0:
        b.pop()
    return a == b


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i + j] += u * v
    return c


def subtract(a, b):
    return [(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))]


def evaluate(a, z):
    result = 0
    for coeff in reversed(a):
        result = result * z + coeff
    return result


def solve(a, b):
    n = len(b)
    rows = [[Fraction(x) for x in row] + [Fraction(rhs)]
            for row, rhs in zip(a, b)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if rows[i][k])
        rows[k], rows[pivot] = rows[pivot], rows[k]
        f = rows[k][k]
        rows[k] = [v / f for v in rows[k]]
        for i in range(n):
            if i != k and rows[i][k]:
                factor = rows[i][k]
                rows[i] = [x - factor * y for x, y in zip(rows[i], rows[k])]
    return [row[-1] for row in rows]


def extinction_times(edges, rate):
    a = [[0] * 15 for _ in range(15)]
    for state in range(1, 16):
        i = state - 1
        occupied = [v for v in range(4) if state & (1 << v)]
        empty = [v for v in range(4) if not state & (1 << v)]
        a[i][i] += len(occupied)
        for v in occupied:
            smaller = state ^ (1 << v)
            if smaller:
                a[i][smaller - 1] -= 1
        for v in empty:
            count = sum((u == v and w in occupied) or
                        (w == v and u in occupied) for u, w in edges)
            a[i][i] += rate * count
            if count:
                a[i][(state | (1 << v)) - 1] -= rate * count
    return solve(a, [1] * 15)


# Coefficients in ascending powers of the positive colonization-to-extinction ratio.
A = multiply([2, 3], [3, 4])
C = multiply([6, 9, 4], [12, 32, 31, 12])
B = multiply(A, C)
SC = [12, 52, 69, 40, 16, 3]
SL = [36, 120, 153, 94, 42, 9]
PE = [144, 672, 1404, 1742, 1420, 800, 321, 88, 12]
PI = [144, 744, 1680, 2176, 1783, 975, 368, 94, 12]

# Exact coefficient identities; no numeric approximations used.
P_CE = [864, 5256, 14088, 21880, 21743, 14350, 6237, 1649, 204]
P_CI = [432, 1944, 3984, 5028, 4286, 2451, 851, 132]
P_LE = [1080, 5400, 11976, 15639, 13208, 7213, 2307, 324]
Q = [-1296, -7560, -19080, -26628, -21648, -9631, -1592, 309, 108]
assert same(subtract(multiply(SC, C), multiply(PE, A)), multiply([0, 1], P_CE))
assert same(subtract(multiply(SC, C), multiply(PI, A)), multiply([0, 1, 1], P_CI))
assert same(subtract(multiply(SL, C), [3 * k for k in multiply(PE, A)]), multiply([0, 0, 1], P_LE))
assert same(subtract(multiply(SL, C), [3 * k for k in multiply(PI, A)]), multiply([0, 1], Q))
assert same(subtract([3*x for x in SC], SL), [0, 36, 54, 26, 6, 0])
assert same(subtract(PI, PE), [0, 72, 276, 434, 363, 175, 47, 6, 0])

# Every entry of the 15-state matrix Q(lambda) has degree at most one.
# Its determinant has degree <= 15; a Cramer numerator has degree <= 14.
# Candidate rational expressions have numerator degree <= 8, denominator
# degree <= 5, so their cross-multiplied difference has degree <= 23.
# Equality at 24 distinct positive points proves the rational identity
# for ALL positive rates, not merely the 24 sampled rates.
for lam in range(1, 25):
    star = extinction_times(STAR, lam)
    path = extinction_times(PATH, lam)
    assert star[0] == Fraction(evaluate(SC, lam), 2 * evaluate(A, lam))
    assert star[1] == Fraction(evaluate(SL, lam), 6 * evaluate(A, lam))
    assert path[0] == Fraction(evaluate(PE, lam), 2 * evaluate(C, lam))
    assert path[1] == Fraction(evaluate(PI, lam), 2 * evaluate(C, lam))
    assert star[1] == star[3] == star[7]
    assert path[0] == path[7] and path[1] == path[3]
    assert star[0] > path[1] > path[0] and star[0] > star[1] > path[0]

# Descartes' rule: Q has one sign change in descending coefficient order.
signs = [1 if v > 0 else -1 for v in reversed(Q) if v]
assert sum(signs[i] != signs[i + 1] for i in range(len(signs) - 1)) == 1
assert evaluate(Q, 5) < 0 < evaluate(Q, 6)
print('VERIFY_OK polynomial_identities=6 exact_system_solves=48')
print('Cramer_degree_bound=23 distinct_positive_evaluations=24')
print('positive_root_interval=(5,6) exactly_one_by_Descartes')
