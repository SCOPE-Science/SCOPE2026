"""Exact Weddle quartic census over the two smallest characteristic-two fields
admitting six distinct rational points of the projective line.
Run with Python 3, standard library only: python verify.py.
"""
from itertools import permutations, product
from collections import Counter


def binary_field_multiplication(x, y, modulus, degree):
    result = 0
    while y:
        if y & 1:
            result ^= x
        y >>= 1
        x <<= 1
        if x & (1 << degree):
            x ^= modulus
    return result


def normalized_points(q):
    """Exactly one representative for each point of P^3(F_q)."""
    for pivot in range(4):
        for tail in product(range(q), repeat=3-pivot):
            yield (0,) * pivot + (1,) + tail


def direct_determinant(point, coefficients, mul):
    x, y, z, w = point
    a, b, c, d = coefficients
    rows = ((mul(a, mul(y, mul(z, w))), x, 1, a),
            (mul(b, mul(x, mul(z, w))), y, 1, b),
            (mul(c, mul(x, mul(y, w))), z, 1, c),
            (mul(d, mul(x, mul(y, z))), w, 1, d))
    det = 0
    # In characteristic two, the sign of a permutation is always +1.
    for p in permutations(range(4)):
        det ^= mul(mul(rows[0][p[0]], rows[1][p[1]]),
                   mul(rows[2][p[2]], rows[3][p[3]]))
    return det


def census(degree, modulus):
    q = 1 << degree
    multiplication = [[binary_field_multiplication(i, j, modulus, degree)
                       for j in range(q)] for i in range(q)]
    def mul(i, j):
        return multiplication[i][j]
    assert all(mul(1, i) == i for i in range(q))
    assert all(mul(i, j) == mul(j, i) for i in range(q) for j in range(q))
    # These two listed polynomial moduli are irreducible over F_2.
    # For degree 3: t^3+t+1 has no F_2 root.
    # For degree 4: t^4+t+1 has no F_2 root and is not divisible by t^2+t+1.
    assert (degree, modulus) in ((3, 0b1011), (4, 0b10011))
    points = list(normalized_points(q))
    assert len(points) == q**3 + q**2 + q + 1
    # A polynomial is the six-term expression of Dolgachev's determinant,
    # obtained by expanding the 4x4 determinant in characteristic two.
    forms = []
    for x, y, z, w in points:
        forms.append((mul(mul(w,z),mul(w^z,x^y)),
                      mul(mul(w,y),mul(w^y,x^z)),
                      mul(mul(y,z),mul(y^z,w^x)),
                      mul(mul(w,x),mul(w^x,y^z)),
                      mul(mul(x,z),mul(x^z,w^y)),
                      mul(mul(x,y),mul(x^y,w^z))))
    histogram = Counter()
    witnesses = {}
    for b,c,d in permutations(range(2,q), 3):
        coeff = (b,c,d,mul(b,c),mul(b,d),mul(c,d))
        count = sum(1 for u,v,s,t,h,k in forms
                    if not (mul(coeff[0],u)^mul(coeff[1],v)^mul(coeff[2],s)
                            ^mul(coeff[3],t)^mul(coeff[4],h)^mul(coeff[5],k)))
        histogram[count] += 1
        witnesses.setdefault(count,(1,b,c,d))
    # Directly compare the expanded quartic with the defining determinant
    # at every projective point for one parameter of every point-count class.
    for value,par in witnesses.items():
        a,b,c,d=par
        cf=(mul(a,b),mul(a,c),mul(a,d),mul(b,c),mul(b,d),mul(c,d))
        for point, form in zip(points, forms):
            expanded=0
            for h,k in zip(cf,form):
                expanded ^= mul(h,k)
            assert expanded == direct_determinant(point,par,mul), (q,value,point)
    assert sum(histogram.values()) == (q-2)*(q-3)*(q-4)
    return dict(sorted(histogram.items())), witnesses


if __name__ == '__main__':
    c8,w8 = census(3,0b1011)
    c16,w16 = census(4,0b10011)
    assert c8 == {145:120}, c8
    assert c16 == {417:1440, 433:144, 449:600}, c16
    print('F8',c8,'F16',c16)
    print('examples F8',w8,'F16',w16)
    print('VERIFY_OK')
