"""Exact standard-library certificate for the index-thirteen permutation-binomial characteristic classification.

Run: python3 verify_index13.py
All finite-field arithmetic and recurrences are exact; no external files or modules.
"""
from math import comb, isqrt

G = 13
CANDIDATES = (3, 53, 79, 131, 521, 8191)
EXCLUDED = (79, 131, 521, 8191)
EXPECTED = {
    79: {18: (), 22: (), 62: (), 65: ()},
    131: {52: (), 63: (), 80: (), 113: ()},
    521: {101: (), 421: (), 422: (), 423: ()},
    8191: {2: (7564, 7994), 4096: (840, 1270)},
}
EXPECTED_SECOND = {
    (2, 7564): (3849, 862), (2, 7994): (4023, 3293),
    (4096, 840): (6586, 8046), (4096, 1270): (1724, 7698),
}


def determinant_bareiss(rows):
    a = [row[:] for row in rows]
    n = len(a)
    previous = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            v = next((i for i in range(k + 1, n) if a[i][k]), None)
            assert v is not None
            a[k], a[v] = a[v], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def inverse_sum_polynomial(p, k, x, y):
    """P_k(-1/13,x,y) mod p by the coefficient recurrence in Fp[Y]."""
    t = -pow(G, -1, p) % p
    a = [1]
    for j in range(1, k):
        new = [0] * (len(a) + 1)
        for h in range(len(new)):
            if h < len(a):
                new[h] -= (x - j + t*h) * a[h]
            if h:
                new[h] += (x - j - j*t + t*(h-1)) * a[h-1]
        a = [v % p for v in new]
    val = 0
    for coefficient in reversed(a):
        val = (val * y + coefficient) % p
    return val


def inverse_sum_series(p, k, x, y):
    """Independent generating-function evaluation (valid for k<p and y!=1)."""
    t = -pow(G, -1, p) % p
    n = k - 1
    b = [1]
    # formal generalized binomial coefficients for (1+w)^t
    for h in range(1, k):
        b.append(b[-1] * (t - h + 1) * pow(h, -1, p) % p)
    # denominator y*(1+w)^t - 1
    den = [(y * b[h] - (1 if h == 0 else 0)) % p for h in range(k)]
    assert den[0] != 0
    inv = [pow(den[0], -1, p)]
    for h in range(1, k):
        inv.append(-sum(den[j] * inv[h-j] for j in range(1, h+1)) * inv[0] % p)
    numer = [1]
    for h in range(1, k):
        numer.append(numer[-1] * (x - h) * pow(h, -1, p) % p)
    coeff = sum(numer[j] * inv[n-j] for j in range(k)) % p
    factorial = 1
    for h in range(1, k):
        factorial = (factorial * h) % p
    return factorial * pow(y-1, k, p) * coeff % p


def root_candidates(p):
    return tuple(z for z in range(2, p) if pow(z, 13, p) == 1
                 and pow((z-1) % p, 13, p) in (1, p-1))


def extension_mul(x, y):
    """F_3[a]/(a^3-a-1); vectors in basis (1,a,a^2)."""
    coeff = [0]*5
    for i in range(3):
        for j in range(3):
            coeff[i+j] += x[i]*y[j]
    for i in (4, 3):
        coeff[i-2] += coeff[i]
        coeff[i-3] += coeff[i]
    return tuple(v % 3 for v in coeff[:3])


def extension_pow(a, k):
    v = (1, 0, 0)
    while k:
        if k & 1:
            v = extension_mul(v, a)
        a = extension_mul(a, a)
        k >>= 1
    return v


def run():
    c = [comb(G, j) for j in range(G)]
    multiplication = [[c[(i-j) % G] for j in range(G)] for i in range(G)]
    w = determinant_bareiss(multiplication)
    factors = {3:6, 53:2, 79:2, 131:2, 521:2, 8191:1}
    assert w == 487627751563388801409591
    assert w == __import__('math').prod(p**e for p, e in factors.items())
    assert all(prime(p) for p in factors)
    print('WENDT_OK', w, factors)
    checked_first = 0
    checked_second = 0
    for p in EXCLUDED:
        zs = root_candidates(p)
        assert set(zs) == set(EXPECTED[p])
        actual = {}
        for z in zs:
            roots = tuple(x for x in range(p) if inverse_sum_polynomial(p, G, x, z) == 0)
            actual[z] = roots
            assert roots == EXPECTED[p][z]
            checked_first += p
            for u in roots:
                values = tuple(inverse_sum_polynomial(p, 2*G, (2*u+(1-d)*pow(G,-1,p))%p, z)
                               for d in (0,1))
                assert values == EXPECTED_SECOND[(z, u)]
                assert all(v != 0 for v in values)
                checked_second += 2
                for d in (0,1):
                    x2 = (2*u+(1-d)*pow(G,-1,p))%p
                    assert inverse_sum_series(p, 2*G, x2, z) == values[d]
            # sample an independent computation of the first inverse power sum
            for x in (0, 1, p//2, p-1):
                assert inverse_sum_series(p, G, x, z) == inverse_sum_polynomial(p, G, x, z)
        print('EXCLUSION_OK', p, actual)
    assert checked_first == sum(p*len(EXPECTED[p]) for p in EXCLUDED)
    assert checked_second == 8
    # Characteristic 53, prime-field witness f(X)=X^3(X^13+2).
    p = 53
    t = (p-1)//G
    h = [z for z in range(1, p) if pow(z, t, p) == 1]
    assert h == [1, 23, 30, 52]
    assert [pow(z, 3, p)*pow((z+2) % p, 13, p)%p for z in h] == [30, 23, 1, 52]
    assert len({pow(x,3,p)*((pow(x,13,p)+2)%p)%p for x in range(p)}) == p
    print('WITNESS_53_OK', h)
    # Characteristic 3, degree-three irreducible a^3-a-1=0.
    # No roots in F_3: evaluate at 0,1,2.
    assert all((u**3-u-1)%3 for u in range(3))
    a = (0,1,0)
    assert extension_pow(a,13) == (1,0,0)
    assert extension_pow(((0+1)%3,1,0),13) == (1,0,0)
    assert extension_pow(((0-1)%3,1,0),13) == (1,0,0)
    elems = [(i,j,k) for i in range(3) for j in range(3) for k in range(3)]
    out = []
    for x in elems:
        x13 = extension_pow(x,13)
        x13_plus_a = tuple((x13[i]+a[i])%3 for i in range(3))
        out.append(extension_mul(x,x13_plus_a))
    assert len(set(out)) == 27
    print('WITNESS_27_OK degree=3 cardinality=27')
    print('CERTIFICATE_OK first_tests=',checked_first,'second_tests=',checked_second)

if __name__=='__main__':
    run()
