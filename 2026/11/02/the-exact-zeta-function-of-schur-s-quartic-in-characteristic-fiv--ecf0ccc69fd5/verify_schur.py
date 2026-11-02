#!/usr/bin/env python3
"""Exact arithmetic for Schur's quartic over F5 and F25.

All operations are finite, exhaustive, and independent of computer algebra packages.
The geometric smoothness and Weil-theoretic implications are proved in RESULT.md.
"""
from collections import Counter


def field(q):
    if q not in (5, 25):
        raise ValueError(q)
    def mul(a, b):
        if q == 5:
            return a*b % 5
        a0, a1 = a % 5, a // 5
        b0, b1 = b % 5, b // 5
        return (a0*b0 + 2*a1*b1) % 5 + 5*((a0*b1+a1*b0) % 5)
    def sub(a, b):
        if q == 5:
            return (a-b) % 5
        return (a%5-b%5) % 5 + 5*((a//5-b//5) % 5)
    def power(a, n):
        t = 1
        while n:
            if n & 1:
                t = mul(t, a)
            a = mul(a, a)
            n >>= 1
        return t
    def f(x, y):
        return sub(power(x, 4), mul(x, power(y, 3)))
    return mul, sub, power, f


def projective_count(q, mul, sub, power, f):
    # Unique normalized representative: first nonzero coordinate equals 1.
    result = 0
    for y in range(q):
        for z in range(q):
            for w in range(q):
                result += f(1, y) == f(z, w)
    for z in range(q):
        for w in range(q):
            result += f(0, 1) == f(z, w)
    for w in range(q):
        result += f(0, 0) == f(1, w)
    result += f(0, 0) == f(0, 1)
    return result


def run():
    for q, expected in ((5, 36), (25, 1176)):
        mul, sub, power, f = field(q)
        counts = Counter(f(x, y) for x in range(q) for y in range(q))
        for v in range(q):
            counts.setdefault(v, 0)
        weighted = (sum(counts[v]*counts[v] for v in range(q)) - 1)
        assert weighted % (q-1) == 0
        n = weighted // (q-1)
        assert n == expected
        chart = projective_count(q, mul, sub, power, f)
        assert chart == expected
        assert sum(counts.values()) == q*q
        if q == 5:
            assert counts[0] == 9
            assert all(counts[v] == 4 for v in range(1, q))
            print('F5_BINARY_FIBERS: zero=9, other_four=4')
        else:
            g = 2 + 5  # 2+u, with u^2=2 in F25.
            assert power(g, 24) == 1 and power(g, 12) != 1 and power(g, 8) != 1
            coset_fibers = []
            subgroup = {power(g, 4*j) for j in range(6)}
            assert len(subgroup) == 6
            for i in range(4):
                coset = {power(g, i+4*j) for j in range(6)}
                assert len(coset) == 6
                values = {counts[v] for v in coset}
                assert len(values) == 1
                coset_fibers.append(values.pop())
            assert coset_fibers == [16, 0, 48, 24]
            assert counts[0] == 97
            assert Counter(counts.values()) == Counter({97: 1, 16: 6, 0: 6, 48: 6, 24: 6})
            # Inspect the 9 possible cubic powers t^3 and their weights 1,3.
            cubic_weights = Counter(power(t, 3) for t in range(q))
            assert cubic_weights[0] == 1
            assert sorted(cubic_weights.values()) == [1] + [3]*8
            cube_coset_weight = [0, 0, 0, 0]
            for cube, weight in cubic_weights.items():
                if cube == 1:
                    continue
                x = sub(1, cube)
                i = next(i for i in range(4)
                         if x in {power(g, i+4*j) for j in range(6)})
                cube_coset_weight[i] += weight
            assert cube_coset_weight == [4, 0, 12, 6]
            print('F25_BINARY_FIBERS: zero=97; g^i<g^4> fibers i=0,1,2,3: 16,0,48,24')
            print('F25_CUBIC_WEIGHT_CLASSES: 4,0,12,6')
        print(f'PROJECTIVE_COUNT_F{q}={chart}; FIBER_MOMENT_COUNT_F{q}={n}')
    # Smooth quartic surface => rank 22 weight-2 cohomology.
    # N(F25)=1+25^2+22*25 enforces all F25 eigenvalues equal 25.
    assert 1176 == 1 + 25*25 + 22*25
    assert 36 - 1 - 25 == 10
    assert 12*5 + 10*(-5) == 10
    for m in range(1, 9):
        q = 5**m
        via_eigenvalues = q*q + 1 + 12*(5**m) + 10*((-5)**m)
        via_closed_formula = q*q+1+q*(12+10*(-1)**m)
        assert via_eigenvalues == via_closed_formula
    print('FROBENIUS_MULTIPLICITIES: +5 x 12, -5 x 10')
    print('ZETA_RECIPROCAL: (1-T)(1-25T)(1-5T)^12(1+5T)^10')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
