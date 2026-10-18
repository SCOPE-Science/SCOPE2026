"""Independent LCF-based exhaustive verifier for Pappus induced matchings.

The graph and compatibility test are separate from the affine incidence model.
"""
import json
from itertools import combinations
from collections import Counter,deque
from pathlib import Path

cert=json.loads((Path(__file__).parent/'induced_matching_certificate.json').read_text())
perm=cert['lcf_to_incidence_vertices']
assert sorted(perm)==list(range(18))
step=[5,7,-7,7,-7,-5]*3
E=sorted({tuple(sorted((i,(i+1)%18))) for i in range(18)} |
         {tuple(sorted((i,(i+step[i])%18))) for i in range(18)})
assert len(E)==27
neighbors=[set() for _ in range(18)]
for u,v in E:neighbors[u].add(v);neighbors[v].add(u)
assert all(len(n)==3 for n in neighbors)

# Independent verification of the claimed graph equivalence by inspecting
# every edge and nonedge under the explicit vertex permutation.
P=[(x,y) for x in range(3) for y in range(3)]
L=[(m,b) for m in range(3) for b in range(3)]
Ie=sorted((i,9+j) for i,(x,y) in enumerate(P) for j,(m,b) in enumerate(L)
          if y%3==(m*x+b)%3)
assert {tuple(sorted((perm[u],perm[v]))) for u,v in E}==set(Ie)
Iindex={e:i for i,e in enumerate(Ie)}
edge_perm=[Iindex[tuple(sorted((perm[u],perm[v])))] for u,v in E]
assert sorted(edge_perm)==list(range(27))

# Enumerate all subsets of at most six graph edges. Forbid shared endpoints
# and any extra graph edge between endpoints of distinct matching edges.
def valid(ids):
    endpoints=[]
    for j in ids:
        u,v=E[j]
        for a,b in endpoints:
            if u==a or u==b or v==a or v==b: return False
            if a in neighbors[u] or b in neighbors[u]:return False
            if a in neighbors[v] or b in neighbors[v]:return False
        endpoints.append((u,v))
    return True

by_size={}
for k in range(7):
    by_size[k]=[tuple(t) for t in combinations(range(27),k) if valid(t)]
assert tuple(len(by_size[k]) for k in range(7))==(1,27,189,387,135,27,0)

def mapped_mask(t):
    return sum(1<<edge_perm[e] for e in t)
maxima=sorted(mapped_mask(t) for t in by_size[5])
assert maxima==cert['maxima_masks']
S=sorted(mapped_mask(t) for k in (3,4,5) for t in by_size[k])
assert S==cert['states_at_least_three']

# Independent reconstruction of the transition list using only set inclusion.
sets=[set(x) for k in (3,4,5) for x in by_size[k]]
# Sort on the affine-model bit encoding, never on LCF edge indices.
sets.sort(key=lambda t:mapped_mask(t))
by_card={k:[i for i,t in enumerate(sets) if len(t)==k] for k in (3,4,5)}
A=[[] for _ in sets]
T=[]
for i in by_card[3]:
    for j in by_card[4]:
        if sets[i]<sets[j]:
            A[i].append(j);A[j].append(i);T.append([i,j])
for i in by_card[4]:
    for j in by_card[5]:
        if sets[i]<sets[j]:
            A[i].append(j);A[j].append(i);T.append([i,j])
assert sorted(T)==cert['tar_edges']
assert len(T)==675

# Distances are computed on the LCF-generated reconfiguration graph.
Mids=by_card[5]
assert len(Mids)==27
count=Counter();ecc=Counter()
for k,i in enumerate(Mids):
    dist={i:0};q=deque([i])
    while q:
        a=q.popleft()
        for b in A[a]:
            if b not in dist:dist[b]=dist[a]+1;q.append(b)
    assert len(dist)==396
    ecc[max(dist[x] for x in Mids)] += 1
    for j in Mids[k+1:]:count[dist[j]]+=1
assert dict(sorted(count.items()))=={4:54,8:108,12:162,16:27}
assert ecc=={16:27}
# The line-graph certificate is checked against the LCF edges, independently
# transporting the affine index map back to LCF labeling.
compressed={i:set() for i in range(27)}
for i,s in enumerate(maxima):
    for j,t in enumerate(maxima[:i]):
        if (s&t).bit_count()==3:
            compressed[i].add(j);compressed[j].add(i)
F=cert['line_graph_edge_mapping']
inv={j:i for i,j in enumerate(edge_perm)}
for i in range(27):
    for j in range(i):
        e=E[inv[F[i]]];f=E[inv[F[j]]]
        assert (j in compressed[i]) == bool(set(e)&set(f))
print('VERIFY_OK LCF; 27 maximum induced matchings of size five; '
      '153 non-extendible matchings of size three; '
      'maxima distances '+str(dict(sorted(count.items())))+'; line-graph certificate verified')
