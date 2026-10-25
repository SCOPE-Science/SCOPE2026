"""Exact characteristic-dependent incidence of Fermat-quartic bitangents.

Uses only the Python standard library. Mathematical certificate: all 3276
3x3 determinants in Z[zeta_8], their field norms, and projective intersections
of all 28 lines over F_{p^2} for p=5,17 (and p=7 as a generic check).
"""
from collections import Counter
from itertools import combinations, permutations

PERMS = tuple(permutations(range(3)))


def line_exponents():
    # None denotes zero, (sign, exponent) denotes sign*zeta_8**exponent.
    lines = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        for e in (1, 3, 5, 7):
            row = [None, None, None]
            row[i], row[j] = (1, 0), (-1, e)
            lines.append(tuple(row))
    for a in (0, 2, 4, 6):
        for b in (0, 2, 4, 6):
            lines.append(((1, 0), (1, a), (1, b)))
    assert len(lines) == 28
    return lines


def det_in_zeta8(rows):
    ans = [0] * 4
    for pi in PERMS:
        terms = [rows[k][pi[k]] for k in range(3)]
        if None in terms:
            continue
        inversions = sum(pi[i] > pi[j] for i in range(3) for j in range(i+1, 3))
        sign = (-1 if inversions & 1 else 1)
        power = 0
        for s, e in terms:
            sign *= s
            power += e
        power %= 8
        if power >= 4:
            power -= 4
            sign = -sign
        ans[power] += sign
    return tuple(ans)


def absolute_norm_in_zeta8(a):
    # zeta_8**2=i, so f(zeta)*f(-zeta)=g_0+i*g_1 in Z[i].
    a0, a1, a2, a3 = a
    g0 = a0*a0 - a2*a2 + 2*a1*a3
    g1 = 2*a0*a2 - a1*a1 + a3*a3
    return g0*g0 + g1*g1


def verify_norm_sieve():
    lines = line_exponents()
    counts = Counter(absolute_norm_in_zeta8(det_in_zeta8(tuple(lines[i] for i in ids)))
                     for ids in combinations(range(28), 3))
    expected = {0:60, 1:384, 2:64, 4:864, 8:384, 9:192,
                16:560, 17:192, 32:96, 36:192, 64:192, 256:64, 400:32}
    assert dict(counts) == expected, (counts, expected)
    assert sum(counts.values()) == 3276
    assert all(n == 0 or not (n % q == 0) for n in counts for q in (7, 11, 13, 19, 23, 29, 31, 37, 41))
    return dict(sorted(counts.items()))


def finite_incidence(p):
    # Choose a quadratic nonsquare and work in F_p[t]/(t^2-d).
    squares = {i*i % p for i in range(1, p)}
    d = next(i for i in range(2, p) if i not in squares)
    z, one = (0, 0), (1, 0)
    def add(x, y): return ((x[0]+y[0]) % p, (x[1]+y[1]) % p)
    def mul(x, y): return ((x[0]*y[0]+d*x[1]*y[1]) % p,
                           (x[0]*y[1]+x[1]*y[0]) % p)
    def neg(x): return ((-x[0]) % p, (-x[1]) % p)
    def powr(a, n):
        b = one
        while n:
            if n & 1: b = mul(b, a)
            a = mul(a, a)
            n >>= 1
        return b
    roots = [r for r in ((a,b) for a in range(p) for b in range(p))
             if powr(r, 4) == neg(one)]
    assert len(roots) == 4
    w = roots[0]
    # Select generator zeta of all eight roots of unity, w^4=-1.
    assert powr(w, 8) == one
    powers = [powr(w, k) for k in range(8)]
    def val(t): return z if t is None else (powers[t[1]] if t[0] == 1 else neg(powers[t[1]]))
    lines = [tuple(val(t) for t in row) for row in line_exponents()]
    def cross(x,y):
        return (add(mul(x[1],y[2]),neg(mul(x[2],y[1]))),
                add(mul(x[2],y[0]),neg(mul(x[0],y[2]))),
                add(mul(x[0],y[1]),neg(mul(x[1],y[0]))))
    def dot(x,y): return add(add(mul(x[0],y[0]),mul(x[1],y[1])),mul(x[2],y[2]))
    def norm(x):
        lead = next(v for v in x if v != z)
        inv = powr(lead, p*p-2)
        return tuple(mul(v,inv) for v in x)
    points = {}
    for i,j in combinations(range(28),2):
        c = cross(lines[i], lines[j])
        assert c != (z,z,z), (p,i,j)
        key = norm(c)
        points.setdefault(key, set()).update((i,j))
    mult = Counter()
    for pt in points:
        n = sum(dot(pt,line) == z for line in lines)
        assert n >= 2
        mult[n] += 1
    assert sum(n*(n-1)//2 * k for n,k in mult.items()) == 378
    return dict(sorted(mult.items()))


def main():
    norms = verify_norm_sieve()
    assert finite_incidence(5) == {2:240,3:16,4:15}
    assert finite_incidence(17) == {2:144,3:48,4:15}
    assert finite_incidence(7) == {2:288,4:15}
    print('VERIFY_OK')
    print('Exact cyclotomic determinant norm histogram:', norms)
    print('Fp2 incidence: p=5 {2:240,3:16,4:15}; p=17 {2:144,3:48,4:15}; p=7 {2:288,4:15}')
    print('For any p>=5 except 5,17, all additional nonzero cyclotomic determinants remain nonzero.')

if __name__ == '__main__':
    main()
