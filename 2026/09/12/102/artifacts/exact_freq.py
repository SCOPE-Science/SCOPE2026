"""Exact stationary frequencies in Q(beta), beta^3 = 2 beta^2 + 1 (stdlib only).

Solves (N - beta I) v = 0 normalized by v[B2] = 1 over Q(beta), checks the
residual exactly, checks positivity from beta in (2.2, 2.21), and derives the
exact coincidence densities:
  letter density = (-3 - 9 b + 7 b^2)/32  ~= 0.350051
  block  density = (-3 -104 b + 90 b^2)/347 ~= 0.592015
Run: python3 exact_freq.py
"""
from fractions import Fraction

Z = (Fraction(0), Fraction(0), Fraction(0))
B = (Fraction(0), Fraction(1), Fraction(0))
LO, HI = Fraction(22, 10), Fraction(221, 100)  # 2.2 < beta < 2.21


def add(p, q):
    return (p[0] + q[0], p[1] + q[1], p[2] + q[2])


def neg(p):
    return (-p[0], -p[1], -p[2])


def mul(p, q):
    a1, b1, c1 = p
    a2, b2, c2 = q
    P = [a1, b1, c1]
    Q = [a2, b2, c2]
    c = [Fraction(0)] * 5
    for i in range(3):
        for j in range(3):
            c[i + j] += P[i] * Q[j]
    c0, c1, c2, c3, c4 = c
    # b^3 = 2 b^2 + 1 ; b^4 = b + 4 b^2 + 2
    return (c0 + 2 * c4 + c3, c1 + c4, c2 + 4 * c4 + 2 * c3)


def inv(p):
    one = (Fraction(1), Fraction(0), Fraction(0))
    b = (Fraction(0), Fraction(1), Fraction(0))
    b2 = (Fraction(0), Fraction(0), Fraction(1))
    cols = [mul(p, e) for e in (one, b, b2)]
    M = [[cols[j][i] for j in range(3)] for i in range(3)]
    rhs = [Fraction(1), Fraction(0), Fraction(0)]
    A = [row[:] + [rhs[i]] for i, row in enumerate(M)]
    for col in range(3):
        piv = next(r for r in range(col, 3) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        d = A[col][col]
        A[col] = [x / d for x in A[col]]
        for r in range(3):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
    return (A[0][3], A[1][3], A[2][3])


def sub(p, q):
    return add(p, neg(q))


def div(p, q):
    return mul(p, inv(q))


def smul(k, p):
    return (k * p[0], k * p[1], k * p[2])


def ev(p):
    b = 2.2055694304005904
    return float(p[0] + p[1] * b + p[2] * b * b)


def poleval(p, x):
    return p[0] + p[1] * x + p[2] * x * x


def pos_on_interval(p):
    # rigorous positivity of a+b b+c b^2 on [LO,HI] via monotonicity/concavity
    a, b, c = p
    if b == 0 and c == 0:
        return a > 0
    if c == 0:
        return min(poleval(p, LO), poleval(p, HI)) > 0
    vert = -b / (2 * c)
    pts = [LO, HI]
    if LO <= vert <= HI:
        pts.append(vert)
    return min(poleval(p, t) for t in pts) > 0


N = [[0, 0, 0, 0, 0, 0, 1, 1, 2],
     [1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 2, 4, 7],
     [0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 2],
     [0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0]]
LENS = [1, 1, 1, 2, 2, 3, 3, 4, 7]


def main():
    n = 9
    rows = [i for i in range(n) if i != 2]
    A = []
    for i in rows:
        row = []
        for j in range(n):
            base = (Fraction(N[i][j]), Fraction(0), Fraction(0))
            if i == j:
                base = sub(base, B)
            row.append(base)
        A.append(row)
    rhs = [neg(A[k][2]) for k in range(8)]
    M8 = [[r[j] for j in [0, 1, 3, 4, 5, 6, 7, 8]] for r in A]
    Aug = [M8[k][:] + [rhs[k]] for k in range(8)]
    for col in range(8):
        piv = next((r for r in range(col, 8) if Aug[r][col] != Z), None)
        assert piv is not None
        Aug[col], Aug[piv] = Aug[piv], Aug[col]
        d = Aug[col][col]
        Aug[col] = [div(x, d) for x in Aug[col]]
        for r in range(8):
            if r != col and Aug[r][col] != Z:
                f = Aug[r][col]
                Aug[r] = [sub(x, mul(f, y)) for x, y in zip(Aug[r], Aug[col])]
    sol = [Aug[k][8] for k in range(8)]
    order = [0, 1, 3, 4, 5, 6, 7, 8]
    v = {2: (Fraction(1), Fraction(0), Fraction(0))}
    for k, j in enumerate(order):
        v[j] = sol[k]
    for i in range(n):
        s = Z
        for j in range(n):
            base = (Fraction(N[i][j]), Fraction(0), Fraction(0))
            if i == j:
                base = sub(base, B)
            s = add(s, mul(base, v[j]))
        assert s == Z, (i, s)
    print('residual (N-b I)v = 0 exactly: PASS')
    for j in range(n):
        assert pos_on_interval(v[j]), j
    print('v_j > 0 on [2.2,2.21] for all j: PASS')
    S = Z
    for j in range(n):
        S = add(S, v[j])
    L = Z
    for j in range(n):
        L = add(L, smul(LENS[j], v[j]))
    coin_letter = div(add(add(v[0], v[1]), v[2]), L)
    coin_block = div(add(add(v[0], v[1]), v[2]), S)
    print('v triples (v2 = 1):')
    for j in range(n):
        print(' ', j, tuple(str(x) for x in v[j]), '~', round(ev(v[j]), 6))
    print('S =', tuple(str(x) for x in S))
    print('L =', tuple(str(x) for x in L))
    print('coin letter density =', tuple(str(x) for x in coin_letter),
          '~', round(ev(coin_letter), 6))
    print('coin block density  =', tuple(str(x) for x in coin_block),
          '~', round(ev(coin_block), 6))
    assert coin_letter == (Fraction(-3, 32), Fraction(-9, 32), Fraction(7, 32))
    assert coin_block == (Fraction(-3, 347), Fraction(-104, 347), Fraction(90, 347))
    assert pos_on_interval(coin_letter) and pos_on_interval(coin_block)
    print('closed forms + positivity: PASS')
    print('OVERALL: PASS')


if __name__ == '__main__':
    main()
