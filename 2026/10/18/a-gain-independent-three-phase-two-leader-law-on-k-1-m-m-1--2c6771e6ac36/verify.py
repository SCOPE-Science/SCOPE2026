#!/usr/bin/env python3
"""Separate exact-rational arithmetic checks of five pair classes.

Only Python's standard library is needed. Finite-instance tests corroborate
rather than replace the general symbolic sign argument in RESULT.md.
"""
from fractions import Fraction as F

PAIRS = ((0, 1), (0, 2), (1, 1), (1, 2), (2, 2))


def trace_inverse(matrix):
    n = len(matrix)
    a = [list(row) + [F(int(i == j)) for j in range(n)]
         for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if a[i][col])
        a[col], a[pivot] = a[pivot], a[col]
        v = a[col][col]
        a[col] = [x / v for x in a[col]]
        for i in range(n):
            if i != col and a[i][col]:
                v = a[i][col]
                a[i] = [a[i][j] - v * a[col][j] for j in range(2 * n)]
    return sum((a[i][n + i] for i in range(n)), F(0))


def matrix_cost(m, gain, pair):
    sizes = (1, m, m + 1)
    parts = [p for p, size in enumerate(sizes) for _ in range(size)]
    n = len(parts)
    lap = [[F(int(i == j) * (n - sizes[parts[i]])
              - int(i != j and parts[i] != parts[j]))
            for j in range(n)] for i in range(n)]
    reps = (0, 1, m + 1)
    i, j = pair
    u, v = reps[i], reps[j] + int(i == j)
    if u == v or v >= n or parts[v] != j:
        raise ValueError('invalid selected pair')
    lap[u][u] += gain
    lap[v][v] += gain
    return trace_inverse(lap)


def resistance(m, v, w):
    if v == w:
        return F(0)
    n = 2 * m + 2
    sz = (1, m, m + 1)
    p, _ = v
    q, _ = w
    if p == q:
        return F(2, n - sz[p])
    a, b = sz[p], sz[q]
    return F(a - 1, a * (n - a)) + F(b - 1, b * (n - b)) + F(1, a * n) + F(1, b * n)


def green_cost(m, k, pair):
    i, j = pair
    r = (i, 0)
    t = (j, int(i == j))
    sz = (1, m, m + 1)
    if t[1] >= sz[j]:
        raise ValueError('not enough vertices in part')
    vertices = [(p, ix) for p in range(3) for ix in range(sz[p])]
    n = len(vertices)
    R = resistance(m, r, t)
    A = sum((resistance(m, v, r) for v in vertices), F(0))
    S = sum(((resistance(m, v, r) + R - resistance(m, v, t)) / 2 for v in vertices), F(0))
    Q = sum((((resistance(m, v, r) + R - resistance(m, v, t)) / 2) ** 2 for v in vertices), F(0))
    g = 1 + k * R / 2
    return F(n, 1) / (2 * k) + A + (-S + n * R / 4 - k * Q / 2) / g


def closed_cost(m, k, pair):
    if m == 1:
        if pair in ((0, 1),):
            return (k*k + 7*k + 8)/(k*(k+4))
        if pair in ((0, 2), (1, 2)):
            return (5*k*k + 32*k + 32)/(k*(5*k+16))
        if pair == (2, 2):
            return (3*k*k + 18*k + 16)/(4*k*(k+2))
        raise ValueError('no two nodes in the size-one part')
    if pair == (0, 1):
        return 2*(4*k*k*m*m+5*k*k*m+7*k*m**3+25*k*m*m+25*k*m+6*k+2*m**4+12*m**3+26*m*m+24*m+8)/(k*(m+1)*(m+2)*(3*k+4*m+8))
    if pair == (0, 2):
        return 2*(4*k*k*m**3+8*k*k*m*m+3*k*k*m+7*k*m**4+27*k*m**3+37*k*m*m+21*k*m+4*k+2*m**5+12*m**4+28*m**3+32*m*m+18*m+4)/(k*(m+1)*(m+2)*(3*k*m+2*k+4*m*m+8*m+4))
    if pair == (1, 1):
        return (6*k*k*m*m+5*k*k*m-2*k*k+8*k*m**3+27*k*m*m+24*k*m+4*k+2*m**4+12*m**3+26*m*m+24*m+8)/(2*k*(m+1)*(m+2)*(k+m+2))
    if pair == (1, 2):
        return 2*(6*k*k*m**4+19*k*k*m**3+17*k*k*m*m+3*k*k*m+8*k*m**5+45*k*m**4+95*k*m**3+93*k*m*m+41*k*m+6*k+2*m**6+16*m**5+52*m**4+88*m**3+82*m*m+40*m+8)/(k*(m+1)*(m+2)*(4*k*m*m+8*k*m+3*k+4*m**3+16*m*m+20*m+8))
    if pair == (2, 2):
        return (6*k*k*m*m+7*k*k*m-4*k*k+8*k*m**3+23*k*m*m+19*k*m+4*k+2*m**4+10*m**3+18*m*m+14*m+4)/(2*k*(m+1)*(m+2)*(k+m+1))
    raise ValueError(pair)


