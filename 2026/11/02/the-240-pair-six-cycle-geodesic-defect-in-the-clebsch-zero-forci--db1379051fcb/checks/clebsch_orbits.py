"""Symmetry-reduced exact certificate for the Clebsch minimum-zero-forcing exchange graph.
Uses the Cayley model on F_2^4, simultaneous closure, and the folded-cube group.
"""
from itertools import combinations, permutations
from collections import Counter, deque

N=16;FULL=(1<<N)-1
DIFFS=(1,2,4,8,15)
NB=tuple(sum(1<<(u^d) for d in DIFFS) for u in range(N))

def closure(B):
    while True:
        gained=0
        for v in range(N):
            if B>>v&1:
                W=NB[v]&~B
                if W and not (W&(W-1)):gained|=W
        if not gained:return B
        B|=gained

# Exhaust all 2^16 subsets and establish the minimum cardinality without sampling.
by_size=Counter();states=[]
for B in range(FULL+1):
    if closure(B)==FULL:
        k=B.bit_count()
        by_size[k]+=1
        if k==10:states.append(B)
assert len(states)==3872
assert min(by_size)==10
assert len(states)==len(set(states))
position={B:j for j,B in enumerate(states)}

# Group consists of all 16 translations and all 120 permutations of the five
# folded-cube coordinate directions. Its 1,920 maps preserve the Clebsch graph.
def coord_perm(v,p):
    out=0
    for j in range(4):
        if v>>j&1:out|=1<<p[j]
    if out>>4:return (out^31)&15
    return out
maps=set()
for p in permutations(range(5)):
    base=[coord_perm(v,p) for v in range(N)]
    for trans in range(N):maps.add(tuple(w^trans for w in base))
assert len(maps)==1920
for phi in maps:
    assert set(phi)==set(range(N))
    assert all({phi[u^d] for d in DIFFS}=={phi[u]^d for d in DIFFS} for u in range(N))

def img(B,phi):
    ans=0
    for v in range(N):
        if B>>v&1:ans|=1<<phi[v]
    return ans

orbits=[];labels={}
for B in states:
    if B in labels:continue
    O={img(B,phi) for phi in maps}
    assert O.issubset(position)
    j=len(orbits)
    for x in O:
        assert x not in labels
        labels[x]=j
    orbits.append((B,len(O)))
assert len(labels)==len(states)
assert len(orbits)==7
assert sorted(k for _,k in orbits)==[192,320,480,480,480,960,960]

G=[]
for B in states:
    neighbors=[]
    for v in range(N):
        if B>>v&1:
            for w in range(N):
                if not (B>>w&1):
                    A=B^(1<<v)^(1<<w)
                    if A in position:neighbors.append(position[A])
    assert len(neighbors)==len(set(neighbors))
    G.append(neighbors)
assert sum(map(len,G))//2==64720
assert Counter(map(len,G))=={30:672,32:960,34:1440,37:800}

pairhist=Counter(); excess=Counter();ecc=Counter();exception_counts=Counter();exception_sources=[]
for j,(B,weight) in enumerate(orbits):
    dist=[-1]*len(states)
    dist[position[B]]=0
    q=deque([position[B]])
    while q:
        u=q.popleft()
        for v in G[u]:
            if dist[v]<0:
                dist[v]=dist[u]+1
                q.append(v)
    assert all(x>=0 for x in dist)
    ecc[max(dist)]+=weight
    bad=[]
    for i,A in enumerate(states):
        if A==B:continue
        d=dist[i]
        h=((B^A).bit_count())//2
        pairhist[d]+=weight
        excess[d-h]+=weight
        if d>h:
            assert d==h+1 and (d,h)==(3,2)
            bad.append(A)
    exception_counts[j]=len(bad)
    if bad:exception_sources.append((j,B,bad,weight))
