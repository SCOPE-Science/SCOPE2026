#!/usr/bin/env python3
"""Exact checks for ordered-cycle left/right signature ambiguity.

Run: python3 verify.py
Uses only the Python standard library. Enumeration fixes the first
vertex in the cycle notation, so each n-cycle occurs exactly once.
"""
from collections import Counter, defaultdict
from itertools import permutations, product
from math import factorial


def orbit_signature(p):
    n = len(p)
    positions = list(range(n))
    sig = bytearray()
    for t in range(1, n):
        positions = [p[x] for x in positions]
        sig.extend(int(positions[x] > x) for x in range(n))
    return bytes(sig)


def single_cycle(p):
    n = len(p)
    x, seen = 0, set()
    for _ in range(n):
        assert x not in seen
        seen.add(x)
        x = p[x]
    return x == 0 and len(seen) == n


def enumerate_max(n):
    classes = defaultdict(int)
    for tail in permutations(range(1, n)):
        word = (0,) + tail
        p = [0] * n
        for j, x in enumerate(word):
            p[x] = word[(j + 1) % n]
        classes[orbit_signature(p)] += 1
    hist = Counter(classes.values())
    assert sum(k * v for k, v in hist.items()) == factorial(n - 1)
    return max(classes.values()), len(classes), dict(sorted(hist.items()))


def conjugacies(p, q):
    """All m isomorphisms a with a(p(x)) = q(a(x))."""
    m = len(p)
    src = [0]
    for _ in range(1, m):
        src.append(p[src[-1]])
    ans = []
    for target in range(m):
        dst = [target]
        for _ in range(1, m):
            dst.append(q[dst[-1]])
        a = [None] * m
        for x, y in zip(src, dst):
            a[x] = y
        assert sorted(a) == list(range(m))
        assert all(a[p[x]] == q[a[x]] for x in range(m))
        ans.append(tuple(a))
    assert len(set(ans)) == m
    return ans


def block_lift(family, b):
    """Construct m^(b-1)*len(family)^b cycles on b consecutive blocks."""
    m = len(family[0])
    assert all(len(p) == m and single_cycle(p) for p in family)
    assert len({orbit_signature(p) for p in family}) == 1
    result = []
    for local_cycles in product(family, repeat=b):
        options = [conjugacies(local_cycles[j], local_cycles[j + 1])
                   for j in range(b - 1)]
        for trans in product(*options):
            n = b * m
            f = [None] * n
            for j, a in enumerate(trans):
                for x in range(m):
                    f[j*m + x] = (j + 1)*m + a[x]
            # Composition of the first b-1 conjugacies, from block 0 to b-1.
            path = list(range(m))
            for a in trans:
                path = [a[y] for y in path]
            # The last return makes f^b on block 0 equal local_cycles[0].
            for x in range(m):
                f[(b - 1)*m + path[x]] = local_cycles[0][x]
            f = tuple(f)
            assert single_cycle(f)
            result.append(f)
    count = m**(b - 1) * len(family)**b
    assert len(result) == count
    assert len(set(result)) == count
    assert len({orbit_signature(p) for p in result}) == 1
    return result


def two_prime_family(p):
    """Independent bitwise construction for the semiprime theorem."""
    result = []
    for bits in product(range(2), repeat=p - 1):
        f = [None] * (2 * p)
        for j, epsilon in enumerate(bits):
            for s in range(2):
                f[2*j + s] = 2*(j + 1) + (s ^ epsilon)
        parity = 1
        for epsilon in bits:
            parity ^= epsilon
        for s in range(2):
            f[2*(p - 1) + s] = s ^ parity
        result.append(tuple(f))
    assert len(result) == 2**(p-1)
    assert len(set(result)) == len(result)
    assert all(single_cycle(f) for f in result)
    assert len({orbit_signature(f) for f in result}) == 1
    return result


def main():
    for n, expected in [(2,1), (3,1), (4,2), (5,1), (6,4),
                        (7,1), (8,16), (9,9), (10,16)]:
        maxi, classes, hist = enumerate_max(n)
        assert maxi == expected
        print('EXHAUSTIVE n=%d cycles=%d classes=%d maximum=%d distribution=%s'
              % (n, factorial(n - 1), classes, maxi, hist), flush=True)
    base = [(1, 0)]
    c4 = block_lift(base, 2)
    c8 = block_lift(c4, 2)
    c16 = block_lift(c8, 2)
    c6 = block_lift(base, 3)
    c9 = block_lift([(1,2,0)], 3)
    for n, family, expected in [(4,c4,2),(6,c6,4),(8,c8,16),
                                (9,c9,9),(16,c16,2048)]:
        assert len(family) == expected
        print('CONSTRUCTIVE n=%d indistinguishable_cycles=%d' % (n, expected))
    for p in (3, 5, 7, 11):
        witnesses = two_prime_family(p)
        print('SEMIPRIME n=%d witnesses=%d signatures=1' %
              (2*p,len(witnesses)))
    print('VERIFIED')


if __name__ == '__main__':
    main()
