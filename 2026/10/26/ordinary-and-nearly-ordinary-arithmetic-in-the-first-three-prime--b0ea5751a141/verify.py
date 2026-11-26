#!/usr/bin/env python3
"""Exact chart and Hasse–Witt computations for the F_5 octic pencil."""

from sympy import Poly, diff, groebner, symbols

x, y, z = variables = symbols('x y z')
P = 5


def equation(k):
    return x**2*(x**5*y-x*y**5) + y**2*(y**5*z-y*z**5) + (z**2+k*x**2)*(z**5*x-z*x**5)


def determinant_mod(A):
    B = [row[:] for row in A]
    det = 1
    for col in range(len(B)):
        pivot = next((r for r in range(col, len(B)) if B[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            B[col], B[pivot] = B[pivot], B[col]
            det = -det
        a = B[col][col]
        det = det*a % P
        for r in range(col+1, len(B)):
            factor = B[r][col]*pow(a, -1, P) % P
            B[r] = [(u-factor*v) % P for u, v in zip(B[r], B[col])]
    return det


def main():
    for k, point in enumerate(((1,1,1), (4,2,1), (4,3,1), (1,4,1))):
        F = equation(k)
        coords = dict(zip(variables, point))
        assert all(int(g.subs(coords)) % P == 0 for g in [F]+[diff(F, a) for a in variables])
    F = equation(4)
    for a in variables:
        u, v = (b for b in variables if b != a)
        f = F.subs(a, 1)
        G = groebner([f, diff(f, u), diff(f, v)], u, v, modulus=P, order='lex')
        assert list(G) == [1]
    coeff = (Poly(F, *variables, modulus=P)**4).as_dict()
    triples = [(i, j, 8-i-j) for i in range(1, 7) for j in range(1, 8-i)]
    assert len(triples) == 21
    H = [[int(coeff.get(tuple(P*a-b for a, b in zip(u, v)), 0)) % P for v in triples] for u in triples]
    det = determinant_mod(H)
    assert det == 4
    print(f'p=5 k=4 smooth genus={len(triples)} det={det} ordinary')


if __name__ == '__main__':
    main()
