#!/usr/bin/env python3
"""Independent exact exhaustive checks for Heawood D_k. Python 3 stdlib."""
from collections import Counter, deque
from itertools import combinations

N = 14
all_mask = (1 << N) - 1
# Cyclic (7,3,1) difference-set model for the Fano plane.
lines = [sum(1 << ((j + t) % 7) for t in (0, 1, 3)) for j in range(7)]
assert all(x.bit_count() == 3 for x in lines)
assert all((lines[i] & lines[j]).bit_count() == 1 for i,j in combinations(range(7),2))
closed = [1 << i for i in range(N)]
for j, line in enumerate(lines):
    for i in range(7):
        if line >> i & 1:
            closed[i] |= 1 << (7 + j)
            closed[7 + j] |= 1 << i

# Distinct algorithm from OR-recurrence: direct closed-neighborhood intersection.
def dominates(s):
    return all(closed[i] & s for i in range(N))

D = {s for s in range(1 << N) if dominates(s)}
counts = Counter(s.bit_count() for s in D)
print('domination counts',sorted(counts.items()),flush=True)
assert [counts[i] for i in range(4,15)] == [21,224,931,1962,2394,1862,987,364,91,14,1]
minimal = {s for s in D if all(s ^ (1 << i) not in D for i in range(N) if (s >> i) & 1)}
assert Counter(s.bit_count() for s in minimal) == {4:21,5:14,6:28,7:2}

# Verify full geometric description of inclusion-minimal dominating sets.
by_pair=set()
for p, q in combinations(range(7),2):
    lines_avoiding=[j for j, m in enumerate(lines) if not (m & (1<<p | 1<<q))]
    assert len(lines_avoiding) == 2
    by_pair.add((1<<p)|(1<<q)|sum(1<<(j+7) for j in lines_avoiding))
by_flag=set()
for p in range(7):
    L=sum(1<<(7+j) for j, m in enumerate(lines) if not m>>p&1)
    by_flag.add((1<<p)|L)
for j,line in enumerate(lines):
    P=sum(1<<i for i in range(7) if not line>>i&1)
    by_flag.add(P | (1<<(7+j)))
by_antiflag=set()
for j,line in enumerate(lines):
    for p in range(7):
        if not (line>>p&1):
            pencils=sum(1<<(7+k) for k, m in enumerate(lines) if m>>p&1)
            by_antiflag.add(line|pencils)
side_pair={(1<<7)-1,((1<<7)-1)<<7}
assert len(by_pair)==21 and len(by_flag)==14 and len(by_antiflag)==28
assert minimal == by_pair | by_flag | by_antiflag | side_pair
print('geometric minimal classification verified',flush=True)

def graph(k):
    nodes=sorted(s for s in D if s.bit_count()<=k)
    pos={s:i for i,s in enumerate(nodes)}
    nbrs=[[pos[t] for bit in range(N) if (t:=s ^ (1<<bit)) in pos] for s in nodes]
    return nodes,nbrs

def component_sizes(nbrs):
    unseen=set(range(len(nbrs))); comps=[]
    while unseen:
        start=unseen.pop(); q=deque([start]); comp=[start]
        while q:
            for y in nbrs[q.popleft()]:
                if y in unseen:
                    unseen.remove(y);q.append(y);comp.append(y)
        comps.append(comp)
    return comps

expected={
4:(21,0,Counter({1:21})),
5:(245,210,Counter({11:21,1:14})),
6:(1176,2226,Counter({1148:1,1:28})),
7:(3138,9674,Counter({3136:1,1:2})),
8:(5532,23408,Counter({5532:1}))}
for k in range(4,9):
    nodes,nbrs=graph(k)
    comps=component_sizes(nbrs)
    observed=(len(nodes),sum(map(len,nbrs))//2,Counter(map(len,comps)))
    assert observed==expected[k],(k,observed)
    # The component graph of minimum dominating sets has the same components.
    mins=[s for s in minimal if s.bit_count()<=k]
    links={s: [t for t in mins if s!=t and (s|t).bit_count()<=k] for s in mins}
    comps_min=component_sizes([[mins.index(t) for t in links[s]] for s in mins])
    assert len(comps_min)==len(comps)
    print('k',k,'V,E,components',observed,flush=True)
# Exhaustive all-sources shortest paths: finite certificate for component radii and diameters.
expected_ecc={5:(11,1,2),6:(1148,10,12),7:(3136,11,14),8:(5532,12,14)}
for k, (expected_size, expected_radius, expected_diameter) in expected_ecc.items():
    states, edges = graph(k)
    main = max(component_sizes(edges), key=len)
    assert len(main) == expected_size
    stamp = [0]*len(states)
    dist = [0]*len(states)
    radius,diameter = len(states)+1,0
    for run,source in enumerate(main,1):
        q=deque([source]); stamp[source]=run; dist[source]=0
        seen_count=0;ecc=0
        while q:
            v=q.popleft();seen_count+=1;ecc=max(ecc,dist[v])
            for w in edges[v]:
                if stamp[w]!=run:
                    stamp[w]=run;dist[w]=dist[v]+1;q.append(w)
        assert seen_count==expected_size
        radius=min(radius,ecc);diameter=max(diameter,ecc)
    assert (radius,diameter)==(expected_radius,expected_diameter), (k,radius,diameter)
    print('all-source distances',k,expected_size,'radius',radius,'diameter',diameter,flush=True)
print('VERIFY_OK full exhaustive classification',flush=True)
