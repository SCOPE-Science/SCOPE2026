"""Exact edge-metric basis enumeration and reconfiguration of the 18-vertex biaffine incidence graph.
Reconstructs distances by breadth-first search on the incidence graph.
Usage: python verify_graph.py [certificate.json]
"""
import collections
import hashlib
import itertools
import json
import sys

N = 18
VERTICES = list(range(N))
EDGES = sorted((3*x+y, 9+3*m+b)
               for x,y,m,b in itertools.product(range(3), repeat=4)
               if (y-m*x-b) % 3 == 0)
assert len(EDGES) == 27 and len(set(EDGES)) == 27
adjacency = [set() for _ in VERTICES]
for a,b in EDGES:
    adjacency[a].add(b)
    adjacency[b].add(a)
assert sorted(map(len,adjacency)) == [3]*18

def distances(source):
    d = {source:0}
    queue = collections.deque([source])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if v not in d:
                d[v] = d[u] + 1
                queue.append(v)
    assert len(d) == N
    return d

d = [distances(v) for v in VERTICES]
edge_vector = [[min(d[s][a],d[s][b]) for a,b in EDGES] for s in VERTICES]

def distinguishes_all(S):
    return len({tuple(edge_vector[s][e] for s in S)
                for e in range(len(EDGES))}) == len(EDGES)

previous_counts = {}
for k in range(4):
    previous_counts[k] = sum(distinguishes_all(S)
                             for S in itertools.combinations(VERTICES,k))
assert list(previous_counts.values()) == [0,0,0,0]
B = sorted(tuple(S) for S in itertools.combinations(VERTICES,4)
           if distinguishes_all(S))
assert len(B) == 540
idx = {v:i for i,v in enumerate(B)}
base_sets = [frozenset(s) for s in B]
TJ = [[] for _ in B]
TS = [[] for _ in B]
for i,S in enumerate(B):
    for old in S:
        reduced = frozenset(S) - {old}
        for new in VERTICES:
            if new in S:
                continue
            key = tuple(sorted(reduced | {new}))
            j = idx.get(key)
            if j is not None:
                TJ[i].append(j)
                if new in adjacency[old]:
                    TS[i].append(j)
for i in range(len(B)):
    TJ[i] = sorted(set(TJ[i]))
    TS[i] = sorted(set(TS[i]))
    assert all(i in TJ[j] for j in TJ[i])
assert all(not a for a in TS)

def components(A):
    remaining = set(range(len(A)))
    comps = []
    while remaining:
        root = min(remaining)
        remaining.remove(root)
        seen = {root}
        q = collections.deque([root])
        while q:
            for w in A[q.popleft()]:
                if w not in seen:
                    seen.add(w)
                    remaining.remove(w)
                    q.append(w)
        comps.append(seen)
    return comps

comps = components(TJ)
assert sorted(map(len,comps)) == [9]*6+[486]
ecc_by_size = collections.defaultdict(collections.Counter)
layers_by_degree = collections.defaultdict(collections.Counter)
for comp in comps:
    for root in comp:
        dis = {root:0}
        q = collections.deque([root])
        while q:
            u = q.popleft()
            for v in TJ[u]:
                if v not in dis:
                    dis[v] = dis[u]+1
                    q.append(v)
        assert len(dis)==len(comp)
        ecc_by_size[len(comp)][max(dis.values())] += 1
        layers = tuple(collections.Counter(dis.values())[k]
                       for k in range(max(dis.values())+1))
        layers_by_degree[(len(comp),len(TJ[root]))][layers] += 1
assert dict(ecc_by_size[9]) == {2:54}
assert dict(ecc_by_size[486]) == {5:486}

purepoint = sum(len(set(s)&set(range(9)))==4 for s in B)
pureline = sum(len(set(s)&set(range(9,18)))==4 for s in B)
mixed = sum(sum(v<9 for v in s)==2 for s in B)
assert (purepoint,mixed,pureline)==(27,486,27)
degree_hist = dict(sorted(collections.Counter(map(len,TJ)).items()))
assert degree_hist == {4:54,12:54,14:216,16:216}
edge_pairs = [(i,j) for i in range(len(B)) for j in TJ[i] if i<j]
assert len(edge_pairs)==3672
certificate = {'vertex_order':list(range(N)), 'incidences':[list(e) for e in EDGES],
               'bases':[list(s) for s in B], 'token_jump_edges':[list(e) for e in edge_pairs]}
if len(sys.argv)>1:
    with open(sys.argv[1], encoding='utf-8') as f:
        assert json.load(f)==certificate
basis_digest = hashlib.sha256(json.dumps(certificate['bases'],separators=(',',':')).encode()).hexdigest()
edge_digest = hashlib.sha256(json.dumps(certificate['token_jump_edges'],separators=(',',':')).encode()).hexdigest()
summary = {'method':'incidence BFS and exhaustive four-subset signature search',
 'vertices':N,'incidences':len(EDGES),'lower_cardinality_counts':previous_counts,
 'edge_metric_dimension':4,'basis_count':len(B),'basis_types':{'points_only':purepoint,'mixed':mixed,'lines_only':pureline},
 'jump_edges':len(edge_pairs),'jump_components':sorted(map(len,comps),reverse=True),
 'jump_degrees':degree_hist,'eccentricities_by_component_size':{str(k):dict(v) for k,v in ecc_by_size.items()},
 'slide_edges':sum(map(len,TS))//2,'basis_sha256':basis_digest,'jump_edge_sha256':edge_digest,
 'mixed_layers_by_degree':{str(key):{str(k):v for k,v in c.items()} for key,c in layers_by_degree.items() if key[0]==486},
 'certificate_checked':len(sys.argv)>1}
print(json.dumps(summary,sort_keys=True,indent=2))
