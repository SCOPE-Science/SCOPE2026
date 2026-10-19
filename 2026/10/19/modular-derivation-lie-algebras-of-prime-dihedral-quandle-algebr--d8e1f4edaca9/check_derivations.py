#!/usr/bin/env python3
"""Finite-field checks for the derivations of prime dihedral quandle algebras.

Uses original quandle-basis Leibniz equations, independently of the
truncated-polynomial proof; also checks graded candidate operators.
Run with `python3 check_derivations.py` (Python 3.8+; no dependencies).
"""
from math import lcm

def fp_rank_sparse(equations, p):
    pivots = {}
    for eq in equations:
        row = {k: v % p for k, v in eq.items() if v % p}
        while row:
            col = min(row)
            if col not in pivots:
                inv = pow(row[col], -1, p)
                pivots[col] = {k: v * inv % p for k, v in row.items()}
                break
            f = row[col]
            for k, v in pivots[col].items():
                nv = (row.get(k, 0) - f * v) % p
                if nv:
                    row[k] = nv
                else:
                    row.pop(k, None)
    return len(pivots)

def quandle_equations(p):
    inv2 = pow(2, -1, p)
    for i in range(p):
        for j in range(p):
            k0 = (2 * j - i) % p
            for k in range(p):
                terms = (k * p + k0, ((2 * j - k) % p) * p + i,
                         ((k + i) * inv2 % p) * p + j)
                eq = {}
                for ix, sign in zip(terms, (1, -1, -1)):
                    eq[ix] = (eq.get(ix, 0) + sign) % p
                yield eq

def order2(p):
    o, x = 0, 1
    while True:
        o += 1; x = 2 * x % p
        if x == 1:
            return o

def predicted_m(p):
    return (p - 1) // lcm(2, order2(p))

def graded_operator(p, kind, j):
    L = lcm(2, order2(p))
    t = j * L + (kind == 'E')
    out = [0] * p
    for a in range(p):
        b = a + t
        if b < p:
            out[a] = (1 if kind == 'E' else a) % p
    return t, out

def verify_operator(p, kind, j):
    t, c = graded_operator(p, kind, j)
    for a in range(p):
        for b in range(p):
            n = a + b + t
            if n >= p:
                continue
            lhs = (((-1) ** a) * pow(2, b, p) * c[a + b]) % p
            rhs = ((c[a] * ((-1) ** (a + t)) * pow(2, b, p)) +
                   c[b] * ((-1) ** a) * pow(2, b + t, p)) % p
            assert lhs == rhs, (p, kind, j, a, b)

def matrix(D, p):
    t, c = D
    M = [[0] * p for _ in range(p)]
    for a in range(p):
        if a + t < p:
            M[a + t][a] = c[a]
    return M

def multiply_matrices(A, B, p):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) % p for j in range(n)] for i in range(n)]

def bracket_check(p):
    m = predicted_m(p); L = lcm(2, order2(p))
    E = [matrix(graded_operator(p,'E',j),p) for j in range(m)]
    H = [matrix(graded_operator(p,'H',j),p) for j in range(m)]
    def check(A,B,kind,coeff,k):
        AB = multiply_matrices(A,B,p); BA = multiply_matrices(B,A,p)
        C = ([[coeff * (E if kind == 'E' else H)[k][i][j] % p for j in range(p)] for i in range(p)]
             if k < m else [[0] * p for _ in range(p)])
        assert all((AB[i][j]-BA[i][j])%p == C[i][j] for i in range(p) for j in range(p))
    for i in range(m):
        for j in range(m):
            check(H[i],H[j],'H',(j-i)*L,i+j)
            check(H[i],E[j],'E',1+j*L,i+j)
            check(E[i],E[j],'E',0,i+j)

if __name__ == '__main__':
    # The original-basis equations do not assume the claimed differential form.
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43):
        rank = fp_rank_sparse(quandle_equations(p), p)
        dim = p*p-rank
        expected = 2*predicted_m(p)
        assert dim == expected, (p, dim, expected)
        print(f'ORIGINAL_BASIS p={p} rank={rank} dimension={dim}')
    for p in (3,5,7,11,13,17,19,23,29,31,37,41,43):
        m = predicted_m(p)
        for j in range(m):
            verify_operator(p,'E',j); verify_operator(p,'H',j)
        bracket_check(p)
        print(f'OPERATORS_BRACKETS p={p} dimension={2*m} PASS')
    print('ALL_CHECKS_PASSED')
