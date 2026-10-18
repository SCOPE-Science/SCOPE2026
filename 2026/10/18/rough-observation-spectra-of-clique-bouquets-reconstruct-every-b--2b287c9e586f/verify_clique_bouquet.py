"""Reproducible finite checks for the clique-bouquet rough-observation theorem."""
from collections import Counter
from itertools import product
from math import prod, log2


def recover_factors(full_products, r):
    target = Counter(full_products)
    built = Counter({1: 1})
    factors = []
    for _ in range(r):
        diff = target - built
        assert diff
        a = min(diff)
        assert a > 1
        new = Counter(built)
        for p, c in built.items():
            new[p * a] += c
        built = new
        factors.append(a)
    assert built == target
    return sorted(factors)


def verify(profile):
    r = len(profile)
    n = 1 + sum(profile)
    blades = []
    idx = 1
    for s in profile:
        blades.append(tuple(range(idx, idx+s)))
        idx += s
    neighborhoods = [set(range(n))]
    for b in blades:
        bset = set(b)
        for _ in b:
            neighborhoods.append({0} | bset)
    assert len(neighborhoods) == n
    fibers = Counter()
    for mask in range(1 << n):
        x = {v for v in range(n) if mask & (1 << v)}
        lower = tuple(i for i, neighborhood in enumerate(neighborhoods) if neighborhood <= x)
        upper = tuple(i for i, neighborhood in enumerate(neighborhoods) if neighborhood & x)
        fibers[(lower, upper)] += 1
    a = [2 ** s - 1 for s in profile]
    p = prod(a)
    expect = Counter({1: 2, 2 * p: 1})
    subset_products = []
    for bitmask in range(1 << r):
        sub = prod(a[i] for i in range(r) if bitmask & (1 << i))
        subset_products.append(sub)
        if bitmask not in (0, (1 << r)-1):
            expect[sub] += 2
    assert Counter(fibers.values()) == expect, (profile, Counter(fibers.values()), expect)
    assert len(fibers) == 2 ** (r+1) - 1
    assert fibers[((), tuple(range(n)))] == 2 * p
    others = [(k, v) for k, v in fibers.items() if k != ((), tuple(range(n)))]
    second = p // min(a)
    assert max(v for _, v in others) == second
    assert sum(v == second for _, v in others) == 2 * sum(x == min(a) for x in a)
    assert recover_factors(subset_products, r) == sorted(a)
    assert sum(k*v for k,v in expect.items()) == (1 << n)
    return len(fibers), 1 << n


def main():
    cases = 0
    inputs = 0
    for r in range(2, 5):
        for profile in product(range(2, 6), repeat=r):
            if 1+sum(profile)>13:
                continue
            _, q = verify(profile)
            cases += 1
            inputs += q
    for profile in [(2,2,2,2,2), (2,2,2,3), (2,3,5), (3,3,5), (2,2,7)]:
        _, q = verify(profile)
        cases += 1
        inputs += q
    print('VERIFY_OK profiles=',cases,'vertex_subsets=',inputs,'fiber_spectrum=PASS central_uniqueness=PASS runnerup=PASS size_reconstruction=PASS')


if __name__ == '__main__':
    main()
