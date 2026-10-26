"""Exact finite-field certificate for zero-Welch three-subspace orbits in GF(512)."""
from functools import reduce
from operator import xor

POLY = 0x211
SIZE = 512

def product(a, b):
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
        if a & SIZE:
            a ^= POLY
    return z

def exponent(a, n):
    z = 1
    while n:
        if n & 1:
            z = product(z, a)
        a = product(a, a)
        n >>= 1
    return z

def poly_remainder(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a

def poly_gcd(a, b):
    while b:
        a, b = b, poly_remainder(a, b)
    return a

def poly_square_mod(a):
    res = 0
    bit = 0
    while a:
        if a & 1:
            res ^= 1 << (2 * bit)
        a >>= 1
        bit += 1
    return poly_remainder(res, POLY)

# Rabin irreducibility test: divisors of degree 9 are 3, with x^(2^9)=x.
t = 2
x_power = t
for i in range(1, 10):
    x_power = poly_square_mod(x_power)
    if i == 3:
        assert poly_gcd(POLY, x_power ^ t) == 1
assert x_power == t

assert all(exponent(a, 511) == 1 for a in range(1, SIZE))
INV = [0] + [exponent(a, 510) for a in range(1, SIZE)]
assert all(product(a, INV[a]) == 1 for a in range(1, SIZE))
W = [exponent(a, 19) for a in range(SIZE)]

def three_space(x, y):
    return tuple(sorted({0, 1, x, x ^ 1, y, y ^ 1, x ^ y, 1 ^ x ^ y}))

all_normalized = {three_space(x, y)
                  for x in range(2, SIZE)
                  for y in range(x + 1, SIZE)
                  if len(three_space(x, y)) == 8}
assert len(all_normalized) == (255 * 254) // 6 == 10795
zero_normalized = {E for E in all_normalized if reduce(xor, (W[z] for z in E), 0) == 0}
assert len(zero_normalized) == 22

def scalar_normalizations(E):
    return {tuple(sorted(product(z, INV[u]) for z in E)) for u in E if u}

def frobenius(E):
    return tuple(sorted(product(z, z) for z in E))

classes = []
remaining = set(zero_normalized)
while remaining:
    E = min(remaining)
    cls = scalar_normalizations(E)
    assert cls <= remaining
    classes.append(cls)
    remaining -= cls
classes.sort(key=lambda c: (len(c), min(c)))
assert sorted(map(len, classes)) == [1, 7, 7, 7]
exceptional = [c for c in classes if len(c) == 1][0]
assert len(exceptional) == 1
exceptional_E = next(iter(exceptional))
assert all((not u or {product(u, v) for v in exceptional_E} == set(exceptional_E)) for u in exceptional_E)
# The three full-size classes are cyclically permuted by Frobenius.
class_index = {E: j for j, cls in enumerate(classes) for E in cls}
permutation = [class_index[frobenius(min(cls))] for cls in classes]
assert permutation[0] == 0
assert sorted(permutation) == list(range(4))
assert permutation[permutation[permutation[1]]] == 1
assert len({1, permutation[1], permutation[permutation[1]]}) == 3

for cls in classes:
    for E in cls:
        assert frobenius(E) in zero_normalized
        assert scalar_normalizations(E) == cls

# Independently reproduce the source's Kloosterman input via field traces.
def trace(z):
    v, accum = z, 0
    for _ in range(9):
        accum ^= v
        v = product(v, v)
    assert accum in (0, 1)
    return accum

kl = sum(1 if trace(z ^ INV[z]) == 0 else -1 for z in range(1, SIZE))
assert kl == -5
assert (SIZE + 1 - 3 * kl) // 24 == 22
assert (SIZE - 1) * (SIZE + 1 - 3 * kl) // 168 == 1606
assert 1606 == 73 + 3 * 511

GENERIC = three_space(8, 480)
assert GENERIC in zero_normalized
assert len(scalar_normalizations(GENERIC)) == 7
frob_classes = {class_index[tuple(sorted(product(z, exponent(2, 0)) for z in frobenius(GENERIC)))]}
assert len({class_index[frobenius(GENERIC)], class_index[frobenius(frobenius(GENERIC))], class_index[GENERIC]}) == 3

print('CERTIFICATE_OK irreducible_degree=9 normalized_spaces=10795 zero_normalized=22 kloosterman=-5')
print('SCALAR_CLASS_SIZES', sorted(map(len, classes)), 'FROBENIUS_CLASS_PERMUTATION', permutation)
print('SEMILINEAR_ORBITS', (73, 1533), 'TOTAL', 1606)
print('EXCEPTIONAL_F8', exceptional_E, 'GENERIC', GENERIC)
