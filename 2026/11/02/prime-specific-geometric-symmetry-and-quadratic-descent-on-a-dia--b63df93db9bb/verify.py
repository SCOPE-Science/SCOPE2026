#!/usr/bin/env python3
"""Exact certificate for the automorphisms of a diagonal degree-4 del Pezzo surface.

Runs with Python 3's standard library. Each permutation of five branch parameters
is tested by its unique projective fractional-linear interpolation matrix.
"""
from itertools import permutations
from math import gcd

POINTS = range(5)
ID = tuple(POINTS)
REV = (4, 3, 2, 1, 0)


def det3(M):
    a, b, c = M[0]; d, e, f = M[1]; g, h, i = M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def fraction_matrix(perm):
    # (a*x+b)/(c*x+d) must take 0,1,2 to perm[0:3].
    rows = [[x, 1, -perm[x]*x, -perm[x]] for x in (0, 1, 2)]
    vec = [(-1)**j*det3([[row[k] for k in range(4) if k != j]
                         for row in rows]) for j in range(4)]
    div = gcd(*vec)
    assert div
    a, b, c, d = [v//div for v in vec]
    assert a*d-b*c != 0
    for x in (0, 1, 2):
        assert a*x+b == perm[x]*(c*x+d)
    return (a, b, c, d)


def residuals(perm, mat):
    a, b, c, d = mat
    return tuple(a*x+b-perm[x]*(c*x+d) for x in (3, 4))


def primes(n):
    n = abs(n); out = []
    k = 2
    while k*k <= n:
        if n % k == 0:
            out.append(k)
            while n % k == 0:
                n //= k
        k += 1
    if n > 1:
        out.append(n)
    return out


def admissible(perm, mat, p):
    a, b, c, d = mat
    if (a*d-b*c) % p == 0:
        return False
    for x in POINTS:
        if (c*x+d) % p == 0:
            return False
        if (a*x+b-perm[x]*(c*x+d)) % p:
            return False
    return True


def lifts(mat, p):
    c, d = mat[2:]
    chars = {pow((c*x+d) % p, (p-1)//2, p) for x in POINTS}
    return chars == {1} or chars == {p-1}


def order(perm):
    current = ID
    n = 0
    while True:
        current = tuple(perm[current[x]] for x in POINTS)
        n += 1
        if current == ID:
            return n
        assert n < 120


def main():
    all_data = {perm: fraction_matrix(perm) for perm in permutations(POINTS)}
    assert len(all_data) == 120
    globally_admissible = [perm for perm, mat in all_data.items()
                          if residuals(perm, mat) == (0, 0)]
    assert globally_admissible == [ID, REV]
    possible_primes = set()
    for perm, mat in all_data.items():
        r = residuals(perm, mat)
        if r != (0, 0):
            possible_primes.update(primes(gcd(*r)))
    assert possible_primes == {2, 3, 5, 7, 11, 13}, possible_primes
    print('120 exact interpolation tests; generic stabilizer:', len(globally_admissible))
    print('exceptional possible prime divisors:', sorted(possible_primes))

    generators = {
        7: (2, 1, 4, 3, 0),
        11: (1, 3, 0, 4, 2),
        13: (0, 2, 3, 1, 4),
    }
    for p, geom, geno in [(7, 6, 3), (11, 10, 5), (13, 6, 3),
                           (17, 2, None), (19, 2, None), (23, 2, None)]:
        allowed = [perm for perm, mat in all_data.items() if admissible(perm, mat, p)]
        lifted = [perm for perm in allowed if lifts(all_data[perm], p)]
        assert len(allowed) == geom and lifted == [ID, REV], (p, len(allowed), lifted)
        assert admissible(REV, all_data[REV], p)
        print('p=%d: branch-stabilizer=%d; rational-image=%d; geometric=%d; rational=%d' %
              (p, len(allowed), len(lifted), 16*len(allowed), 16*len(lifted)))
        if p in generators:
            g = generators[p]
            assert g in allowed and order(g) == geno
            a, b, c, d = all_data[g]
            denom = tuple((c*x+d) % p for x in POINTS)
            chars = tuple('+' if pow(z, (p-1)//2, p) == 1 else '-' for z in denom)
            assert '+' in chars and '-' in chars
            print('  extra generator:', g, 'order:', geno,
                  'matrix:', all_data[g], 'denominators:', denom, 'quadratic classes:', ''.join(chars))
    # Independent direct diagonal equations for all p in a longer safe sample.
    for p in (7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53):
        allowed = [perm for perm, mat in all_data.items() if admissible(perm, mat, p)]
        lifted = [perm for perm in allowed if lifts(all_data[perm], p)]
        assert lifted == [ID, REV]
        assert len(allowed) == ({7:6, 11:10, 13:6}.get(p, 2))
    # Over the quadratic extension all base-field nonzero elements have square roots:
    # for z in Fp*, z^((p^2-1)/2)=(z^((p-1)/2))^(p+1)=1.
    for p in (7,11,13,17,19,23):
        for perm, mat in all_data.items():
            if admissible(perm, mat, p):
                assert all(pow((mat[2]*x+mat[3])%p, (p*p-1)//2, p) == 1
                           for x in POINTS)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
