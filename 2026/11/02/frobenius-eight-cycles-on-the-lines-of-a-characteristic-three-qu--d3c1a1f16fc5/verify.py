#!/usr/bin/env python3
"""Exact self-contained checks for the line scheme of a ternary quartic pencil.

Run: python3 verify.py
Only the Python standard library is needed. All coefficients and arithmetic
in this script are exact, and all assertions must succeed.
"""
from itertools import product

MOD = 3
VARS = ("U", "V", "u", "v", "s", "t", "a")
N = len(VARS)


def polynomial(n=0):
    return {} if n % MOD == 0 else {(0,) * N: n % MOD}


def var(name):
    exp = [0] * N
    exp[VARS.index(name)] = 1
    return {tuple(exp): 1}


def add(a, b):
    out = dict(a)
    for k, c in b.items():
        out[k] = (out.get(k, 0) + c) % MOD
        if out[k] == 0:
            del out[k]
    return out


def neg(a):
    return {k: (-c) % MOD for k, c in a.items()}


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    out = {}
    for x, c in a.items():
        for y, d in b.items():
            k = tuple(i + j for i, j in zip(x, y))
            out[k] = (out.get(k, 0) + c * d) % MOD
            if out[k] == 0:
                del out[k]
    return out


def power(a, e):
    out = polynomial(1)
    for _ in range(e):
        out = mul(out, a)
    return out


U, V, u, v, s, t, a = (var(w) for w in VARS)
Z, ONE = polynomial(), polynomial(1)


def quartic(x):
    x0, x1, x2, x3 = x
    return sub(
        add(sub(mul(power(x1, 3), x2), mul(x1, power(x2, 3))),
            sub(mul(power(x0, 3), x3), mul(x0, power(x3, 3)))),
        mul(a, mul(power(x0, 2), mul(x1, x2))),
    )


def coeffs(f):
    out = [Z for _ in range(5)]
    for ex, c in f.items():
        assert ex[0] + ex[1] == 4
        k = ex[1]
        param_exp = (0, 0) + ex[2:]
        out[k] = add(out[k], {param_exp: c})
    return out


def times(*things):
    ans = ONE
    for x in things:
        ans = mul(ans, x)
    return ans


charts = [
    ([U, V, add(times(u, U), times(s, V)), add(times(v, U), times(t, V))],
     [sub(v, power(v, 3)), sub(sub(t, power(u, 3)), times(a, u)),
      neg(times(a, s)), sub(u, power(t, 3)), sub(s, power(s, 3))]),
    ([U, times(u, U), V, add(times(v, U), times(t, V))],
     [sub(v, power(v, 3)), sub(add(power(u, 3), t), times(a, u)),
      Z, neg(add(u, power(t, 3))), Z]),
    ([U, times(u, U), times(v, U), V],
     [sub(sub(times(power(u, 3), v), times(u, power(v, 3))), times(a, u, v)),
      ONE, Z, neg(ONE), Z]),
    ([Z, U, V, add(times(u, U), times(v, V))],
     [Z, ONE, Z, neg(ONE), Z]),
    ([Z, U, times(u, U), V],
     [sub(u, power(u, 3)), Z, Z, Z, Z]),
    ([Z, Z, U, V],
     [Z, Z, Z, Z, Z]),
]
for idx, (point, expected) in enumerate(charts):
    actual = coeffs(quartic(point))
    assert actual == expected, (idx, actual, expected)
print('All six RREF restriction coefficient identities: OK')


def gf9():
    # a+bt in F3[t]/(t^2+1), represented by a+3*b
    q = 9
    aa = [[((x % 3 + y % 3) % 3) + 3 * ((x // 3 + y // 3) % 3)
           for y in range(q)] for x in range(q)]
    mm = [[((x % 3 * (y % 3) + 2 * (x // 3) * (y // 3)) % 3)
           + 3 * (((x % 3) * (y // 3) + (x // 3) * (y % 3)) % 3)
           for y in range(q)] for x in range(q)]
    nn = [((-x) % 3) + 3 * ((-(x // 3)) % 3) for x in range(q)]
    return aa, mm, nn


def line_census(q, arith):
    aa, mm, nn = arith
    ss = [[aa[x][nn[y]] for y in range(q)] for x in range(q)]
    cube = [mm[mm[x][x]][x] for x in range(q)]
    sq = [mm[x][x] for x in range(q)]
    counts = {}
    for a_value in (0, 1, 2):
        ans = 0
        for i in range(4):
            for j in range(i + 1, 4):
                free = [(r, c) for r in (0, 1) for c in range(4)
                        if c not in (i, j) and (c > i if r == 0 else c > j)]
                for vals in product(range(q), repeat=len(free)):
                    A, B = [0] * 4, [0] * 4
                    A[i], B[j] = 1, 1
                    for (r, c), val in zip(free, vals):
                        (A if r == 0 else B)[c] = val
                    C = [0] * 5
                    for n, m, sign in ((1, 2, 1), (2, 1, -1),
                                       (0, 3, 1), (3, 0, -1)):
                        x, y = cube[A[n]], cube[B[n]]
                        pieces = ((0, mm[x][A[m]]), (1, mm[x][B[m]]),
                                  (3, mm[y][A[m]]), (4, mm[y][B[m]]))
                        for k, value in pieces:
                            C[k] = (aa if sign == 1 else ss)[C[k]][value]
                    d0 = [sq[A[0]], mm[2][mm[A[0]][B[0]]], sq[B[0]]]
                    d1 = [mm[A[1]][A[2]],
                          aa[mm[A[1]][B[2]]][mm[B[1]][A[2]]],
                          mm[B[1]][B[2]]]
                    for ii in range(3):
                        for jj in range(3):
                            C[ii + jj] = ss[C[ii + jj]][mm[a_value][mm[d0[ii]][d1[jj]]]]
                    if not any(C):
                        ans += 1
        counts[a_value] = ans
    return counts

f9 = gf9()
f3 = ([[(x + y) % 3 for y in range(3)] for x in range(3)],
      [[x * y % 3 for y in range(3)] for x in range(3)],
      [(-x) % 3 for x in range(3)])
assert line_census(3, f3) == {0: 40, 1: 10, 2: 10}
assert line_census(9, f9) == {0: 112, 1: 10, 2: 10}
print('Exhaustive rational-line census over F3 and F9: OK')


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) % 3 for j in range(2)]
            for i in range(2)]


for av in (1, 2):
    for eps in (1, -1):
        M = [[0, 1], [1, -eps * av % 3]]
        P = [[1, 0], [0, 1]]
        for k in range(1, 9):
            P = matmul(P, M)
            if k == 4:
                assert P == [[2, 0], [0, 2]]
            if k == 8:
                assert P == [[1, 0], [0, 1]]
        seen = set()
        orbits = []
        for pair in product(range(3), repeat=2):
            if pair == (0, 0) or pair in seen:
                continue
            orbit, cur = [], pair
            while cur not in orbit:
                orbit.append(cur)
                seen.add(cur)
                cur = tuple((M[i][0] * cur[0] + M[i][1] * cur[1]) % 3 for i in (0, 1))
            assert cur == pair and len(orbit) == 8
            orbits.append(orbit)
        assert len(orbits) == 1 and len(seen) == 8
print('Frobenius order-eight actions on the two nine-root additive spaces: OK')
print('VERIFY_OK')
