"""Exact finite certificate for the Clebsch perfect-matching flip graph.

Usage: python3 verify.py
Every vertex is an integer 0..15, interpreted as a vector in F_2^4.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import permutations

N=16
DIRECTIONS=(1,2,4,8,15)
E={tuple(sorted((v,v^s))) for v in range(N) for s in DIRECTIONS}
assert len(E)==40
adj={v:{v^s for s in DIRECTIONS} for v in range(N)}
assert all(len(adj[v])==5 for v in range(N))
for a in range(N):
    for b in range(a+1,N):
        assert len(adj[a]&adj[b])==(0 if b in adj[a] else 2)

# Complete matching enumeration by covering the smallest uncovered vertex.
matchings=[]
def enumerate_matchings(uncovered, pairs):
    if not uncovered:
        matchings.append(tuple(sorted(pairs)))
        return
    a=min(uncovered)
    for b in sorted(adj[a]&uncovered):
        enumerate_matchings(uncovered-{a,b}, pairs+((a,b),))
enumerate_matchings(frozenset(range(N)), ())
matchings=sorted(set(matchings))
assert len(matchings)==705

# Independent subset recurrence, without any use of the enumeration above.
@lru_cache(None)
def count_completions(bits):
    if bits==0:return 1
    low=bits & -bits
    u=low.bit_length()-1
    remainder=bits^low
    return sum(count_completions(remainder^(1<<v)) for v in range(N)
               if (remainder>>v)&1 and (u^v) in DIRECTIONS)
assert count_completions((1<<N)-1)==705

id_of={m:i for i,m in enumerate(matchings)}
flip_neigh=[set() for _ in matchings]
for i,m in enumerate(matchings):
    for p in range(8):
        a,b=m[p]
        for q in range(p+1,8):
            c,d=m[q]
            for alternative in (((a,c),(b,d)),((a,d),(b,c))):
                proposed=tuple(sorted(tuple(sorted(e)) for e in alternative))
                if proposed[0] in E and proposed[1] in E:
                    m2=tuple(sorted(m[:p]+m[p+1:q]+m[q+1:]+proposed))
                    flip_neigh[i].add(id_of[m2])
assert all(i not in flip_neigh[i] for i in range(705))
assert all(i in flip_neigh[j] for i,near in enumerate(flip_neigh) for j in near)

# Independent all-pairs symmetric-difference adjacency certificate.
sets=[frozenset(m) for m in matchings]
for i in range(len(sets)):
    for j in range(i+1,len(sets)):
        assert ((j in flip_neigh[i]) == (len(sets[i]^sets[j])==4))

deg=Counter(map(len,flip_neigh))
assert deg==Counter({4:200,6:360,8:60,10:80,16:5}),deg
assert sum(map(len,flip_neigh))//2==2160
assert sum(len(flip_neigh[i]&flip_neigh[j]) for i in range(705)
           for j in flip_neigh[i] if j>i)==0

# All-pairs BFS is a proof of complete shortest-path metrics, not a sampled test.
eccentricities=[]
distance_hist=Counter()
for root in range(705):
    d={root:0}
    queue=deque([root])
    while queue:
        u=queue.popleft()
        for v in flip_neigh[u]:
            if v not in d:
                d[v]=d[u]+1
                queue.append(v)
    assert len(d)==705
    eccentricities.append(max(d.values()))
    for j,dij in d.items():
        if root<j:distance_hist[dij]+=1
assert Counter(eccentricities)==Counter({7:5,8:700})
assert distance_hist==Counter({1:2160,2:8040,3:22360,4:45160,
                              5:64800,6:61920,7:34880,8:8840}),distance_hist
assert sum(distance_hist.values())==705*704//2

# Explicit full automorphism group: 2^4:S_5, where the fifth generator
# is the sum of the first four. Any four generators form an F_2 basis.
linear_maps=[]
for ordered_basis in permutations(DIRECTIONS,4):
    mapping=[0]*N
    for x in range(1,N):
        low=x & -x
        r=low.bit_length()-1
        mapping[x]=mapping[x^low]^ordered_basis[r]
    assert {mapping[s] for s in DIRECTIONS}==set(DIRECTIONS)
    linear_maps.append(tuple(mapping))
assert len(set(linear_maps))==120

remaining=set(matchings)
orbit_info=[]
while remaining:
    representative=min(remaining)
    orbit={tuple(sorted(tuple(sorted((linear[a]^t,linear[b]^t)))
                        for a,b in representative))
           for linear in linear_maps for t in range(N)}
    assert orbit<=remaining
    remaining-=orbit
    rep_index=id_of[representative]
    orbit_info.append((len(orbit),len(flip_neigh[rep_index]),
                       eccentricities[rep_index],representative))
assert sorted((size,degree,ecc) for size,degree,ecc,_ in orbit_info)==[
    (5,16,7),(40,4,8),(60,8,8),(80,10,8),
    (120,6,8),(160,4,8),(240,6,8)]

# Exhaustive direction patterns in every automorphism orbit, not just orbit sizes.
expected_patterns=sorted([
    (5,(8,),16,7), (80,(6,2),10,8), (60,(4,4),8,8),
    (120,(4,2,2),6,8), (240,(4,2,2),6,8),
    (160,(2,2,2,2),4,8), (40,(2,2,2,2),4,8)])
actual_patterns=sorted((size,tuple(sorted(Counter(a^b for a,b in rep).values(),reverse=True)),degree,ecc)
                       for size,degree,ecc,rep in orbit_info)
assert actual_patterns==expected_patterns,actual_patterns

parallel_matchings={tuple(sorted(tuple(sorted((x,x^s))) for x in range(N)
                                 if x < (x^s))) for s in DIRECTIONS}
centers={m for i,m in enumerate(matchings) if eccentricities[i]==7}
assert centers==parallel_matchings
print('GRAPH_OK vertices=16 edges=40 parameters=(16,5,0,2)')
print('MATCHINGS_OK enumerated=705 independent_recurrence=705')
print('FLIPS_OK edges=2160 degree_counts='+str(sorted(deg.items())))
print('METRIC_OK connected=1 radius=7 diameter=8 antipodal_pairs=8840')
print('DISTANCES_OK '+str(sorted(distance_hist.items())))
print('ORBITS_OK automorphisms=1920 seven_orbits='+str(sorted((x[:3] for x in orbit_info))))
print('CENTERS_OK exactly_five_parallel_matchings')
print('ALL_VERIFY_OK')
