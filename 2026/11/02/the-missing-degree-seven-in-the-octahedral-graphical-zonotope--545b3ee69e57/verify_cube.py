#!/usr/bin/env python3
"""Independent strong-orientation count via exhaustive directed-cut tests."""
from collections import Counter,deque
E=tuple((v,v^(1<<i)) for v in range(8) for i in range(3) if v<(v^(1<<i)))
assert len(E)==12

def strong(mask):
    # A finite directed graph is strongly connected iff every proper,
    # nonempty vertex cut has an edge directed into it and one out of it.
    for cut in range(1,255):
        enter=leave=False
        for i,(a,b) in enumerate(E):
            if bool((cut>>a)&1)==bool((cut>>b)&1):continue
            source,target=(a,b) if (mask>>i)&1 else (b,a)
            if (cut>>source)&1:leave=True
            else:enter=True
            if enter and leave:break
        if not (enter and leave):return False
    return True

S={a for a in range(1<<len(E)) if strong(a)}
assert len(S)==426
adj={a:{a^(1<<i) for i in range(12) if (a^(1<<i)) in S} for a in S}
assert Counter(map(len,adj.values()))==Counter({5:288,6:120,8:18})
assert sum(map(len,adj.values()))==2304

# Reversal graph connected, and all geodesics have minimum Hamming length.
seen={next(iter(S))}; q=deque(seen)
while q:
    a=q.popleft()
    for b in adj[a]:
        if b not in seen:seen.add(b);q.append(b)
assert seen==S
for a in S:
    dist={a:0};q=deque([a])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v]=dist[u]+1;q.append(v)
    assert len(dist)==426
    assert all(dist[b]==(a^b).bit_count() for b in S)
print('CUBE_DIRECTED_CUT_ORIENTATIONS_PASS')
print('cube_vertices',len(S),'cube_exchanges',sum(map(len,adj.values()))//2)
