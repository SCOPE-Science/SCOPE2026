"""Exact-integer reproducibility tests for centered-polygonal semigroup classification.

Run: python3 verify.py
The finite tests supplement, but do not replace, the general proof.
"""
from math import gcd
from heapq import heappop, heappush


def centered(m, n):
    return 1 + m * n * (n - 1) // 2


def apery_invariants(a, b, c):
    # Dijkstra shortest paths in the residue graph modulo the least generator.
    if gcd(gcd(a, b), c) != 1:
        raise ValueError('Generators must be jointly coprime')
    dist = [None] * a
    dist[0] = 0
    heap = [(0, 0)]
    while heap:
        cost, r = heappop(heap)
        if cost != dist[r]:
            continue
        for w in (b, c):
            nxt = (r + w) % a
            cand = cost + w
            if dist[nxt] is None or cand < dist[nxt]:
                dist[nxt] = cand
                heappush(heap, (cand, nxt))
    assert all(v is not None for v in dist)
    frobenius = max(dist) - a
    genus_numer = sum(dist) * 2 - a * (a - 1)
    assert genus_numer % (2 * a) == 0
    genus = genus_numer // (2 * a)
    return frobenius, genus


def in_twogen(target, a, c):
    assert gcd(a, c) == 1
    if a == 1:
        return True
    # The least nonnegative y solving c*y == target modulo a.
    y = (target * pow(c, -1, a)) % a
    return y * c <= target


def oddpart(t):
    while t % 2 == 0:
        t //= 2
    return t


def proper_divisor_count(t):
    return sum(1 for d in range(5, t + 1, 2) if t % d == 0)


# Arithmetic and all possible gluing orientations, including the odd-m exceptions.
checks = 0
for m in range(3, 401):
    for n in range(2, 501):
        a, b, c = (centered(m, j) for j in (n, n + 1, n + 2))
        t = 2 * n + 1
        dab, dbc, dac = gcd(a, b), gcd(b, c), gcd(a, c)
        assert dac == gcd(t, 3 * m + 8)
        assert dab == (2 if m % 2 and n % 4 == 2 else 1)
        assert dbc == (2 if m % 2 and n % 4 == 1 else 1)
        gluing = any((d > 1 and in_twogen(z, x//d, y//d))
                      for x, y, z, d in ((a, b, c, dab), (b, c, a, dbc), (a, c, b, dac)))
        predicted = (3*m+8) % t == 0 or (n == 2 and m in (3, 5, 7))
        assert gluing == predicted, (m, n, dab, dbc, dac, gluing, predicted)
        if (3*m+8) % t == 0:
            assert b == (n+1)*(a//t)+n*(c//t)
        checks += 1

# Independent Apéry enumeration checks symmetry, Frobenius number and genus.
aperies = 0
for m in range(3, 29):
    for n in range(2, 26):
        a, b, c = (centered(m, j) for j in (n, n + 1, n + 2))
        f, g = apery_invariants(a, b, c)
        exceptional = n == 2 and m in (3, 5, 7)
        expected = ((3*m+8) % (2*n+1) == 0) or exceptional
        assert (2*g == f+1) == expected, (m,n,a,b,c,f,g)
        if expected and not exceptional:
            t = 2*n+1
            assert a % t == c % t == 0
            aa, cc = a//t, c//t
            expected_f = t * (aa*cc-aa-cc)+(t-1)*b
            assert f == expected_f
            assert g == (f+1)//2
        aperies += 1

assert apery_invariants(4,10,19) == (25,13)
assert apery_invariants(6,16,31)[1]*2 == apery_invariants(6,16,31)[0]+1
assert apery_invariants(8,22,43)[1]*2 == apery_invariants(8,22,43)[0]+1
assert apery_invariants(5,13,25) == (47,24)
assert apery_invariants(85,109,136) == (2203,1102)
print('VERIFY_OK:', checks, 'exact GCD/gluing cases;', aperies,
      'separate-method Apéry symmetry/genus/Frobenius cases')
