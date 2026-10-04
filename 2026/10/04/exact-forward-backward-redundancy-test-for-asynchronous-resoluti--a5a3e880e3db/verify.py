#!/usr/bin/env python3
from itertools import combinations, product

def groups(n):
    return [tuple(c) for r in range(1, n + 1) for c in combinations(range(n), r)]

def update(state, B):
    B = tuple(B)
    union = 0
    for b in B:
        union |= state[b]
    out = list(state)
    for a in B:
        out[a] = union
    return tuple(out)

def views(n, history):
    state = tuple(1 << a for a in range(n))
    for B in history:
        state = update(state, B)
    return state

def union_rows(state, index_mask):
    out = 0
    for i in range(len(state)):
        if (index_mask >> i) & 1:
            out |= state[i]
    return out

def criterion(n, prefix, B, suffix):
    V = views(n, prefix)
    Q = views(n, suffix)
    U = 0
    for b in B:
        U |= V[b]
    for a in range(n):
        touches = any((Q[a] >> b) & 1 for b in B)
        if touches:
            F = union_rows(V, Q[a])
            if U & ~F:
                return False
    return True

def all_histories(gs, max_len):
    ans = [()]
    for length in range(1, max_len + 1):
        ans.extend(product(gs, repeat=length))
    return ans

for n in range(1, 5):
    gs = groups(n)
    histories = all_histories(gs, 2)

    # Exact arbitrary-occurrence criterion.
    for prefix in histories:
        for B in gs:
            for suffix in histories:
                with_B = views(n, prefix + (B,) + suffix)
                without_B = views(n, prefix + suffix)
                assert (with_B == without_B) == criterion(n, prefix, B, suffix)

    # Immediate criterion: participants already have equal views.
    for prefix in histories:
        V = views(n, prefix)
        for B in gs:
            equal_participants = len({V[b] for b in B}) == 1
            direct = views(n, prefix + (B,)) == V
            assert direct == equal_participants

            # Immediate repetition is always relation-state redundant.
            once = views(n, prefix + (B,))
            twice = views(n, prefix + (B, B))
            assert once == twice

    # Coordinate-equality model: distinct index sets induce distinct intersections.
    # Represent the intersection relation for C by the set of ordered world pairs
    # agreeing on every coordinate in C.
    worlds = range(1 << n)
    relation_signatures = {}
    for C in range(1 << n):
        pairs = []
        for x in worlds:
            for y in worlds:
                if ((x ^ y) & C) == 0:
                    pairs.append((x, y))
        sig = tuple(pairs)
        assert sig not in relation_signatures.values()
        relation_signatures[C] = sig

print("VERIFY_OK")
