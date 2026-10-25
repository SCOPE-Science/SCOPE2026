"""Exact finite-field spot checks for a two-pole Artin--Schreier Cartier calculation.

The all-fields theorem is established separately by the displayed Cartier identities.
Run with Python 3: python check_cartier.py
"""
from itertools import product

P = 3
BASIS = [(-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1)]
INDEX = {v: i for i, v in enumerate(BASIS)}


def cartier_column(i, j, coeff):
    """Cartier on x^i y^j dx, using y = y^3 - f and p=3."""
    z = [0] * len(BASIS)
    if i % P == P - 1:
        key = ((i - (P - 1)) // P, j)
        z[INDEX[key]] += 1
    if j == 1:
        for exp, a in coeff.items():
            degree = i + exp
            if degree % P == P - 1:
                key = ((degree - (P - 1)) // P, 0)
                z[INDEX[key]] -= a  # 3rd roots are identities on F_3.
    return [v % P for v in z]


def rank_mod_3(matrix):
    a = [list(row) for row in matrix]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c] % P), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, P)
        a[r] = [(inv * v) % P for v in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [(v - factor * w) % P for v, w in zip(a[i], a[r])]
        r += 1
    return r


# Orders at the two ramification points are v_0(x)=3, v_0(y)=-1,
# v_0(dx)=4 and v_inf(x)=-3, v_inf(y)=-4, v_inf(dx)=4.
for i, j in BASIS:
    assert 3 * i - j + 4 >= 0 and -3 * i - 4 * j + 4 >= 0
for j in (0, 1, 2):
    for i in range(-4, 5):
        if 3 * i - j + 4 >= 0 and -3 * i - 4 * j + 4 >= 0:
            assert (i, j) in BASIS

for A, D, B, C in product((1, 2), (1, 2), range(P), range(P)):
    coeff = {4: A, 2: B, 1: C, -1: D}
    cols = [cartier_column(*form, coeff) for form in BASIS]
    mat = [list(row) for row in zip(*cols)]
    rank = rank_mod_3(mat)
    assert rank == 2 + (B != 0), (coeff, rank)
    assert mat[0] == [1, 0, 0, 0, (-D) % P]
    assert mat[1] == [0, 0, 0, 0, -B % P]
    assert mat[3] == [0, 0, 0, 1, 0]
    assert all(not any(mat[r][c] for c in range(5)) for r in (2, 4))

# The extreme pole coefficients force lambda^{-1}=u=lambda^4;
# u in F_3^*={1,-1} gives lambda=u and u=1 in characteristic 3.
for u in (1, 2):
    lam = u
    assert (lam**4 - u) % P == 0 if u == 1 else (lam**4 - u) % P != 0
print('CARTIER_CHECK_OK: 36 coefficient cases, rank 2 (B=0), rank 3 (B!=0)')
print('POLE_AND_SYMMETRY_CHECK_OK')
