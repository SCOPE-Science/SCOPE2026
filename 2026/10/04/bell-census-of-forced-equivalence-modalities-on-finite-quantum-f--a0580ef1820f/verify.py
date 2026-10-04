#!/usr/bin/env python3
from itertools import product


def partitions(n):
    if n == 0:
        yield ()
        return
    a = [0] * n
    def rec(i, mx):
        if i == n:
            yield tuple(a)
            return
        for v in range(mx + 2):
            a[i] = v
            yield from rec(i + 1, max(mx, v))
    a[0] = 0
    if n == 1:
        yield (0,)
    else:
        yield from rec(1, 0)


def bell(n):
    return sum(1 for _ in partitions(n))


def q_relation(n, edge_mask):
    Q = {(i, i) for i in range(n)}
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (edge_mask >> k) & 1:
                Q.add((i, j)); Q.add((j, i))
            k += 1
    return Q


def components(n, Q):
    unseen = set(range(n)); out = []
    while unseen:
        root = min(unseen); stack = [root]; C = {root}; unseen.remove(root)
        while stack:
            u = stack.pop()
            for v in list(unseen):
                if (u, v) in Q:
                    unseen.remove(v); C.add(v); stack.append(v)
        out.append(frozenset(C))
    return tuple(out)


def eq_relation(labels):
    n = len(labels)
    return frozenset((i, j) for i in range(n) for j in range(n) if labels[i] == labels[j])


def forced(Q, R):
    n = 1 + max(max(x) for x in Q | set(R)) if (Q or R) else 0
    for u, w in R:
        for v in range(n):
            if (u, v) in Q and (v, w) not in R:
                return False
    return True


def rows(n, R):
    return tuple(frozenset(v for v in range(n) if (u, v) in R) for u in range(n))


def coarsens_components(n, comps, labels):
    for C in comps:
        labs = {labels[x] for x in C}
        if len(labs) != 1:
            return False
    return True


def component_partition_relations(n, comps):
    rels = set()
    c = len(comps)
    for plab in partitions(c):
        world_lab = [None] * n
        for ci, C in enumerate(comps):
            for x in C:
                world_lab[x] = plab[ci]
        rels.add(eq_relation(tuple(world_lab)))
    return rels

# Exhaustive Bell classification through five worlds.
summary = {}
for n in range(1, 6):
    m = n * (n - 1) // 2
    eqs = [(lab, eq_relation(lab)) for lab in partitions(n)]
    checked_graphs = 0
    for mask in range(1 << m):
        Q = q_relation(n, mask)
        comps = components(n, Q)
        c = len(comps)
        accepted = set()
        for lab, R in eqs:
            f = forced(Q, R)
            coarse = coarsens_components(n, comps, lab)
            assert f == coarse, (n, mask, lab, f, coarse)
            if f:
                accepted.add(R)
        expected = bell(c)
        assert len(accepted) == expected, (n, mask, c, len(accepted), expected)
        generated = component_partition_relations(n, comps)
        assert accepted == generated
        if c == 1:
            assert accepted == {frozenset((i, j) for i in range(n) for j in range(n))}
        checked_graphs += 1
    summary[n] = checked_graphs

# Independently check the source structural premise for arbitrary modal
# relations through three worlds: forcing iff rows are constant on components.
for n in range(1, 4):
    m = n * (n - 1) // 2
    pairs = [(i, j) for i in range(n) for j in range(n)]
    for mask in range(1 << m):
        Q = q_relation(n, mask)
        comps = components(n, Q)
        for rmask in range(1 << (n * n)):
            R = frozenset(pairs[k] for k in range(n * n) if (rmask >> k) & 1)
            rs = rows(n, R)
            const = all(len({rs[x] for x in C}) == 1 for C in comps)
            assert forced(Q, R) == const

print('GRAPHS', summary)
print('BELLS', [bell(i) for i in range(1, 6)])
print('VERIFY_OK')
