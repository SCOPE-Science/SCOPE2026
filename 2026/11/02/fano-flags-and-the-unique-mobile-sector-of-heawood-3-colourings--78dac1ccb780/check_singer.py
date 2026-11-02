"""Independent complete enumeration of the three-colouring recolouring graph of the Heawood graph.
Python 3 standard library. Run: python check_singer.py.
"""
from collections import Counter, deque
from itertools import permutations

D=(0,1,3)
lines=[frozenset((j+d)%7 for d in D) for j in range(7)]
assert len(set(lines))==7
assert all(sum(a in line and b in line for line in lines)==1 for a in range(7) for b in range(a+1,7))
nbr=[set() for _ in range(14)]
for j,line in enumerate(lines):
    for p in line:
        nbr[p].add(j+7)
        nbr[j+7].add(p)
assert all(len(x)==3 for x in nbr)
order=[x for p in range(7) for x in (p,p+7)]
a=[-1]*14
states=[]
def visit(d):
    if d==14:
        states.append(tuple(a));return
    v=order[d]
    used={a[u] for u in nbr[v] if a[u]>=0}
    for color in range(3):
        if color not in used:
            a[v]=color
            visit(d+1)
    a[v]=-1
visit(0)
assert len(states)==2106, len(states)
lookup={a:i for i,a in enumerate(states)}
assert len(lookup)==len(states)
adj=[set() for _ in states]
for i,state in enumerate(states):
    for v in range(14):
        used={state[u] for u in nbr[v]}
        for color in range(3):
            if color==state[v] or color in used:continue
            b=list(state);b[v]=color
            j=lookup[tuple(b)]
            adj[i].add(j)
for i,nei in enumerate(adj):
    assert all(i in adj[j] for j in nei)
E=sum(map(len,adj))//2
assert E==6804,E
assert Counter(map(len,adj))=={0:126,4:126,5:420,6:504,8:588,9:252,11:84,14:6}
seen=set(); components=[]
for i in range(len(states)):
    if i in seen:continue
    q=deque([i]);seen.add(i);component=[]
    while q:
        u=q.popleft();component.append(u)
        for v in adj[u]:
            if v not in seen:seen.add(v);q.append(v)
    components.append(component)
assert Counter(map(len,components))=={1:126,1980:1}
main=next(c for c in components if len(c)==1980)
ecc=Counter()
for i in main:
    dist={i:0}; q=deque([i])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in dist:dist[v]=dist[u]+1;q.append(v)
    assert len(dist)==1980
    ecc[max(dist.values())]+=1
assert ecc=={21:1980}, ecc
# Point-line graph collineations, then an incidence duality and all colour permutations.
line_lookup={t:j for j,t in enumerate(lines)}
collineations=[]
for perm in permutations(range(7)):
    if all(frozenset(perm[x] for x in t) in line_lookup for t in lines):
        collineations.append(tuple(perm)+tuple(7+line_lookup[frozenset(perm[x] for x in line)] for line in lines))
assert len(collineations)==168
polarity=tuple(7+(-j)%7 for j in range(7))+tuple((-j)%7 for j in range(7))
G=set(collineations)|{tuple(polarity[g[i]] for i in range(14)) for g in collineations}
assert len(G)==336
frozen={states[i] for i in range(len(states)) if not adj[i]}
seed=next(iter(frozen))
orbit={tuple(p[seed[g[i]]] for i in range(14)) for g in G for p in permutations(range(3))}
assert orbit==frozen
print('SINGER_RECURSIVE_2106_COLORINGS_6804_EDGES_PASS')
print('SINGER_126_FROZEN_1980_CONNECTED_PASS')
print('SINGER_EVERY_MOBILE_ECCENTRICITY_21_PASS')
print('SINGER_ONE_FROZEN_SYMMETRY_ORBIT_PASS')
