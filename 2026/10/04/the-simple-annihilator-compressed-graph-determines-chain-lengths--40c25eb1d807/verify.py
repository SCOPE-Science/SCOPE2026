#!/usr/bin/env python3
from itertools import combinations_with_replacement, product
from math import prod

def graph(lengths):
    lengths = tuple(lengths)
    zero = tuple(0 for _ in lengths)
    top = tuple(lengths)
    verts = [a for a in product(*[range(e + 1) for e in lengths]) if a not in (zero, top)]
    adj = {a: set() for a in verts}
    for i, a in enumerate(verts):
        for b in verts[i + 1:]:
            if all(a[j] + b[j] >= lengths[j] for j in range(len(lengths))):
                adj[a].add(b)
                adj[b].add(a)
    return verts, adj

def predicted_degree(a, lengths):
    P = prod(x + 1 for x in a)
    self_ann = all(2 * a[i] >= lengths[i] for i in range(len(lengths)))
    return P - 1 - int(self_ann)

def recover(verts, adj):
    n = len(verts)
    T = n + 2
    if n == 0:
        return {(1,)}
    if n == 1:
        return {(2,)}
    if n == 2:
        assert sum(len(adj[v]) for v in verts) == 2
        return {(3,), (1, 1)}
    if n == 3:
        assert T == 5
        return {(4,)}

    leaves = [v for v in verts if len(adj[v]) == 1]
    if len(leaves) == 1:
        return {(n + 1,)}

    r = len(leaves)
    assert r >= 2
    if T == 6:
        assert r == 2
        return {(1, 2)}

    lengths = []
    for leaf in leaves:
        (c,) = tuple(adj[leaf])
        d = len(adj[c])
        if 2 * (d + 1) == T:
            ell = 1
        else:
            den = T - d - 2
            assert den > 0 and T % den == 0
            ell = T // den - 1
            assert ell >= 2
        lengths.append(ell)
    lengths.sort()
    assert prod(e + 1 for e in lengths) == T
    return {tuple(lengths)}

checked = 0
max_order = 0
for r in range(1, 6):
    for lengths in combinations_with_replacement(range(1, 7), r):
        order = prod(e + 1 for e in lengths) - 2
        if order > 500:
            continue
        verts, adj = graph(lengths)
        max_order = max(max_order, len(verts))
        for a in verts:
            assert len(adj[a]) == predicted_degree(a, lengths)
        got = recover(verts, adj)
        target = tuple(lengths)
        if target in ((3,), (1, 1)):
            assert got == {(3,), (1, 1)}
        else:
            assert got == {target}, (target, got)
        checked += 1

# Explicitly verify the unique exceptional pair is K_2 in both cases.
for lengths in [(3,), (1, 1)]:
    verts, adj = graph(lengths)
    assert len(verts) == 2
    assert all(len(adj[v]) == 1 for v in verts)

print('VERIFY_OK')
print(f'length_multisets_checked={checked}')
print(f'maximum_graph_order_checked={max_order}')
print('exception=(3)<->(1,1)=K2')
