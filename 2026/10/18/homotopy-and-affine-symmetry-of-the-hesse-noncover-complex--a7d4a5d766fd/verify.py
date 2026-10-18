#!/usr/bin/env python3
"""Exact, standalone verification of the affine-plane noncover homotopy and rational characters.
Only Python's standard library is required; all arithmetic is integral.
"""
from itertools import product, combinations
from collections import defaultdict, deque
import hashlib, json

POINTS = list(product(range(3), repeat=2))
PINDEX = {p: i for i, p in enumerate(POINTS)}
UNIVERSE = set(range(9))
LINES = sorted({tuple(sorted(PINDEX[p] for p in POINTS
                      if (a*p[0] + b*p[1] - c) % 3 == 0))
                for a,b in product(range(3), repeat=2) if (a,b)!=(0,0)
                for c in range(3)})
assert len(LINES) == 12 and all(len(line)==3 for line in LINES)
FACETS = [tuple(sorted(UNIVERSE - set(line))) for line in LINES]
FACES = {d: sorted({t for facet in FACETS
                     for t in combinations(facet,d+1)}) for d in range(6)}
assert tuple(len(FACES[d]) for d in range(6)) == (9,36,84,126,72,12)
ALL = set(sum((FACES[d] for d in range(6)), []))
assert len(ALL)==339

# A sequential vertex-toggle matching. Each stage matches all still-unmatched
# simplices not containing v to their union with v whenever both remain.
# Cycles in the resulting Morse orientation are independently checked below.
ORDER = (2,6,7,3,5,1,4,0,8)
remaining = set(ALL)
pairs=[]
for v in ORDER:
    stage = [(f,tuple(sorted(f+(v,)))) for f in sorted(remaining)
             if v not in f and tuple(sorted(f+(v,))) in remaining]
    for low,high in stage:
        assert low in remaining and high in remaining
        remaining.remove(low)
        remaining.remove(high)
        pairs.append((low,high))
critical = {d: sorted(f for f in remaining if len(f)==d+1) for d in range(6)}
assert [len(critical[d]) for d in range(6)] == [1,0,0,11,1,0]
assert len(pairs)==163
# Orient ordinary face-poset covers high -> low, except matched covers low -> high.
matchset = set(pairs)
adj=defaultdict(list)
indeg={f:0 for f in ALL}
incidences=0
for d in range(1,6):
    for high in FACES[d]:
        for i in range(d+1):
            low = high[:i]+high[i+1:]
            incidences += 1
            a,b=(low,high) if (low,high) in matchset else (high,low)
            adj[a].append(b)
            indeg[b]+=1
assert incidences == 1260
queue=deque(f for f in ALL if indeg[f]==0)
seen=0
while queue:
    a=queue.popleft(); seen+=1
    for b in adj[a]:
        indeg[b]-=1
        if indeg[b]==0:queue.append(b)
assert seen==len(ALL), 'Morse matching has a directed cycle'

# Signed cellular simplicial chains, represented as dicts {face: integer}.
def boundary(chain):
    out=defaultdict(int)
    for f,coeff in chain.items():
        for j in range(len(f)):
            out[f[:j]+f[j+1:]]+=coeff * (-1)**j
    return {k:v for k,v in out.items() if v}
def perm_action(chain,perm):
    out=defaultdict(int)
    for f,coeff in chain.items():
        dest=[perm[k] for k in f]
        inversions=sum(a>b for i,a in enumerate(dest) for b in dest[i+1:])
        out[tuple(sorted(dest))] += coeff*(-1)**inversions
    return {k:v for k,v in out.items() if v}
def subchains(a,b):
    out=defaultdict(int)
    for f,v in a.items():out[f]+=v
    for f,v in b.items():out[f]-=v
    return {k:v for k,v in out.items() if v}

# Sparse integral four-cycle, certified by exact boundary cancellation.
Z_ENTRIES = [(0,1),(1,-1),(2,1),(3,1),(4,-1),(5,1),(7,-1),
 (9,1),(11,-1),(14,-1),(16,1),(18,-1),(22,1),(23,-1),
 (25,-1),(28,1),(30,1),(31,1),(34,-1),(35,-1),(36,-1),
 (37,1),(38,-1),(39,1),(42,-1),(43,1),(46,1),(47,-1),
 (50,-1),(51,-1),(55,1),(56,1),(59,-1),(66,1),(67,-1),(68,1)]
