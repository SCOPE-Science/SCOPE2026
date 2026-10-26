#!/usr/bin/env python3
"""Verify a four-state tree automaton's strong synchronization threshold.

A full-context variable has an arbitrary state of Q at each leaf. Images of
independent child contexts combine by Cartesian product.
"""

Q = frozenset(range(4))
W = (1, 3, 0, 2)
F = ((0, 2, 2, 3),
     (2, 2, 2, 3),
     (2, 3, 3, 0),
     (3, 3, 2, 3))
EXPECTED_NEW_MASKS = (15, 13, 7, 11, 14, 12, 5, 3, 10, 9, 6, 4)


def as_mask(s):
    return sum(1 << x for x in s)


def word_image(a):
    return frozenset(W[x] for x in a)


def fork_image(a, b):
    return frozenset(F[x][y] for x in a for y in b)


def layer_reach():
    """Enumerate the images of all full contexts of bounded height."""
    reachable = {Q}
    images = [Q]
    for height in range(1, 12):
        next_reachable = set(reachable)
        for a in reachable:
            next_reachable.add(word_image(a))
            for b in reachable:
                next_reachable.add(fork_image(a, b))
        new = next_reachable - reachable
        assert len(new) == 1, (height, sorted(new))
        only = new.pop()
        assert as_mask(only) == EXPECTED_NEW_MASKS[height], (height, only)
        images.append(only)
        reachable = next_reachable
        if height < 11:
            assert all(len(s) > 1 for s in reachable)
    assert len(reachable) == 12
    assert {s for s in reachable if len(s) == 1} == {frozenset({2})}
    assert {s for s in reachable if len(s) > 1} == {
        frozenset(i for i in Q if mask & (1 << i))
        for mask in range(1, 16) if mask.bit_count() > 1
    }
    return images


def independent_min_height():
    """Compute least height by weighted min/max relaxation, not layer search."""
    all_masks = range(1, 16)
    costs = [10 ** 9] * 16
    costs[15] = 0
    while True:
        changes = 0
        for a in all_masks:
            if costs[a] == 10 ** 9:
                continue
            sub_a = {i for i in Q if a & (1 << i)}
            wa = as_mask(word_image(sub_a))
            next_cost = costs[a] + 1
            if next_cost < costs[wa]:
                costs[wa] = next_cost
                changes += 1
            for b in all_masks:
                if costs[b] == 10 ** 9:
                    continue
                sub_b = {i for i in Q if b & (1 << i)}
                ab = as_mask(fork_image(sub_a, sub_b))
                next_cost = max(costs[a], costs[b]) + 1
                if next_cost < costs[ab]:
                    costs[ab] = next_cost
                    changes += 1
        if not changes:
            break
    assert costs[4] == 11
    assert all(costs[x] > 11 for x in (1, 2, 8))
    assert min(costs[x] for x in (1, 2, 4, 8)) == 11
    assert tuple(costs[m] for m in EXPECTED_NEW_MASKS) == tuple(range(12))
    return costs


def explicit_full_context():
    """Build the witness tree; each 'v' leaf is a fresh distinct variable."""
    t = [None] * 12
    t[0] = 'v'
    t[1] = ('f', t[0], t[0])
    for i in (2, 3, 4):
        t[i] = ('w', t[i - 1])
    t[5] = ('f', t[4], t[2])
    for i in (6, 7, 8):
        t[i] = ('w', t[i - 1])
    t[9] = ('f', t[5], t[8])
    t[10] = ('w', t[9])
    t[11] = ('f', t[7], t[10])

    serial = iter(range(1000000))

    def freshen(tree):
        if tree == 'v':
            return ('var', next(serial))
        return (tree[0],) + tuple(freshen(child) for child in tree[1:])

    def inspect(tree):
        if tree[0] == 'var':
            return 0, 1, Q
        if tree[0] == 'w':
            h, leaves, image = inspect(tree[1])
            return h + 1, leaves, word_image(image)
        h1, leaves1, a = inspect(tree[1])
        h2, leaves2, b = inspect(tree[2])
        return max(h1, h2) + 1, leaves1 + leaves2, fork_image(a, b)

    heights = []
    for k, tree in enumerate(t):
        h, _, s = inspect(freshen(tree))
        assert h == k
        assert as_mask(s) == EXPECTED_NEW_MASKS[k]
        heights.append(h)
    concrete = freshen(t[11])
    height, leaves, image = inspect(concrete)
    assert (height, leaves, image) == (11, 12, frozenset({2}))
    return height, leaves, image


if __name__ == '__main__':
    images = layer_reach()
    costs = independent_min_height()
    height, leaves, image = explicit_full_context()
    print('VERIFY_OK')
    print('exact_first_appearance_masks:', *[as_mask(s) for s in images])
    print('minimum_sync_height:', height)
    print('witness_leaves:', leaves)
    print('singleton_output:', sorted(image))
    print('reachable_masks_and_costs:', *sorted((m, costs[m]) for m in range(1,16) if costs[m] < 10**9))
