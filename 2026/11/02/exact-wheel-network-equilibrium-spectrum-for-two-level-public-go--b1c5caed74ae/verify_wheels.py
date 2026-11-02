#!/usr/bin/env python3
"""Independent finite checks of exact wheel public-goods equilibrium counts.

Use: python3 verify_wheels.py
Standard library only. This is corroboration of, not a substitute for, the all-size proof.
"""
from itertools import product
from math import comb


def cyclic_mis_count(m, k):
    """Combinatorial formula, with out-of-range binomial coefficients zero."""
    if k <= 0 or not (0 <= m-2*k <= k):
        return 0
    num = m * comb(k, m-2*k)
    assert num % k == 0
    return num // k


def predicted(m, r):
    assert m >= 3 and r >= 2
    if r == 2:
        return 2 + 3*int(m % 3 == 0 and m != 6) + 3*int(m == 3)
    P = sum(cyclic_mis_count(m,k) for k in range(1,m+1))
    return 1 + P - cyclic_mis_count(m,r) + int(m == r == 3)


def direct_count(m,r):
    """Use open neighbor lists and test each binary state against the local rule."""
    neigh = [((v - 1) % m, (v + 1) % m, m) for v in range(m)]
    neigh.append(tuple(range(m)))
    count = 0
    all_tests = 0
    for bits in product((0,1), repeat=m+1):
        all_tests += 1
        if all(bits[v] == int(sum(bits[w] for w in neigh[v]) in (0,r))
               for v in range(m+1)):
            count += 1
    return count, all_tests


def direct_cycle_mis(m):
    """No use of the cyclic-composition formula or game equations."""
    counts = {}
    for bits in product((0,1),repeat=m):
        if all(not (bits[i] and bits[(i+1)%m]) for i in range(m)) \
           and all(bits[i] or bits[(i-1)%m] or bits[(i+1)%m] for i in range(m)):
            k=sum(bits)
            counts[k]=counts.get(k,0)+1
    return counts


def main():
    profiles = 0
    cases = 0
    for m in range(3,14):
        for r in range(2,m+3):
            actual, n = direct_count(m,r)
            profiles += n
            cases += 1
            expect = predicted(m,r)
            assert actual == expect, (m,r,actual,expect)
            if actual == 1:
                assert (m,r) == (7,3), (m,r)
    assert predicted(7,3) == 1

    cycle_cases = 0
    for m in range(3,19):
        table=direct_cycle_mis(m)
        expect={k:cyclic_mis_count(m,k) for k in range(1,m+1)
                if cyclic_mis_count(m,k)>0}
        assert table == expect, (m, table, expect)
        cycle_cases+=1

    perrin = {3:3,4:2,5:5}
    for m in range(6,101):
        perrin[m]=perrin[m-2]+perrin[m-3]
    for m in range(3,101):
        assert perrin[m] == sum(cyclic_mis_count(m,k) for k in range(1,m+1))
    print(f"OK: {cases} wheel parameter cases; {profiles} full binary profiles; "
          f"{cycle_cases} independently enumerated cycle tables; "
          "98 Perrin values; unique equilibrium only at (m,r)=(7,3) within tests")


if __name__ == '__main__':
    main()
