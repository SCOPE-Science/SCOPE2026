"""Reproducible finite checks for modular null-filiform Zinbiel ideals.
Run: python3 artifacts/verify.py ; standard library only.
All infinite claims in the accompanying proof are mathematical, not inferred from these tests.
"""
from math import comb
from itertools import product


def coeff(i, j):
    return comb(i + j - 1, j)


# The structure constants satisfy the defining Zinbiel relation over Z;
# every residue field therefore gives a well-defined Zinbiel algebra.
for i, j, k in product(range(1, 26), repeat=3):
    lhs = coeff(i, j) * coeff(i + j, k)
    rhs = (coeff(j, k) + coeff(k, j)) * coeff(i, j + k)
    assert lhs == rhs, (i, j, k, lhs, rhs)


# Pascal/Lucas parity criterion is checked independently using integer binomials.
for i, j in product(range(1, 257), repeat=2):
    assert coeff(i, j) % 2 == (1 if ((i - 1) & j) == 0 else 0)


# Every nonzero product between indices >=j must have total degree >=
# j + least power of two >=j. Reconstruct the true least degree by
# searching BOTH product orientations, not by presuming the formula.
N = 1024
INF = 10**9
S = [INF] * (N + 2)
for j in range(N, 0, -1):
    best = S[j + 1]
    for k in range(j, N + 1):
        if ((j - 1) & k) == 0:
            best = min(best, j + k)
        if ((k - 1) & j) == 0:
            best = min(best, j + k)
    S[j] = best

for j in range(1, 513):
    power = 1 << (j - 1).bit_length()
    assert S[j] == j + power, (j, S[j], j + power)

for n in range(2, 513):
    r = n.bit_length() - 1
    predicted = min(1 << r, n - (1 << (r - 1)))
    actual_j = next(j for j in range(1, n + 1) if S[j] > n)
    actual_beta = n - actual_j + 1
    assert actual_beta == predicted, (n, actual_beta, predicted)


# Exhaustive subspace census, independently checking that every ideal is
# one of the shift-invariant tails (small n only). Vectors are bit-encoded.
def product_mod2(v, w, n):
    z = 0
    for i in range(1, n + 1):
        if not (v & (1 << (i - 1))):
            continue
        for j in range(1, n - i + 1):
            if (w & (1 << (j - 1))) and coeff(i, j) % 2:
                z ^= 1 << (i + j - 1)
    return z


def all_subspaces(n):
    # Start at zero and adjoin vectors, quotienting by their actual spans.
    zero = frozenset((0,))
    seen = {zero}
    frontier = [zero]
    while frontier:
        U = frontier.pop()
        for v in range(1, 1 << n):
            if v in U:
                continue
            V = frozenset(U | {u ^ v for u in U})
            if V not in seen:
                seen.add(V)
                frontier.append(V)
    return seen


for n in range(2, 7):
    spaces = all_subspaces(n)
    ideals = []
    abelian_ideals = []
    for U in spaces:
        ideal = all(
            product_mod2(x, 1 << k, n) in U and
            product_mod2(1 << k, x, n) in U
            for x in U for k in range(n)
        )
        if ideal:
            ideals.append(U)
            if all(product_mod2(x, y, n) == 0 for x in U for y in U):
                abelian_ideals.append(U)
    tails = set()
    for j in range(1, n + 2):
        tails.add(frozenset(x for x in range(1 << n) if not (x & ((1 << (j - 1)) - 1))))
    assert set(ideals) == tails, (n, len(ideals), len(tails))
    r = n.bit_length() - 1
    beta = min(1 << r, n - (1 << (r - 1)))
    largest = [U for U in abelian_ideals if len(U) == (1 << beta)]
    assert len(largest) == 1, (n, beta, len(largest))
    print(f"n={n} subspaces={len(spaces)} ideals={len(ideals)} beta={beta} largest_abelian_ideals=1")

for r in range(2, 10):
    n = 3 * (1 << (r - 1))
    beta_char2 = min(1 << r, n - (1 << (r - 1)))
    beta_complex = n - n // 2
    assert beta_char2 - beta_complex == (1 << (r - 2))
print("range_n=2..512 closed_dimension_formula_verified")
print("product_identity_integral_verification_indices_1..25")
print("parity_lucas_verified_indices_1..256")
print("VERIFY_OK")
