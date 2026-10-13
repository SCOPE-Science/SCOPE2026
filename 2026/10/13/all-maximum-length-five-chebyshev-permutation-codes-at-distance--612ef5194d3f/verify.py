#!/usr/bin/env python3
import itertools, json, os
from collections import Counter, defaultdict

N=5
PERMS=list(itertools.permutations(range(1,N+1)))
PID={p:i for i,p in enumerate(PERMS)}

def dist(p,q): return max(abs(a-b) for a,b in zip(p,q))
ADJ=[0]*len(PERMS)
EDGE_COUNT=0
for i,p in enumerate(PERMS):
    m=0
    for j,q in enumerate(PERMS):
        if i!=j and dist(p,q)>=3: m|=1<<j
    ADJ[i]=m
    EDGE_COUNT += m.bit_count()
EDGE_COUNT//=2

def k_cliques(k):
    out=[]
    def rec(chosen,cand):
        if len(chosen)==k:
            out.append(tuple(chosen)); return
        if len(chosen)+cand.bit_count()<k: return
        while cand:
            b=cand & -cand; cand ^= b
            v=b.bit_length()-1
            rec(chosen+[v], cand & ADJ[v])
    rec([], (1<<len(PERMS))-1)
    return out

# Direct upper bound certificate: for a code with distance >=3, the set of positions occupied by values 1 and 2 is injective.
def low_signature(p): return tuple(i for i,x in enumerate(p) if x<=2)
def high_signature(p): return tuple(i for i,x in enumerate(p) if x>=4)
assert len(set(low_signature(p) for p in PERMS))==10
# If signatures agree, distance is <=2.
for i,p in enumerate(PERMS):
    for q in PERMS[i+1:]:
        if low_signature(p)==low_signature(q): assert dist(p,q)<=2
        if high_signature(p)==high_signature(q): assert dist(p,q)<=2
MAXIMA=set(tuple(c) for c in k_cliques(10))
assert MAXIMA
assert len(MAXIMA)==192
for C in MAXIMA:
    assert len({low_signature(PERMS[i]) for i in C})==10
    assert len({high_signature(PERMS[i]) for i in C})==10

# Petersen-supported bijections L -> H, where L,H are 2-subsets and disjoint.
EDGES=list(itertools.combinations(range(N),2)); EID={e:i for i,e in enumerate(EDGES)}
DISJ=[[j for j,h in enumerate(EDGES) if set(e).isdisjoint(h)] for e in EDGES]
MATCHINGS=[]
def enum_maps(i,used,f):
    if i==10:
        MATCHINGS.append(tuple(f)); return
    for j in DISJ[i]:
        if not (used>>j)&1:
            f.append(j); enum_maps(i+1,used|(1<<j),f); f.pop()
enum_maps(0,0,[])
assert len(MATCHINGS)==60

def cyc_type(f):
    seen=set(); ls=[]
    for i in range(10):
        if i not in seen:
            j=i; n=0
            while j not in seen:
                seen.add(j); n+=1; j=f[j]
            ls.append(n)
    return tuple(sorted(ls))

def word_candidates(i,j):
    L=EDGES[i]; H=EDGES[j]
    assert set(L).isdisjoint(H)
    r=({0,1,2,3,4}-set(L)-set(H)).pop()
    out=[]
    for lo in (L,L[::-1]):
        for hi in (H,H[::-1]):
            p=[None]*5
            p[lo[0]]=1; p[lo[1]]=2; p[r]=3; p[hi[0]]=4; p[hi[1]]=5
            out.append(PID[tuple(p)])
    return tuple(sorted(out))

def codes_for_map(f):
    parts=[word_candidates(i,f[i]) for i in range(10)]
    # order parts by a static compatibility score to prune, while retaining one from each part
    order=sorted(range(10), key=lambda i: sum(sum(1 for w in parts[j] if (ADJ[v]>>w)&1) for j in range(10) if j!=i for v in parts[i]))
    sol=[]
    def rec(t,chosen):
        if t==10:
            sol.append(tuple(sorted(chosen))); return
        i=order[t]
        for v in parts[i]:
            if all((ADJ[v]>>u)&1 for u in chosen): rec(t+1,chosen+[v])
    rec(0,[])
    return set(sol)

