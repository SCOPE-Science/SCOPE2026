"""Exact Morse certificates for the twelve Frucht two-independence links."""
from collections import Counter
from functools import cache
from graphlib import TopologicalSorter

EDGES = ((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
         (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
LCF = (-5,-2,-4,2,5,-2,2,5,-2,-5,4,2)
label = (4,3,2,1,7,0,6,5,10,11,8,9)
assert sorted(label) == list(range(12))
assert set(map(frozenset, EDGES)) == {
    frozenset((label[i], label[(i+j)%12])) for i in range(12) for j in (1,LCF[i])}
V = set(range(12))
N = {v:{u for u in V if (v,u) in EDGES or (u,v) in EDGES} for v in V}
faces = set()
for bits in range(1,1<<12):
    f = frozenset(v for v in V if bits & (1<<v))
    if all(len(f & N[v]) <= 1 for v in f):
        faces.add(f)

def bd(f):
    return [(f-{v}, (-1)**i) for i,v in enumerate(sorted(f)) if len(f)>1]

def morse(K):
    critical = K.copy()
    up = {}
    for v in sorted(V):
        lower = {f for f in critical if v not in f and f|{v} in critical}
        upper = {f|{v} for f in lower}
        up.update({f:f|{v} for f in lower})
        critical -= lower | upper
    dag = TopologicalSorter()
    for t in K:
        dag.add(t)
        for f,_ in bd(t):
            assert f in K
            if up.get(f) == t: dag.add(t, f)
            else: dag.add(f, t)
    assert len(list(dag.static_order())) == len(K)

    @cache
    def descend(f):
        if f in critical: return {f:1}
        if f not in up: return {}
        b = dict(bd(up[f]))
        pivot = b.pop(f)
        answer = Counter()
        for g,sign in b.items():
            for c,weight in descend(g).items():
                answer[c] -= pivot*sign*weight
        return {c:z for c,z in answer.items() if z}

    counts = Counter(len(f)-1 for f in critical)
    assert counts[0] == 1 and set(counts) <= {0,2,3}
    columns = {}
    for t in critical:
        col = Counter()
        for f,z in bd(t):
            for c,y in descend(f).items():
                col[c] += z*y
        col = {c:z for c,z in col.items() if z}
        if col:
            assert len(t) == 4 and all(len(c)==3 for c in col)
            columns[t] = col
    rows = {f for col in columns.values() for f in col}
    assert len(rows) <= 1
    entries = sorted(x for col in columns.values() for x in col.values())
    assert not entries or any(abs(x)==1 for x in entries)
    return (counts[2], counts[3], entries)

critical_patterns = [(1,2,[]),(0,1,[]),(1,2,[-1,1]),(0,0,[]),(0,1,[]),(0,1,[]),
                     (2,2,[-1,-1]),(0,2,[]),(1,1,[]),(1,2,[]),(1,2,[1]),(0,3,[])]
wedges = [(1,2),(0,1),(0,1),(0,0),(0,1),(0,1),(1,1),(0,2),(1,1),(1,2),(0,1),(0,3)]
for v in sorted(V):
    link = {f-{v} for f in faces if v in f and len(f)>1}
    q,r,entries = morse(link)
    assert (q,r,entries) == critical_patterns[v]
    rank = int(bool(entries))
    assert (q-rank,r-rank) == wedges[v]
    print(v, len(link), q, r, entries, wedges[v])
print('ALL_12_FRUCHT_LINK_WEDGES_OK')
