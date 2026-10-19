#!/usr/bin/env python3
"""Exact enumeration of Pappus 3-edge-colourings using perfect matchings.

The 27 entries of a colouring are ordered lexicographically by (x,y,m),
with the edge (x,y,m) joining point (x,y) to line (m,y-m*x mod 3).
Run: python verify_factorizations.py --certificate pappus_hexagon_certificate.json
"""
import argparse
import hashlib
import json
from collections import Counter, deque
from itertools import combinations, permutations

EDGES = tuple((x,y,m) for x in range(3) for y in range(3) for m in range(3))
POINTS = tuple((x,y) for x in range(3) for y in range(3))
LINES = tuple((m,b) for m in range(3) for b in range(3))
point_edges = {p:[] for p in POINTS}
line_edges = {l:[] for l in LINES}
ends = []
for i,(x,y,m) in enumerate(EDGES):
    p=(x,y); l=(m,(y-m*x)%3)
    ends.append((p,l));point_edges[p].append(i);line_edges[l].append(i)
assert len(EDGES)==27 and all(len(v)==3 for v in point_edges.values())
assert all(len(v)==3 for v in line_edges.values())

# Exhaustive traversal of all point-to-line bijections respecting incidence.
matchings=[]
def visit(i,used,m):
    if i==len(POINTS):
        matchings.append(tuple(m));return
    for edge in point_edges[POINTS[i]]:
        line=ends[edge][1]
        if line not in used:
            used.add(line);m.append(edge)
            visit(i+1,used,m)
            m.pop();used.remove(line)
visit(0,set(),[])
assert len(matchings)==42 and len(set(matchings))==42

def components_of_edges(indices):
    allowed=set(indices)
    unseen=set(allowed);out=[]
    while unseen:
        first=min(unseen);group=set([first]);todo=[first]
        unseen.remove(first)
        while todo:
            j=todo.pop()
            p,l=ends[j]
            for k in point_edges[p]+line_edges[l]:
                if k in unseen:
                    unseen.remove(k);group.add(k);todo.append(k)
        out.append(tuple(sorted(group)))
    return tuple(sorted(out))

def alternating_colour(component):
    # BFS 2-colouring of the edge adjacencies in one even residual cycle.
    rem=set(component)
    colour={component[0]:1};q=deque([component[0]])
    while q:
        i=q.popleft();p,l=ends[i]
        for j in point_edges[p]+line_edges[l]:
            if j==i or j not in rem: continue
            need=3-colour[i]
            if j in colour:assert colour[j]==need
            else: colour[j]=need;q.append(j)
    assert len(colour)==len(component)
    return colour

states=set();mtypes=Counter()
for matching in matchings:
    residual=set(range(27))-set(matching)
    parts=components_of_edges(residual)
    assert all(len(p)%2==0 for p in parts)
    mtypes[tuple(sorted(map(len,parts)))]+=1
    base={i:0 for i in matching}
    alt=[alternating_colour(part) for part in parts]
    for mask in range(1<<len(parts)):
        d=base.copy()
        for j,cc in enumerate(alt):
            flip=(mask>>j)&1
            d.update({i:3-c if flip else c for i,c in cc.items()})
        state=tuple(d[i] for i in range(27))
        assert all(sorted(state[i] for i in ids)==[0,1,2] for ids in point_edges.values())
        assert all(sorted(state[i] for i in ids)==[0,1,2] for ids in line_edges.values())
        states.add(state)
states=sorted(states)
assert len(states)==120
assert mtypes==Counter({(18,):36,(6,6,6):6})
index={s:i for i,s in enumerate(states)}

def sign(triple):
    return -1 if sum(triple[i]>triple[j] for i in range(3) for j in range(i+1,3))%2 else 1

def parity(s):
    z=1
    for ids in point_edges.values():
        # point neighbors are already in slope order 0,1,2
        z*=sign([s[i] for i in ids])
    for ids in line_edges.values():
        # line neighbors are in abscissa order 0,1,2
        z*=sign([s[i] for i in ids])
    return z
parities=tuple(parity(s) for s in states)
assert Counter(parities)==Counter({-1:60,+1:60})

