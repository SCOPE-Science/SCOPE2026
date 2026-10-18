"""Exact finite verification of Coxeter graph independence homology and automorphism character.
Python 3.10+ and networkx 3.x. Run: python verify_coxeter.py
"""
import itertools
from collections import Counter, deque
from functools import lru_cache
import networkx as nx

LINES = frozenset(frozenset(((j) % 7, (j+1) % 7, (j+3) % 7)) for j in range(7))
VERTICES = tuple(t for t in itertools.combinations(range(7),3) if frozenset(t) not in LINES)
assert len(VERTICES)==28
INDEX = {v:i for i,v in enumerate(VERTICES)}
ADJ = tuple(sum(1<<j for j,b in enumerate(VERTICES) if i!=j and not set(a).intersection(b)) for i,a in enumerate(VERTICES))
G=nx.Graph()
G.add_nodes_from(range(28))
G.add_edges_from((i,j) for i in range(28) for j in range(i+1,28) if (ADJ[i]>>j)&1)
assert G.number_of_edges()==42 and all(G.degree(v)==3 for v in range(28))

# Include the augmented (-1)-simplex for reduced homology.
FACES=[]
def visit(i,chosen,forbidden):
    if i==28:
        FACES.append(chosen)
        return
    visit(i+1,chosen,forbidden)
    if not (forbidden>>i)&1:
        visit(i+1,chosen | (1<<i),forbidden | ADJ[i])
visit(0,0,0)
assert len(FACES)==196009 and len(set(FACES))==len(FACES)

@lru_cache(maxsize=None)
def boundary(f):
    return tuple((f^(1<<i), 1 if j%2==0 else -1)
                 for j,i in enumerate(k for k in range(28) if (f>>k)&1))

# Lexicographic elementary matching in the augmented simplicial face poset.
UNMATCHED=set(FACES)
LOWER_UPPER={}
UPPER_LOWER={}
for v in range(28):
    bit=1<<v
    for f in list(UNMATCHED):
        if f & bit or (f|bit) not in UNMATCHED:
            continue
        up=f|bit
        UNMATCHED.remove(f)
        UNMATCHED.remove(up)
        LOWER_UPPER[f]=up
        UPPER_LOWER[up]=f
assert len(LOWER_UPPER)==97999
assert Counter(f.bit_count()-1 for f in UNMATCHED)=={6:8,7:2,8:1}

# Check the entire oriented Hasse graph of the matching is acyclic:
# lower -> upper for matched incidence, upper -> lower otherwise.
INDEG={f:0 for f in FACES}
for upper in FACES:
    for lower,_ in boundary(upper):
        if LOWER_UPPER.get(lower)==upper:
            INDEG[upper]+=1
        else:
            INDEG[lower]+=1
queue=deque(f for f in FACES if INDEG[f]==0)
processed=0
while queue:
    f=queue.popleft(); processed+=1
    if f in LOWER_UPPER:
        hi=LOWER_UPPER[f]
        INDEG[hi]-=1
        if not INDEG[hi]: queue.append(hi)
    for low,_ in boundary(f):
        if LOWER_UPPER.get(low)!=f:
            INDEG[low]-=1
            if not INDEG[low]: queue.append(low)
assert processed==len(FACES), (processed,len(FACES))

# Projection of each facet into its critical Morse basis by unit elimination.
@lru_cache(maxsize=None)
def project(f):
    if f in UNMATCHED:
        return {f:1}
    if f in UPPER_LOWER:
        return {}
    upper=LOWER_UPPER[f]
    coefficient=dict(boundary(upper))[f]
    accum={}
    for lower,sgn in boundary(upper):
        if lower==f: continue
        for critical, coefficient2 in project(lower).items():
            accum[critical]=accum.get(critical,0)-sgn*coefficient2*coefficient
    return {k:v for k,v in accum.items() if v}

def morse_boundary(f):
    ans={}
    for facet,sgn in boundary(f):
        for c,value in project(facet).items():
            ans[c]=ans.get(c,0)+sgn*value
    return {k:v for k,v in ans.items() if v}

