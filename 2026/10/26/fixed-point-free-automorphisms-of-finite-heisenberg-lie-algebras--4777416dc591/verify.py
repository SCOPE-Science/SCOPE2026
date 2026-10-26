"""Finite checks for the fixed-point-free Heisenberg automorphism formula.

Uses only the Python standard library. The proof in RESULT.md is general;
these enumerations are independent finite corroborations only.
"""
from itertools import product
from math import prod


def matmul(a, b, q):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % q
             for j in range(len(b[0]))] for i in range(len(a))]


def rank_mod(a, q):
    a = [row[:] for row in a]
    m, n, rank = len(a), len(a[0]), 0
    for col in range(n):
        pivot = next((i for i in range(rank, m) if a[i][col] % q), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, q)
        a[rank] = [(x * inv) % q for x in a[rank]]
        for i in range(m):
            if i != rank and a[i][col] % q:
                factor = a[i][col] % q
                a[i] = [(a[i][j] - factor * a[rank][j]) % q
                        for j in range(n)]
        rank += 1
        if rank == m:
            break
    return rank


def symplectic_form(n, q):
    d = 2 * n
    j = [[0] * d for _ in range(d)]
    for i in range(n):
        j[i][n + i] = 1
        j[n + i][i] = (-1) % q
    return j


def formula(n, q):
    total_per_multiplier = 0
    for r in range(n + 1):
        numerator = prod(q ** (2 * (n - i)) - 1 for i in range(r))
        denominator = prod(q ** (r - i) - 1 for i in range(r))
        isotropic = numerator // denominator
        sp_order = q ** ((n-r) ** 2) * prod(
            q ** (2*j) - 1 for j in range(1, n-r+1))
        total_per_multiplier += ((-1) ** r * q ** (r * (2*n-r))
                                 * isotropic * sp_order)
    return q ** (2*n) * (q-2) * total_per_multiplier


def enumerate_gsp2(q):
    """Exhaustively count 2x2 GSp matrices with multiplier != 1 and no 1-eigenvector.

    This routine is used only for prime q, so modular arithmetic is a field.
    """
    j = symplectic_form(1, q)
    count = 0
    by_multiplier = {}
    for values in product(range(q), repeat=4):
        m = [list(values[:2]), list(values[2:])]
        mt = [[m[col][row] for col in range(2)] for row in range(2)]
        mtjm = matmul(matmul(mt, j, q), m, q)
        multiplier = mtjm[0][1] % q
        if multiplier == 0 or multiplier == 1:
            continue
        if any(mtjm[i][k] != multiplier * j[i][k] % q
               for i in range(2) for k in range(2)):
            continue
        m_minus_i = [[(m[i][k] - (i == k)) % q for k in range(2)]
                     for i in range(2)]
        if rank_mod(m_minus_i, q) == 2:
            count += 1
            by_multiplier[multiplier] = by_multiplier.get(multiplier, 0) + 1
    return count, by_multiplier


def enumerate_gsp4_multiplier2_q3():
    """Enumerate Sp_4(3) symplectic bases, then test diag(1,1,2,2) times each."""
    q, n, d = 3, 2, 4
    j = symplectic_form(n, q)
    vectors = list(product(range(q), repeat=d))

    def pairing(x, y):
        return sum(x[i] * j[i][k] * y[k]
                   for i in range(d) for k in range(d)) % q

    nonzero = [v for v in vectors if any(v)]
    total_sp = 0
    no_fixed = 0
    for e1 in nonzero:
        for f1 in vectors:
            if pairing(e1, f1) != 1:
                continue
            complement = [w for w in vectors
                          if pairing(e1, w) == 0 and pairing(f1, w) == 0]
            for e2 in complement:
                if not any(e2):
                    continue
                for f2 in complement:
                    if pairing(e2, f2) != 1:
                        continue
                    columns = [e1, e2, f1, f2]
                    assert all(pairing(columns[a], columns[b]) == j[a][b]
                               for a in range(d) for b in range(d))
                    s = [[columns[col][row] for col in range(d)]
                         for row in range(d)]
                    total_sp += 1
                    g = [[(s[i][k] * (1 if i < 2 else 2)) % q
                          for k in range(d)] for i in range(d)]
                    g_minus_i = [[(g[i][k] - (i == k)) % q
                                  for k in range(d)] for i in range(d)]
                    if rank_mod(g_minus_i, q) == d:
                        no_fixed += 1
    return total_sp, no_fixed


def main():
    assert formula(1, 2) == 0
    for q in (2, 3, 5):
        direct, by_multiplier = enumerate_gsp2(q)
        assert formula(1, q) == q*q*direct
        assert sum(by_multiplier.values()) == direct
    assert formula(1, 3) == 108
    assert formula(1, 5) == 6750
    sp_order, coset_count = enumerate_gsp4_multiplier2_q3()
    assert sp_order == 51840
    assert coset_count == 29160
    assert formula(2, 3) == 3**4 * 29160 == 2361960
    print("VERIFY_OK_HEISENBERG_FPF")


if __name__ == "__main__":
    main()
