"""Exact Tutte--Coxeter matching-flip census via duads and synthemes.
Requires only Python 3 standard library. Run `python3 verify_duads.py`.
"""
from collections import Counter,deque
from itertools import combinations,permutations
from math import factorial

symbols=tuple(range(6))
duads=tuple(combinations(symbols,2))
duad_id={frozenset(e):i for i,e in enumerate(duads)}
def perfect_partitions(S):
    if not S:
        yield ()
        return
    a,*tail=S
    for b in tail:
        for R in perfect_partitions([x for x in tail if x!=b]):
            yield ((a,b),)+R
synthemes=tuple(perfect_partitions(list(symbols)))
syn_id={frozenset(map(frozenset,s)):i for i,s in enumerate(synthemes)}
assert len(duads)==len(synthemes)==15
incidence=tuple(tuple(i for i,s in enumerate(synthemes) if e in s) for e in duads)
assert all(len(neigh)==3 for neigh in incidence)
# One vertex for each incidence-preserving bijection from duads to synthemes.
states=[]
def assign(i,used,prefix):
    if i==15:
        states.append(tuple(prefix));return
    for j in incidence[i]:
        if not used>>j&1:
            assign(i+1,used|(1<<j),prefix+[j])
assign(0,0,[])
states=tuple(states)
assert len(states)==288 and len(set(states))==288
# The graph has no 4-cycles: no two synthemes share two duads.
assert all(len(set(s)&set(t))<=1 for s,t in combinations(synthemes,2))
# If two incidence-preserving bijections differ at exactly 4 duads,
# their symmetric difference is an alternating 8-cycle; a union of
# two alternating 4-cycles is impossible by the preceding check.
G=[set() for _ in states]
for a,s in enumerate(states):
    for b in range(a+1,len(states)):
        if sum(s[i]!=states[b][i] for i in range(15))==4:
            G[a].add(b);G[b].add(a)
assert all(len(n)==10 for n in G)
assert sum(map(len,G))//2==1440

def sign(s):
    return sum(s[i]>s[j] for i in range(15) for j in range(i+1,15))%2
assert Counter(map(sign,states))=={0:144,1:144}
assert all(sign(states[a])!=sign(states[b]) for a in range(len(G)) for b in G[a])
# Construct orbit action of the five adjacent transpositions of S6,
# and exhaust every orbit by closure under the generators.
index={s:i for i,s in enumerate(states)}
acts=[]
for swap in range(5):
    sigma=list(range(6));sigma[swap],sigma[swap+1]=sigma[swap+1],sigma[swap]
    dmap=[duad_id[frozenset((sigma[u],sigma[v]))] for u,v in duads]
    smap=[syn_id[frozenset(frozenset((sigma[u],sigma[v])) for u,v in s)] for s in synthemes]
    images=[]
    for state in states:
        dest=[None]*15
        for i,j in enumerate(state):dest[dmap[i]]=smap[j]
        images.append(index[tuple(dest)])
    acts.append(images)
seen=set();orbits=[]
for s in range(len(states)):
    if s in seen:continue
    orb={s};q=[s]
    for x in q:
        for action in acts:
            y=action[x]
            if y not in orb:orb.add(y);q.append(y)
    assert orb.isdisjoint(seen)
    seen.update(orb);orbits.append(orb)
assert sorted(map(len,orbits))==[144,144]
assert all(len(set(sign(states[i]) for i in orb))==1 for orb in orbits)
# All-source BFS establishes connectivity, radius, diameter, and exact spheres.
profiles=Counter();byparity={0:Counter(),1:Counter()}
for source in range(len(states)):
    distances={source:0};q=deque([source])
    while q:
        u=q.popleft()
        for v in G[u]:
            if v not in distances:distances[v]=distances[u]+1;q.append(v)
    assert len(distances)==len(states)
    counts=Counter(distances.values())
    profile=tuple(counts[d] for d in range(max(distances.values())+1))
    profiles[profile]+=1
    byparity[sign(states[source])][profile]+=1
A=(1,10,45,97,96,37,2)
B=(1,10,42,97,101,37)
assert profiles=={A:144,B:144}
assert byparity[0]=={A:144} and byparity[1]=={B:144}
# G is bipartite, hence triangle-free. Count all four-cycles exactly.
squares=sum(len(G[i]&G[j])*(len(G[i]&G[j])-1)//2
            for i in range(len(G)) for j in range(i+1,len(G)))//2
assert squares==4320
print('DUAD_MATCHING_CENSUS_PASS states=288 flips=1440 degree=10')
print('DUAD_SYMMETRY_PASS orbits=144,144 parity_even_ecc=6 parity_odd_ecc=5')
print('DUAD_METRIC_PASS connected=1 radius=5 diameter=6 squares=4320')
print('DUAD_SPHERE_PROFILES_PASS',repr(dict(profiles)))