C6=sorted(f for f in UNMATCHED if f.bit_count()==7)
C7=sorted(f for f in UNMATCHED if f.bit_count()==8)
C8=sorted(f for f in UNMATCHED if f.bit_count()==9)
D7=[morse_boundary(f) for f in C7]
D8=morse_boundary(C8[0])
assert len(D7)==2 and D7[0] and D7[1]
assert D7[0]=={c:-v for c,v in D7[1].items()}
assert set(D8.values())=={1} and set(D8)==set(C7)
# Thus rank d7 = rank d8 = 1 and d7*d8=0; only H_6=Q^7.

@lru_cache(maxsize=None)
def alt_independence(adj):
    @lru_cache(None)
    def f(rem):
        if not rem:return 1
        v=rem & -rem
        idx=v.bit_length()-1
        return f(rem^v)-f(rem & ~v & ~adj[idx])
    return f((1<<len(adj))-1)

def fixed_face_trace(perm):
    visited=set()
    cycles=[]
    for v in range(28):
        if v in visited: continue
        cyc=[]; w=v
        while w not in visited:
            visited.add(w);cyc.append(w);w=perm[w]
        assert w==v
        cycles.append(cyc)
    good=[]
    for cyc in cycles:
        m=sum(1<<v for v in cyc)
        if all((ADJ[v]&m)==0 for v in cyc):
            good.append(cyc)
    adj2=tuple(sum(1<<j for j,b in enumerate(good) if i!=j and
                   any((ADJ[x]>>y)&1 for x in a for y in b))
               for i,a in enumerate(good))
    # Reduced Lefschetz trace: minus the (-1)-independence polynomial of
    # compatible, whole vertex orbits; each selected orbit contributes -1.
    return -alt_independence(adj2)

def perm_order(p):
    seen=set();ans=1
    from math import lcm
    for v in range(len(p)):
        if v in seen: continue
        w=v;count=0
        while w not in seen:
            seen.add(w);count+=1;w=p[w]
        ans=lcm(ans,count)
    return ans

def direct_trace(p):
    ans=0
    for face in FACES:
        image=[p[v] for v in range(28) if face>>v&1]
        if sum(1<<k for k in image)!=face:continue
        inversions=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
        # reduced simplicial Lefschetz contribution including empty face
        ans-=(-1)**(len(image)+inversions)
    return ans

AUT=[]
COUNTS=Counter()
representatives={}
for m in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter():
    p=tuple(m[v] for v in range(28))
    t=fixed_face_trace(p)
    o=perm_order(p)
    COUNTS[o,t]+=1
    AUT.append((p,t))
    representatives.setdefault(o,p)
assert len(AUT)==336
expected={(1,7):1,(2,-1):49,(3,1):56,(4,-1):42,(6,-1):56,(7,0):48,(8,1):84}
assert COUNTS==expected, (COUNTS,expected)
assert sum(t*t for _,t in AUT)==336
assert sum(t for _,t in AUT)==0
for o,p in sorted(representatives.items()):
    assert direct_trace(p)==fixed_face_trace(p),o

# Independent 168-element Fano-plane collineation subgroup and restriction.
FANO_AUT=[]
for perm in itertools.permutations(range(7)):
    if {frozenset(perm[z] for z in l) for l in LINES} != set(LINES): continue
    p=tuple(INDEX[tuple(sorted(perm[z] for z in t))] for t in VERTICES)
    assert all((ADJ[i]>>j)&1 == ((ADJ[p[i]]>>p[j])&1) for i in range(28) for j in range(28))
    FANO_AUT.append(p)
assert len(FANO_AUT)==168
assert sum(fixed_face_trace(p)**2 for p in FANO_AUT)==168
assert sum(fixed_face_trace(p) for p in FANO_AUT)==0
print('PASS: graph (28,42), augmented faces 196009, acyclic matching',len(LOWER_UPPER),'pairs')
print('PASS: critical cells 8 in dimension 6, 2 in dimension 7, 1 in dimension 8')
print('PASS: Morse d7 and d8 both rank 1; reduced rational H6 has dimension 7, other groups vanish')
print('PASS: 336 automorphisms; (order,trace):count',sorted(COUNTS.items()))
print('PASS: independent direct Lefschetz calculation on 7 order representatives')
print('PASS: character inner product 1, no full-group invariants')
print('PASS: on 168 Fano collineations, character inner product 1 and no invariants')
