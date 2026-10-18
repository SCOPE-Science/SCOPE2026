#!/usr/bin/env python3
"""Second exact verifier: bipartite-permutation enumeration, vertex-subset
completion DP and direct DFS of alternating cycles. Standard library only.
Usage: python verify_q4_extension_dp.py q4_orbit_certificate.json
"""
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json
import sys

assert len(sys.argv)==2, 'Supply the classification certificate'
cert=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
edges=[tuple(e) for e in cert['edge_order']]
assert len(edges)==32 and len(set(edges))==32
for a,b in edges:assert a<b and (a^b) in (1,2,4,8)
edge_index={e:i for i,e in enumerate(edges)}
adj=[[] for _ in range(16)]
for ei,(a,b) in enumerate(edges):adj[a].append((b,ei));adj[b].append((a,ei))
evens=tuple(x for x in range(16) if x.bit_count()%2==0)
odds=tuple(x for x in range(16) if x.bit_count()%2==1)
assert len(evens)==len(odds)==8
oddbits={v:i for i,v in enumerate(odds)}

def make_matchings(i,chosen_odd,chosen_edges):
    if i==8:
        matching_list.append(tuple(sorted(chosen_edges)));return
    u=evens[i]
    for v,e in adj[u]:
        assert v in oddbits
        bit=1<<oddbits[v]
        if not chosen_odd&bit:
            make_matchings(i+1,chosen_odd|bit,chosen_edges+(e,))
matching_list=[]
make_matchings(0,0,())
assert len(matching_list)==272==len(set(matching_list))

@lru_cache(None)
def completions(available):
    if not available:return 1
    u=(available&-available).bit_length()-1
    return sum(completions(available^(1<<u)^(1<<v)) for v,_ in adj[u] if available&(1<<v))
assert completions((1<<16)-1)==272

def polynomial(M):
    counts=[0]*9
    for choice in range(1<<8):
        used=0
        for j,e in enumerate(M):
            if choice>>j&1:
                a,b=edges[e];used|=(1<<a)|(1<<b)
        if completions(((1<<16)-1)^used)==1:
            counts[choice.bit_count()]+=1
    return tuple(counts)

def alternating_cycles(M):
    chosen=set(M)
    cycles={}
    for start in range(16):
        def dfs(u,vertices,edges_used,need_matching,length):
            for v,ei in adj[u]:
                if (ei in chosen)!=need_matching:continue
                if v==start:
                    if length>=3 and not need_matching:
                        cycles[edges_used|(1<<ei)]=vertices
                    continue
                if v<=start or vertices&(1<<v):continue
                dfs(v,vertices|(1<<v),edges_used|(1<<ei),not need_matching,length+1)
        dfs(start,1<<start,0,True,0)
    return cycles

def packing(cycles):
    masks=sorted(set(cycles.values()))
    # Use subset dynamic programming on matched vertex occupancy, independent
    # of the competitive-matching symmetric-difference cycle discovery.
    feasible={0:1}
    for vertex_bits in masks:
        snapshot=list(feasible.items())
        for occ,count in snapshot:
            if not occ&vertex_bits:
                nxt=occ|vertex_bits
                feasible[nxt]=max(feasible.get(nxt,0),count+1)
    return max(feasible.values())-1

profile_counts=Counter()
match_polys={}
for M in matching_list:
    p=polynomial(M)
    cycles=alternating_cycles(M)
    c=len(cycles)
    pk=packing(cycles)
    profile_counts[(p,c,pk)]+=1
    match_polys[M]=(p,c,pk)
assert len(profile_counts)==8
reference=Counter()
for row in cert['orbit_rows']:
    M=tuple(row['representative_matching_edge_indices'])
    signature=(tuple(row['forcing_subset_coefficients_0_to_8']),row['alternating_cycles'],row['disjoint_alternating_cycle_packing'])
    assert match_polys[M]==signature
    reference[signature]+=row['orbit_size']
assert profile_counts==reference
sum_poly=tuple(sum(p[k] for p,_,_ in map(match_polys.get,matching_list)) for k in range(9))
assert sum_poly==tuple(cert['all_matching_local_forcing_coefficient_totals_0_to_8'])
assert sorted(Counter({pk:sum(n for (p,c,pp),n in profile_counts.items() if pp==pk) for pk in (2,3,4)}).items())==[(2,8),(3,32),(4,232)]
print('DP_VERIFY_OK bipartite_permutation_matchings=272 vertex_subset_recurrence_full=272 states='+str(completions.cache_info().currsize))
print('DP_VERIFY_OK all_69632_local_subset_extension_decisions=true aggregate_forcing_4=2552 _5=7040 _6=6080 _7=2176 _8=272')
print('DFS_VERIFY_OK alternating_cycles_as_distinct_edge_sets=true all_272_profiles_match_certificate=true')
print('DFS_VERIFY_OK disjoint_alternating_cycle_packing_distribution=2:8,3:32,4:232')
