"""Independent face-cycle flip reconstruction of dodecahedral matching states."""
import collections
import hashlib
import json

n=10
E=set()
for x in range(n):
    E.update({frozenset((x,(x+1)%n)),frozenset((x,x+n)),frozenset((x+n,((x+2)%n)+n))})
assert len(E)==30
V=set(range(20))
A={v:set() for v in V}
for e in E:
    a,b=tuple(e);A[a].add(b);A[b].add(a)

# Enumerate complete matchings by the least-constrained available vertex.
def enumerate_1factors(open_vertices,chosen):
    if not open_vertices:
        yield frozenset(chosen)
    else:
        options={v:A[v]&open_vertices for v in open_vertices}
        v=min(open_vertices,key=lambda x:(len(options[x]),-x))
        for u in sorted(options[v],reverse=True):
            yield from enumerate_1factors(open_vertices-{v,u},chosen+(frozenset((v,u)),))

matching_edges=set(enumerate_1factors(V,()))
assert len(matching_edges)==36

def canon_cycle(seq):
    candidates=[]
    for path in (list(seq),list(reversed(seq))):
        idx=path.index(min(path));candidates.append(tuple(path[idx:]+path[:idx]))
    return min(candidates)

def cycles(k):
    found=set()
    def visit(p):
        if len(p)==k:
            if p[0] in A[p[-1]]:found.add(canon_cycle(p))
            return
        for nxt in A[p[-1]]:
            if nxt not in p:visit(p+[nxt])
    for start in V:
        visit([start])
    return found

def cycle_edges(c):
    return frozenset(frozenset((c[i],c[(i+1)%len(c)])) for i in range(len(c)))

assert len(cycles(3))==0 and len(cycles(4))==0
assert len(cycles(5))==12
assert len(cycles(6))==0
simple8=cycles(8)
assert len(simple8)==30
# The boundaries of each adjacent pentagon pair exhaust all octagons.
faces=[tuple((i,i+1 if i+1<10 else 0,(i+2)%10,10+(i+2)%10,10+i)) for i in range(10)]
faces.extend((tuple(range(10,20,2)),tuple(range(11,20,2))))
face_edges=[cycle_edges(f) for f in faces]
assert len(set(face_edges))==12
assert {canon_cycle(f) for f in faces}==cycles(5)
octagon_boundaries=set()
for i in range(12):
    for j in range(i+1,12):
        if len(face_edges[i]&face_edges[j])==1:
            octagon_boundaries.add(face_edges[i]^face_edges[j])
assert len(octagon_boundaries)==30
assert octagon_boundaries=={cycle_edges(c) for c in simple8}

# Independent dynamics: toggle the eight edges of each alternating octagon.
Ms=sorted(matching_edges,key=lambda s:tuple(sorted(tuple(sorted(e)) for e in s)))
lookup={m:i for i,m in enumerate(Ms)}
neighbor=[set() for _ in Ms]
incidence={c:0 for c in octagon_boundaries}
for idx,matching in enumerate(Ms):
    for octagon in octagon_boundaries:
        # A four-edge selection from an octagon is alternating iff no endpoints overlap.
        chosen=matching&octagon
        if len(chosen)!=4:continue
        covered=set().union(*(set(e) for e in chosen))
        if len(covered)!=8:continue
        target=matching^octagon
        assert target in lookup
        neighbor[idx].add(lookup[target]);incidence[octagon]+=1
assert set(incidence.values())=={8},set(incidence.values())
assert all(i not in neighbor[i] for i in range(36))
assert all(i in neighbor[j] for i in range(36) for j in neighbor[i])
assert collections.Counter(len(x) for x in neighbor)=={6:30,10:6}
# Floyd-Warshall, logically distinct from the pairwise program's BFS.
INF=999
dist=[[0 if i==j else 1 if j in neighbor[i] else INF for j in range(36)] for i in range(36)]
for k in range(36):
    for i in range(36):
        for j in range(36):
            if dist[i][k]+dist[k][j]<dist[i][j]:dist[i][j]=dist[i][k]+dist[k][j]
assert max(max(row) for row in dist)==3
assert collections.Counter(max(row) for row in dist)=={3:36}
centers={i for i,a in enumerate(neighbor) if len(a)==10}
assert all(not (neighbor[i]&centers) for i in centers)
assert all(len(neighbor[i]&centers)==2 for i in range(36) if i not in centers)
assert all(len(neighbor[i]&neighbor[j])==2 for i in centers for j in centers if i<j)
for i in centers:
    hood=neighbor[i]
    assert all(len(neighbor[j]&hood)==2 for j in hood)
    todo=set(hood);seed=todo.pop();front=[seed];seen={seed}
    for u in front:
        for v in neighbor[u]&hood:
            if v not in seen:seen.add(v);todo.discard(v);front.append(v)
    assert len(seen)==10 and not todo
assert (collections.Counter(tuple(row.count(x) for x in range(4)) for row in dist)==
       {(1,10,15,10):6,(1,6,19,10):30})
# Normalize the same edge-indexed canonical certificate as an independent reference.
edges=sorted(tuple(sorted(e)) for e in E)
ei={e:i for i,e in enumerate(edges)}
indexed=[sum(1<<ei[tuple(sorted(e))] for e in m) for m in Ms]
ordered=sorted(range(36),key=lambda i:indexed[i]);back={j:i for i,j in enumerate(ordered)}
payload=json.dumps({'edges':edges,'states':[indexed[i] for i in ordered],
    'adjacency':[sorted(back[j] for j in neighbor[i]) for i in ordered]},
    separators=(',',':'),sort_keys=True).encode()
print(json.dumps({'status':'VERIFY_OK','method':'face boundaries plus eight-edge toggles',
    'pentagonal_faces':len(face_edges),'six_cycles':0,'octagonal_cycles':len(simple8),
    'octagon_matching_incidence':8,'matchings':len(Ms),
    'flips':sum(map(len,neighbor))//2,'degree_distribution':dict(collections.Counter(map(len,neighbor))),
    'eccentricity_distribution':dict(collections.Counter(max(x) for x in dist)),
    'exceptional_pair_common_neighbors':2,
    'special_neighborhoods':'six induced C10',
    'graph_certificate_sha256':hashlib.sha256(payload).hexdigest()},sort_keys=True))
