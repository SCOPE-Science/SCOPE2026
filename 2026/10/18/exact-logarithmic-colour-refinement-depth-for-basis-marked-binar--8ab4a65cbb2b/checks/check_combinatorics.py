"""Independent incidence-type counting, without constructing a graph or calling 1-WL.

Usage: python checks/check_combinatorics.py
No external modules required.
"""
from collections import Counter
from math import ceil, log2


def signature(x, d, named):
    # An incidence line through x is {x,y,x xor y}; each pair {y,x xor y}
    # is counted once by taking y < x xor y.
    result = Counter()
    for y in range(1, 1 << d):
        z = x ^ y
        if not z or y >= z:
            continue
        result[tuple(sorted(v for v in (y,z) if v in named))] += 1
    return tuple(sorted(result.items()))


def main():
    comparisons = 0
    for d in range(2, 11):
        full = set(range(1, 1 << d))
        limit = ceil(log2(d-1)) if d>2 else 0
        for k in range(limit):
            named = {x for x in full if x.bit_count() <= (1 << k)}
            reachable = {x ^ y for x in named for y in named if x != y}
            next_named = named | reachable
            expected = {x for x in full if x.bit_count() <= (1 << (k+1))}
            assert next_named == expected, (d,k,'closure mismatch')
            signatures = {x:signature(x,d,named) for x in full - named}
            unknown = set(signatures) - reachable
            unknown_types = {signatures[x] for x in unknown}
            assert len(unknown_types) <= 1, (d,k,'residual not uniform')
            # The new vertices have pair-specific line colors; verify
            # their signatures cannot coincide with any other vertex.
            groups = {}
            for x, sig in signatures.items():
                groups.setdefault(sig, []).append(x)
            assert sorted(sorted(v) for v in groups.values()) == sorted(
                [[x] for x in reachable - named] + ([sorted(unknown)] if unknown else [])
            ), (d,k,'predicted point split mismatch')
            comparisons += len(signatures)
    print('PASS algebraic doubling and anonymous incidence signatures; dimensions 2..10; cases', comparisons)
    for d in range(3, 18):
        k = ceil(log2(d-1))
        t = 1 << (k-1)
        # When d is larger than t+2, two lines with the same sole named
        # point x must exist. Enumerate the explicit construction.
        if d > t+2:
            assert t >= 2
            x = 3
            H = [h for h in range(1,1<<d) if h & 3 == 0 and h.bit_count()==t]
            assert len(H) >= 2
            lines = {(h | 1,h | 2,x) for h in H}
            assert len(lines) >= 2
            assert all(a.bit_count()>t and b.bit_count()>t and a^b==x for a,b,_ in lines)
    print('PASS late-round line collision construction; dimensions 3..17')

if __name__ == '__main__':
    main()
