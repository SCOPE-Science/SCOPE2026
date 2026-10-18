"""Exhaustive small-order connected-chordal 1-WL census.

Requires Python 3.10+ and NetworkX 3.5+ (tested with 3.6.1).
Run: python artifacts/verify.py
No network access or external graph database file is required.
"""
from itertools import combinations
from collections import Counter,defaultdict
import networkx as nx

assert nx.__version__.split('.')[0]=='3'
base_all=[g.copy() for g in nx.graph_atlas_g() if 1<=len(g)<=7 and nx.is_connected(g) and nx.is_chordal(g)]
counts=Counter(len(g) for g in base_all)
assert [counts[n] for n in range(1,8)] == [1,1,2,5,15,58,272]

# Complete enumeration of connected chordal graphs: a connected chordal H
# on 8 vertices admits a simplicial vertex whose deletion stays connected.
# Conversely, adding a vertex with a nonempty clique neighborhood preserves
# connectedness and chordality.
reps_by_hash=defaultdict(list)
attempts=0
for B in [x for x in base_all if len(x)==7]:
    vs=list(B)
    for mask in range(1,1<<7):
        S=[vs[i] for i in range(7) if mask >> i & 1]
        if any(not B.has_edge(a,b) for a,b in combinations(S,2)):continue
        G=B.copy(); G.add_node(7);G.add_edges_from((7,u) for u in S)
        attempts += 1
        # This cryptographic hash merely indexes a candidate bucket; each
        # graph in the bucket is tested by exact isomorphism, not hash equality.
        h=nx.weisfeiler_lehman_graph_hash(G,iterations=8,digest_size=24)
        if not any(nx.is_isomorphic(G,H) for H in reps_by_hash[h]):
            reps_by_hash[h].append(G)

base8=[g for v in reps_by_hash.values() for g in v]
assert attempts==7268 and len(base8)==1614
assert all(nx.is_chordal(g) and nx.is_connected(g) for g in base8)

# Independent, deterministic, collision-free 1-WL canonical refinement
# simultaneously across all representatives of orders <=8.
all_graphs=base_all+base8
colours=[[0]*len(g) for g in all_graphs]
profiles=None
previous_signature_partition = None
last_signature_partition = None
for round_id in range(16):
    raw=[]
    for g,C in zip(all_graphs,colours):
        raw.append([(C[v], tuple(sorted(C[w] for w in g.neighbors(v)))) for v in g])
    types={s:k for k,s in enumerate(sorted(set(s for r in raw for s in r)))}
    colours=[[types[s] for s in r] for r in raw]
    prof=defaultdict(list)
    for idx,C in enumerate(colours):prof[tuple(sorted(C))].append(idx)
    if round_id in [1,7]:
        small_bad=[v for v in prof.values() if len(v)>1 and min(len(all_graphs[i]) for i in v)<=7]
        ambiguous=[v for v in prof.values() if len(v)>1 and len(all_graphs[v[0]])==8]
        print('round',round_id+1,'small_bad',len(small_bad),'ambiguous8',len(ambiguous),'sizes',[len(x) for x in ambiguous])
    profiles=prof
    # Grouping of each vertex across all graphs, with equal colours.
    partitions_by_id = defaultdict(set)
    for i,C in enumerate(colours):
        for v,c in enumerate(C):partitions_by_id[c].add((i,v))
    vertex_partition = frozenset(map(frozenset, partitions_by_id.values()))
    if round_id == 8: previous_signature_partition=vertex_partition
    if round_id == 15: last_signature_partition=vertex_partition
assert previous_signature_partition == last_signature_partition, 'Global colour partition not stable'
assert not any(len(v)>1 and len(all_graphs[v[0]])<=7 for v in profiles.values())
ambiguous=[v for v in profiles.values() if len(v)>1]
assert len(ambiguous)==2 and [len(z) for z in ambiguous]==[2,2]
print('connected_counts',dict(sorted(counts.items())),'n8',len(base8),'new_graph_attempts',attempts)

for p,inds in enumerate(ambiguous,1):
    H,K=(all_graphs[i] for i in inds)
    assert len(H)==len(K)==8
    assert not nx.is_isomorphic(H,K)
    print('PAIR',p,'m',H.number_of_edges(),K.number_of_edges(),'degree_hist',dict(sorted(Counter(dict(H.degree()).values()).items())))
    for name,G in [('H',H),('K',K)]:
      print(name,'edges',sorted([tuple(sorted(e)) for e in G.edges()]))
      print(name,'cliques4',sum(1 for x in nx.enumerate_all_cliques(G) if len(x)==4))
      degs=dict(G.degree()); dsmall=min(degs.values()); dlarge=max(degs.values());
      print(name,'degree2_neighborhoods',sorted(tuple(sorted(G.neighbors(v))) for v in G if G.degree(v)==2))
    # Both graphs have 3 color classes by degree, except second pair only 2 classes.
    for G in (H,K):
      deg_groups=defaultdict(list)
      for v,d in G.degree: deg_groups[d].append(v)
      quotient=[]
      for d,vs in sorted(deg_groups.items()):
        row=[len(set(G.neighbors(vs[0])) & set(deg_groups[e])) for e in sorted(deg_groups)]
        assert all([len(set(G.neighbors(v)) & set(deg_groups[e])) for e in sorted(deg_groups)]==row for v in vs)
        quotient.append(row)
      print('quotient',quotient)

print('VERIFICATION_PASS: 1-WL ambiguities are precisely two unordered pairs on eight vertices.')
