#!/usr/bin/env python3
"""Verify the support-containment certificate for the published ternary 6x24 matrix."""

G_ROWS = [
    "101111101000011011111111",
    "012200000101120112210201",
    "121212202202012220112100",
    "110110100011120021110011",
    "220002101012122202102210",
    "010002111020111202200000",
]

G = [[int(c) for c in row] for row in G_ROWS]
assert len(G) == 6 and all(len(row) == 24 for row in G)


def codeword(coeffs):
    return [sum(coeffs[i] * G[i][j] for i in range(6)) % 3 for j in range(24)]


def support(word):
    return [j + 1 for j, x in enumerate(word) if x != 0]


def det_mod3(matrix):
    a = [row[:] for row in matrix]
    det = 1
    n = len(a)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col] % 3), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = (-det) % 3
        pv = a[col][col] % 3
        det = (det * pv) % 3
        inv = 1 if pv == 1 else 2
        for j in range(col, n):
            a[col][j] = (a[col][j] * inv) % 3
        for r in range(col + 1, n):
            factor = a[r][col] % 3
            for j in range(col, n):
                a[r][j] = (a[r][j] - factor * a[col][j]) % 3
    return det % 3


# The first six columns already certify rank 6.
minor = [[G[r][c] for c in range(6)] for r in range(6)]
minor_det = det_mod3(minor)
assert minor_det == 2

a_coeffs = (0, 1, 1, 0, 0, 0)  # row 2 + row 3
b_coeffs = (1, 0, 0, 1, 0, 0)  # row 1 + row 4
a = codeword(a_coeffs)
b = codeword(b_coeffs)
minus_a = [(-x) % 3 for x in a]
sa = support(a)
sb = support(b)

assert set(sa) < set(sb)
assert a != b and a != minus_a and b != minus_a
assert all({a[j], b[j], minus_a[j]} != {0, 1, 2} for j in range(24))

print("det(first six columns) mod 3 =", minor_det)
print("a =", "".join(map(str, a)))
print("supp(a) =", sa)
print("b =", "".join(map(str, b)))
print("supp(b) =", sb)
print("strict_support_containment =", set(sa) < set(sb))
print("trifferent_coordinate_exists_for_(a,b,-a) =",
      any({a[j], b[j], minus_a[j]} == {0, 1, 2} for j in range(24)))
