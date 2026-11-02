#!/usr/bin/env python3
"""Direct finite tests for generator counts of permutation tense algebras.

No external packages. All direct checks use full closure under Boolean/tense
operations, not a necklace or itinerary criterion.
"""
from itertools import permutations, product
from collections import Counter
from math import comb, factorial, exp, log


def moebius(d):
    p = 2
    s = 1
    while p * p <= d:
        if d % p == 0:
            d //= p
            if d % p == 0:
                return 0
            s = -s
        p += 1
    if d > 1:
        s = -s
    return s


def necklace_primitive(n, q):
    return sum(moebius(d) * q ** (n // d) for d in range(1, n + 1) if n % d == 0) // n


def cycle_multiplicities(perm):
    visited = set()
    result = Counter()
    for x in range(len(perm)):
        if x not in visited:
            y = x
            n = 0
            while y not in visited:
                visited.add(y)
                n += 1
                y = perm[y]
            assert y == x
            result[n] += 1
    return result


def predicted_count(perm, k):
    q = 1 << k
    val = 1
    for n, m in cycle_multiplicities(perm).items():
        p = necklace_primitive(n, q)
        for j in range(m):
            val *= n * (p - j)
    return val


def full_generation_by_closure(perm, colors, k):
    n = len(perm)
    full = (1 << n) - 1
    inv = [0] * n
    for u, v in enumerate(perm):
        inv[v] = u
    start = {0, full}
    for i in range(k):
        start.add(sum(((col >> i) & 1) << x for x, col in enumerate(colors)))
    sub = set(start)
    while True:
        new = set(sub)
        for a in sub:
            new.add(full ^ a)
            new.add(sum(((a >> perm[x]) & 1) << x for x in range(n)))  # forward diamond
            new.add(sum(((a >> inv[x]) & 1) << x for x in range(n)))   # backward diamond
            for b in sub:
                new.add(a | b)
                new.add(a & b)
        if len(new) == len(sub):
            break
        sub = new
    return len(sub) == (1 << n)


def direct_count(perm, k):
    q = 1 << k
    return sum(full_generation_by_closure(perm, colors, k)
               for colors in product(range(q), repeat=len(perm)))


def validate_tense_axioms(perm):
    n = len(perm)
    full = (1 << n) - 1
    inv = [0] * n
    for u, v in enumerate(perm):
        inv[v] = u
    F = lambda a: sum(((a >> perm[x]) & 1) << x for x in range(n))
    P = lambda a: sum(((a >> inv[x]) & 1) << x for x in range(n))
    G = lambda a: full ^ F(full ^ a)
    H = lambda a: full ^ P(full ^ a)
    assert G(full) == H(full) == full
    for a in range(1 << n):
        assert F(full ^ a) == (full ^ G(a))
        assert P(full ^ a) == (full ^ H(a))
        assert a & G(P(a)) == a
        assert a & H(F(a)) == a
        for b in range(1 << n):
            assert G(a & b) == G(a) & G(b)
            assert H(a & b) == H(a) & H(b)


def log_probability(n, q, m):
    if m == 0: return 0.0
    p = necklace_primitive(n, q)
    if m > p: return float('-inf')
    return m * log(n * p / q ** n) + sum(log(1 - j / p) for j in range(m))


def run():
    cases = 0
    masks = 0
    for n in range(1, 6):
        for perm in permutations(range(n)):
            ks = [0, 1, 2] if n <= 4 else [0, 1]
            validate_tense_axioms(perm)
            for k in ks:
                actual = direct_count(perm, k)
                expected = predicted_count(perm, k)
                assert actual == expected, (n, perm, k, actual, expected)
                cases += 1
                masks += (1 << k) ** n
    print('FINITE_GENERATION_OK', 'permutation_generator_cases='+str(cases), 'tuples='+str(masks))
    for n, m in [(1, 4), (2, 2), (3, 2), (4, 1), (4, 2)]:
        perm = tuple(j + 1 if (j + 1) % n else j + 1 - n for j in range(n)) * m
        # Correct labels for disjoint cycles.
        perm = tuple(b + (i + 1) % n for b in range(0, n*m, n) for i in range(n))
        k = 2
        print('EXAMPLE', 'cycle_length='+str(n), 'multiplicity='+str(m), 'k='+str(k), 'count='+str(predicted_count(perm,k)))
    for n in [1, 2, 3, 4, 6]:
        for q in [64, 256]:
            m = max(1, round(.75 * q ** (n/2)))
            if m > 200000:
                continue
            probability = exp(log_probability(n, q, m))
            target = exp(-.75*(n%2==0) - n*.75*.75/2)
            print('ASYMPTOTIC_CHECK', n, q, m, format(probability, '.8f'), format(target, '.8f'))
    print('ALL_CHECKS_OK')

if __name__ == '__main__': run()
