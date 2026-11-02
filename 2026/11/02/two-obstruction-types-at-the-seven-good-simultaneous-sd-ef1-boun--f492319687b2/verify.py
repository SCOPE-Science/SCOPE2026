"""Exact finite classification of simultaneous SD-EF1 for two agents and seven goods.

The market order is (0,1,2,3,4,5,6).  A subjective ranking is
represented by its consecutive, internally unordered pairs and final good.
This script requires only Python 3.10+ from the standard library.
"""
from collections import Counter
from itertools import permutations, product
from math import factorial
from fractions import Fraction

N = 7
MARKET_PAIRS = ((0, 1), (2, 3), (4, 5))
REPRESENTATIVES = (
    ((0, 2, 1, 4, 3, 6, 5), (0, 4, 1, 2, 5, 6, 3)),
    ((0, 2, 1, 6, 3, 4, 5), (2, 4, 5, 6, 0, 3, 1)),
)


def market_bundles():
    """All sixteen bundles given to agent 1 that satisfy market SD-EF1."""
    result = []
    for choices in product((0, 1), repeat=4):
        mask = (choices[3] << 6)
        for idx in range(3):
            mask |= 1 << MARKET_PAIRS[idx][choices[idx]]
        result.append(mask)
    assert len(result) == 16 and len(set(result)) == 16
    return tuple(result)


def canonical_pairs():
    """Exactly 7!/2^3 ordered triples of unordered pairs plus a singleton."""
    rows = []
    for order in permutations(range(N)):
        if all(order[2*t] < order[2*t+1] for t in range(3)):
            rows.append(order)
    assert len(rows) == factorial(N) // 8 == 630
    return tuple(rows)


def own_prefix_ok(order, bundle):
    """Direct SD-EF1 prefix test: one's own share never trails by two."""
    owned = 0
    for j, good in enumerate(order, start=1):
        owned += (bundle >> good) & 1
        if owned < j // 2:
            return False
    return True


def sig(order, agent, bundles):
    """Sixteen-bit signature of all compatible market allocations."""
    bits = 0
    for j, mask in enumerate(bundles):
        own = mask if agent == 0 else mask ^ 127
        if own_prefix_ok(order, own):
            bits |= 1 << j
    return bits


def market_group():
    """48 item permutations preserving the set of market pair blocks."""
    maps = []
    for pair_order in permutations(range(3)):
        for flip in product((0, 1), repeat=3):
            f = [None] * 7
            for i in range(3):
                src, dst = MARKET_PAIRS[i], MARKET_PAIRS[pair_order[i]]
                f[src[0]], f[src[1]] = dst[flip[i]], dst[1-flip[i]]
            f[6] = 6
            maps.append(tuple(f))
    assert len(set(maps)) == 48
    return tuple(maps)


def act(order, relabel):
    transformed = tuple(relabel[x] for x in order)
    return tuple(x for j in range(3)
                 for x in sorted(transformed[2*j:2*j+2])) + (transformed[6],)


def orbit(pair, relabelings):
    raw = {(act(pair[0], r), act(pair[1], r)) for r in relabelings}
    return raw | {(second, first) for first, second in raw}


def main():
    orders = canonical_pairs()
    bundles = market_bundles()
    support1 = {p: sig(p, 0, bundles) for p in orders}
    support2 = {p: sig(p, 1, bundles) for p in orders}
    assert len(support1) == len(support2) == 630
    hist = Counter()
    bad = set()
    for p in orders:
        for q in orders:
            count = (support1[p] & support2[q]).bit_count()
            hist[count] += 1
            if not count:
                bad.add((p, q))
    assert sum(hist.values()) == 630 * 630
    assert len(bad) == hist[0] == 96
    refined_hist = {k: v * 64 for k, v in hist.items()}
    assert refined_hist[0] == 6144
    assert sum(refined_hist.values()) == factorial(7) ** 2 == 25401600
    assert sum(k * v for k, v in refined_hist.items()) == 130056192
    assert Fraction(refined_hist[0], factorial(7)**2) == Fraction(8, 33075)
    assert Fraction(sum(k * v for k, v in refined_hist.items()), factorial(7)**2) == Fraction(128, 25)
    symmetries = market_group()
    orbit1, orbit2 = (orbit(rep, symmetries) for rep in REPRESENTATIVES)
    assert len(orbit1) == len(orbit2) == 48
    assert orbit1.isdisjoint(orbit2)
    assert orbit1 | orbit2 == bad
    assert all((p.index(6)//2, q.index(6)//2) == (2, 2) for p,q in orbit1)
    assert all((p.index(6)//2, q.index(6)//2) == (1, 1) for p,q in orbit2)
    # An independent direct allocation test for both orbit representatives,
    # checking every one of the 2^7 (not just market-compatible) allocations.
    for p, q in REPRESENTATIVES:
        direct = []
        for mask in range(128):
            complement = mask ^ 127
            market_ok = (own_prefix_ok(tuple(range(7)), mask) and
                         own_prefix_ok(tuple(range(7)), complement))
            subjective_ok = own_prefix_ok(p, mask) and own_prefix_ok(q, complement)
            if market_ok and subjective_ok:
                direct.append(mask)
        assert not direct
    print('canonical subjective rankings:',len(orders))
    print('canonical profile pairs:',sum(hist.values()))
    print('infeasible canonical pairs:',len(bad))
    print('infeasible strict-ranking profiles:',refined_hist[0])
    print('failure probability:',Fraction(8,33075))
    print('mean number of feasible allocations:',Fraction(128,25))
    print('obstruction orbits:',len(orbit1),len(orbit2))
    print('full histogram (solutions: strict-ranking profiles):')
    for k in sorted(refined_hist):
        print(f'{k}: {refined_hist[k]}')

if __name__ == '__main__':
    main()
