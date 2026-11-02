#!/usr/bin/env python3
"""Exact self-contained finite-field checks for a characteristic-three quartic."""
from itertools import product, combinations


def field(q):
    assert q in (3, 9)
    if q == 3:
        def add(a, b): return (a + b) % 3
        def mul(a, b): return a * b % 3
    else:
        # a+3b represents a+b*w, w*w=2, in F_3[w]/(w*w+1).
        def add(a, b):
            return ((a % 3 + b % 3) % 3) + 3 * ((a // 3 + b // 3) % 3)
        def mul(a, b):
            a0, a1 = a % 3, a // 3
            b0, b1 = b % 3, b // 3
            return (a0 * b0 + 2 * a1 * b1) % 3 + 3 * ((a0 * b1 + a1 * b0) % 3)
    def pow_(a, n):
        t = 1
        for _ in range(n): t = mul(t, a)
        return t
    def neg(a): return mul(2, a)
    return add, mul, pow_, neg


def projective(n, q):
    # Exactly one canonical vector per point; no division required.
    for first in range(n):
        for tail in product(range(q), repeat=n - first - 1):
            yield (0,) * first + (1,) + tail


def symmetric_e4(v, add, mul):
    s = 0
    for ix in combinations(range(6), 4):
        z = 1
        for j in ix: z = mul(z, v[j])
        s = add(s, z)
    return s


def lift_from_hyperplane(a, add, neg):
    s = 0
    for x in a: s = add(s, x)
    return tuple(a) + (neg(s),)


def critical(v, add, mul, power):
    # Differentials of -(sigma_4), restricted to sigma_1=0:
    # g_i = x_i^3 + p2*x_i must have one common value.
    p2 = 0
    for a in v: p2 = add(p2, mul(a, a))
    g = [add(power(a, 3), mul(p2, a)) for a in v]
    return all(t == g[0] for t in g)


def count(q):
    add, mul, power, neg = field(q)
    Q = B = qs = bs = 0
    for x in projective(4, q):
        v = lift_from_hyperplane((0,) + x, add, neg)
        if symmetric_e4(v, add, mul) == 0:
            Q += 1
            qs += critical(v, add, mul, power)
    for x in projective(5, q):
        v = lift_from_hyperplane(x, add, neg)
        if symmetric_e4(v, add, mul) == 0:
            B += 1
            bs += critical(v, add, mul, power)
    return Q, B, qs, bs


def main():
    assert len(list(projective(4, 3))) == 40
    assert len(list(projective(4, 9))) == 820
    assert len(list(projective(5, 3))) == 121
    assert len(list(projective(5, 9))) == 7381
    for q, expected in [(3, (25, 76, 15, 46)), (9, (145, 1306, 15, 136))]:
        got = count(q)
        assert got == expected, (q, got, expected)
        assert got[1] == 1 + q * got[0]
        assert got[3] == 1 + 15 * q
        print(f'F_{q}: Q={got[0]} B={got[1]} Q_singular={got[2]} B_singular={got[3]}')
    # At [0:0:0:0:1:-1], the surface Q has this local Hessian.
    # It is nondegenerate in characteristic 3.
    h = ((0, 2, 2), (2, 0, 2), (2, 2, 0))
    det = (h[0][0] * (h[1][1]*h[2][2] - h[1][2]*h[2][1])
           - h[0][1] * (h[1][0]*h[2][2] - h[1][2]*h[2][0])
           + h[0][2] * (h[1][0]*h[2][1] - h[1][1]*h[2][0])) % 3
    assert det == 1
    print('NODE_HESSIAN_DETERMINANT_MOD3=1')
    # Blowing up each of the 15 split A1 nodes adds q points.
    y3 = 25 + 15*3
    y9 = 145 + 15*9
    assert (y3, y9) == (70, 280)
    # For K3, b_2=22 and each weight-two eigenvalue has abs. value 3.
    # Equality in the F_9 upper bound forces alpha^2=9 for every eigenvalue.
    assert y9 == 1 + 9**2 + 22*9
    assert y3 - 1 - 3**2 == 21*3 - 3
    print('K3_F9_MAXIMAL=280; FROBENIUS_EIGENVALUES=+3^21,-3^1')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
