"""Independent S6-orbit and forcing-sequence certification for KG(6,2)."""
from itertools import combinations,permutations
from collections import Counter

V=list(combinations(range(6),2))
edge_index={pair:i for i,pair in enumerate(V)}
N=15;U=(1<<N)-1
nbh=[tuple(j for j,b in enumerate(V) if a[0] not in b and a[1] not in b) for a in V]

# Non-greedy recursive forcing: a seed succeeds if some sequence of legal
# individual forces fills all vertices. Memoization ensures finite exhaustion.
cache={U:True}
def forceable(colored):
    if colored in cache:return cache[colored]
    future=set()
    for v in range(N):
        if colored&(1<<v):
            white=[w for w in nbh[v] if not colored&(1<<w)]
            if len(white)==1:
                future.add(white[0])
    cache[colored]=any(forceable(colored|(1<<v)) for v in future)
    return cache[colored]

# Build all unlabeled 5-edge patterns as full S6 vertex relabeling orbits.
perms=[]
for p in permutations(range(6)):
    perms.append(tuple(edge_index[tuple(sorted((p[i],p[j])))] for i,j in V))
remaining={sum(1<<i for i in ix) for ix in combinations(range(N),5)}
rows=[];accepted=set();rep_and_orbit=[]
while remaining:
    rep=min(remaining)
    ix=[i for i in range(N) if rep>>i&1]
    orb={sum(1<<p[i] for i in ix) for p in perms}
    assert orb<=remaining
    remaining-=orb
    good=forceable(U^rep)
    deg=[0]*6
    for i in ix:
        u,v=V[i];deg[u]+=1;deg[v]+=1
    key=(len(orb),tuple(sorted(deg,reverse=True)),good)
    rows.append(key)
    if good:accepted|=orb;rep_and_orbit.append((rep,len(orb)))
assert len(rows)==15 and len(accepted)==1662
assert sorted(length for rep,length in rep_and_orbit)==[60,72,90,360,360,360,360]
assert sum(1 for r in rows if r[2])==7
assert not any(forceable(U^m) for m in [sum(1<<i for i in ix) for ix in combinations(range(N),6)])

# Exchange adjacency on complements.  Use S6 orbit representatives to
# prove all 1662 eccentricities and the full pairwise distance profile.
links={}
for a in accepted:
    around=[]
    for i in range(N):
        if a&(1<<i):
            for j in range(N):
                if not a&(1<<j):
                    b=a^(1<<i)^(1<<j)
                    if b in accepted:
                        around.append(b)
    links[a]=around
assert sum(len(s) for s in links.values())//2==24270

degree_counter=Counter();ecc_counter=Counter();distance_counter=Counter()
for rep,orbit_size in rep_and_orbit:
    degree_counter[len(links[rep])]+=orbit_size
    dist={rep:0};queue=[rep]
    for x in queue:
        for y in links[x]:
            if y not in dist:
                dist[y]=dist[x]+1;queue.append(y)
    assert len(queue)==1662
    eccentricity=max(dist.values());ecc_counter[eccentricity]+=orbit_size
    for d in dist.values():
        if d:distance_counter[d]+=orbit_size
assert ecc_counter=={5:1662}
assert degree_counter=={26:450,30:432,32:420,29:360},degree_counter
assert all(n%2==0 for n in distance_counter.values())
distance_counter={str(d):v//2 for d,v in sorted(distance_counter.items())}
assert sum(distance_counter.values())==1662*1661//2
print('ORBIT_PASS',{'unlabeled_patterns':15,'accepted_orbits':7,'orbit_sizes':sorted(z for _,z in rep_and_orbit),'minimum_sets':1662,'edges':24270,'degree_histogram':dict(sorted(degree_counter.items())),'eccentricities':dict(ecc_counter),'distance_histogram':distance_counter})
