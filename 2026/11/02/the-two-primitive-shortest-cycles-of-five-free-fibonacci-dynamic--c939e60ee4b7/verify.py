#!/usr/bin/env python3
"""Exact arithmetic checks for the six-cycle classification of five-free Fibonacci sequences."""
from fractions import Fraction
from itertools import permutations

N = 6
BASES = ((1, 1, 2, 3, 1, 4), (4, 3, 7, 2, 9, 11))


def independent(mask):
    return all(not ((mask >> i & 1) and (mask >> ((i + 1) % N) & 1))
               for i in range(N))


def weighted_polynomial(d):
    total = 0
    for m in range(1, 1 << N):
        if independent(m):
            product = 1
            for i in range(N):
                if m >> i & 1:
                    product *= d[i]
            total += product
    return total


def signature(a):
    out = []
    for i in range(N):
        s, c = a[i] + a[(i + 1) % N], a[(i + 2) % N]
        assert s % c == 0
        x = s // c
        e = 0
        while x % 5 == 0:
            e += 1
            x //= 5
        assert x == 1
        out.append(e)
    return tuple(out)


def rank(A):
    B = [[Fraction(x) for x in row] for row in A]
    r = 0
    for c in range(len(B[0])):
        j = next((i for i in range(r, len(B)) if B[i][c]), None)
        if j is None:
            continue
        B[r], B[j] = B[j], B[r]
        v = B[r][c]
        B[r] = [x / v for x in B[r]]
        for i in range(len(B)):
            if i != r and B[i][c]:
                w = B[i][c]
                B[i] = [x - w * y for x, y in zip(B[i], B[r])]
        r += 1
    return r


# Signed permutation expansion of the cyclic 6-by-6 recurrence matrix.
coeff = {}
terms = 0
for perm in permutations(range(N)):
    inv = sum(perm[i] > perm[j] for i in range(N) for j in range(i + 1, N))
    sgn, monomial = (-1 if inv % 2 else 1), 0
    for i, col in enumerate(perm):
        if col == i or col == (i + 1) % N:
            sgn *= -1
        elif col == (i + 2) % N:
            monomial |= 1 << i
        else:
            break
    else:
        coeff[monomial] = coeff.get(monomial, 0) + sgn
        terms += 1
coeff = {m: v for m, v in coeff.items() if v}
expected = {((1 << N) - 1): 1}
for m in range(1, 1 << N):
    if independent(m):
        expected[m] = -1
assert coeff == expected, (coeff, expected)
assert len(coeff) == 18  # Full monomial and 17 nonempty independent sets.

# Modulo-five condition gives exactly 12 possible division supports.
supports = []
count_table = {}
for U in range(1, (1 << N) - 1):
    c = sum(independent(m) for m in range(1, 1 << N) if (m & ~U) == 0)
    count_table.setdefault(U.bit_count(), set()).add(c)
    if c % 5 == 0:
        supports.append(tuple(0 if (U >> i) & 1 else 1 for i in range(N)))
assert {k: sorted(v) for k, v in count_table.items()} == {
    1: [1], 2: [2, 3], 3: [4, 5, 7], 4: [7, 8, 9], 5: [12]
}
assert len(supports) == 12

# At the minimal positive exponents, the determinant equality already holds.
# The normalized polynomial decreases strictly if any positive exponent is raised.
for e in supports:
    d = [5 ** t for t in e]
    assert weighted_polynomial(d) == 125 == __import__('math').prod(d)
    for i, t in enumerate(e):
        if t:
            larger = d.copy()
            larger[i] *= 5
            assert Fraction(weighted_polynomial(larger), __import__('math').prod(larger)) < 1

# Every support has a one-dimensional rational kernel. Each is a rotation
# of exactly one of the two primitive cycles.
rotated = {}
for base in BASES:
    assert all(a > 0 and a % 5 for a in base)
    assert signature(base) in supports
    for r in range(N):
        a = base[r:] + base[:r]
        e = signature(a)
        assert e in supports
        assert e not in rotated
        rotated[e] = a
assert set(rotated) == set(supports)
for e in supports:
    M = [[0] * N for _ in range(N)]
    for i in range(N):
        M[i][i] -= 1
        M[i][(i + 1) % N] -= 1
        M[i][(i + 2) % N] += 5 ** e[i]
    assert rank(M) == 5
    a = rotated[e]
    assert all(sum(M[i][j] * a[j] for j in range(N)) == 0 for i in range(N))

# Cyclic parity of a primitive positive orbit forces the period to divide a
# multiple of 3; these exhibited cycles have minimal period exactly six.
for base in BASES:
    assert all(base != base[r:] + base[:r] for r in (1, 2, 3))

print('VERIFY_OK signed_determinant_terms=%d division_supports=%d primitive_rotation_classes=%d kernel_rank=5' %
      (terms, len(supports), len(BASES)))
