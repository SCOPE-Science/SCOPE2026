"""Exact integral certificate for the vanishing divisor product on a toric base.

Run with Python 3; only the standard library is required. The calculation
checks a degree-four integral-cohomology relation from the fan presentation.
It is not a computational test of any generalized cohomology theory.
"""

# Eliminate divisor variables D1, D3 and D5 via the three linear fan relations.
# Sparse polynomials are dictionaries from monomial exponent tuples to integers.
names = ('D2', 'D4', 'D6', 'D7', 'D8', 'D9')
zero = (0,) * len(names)

def add(*polys):
    result = {}
    for p in polys:
        for m, c in p.items():
            result[m] = result.get(m, 0) + c
    return {m: c for m, c in result.items() if c}

def scale(k, p):
    return {m: k * c for m, c in p.items() if k * c}

def mul(a, b):
    result = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = tuple(x + y for x, y in zip(ma, mb))
            result[m] = result.get(m, 0) + ca * cb
    return {m: c for m, c in result.items() if c}

basis = {}
for j, i in enumerate((2,4,6,7,8,9)):
    e = tuple(int(k == j) for k in range(6))
    basis[i] = {e: 1}
D = dict(basis)
D[1] = add(D[2], scale(-1, D[7]), scale(-1, D[8]))
D[3] = add(D[4], scale(-1, D[7]), scale(-1, D[8]), scale(-1, D[9]))
D[5] = add(D[6], scale(-1, D[7]), scale(-2, D[8]), scale(-1, D[9]))
u = add(D[2], scale(-1,D[4]), D[6], scale(-2,D[7]), scale(-4,D[8]), scale(-1,D[9]))
v = add(scale(-1,D[2]), scale(-1,D[4]), D[6], D[8], scale(2,D[9]))
# Every pair below is a nonface of the 9-ray fan and has zero divisor product.
certificate = {
    (1,2):-1, (1,9):3, (2,7):1, (2,8):4, (3,4):1,
    (3,5):-2, (4,7):1, (4,9):-2, (5,6):1, (5,7):-2,
    (6,7):-1, (6,8):-3, (7,9):1,
}
rhs = add(*(scale(c, mul(D[i], D[j])) for (i,j), c in certificate.items()))
assert mul(u,v) == rhs, 'The integer certificate does not expand to the divisor product.'
assert all((i,j) in {
    (1,2),(1,9),(2,7),(2,8),(3,4),(3,5),(4,7),(4,8),
    (4,9),(5,6),(5,7),(6,7),(6,8),(6,9),(7,9)
} for i,j in certificate), 'A claimed zero monomial is not a nonface.'
print('UV_CERTIFICATE_OK: 13 allowed Stanley--Reisner zero monomials')
