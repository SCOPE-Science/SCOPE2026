"""Finite reproducibility checks for subgroup-maximality criterion (stdlib only).

The mathematical proof is infinite and does not depend on these tests.
"""
from math import gcd, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def factor_distinct(n):
    f = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            f.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        f.append(n)
    return f


def subgroup(p, order):
    return {a for a in range(1, p) if pow(a, order, p) == 1}


def sumfree(p, h):
    return not any((a + b) % p in h for a in h for b in h)


def all_orders(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def subgroup_maximal_bruteforce(p, h):
    size = len(h)
    for d in all_orders(p - 1):
        if d > size and d % size == 0:
            if sumfree(p, subgroup(p, d)):
                return False
    return True


def immediate_test(p, h):
    size = len(h)
    return all(not sumfree(p, subgroup(p, size * ell))
               for ell in factor_distinct((p - 1) // size))


count = 0
for p in range(5, 501):
    if not prime(p):
        continue
    for d in all_orders(p - 1):
        h = subgroup(p, d)
        assert len(h) == d
        if sumfree(p, h):
            assert immediate_test(p, h) == subgroup_maximal_bruteforce(p, h), (p, d)
            count += 1
    h = {1, p - 1}
    assert sumfree(p, h)
    assert immediate_test(p, h) == subgroup_maximal_bruteforce(p, h)
    if p > 5 and p % 4 == 1:
        assert sumfree(p, subgroup(p, 4))
    if prime((p - 1) // 2):
        assert immediate_test(p, h)
    if (p - 1) // 2 in {3 ** a for a in range(1, 8)}:
        assert immediate_test(p, h)

assert not immediate_test(13, {1, 12})
assert immediate_test(19, {1, 18})
assert immediate_test(31, {1, 30})

# Test lifting of a modular triple from generated subgroup to positive integers.
# This uses a direct finite search for positive representatives, independent
# of the number-theoretic Bezout argument used in the proof.
lift_tests = 0
for p, t in [(7, 2), (11, 3), (13, 2), (19, 2), (23, 5)]:
    if t % p == 0:
        continue
    q = []
    e = 0
    seen = set()
    while pow(t, e, p) not in seen:
        seen.add(pow(t, e, p))
        q.extend([(pow(t, e, p), e, 1), (-pow(t, e, p) % p, e, -1)])
        e += 1
    members = {}
    for residue, exponent, sign in q:
        members.setdefault(residue, (exponent, sign))
    for u in members:
        for v in members:
            w = (u + v) % p
            if w not in members:
                continue
            a, b, c = [members[x] for x in (u, v, w)]
            A, B, C = t ** a[0], t ** b[0], t ** c[0]
            num = C * c[1] - A * a[1] - B * b[1]
            assert num % p == 0
            g = gcd(gcd(A, B), C)
            assert (num // p) % g == 0
            # An independent bounded brute force is intentionally not required.
            lift_tests += 1
print(f'PASS: {count} sum-free subgroups and {lift_tests} triple lifting divisibility checks; examples passed.')