six=set();full=set();types=Counter()
for i,s in enumerate(states):
    for a,b in combinations((0,1,2),2):
        parts=components_of_edges(j for j,c in enumerate(s) if c in (a,b))
        types[tuple(sorted(map(len,parts)))]+=1
        for part in parts:
            new=list(s)
            for k in part: new[k]=a+b-new[k]
            t=tuple(new)
            assert t in index and t!=s
            j=index[t];pair=(min(i,j),max(i,j))
            full.add(pair)
            if len(part)==6:six.add(pair)
assert len(six)==216 and len(full)==324

def adjacency(pairs):
    adj=[set() for _ in states]
    for i,j in pairs:adj[i].add(j);adj[j].add(i)
    return adj

def connected_parts(adj):
    unseen=set(range(len(adj)));out=[]
    while unseen:
        root=min(unseen);unseen.remove(root);q=[root];part={root}
        while q:
            v=q.pop()
            for u in adj[v]&unseen:
                unseen.remove(u);part.add(u);q.append(u)
        out.append(part)
    return out

def diameter_and_radius(adj,part):
    eccentricities=[]
    for start in sorted(part):
        dist={start:0};q=deque([start])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if w not in dist:
                    dist[w]=dist[v]+1;q.append(w)
        assert set(dist)==part
        eccentricities.append(max(dist.values()))
    return min(eccentricities),max(eccentricities)

adjsix=adjacency(six);adjfull=adjacency(full)
Cs=connected_parts(adjsix);Cf=connected_parts(adjfull)
assert sorted(map(len,Cs))==[60,60]
assert sorted(map(len,Cf))==[60,60]
assert sorted(diameter_and_radius(adjsix,c) for c in Cs)==[(6,6),(6,6)]
assert sorted(diameter_and_radius(adjfull,c) for c in Cf)==[(4,4),(4,4)]
assert all(len({parities[v] for v in c})==1 for c in Cs)
assert all(len({parities[v] for v in c})==1 for c in Cf)
assert Counter(map(len,adjsix))==Counter({3:108,9:12})
assert Counter(map(len,adjfull))==Counter({5:108,9:12})

# Combinatorial isomorphism test: each component has six degree-nine hubs.
# Their deletion leaves nine 6-cycles, alternatingly assigned to two hubs.
# The nine hub pairs form exactly K_{3,3}.
for comp in Cs:
    hubs={v for v in comp if len(adjsix[v])==9}
    assert len(hubs)==6
    ordinary=comp-hubs
    assert len(ordinary)==54
    assert all(len(adjsix[v]&hubs)==1 and len(adjsix[v]&ordinary)==2 for v in ordinary)
    undiscovered=set(ordinary);pairs=[]
    while undiscovered:
        root=min(undiscovered);undiscovered.remove(root);todo=[root];cycle={root}
        while todo:
            v=todo.pop()
            for w in adjsix[v]&undiscovered:
                undiscovered.remove(w);cycle.add(w);todo.append(w)
        assert len(cycle)==6
        assert all(len(adjsix[v]&cycle)==2 for v in cycle)
        touched={next(iter(adjsix[v]&hubs)) for v in cycle}
        assert len(touched)==2
        p,q=sorted(touched)
        assert sum(next(iter(adjsix[v]&hubs))==p for v in cycle)==3
        assert sum(next(iter(adjsix[v]&hubs))==q for v in cycle)==3
        assert all(next(iter(adjsix[v]&hubs))!=next(iter(adjsix[w]&hubs))
                   for v in cycle for w in adjsix[v]&cycle)
        pairs.append((p,q))
    assert len(pairs)==9 and len(set(pairs))==9
    meta={v:set() for v in hubs}
    for p,q in pairs:meta[p].add(q);meta[q].add(p)
    assert all(len(nbrs)==3 for nbrs in meta.values())
    # K3,3 criterion among six vertices with nine edges
    U={min(hubs)}|meta[min(hubs)]
    assert len(U)==4 # root and three opposite hubs
    left=set(hubs)-meta[min(hubs)]
    right=meta[min(hubs)]
    assert len(left)==3 and len(right)==3
    assert all(meta[x]==right for x in left)
    assert all(meta[y]==left for y in right)

