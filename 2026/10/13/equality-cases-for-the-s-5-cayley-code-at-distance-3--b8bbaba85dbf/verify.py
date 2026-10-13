from itertools import permutations, combinations
from collections import Counter, deque

N=5
PERMS=list(permutations(range(N)))
IDX={p:i for i,p in enumerate(PERMS)}
ID=tuple(range(N))

def comp(p,q):
    return tuple(p[q[i]] for i in range(N))

def inv(p):
    r=[0]*N
    for i,x in enumerate(p): r[x]=i
    return tuple(r)

def cycles_count(p):
    seen=[False]*N; c=0
    for i in range(N):
        if not seen[i]:
            c+=1; j=i
            while not seen[j]:
                seen[j]=True; j=p[j]
    return c

def cycle_type(p):
    seen=[False]*N; lens=[]
    for i in range(N):
        if not seen[i]:
            j=i; k=0
            while not seen[j]:
                seen[j]=True; k+=1; j=p[j]
            lens.append(k)
    return tuple(sorted(lens,reverse=True))

def dist(p,q):
    return N-cycles_count(comp(inv(p),q))

def even(p):
    return dist(ID,p)%2==0

def word(p):
    return ''.join(str(x+1) for x in p)

# Independent shortest-path reconstruction of the metric from all transpositions.
trans=[]
for i in range(N):
    for j in range(i+1,N):
        t=list(ID); t[i],t[j]=t[j],t[i]; trans.append(tuple(t))
bfs={ID:0}; q=deque([ID])
while q:
    p=q.popleft()
    for t in trans:
        y=comp(t,p)
        if y not in bfs:
            bfs[y]=bfs[p]+1; q.append(y)
assert len(bfs)==120
assert all(bfs[p]==dist(ID,p) for p in PERMS)
dist_hist=Counter(dist(ID,p) for p in PERMS)
assert dist_hist==Counter({0:1,1:10,2:35,3:50,4:24})

# Normalize by requiring the identity. The remaining 74 candidates have distance at least 3 from it.
V=[p for p in PERMS if p!=ID and dist(ID,p)>=3]
m=len(V)
adj=[0]*m; edges=0
for i in range(m):
    for j in range(i+1,m):
        if dist(V[i],V[j])>=3:
            adj[i]|=1<<j; adj[j]|=1<<i; edges+=1
assert len(V)==74 and edges==1536

# Exhaustive Bron-Kerbosch enumeration of all maximal cliques in the normalized compatibility graph.
maximal=[]
def bk(R,P,X):
    if not P and not X:
        maximal.append(tuple(R)); return
    union=P|X
    if union:
        u=max((i for i in range(m) if (union>>i)&1), key=lambda i:(P&adj[i]).bit_count())
        cand=P & ~adj[u]
    else:
        cand=P
    while cand:
        bit=cand & -cand; v=bit.bit_length()-1
        bk(R+[v],P&adj[v],X&adj[v])
        P &= ~bit; X |= bit; cand &= ~bit
bk([], (1<<m)-1, 0)
maximal_hist=Counter(len(c) for c in maximal)
assert maximal_hist==Counter({4:1250,5:6480,6:2520,9:12})
maxcls=[c for c in maximal if len(c)==9]
assert len(maxcls)==12
norm=[frozenset([ID]+[V[i] for i in cl]) for cl in maxcls]

# Structural classification of the twelve normalized maxima.
H_to_codes={}
for C in norm:
    assert len(C)==10
    pair_types=Counter(cycle_type(comp(inv(a),b)) for a,b in combinations(C,2))
    assert pair_types==Counter({(4,1):25,(5,):20})
    ev=frozenset(x for x in C if even(x)); od=frozenset(C-ev)
    assert len(ev)==5 and len(od)==5 and ID in ev
    assert all(comp(a,b) in ev for a in ev for b in ev)
    assert all(cycle_type(x)==(5,) for x in ev if x!=ID)
    H=ev
    g=next(iter(od))
    assert od==frozenset(comp(g,h) for h in H)==frozenset(comp(h,g) for h in H)
    normal=frozenset(x for x in PERMS if frozenset(comp(comp(x,h),inv(x)) for h in H)==H)
    assert len(normal)==20 and g in normal
    # The odd coset represents an element of order four in the quotient N(H)/H.
    g2=comp(g,g); g4=comp(g2,g2)
    assert g2 not in H and g4 in H
    H_to_codes.setdefault(H,[]).append(C)
assert len(H_to_codes)==6 and all(len(v)==2 for v in H_to_codes.values())

# All labeled maxima and the exact 24-per-subgroup decomposition.
allmax=set()
per_H=[]
for H,codes in H_to_codes.items():
    fam=set()
    for C in codes:
        for a in PERMS:
            fam.add(frozenset(comp(a,x) for x in C))
    assert len(fam)==24
    per_H.append(fam)
    allmax.update(fam)
assert len(allmax)==144
for C in allmax:
    assert len(C)==10
    assert min(dist(a,b) for a,b in combinations(C,2))>=3
    assert Counter(cycle_type(comp(inv(a),b)) for a,b in combinations(C,2))==Counter({(4,1):25,(5,):20})

# A concrete representative: H=< (1 2 3 4 5) > and a multiplier-by-2 normalizer element.
r=(1,2,3,4,0)
g=(0,2,4,1,3)
H={ID}; x=ID
for _ in range(4):
    x=comp(r,x); H.add(x)
REP=frozenset(H | {comp(g,h) for h in H})
assert REP in allmax
assert sorted(map(word,REP))==['12345','13524','23451','24135','34512','35241','41352','45123','51234','52413']

# The explicit group x -> a x b and x -> a x^{-1} b has 28,800 distinct maps.
adjtrans=[]
for i in range(N-1):
    t=list(ID); t[i],t[i+1]=t[i+1],t[i]; adjtrans.append(tuple(t))
tests=[ID]+adjtrans+[(1,2,0,3,4)]
sigs=set()
for eps in (0,1):
    for a in PERMS:
        for b in PERMS:
            sig=[]
            for x in tests:
                y=inv(x) if eps else x
                sig.append(IDX[comp(comp(a,y),b)])
            sigs.add(tuple(sig))
assert len(sigs)==28800

# Generator-by-generator metric preservation, followed by the code orbit.
maps=[]
for t in adjtrans:
    maps.append(lambda x,t=t: comp(t,x))
    maps.append(lambda x,t=t: comp(x,t))
maps.append(inv)
for f in maps:
    for a,b in combinations(PERMS,2):
        assert dist(f(a),f(b))==dist(a,b)
orbit={REP}; q=deque([REP])
while q:
    C=q.popleft()
    for f in maps:
        D=frozenset(f(x) for x in C)
        if D not in orbit:
            orbit.add(D); q.append(D)
assert orbit==allmax and len(orbit)==144
assert 28800//144==200

print('VERIFY_OK',
      'vertices=120',
      'id_distance_hist=0:1,1:10,2:35,3:50,4:24',
      'normalized_candidates=74',
      'compatibility_edges=1536',
      'maximal_cliques=10262',
      'maximal_hist=4:1250,5:6480,6:2520,9:12',
      'normalized_maxima=12',
      'labeled_maxima=144',
      'c5_subgroups=6',
      'codes_per_c5_subgroup=24',
      'pair_types=(4,1):25,(5):20',
      'isometry_group_size=28800',
      'orbits=1',
      'orbit_size=144',
      'stabilizer=200')