assert ecc=={6:3872},ecc
assert {d:c//2 for d,c in pairhist.items()}=={1:64720,2:625440,3:2214640,4:2986160,5:1412976,6:190320}
assert {d:c//2 for d,c in excess.items()}=={0:7494016,1:240}
assert len(exception_sources)==1
j,B,bad,weight=exception_sources[0]
assert weight==480 and len(bad)==1 and labels[bad[0]]==j
# Symmetry transitivity forces every configuration in this 480-state orbit
# to have exactly one exceptional partner, and all other types none.
print('SYMMETRY_REDUCED_CLEBSCH_CERTIFICATE_PASS')
print('all_zero_forcing_cardinality_counts',dict(sorted(by_size.items())))
print('minimum=10 states=3872 orbit_sizes', [weight for _,weight in orbits])
print('degree_hist',{k:v for k,v in sorted(Counter(map(len,G)).items())})
print('pair_distance_hist',{k:v//2 for k,v in sorted(pairhist.items())})
print('distance_minus_Johnson_hist',{k:v//2 for k,v in sorted(excess.items())})
print('exceptional_pair_matching_vertices=480 exceptional_pairs=240 source_orbit',j)
print('exception_example_initial_black_mask',B,'terminal_black_mask',bad[0])

# Intrinsic seven-type characterization from the induced graph on six white vertices.
# The only degree sequences with two nonisomorphic realizations are distinguished
# by adjacency of the two degree-three vertices.
type_sizes=Counter()
for W in combinations(range(N),6):
    degree={v:sum(((v^u) in DIFFS) for u in W if u!=v) for v in W}
    seq=tuple(sorted(degree.values()))
    name={
      (1,1,2,2,2,4):'C4_with_two_leaves_on_same_vertex',
      (1,1,2,2,3,3):'C4_with_leaves_on_adjacent_vertices',
      (2,2,2,2,3,3):'theta_2_2_3',
      (1,1,1,1,2,4):'star4_one_edge_subdivided',
      (0,1,1,1,2,3):'subdivided_claw_and_isolate',
      (0,2,2,2,2,2):'C5_and_isolate',
      (0,0,1,1,2,2):'P4_and_two_isolates',
    }.get(seq)
    if name is not None and seq in ((1,1,2,2,3,3),(2,2,2,2,3,3)):
        a,b=(v for v in W if degree[v]==3)
        edge=(a^b) in DIFFS
        if edge!=(seq==(1,1,2,2,3,3)):name=None
    B=FULL^sum(1<<v for v in W)
    assert (name is not None)==(B in position)
    if name is not None:type_sizes[name]+=1
assert sorted(type_sizes.values())==[192,320,480,480,480,960,960]

# Complete structural description of the exceptional shortest-path detours.
from itertools import combinations as cmb
j,B,bad,weight=exception_sources[0]
seed=bad[0]
exception_pairs={tuple(sorted((img(B,phi),img(seed,phi)))) for phi in maps}
assert len(exception_pairs)==240

def neighbors_in(vertices,u):
    return [v for v in vertices if v!=u and (u^v) in DIFFS]

geometric_pairs=set()
number_eightsets=0
for U in cmb(range(N),8):
    degrees={u:len(neighbors_in(U,u)) for u in U}
    if sorted(degrees.values())!=[0,0,2,2,2,2,2,2]:continue
    isolated={u for u in U if degrees[u]==0}
    C=set(U)-isolated
    reached={next(iter(C))}
    frontier=list(reached)
    for u in frontier:
        for v in neighbors_in(C,u):
            if v not in reached:
                reached.add(v);frontier.append(v)
    if len(reached)!=6:continue
    number_eightsets+=1
    # The opposite pairs in the cycle are exactly its three pairs at distance three.
    for s,t in cmb(sorted(C),2):
        paths=[]
        for a in neighbors_in(C,s):
            bnext=[b for b in neighbors_in(C,a) if b!=s]
            assert len(bnext)==1
            b=bnext[0]
            if (b^t) in DIFFS:
                paths.append({s,a,b,t})
        if len(paths)!=2:continue
        W0=isolated|paths[0]
        W1=isolated|paths[1]
        S0=FULL^sum(1<<u for u in W0)
        S1=FULL^sum(1<<u for u in W1)
        assert S0 in position and S1 in position
        geometric_pairs.add(tuple(sorted((S0,S1))))
assert number_eightsets==80,number_eightsets
assert geometric_pairs==exception_pairs,(len(geometric_pairs),len(exception_pairs))
print('SEVEN_INDUCED_TYPES_AND_80_C6_PLUS_TWO_ISOLATES_PASS')
print('white_induced_types',dict(sorted(type_sizes.items())))
print('exceptional_pairs_80_c6_times_3_opposite_pairs',len(geometric_pairs))
