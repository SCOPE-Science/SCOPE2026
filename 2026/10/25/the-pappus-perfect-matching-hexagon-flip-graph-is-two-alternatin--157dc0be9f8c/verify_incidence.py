#!/usr/bin/env python3
"""Exact Pappus incidence-configuration matching-switch classification; Python stdlib."""
import collections, hashlib, itertools, json

# Points A,B,C,a,b,c,X,Y,Z are numbered 0,...,8. Each triple is one line.
LINES = ((0,1,2),(3,4,5),(0,4,6),(3,1,6),(0,5,7),
         (3,2,7),(1,5,8),(4,2,8),(6,7,8))
INC = tuple(tuple(j for j,L in enumerate(LINES) if i in L) for i in range(9))
assert all(len(x)==3 for x in INC)
assert len({frozenset((i,j)) for L in LINES for i,j in itertools.combinations(L,2)}) == 27

matchings=[]
def extend(p,used):
    if len(p)==9:
        matchings.append(tuple(p));return
    for j in INC[len(p)]:
        if not (used>>j)&1:extend(p+[j],used|(1<<j))
extend([],0)
matchings.sort(); ids={p:i for i,p in enumerate(matchings)}
assert len(ids)==42

def parity(p):
    return sum(p[i]>p[j] for i in range(9) for j in range(i+1,9))%2

adj=[set() for _ in matchings]
for i,p in enumerate(matchings):
    for aa,bb,cc in itertools.combinations(range(9),3):
        for qvals in ((p[bb],p[cc],p[aa]),(p[cc],p[aa],p[bb])):
            if all(q in INC[v] for v,q in zip((aa,bb,cc),qvals)):
                q=list(p)
                q[aa],q[bb],q[cc]=qvals
                j=ids[tuple(q)]
                adj[i].add(j)
                assert parity(p)==parity(q)
for i in range(len(ids)):
    assert i not in adj[i]
    assert all(i in adj[j] for j in adj[i])

components=[];seen=set()
for root in range(len(ids)):
    if root in seen:continue
    c={root};todo=[root];seen.add(root)
    while todo:
        v=todo.pop()
        for w in adj[v]-seen:seen.add(w);c.add(w);todo.append(w)
    components.append(c)
assert sorted(map(len,components))==[21,21]
assert {len({parity(matchings[i]) for i in c}) for c in components}=={1}
assert {parity(matchings[next(iter(c))]) for c in components}=={0,1}

def shortest(start, c):
    dist={start:0};todo=collections.deque([start])
    while todo:
        u=todo.popleft()
        for v in adj[u]&c:
            if v not in dist:dist[v]=dist[u]+1;todo.append(v)
    assert len(dist)==len(c)
    return max(dist.values())

results=[]
for c in components:
    degrees=collections.Counter(len(adj[i]) for i in c)
    assert degrees=={3:18,6:3},degrees
    hubs=sorted(i for i in c if len(adj[i])==6)
    assert all(not (adj[h]&set(hubs)) for h in hubs)
    assert all(len(adj[v]&set(hubs))==1 for v in c if v not in hubs)
    rest=c-set(hubs)
    peripheral=[];done=set()
    for start in rest:
        if start in done:continue
        todo=[start];sub={start};done.add(start)
        while todo:
            v=todo.pop()
            for u in (adj[v]&rest)-done:done.add(u);sub.add(u);todo.append(u)
        peripheral.append(sub)
    assert len(peripheral)==3 and all(len(a)==6 for a in peripheral)
    hubpairs=[]
    for cyc in peripheral:
        assert all(len(adj[v]&cyc)==2 for v in cyc)
        hset=set()
        for v in cyc:
            hh=next(h for h in hubs if h in adj[v]);hset.add(hh)
            assert all(next(h for h in hubs if h in adj[u])!=hh for u in adj[v]&cyc)
        assert len(hset)==2
        assert all(sum(h in adj[v] for v in cyc)==3 for h in hset)
        hubpairs.append(frozenset(hset))
    assert set(hubpairs)=={frozenset(p) for p in itertools.combinations(hubs,2)}
    es=sum(len(adj[i]) for i in c)//2
    ecc={shortest(v,c) for v in c}
    assert es==36 and ecc=={4},ecc
    results.append({'size':len(c),'edges':es,'degree_histogram':dict(sorted(degrees.items())),
                    'peripheral_cycles':sorted(len(t) for t in peripheral),'radius':min(ecc),'diameter':max(ecc),
                    'parity':parity(matchings[next(iter(c))])})
result={'graph':'Pappus incidence graph','matchings':len(matchings),'flip_edges':sum(map(len,adj))//2,
        'components':sorted(results,key=lambda x:x['parity']),
        'matching_sign_counts':dict(sorted(collections.Counter(parity(p) for p in matchings).items())),
        'claim':'each component is a triangle of alternating hub-attached hexagons'}
assert result['flip_edges']==72
print(json.dumps(result,sort_keys=True,indent=2))
