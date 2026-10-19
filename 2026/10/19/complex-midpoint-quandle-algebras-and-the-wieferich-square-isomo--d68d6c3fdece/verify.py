#!/usr/bin/env python3
"""Exact standalone checks for Fourier-cycle midpoint-quandle algebra classification.

All group operations and identity tests use integers or prime finite fields.
The infinite-family arguments are given in RESULT.md; this script only
exercises their critical finite identities and explicit witness.
"""
from itertools import product, permutations
from collections import Counter, defaultdict
from math import gcd, prod


def prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def factor(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def order2(n):
    assert n % 2 == 1
    r, x = 0, 1
    while True:
        r += 1
        x = x * 2 % n
        if x == 1:
            return r


def s_p(p):
    d = order2(p)
    v = 0
    z = pow(2, d, p ** 8) - 1
    while z % p == 0:
        v += 1
        z //= p
    return v


def parts(n, at_least=1):
    if not n:
        yield ()
    for k in range(at_least, n + 1):
        for p in parts(n - k, k):
            yield (k,) + p


def group_types(n):
    pp = []
    for p, e in factor(n).items():
        pp.append([tuple(p ** a for a in part) for part in parts(e)])
    return [tuple(sorted(sum(combo, ()))) for combo in product(*pp)]


def cycles_of_group(factors):
    points = list(product(*(range(m) for m in factors)))
    seen = set()
    counts = Counter()
    for x in points:
        if x in seen:
            continue
        y, steps = x, 0
        while y not in seen:
            seen.add(y)
            steps += 1
            y = tuple(2 * a % m for a, m in zip(y, factors))
        assert y == x
        counts[steps] += 1
    assert sum(length * multiplicity for length, multiplicity in counts.items()) == len(points)
    return tuple(sorted(counts.items()))


def local_profile(factors, p):
    ps = []
    for m in factors:
        if m % p == 0:
            exponent = 0
            while m % p == 0:
                m //= p
                exponent += 1
            ps.append(exponent)
    s = s_p(p)
    return tuple(sum(min(t, e) for e in ps) for t in range(s, max(ps, default=0) + 2))


def arithmetic_equivalent(a, b):
    if prod(a) != prod(b):
        return False
    return all(local_profile(a, p) == local_profile(b, p)
               for p in factor(prod(a)))


def direct_group_tests():
    comparisons = 0
    tested = 0
    for size in range(1, 241, 2):
        types = group_types(size)
        c = {group: cycles_of_group(group) for group in types}
        tested += len(types)
        for i, a in enumerate(types):
            for b in types[i:]:
                assert (c[a] == c[b]) == arithmetic_equivalent(a, b), (size, a, b)
                comparisons += 1
    return tested, comparisons


def smallest_prime_congruent_one(m):
    return next(q for q in range(m + 1, 5000) if q % m == 1 and prime(q))


def primitive_root(q):
    return next(g for g in range(2, q) if all(pow(g, (q - 1) // p, q) != 1 for p in factor(q - 1)))


def fourier_test(m):
    # Evaluate F(e_x e_y)(chi) = F(e_x)(chi/2) F(e_y)(chi/2)
    # at every basis pair and every character of the cyclic group.
    q = smallest_prime_congruent_one(m)
    root = pow(primitive_root(q), (q - 1) // m, q)
    assert pow(root, m, q) == 1 and all(pow(root, m // p, q) != 1 for p in factor(m))
    inverse2 = pow(2, -1, m)
    for x, y, k in product(range(m), repeat=3):
        left = pow(root, k * ((x + y) * inverse2 % m), q)
        right = pow(root, (k * inverse2 * x) % m, q) * pow(root, (k * inverse2 * y) % m, q) % q
        assert left == right, (m, x, y, k)
    return q


def evolution_auto_test(m, q):
    # Enumerate exactly all monomial maps of the predicted form and test
    # preservation of each square and distinct-pair product.
    assert (q - 1) % m == 0
    root = primitive_root(q)
    kappa = lambda i: (2 * i) % m
    seen = set()
    cycs = []
    for i in range(m):
        if i in seen:
            continue
        c, j = [], i
        while j not in seen:
            seen.add(j)
            c.append(j)
            j = kappa(j)
        assert j == i
        cycs.append(c)
    groups = defaultdict(list)
    for c in cycs:
        groups[len(c)].append(c)
    target_maps_by_length = []
    for length, cs in groups.items():
        choices = []
        roots = [pow(root, ((q - 1) // gcd(2 ** length - 1, q - 1)) * j, q)
                 for j in range(gcd(2 ** length - 1, q - 1))]
        assert len(set(roots)) == len(roots)
        for matching in permutations(range(len(cs))):
            for shifts in product(range(length), repeat=len(cs)):
                for initial_scalars in product(roots, repeat=len(cs)):
                    mapping = {}
                    scales = {}
                    for cidx, c in enumerate(cs):
                        dest = cs[matching[cidx]]
                        for t, index in enumerate(c):
                            mapping[index] = dest[(t + shifts[cidx]) % length]
                            scales[index] = pow(initial_scalars[cidx], 2 ** t, q)
                    choices.append((mapping, scales))
        target_maps_by_length.append(choices)
    checks = 0
    for block_choice in product(*target_maps_by_length):
        pi = {}
        lam = {}
        for block_p, block_l in block_choice:
            pi.update(block_p)
            lam.update(block_l)
        assert len(pi) == m and len(set(pi.values())) == m
        for i in range(m):
            assert pi[kappa(i)] == kappa(pi[i])
            assert lam[kappa(i)] == lam[i] ** 2 % q
        checks += 1
    expected = prod((2 ** length - 1) ** len(cs) * length ** len(cs)
                    * __import__('math').factorial(len(cs)) for length, cs in groups.items())
    # The field must contain all needed roots of unity.
    assert all((q - 1) % (2 ** length - 1) == 0 for length in groups)
    assert checks == expected, (checks, expected)
    return checks, tuple(sorted((length, len(cs)) for length, cs in groups.items()))


def wieferich_witness():
    p = 1093
    d = order2(p)
    assert d == 364
    assert all(pow(2, d // r, p) != 1 for r in factor(d))
    assert pow(2, d, p ** 2) == 1
    assert pow(2, d, p ** 3) != 1
    assert s_p(p) == 2
    # Both C_(p^2) and C_p x C_p have the same entire doubling-cycle type.
    assert (p * p - 1) % d == 0
    count = (p * p - 1) // d
    assert count == 3282
    for r in range(1, 2 * d + 1):
        f1 = gcd(p * p, 2 ** r - 1)
        f2 = gcd(p, 2 ** r - 1) ** 2
        assert f1 == f2, (r, f1, f2)
    assert tuple(sorted((p * p,))) != tuple(sorted((p, p)))
    return p, d, count


def main():
    ntypes, pairs = direct_group_tests()
    params = [3, 5, 7, 9, 15, 21, 25]
    qlist = [(m, fourier_test(m)) for m in params]
    auto_5 = evolution_auto_test(5, 31)
    auto_7 = evolution_auto_test(7, 29)
    w = wieferich_witness()
    print('VERIFY_OK:', ntypes, 'direct groups /', pairs, 'same-order comparisons;',
          len(qlist), 'exact Fourier identities;',
          'complex-size monomial automorphisms F31/Z5:', auto_5,
          'F29/Z7:', auto_7,
          'Wieferich witness:', w)


if __name__ == '__main__':
    main()
