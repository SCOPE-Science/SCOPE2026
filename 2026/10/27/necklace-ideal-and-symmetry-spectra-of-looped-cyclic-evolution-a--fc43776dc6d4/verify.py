"""Exact finite checks for looped cyclic evolution algebras.

Requires Python 3 standard library only. These finite tests do not replace the
proof for arbitrary fields and dimensions.
"""
from itertools import product
from math import gcd, factorial


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def phi(n):
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))


def mobius(n):
    primes = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            n //= d
            if n % d == 0:
                return 0
            primes.append(d)
        d += 1
    if n > 1:
        primes.append(n)
    return (-1) ** len(primes)


def rotation_orbit(word):
    n = len(word)
    return {word[r:] + word[:r] for r in range(n)}


def minimal_period(word):
    n = len(word)
    return min(m for m in divisors(n) if all(word[i] == word[i % m] for i in range(n)))


def predicted(q, n):
    Q = q - 1
    total = sum(phi(e) * Q ** (n // e) for e in divisors(n)) // n
    sing = sum(phi(e) * gcd(e, Q) * Q ** (n // e - 1) for e in divisors(n)) // n
    breakdown = {}
    for m in divisors(n):
        at = sum(mobius(m // d) * Q ** d for d in divisors(m))
        ass = sum(mobius(m // d) * Q ** (d - 1) * gcd(n // d, Q) for d in divisors(m))
        assert at % m == ass % m == 0
        breakdown[m] = ((at - ass) // m, ass // m)
    assert sum(x for x, y in breakdown.values()) == total - sing
    assert sum(y for x, y in breakdown.values()) == sing
    return total, sing, breakdown


def rank_mod_prime(M, p):
    a = [[v % p for v in row] for row in M]
    h = len(a)
    w = len(a[0])
    r = 0
    for j in range(w):
        pivot = next((i for i in range(r, h) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][j], -1, p)
        a[r] = [v * inv % p for v in a[r]]
        for i in range(h):
            if i != r and a[i][j]:
                s = a[i][j]
                a[i] = [(a[i][k] - s * a[r][k]) % p for k in range(w)]
        r += 1
        if r == h:
            break
    return r


def algebra_product(u, v, c, p):
    n = len(c)
    out = [0] * n
    for i in range(n):
        x = (u[i] * v[i]) % p
        out[i] = (out[i] + x) % p
        out[(i + 1) % n] = (out[(i + 1) % n] + c[i] * x) % p
    return tuple(out)


def automorphisms_by_matrices(c, p):
    n = len(c)
    assert n == 3
    count = 0
    for entries in product(range(p), repeat=n * n):
        cols = [tuple(entries[n * i + j] for i in range(n)) for j in range(n)]
        # Test multiplication before invertibility to avoid unnecessary elimination.
        if any(algebra_product(cols[i], cols[j], c, p) != (0,) * n
               for i in range(n) for j in range(i + 1, n)):
            continue
        if any(algebra_product(cols[i], cols[i], c, p)
               != tuple((cols[i][j] + c[i] * cols[(i + 1) % n][j]) % p for j in range(n))
               for i in range(n)):
            continue
        if rank_mod_prime(cols, p) == n:
            count += 1
    return count


def verify():
    tested = 0
    for q in (2, 3, 5, 7):
        Q = q - 1
        # Count color orbits using exponents of cyclic multiplicative group.
        # (-1)^n is exponent Q/2 for n odd and q odd, and exponent zero otherwise.
        for n in range(3, 9):
            if Q ** n > 180000:
                continue
            seen = set()
            by_period = {m: [0, 0] for m in divisors(n)}
            for word in product(range(Q), repeat=n):
                if word in seen:
                    continue
                orbit = rotation_orbit(word)
                seen.update(orbit)
                m = minimal_period(word)
                exponent = sum(word) % Q
                target = Q // 2 if (n % 2 and q % 2) else 0
                singular = exponent == target
                by_period[m][int(singular)] += 1
            expected_total, expected_sing, expected = predicted(q, n)
            assert len(seen) == Q ** n
            assert sum(map(sum, by_period.values())) == expected_total
            assert sum(v[1] for v in by_period.values()) == expected_sing
            assert {m: tuple(v) for m, v in by_period.items()} == expected, (q, n)
            tested += 1
    # Direct ranks and cyclic-scaling normalizations of arbitrary edge weights.
    for p in (2, 3, 5):
        n = 3
        for a in product(range(1, p), repeat=n):
            for b in product(range(1, p), repeat=n):
                c = tuple((b[i] * a[(i + 1) % n] * pow(a[i], -2, p)) % p for i in range(n))
                # Original matrix rows are a_i e_i+b_i e_(i+1).
                M = [[0] * n for _ in range(n)]
                for i in range(n):
                    M[i][i] = a[i]
                    M[i][(i + 1) % n] = b[i]
                singular = (1 - (-1) ** n * __import__('math').prod(c)) % p == 0
                assert rank_mod_prime(M, p) == n - int(singular)
                assert (rank_mod_prime(M, p) == n) == ((__import__('math').prod(a) - (-1)**n * __import__('math').prod(b)) % p != 0)
    # Check every linear automorphism in GL_3(F_2) and GL_3(F_3) without assuming monomiality.
    for p in (2, 3):
        for c in product(range(1, p), repeat=3):
            predicted_aut = 3 // minimal_period(c)
            actual = automorphisms_by_matrices(c, p)
            assert actual == predicted_aut, (p, c, actual, predicted_aut)
    print('VERIFY_OK: necklace, singularity, symmetry spectra and unrestricted-matrix automorphisms;', tested, 'necklace configurations')


if __name__ == '__main__':
    verify()