STRUCT=set(); map_counts=Counter(); cycle_counts=Counter(); map_orientation_counts=defaultdict(list)
for f in MATCHINGS:
    cs=codes_for_map(f)
    ct=cyc_type(f)
    cycle_counts[ct]+=1
    map_orientation_counts[ct].append(len(cs))
    map_counts[len(cs)]+=1
    STRUCT |= cs
assert STRUCT==MAXIMA
assert cycle_counts==Counter({(2,8):30,(5,5):24,(2,2,2,2,2):6})
assert set(map_orientation_counts[(2,8)])=={4}
assert set(map_orientation_counts[(5,5)])=={2}
assert set(map_orientation_counts[(2,2,2,2,2)])=={4}

# Natural isometry group: coordinate permutations and global value reflection.
COORDS=list(itertools.permutations(range(5)))
def transform_idx(idx,rho,reflect):
    p=PERMS[idx]; q=tuple((6-p[rho[j]]) if reflect else p[rho[j]] for j in range(5)); return PID[q]
def transform_code(C,rho,reflect): return tuple(sorted(transform_idx(i,rho,reflect) for i in C))
unseen=set(MAXIMA); orbits=[]
while unseen:
    C=min(unseen)
    O={transform_code(C,rho,r) for rho in COORDS for r in (False,True)}
    assert O <= MAXIMA
    orbits.append(O); unseen-=O
orbits.sort(key=lambda O:(len(O), min(O)))
assert [len(o) for o in orbits]==[24,48,120]

def profile(C):
    c=Counter(dist(PERMS[a],PERMS[b]) for a,b in itertools.combinations(C,2)); return (c[3],c[4])
profiles=[profile(min(O)) for O in orbits]
assert profiles==[(30,15),(25,20),(28,17)]
assert [240//len(O) for O in orbits]==[10,5,2]

# Every maximum is position-symbol balanced: each symbol occurs twice in each position.
for C in MAXIMA:
    for pos in range(5):
        cnt=Counter(PERMS[i][pos] for i in C)
        assert cnt==Counter({1:2,2:2,3:2,4:2,5:2})

# Map cycle type of each code and check it is constant on the three code orbits.
def map_of_code(C):
    f=[None]*10
    for idx in C:
        p=PERMS[idx]; f[EID[low_signature(p)]]=EID[high_signature(p)]
    return tuple(f)
orb_ct=[]
for O in orbits:
    s={cyc_type(map_of_code(C)) for C in O}
    assert len(s)==1; orb_ct.append(next(iter(s)))
assert orb_ct==[(2,2,2,2,2),(5,5),(2,8)]

def fmtperm(p): return ''.join(map(str,p))
reps=[[fmtperm(PERMS[i]) for i in min(O)] for O in orbits]

census={
  "schema_version":1,
  "metric":"Chebyshev distance on S_5",
  "minimum_distance":3,
  "maximum_size":10,
  "labeled_maxima":192,
  "petersen_supported_bijections":60,
  "matching_cycle_types":{"2+2+2+2+2":6,"5+5":24,"2+8":30},
  "admissible_orientations_per_matching":{"2+2+2+2+2":4,"5+5":2,"2+8":4},
  "natural_isometry_group_size":240,
  "orbit_sizes":[24,48,120],
  "stabilizer_orders":[10,5,2],
  "distance_profiles":[{"orbit_size":24,"d3_pairs":30,"d4_pairs":15},{"orbit_size":48,"d3_pairs":25,"d4_pairs":20},{"orbit_size":120,"d3_pairs":28,"d4_pairs":17}],
  "matching_cycle_type_by_orbit":["2+2+2+2+2","5+5","2+8"],
  "representatives":reps,
  "all_maximum_codes":[[fmtperm(PERMS[i]) for i in C] for C in sorted(MAXIMA)]
}
if os.path.exists(os.path.join(os.path.dirname(__file__),"census.json")):
    with open(os.path.join(os.path.dirname(__file__),"census.json"),encoding="utf-8") as f: stored=json.load(f)
    assert stored==census
else:
    with open(os.path.join(os.path.dirname(__file__),"census.json"),"w",encoding="utf-8") as f: json.dump(census,f,sort_keys=True,separators=(",",":")); f.write("\n")
print("VERIFY_OK perms=120 compatibility_edges=%d maximum=10 labeled_maxima=192 petersen_maps=60 cycle_types=2^5:6,5^2:24,2+8:30 orientation_counts=4,2,4 natural_group=240 orbits=24,48,120 stabilizers=10,5,2 profiles=30/15,25/20,28/17 balanced=true"%EDGE_COUNT)