def gap_from_hub(m, k, pair):
    assert m >= 2
    if pair == (0, 2):
        p = 2*(k*k*(m*m-m)+k*(4*m**3+6*m*m-m)+4*m**4+18*m**3+28*m*m+18*m+4)
        d = (m+1)*(m+2)*(3*k+4*m+8)*(3*k*m+2*k+4*m*m+8*m+4)
    elif pair == (1, 1):
        p = k*k*(2*m*m-5*m-6)+k*(4*m**3-3*m*m-36*m-28)+2*m**4+4*m**3-14*m*m-40*m-24
        d = 2*(m+1)*(m+2)*(k+m+2)*(3*k+4*m+8)
    elif pair == (1, 2):
        p = 2*m*(k*k*(2*m*m+m-3)+k*(4*m**3+11*m*m+2*m-8)+2*m**4+12*m**3+26*m*m+24*m+8)
        d = (m+1)*(3*k+4*m+8)*(4*k*m*m+8*k*m+3*k+4*m**3+16*m*m+20*m+8)
    elif pair == (2, 2):
        p = k*k*(2*m*m+m-12)+k*(4*m**3+9*m*m-23*m-44)+2*m**4+10*m**3+10*m*m-10*m-12
        d = 2*(m+1)*(m+2)*(k+m+1)*(3*k+4*m+8)
    else:
        raise ValueError(pair)
    return p/d


def check():
    count = 0
    for m in range(1, 14):
        valid = ((0, 1), (0, 2), (1, 2), (2, 2)) if m == 1 else PAIRS
        for k in (F(1, 13), F(1, 2), F(1), F(7, 3), F(17)):
            js = {p: green_cost(m, k, p) for p in valid}
            for pair in valid:
                assert js[pair] == closed_cost(m, k, pair), (m, k, pair)
                if m >= 2 and pair not in ((0, 1),):
                    assert js[pair] - js[(0, 1)] == gap_from_hub(m, k, pair), (m, k, pair)
            minimum = min(js.values())
            expected = (2, 2) if m == 1 else (1, 1) if m in (2, 3) else (0, 1)
            assert [p for p in valid if js[p] == minimum] == [expected], (m, k, js)
            count += len(valid)
    # Separately reconstruct H and invert exact rational matrices on concrete graphs.
    concrete = 0
    for m in range(1, 7):
        valid = ((0, 1), (0, 2), (1, 2), (2, 2)) if m == 1 else PAIRS
        for k in (F(1, 3), F(1), F(11)):
            for pair in valid:
                assert matrix_cost(m, k, pair) == green_cost(m, k, pair), (m, k, pair)
                concrete += 1
    # Positive polynomial-coefficient witnesses for all m>=4: m=4+t, t>=0.
    shifted_coefficients = {
        (0,2): [[2,14,24],[8,108,478,696],[8,164,1256,4260,5400]],
        (1,1): [[2,11,6],[4,45,132,36],[2,36,226,552,360]],
        (1,2): [[4,50,202,264],[8,150,1036,3120,3456],[4,104,1076,5536,14160,14400]],
        (2,2): [[2,17,24],[4,57,241,264],[2,42,322,1062,1260]],
    }
    for coeffs in shifted_coefficients.values():
        for poly in coeffs:
            assert all(c > 0 for c in poly)
    print('PASS:', count, 'exact effective-resistance/closed-form comparisons;', concrete,
          'separately constructed exact matrix inversions; general inequality proofs in RESULT.md')

if __name__ == '__main__':
    check()
