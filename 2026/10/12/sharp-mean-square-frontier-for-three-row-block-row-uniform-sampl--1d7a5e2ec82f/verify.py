"""Exact-rational tests for the four-row, three-sampled-row update."""
from fractions import Fraction as F
from itertools import combinations

N = 4
I = [[F(i == j) for j in range(N)] for i in range(N)]
J = [[F(1) for j in range(N)] for i in range(N)]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(N)] for i in range(N)]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(N)) for j in range(N)] for i in range(N)]


def scale(a, t):
    return [[t * a[i][j] for j in range(N)] for i in range(N)]


def trans(a):
    return [[a[j][i] for j in range(N)] for i in range(N)]


def gram(mu):
    return add(scale(I, 1 - mu), scale(J, mu))


def selection(omitted):
    return [[F(i == j and i != omitted) for j in range(N)] for i in range(N)]


def transfer(y, mu):
    g = gram(mu)
    out = scale(I, F(0))
    for omitted in range(N):
        d = selection(omitted)
        b = add(I, scale(mul(g, d), -1))
        out = add(out, mul(mul(b, y), trans(b)))
    return scale(out, F(1, N))


def expected_b_squared(mu):
    g = gram(mu)
    sum_dgd = scale(I, F(0))
    for omitted in range(N):
        d = selection(omitted)
        sum_dgd = add(sum_dgd, mul(mul(d, g), d))
    edgd = scale(sum_dgd, F(1, N))
    # The positive square root of G commutes with EDGD on this symmetric family.
    return add(add(I, scale(g, F(-3, 2))), mul(g, edgd))


def analytical_m(mu):
    return (
        ((1 + 9 * mu * mu) / 4, (6 * mu * mu - 3 * mu) / 2),
        (3 * mu * mu / 2, (7 * mu * mu - 2 * mu) / 2),
    )


def determinant_2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def check(mu):
    ti, tj = transfer(I, mu), transfer(J, mu)
    mm = ((ti[0][0], tj[0][0] - ti[0][0]),
          (ti[0][1], tj[0][1] - ti[0][1]))
    want = analytical_m(mu)
    assert mm == want
    for u, v in [(F(0), F(1)), (F(1), F(0)), (F(7, 9), F(13, 19))]:
        y = add(scale(I, u - v), scale(J, v))
        ty = transfer(y, mu)
        target_u = want[0][0] * u + want[0][1] * v
        target_v = want[1][0] * u + want[1][1] * v
        assert ty == add(scale(I, target_u - target_v), scale(J, target_v))
    det = determinant_2(want)
    assert det == mu * (27 * mu ** 3 + 7 * mu - 2) / 8
    tr = want[0][0] + want[1][1]
    assert tr == (23 * mu ** 2 - 4 * mu + 1) / 4
    assert 1 - tr + det == 3 * (mu - 1) * (3 * mu + 1) * (3 * mu ** 2 + 2 * mu - 2) / 8
    assert 1 + tr + det == (27 * mu ** 4 + 53 * mu ** 2 - 10 * mu + 10) / 8
    e = expected_b_squared(mu)
    diagonal, off_diagonal = e[0][0], e[0][1]
    assert all(e[i][j] == (diagonal if i == j else off_diagonal)
               for i in range(N) for j in range(N))
    assert diagonal + 3 * off_diagonal == (18 * mu ** 2 - 3 * mu + 1) / 4
    assert diagonal - off_diagonal == (2 * mu ** 2 + mu + 1) / 4


cases = [F(0), F(1, 100), F(1, 4), F(1, 3), F(1, 2),
         F(13, 25), F(8, 15), F(11, 20), F(3, 5), F(2, 3),
         F(3, 4), F(99, 100)]
for mu in cases:
    check(mu)
assert (18 * F(13, 25) ** 2 - 3 * F(13, 25) + 1) / 4 == F(673, 625)
assert analytical_m(F(3, 5)) == ((F(53, 50), F(9, 50)),
                                     (F(27, 50), F(33, 50)))
print("EXACT_CHECK_OK", len(cases), "rational parameters; four subsets each")
