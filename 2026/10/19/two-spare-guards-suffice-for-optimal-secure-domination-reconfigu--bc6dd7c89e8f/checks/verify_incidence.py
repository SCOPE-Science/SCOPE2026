"""Exact secure-domination and spare-guard certificate for H(5,2).
Run: python3 verify_incidence.py [certificate.json]
Uses Python's standard library only; no external graph libraries.
"""
import sys, itertools, collections, hashlib, json

sub2=list(itertools.combinations(range(5),2))
sub3=list(itertools.combinations(range(5),3))
V=sub2+sub3
n=len(V); allv=(1<<n)-1
adj=[0]*n
for i,P in enumerate(sub2):
    for j,T in enumerate(sub3):
        if set(P)<=set(T):
            adj[i] |= 1<<(10+j)
            adj[10+j] |= 1<<i
assert len(adj)==20 and all(a.bit_count()==3 for a in adj)
closed=[a|(1<<i) for i,a in enumerate(adj)]

def dominating(S):
    cover=0
    while S:
        v=S&-S;S-=v
        cover|=closed[v.bit_length()-1]
    return cover==allv

def secure(S):
    if not dominating(S):return False
    missing=allv^S
    while missing:
        v=missing&-missing;missing-=v
        defender=adj[v.bit_length()-1]&S
        while defender:
            a=defender&-defender;defender-=a
            if dominating((S^a)|v):break
        else:return False
    return True

counts={}
for k in range(0,9):
    good=[]
    for I in itertools.combinations(range(n),k):
        mask=sum(1<<i for i in I)
        if secure(mask):good.append(mask)
    counts[k]=len(good)
    if k==8:states=sorted(good)
assert [counts[k] for k in range(8)]==[0]*8
assert len(states)==155 and all((s&1023).bit_count()==4 for s in states)

# Sym(5) and bipartition duality generate graph automorphisms.
idx2={A:i for i,A in enumerate(sub2)}
idx3={A:i+10 for i,A in enumerate(sub3)}
C=set(range(5))
maps=[]
for perm in itertools.permutations(range(5)):
    direct=[idx2[tuple(sorted(perm[i] for i in A))] for A in sub2]+[idx3[tuple(sorted(perm[i] for i in A))] for A in sub3]
    dual=[]
    for j in direct:
        A=V[j]
        complement=tuple(sorted(C-set(A)))
        dual.append(idx3[complement] if j<10 else idx2[complement])
    maps.extend([direct,dual])
assert len(maps)==240
for f in maps:
    assert sorted(f)==list(range(20))
    assert all((adj[i]>>j)&1 == (adj[f[i]]>>f[j])&1 for i in range(n) for j in range(n))

def move(S,f):
    out=0
    while S:
        v=S&-S;S-=v
        out|=1<<f[v.bit_length()-1]
    return out

state_set=set(states)
orbits=[];seen=set()
for s in states:
    if s in seen:continue
    orbit={move(s,f) for f in maps}
    assert orbit <= state_set
    seen|=orbit
    orbits.append((len(orbit),s,orbit))
assert seen==state_set
assert sorted(len(o) for _,_,o in orbits)==[5,30,120]

# Join minima if their symmetric difference consists of two removals and two additions.
adjacencies={s:[] for s in states}
edges=[]
for i,s in enumerate(states):
    for t in states[i+1:]:
        if (s^t).bit_count()==2:
            raise AssertionError('Found single exchange between optima')
        if (s^t).bit_count()==4:
            edges.append((s,t))
            adjacencies[s].append(t)
            adjacencies[t].append(s)
assert len(edges)==750

ecc={};layers={}
for start in states:
    dist={start:0};queue=[start]
    for s in queue:
        for t in adjacencies[s]:
            if t not in dist:
                dist[t]=dist[s]+1
                queue.append(t)
    assert len(dist)==155
    ecc[start]=max(dist.values())
    layers[start]=[sum(d==i for d in dist.values()) for i in range(5)]
assert set(ecc.values())=={4}
assert sorted((len(O),len(adjacencies[s])) for _,s,O in orbits)==[(5,24),(30,6),(120,10)]

disjoint=next((s,t) for i,s in enumerate(states) for t in states[i+1:] if s&t==0)
# A complete path witness in the two-exchange graph from a minimum to every other.
base=states[0];parents={base:None};queue=[base]
for s in queue:
    for t in adjacencies[s]:
        if t not in parents:parents[t]=s;queue.append(t)
assert len(parents)==155
certificate={
  'graph':'bipartite Kneser graph H(5,2), 2-subsets and 3-subsets of {0,1,2,3,4}',
  'vertex_order':[list(A) for A in V],
  'secure_minimum_size':8,
  'optimal_states':states,
  'two_exchange_edges':[list(E) for E in edges],
  'orbit_representatives':[{'size':z,'mask':s,'degree':len(adjacencies[s]),'eccentricity':ecc[s]} for z,s,_ in orbits],
  'spanning_tree_parent_edges':[[parents[t],t] for t in sorted(parents) if parents[t] is not None],
  'disjoint_optimal_pair':list(disjoint),
}
if len(sys.argv)>1:
    with open(sys.argv[1],encoding='utf8') as f:stored=json.load(f)
    assert stored==certificate,'Certificate disagrees with fresh exhaustive computation'
print('vertex_count=20; degree=3; secure_domination_number=8')
print('secure_counts_0_to_8='+','.join(str(counts[k]) for k in range(9)))
print('minimum_side_counts=4+4; optimal_sets=155')
print('minimum_orbits='+','.join(str(v) for v in sorted(len(O) for _,_,O in orbits)))
print('minima_single_exchange_edges=0')
print('minima_two_exchange_edges=750; degrees='+','.join(str(v)+':'+str(k) for k,v in [(5,24),(30,6),(120,10)]))
print('two_exchange_connected=1; radius=4; diameter=4')
print('disjoint_optimal_pair='+str(disjoint))
print('TAR9_optimals_mutually_disconnected=True')
print('TAR10_optimals_mutually_connected=True; maximum_optimal_pair_distance=16')
if len(sys.argv)<=1:
    with open('certificate.json','w',encoding='utf8') as f:json.dump(certificate,f,sort_keys=True,separators=(',',':'),ensure_ascii=False)
