"""Standalone exhaustive certificate for the intrinsic graph Cech filtration of the Petersen graph.
Python 3 standard library only. Assert-based finite proof certificate."""
from itertools import combinations
from collections import Counter, deque

EDGES = ((0,1),(0,4),(0,5),(1,2),(1,6),(2,3),(2,7),(3,4),(3,8),(4,9),(5,7),(5,8),(6,8),(6,9),(7,9))
V = frozenset(range(10))
N = {v:set() for v in V}
for a,b in EDGES:
    N[a].add(b); N[b].add(a)
assert len(EDGES)==15 and all(len(N[v])==3 for v in V)

def faces(facets):
    F=set()
    for facet in facets:
        for k in range(1,len(facet)+1):
            F.update(frozenset(t) for t in combinations(sorted(facet),k))
    return F

def fv(F):
    return tuple(sum(1 for s in F if len(s)==k) for k in range(1,max(map(len,F))+1))

G=faces([frozenset(e) for e in EDGES])
F2=faces([frozenset(N[v]|{v}) for v in V])
F3=faces([frozenset(N[a]|N[b]|{a,b}) for a,b in EDGES])
assert fv(G)==(10,15)
assert fv(F2)==(10,45,40,10),fv(F2)
assert fv(F3)==(10,45,120,195,90,15),fv(F3)
assert len(F3)==475
assert all(len(N[a]|N[b]|{a,b})==6 for a,b in EDGES)

# Elementary relative collapse for the r=2 complex: every pair is free.
live=set(F2)
collapse_pairs=[]
for v in sorted(V):
    for k in (3,2):
        for t in combinations(sorted(N[v]),k):
            low=frozenset(t); high=low|{v}
            assert low in live and high in live
            immediate=[s for s in live if len(s)==len(low)+1 and low<=s]
            assert immediate==[high],(v,low,immediate)
            live.remove(high); live.remove(low)
            collapse_pairs.append((low,high))
assert len(collapse_pairs)==40 and live==G

# Staged vertex-toggle matching on the complete face poset.
remaining=set(F3); pairs=[]
for v in sorted(V):
    for low in sorted((s for s in remaining if v not in s),key=lambda s:(len(s),tuple(sorted(s)))):
        high=low|{v}
        if low in remaining and high in remaining:
            remaining.remove(low); remaining.remove(high)
            pairs.append((low,high))
assert len(pairs)==219 and len(remaining)==37,(len(pairs),len(remaining))
assert Counter(len(s)-1 for s in remaining)=={0:1,3:36},Counter(len(s)-1 for s in remaining)

# Verify no closed V-path by topologically sorting the entire directed Hasse diagram.
# Unmatched arcs point down, matched arcs point up.
matched=set(pairs)
arrow={f:[] for f in F3}; indeg={f:0 for f in F3}
incidences=0
for big in F3:
    if len(big)==1:continue
    for v in big:
        small=big-{v}
        if (small,big) in matched:
            source,dest=small,big
        else:
            source,dest=big,small
        arrow[source].append(dest)
        indeg[dest]+=1
        incidences+=1
q=deque(f for f in F3 if indeg[f]==0); count=0
while q:
    x=q.popleft();count+=1
    for y in arrow[x]:
        indeg[y]-=1
        if indeg[y]==0:q.append(y)
assert count==len(F3),(count,len(F3),incidences)

# Independent mod-2 chain ranks via sparse exact binary Gaussian elimination.
def mod2rank(boundary_rows):
    pivots={};r=0
    for x in boundary_rows:
        while x:
            p=x.bit_length()-1
            if p not in pivots:
                pivots[p]=x;r+=1;break
            x^=pivots[p]
    return r
bydim={k:sorted((s for s in F3 if len(s)==k+1),key=lambda s:tuple(sorted(s))) for k in range(6)}
ranks=[]
for k in range(1,6):
    idx={s:j for j,s in enumerate(bydim[k-1])}
    columns=[]
    for simplex in bydim[k]:
        b=0
        for v in simplex:b ^= (1<<idx[simplex-{v}])
        columns.append(b)
    ranks.append(mod2rank(columns))
assert ranks==[9,36,84,75,15],ranks
bettis=[len(bydim[0])-ranks[0]]+[len(bydim[k])-ranks[k-1]-ranks[k] for k in range(1,5)]+[len(bydim[5])-ranks[4]]
assert bettis==[1,0,0,36,0,0],bettis
# Self-check graph girth 5 and diameter 2, and thus the 4th-scale nerve is simplex.
D={v:{v:0} for v in V}
for v in V:
    todo=[v]
    for x in todo:
        for y in N[x]:
            if y not in D[v]:D[v][y]=D[v][x]+1;todo.append(y)
assert max(max(d.values()) for d in D.values())==2
assert all(len(set(N[a])&set(N[b]))==0 for a,b in EDGES)
assert all(len(set(N[a])&set(N[b]))==1 for a,b in combinations(sorted(V),2) if frozenset((a,b)) not in map(frozenset,EDGES))
print('VERIFY_OK', 'f2',fv(F2),'f3',fv(F3),'rel_collapse',len(collapse_pairs),'morse_pairs',len(pairs),'critical',(1,36),'Hasse_incidences',incidences,'ranks_mod2',ranks)
