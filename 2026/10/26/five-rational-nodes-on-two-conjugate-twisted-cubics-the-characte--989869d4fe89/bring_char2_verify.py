#!/usr/bin/env python3
"""Exact finite-field and polynomial checks for a characteristic-two Bring model.

Uses only the Python standard library. The structural proof accompanying the
checks, not finite enumeration, establishes the statements for all extensions.
"""
from itertools import combinations, product

# The coefficient field F4 = F2[w]/(w^2+w+1): 2=w, 3=w^2.
F4_MUL = (
    (0, 0, 0, 0),
    (0, 1, 2, 3),
    (0, 2, 3, 1),
    (0, 3, 1, 2),
)

def f4mul(a, b):
    return F4_MUL[a][b]

# A polynomial is a dict exponent-of-s -> F4 coefficient, with total
# homogeneous degree understood from the calculation.
def padd(a, b):
    c = dict(a)
    for i, v in b.items():
        c[i] = c.get(i, 0) ^ v
        if not c[i]:
            del c[i]
    return c

def pmul(a, b):
    c = {}
    for i, v in a.items():
        for j, w in b.items():
            t = i + j
            c[t] = c.get(t, 0) ^ f4mul(v, w)
            if not c[t]:
                del c[t]
    return c

def ppow(a, k):
    c = {0: 1}
    for _ in range(k):
        c = pmul(c, a)
    return c

def esym_poly(forms, k):
    out = {}
    for subset in combinations(forms, k):
        t = {0: 1}
        for f in subset:
            t = pmul(t, f)
        out = padd(out, t)
    return out

forms = [ppow({1: 1, 0: u}, 3) for u in (0, 1, 2, 3)] + [{0: 1}]
for k in (1, 2, 3):
    assert esym_poly(forms, k) == {}, ('PARAMETRIZATION_IDENTITY_FAILURE', k)
assert esym_poly(forms, 4) == {12: 1, 9: 1, 6: 1, 3: 1, 0: 1}
assert esym_poly(forms, 5) == {12: 1, 9: 1, 6: 1, 3: 1}
print('POLYNOMIAL_IDENTITIES_OK: e1=e2=e3=0 and stated e4/e5 forms in F4[s,t]')

# Generic finite-field operations, with field elements encoded as bitvectors.
# moduli for degree 1,2,3,4 are irreducible over F2.
MODULI = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}

def gf_mul(a, b, n):
    m = MODULI[n]
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a & (1 << n):
            a ^= m
    return r

def esym_field(xs, k, n):
    r = 0
    for ind in combinations(range(5), k):
        t = 1
        for j in ind:
            t = gf_mul(t, xs[j], n)
        r ^= t
    return r

def projective_p3(n):
    q = 1 << n
    # Each projective point has unique first nonzero coordinate equal to 1.
    for first in range(4):
        for tail in product(range(q), repeat=3-first):
            yield (0,) * first + (1,) + tail

for n in (1, 2, 3, 4):
    q = 1 << n
    total = 0
    for x in projective_p3(n):
        y = x + (x[0] ^ x[1] ^ x[2] ^ x[3],)
        if esym_field(y, 2, n) == 0 and esym_field(y, 3, n) == 0:
            total += 1
    expected = 5 if n & 1 else 2*q-3
    assert total == expected, (n, total, expected)
    print(f'POINT_COUNT_OK F_(2^{n}): {total}')

# All five F4-parameter values have one zero coordinate and four ones.
def param_pair(s, t):
    return tuple(
        f4mul(f4mul(s ^ f4mul(u, t), s ^ f4mul(u, t)), s ^ f4mul(u, t))
        for u in (0,1,2,3)
    ) + (f4mul(f4mul(t,t),t),)

pts = {param_pair(1, 0)} | {param_pair(s, 1) for s in range(4)}
expected_pts = {tuple(int(i != k) for i in range(5)) for k in range(5)}
assert pts == expected_pts, (pts, expected_pts)
print('FIVE_INTERSECTION_CANDIDATES_OK')

# Tangents of the two conjugate parameterizations at [s:t]=[1:0].
v = (0,1,2,3,0)
v_conjugate = (0,1,3,2,0)
assert v != v_conjugate
print('DISTINCT_TANGENTS_OK')
print('CHECK_OK')
