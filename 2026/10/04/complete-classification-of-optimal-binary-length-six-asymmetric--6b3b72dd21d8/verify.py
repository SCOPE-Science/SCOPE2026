from itertools import combinations, permutations
from collections import Counter

N=6
FULL=(1<<N)-1

def n01(x,y):
    # coordinates with x_i=0,y_i=1
    return ((~x)&y&FULL).bit_count()

def da(x,y):
    return max(n01(x,y),n01(y,x))

# Compatibility graph: edge iff asymmetric distance >= 2.
adj=[0]*(1<<N)
for x in range(1<<N):
    m=0
    for y in range(1<<N):
        if y!=x and da(x,y)>=2:
            m |= 1<<y
    adj[x]=m

# Exact maximum-clique enumeration by Bron-Kerbosch + cardinality pruning.
best=0
maxima=[]
nodes=0

def bk(R,P,X):
    global best,maxima,nodes
    nodes += 1
    rlen=len(R)
    if rlen + P.bit_count() < best:
        return
    if P==0 and X==0:
        if rlen>best:
            best=rlen; maxima=[tuple(R)]
        elif rlen==best:
            maxima.append(tuple(R))
        return
    U=P|X
    if U:
        # pivot maximizing neighbors in P
        uu=[]; t=U
        while t:
            b=t & -t; u=b.bit_length()-1; t-=b
            uu.append(( (P & adj[u]).bit_count(), u))
        u=max(uu)[1]
        cand=P & ~adj[u]
    else:
        cand=P
    while cand:
        b=cand & -cand; v=b.bit_length()-1; cand-=b
        bk(R+[v], P & adj[v], X & adj[v])
        P &= ~b
        X |= b
        if len(R)+P.bit_count() < best:
            break

bk([], (1<<(1<<N))-1, 0)
maxset={frozenset(C) for C in maxima}
assert best==12
assert len(maxset)==30, len(maxset)

# Enumerate perfect matchings of six coordinates.
def matchings(points):
    points=tuple(points)
    if not points:
        yield ()
        return
    a=points[0]
    for j in range(1,len(points)):
        b=points[j]
        rem=points[1:j]+points[j+1:]
        for rest in matchings(rem):
            yield ((a,b),)+rest

Ms=list(matchings(range(N)))
assert len(Ms)==15

# For each perfect matching, its transversal graph is a 3-cube; the two
# bipartition classes are independent of pair orientation up to swapping.
def code_from_matching(M,eps):
    edge_words=[]
    for a,b in M:
        edge_words.append((1<<a)|(1<<b))
    trans=[]
    for mask in range(8):
        w=0
        parity=0
        for j,(a,b) in enumerate(M):
            bit=(mask>>j)&1
            parity ^= bit
            w |= 1<<(b if bit else a)
        if parity==eps:
            trans.append(w)
    C={0,FULL,*edge_words,*[FULL^w for w in edge_words],*trans}
    assert len(C)==12
    assert min(da(x,y) for x,y in combinations(C,2))>=2
    return frozenset(C)

constructed={code_from_matching(M,e) for M in Ms for e in (0,1)}
assert len(constructed)==30
assert constructed==maxset

# Coordinate-permutation orbit is all 30 maxima.
def perm_word(x,p):
    y=0
    for i,j in enumerate(p):
        if (x>>i)&1:
            y |= 1<<j
    return y
rep=min(maxset,key=lambda C:tuple(sorted(C)))
orb={frozenset(perm_word(x,p) for x in rep) for p in permutations(range(N))}
assert orb==maxset
assert len(orb)==30
stabilizer=720//len(orb)
assert stabilizer==24

# Structural invariants and representative.
wd=Counter(x.bit_count() for x in rep)
assert wd==Counter({0:1,2:3,3:4,4:3,6:1})
rep_words=[''.join(str((x>>(N-1-i))&1) for i in range(N)) for x in sorted(rep)]
print('VERIFY_OK maximum=12 labeled_maxima=30 matchings=15 maxima_per_matching=2 coordinate_orbit=30 stabilizer=24 nodes=%d' % nodes)
print('REP=' + ','.join(rep_words))
print('WEIGHTS=' + ','.join(f'{k}:{wd[k]}' for k in sorted(wd)))
