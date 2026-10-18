"""Independent finite tests for implication-algebra endomorphism rank and idempotent counts.
Run: python3 verify.py  (standard library only)."""
import itertools
import math
from collections import Counter
from functools import reduce


def stirling(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return stirling(n-1, k-1) + k * stirling(n-1, k)


def closed_form(n):
    c = Counter({(1 << n) - 1: math.factorial(n)})
    idem = 1
    for r in range(n):
        c[1 << r] += math.comb(n, r) * math.factorial(r+1) * stirling(n, r+1)
        idem += math.comb(n, r) * ((r+1)**(n-r) - r**(n-r))
    assert sum(c.values()) == (n+1)**n - n**n + math.factorial(n)
    return c, idem


def from_generators(n):
    """Enumerate ALL join-preserving mappings using images of singleton generators.
    Then independently test the defining binary implication equation."""
    full = (1 << n) - 1
    elems = range(1, full + 1)
    counts = Counter()
    idem = 0
    valid = set()
    for atoms in itertools.product(elems, repeat=n):
        if reduce(int.__or__, atoms, 0) != full:
            continue
        mapping = [0] * (full+1)
        for mask in elems:
            i = (mask & -mask).bit_length() - 1
            mapping[mask] = mapping[mask ^ (1 << i)] | atoms[i]
        # Implication, NOT just join or existing-meet preservation.
        if not all(mapping[(full ^ x) | y] == ((full ^ mapping[x]) | mapping[y])
                   for x in elems for y in elems):
            continue
        v = tuple(mapping[1:])
        assert v not in valid
        valid.add(v)
        counts[len(set(v))] += 1
        idem += all(mapping[mapping[x]] == mapping[x] for x in elems)
    return counts, idem


def normal_form(n):
    """Independent enumeration of all pointed maps, including forbidden cases."""
    full = (1 << n)-1
    counts = Counter()
    idem = 0
    for vals in itertools.product(range(n+1), repeat=n):
        if 0 not in vals and set(vals) != set(range(1,n+1)):
            continue
        result = []
        for x in range(1, full+1):
            result.append(sum(1 << j for j,v in enumerate(vals) if v == 0 or x & (1 << (v-1))))
        counts[len(set(result))] += 1
        idem += all(vals[v-1] == v if v else True for v in vals)
    return counts, idem


def run():
    for n in (2,3,4):
        expected = closed_form(n)
        direct = from_generators(n)
        pointed = normal_form(n)
        assert expected == direct == pointed, (n,expected,direct,pointed)
        print("n=%d endomorphisms=%d idempotents=%d image_size_counts=%s" %
              (n,sum(expected[0].values()),expected[1],dict(sorted(expected[0].items()))))
    print("VERIFY_OK")

if __name__ == '__main__':
    run()
