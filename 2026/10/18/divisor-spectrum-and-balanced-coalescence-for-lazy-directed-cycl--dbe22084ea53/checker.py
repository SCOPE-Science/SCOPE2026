"""Finite diagnostic checks for directed-cycle grand couplings.

No finite enumeration is used to prove the general infinite-family theorem.
Execute: python3 checker.py
"""
from itertools import product


def compose(f, g):
    """Composition f after g, with maps represented as image tuples."""
    return tuple(f[i] for i in g)


def semigroup_min_rank(maps, n):
    identity = tuple(range(n))
    visited = {identity}
    queue = [identity]
    minrank = n
    for state in queue:
        minrank = min(minrank, len(set(state)))
        if minrank == 1:
            return 1
        for f in maps:
            nxt = compose(f, state)
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    return minrank


def common_period_count(masks, n):
    return sum(
        all(mask[(i + shift) % n] == mask[i]
            for mask in masks for i in range(n))
        for shift in range(n)
    )


def map_from_mask(mask, n):
    return tuple((i + mask[i]) % n for i in range(n))


assert compose((1, 0), (0, 1)) == (1, 0)
checks = 0
for n in range(2, 9):
    for word in product((0, 1), repeat=n):
        complementary = tuple(1 - b for b in word)
        maps = [map_from_mask(word, n), map_from_mask(complementary, n)]
        rank = semigroup_min_rank(maps, n)
        symmetry_order = common_period_count([word, complementary], n)
        assert rank == symmetry_order, (n, word, rank, symmetry_order)
        assert n % symmetry_order == 0
        checks += 1

# Examples of the full-support construction for each divisor.
for n in range(2, 7):
    for q in range(1, n + 1):
        if n % q:
            continue
        masks = [tuple(word[i % q] for i in range(n))
                 for word in product((0, 1), repeat=q)]
        k = n // q
        assert common_period_count(masks, n) == k
        if q <= 4:
            rank = semigroup_min_rank(
                [map_from_mask(mask, n) for mask in masks], n)
            assert rank == k, (n, q, rank, k)
            checks += 1

print('PASS:', checks, 'exact finite checks, n <= 8')
