"""Exact finite checks for minimum power domination on GP(8,3)."""
from collections import deque
from itertools import combinations


def graph():
    adj = [set() for i in range(16)]
    for i in range(8):
        for u, v in ((i, (i+1)%8), (i, 8+i), (8+i, 8+(i+3)%8)):
            adj[u].add(v)
            adj[v].add(u)
    return adj


def rounds(adj, seed):
    marked = set(seed)
    for u in seed:
        marked.update(adj[u])
    sizes = [len(marked)]
    while True:
        targets = set()
        for u in marked:
            other = adj[u]-marked
            if len(other) == 1:
                targets.update(other)
        if not targets:
            return tuple(sizes)
        marked.update(targets)
        sizes.append(len(marked))


def main():
    adj = graph()
    color = [i%2 for i in range(8)] + [(i+1)%2 for i in range(8)]
    assert all(len(ns)==3 and all(color[u]!=color[v] for v in ns)
               for u, ns in enumerate(adj))
    table = {None:(4,), 1:(6,), 2:(7,8), 3:(8,12,16), 4:(8,),
             8:(6,), 9:(7,8), 10:(8,14,16), 11:(7,8), 12:(8,12,16)}
    for v, expected in table.items():
        assert rounds(adj, (0,) if v is None else (0,v)) == expected
    assert all(rounds(adj, (v,))[-1] < 16 for v in range(16))
    pairs = [frozenset(s) for s in combinations(range(16),2)
             if rounds(adj, s)[-1]==16]
    complement = {frozenset((u,v)) for u,v in combinations(range(16),2)
                  if color[u]!=color[v] and v not in adj[u]}
    assert len(pairs)==40 and set(pairs)==complement
    jumps = [set() for s in pairs]
    slides = 0
    for a,b in combinations(range(len(pairs)),2):
        exch = pairs[a]^pairs[b]
        if len(exch)==2:
            x,y = exch
            jumps[a].add(b)
            jumps[b].add(a)
            slides += y in adj[x]
    assert sum(map(len,jumps))==320 and slides==0
    for s in range(len(pairs)):
        depth = {s:0}
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for v in jumps[u]-depth.keys():
                depth[v] = depth[u]+1
                queue.append(v)
        assert len(depth)==40 and max(depth.values())==3
    print('GP(8,3): 40 minima, 160 jump edges, all jump eccentricities 3, no slides')


if __name__=='__main__':
    main()
