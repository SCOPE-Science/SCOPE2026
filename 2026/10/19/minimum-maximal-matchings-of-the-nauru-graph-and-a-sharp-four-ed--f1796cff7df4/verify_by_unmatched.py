#!/usr/bin/env python3
"""Independent-set/complement-perfect-matching enumeration for GP(12,5)."""
import itertools, json, collections, hashlib
from pathlib import Path

N = 24
edges = sorted({tuple(sorted(e)) for i in range(12) for e in
                ((i, (i + 1) % 12), (i, 12+i), (12+i, 12+(i+5) % 12))})
assert len(edges) == 36
edge_index = {e: j for j, e in enumerate(edges)}
adj = [0] * N
for a,b in edges:
    adj[a] |= 1<<b
    adj[b] |= 1<<a

def complement_matchings(mask):
    if not mask:
        yield ()
        return
    bit = mask & -mask
    u = bit.bit_length()-1
    neighbors = adj[u] & (mask ^ bit)
    while neighbors:
        b = neighbors & -neighbors
        neighbors -= b
        v = b.bit_length()-1
        for tail in complement_matchings(mask ^ bit ^ b):
            yield tuple(sorted((edge_index[(min(u,v), max(u,v))],)+tail))

full = (1<<N)-1
independent_count = 0
multiplicity = collections.Counter()
matchings = set()
for chosen in itertools.combinations(range(N), 8):
    mask = sum(1<<v for v in chosen)
    if any(adj[v] & mask for v in chosen):
        continue
    independent_count += 1
    found = list(complement_matchings(full ^ mask))
    multiplicity[len(found)] += 1
    matchings.update(found)
matchings = sorted(matchings)
assert independent_count == 2964 and multiplicity == {0:2874, 1:90}
assert len(matchings) == 90

# Every maximal matching has >= ceil(36/5)=8 edges by cubic edge domination.
# The following exhaustive list therefore contains all minimum maximal matchings.

def graph_at(k):
    adjacency = [set() for _ in matchings]
    for i, a in enumerate(matchings):
        aa = set(a)
        for j in range(i+1,len(matchings)):
            if len(aa.difference(matchings[j])) <= k:
                adjacency[i].add(j)
                adjacency[j].add(i)
    return adjacency

def components(adjacency):
    done=set()
    out=[]
    for i in range(len(adjacency)):
        if i in done: continue
        seen={i}
        queue=[i]
        for v in queue:
            for w in sorted(adjacency[v]):
                if w not in seen:
                    seen.add(w); queue.append(w)
        done.update(seen)
        out.append(sorted(seen))
    return sorted(out, key=lambda comp: comp[0])

def ecc_map(adjacency):
    all_ecc=[]
    for s in range(len(adjacency)):
        d={s:0}
        queue=[s]
        for u in queue:
            for v in sorted(adjacency[u]):
                if v not in d:
                    d[v]=d[u]+1; queue.append(v)
        all_ecc.append(max(d.values()))
    return all_ecc

adjs={i:graph_at(i) for i in [1,2,3,4]}
comps={i:components(adjs[i]) for i in adjs}
ecc2=ecc_map(adjs[2]); ecc4=ecc_map(adjs[4])
assert [len(c) for c in comps[1]]==[1]*90
assert sorted(map(len,comps[2]))==[30]*3
assert comps[2]==comps[3]
assert [sum(len(x) for x in adjs[k])//2 for k in (1,2,3,4)] == [0,180,180,522]
assert collections.Counter(ecc2)=={5:90}
assert collections.Counter(ecc4)=={3:18,4:72}
assert len(comps[4])==1
assert collections.Counter(map(len,adjs[2]))=={4:90}
assert collections.Counter(map(len,adjs[4]))=={11:72,14:18}

# The natural graph symmetries cycle the three components and transpose two.
idx={x:i for i,x in enumerate(matchings)}
def image_matching(m, vertex_map):
    return idx[tuple(sorted(edge_index[tuple(sorted((vertex_map[edges[e][0]],vertex_map[edges[e][1]])))] for e in m))]
rot=[(v+1)%12 if v<12 else 12+(v-12+1)%12 for v in range(N)]
ref=[(-v)%12 if v<12 else 12+(-(v-12))%12 for v in range(N)]
labels={v:c for c, comp in enumerate(comps[2]) for v in comp}
def component_permutation(vertex_map):
    return [labels[image_matching(matchings[comp[0]],vertex_map)] for comp in comps[2]]
rotperm=component_permutation(rot)
refperm=component_permutation(ref)
assert sorted(rotperm)==sorted(refperm)==[0,1,2]
assert all(rotperm[i]!=i for i in range(3))
assert sum(refperm[i]==i for i in range(3))==1

cert = {
    'definition': 'GP(12,5), u_i=i, v_i=12+i, i mod 12; edges u_i u_(i+1), u_i v_i, v_i v_(i+5)',
    'edges': [list(e) for e in edges],
    'matching_size':8,
    'independent_eight_sets':independent_count,
    'independent_eight_multiplicities':{str(k):v for k,v in sorted(multiplicity.items())},
    'minimum_maximal_matchings':[list(m) for m in matchings],
    'exchange_edges':{str(k):[[i,j] for i,ns in enumerate(adjs[k]) for j in sorted(ns) if i<j] for k in [1,2,3,4]},
    'components_t2':comps[2],
    'eccentricities_t2':ecc2,
    'eccentricities_t4':ecc4,
    'component_action_rotation':rotperm,
    'component_action_reflection':refperm,
}
path=Path(__file__).with_name('certificate.json')
path.write_text(json.dumps(cert,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n', encoding='utf-8')
print('minimum=8 matchings=90 independent8=2964 zero_induced_factor=2874 unique_induced_factor=90')
print('edges_by_t=' + str([len(cert['exchange_edges'][str(k)]) for k in [1,2,3,4]]))
print('t2_components=' + str([len(c) for c in comps[2]]) + ' t2_ecc=' + str(dict(sorted(collections.Counter(ecc2).items()))))
print('t4_components=' + str([len(c) for c in comps[4]]) + ' t4_ecc=' + str(dict(sorted(collections.Counter(ecc4).items()))))
print('t2_component_symmetries=' + str((rotperm,refperm)))
print('certificate_sha256=' + hashlib.sha256(path.read_bytes()).hexdigest())
