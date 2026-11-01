"""Exact checks for prime-base simplex Fourier null frequencies.
Run: python3 verify_zero_density.py (standard library only).
"""
from itertools import product
from math import factorial


def expected_vanish(vector, p, L):
    for v in range(L):
        q = p ** (v + 1)
        if sorted((x // p**v) % p for x in vector if x % (p**v) == 0) == list(range(1, p)) and all(x % p**v == 0 for x in vector):
            return True
    return False


def first_zero_mask(vector, p, L):
    # Independently perform exact monic polynomial division by
    # Phi_{p^j}(z) = 1 + z^(p^(j-1)) + ... + z^((p-1)*p^(j-1)).
    for j in range(1, L+1):
        q = p ** j
        coeffs = [0] * q
        coeffs[0] += 1
        for x in vector: coeffs[x % q] += 1
        cyclo = [0] * (q - q // p + 1)
        for r in range(p): cyclo[r * (q // p)] = 1
        d = len(cyclo) - 1
        for k in range(q-1, d-1, -1):
            f = coeffs[k]
            if f:
                for i, c in enumerate(cyclo):
                    if c:
                        coeffs[k - d + i] -= f * c
        if not any(coeffs):
            return True
    return False


def main():
    checks = 0
    for p, L in ((2, 7), (3, 4), (5, 1)):
        d = p - 1
        q = p ** L
        actual = 0
        for vector in product(range(q), repeat=d):
            criterion = expected_vanish(vector, p, L)
            assert criterion == first_zero_mask(vector, p, L), (p, L, vector)
            actual += criterion
            checks += 1
        predicted = factorial(d) * (p**(L*d) - 1) // (p**d - 1)
        assert actual == predicted, (p, L, actual, predicted)
    # Exhaustive modular census for base five through two levels (390625 tuples).
    p, L, d = 5, 2, 4
    actual = sum(expected_vanish(x, p, L) for x in product(range(25), repeat=d))
    assert actual == factorial(d) * (p**(L*d) - 1) // (p**d - 1)
    # More prime-power cyclotomic divisibility tests, at independently selected vectors.
    for p, L in ((5, 2), (7, 2)):
        q = p ** L
        d = p-1
        for i in range(500):
            x = tuple((i**3 + 17*i*(j+1) + 71*j*j + j) % q for j in range(d))
            assert expected_vanish(x,p,L) == first_zero_mask(x,p,L)
            checks += 1
    print('PRIME_SIMPLEX_FOURIER_NULL_DENSITY_OK',checks,
          'exhaustive finite characters plus 1000 higher prime-power divisibility comparisons')

if __name__ == '__main__': main()
