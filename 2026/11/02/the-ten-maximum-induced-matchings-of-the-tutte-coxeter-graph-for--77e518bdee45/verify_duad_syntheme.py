"""Independent exhaustive finite check for induced matchings in the 30-vertex duad-syntheme graph."""
from itertools import combinations
from collections import Counter

P = tuple(combinations(range(6), 2))

def partitions(a):
    if not a:
        yield ()
        return
    x = a[0]
    for y in a[1:]:
        remaining = tuple(z for z in a[1:] if z != y)
        for rest in partitions(remaining):
            yield (tuple(sorted((x, y))),) + rest

L = tuple(tuple(sorted(s)) for s in partitions(tuple(range(6))))
assert len(P) == len(L) == 15 and len(set(L)) == 15
flags = {(p,s) for p in P for s in L if p in s}
assert len(flags) == 45

parts = []
for a in combinations(range(6), 3):
    b = tuple(x for x in range(6) if x not in a)
    if a > b:
        continue
    aa, bb = set(a), set(b)
    matching = {
        (tuple(sorted((u,v))), tuple(sorted((tuple(sorted(aa-{u})), tuple(sorted(bb-{v})), tuple(sorted((u,v)))))))
        for u in a for v in b
    }
    assert len(matching) == 9 and matching <= flags
    assert all(p not in t and q not in s for (p,s),(q,t) in combinations(matching,2))
    parts.append((a,b,matching))
assert len(parts) == 10 and len({frozenset(m) for _,_,m in parts}) == 10
assert all(len(x[2]&y[2]) == 1 for x,y in combinations(parts,2))
assert Counter(f for _,_,m in parts for f in m) == Counter({f:2 for f in flags})

# Every nine-duad choice corresponds to a 9-edge spanning graph on six points.
# Its perfect-matchings count is at most six, with equality only for K_{3,3}.
pm_count=Counter()
optimal_graphs=[]
for x in combinations(P, 9):
    xx = set(x)
    c = sum(all(e in xx for e in s) for s in L)
    pm_count[c] += 1
    if c == 6:
        optimal_graphs.append(frozenset(xx))
assert pm_count == Counter({0:75,1:360,2:1380,3:2040,4:1140,6:10}),pm_count
assert set(optimal_graphs) == {frozenset(tuple(sorted((a,b))) for a in A for b in B) for A,B,_ in parts}
print('DUAD_SYNTHEME_EXHAUSTIVE_PASS flags=45 maxima=10 size=9 pair_intersection=1')
print('nine_duad_graph_perfect_matching_histogram=',sorted(pm_count.items()))
