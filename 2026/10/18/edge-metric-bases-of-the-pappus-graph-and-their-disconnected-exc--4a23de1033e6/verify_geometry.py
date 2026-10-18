"""Independent coordinate-algebra verification for minimum edge resolvers.
Does not compute graph distances by BFS: uses explicit point-line distance formulae
in AG(2,3) with the vertical parallel class removed.
Usage: python verify_geometry.py [certificate.json]
"""
import collections
import hashlib
import itertools
import json
import sys

F = range(3)
points = [(x,y) for x in F for y in F]
lines = [(m,b) for m in F for b in F]
labels = list(range(18))
P = lambda i:points[i]
L = lambda i:lines[i-9]
incident = lambda p,l: (p[1]-l[0]*p[0]-l[1])%3==0
inverses = {1:1,2:2}
incidences = sorted((p,9+l) for p in range(9) for l in range(9)
                    if incident(P(p), lines[l]))
assert len(incidences)==27

def algebraic_edge_distance(s, e):
    p,l=e
    x,y=P(p)
    m,b=L(l)
    if s < 9:
        xx,yy=P(s)
        if s==p:return 0
        if incident((xx,yy),(m,b)):return 1
        if xx!=x:return 2
        return 3
    mm,bb=L(s)
    if s==l:return 0
    if incident((x,y),(mm,bb)):return 1
    if mm!=m:return 2
    return 3

profiles=[[algebraic_edge_distance(v,e) for e in incidences] for v in labels]
def resolver(S):
    codes={tuple(profiles[v][j] for v in S) for j in range(27)}
    return len(codes)==27

counts={k:sum(resolver(S) for S in itertools.combinations(labels,k)) for k in range(4)}
assert counts=={0:0,1:0,2:0,3:0}

def intersect_lines(a,b):
    m,c=L(a)
    n,d=L(b)
    assert m!=n
    x=((d-c)*inverses[(m-n)%3])%3
    return (x,(m*x+c)%3)

def joined_line(a,b):
    x,y=P(a)
    u,v=P(b)
    assert x!=u
    m=((v-y)*inverses[(u-x)%3])%3
    return (m,(y-m*x)%3)

def geometric_basis(S):
    pp=[v for v in S if v<9]
    ll=[v for v in S if v>=9]
    if len(pp)==4:
        occupancy=sorted(collections.Counter(P(v)[0] for v in pp).values())
        return occupancy==[2,2]
    if len(ll)==4:
        occupancy=sorted(collections.Counter(L(v)[0] for v in ll).values())
        return occupancy==[2,2]
    if len(pp)!=2 or len(ll)!=2:return False
    a,b=pp;c,d=ll
    if P(a)[0]==P(b)[0] or L(c)[0]==L(d)[0]:return False
    x,y=intersect_lines(c,d)
    m,k=joined_line(a,b)
    return (y-m*x-k)%3 != 0

proposed=[tuple(S) for S in itertools.combinations(labels,4) if geometric_basis(S)]
actual=[tuple(S) for S in itertools.combinations(labels,4) if resolver(S)]
assert proposed==actual and len(actual)==540
part_hist=dict(sorted(collections.Counter(sum(v<9 for v in s) for s in actual).items()))
assert part_hist=={0:27,2:486,4:27}

# Make the exchange graph by indexing common triples, not by vertex-replacement loops.
index={S:i for i,S in enumerate(actual)}
groups=collections.defaultdict(list)
for i,S in enumerate(actual):
    for T in itertools.combinations(S,3):
        groups[T].append(i)
links=set()
for group in groups.values():
    for a,b in itertools.combinations(group,2):
        links.add((a,b) if a<b else (b,a))
links=sorted(links)
assert len(links)==3672
A=[set() for _ in actual]
for i,j in links:
    assert len(set(actual[i]) & set(actual[j]))==3
    A[i].add(j)
    A[j].add(i)

components=[]
remaining=set(range(540))
while remaining:
    s=min(remaining)
    active={s}
    remaining.remove(s)
    while True:
        neighbors=set().union(*(A[x] for x in active)) if active else set()
        additional=(neighbors & remaining)
        if not additional: break
        active |= additional
        remaining-=additional
    components.append(active)
components=sorted(components,key=lambda c:(-len(c),min(c)))
assert sorted(map(len,components))==[9]*6+[486]

# Bit-parallel breadth-first shells; a separate shortest-path implementation.
bitneighbors=[]
for neighbors in A:
    bitneighbors.append(sum(1<<j for j in neighbors))
ecc=collections.defaultdict(collections.Counter)
for comp in components:
    for source in comp:
        seen=1<<source
        shell=seen
        radius=0
        while True:
            reach=0
            for i in range(540):
                if shell>>i&1:reach |= bitneighbors[i]
            shell=reach & ~seen
            if not shell:break
            seen|=shell
            radius+=1
        assert seen.bit_count()==len(comp)
        ecc[len(comp)][radius]+=1
assert dict(ecc[486])=={5:486} and dict(ecc[9])=={2:54}

# Each small component is the rook graph K_3 square K_3, and corresponds to
# fixed pair of parallel classes and free two-of-three choices within each class.
for comp in components[1:]:
    assert len(comp)==9 and len({sum(v<9 for v in actual[i]) for i in comp})==1
    assert {len(A[i]) for i in comp}=={4}
    S=actual[min(comp)]
    if all(v<9 for v in S):classes=[P(v)[0] for v in S]
    else:classes=[L(v)[0] for v in S]
    assert len(set(classes))==2
    # Connectivity + Hamming adjacency of the 3x3 two-of-three choices gives K3 □ K3.

# Any original graph edge joins point to line, so a one-edge slide changes
# the number of selected points by +/-1; all four-point bases have even count.
assert all(sum(v<9 for v in S)%2==0 for S in actual)
certificate={'vertex_order':labels,'incidences':[list(x) for x in incidences],
             'bases':[list(s) for s in actual],
             'token_jump_edges':[list(x) for x in links]}
if len(sys.argv)>1:
    with open(sys.argv[1],encoding='utf-8') as f:
        assert json.load(f)==certificate
bhash=hashlib.sha256(json.dumps(certificate['bases'],separators=(',',':')).encode()).hexdigest()
ehash=hashlib.sha256(json.dumps(certificate['token_jump_edges'],separators=(',',':')).encode()).hexdigest()
result={'method':'finite-field closed-form distances and triple-indexed exchange graph',
        'edge_metric_dimension':4,'basis_count':len(actual),'counts_below_four':counts,
        'point_landmark_histogram':part_hist,
        'geometric_characterization_matches_all_four_subsets':True,
        'jump_edges':len(links),'jump_components':[len(c) for c in components],
        'component_eccentricities':{str(k):dict(v) for k,v in ecc.items()},
        'token_slide_edges':0,'basis_sha256':bhash,'jump_edge_sha256':ehash,
        'certificate_checked':len(sys.argv)>1}
print(json.dumps(result,indent=2,sort_keys=True))
