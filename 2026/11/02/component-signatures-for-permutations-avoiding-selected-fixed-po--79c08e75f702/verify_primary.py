#!/usr/bin/env python3
"""Exhaustive verification of diagonal-forbidden adjacent-swap components."""
from itertools import permutations
from collections import defaultdict, deque


def signature(p, forbidden):
    pos = {x: i for i, x in enumerate(p)}
    return tuple(x for x in forbidden if pos[x] < x)


def canonical(n, forbidden, left):
    l = sorted(left)
    u = [x for x in range(n) if x not in forbidden]
    r = sorted(set(forbidden) - set(left))
    return tuple(l + u + r)


def normalize(p, forbidden):
    n = len(p)
    p = list(p)
    left = set(signature(tuple(p), forbidden))
    right = set(forbidden) - left
    def group(x):
        return 0 if x in left else (2 if x in right else 1)
    moves = 0
    # Bubble adjacent category inversions to collect the groups.
    for _ in range(n):
        for i in range(n-1):
            if group(p[i]) > group(p[i+1]):
                p[i],p[i+1] = p[i+1],p[i]
                moves += 1
                assert all(p[j] != j for j in forbidden)
    # Sort each group in increasing label order.
    for _ in range(n):
        for i in range(n-1):
            if group(p[i]) == group(p[i+1]) and p[i] > p[i+1]:
                p[i],p[i+1] = p[i+1],p[i]
                moves += 1
                assert all(p[j] != j for j in forbidden)
    assert tuple(p) == canonical(n, forbidden, left)
    assert moves <= n*(n-1)//2
    return moves


def verify(n, mask):
    forbidden = frozenset(i for i in range(n) if mask >> i & 1)
    ps = [p for p in permutations(range(n)) if all(p[i] != i for i in forbidden)]
    assert ps
    assert len({signature(p, forbidden) for p in ps}) == 2 ** len([x for x in forbidden if 0 < x < n-1])
    index = {p: i for i,p in enumerate(ps)}
    seen = set()
    component_count = 0
    for i,p in enumerate(ps):
        if i in seen: continue
        component_count += 1
        sig = signature(p, forbidden)
        seen.add(i)
        dq = deque([i])
        while dq:
            k = dq.popleft()
            q = ps[k]
            assert signature(q, forbidden) == sig
            for j in range(n-1):
                t = list(q)
                t[j],t[j+1] = t[j+1],t[j]
                h = index.get(tuple(t))
                if h is not None and h not in seen:
                    seen.add(h)
                    dq.append(h)
    assert component_count == 2 ** len([x for x in forbidden if 0 < x < n-1]), (n,mask,component_count)
    for p in ps:
        normalize(p, forbidden)
    return len(ps)

if __name__ == '__main__':
    for n in range(2, 8):
        count = sum(verify(n, m) for m in range(1<<n))
        print(f'PRIMARY_OK n={n} masks={1<<n} examined_states={count}')
    print('PRIMARY_ALL_PASS')
