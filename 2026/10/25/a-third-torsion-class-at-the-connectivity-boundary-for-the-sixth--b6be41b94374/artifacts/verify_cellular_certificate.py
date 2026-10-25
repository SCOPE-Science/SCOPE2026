#!/usr/bin/env python3
"""Dependency-free verification of the cellular certificate for exp_6(S^2)."""
import json
import math
from pathlib import Path

CERT = Path(__file__).with_name("cellular_certificate.json")

def compositions(n):
    if n == 0:
        return [()]
    out = []
    for mask in range(1 << (n - 1)):
        parts = []
        last = 0
        for i in range(n - 1):
            if mask & (1 << i):
                parts.append(i + 1 - last)
                last = i + 1
        parts.append(n - last)
        out.append(tuple(parts))
    return out

def qbinom_minus1(n, r):
    if r < 0 or r > n:
        return 0
    if n % 2 == 0:
        if r % 2:
            return 0
        return math.comb(n // 2, r // 2)
    return math.comb(n // 2, r // 2)

def down(S, a):
    T = list(S)
    if T[a] == 1:
        T.pop(a)
    else:
        T[a] -= 1
    return tuple(T)

def merge(S, a):
    return tuple(S[:a] + (S[a] + S[a + 1],) + S[a + 2:])

def cell_label(cell):
    kind, S = cell
    name = "tau" if kind == "tau" else "tilde_tau"
    return name + "(" + ",".join(str(x) for x in S) + ")"

def basis(k, degree):
    out = []
    for j in range(1, k + 1):
        for S in compositions(j):
            if j + len(S) != degree:
                continue
            if j <= k - 1:
                out.append(("tau", S))
            out.append(("tilde", S))
    return out

def boundary(cell):
    kind, S = cell
    j = sum(S)
    terms = {}
    prefix = 0
    for a, s in enumerate(S):
        if s % 2 == 0:
            T = down(S, a)
            if kind == "tau":
                coeff = (-1) ** (prefix + 1)
                terms[("tau", T)] = terms.get(("tau", T), 0) + coeff
            else:
                c_tau = 2 * (-1) ** (prefix + 1)
                c_tilde = (-1) ** prefix
                terms[("tau", T)] = terms.get(("tau", T), 0) + c_tau
                terms[("tilde", T)] = terms.get(("tilde", T), 0) + c_tilde
        prefix += s
    for a in range(len(S) - 1):
        c = qbinom_minus1(S[a] + S[a + 1], S[a])
        if c:
            T = merge(S, a)
            coeff = (-1) ** (j + a - 1) * c
            terms[(kind, T)] = terms.get((kind, T), 0) + coeff
    return {k: v for k, v in terms.items() if v}

def boundary_matrix(k, degree):
    src = basis(k, degree)
    tgt = basis(k, degree - 1)
    index = {cell: i for i, cell in enumerate(tgt)}
    M = [[0 for _ in src] for _ in tgt]
    for col, cell in enumerate(src):
        for target, coeff in boundary(cell).items():
            if target not in index:
                raise AssertionError("boundary target absent from target basis: " + cell_label(target))
            M[index[target]][col] += coeff
    return M, src, tgt

def mm(A, B):
    if not A:
        return []
    if not B:
        return [[] for _ in A]
    if len(A[0]) != len(B):
        raise AssertionError("matrix shape mismatch")
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def mat_equal(A, B):
    return A == B

def identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def determinant(A):
    n = len(A)
    if n == 0:
        return 1
    if any(len(row) != n for row in A):
        raise AssertionError("determinant requires a square matrix")
    B = [row[:] for row in A]
    sign, denom = 1, 1
    for k in range(n - 1):
        if B[k][k] == 0:
            pivot_row = next((i for i in range(k + 1, n) if B[i][k] != 0), None)
            if pivot_row is None:
                return 0
            B[k], B[pivot_row] = B[pivot_row], B[k]
            sign *= -1
        pivot = B[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = B[i][j] * pivot - B[i][k] * B[k][j]
                if numerator % denom != 0:
                    raise AssertionError("Bareiss division was not exact")
                B[i][j] = numerator // denom
        for i in range(k + 1, n):
            B[i][k] = 0
        denom = pivot
    return sign * B[n - 1][n - 1]

def diag_shape(M, diagonal):
    for i, row in enumerate(M):
        for j, value in enumerate(row):
            expected = diagonal[i] if i == j and i < len(diagonal) else 0
            if value != expected:
                return False
    return True

def rank_mod(M, p):
    A = [[x % p for x in row] for row in M]
    m = len(A)
    n = len(A[0]) if m else 0
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, m) if A[i][col] % p), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        inv = pow(A[rank][col], -1, p)
        A[rank] = [(x * inv) % p for x in A[rank]]
        for i in range(m):
            if i != rank and A[i][col] % p:
                factor = A[i][col] % p
                A[i] = [(A[i][j] - factor * A[rank][j]) % p for j in range(n)]
        rank += 1
        if rank == m:
            break
    return rank

def main():
    c = json.loads(CERT.read_text(encoding="utf-8"))
    D6, src6, tgt5 = boundary_matrix(6, 6)
    D7, src7, tgt6 = boundary_matrix(6, 7)
    assert [cell_label(x) for x in tgt5] == c["bases"]["C5"]
    assert [cell_label(x) for x in src6] == c["bases"]["C6"]
    assert [cell_label(x) for x in src7] == c["bases"]["C7"]
    assert D6 == c["D6"]
    assert D7 == c["D7"]
    assert mat_equal(mm(D6, D7), [[0] * len(src7) for _ in tgt5])

    U6 = c["D6_smith_left"]
    V6 = c["D6_smith_right"]
    V6i = c["D6_smith_right_inverse"]
    S6 = c["D6_smith_diagonal"]
    B = c["kernel_image_coordinates_B"]
    UB = c["B_smith_left"]
    VB = c["B_smith_right"]
    SB = c["B_smith_diagonal"]

    assert mat_equal(mm(U6, mm(D6, V6)), S6)
    assert mat_equal(mm(V6i, V6), identity(10))
    assert mat_equal(mm(V6, V6i), identity(10))
    assert determinant(U6) in (-1, 1)
    assert determinant(V6) in (-1, 1)
    assert determinant(UB) in (-1, 1)
    assert determinant(VB) in (-1, 1)
    coords = mm(V6i, D7)
    assert all(coords[i][j] == 0 for i in range(2) for j in range(15))
    assert [row[0:] for row in coords[2:]] == B
    assert mat_equal(mm(UB, mm(B, VB)), SB)
    assert diag_shape(S6, [1, 1])
    assert diag_shape(SB, [1, 1, 1, 1, 1, 1, 1, 3])
    assert c["exact_checks"]["kernel_rank"] == 8
    assert rank_mod(B, 2) == 8
    assert rank_mod(B, 3) == 7
    assert c["exact_checks"]["rank_B_mod_2"] == 8
    assert c["exact_checks"]["rank_B_mod_3"] == 7
    print("PASS: D6 D7 = 0; unimodular Smith certificates verified.")
    print("PASS: ker(D6) has rank 8 and im(D7) has index 3 in ker(D6).")
    print("RESULT: H_6(exp_6(S^2); Z) is isomorphic to Z/3Z.")

if __name__ == "__main__":
    main()
