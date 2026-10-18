#!/usr/bin/env python3
"""Independent team-0-anchored edge-coloring enumeration and local-swap checker.
Use: python verify_coloring.py. Python standard library only.
"""
import itertools, collections, hashlib, json
V=tuple(range(8))
E=tuple(itertools.combinations(V,2))
bit={e:1<<i for i,e in enumerate(E)}
complete=(1<<28)-1

def build_matching(participants):
    if not participants:
        yield frozenset()
    else:
        a=participants[0]
        for b in participants[1:]:
            for tail in build_matching(tuple(x for x in participants[1:] if x!=b)):
                yield tail|{(a,b)}

M=[(sum(bit[e] for e in m),m) for m in build_matching(V)]
assert len(M)==105
# Each factor is distinguished by the opponent of team 0, avoiding factor order symmetry.
anchored={v:[] for v in V[1:]}
for mask,edges in M:
    for v in V[1:]:
        if (0,v) in edges:
            anchored[v].append(mask)
assert all(len(x)==15 for x in anchored.values())
factorizations=[]
def edge_coloring(opponent,occupied,classes):
    if opponent==8:
        assert occupied==complete
        factorizations.append(tuple(sorted(classes)))
        return
    for mask in anchored[opponent]:
        if mask&occupied==0:
            edge_coloring(opponent+1,occupied|mask,classes+(mask,))
edge_coloring(1,0,())
factorizations.sort()
assert len(factorizations)==6240 and len(set(factorizations))==6240
lookup={f:i for i,f in enumerate(factorizations)}

# Build independent neighbors by choosing each 4-vertex team set and a pair of classes.
# The two classes must each restrict to a full matching on these four teams,
# and their restricted edge sets must be disjoint and cover the same four-cycle.
blocks=[tuple(itertools.combinations(block,2)) for block in itertools.combinations(V,4)]
block_masks=[sum(bit[e] for e in B) for B in blocks]
valid_masks=set(mask for mask,_ in M)
adj=[set() for _ in factorizations]
for i,f in enumerate(factorizations):
    for a,b in itertools.combinations(f,2):
        pair=a|b
        found=False
        for block in block_masks:
            shared=pair&block
            if shared.bit_count()!=4:continue
            aa=a&shared;bb=b&shared
            if aa.bit_count()!=2 or bb.bit_count()!=2:continue
            # Each is a perfect matching, so two edges in the block cover four teams.
            nxt_a=a^shared;nxt_b=b^shared
            assert nxt_a in valid_masks and nxt_b in valid_masks
            new_f=tuple(sorted((set(f)-{a,b})|{nxt_a,nxt_b}))
            j=lookup[new_f]
            assert i!=j
            adj[i].add(j)
assert all(i in adj[j] for i,A in enumerate(adj) for j in A)
components=[];visited=set()
for s in range(len(adj)):
    if s in visited:continue
    component={s};front=[s]
    for u in front:
        for v in adj[u]:
            if v not in component:
                component.add(v);front.append(v)
    visited.update(component)
    components.append(front)
assert len(visited)==6240
size_count=collections.Counter(map(len,components))
ecc_count=collections.Counter()
for comp in components:
    if len(comp)==1:continue
    for s in comp:
        distances=[-1]*len(adj);distances[s]=0
        q=collections.deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if distances[v]<0:
                    distances[v]=distances[u]+1;q.append(v)
        assert sum(t>=0 for t in distances)==len(comp)
        ecc_count[max(distances)]+=1
state_lines=[' '.join(f'{m:07x}' for m in ff)+'\n' for ff in factorizations]
state_bytes=''.join(state_lines).encode('ascii')
lines=[f'{i} {j}\n' for i,A in enumerate(adj) for j in sorted(A) if j>i]
summary={'vertices':len(factorizations),'perfect_matchings':len(M),'edges':len(lines),
         'degree_distribution':dict(sorted(collections.Counter(map(len,adj)).items())),
         'component_sizes':dict(sorted(size_count.items())),
         'eccentricities_nontrivial':dict(sorted(ecc_count.items())),
         'radius_nontrivial':min(ecc_count),'diameter_nontrivial':max(ecc_count),
         'ordered_edge_list_sha256':hashlib.sha256(''.join(lines).encode('ascii')).hexdigest(),
         'ordered_states_sha256':hashlib.sha256(state_bytes).hexdigest()}
print(json.dumps(summary,sort_keys=True))
assert summary['edges']==17640 and summary['component_sizes']=={1:960,5280:1}