# Refine comparison with the known 20-class color-permutation quotient.
# The new local switching graph is a six-sheeted regular covering of it.
relabelings=list(permutations((0,1,2)))
reps=[min(tuple(pi[col] for col in state) for pi in relabelings) for state in states]
canonical_orbits=sorted(set(reps));orbit_index={t:i for i,t in enumerate(canonical_orbits)}
orb=[orbit_index[t] for t in reps]
assert len(canonical_orbits)==20
assert Counter(orb)==Counter({j:6 for j in range(20)})
q_edges={tuple(sorted((orb[i],orb[j]))) for i,j in six if orb[i]!=orb[j]}
assert len(q_edges)==36
q_adj=[set() for _ in range(20)]
for i,j in q_edges:q_adj[i].add(j);q_adj[j].add(i)
assert Counter(map(len,q_adj))==Counter({3:18,9:2})
q_components=[];unseen=set(range(20))
while unseen:
    root=min(unseen);unseen.remove(root);work=[root];group={root}
    while work:
        v=work.pop()
        for w in q_adj[v]&unseen:
            unseen.remove(w);group.add(w);work.append(w)
    q_components.append(group)
assert sorted(map(len,q_components))==[10,10]
for group in q_components:
    hubs=[j for j in group if len(q_adj[j])==9]
    assert len(hubs)==1
    center=hubs[0];leaves=group-{center};components=[]
    while leaves:
        first=min(leaves);leaves.remove(first);todo=[first];C={first}
        while todo:
            v=todo.pop()
            for w in q_adj[v]&leaves:
                leaves.remove(w);C.add(w);todo.append(w)
        assert len(C)==3 and all(len(q_adj[u]&C)==2 for u in C)
        components.append(C)
    assert len(components)==3
for v in range(len(states)):
    assert len({orb[w] for w in adjsix[v]})==len(adjsix[v])==len(q_adj[orb[v]])
    assert {orb[w] for w in adjsix[v]}==q_adj[orb[v]]
assert all(len({parities[v] for v in range(120) if orb[v]==i})==1 for i in range(20))

for i,j in six:assert parities[i]==parities[j]
canon={'states':[list(s) for s in states], 'hexagon_edges':[list(p) for p in sorted(six)]}
hash_states=hashlib.sha256(json.dumps(canon['states'],separators=(',',':')).encode()).hexdigest()
hash_edges=hashlib.sha256(json.dumps(canon['hexagon_edges'],separators=(',',':')).encode()).hexdigest()
summary={
 'graph':'Pappus incidence graph over F_3, edges ordered (x,y,m)',
 'matching_count':len(matchings),
 'color_permutation_quotient_vertices':len(canonical_orbits),
 'color_permutation_quotient_edges':len(q_edges),
 'color_permutation_quotient_components':sorted(map(len,q_components)),
 'color_permutation_quotient_structure':'two K1 join 3 disjoint K3; six-sheeted covering',
 'matching_complement_cycle_types':{','.join(map(str,key)):val for key,val in sorted(mtypes.items())},
 'state_count':len(states),'parity_counts':{str(k):v for k,v in sorted(Counter(parities).items())},
 'hexagon_edges':len(six),'hexagon_component_sizes':sorted(map(len,Cs)),
 'hexagon_degrees':{str(k):v for k,v in sorted(Counter(map(len,adjsix)).items())},
 'hexagon_component_radius_diameter':sorted([list(diameter_and_radius(adjsix,c)) for c in Cs]),
 'hexagon_component_structure':'two copies of the alternating 6-cycle thickening of K3,3',
 'all_kempe_edges':len(full),'all_kempe_component_sizes':sorted(map(len,Cf)),
 'all_kempe_degrees':{str(k):v for k,v in sorted(Counter(map(len,adjfull)).items())},
 'all_kempe_component_radius_diameter':sorted([list(diameter_and_radius(adjfull,c)) for c in Cf]),
 'states_sha256':hash_states,'hexagon_edges_sha256':hash_edges
}
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--certificate')
    args=parser.parse_args()
    if args.certificate:
        with open(args.certificate,'w',encoding='utf-8') as f:
            json.dump({'schema_version':1,'summary':summary,**canon},f,sort_keys=True,separators=(',',':'))
            f.write('\n')
    print(json.dumps(summary,sort_keys=True,indent=2))
    print('VERIFY_OK')
