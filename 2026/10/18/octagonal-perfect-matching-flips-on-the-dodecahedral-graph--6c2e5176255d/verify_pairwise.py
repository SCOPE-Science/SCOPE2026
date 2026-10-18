"""Exhaustive pairwise certificate for octagonal flips of dodecahedron perfect matchings."""
import collections
import hashlib
import json

N=10
vertices=tuple(range(20))
edges=sorted({tuple(sorted(e)) for i in range(N) for e in ((i,(i+1)%N),(i,i+N),(i+N, N+(i+2)%N))})
assert len(edges)==30
neighbors=[set() for _ in vertices]
for a,b in edges:
    neighbors[a].add(b);neighbors[b].add(a)
assert all(len(s)==3 for s in neighbors)
edge_index={e:i for i,e in enumerate(edges)}

def perfect_matchings(free, chosen):
    if not free:
        yield chosen
        return
    v=min(free)
    for w in sorted(neighbors[v]&free):
        e=edge_index[tuple(sorted((v,w)))]
        yield from perfect_matchings(free-{v,w},chosen|(1<<e))

states=sorted(perfect_matchings(set(vertices),0))
assert len(states)==36 and len(set(states))==36

def cycle_components(bits):
    adj=[[] for _ in vertices]
    while bits:
        e=(bits&-bits).bit_length()-1
        a,b=edges[e]
        adj[a].append(b);adj[b].append(a)
        bits&=bits-1
    nonempty={v for v in vertices if adj[v]}
    components=[]
    while nonempty:
        start=min(nonempty); todo=[start]; seen={start}
        while todo:
            for w in adj[todo.pop()]:
                if w not in seen:
                    seen.add(w);todo.append(w)
        assert all(len(adj[v])==2 for v in seen)
        components.append(len(seen));nonempty-=seen
    return tuple(sorted(components))

adj=[set() for _ in states]
flip_length_counts=collections.Counter()
for i in range(len(states)):
    for j in range(i+1,len(states)):
        diff=states[i]^states[j]
        lengths=cycle_components(diff)
        if len(lengths)==1:
            flip_length_counts[lengths[0]]+=1
            if lengths==(8,):
                adj[i].add(j);adj[j].add(i)
assert flip_length_counts=={8:120,10:60,12:30,14:120,16:60,20:30},flip_length_counts
assert sum(map(len,adj))==240

def dists(v):
    ans={v:0};front=[v]
    for u in front:
        for w in sorted(adj[u]):
            if w not in ans:
                ans[w]=ans[u]+1;front.append(w)
    return ans
DS=[dists(i) for i in range(36)]
assert all(len(ds)==36 for ds in DS)
assert collections.Counter(max(ds.values()) for ds in DS)=={3:36}
assert collections.Counter(map(len,adj))=={10:6,6:30}
exceptional={i for i in range(36) if len(adj[i])==10}
ordinary=set(range(36))-exceptional
assert all(not (adj[i]&exceptional) for i in exceptional)
assert all(len(adj[i]&exceptional)==2 for i in ordinary)
assert all(sum(1 for w in ordinary if {i,j}<=(adj[w]&exceptional))==2
           for i in exceptional for j in exceptional if i<j)
# The ten configurations next to each exceptional one form an induced ten-cycle.
for z in exceptional:
    hood=set(adj[z]);remaining=set(hood);components=[]
    assert all(len(adj[u]&hood)==2 for u in hood)
    while remaining:
        root=remaining.pop();reachable={root};front=[root]
        for u in front:
            for v in adj[u]&hood:
                if v not in reachable:
                    reachable.add(v);front.append(v);remaining.discard(v)
        components.append(len(reachable))
    assert components==[10]
assert collections.Counter(tuple(sum(ds[j]==k for j in range(36)) for k in range(4))
        for ds in DS)=={(1,10,15,10):6,(1,6,19,10):30}
# Classify by cycle lengths of unmatched edges; complement is a 2-factor.
full=(1<<30)-1
assert collections.Counter(cycle_components(full^s) for s in states)=={(20,):30,(5,5,10):6}
assert all((cycle_components(full^states[i])==(5,5,10))==(i in exceptional) for i in range(36))
# Unambiguous bytes for third-party replay across different implementations.
payload=json.dumps({'edges':edges,'states':states,'adjacency':[sorted(x) for x in adj]},
                   separators=(',',':'),sort_keys=True).encode()
print(json.dumps({'status':'VERIFY_OK','method':'pairwise symmetric difference',
    'matchings':len(states),'flip_counts_by_cycle_length':dict(sorted(flip_length_counts.items())),
    'eight_cycle_flips':sum(map(len,adj))//2,
    'degrees':dict(sorted(collections.Counter(map(len,adj)).items())),
    'eccentricities':dict(sorted(collections.Counter(max(ds.values()) for ds in DS).items())),
    'exceptional_common_neighbor_multiplicity':2,
    'special_neighborhoods':'six induced C10',
    'distance_layers':{'degree10':[1,10,15,10],'degree6':[1,6,19,10]},
    'complement_factor_types':{'20':30,'5+5+10':6},
    'graph_certificate_sha256':hashlib.sha256(payload).hexdigest()},sort_keys=True))
