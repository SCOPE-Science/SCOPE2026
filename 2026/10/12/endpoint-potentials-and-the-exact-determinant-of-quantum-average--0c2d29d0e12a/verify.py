#!/usr/bin/env python3
"""Exact rational checks of the path endpoint-potential mixing determinant.

Requires SymPy >= 1.12.  Run: python3 verify.py
Finite checks corroborate, but do not replace, the written all-size proof.
"""
from itertools import product
from sympy import Matrix, eye, symbols, discriminant, factor, Rational

z = symbols('z')


def check(couplings, tau):
    n = len(couplings) + 1
    H = Matrix.zeros(n)
    H[0, 0] = tau
    for k, a in enumerate(couplings):
        H[k, k + 1] = H[k + 1, k] = a
    powers = [eye(n)]
    for _ in range(2 * n - 2):
        powers.append(powers[-1] * H)
    V = Matrix(n, n, lambda i, j: powers[j][i, i])
    G = Matrix(n, n, lambda i, j: sum(powers[i + j][r, r] for r in range(n)))
    assert G.det() != 0  # Simple spectrum, polynomial commutant basis.
    M = V * G.inv() * V.T
    assert M == M.T
    assert M * Matrix.ones(n, 1) == Matrix.ones(n, 1)
    assert M.rank() == (n if tau != 0 else (n + 1) // 2)
    chi = H.charpoly(z).as_expr()
    delta = discriminant(chi, z)
    assert delta > 0
    L = 1
    D0 = 1
    for j, a in enumerate(couplings, start=1):
        L *= a ** (2 * (n - j))
        if (n % 2 == 0 and j % 2 == 1) or (n % 2 == 1 and j % 2 == 0):
            D0 *= a ** 2
    prediction = Rational(L, D0) * tau ** (2 * (n // 2)) / delta
    assert factor(M.det() - prediction) == 0
    return n * n


def main():
    cases = 0
    entries = 0
    for n in range(2, 8):
        weight_choices = [tuple([1] * (n - 1)), tuple(range(2, n + 1))]
        for weights in weight_choices:
            for tau in [0, 1, -1, Rational(1, 2)]:
                entries += check(weights, tau)
                cases += 1
    print('VERIFY_OK exact_cases=%d exact_mixing_entries=%d orders=2..7 including_zero_and_signed_field' % (cases, entries))


if __name__ == '__main__':
    main()
