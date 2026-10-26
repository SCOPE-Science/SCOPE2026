"""Independent edge-list, matching, ILP, and automorphism check for the McGee cage.
Dependencies: networkx>=2.8; scipy>=1.9; numpy>=1.23.
Run: python verify_independent.py certificate.json
"""
import json, sys
from collections import Counter
import networkx as nx
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

# 36-edge presentation independent of LCF construction in verify_exact.py
EDGES = [
 (0,1),(0,12),(0,23),(1,2),(1,8),(2,3),(2,19),
 (3,4),(3,15),(4,5),(4,11),(5,6),(5,22),(6,7),(6,18),
 (7,8),(7,14),(8,9),(9,10),(9,21),(10,11),(10,17),
 (11,12),(12,13),(13,14),(13,20),(14,15),(15,16),
 (16,17),(16,23),(17,18),(18,19),(19,20),(20,21),
 (21,22),(22,23)]

G=nx.Graph();G.add_nodes_from(range(24));G.add_edges_from(EDGES)
assert G.number_of_nodes()==24 and G.number_of_edges()==36
assert nx.is_connected(G) and all(d==3 for v,d in G.degree())

# Matching enumeration chooses the first still-uncovered EDGE, branching over
# edges at the smallest unmatched endpoint; separate representation/recursion.
adj=[[] for _ in range(24)]
for a,b in EDGES:adj[a].append(b);adj[b].append(a)

def enumerate_matchings():
    out=set()
    def extend(mates,chosen):
        start=next((i for i in range(24) if i not in mates),None)
        if start is None:
            out.add(tuple(sorted(chosen)));return
        for b in adj[start]:
            if b not in mates:
                extend(mates|{start,b},chosen+[(min(start,b),max(start,b))])
    extend(set(),[])
    return sorted(out)

M=enumerate_matchings();assert len(M)==60
if len(sys.argv)!=2:raise SystemExit('usage: python verify_independent.py certificate.json')
with open(sys.argv[1],encoding='utf-8') as f:certificate=json.load(f)
assert len(certificate['rows'])==60
assert [list(map(list,m)) for m in M]==[row['matching'] for row in certificate['rows']]
assert [list(e) for e in sorted(EDGES)]==certificate['edges']

# Different optimization method: integer linear program for each matching.
# Matrix rows are rival matchings, columns are eligible deleted edges.
counts=Counter()
for idx,target in enumerate(M):
    targetset=set(target)
    choices=[e for e in sorted(EDGES) if e not in targetset]
    competitors=[set(x) for x in M if x!=target]
    A=np.array([[int(e in alt) for e in choices] for alt in competitors], dtype=float)
    result=milp(np.ones(len(choices)),integrality=np.ones(len(choices)),
       bounds=Bounds(np.zeros(len(choices)),np.ones(len(choices))),
       constraints=LinearConstraint(A,np.ones(len(competitors)),np.inf),
       options={'time_limit':5,'mip_rel_gap':0})
    assert result.success and result.mip_gap<=1e-8,(idx,result.message)
    answer=round(result.fun)
    assert abs(result.fun-answer)<1e-8
    row=certificate['rows'][idx]
    assert answer==row['anti_forcing_number'],idx
    deletion={tuple(e) for e in row['witness_deleted_edges']}
    assert len(deletion)==answer and not deletion.intersection(targetset)
    # Directly count remaining perfect matchings after proposed deletion.
    assert sum(not deletion.intersection(alt) for alt in competitors)==0
    counts[answer]+=1
assert counts=={5:40,6:20},counts

# Independently check the natural complement 2-factor invariant.
profile=Counter()
for m in M:
    H=G.copy();H.remove_edges_from(m)
    assert all(d==2 for _,d in H.degree())
    profile[tuple(sorted(map(len,nx.connected_components(H))))]+=1
assert profile=={(8,8,8):12,(12,12):6,(24,):42}

# Verify the eight perfect-matching orbits under all graph automorphisms.
match_index={m:i for i,m in enumerate(M)}
perms=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
assert len(perms)==32
remaining=set(range(60));orbits=[]
while remaining:
    i=min(remaining)
    orbital={match_index[tuple(sorted((min(p[a],p[b]),max(p[a],p[b])) for a,b in M[i]))]
             for p in perms}
    assert orbital <= remaining
    remaining-=orbital
    nums={certificate['rows'][j]['anti_forcing_number'] for j in orbital}
    optcerts={certificate['rows'][j]['minimum_deletion_sets'] for j in orbital}
    assert len(nums)==len(optcerts)==1
    orbits.append([i,len(orbital),next(iter(nums)),next(iter(optcerts))])
assert orbits==[[0,4,6,272],[1,16,5,62],[4,8,5,88],[5,16,5,158],
                [7,4,6,1198],[10,8,6,724],[24,2,6,424],[29,2,6,728]]
print('INDEPENDENT_MATCHINGS',len(M),'ANTI_FORCING',dict(sorted(counts.items())))
print('TWO_FACTOR_TYPES',dict(sorted(profile.items())))
print('AUTOMORPHISM_GROUP',len(perms),'MATCHING_ORBITS',orbits)
print('INTEGER_PROGRAMS_AND_WITNESSES_OK')
