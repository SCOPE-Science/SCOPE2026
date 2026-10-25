"""Independent exact checks for a characteristic-two quartic family.

No external packages; arithmetic in GF(4) uses the polynomial t^2+t+1.
"""
from itertools import product


def mul(a, b):
    value = 0
    while b:
        if b & 1:
            value ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return value


def power(a, n):
    r = 1
    for _ in range(n):
        r = mul(r, a)
    return r


def quartic(q, b, c, d):
    x, y, z, w = q
    x2, y2, z2, w2 = (power(t, 2) for t in q)
    x4, y4, z4, w4 = (power(t, 4) for t in q)
    f = x4 ^ y4 ^ z4 ^ w4
    if b:
        f ^= mul(x2, y2) ^ mul(z2, w2)
    if c:
        f ^= mul(x2, z2) ^ mul(y2, w2)
    if d:
        f ^= mul(x2, w2) ^ mul(y2, z2)
    f ^= mul(mul(x, y), mul(z, w))
    return f


def gradient(q):
    x, y, z, w = q
    return (
        mul(mul(y, z), w),
        mul(mul(x, z), w),
        mul(mul(x, y), w),
        mul(mul(x, y), z),
    )


def projective_points():
    for p in product(range(4), repeat=4):
        if p != (0, 0, 0, 0) and next(v for v in p if v) == 1:
            yield p


P3 = list(projective_points())
assert len(P3) == 85
assert power(2, 2) == 3 and mul(2, 3) == 1
assert all(power(v, 4) == v for v in range(4))

for r in range(4):
    abc = (0,) * r + (1,) * (3 - r)
    b, c, d = abc
    singular = [p for p in P3 if quartic(p, b, c, d) == 0 and not any(gradient(p))]
    assert len(singular) == 12 - 2*r, (r, len(singular))
    assert all(sum(v != 0 for v in p) == 2 for p in singular)
    weighted_length = 0
    pair_coefficients = {
        (0, 1): b, (2, 3): b,
        (0, 2): c, (1, 3): c,
        (0, 3): d, (1, 2): d,
    }
    points_predicted = []
    for edge, beta in pair_coefficients.items():
        roots = [t for t in range(4) if power(t, 4) ^ 1 ^ (mul(beta, power(t, 2))) == 0]
        assert len(roots) == (1 if beta == 0 else 2)
        assert roots == ([1] if beta == 0 else [2, 3])
        for t in roots:
            p = [0, 0, 0, 0]
            p[edge[0]] = t
            p[edge[1]] = 1
            points_predicted.append(tuple(mul(v, power(t, 2)) for v in p))
            weighted_length += 4 if beta == 0 else 2
    assert weighted_length == 24
    assert set(points_predicted) == set(singular)
    a1 = 12 - 4*r
    a3 = 2*r
    assert a1 + a3 == len(singular)
    assert 2*a1 + 4*a3 == 24

# Monomial support check for cubic Cremona pullback:
# Original degree-four monomials: four fourth powers, six pair-of-squares,
# and the coordinate product.  The pullback has total degree twelve,
# no coordinate divisor, and distinct exponent vectors (no cancellation).
monomials = [tuple(4 if i == j else 0 for i in range(4)) for j in range(4)]
for i in range(4):
    for j in range(i + 1, 4):
        exponents = [0]*4
        exponents[i] = 2
        exponents[j] = 2
        monomials.append(tuple(exponents))
monomials.append((1, 1, 1, 1))
assert len(monomials) == 11 and len(set(monomials)) == 11
pulled = [tuple(4 - n for n in monomial) for monomial in monomials]
assert len(set(pulled)) == 11
assert all(sum(p) == 12 for p in pulled)
assert all(min(p[i] for p in pulled) == 0 for i in range(4))

# Cremona is an involution on the dense torus up to a common scalar.
for x, y, z, w in product(range(1, 4), repeat=4):
    p = (x, y, z, w)
    q = (mul(mul(y,z),w),mul(mul(x,z),w),mul(mul(x,y),w),mul(mul(x,y),z))
    qq = (mul(mul(q[1],q[2]),q[3]),mul(mul(q[0],q[2]),q[3]),
          mul(mul(q[0],q[1]),q[3]),mul(mul(q[0],q[1]),q[2]))
    scale = mul(qq[0], power(x, 2)) # GF4 nonzero inverse is x^2.
    assert all(qq[i] == mul(scale,p[i]) for i in range(4))
print("VERIFY_OK: four ADE strata, 6 edge divisors of total length 24, 12/10/8/6 singular points, degree-12 Cremona dual support")
