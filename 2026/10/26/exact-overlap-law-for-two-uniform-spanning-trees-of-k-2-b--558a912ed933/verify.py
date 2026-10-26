"""Exhaustive finite checks of the exact overlap law on K_(2,b)."""
from fractions import Fraction
from math import comb
from collections import Counter


def trees(b):
    # Edge (hub, spoke) has index 2*spoke+hub.
    # Exactly one spoke joins both hubs; every other spoke joins one.
    for bridge in range(b):
        rest = [x for x in range(b) if x != bridge]
        for bits in range(1 << (b - 1)):
            es = {2*bridge, 2*bridge + 1}
            for i, v in enumerate(rest):
                es.add(2*v + ((bits >> i) & 1))
            yield frozenset(es)


def prediction(b, k):
    # X=2+Bin(b-2,1/2)+Ber(1/(2b)), terms independent.
    p = Fraction(1, 2*b)
    j = k-2
    a = Fraction(comb(b-2,j), 2**(b-2)) if 0<=j<=b-2 else Fraction(0)
    c = Fraction(comb(b-2,j-1), 2**(b-2)) if 0<=j-1<=b-2 else Fraction(0)
    return (1-p)*a+p*c


def verify():
    for b in range(2, 7):
        all_trees = list(trees(b))
        assert len(all_trees) == b * 2**(b-1)
        assert len(set(all_trees)) == len(all_trees)
        assert all(len(t) == b+1 for t in all_trees)
        pairs = len(all_trees)**2
        cnt = Counter(len(t & u) for t in all_trees for u in all_trees)
        assert set(cnt) == set(range(2,b+2))
        assert sum(cnt.values()) == pairs
        for k in range(2,b+2):
            assert Fraction(cnt[k], pairs) == prediction(b,k), (b,k,cnt[k])
        mean = sum(Fraction(k*cnt[k], pairs) for k in cnt)
        variance = sum(Fraction(k*k*cnt[k], pairs) for k in cnt) - mean**2
        assert mean == Fraction((b+1)**2, 2*b)
        assert variance == Fraction((b-1)*(b*b-b+1), 4*b*b)
        shifted = {k: Fraction(comb(b-2,k-2), 2**(b-2))
                   if 0 <= k-2 <= b-2 else Fraction(0)
                   for k in range(2,b+2)}
        tv = sum(abs(Fraction(cnt[k],pairs)-shifted[k]) for k in shifted)/2
        assert tv == Fraction(comb(b-2,(b-2)//2), 2*b*2**(b-2))
        # The exact probability of the maximum b+1 common edges is
        # the collision event of selecting the same entire tree.
        assert cnt[b+1] == len(all_trees)
        print(f'b={b}: trees={len(all_trees)}, pairs={pairs}, overlap_counts={dict(sorted(cnt.items()))}: OK')
    print('ALL_EXACT_CHECKS_PASSED')

if __name__ == '__main__':
    verify()
