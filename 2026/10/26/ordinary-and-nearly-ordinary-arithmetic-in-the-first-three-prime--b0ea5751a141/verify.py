#!/usr/bin/env python3
"""Exact arithmetic verification of arithmetic strata of small plane-filling curves.

Requires Python 3.10+ and SymPy (tested with 1.14.0). All algebra is over F_p;
Groebner bases certify geometric nonsingularity, not merely nonsingularity
at rational points. No remote resources or external files are needed.
"""
from collections import defaultdict
import sympy as sp


def polynomial_data(p, k):
    """The eight monomials in degree p+3, with merged coefficients."""
    d = defaultdict(int)
    terms = [((p+2, 1, 0), 1), ((3, p, 0), -1),
             ((0, p+2, 1), 1), ((0, 3, p), -1),
             ((1, 0, p+2), 1), ((p, 0, 3), -1),
             ((3, 0, p), k), ((p+2, 0, 1), -k)]
    for exponent, c in terms:
        d[exponent] = (d[exponent] + c) % p
    return {e: c for e, c in d.items() if c}


def multiply(A, B, p):
    ans = defaultdict(int)
    for (a, b, c), u in A.items():
        for (d, e, f), v in B.items():
            key = (a+d, b+e, c+f)
            ans[key] = (ans[key] + u*v) % p
    return {exp: c for exp, c in ans.items() if c}


def scalar_poly_power(F, exponent, p):
    result = {(0, 0, 0): 1}
    for _ in range(exponent):
        result = multiply(result, F, p)
    return result


def triple_basis(degree):
    return [(i, j, degree-i-j) for i in range(1, degree-1)
            for j in range(1, degree-i) if degree-i-j >= 1]


def hasse_matrix(p, k):
    degree = p+3
    F = polynomial_data(p, k)
    coeffs = scalar_poly_power(F, p-1, p)
    triples = triple_basis(degree)
    H = [[coeffs.get(tuple(p*ai-bj for ai, bj in zip(a, b)), 0)
          for b in triples] for a in triples]
    return H, F, coeffs, triples


def matrix_rank(A, p):
    B = [[c % p for c in row] for row in A]
    n, m = len(B), len(B[0])
    rank = 0
    for j in range(m):
        i = next((i for i in range(rank, n) if B[i][j]), None)
        if i is None:
            continue
        B[rank], B[i] = B[i], B[rank]
        inv = pow(B[rank][j], -1, p)
        B[rank] = [a*inv % p for a in B[rank]]
        for i in range(n):
            if i != rank and B[i][j]:
                c = B[i][j]
                B[i] = [(a-c*b) % p for a, b in zip(B[i], B[rank])]
        rank += 1
        if rank == n:
            break
    return rank


def determinant(A, p):
    B = [list(row) for row in A]
    n = len(B)
    out = 1
    for j in range(n):
        i = next((i for i in range(j, n) if B[i][j] % p), None)
        if i is None:
            return 0
        if i != j:
            B[i], B[j] = B[j], B[i]
            out = -out
        pivot = B[j][j] % p
        out = out * pivot % p
        inv = pow(pivot, -1, p)
        for r in range(j+1, n):
            c = B[r][j]*inv % p
            if c:
                for s in range(j+1, n):
                    B[r][s] = (B[r][s] - c*B[j][s]) % p
                B[r][j] = 0
    return out % p


def multiply_matrices(A, B, p):
    columns = list(zip(*B))
    return [[sum(a*b for a, b in zip(row, col)) % p for col in columns]
            for row in A]


def minor(A, removed_row, removed_column):
    return [[a for j, a in enumerate(row) if j != removed_column]
            for i, row in enumerate(A) if i != removed_row]


def validate_geometry_and_coeffs(p, k, F, coeffs):
    x, y, z = sp.symbols('x y z')
    symbols = (x, y, z)
    equation = sum(c*x**i*y**j*z**m for (i, j, m), c in F.items())
    poly = sp.Poly(sp.expand(equation**(p-1)), x, y, z, modulus=p)
    other_coeffs = {e: int(c) % p for e, c in poly.terms() if int(c) % p}
    assert coeffs == other_coeffs, 'coefficient expansion mismatch'
    for unit in symbols:
        others = tuple(v for v in symbols if v != unit)
        f = equation.subs(unit, 1)
        G = sp.groebner((f, sp.diff(f, others[0]), sp.diff(f, others[1])),
                        *others, order='lex', modulus=p)
        assert len(G.polys) == 1 and G.polys[0].as_expr() == 1, ('singularity', p, k, unit, G)
    # The defining polynomial vanishes on all rational projective points.
    for a in range(p):
        for b in range(p):
            point = (a, b, 1)
            assert sum(c * pow(point[0], i, p)*pow(point[1], j, p)*pow(point[2], m, p)
                       for (i, j, m), c in F.items()) % p == 0
    for a in range(p):
        point = (a, 1, 0)
        assert sum(c * pow(point[0], i, p)*pow(point[1], j, p)*pow(point[2], m, p)
                   for (i, j, m), c in F.items()) % p == 0
    point = (1, 0, 0)
    assert sum(c * pow(point[0], i, p)*pow(point[1], j, p)*pow(point[2], m, p)
               for (i, j, m), c in F.items()) % p == 0


def run():
    prescribed = {3: [2], 5: [4], 7: [1, 3]}
    expected = {(3, 2): (10, 10, 1), (5, 4): (21, 21, 4),
                (7, 1): (36, 35, 0), (7, 3): (36, 35, 0)}
    for p, good in prescribed.items():
        root_free = [k for k in range(p)
                     if not any((pow(t, 7, p) + k*pow(t, 3, p) - 1) % p == 0
                                for t in range(p))]
        assert root_free == good, (p, root_free)
        for k in good:
            H, F, coeffs, triples = hasse_matrix(p, k)
            g, r, delta = expected[(p, k)]
            assert len(H) == g == (p+1)*(p+2)//2
            assert matrix_rank(H, p) == r
            assert determinant(H, p) == delta
            B = multiply_matrices(H, H, p)
            assert matrix_rank(B, p) == r
            if p == 7:
                deleted_col = 0 if k == 1 else 1
                nonzero = determinant(minor(H, 0, deleted_col), p)
                assert nonzero == 4
                nonzero_square = determinant(minor(B, 0, deleted_col), p)
                assert nonzero_square == (3 if k == 1 else 4)
            validate_geometry_and_coeffs(p, k, F, coeffs)
            print('prime', p, 'parameter', k, 'genus', g,
                  'rank(H)', r, 'rank(H^2)', matrix_rank(B, p),
                  'det(H)', delta, 'smooth YES', 'all Fp points YES')
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