Z={FACES[4][i]:coeff for i,coeff in Z_ENTRIES}
assert not boundary(Z)
# The following integer 4-cochain evaluates 1 on Z and annihilates all
# boundaries of 5-simplices, proving [Z] is primitive and not a boundary.
COCHAIN={FACES[4][0]:1,FACES[4][6]:1}
def ev(chain):return sum(COCHAIN.get(f,0)*coeff for f,coeff in chain.items())
assert ev(Z)==1
for f in FACES[5]:assert ev(boundary({f:1}))==0

# Four affine transformations generate AGL(2,3); each changes Z by a known
# integral boundary. Thus H_4 is the trivial one-dimensional module.
GENERATORS = [
 ((2,0,0,1),(0,0),{11:1}),
 ((1,1,0,1),(0,0),{8:1,9:1}),
 ((0,1,1,0),(0,0),{9:1}),
 ((1,0,0,1),(1,0),{0:1,1:1,3:1,5:-1,7:-1,9:1})]
def permutation(A,t):
    a,b,c,d=A;u,v=t
    return tuple(PINDEX[((a*x+b*y+u)%3,(c*x+d*y+v)%3)] for x,y in POINTS)
G=[]
for A in product(range(3), repeat=4):
    if (A[0]*A[3]-A[1]*A[2]) % 3==0:continue
    for t in POINTS:G.append((A,t,permutation(A,t)))
assert len(G)==432 and len({g[2] for g in G})==432
for A,t,Y in GENERATORS:
    y={FACES[5][i]:v for i,v in Y.items()}
    assert not subchains(subchains(perm_action(Z,permutation(A,t)),Z), boundary(y))
# Confirm the four chosen transformations generate the full finite group.
base=tuple(range(9))
genperm=[permutation(A,t) for A,t,_ in GENERATORS]
visited={base};q=deque([base])
while q:
    h=q.popleft()
    for g in genperm:
        gh=tuple(g[h[i]] for i in range(9))
        if gh not in visited:visited.add(gh);q.append(gh)
assert len(visited)==432

# Direct exact Lefschetz traces for every affine symmetry.
DIRECTIONS=set()
for a,b in product(range(3),repeat=2):
    if (a,b)!=(0,0):DIRECTIONS.add(frozenset({(a,b),((2*a)%3,(2*b)%3)}))
assert len(DIRECTIONS)==4
CHAR_GROUP={}
for A,t,perm in G:
    a,b,c,d=A
    detsign=1 if (a*d-b*c)%3==1 else -1
    fixed_points=sum(perm[i]==i for i in range(9))
    fixed_directions=sum(
       frozenset({((a*x+b*y)%3,(c*x+d*y)%3) for x,y in direction})==direction
       for direction in DIRECTIONS)
    L=0
    for dim in range(6):
        for face in FACES[dim]:
            im=[perm[i] for i in face]
            if tuple(sorted(im))!=face:continue
            inv=sum(a>b for j,a in enumerate(im) for b in im[j+1:])
            L+=(-1)**(dim+inv)
    # H_0 trivial, H_3 the only nonzero homology besides H_4 trivial.
    chi3=2-L
    expected=detsign*(fixed_points+fixed_directions-2)
    assert chi3==expected,(A,t,chi3,expected)
    CHAR_GROUP[(A,t)]=(chi3,fixed_points,fixed_directions,detsign)
assert CHAR_GROUP[((1,0,0,1),(0,0))][0]==11
assert sum(x[0] for x in CHAR_GROUP.values())==0  # no invariant H_3

print('points=9 lines=12 faces=339 f_vector=(9,36,84,126,72,12)')
print('morse_pairs=163 critical=(1,0,0,11,1,0) incidences=1260 acyclic=true')
print('integral_top_cycle_support=36 cochain_pair=(0,6) pairing=1')
print('top_generator_boundary_witnesses=4 affine_group_order=432')
print('rational_h3_character_matches_det_times_aug_points_plus_aug_directions=432/432')
print('reduced_integral_h3_rank=11 reduced_integral_h4_rank=1 other_groups=0')
print('integral_homotopy_type=11S3+S4')
