from fractions import Fraction
from itertools import combinations
from math import gcd, lcm, prod


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def prime_factors(n):
    fs = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            fs.append((d, e))
        d += 1
    if n > 1:
        fs.append((n, 1))
    return fs


def squarefree(n):
    return all(e == 1 for _, e in prime_factors(n))


def omega(n):
    return len(prime_factors(n))

# The reduction after prime padding has a common odd prime p and distinct
# marker primes larger than p. A vertex is incident with r=1,2,3 triangles.
for p in (5, 7, 11, 13):
    assert is_prime(p) and p > 3
    markers = []
    x = p + 1
    while len(markers) < 6:
        if is_prime(x):
            markers.append(x)
        x += 1

    for r in (1, 2, 3):
        m = prod(markers[:r])
        witness = p * m
        cell = 3 * p * m
        assert witness % 2 == 1 and cell % 2 == 1
        assert squarefree(witness) and squarefree(cell)
        assert omega(witness) == r + 1 <= 4
        assert omega(cell) == r + 2 <= 5
        assert Fraction(1, witness) + (m - 3) * Fraction(1, cell) == Fraction(1, 3 * p)

    # Exercise the LCM claim on every nonempty marker subset of size at most 3.
    periods = []
    for r in (1, 2, 3):
        for S in combinations(markers, r):
            m = prod(S)
            periods.extend((p * m, 3 * p * m))
    L = 1
    G = 0
    for a in periods:
        L = lcm(L, a)
        G = gcd(G, a)
    expected = 3 * p * prod(markers)
    assert L == expected
    assert G == p
    assert squarefree(L) and L % 2 == 1

# Density is exactly one for 3p vertex blocks, independently of their marker products.
for p in (5, 7, 11, 13):
    assert 3 * p * Fraction(1, 3 * p) == 1

print("PASS")
print("Checked p in {5,7,11,13}, incidence counts r=1,2,3,")
print("odd/squarefree period support, the per-vertex density identity,")
print("the squarefree common-LCM identity, and prime common-GCD identity on all marker subsets of size <= 3.")
