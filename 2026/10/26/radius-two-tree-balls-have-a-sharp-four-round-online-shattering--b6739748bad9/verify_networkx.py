"""Independent check with NetworkX's nonisomorphic_trees enumerator.
Requires NetworkX: python verify_networkx.py.
The generation, distance calculation and recurrence are separate from verify_pure.py.
"""
from collections import Counter
from functools import cache
import networkx as nx


def dimension(T):
    n = len(T)
    distance = dict(nx.all_pairs_shortest_path_length(T))
    balls = sorted({frozenset(x for x in T if distance[c][x] <= 2) for c in T})
    indicator = [sum(1 << i for i, B in enumerate(balls) if x in B) for x in T]
    @cache
    def ldim(mask):
        if mask.bit_count() <= 1:
            return 0
        best = 0
        for q in indicator:
            yes, no = mask & q, mask & ~q
            if yes and no:
                best = max(best, 1 + min(ldim(yes), ldim(no)))
                if best == mask.bit_count().bit_length()-1:
                    break
        return best
    return ldim((1 << len(balls))-1)


def main():
    trees = list(nx.nonisomorphic_trees(16))
    assert len(trees) == 19320
    census = Counter(dimension(T) for T in trees)
    assert dict(census) == {0: 1, 1: 7, 2: 227, 3: 18516, 4: 569}, census
    print("NETWORKX_VERSION", nx.__version__)
    print("FREE_TREES_16", len(trees))
    print("LDIM_COUNTS_16", sorted(census.items()))
    print("NETWORKX_CENSUS_PASS")


if __name__ == '__main__':
    main()
