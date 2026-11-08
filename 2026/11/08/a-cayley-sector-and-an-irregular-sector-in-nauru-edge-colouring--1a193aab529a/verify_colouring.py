"""Independent direct edge-colouring search and Kempe graph metric for GP(12,5).
Run: python verify_colouring.py  (Python >=3.9, standard library only).
"""
from collections import Counter, deque
from itertools import combinations

N=24
edges=[]
for i in range(12):
    edges.extend([(i,(i+1)%12),(i,i+12),(i+12,(i+5)%12+12)])
edges=[tuple(sorted(x)) for x in edges]
assert len(edges)==36 and len(set(edges))==36
inc=[[] for i in range(N)]
for j,(u,v) in enumerate(edges):inc[u].append(j);inc[v].append(j)
assert all(len(x)==3 for x in inc)

# Independent edge-by-edge CSP, without generating any perfect matchings.
partial=[-1]*len(edges)
used=[0]*N
solutions=[]
def search(left):
    if not left:
        solutions.append(tuple(partial));return
    # Minimum-remaining-values edge, ties broken by immutable index.
    best=min(left,key=lambda e:(3-((used[edges[e][0]]|used[edges[e][1]]).bit_count()),e))
    u,v=edges[best];free=7&~(used[u]|used[v])
    if not free:return
    for color in range(3):
        bit=1<<color
        if not free&bit:continue
        partial[best]=color;used[u]|=bit;used[v]|=bit
        search(left-{best})
        used[u]^=bit;used[v]^=bit;partial[best]=-1
search(set(range(len(edges))))
assert len(solutions)==504
assert len(set(solutions))==504
assert all(set(c[e] for e in inc[v])=={0,1,2} for c in solutions for v in range(N))
ids={c:i for i,c in enumerate(solutions)}

# Alternate alternating-cycle extraction, walking VERTICES rather than edges.
def two_cycles(c,x,y):
    linked=[[] for _ in range(N)]
    for j,(u,v) in enumerate(edges):
        if c[j] in (x,y):
            linked[u].append((v,j));linked[v].append((u,j))
    assert all(len(a)==2 for a in linked)
    visited=set();result=[]
    for start in range(N):
        if start in visited:continue
        prev=-1;at=start;cyc=[]
        while at not in visited:
            visited.add(at)
            w,e=next((w,e) for w,e in linked[at] if w!=prev)
            cyc.append(e);prev,at=at,w
        assert at==start
        result.append(cyc)
    assert sum(map(len,result))==24
    return result

adj=[set() for _ in solutions]
by_type={}
for i,c in enumerate(solutions):
    factor_type=[]
    for x,y in ((0,1),(0,2),(1,2)):
        cycles=two_cycles(c,x,y)
        factor_type.append(tuple(sorted(len(z) for z in cycles)))
        for cycle in cycles:
            d=list(c)
            for j in cycle:d[j]=x+y-d[j]
            dest=tuple(d)
            assert dest in ids
            adj[i].add(ids[dest])
    by_type[i]=tuple(sorted(factor_type))
assert all(i in adj[j] for j,a in enumerate(adj) for i in a)
assert sum(map(len,adj))==3348

def cluster(s):
    q=[s];seen={s}
    for i in q:
        for j in sorted(adj[i]):
            if j not in seen:seen.add(j);q.append(j)
    return seen
notdone=set(range(len(solutions)));components=[]
while notdone:
    component=cluster(min(notdone));components.append(component)
    notdone-=component
assert sorted(map(len,components))==[144,360]

results={}
for comp in components:
    ecc=Counter();distcounts=Counter();degree_counts=Counter(len(adj[v]) for v in comp)
    for s in comp:
        d={s:0};q=deque([s])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if w not in d:d[w]=d[v]+1;q.append(w)
        assert set(d)==comp
        ecc[max(d.values())]+=1
        for t in d.values():
            if t>0:distcounts[t]+=1
    assert all(n%2==0 for n in distcounts.values())
    results[len(comp)]=(ecc,degree_counts,tuple(distcounts[j]//2 for j in range(1,max(ecc)+1)))
ecc,deg,pairs=results[144]
assert ecc=={4:144} and deg=={6:144}
assert pairs==(432,1944,4752,3168)
ecc,deg,pairs=results[360]
assert ecc=={5:330,6:30} and deg=={6:210,8:144,12:6}
assert pairs==(1242,5904,18981,31401,6732,360)
short=next(x for x in components if len(x)==144)
assert {by_type[i] for i in short}=={((10,14),(10,14),(10,14))}
assert all(10 not in sum((list(pair) for pair in by_type[i]),[]) for x in components if len(x)==360 for i in x)
assert sum(pairs)==360*359//2
print('NAURU_COLOURING_VERIFIER_PASS 504 edge CSP solutions, 3348 directed moves')
print('NAURU_ALTERNATE_METRIC_PASS 144 and 360 components',results)
print('NAURU_TEN_FOURTEEN_SEPARATION_PASS')
