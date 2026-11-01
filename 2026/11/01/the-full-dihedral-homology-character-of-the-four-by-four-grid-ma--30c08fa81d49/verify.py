"""Exact integer certificate for the square-grid matching-complex symmetry theorem.

Run: python3 verify.py. Standard library only. Edge numbers are the deterministic
column-major-within-row incidence order described in RESULT.md.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

SIDE=4
V=[(i,j) for i in range(SIDE) for j in range(SIDE)]
EDGES=[]
for i,j in V:
    if i+1<SIDE: EDGES.append(((i,j),(i+1,j)))
    if j+1<SIDE: EDGES.append(((i,j),(i,j+1)))
assert len(EDGES)==24
E=len(EDGES)
EDGEMAP={frozenset(e):i for i,e in enumerate(EDGES)}
ADMISSIBLE=[sum(1<<j for j,(a,b) in enumerate(EDGES)
                if i!=j and len({u,v,a,b})==4)
            for i,(u,v) in enumerate(EDGES)]

# Generate every simplex exactly once by adding only larger edge labels.
BY_SIZE=[{0}]
while True:
    next_faces=set()
    for mask in BY_SIZE[-1]:
        last=mask.bit_length()-1
        for e in range(last+1,E):
            if not mask & ~ADMISSIBLE[e]:
                next_faces.add(mask | (1<<e))
    if not next_faces:break
    BY_SIZE.append(next_faces)
FACES=set().union(*BY_SIZE)
FVECTOR=tuple(len(x) for x in BY_SIZE)
assert FVECTOR==(1,24,224,1044,2593,3388,2150,552,36)

# Independent check via a vertex-by-vertex matching-polynomial recurrence.
VERTEX_INDEX={v:i for i,v in enumerate(V)}
NEIGHBOR=[0]*len(V)
for u,v in EDGES:
    a,b=VERTEX_INDEX[u],VERTEX_INDEX[v]
    NEIGHBOR[a]|=1<<b
    NEIGHBOR[b]|=1<<a
@lru_cache(None)
def matching_poly(vertices):
    if not vertices:return (1,)
    bit=vertices & -vertices
    v=bit.bit_length()-1
    remaining=vertices^bit
    poly=list(matching_poly(remaining))
    neighbors=NEIGHBOR[v]&remaining
    while neighbors:
        a=neighbors&-neighbors;neighbors^=a
        smaller=matching_poly(remaining^a)
        while len(poly)<len(smaller)+1: poly.append(0)
        for k,num in enumerate(smaller):poly[k+1]+=num
    return tuple(poly)
assert matching_poly((1<<len(V))-1)==FVECTOR

# An ordered toggle matching; the ordering is a specific deterministic
# certificate, not an assumption on arbitrary greedy matchings.
TOGGLE_ORDER=(1,23,9,0,6,20,18,21,5,19,3,12,7,22,14,11,10,2,16,8,4,17,15,13)
assert sorted(TOGGLE_ORDER)==list(range(E))
remaining=set(FACES)
PAIRS={}
for e in TOGGLE_ORDER:
    bit=1<<e
    for low in sorted(remaining):
        if low&bit:continue
        high=low|bit
        if high in remaining:
            PAIRS[low]=high
            remaining.remove(low)
            remaining.remove(high)
CRITICAL=remaining
assert len(PAIRS)==5002
assert Counter(s.bit_count()-1 for s in CRITICAL)=={4:6,5:2}

# Full global acyclicity certificate on the augmented Hasse diagram.
OUT=defaultdict(list)
IN=defaultdict(int)
arc_count=0
for high in FACES:
    whilebits=high
    while whilebits:
        bit=whilebits&-whilebits;whilebits^=bit
        low=high^bit
        if PAIRS.get(low)==high:source,target=low,high
        else:source,target=high,low
        OUT[source].append(target)
        IN[target]+=1
        arc_count+=1
assert arc_count==47968
queue=deque(x for x in FACES if IN[x]==0)
processed=0
while queue:
    v=queue.popleft();processed+=1
    for w in OUT[v]:
        IN[w]-=1
        if IN[w]==0:queue.append(w)
assert processed==len(FACES)

CRIT4=sorted(s for s in CRITICAL if s.bit_count()==5)
CRIT5=sorted(s for s in CRITICAL if s.bit_count()==6)

def boundary(high):
    """Oriented boundary as a sparse integral dict (empty face included)."""
    elems=[i for i in range(E) if high&(1<<i)]
    return {high^(1<<i): (-1)**j for j,i in enumerate(elems)}

def vec_plus(a,b,c=1):
    for j,num in enumerate(b):a[j]+=c*num

def reduction(degree,critical):
    """Integral cochains dual to critical cells, by Morse pivot elimination."""
    ix={face:i for i,face in enumerate(critical)}
    @lru_cache(None)
    def reduce(face):
        if face in ix:return tuple(int(j==ix[face]) for j in range(len(critical)))
        if face in PAIRS:
            high=PAIRS[face]
            assert high.bit_count()==degree+1
            bd=boundary(high)
            sign=bd[face]
            ans=[0]*len(critical)
            for lower,c in bd.items():
                if lower!=face:vec_plus(ans,reduce(lower),-sign*c)
            return tuple(ans)
        return (0,)*len(critical)
    return reduce

RED4=reduction(5,CRIT4)
RED5=reduction(6,CRIT5)

def dot_boundary(red,face,dim):
    ans=[0]*dim
    for lower,c in boundary(face).items():vec_plus(ans,red(lower),c)
    return tuple(ans)

# Check cochain property against ALL relevant boundaries, not samples.
assert all(dot_boundary(RED4,face,6)==(0,)*6 for face in BY_SIZE[6])
assert all(dot_boundary(RED5,face,2)==(0,)*2 for face in BY_SIZE[7])
assert all(dot_boundary(RED4,face,6)==(0,)*6 for face in CRIT5)

def pivot_order(degree):
    """A topological elimination order for lower degree-1 faces matched up."""
    lower_to_upper={s:t for s,t in PAIRS.items() if s.bit_count()==degree}
    edges=defaultdict(list)
    indegree={s:0 for s in lower_to_upper}
    for s,t in lower_to_upper.items():
        for d in boundary(t):
            if d!=s and d in lower_to_upper:
                edges[s].append(d)
                indegree[d]+=1
    q=deque(s for s,deg in indegree.items() if deg==0)
    order=[]
    while q:
        s=q.popleft();order.append(s)
        for d in edges[s]:
            indegree[d]-=1
            if indegree[d]==0:q.append(d)
    assert len(order)==len(lower_to_upper)
    return order,lower_to_upper

def lift_cycle(critical_face,pivots,lower_to_upper):
    """Cancel all degree-(q-1) boundary entries with unit pivots."""
    chain=defaultdict(int,{critical_face:1})
    bd=defaultdict(int,boundary(critical_face))
    for low in pivots:
        c=bd.get(low,0)
        if c==0:continue
        high=lower_to_upper[low]
        delta=-c*boundary(high)[low]
        chain[high]+=delta
        for face,a in boundary(high).items():
            bd[face]+=delta*a
            if bd[face]==0:del bd[face]
    assert not bd
    return {s:c for s,c in chain.items() if c}

PIVOT3,LOW_TO_HIGH4=pivot_order(4)
PIVOT4,LOW_TO_HIGH5=pivot_order(5)
Z4=[lift_cycle(s,PIVOT3,LOW_TO_HIGH4) for s in CRIT4]
Z5=[lift_cycle(s,PIVOT4,LOW_TO_HIGH5) for s in CRIT5]

def pairing(red,cycles):
    answer=[]
    for z in cycles:
        acc=[0]*len(cycles)
        for face,c in z.items():vec_plus(acc,red(face),c)
        answer.append(tuple(acc))
    return answer
assert pairing(RED4,Z4)==[tuple(int(i==j) for i in range(6)) for j in range(6)]
assert pairing(RED5,Z5)==[(1,0),(0,1)]

# Eight geometric symmetries, with signed induced simplicial action.
AUTOS={
 'e':lambda v:v,
 'r':lambda v:(v[1],3-v[0]),
 'r2':lambda v:(3-v[0],3-v[1]),
 'r3':lambda v:(3-v[1],v[0]),
 'axis_h':lambda v:(v[0],3-v[1]),
 'axis_v':lambda v:(3-v[0],v[1]),
 'diag':lambda v:(v[1],v[0]),
 'antidiag':lambda v:(3-v[1],3-v[0]),
}
def edge_permutation(transform):
    return tuple(EDGEMAP[frozenset(map(transform,edge))] for edge in EDGES)
PERMS={name:edge_permutation(a) for name,a in AUTOS.items()}
assert len(set(PERMS.values()))==8

def act_simplex(face,p):
    new=[p[i] for i in range(E) if face&(1<<i)]
    inversions=sum(new[i]>new[j] for i in range(len(new)) for j in range(i+1,len(new)))
    return sum(1<<i for i in new),(-1)**inversions

def action_matrix(p,cycles,red):
    size=len(cycles)
    matrix=[[0]*size for _ in range(size)]
    for j,z in enumerate(cycles):
        for face,c in z.items():
            new,sign=act_simplex(face,p)
            for i,entry in enumerate(red(new)):
                matrix[i][j]+=sign*c*entry
    return tuple(tuple(row) for row in matrix)

def mul(a,b):
    n=len(a)
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(n))
                       for j in range(n)) for i in range(n))
def ident(n):return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def trace(a):return sum(a[i][i] for i in range(len(a)))
A4={name:action_matrix(p,Z4,RED4) for name,p in PERMS.items()}
A5={name:action_matrix(p,Z5,RED5) for name,p in PERMS.items()}
for n,action in [(4,A4),(5,A5)]:
    dim=len(next(iter(action.values())))
    assert action['e']==ident(dim)
    r=action['r'];h=action['axis_h'];r3=action['r3']
    assert mul(mul(r,r),mul(r,r))==ident(dim)
    assert mul(h,h)==ident(dim)
    assert mul(mul(h,r),h)==r3
assert A5['r']==((0,1),(-1,0))
assert A5['axis_h']==((-1,0),(0,1))

CHAR4={name:trace(A4[name]) for name in AUTOS}
CHAR5={name:trace(A5[name]) for name in AUTOS}
assert CHAR4==dict(e=6,r=2,r2=2,r3=2,axis_h=0,axis_v=0,diag=-2,antidiag=-2)
assert CHAR5==dict(e=2,r=0,r2=-2,r3=0,axis_h=0,axis_v=0,diag=0,antidiag=0)

# Independent alternating chain-trace formula: signed fixed simplices.
LEFSCHETZ={}
for name,p in PERMS.items():
    tr=-1 # the empty face contributes -1 to reduced Lefschetz
    for face in FACES:
        if not face:continue
        new,sign=act_simplex(face,p)
        if new==face:tr+=(-1)**(face.bit_count()-1)*sign
    LEFSCHETZ[name]=tr
    assert tr==CHAR4[name]-CHAR5[name]
assert LEFSCHETZ==dict(e=4,r=2,r2=4,r3=2,axis_h=0,axis_v=0,diag=-2,antidiag=-2)

# D4 irreducibles: A1 trivial, A2 reflection sign, B1 quarter-turn sign
# with axis reflection +1, B2 both quarter-turn and axis reflection sign,
# E the natural plane representation.
character_irreps={
 'A1':(1,1,1,1,1), 'A2':(1,1,1,-1,-1),
 'B1':(1,-1,1,1,-1), 'B2':(1,-1,1,-1,1),
 'E':(2,0,-2,0,0),
}
cl=['e','r','r2','axis_h','diag']
weights=(1,2,1,2,2)
for char,expected in [(CHAR4,{'A1':1,'A2':2,'B1':1,'B2':0,'E':1}),
                      (CHAR5,{'A1':0,'A2':0,'B1':0,'B2':0,'E':1})]:
    coeff={}
    for name,irr in character_irreps.items():
        numerator=sum(w*char[k]*irr[j] for j,(k,w) in enumerate(zip(cl,weights)))
        assert numerator%8==0
        coeff[name]=numerator//8
    assert coeff==expected

print('FACES_OK',FVECTOR,'total',len(FACES),'independent_vertex_recurrence=PASS')
print('MORSE_OK pairs',len(PAIRS),'critical',dict(Counter(s.bit_count()-1 for s in CRITICAL)),
      'Hasse_arcs',arc_count,'acyclic_processed',processed)
print('CYCLE_OK degree4',tuple(map(len,Z4)),'degree5',tuple(map(len,Z5)),
      'cochains_cocycles_and_dual_pairings=PASS')
print('H5_INTEGRAL_OK rotation',A5['r'],'horizontal_reflection',A5['axis_h'])
print('H4_CHARACTER_OK',CHAR4)
print('H5_CHARACTER_OK',CHAR5)
print('LEFSCHETZ_OK',LEFSCHETZ)
print('RATIONAL_DECOMPOSITION_OK H4=A1+2A2+B1+E H5=E')
print('ALL_VERIFY_OK')
