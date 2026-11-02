#!/usr/bin/env python3
"""Exact arithmetic checks for a characteristic-thirteen plane-quartic family.

Only Python's standard library is required. All arithmetic is over F_13,
except the enumerated geometric parameter roots in F_169.
"""
from collections import defaultdict
from itertools import product
from math import factorial

P = 13
D = ((2, 1, 1), (1, 2, 1), (1, 1, 2))
# (x,y,z)-exponent, scalar coefficient modulo 13, exponent of parameter u.
FAMILY = (((4, 0, 0), 1, 1), ((0, 4, 0), 1, 0),
          ((0, 0, 4), -1, 0), ((2, 2, 0), -2, 0),
          ((1, 1, 2), -4, 0))
SPECIAL = (((4, 0, 0), 1, 0), ((0, 4, 0), 1, 0),
           ((0, 0, 4), 1, 0), ((2, 2, 0), 3, 0),
           ((2, 0, 2), 3, 0), ((0, 2, 2), 3, 0))


def expansion(terms):
    """Independently multiply twelve copies in a four-variable sparse ring."""
    acc = {(0, 0, 0, 0): 1}
    for _ in range(P - 1):
        out = defaultdict(int)
        for (x, y, z, u), c in acc.items():
            for (a, b, d), scalar, ud in terms:
                key = (x + a, y + b, z + d, u + ud)
                out[key] = (out[key] + c * scalar) % P
        acc = {key: value for key, value in out.items() if value}
    return acc


def coefficient_multinomial(terms, exponent):
    """Separate multinomial coefficient construction of one matrix entry."""
    n = len(terms)
    totals = defaultdict(int)
    def visit(i, remaining, counts):
        if i == n - 1:
            ks = counts + [remaining]
            xyz = tuple(sum(ks[j] * terms[j][0][t] for j in range(n))
                        for t in range(3))
            if xyz != exponent:
                return
            power = sum(ks[j] * terms[j][2] for j in range(n))
            coef = factorial(P - 1)
            for k in ks:
                coef //= factorial(k)
            for j in range(n):
                coef *= terms[j][1] ** ks[j]
            totals[power] = (totals[power] + coef) % P
            return
        for k in range(remaining + 1):
            visit(i + 1, remaining - k, counts + [k])
    visit(0, P - 1, [])
    return {j: k for j, k in totals.items() if k}


def matrix(terms):
    sparse = expansion(terms)
    ans = []
    for i in range(3):
        row = []
        for j in range(3):
            target = tuple(P * D[j][t] - D[i][t] for t in range(3))
            coeff = {ud: v for (a, b, c, ud), v in sparse.items()
                     if (a, b, c) == target}
            check = coefficient_multinomial(terms, target)
            assert coeff == check, (i, j, coeff, check)
            row.append(coeff)
        ans.append(row)
    return ans


def poly_eval(coeffs, t):
    value = 0
    for a in reversed(coeffs):
        value = (value * t + a) % P
    return value


def field_add(a, b):
    return ((a[0] + b[0]) % P, (a[1] + b[1]) % P)


def field_mul(a, b):
    # alpha^2 = 5 (5 is a quadratic nonresidue modulo 13).
    return ((a[0]*b[0] + 5*a[1]*b[1]) % P,
            (a[0]*b[1] + a[1]*b[0]) % P)


def evaluate_ext(coeffs, t):
    v = (0, 0)
    for c in reversed(coeffs):
        v = field_add(field_mul(v, t), (c, 0))
    return v


def count_points(curve, u):
    # Exhaustive projective points: z=1 (x,y arbitrary), and z=0 with
    # x=1, y arbitrary plus (0:1:0).
    def vanishes(x, y, z):
        if curve == 'V':
            return (u*x**4 + y**4 - z**4 - 2*x*x*y*y - 4*x*y*z*z) % P == 0
        return (x**4+y**4+z**4+3*(x*x*y*y+x*x*z*z+y*y*z*z)) % P == 0
    return (sum(vanishes(x, y, 1) for x in range(P) for y in range(P))
            + sum(vanishes(1, y, 0) for y in range(P))
            + vanishes(0, 1, 0))


def main():
    # The coefficient polynomial conventions are low-degree first.
    B = (6, 1, 1, 6)
    T = (12, 12, 9, 7)
    A = matrix(FAMILY)
    for i in range(3):
        for j in range(3):
            expected = ({k+3: v for k, v in enumerate(B)} if i == j == 0 else
                        {k: v for k, v in enumerate(B)} if i == j == 1 else
                        {k: v for k, v in enumerate(T)} if i == j == 2 else {})
            assert A[i][j] == expected, (i, j, A[i][j], expected)
    K = matrix(SPECIAL)
    assert K == [[({0: 11} if i == j else {}) for j in range(3)]
                 for i in range(3)], K
    # Factor identities and separation, checked at all 13 coefficients by
    # elementary polynomial multiplication, not interpolation at 13 values.
    def poly_mul(a, b):
        out = [0] * (len(a)+len(b)-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i+j] = (out[i+j] + x*y) % P
        return tuple(out)
    assert tuple((6*x) % P for x in poly_mul((1,1),(1,-3,1))) == B
    assert tuple((-6*x) % P for x in poly_mul((6,1),(4,-1,1))) == T
    assert all(poly_eval(B,t) or poly_eval(T,t) for t in range(P))
    assert poly_eval(B,0)*poly_eval(B,1)*poly_eval(T,0)*poly_eval(T,1) % P
    assert pow(5, (P-1)//2, P) == P-1
    assert pow(11, (P-1)//2, P) == P-1
    roots_B = [(a,b) for a,b in product(range(P), repeat=2)
               if evaluate_ext(B, (a,b)) == (0,0)]
    roots_T = [(a,b) for a,b in product(range(P), repeat=2)
               if evaluate_ext(T, (a,b)) == (0,0)]
    assert len(roots_B) == len(roots_T) == 3
    assert set(roots_B).isdisjoint(roots_T)
    assert set(roots_B) & {(i,0) for i in range(P)} == {(12,0)}
    assert set(roots_T) & {(i,0) for i in range(P)} == {(7,0)}
    assert A[0][0].get(3) == 6
    for u, count in [(-1,12), (7,8), (2,22), (4,12)]:
        assert count_points('V', u % P) == count, (u, count_points('V',u % P))
        trace_mod13 = (1-count) % P
        eigen_trace = (u**3*poly_eval(B,u)+poly_eval(B,u)+poly_eval(T,u)) % P
        assert trace_mod13 == eigen_trace, (u, trace_mod13, eigen_trace)
    k_count = count_points('K',0)
    assert (1-k_count) % P == 3*11 % P
    print('VERIFY_OK: two exact expansion methods, complete 3x3 Hasse-Witt formula over F13[u]')
    print('VERIFY_STRATA_OK: three rank-one parameters, three rank-two parameters in F169; no common zeros')
    print('VERIFY_EXCEPTION_OK: V_-1 rank 1; special quartic K matrix 11I3, ordinary')
    print(f'POINTS_OK: four V parameters and K (K(F13)={k_count}), Frobenius traces agree')


if __name__ == '__main__':
    main()
