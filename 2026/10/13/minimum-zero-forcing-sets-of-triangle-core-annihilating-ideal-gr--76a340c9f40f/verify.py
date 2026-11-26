"""Finite graph and table checks; the ring classification is analytic."""
from itertools import combinations, product


def neighborhoods(order, edges):
    masks = [0] * order
    for a, b in edges:
        masks[a] |= 1 << b
        masks[b] |= 1 << a
    return masks


def minimum_starters(masks):
    order = len(masks)
    universe = (1 << order) - 1
    for size in range(order + 1):
        good = set()
        for seed in combinations(range(order), size):
            white = universe ^ sum(1 << i for i in seed)
            while white:
                forced = 0
                for i, neighbors in enumerate(masks):
                    if white & (1 << i):
                        continue
                    targets = white & neighbors
                    if targets.bit_count() == 1:
                        forced |= targets
                if not forced:
                    break
                white ^= forced
            if not white:
                good.add(frozenset(seed))
        if good:
            return size, good


def expected(pairs, leaves):
    starters = set()
    for chosen in product(*pairs):
        seeds = frozenset(chosen)
        if len(leaves) == 1:
            extras = {0, leaves[0], *(a+b-i for (a, b), i in zip(pairs, chosen))}
            starters.update(seeds | {i} for i in extras)
        else:
            starters.update(seeds | (set(leaves) - {i}) for i in leaves)
    return starters


def table_formula(n, m):
    if m == 1:
        return n+1, 2**(n-1)*(n+4)
    return n+m-1, m*2**n


for n, m in product(range(1, 7), range(1, 5)):
    order = 2*n+m+1
    pairs = [(2*i+1, 2*i+2) for i in range(n)]
    leaves = list(range(2*n+1, order))
    masks = neighborhoods(order, pairs + [(0, i) for i in range(1, order)])
    size, good = minimum_starters(masks)
    assert good == expected(pairs, leaves), (n, m)
    assert (size, len(good)) == table_formula(n, m), (n, m)

masks = neighborhoods(6, [(0, 1), (1, 2), (0, 2), (0, 3), (1, 4), (2, 5)])
size, good = minimum_starters(masks)
assert size == 2
assert good == ({frozenset(s) for s in combinations(range(3, 6), 2)} |
                {frozenset((i, j)) for i in range(3) for j in range(3, 6) if j != i+3})
assert len(good) == 9

for r in range(1, 6):
    q = 2**(r+1)
    assert q+1 == 2*(2**r)+1  # one of the lines is isotropic
    assert table_formula(2**r, 2) == (2**r+1, 2**(2**r+1))
for p, k in product((3, 5, 7), (1, 2, 3)):
    q = p**k
    assert table_formula((q+1)//2, 1) == ((q+3)//2, 2**((q-1)//2)*((q+9)//2))
    assert table_formula((q-1)//2, 3) == ((q+3)//2, 3*2**((q-1)//2))

print('VERIFY_OK fan_profiles=24 separate_leaf_profiles=1 even_field_substitutions=5 odd_field_sizes=9')
