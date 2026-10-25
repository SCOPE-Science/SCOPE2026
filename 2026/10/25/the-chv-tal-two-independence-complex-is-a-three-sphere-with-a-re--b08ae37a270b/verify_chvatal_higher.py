"""Standalone finite certificate for the two-independence complex of the Chvatal graph.
Python 3 standard library only. No external data or packages are used.
"""
from collections import Counter,defaultdict,deque
from itertools import combinations

N = 12
EDGES = [(0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),
         (2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),
         (5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11)]
PIVOTS = [4,10,11,9,8,6,5,0,2,1,7,3]
R = (1,5,11,6,0,4,7,10,9,2,3,8)
S = (0,4,3,2,1,5,9,8,7,6,11,10)
ADJ = [0]*N
for i,j in EDGES:
    assert i<j and not ADJ[i]&(1<<j)
    ADJ[i]|=1<<j; ADJ[j]|=1<<i
assert len(EDGES)==24 and all(a.bit_count()==4 for a in ADJ)
assert all(not (ADJ[i]&ADJ[j]) for i,j in EDGES)  # triangle-free

def admissible(m):
    # Induced connected components of order <=2 iff induced max degree <=1.
    return all((ADJ[i]&m).bit_count()<=1 for i in range(N) if m&(1<<i))

faces = {m for m in range(1,1<<N) if admissible(m)}
vec = tuple(Counter(m.bit_count()-1 for m in faces).get(d,0) for d in range(6))
assert len(faces)==424 and vec==(12,66,148,142,52,4), vec

unmatched=set(faces)
matched=[]
for i in PIVOTS:
    b=1<<i
    for low in sorted(unmatched):
        if not(low&b) and (low|b) in unmatched:
            unmatched.remove(low);unmatched.remove(low|b)
            matched.append((low,low|b))
assert len(matched)==211
assert len(unmatched)==2
crit=Counter(m.bit_count()-1 for m in unmatched)
assert crit=={0:1,3:1},(unmatched,crit)

# The Forman gradient digraph includes every nonempty face-poset cover.
# Matched incidences are oriented upward; all others downward.
pairs=set(matched)
adj=defaultdict(list);indeg={m:0 for m in faces};incidences=0
for m in faces:
    for i in range(N):
        b=1<<i
        if m&b and (m^b) in faces:
            low=m^b
            u,v=(low,m) if (low,m) in pairs else (m,low)
            adj[u].append(v);indeg[v]+=1;incidences+=1
queue=deque(x for x in faces if indeg[x]==0)
visited=0
while queue:
    x=queue.popleft();visited+=1
    for y in adj[x]:
        indeg[y]-=1
        if indeg[y]==0:queue.append(y)
assert visited==len(faces),(visited,len(faces))

# Completely separate modular simplicial boundary ranks: no Morse edges used.
bydim={d:sorted(m for m in faces if m.bit_count()==d+1) for d in range(6)}
def rank_mod_p(d,p):
    if d==0:return 0
    rowid={m:i for i,m in enumerate(bydim[d-1])}
    base={};rank=0
    for mask in bydim[d]:
        vs=[i for i in range(N) if mask>>i&1]
        column={rowid[mask^(1<<i)]:(1 if j%2==0 else p-1) for j,i in enumerate(vs)}
        while column:
            h=max(column)
            if h not in base:
                z=pow(column[h],-1,p)
                base[h]={k:(v*z)%p for k,v in column.items()}
                rank+=1;break
            z=column[h]
            for k,v in base[h].items():
                w=(column.get(k,0)-z*v)%p
                if w:column[k]=w
                else:column.pop(k,None)
    return rank
for p in (2,3,101):
    ranks={d:rank_mod_p(d,p) for d in range(1,6)}
    hom={d:len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(6)}
    assert hom=={0:1,1:0,2:0,3:1,4:0,5:0},(p,ranks,hom)

# Exhaustive graph automorphism backtrack: bijective adjacency / nonadjacency.
# This is independent of homology and matching; all mappings are checked.
def automorphisms():
    # Choose the most constraining currently unmapped domain vertex.
    mapping={}; unused=set(range(N)); answer=[]
    def rec():
        if len(mapping)==N:
            answer.append(tuple(mapping[i] for i in range(N)));return
        i=max((i for i in range(N) if i not in mapping),
              key=lambda j:(sum(1 for k in mapping if ADJ[j]>>k&1), -j))
        for v in sorted(unused):
            if all(bool(ADJ[i]&(1<<j))==bool(ADJ[v]&(1<<w)) for j,w in mapping.items()):
                mapping[i]=v;unused.remove(v);rec();unused.add(v);del mapping[i]
    rec();return answer

def compose(a,b):return tuple(a[b[i]] for i in range(N))

def sign_perm(a):return -1 if sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2 else 1

def character(g):
    # Reduced Hopf trace on H_3: -1 + sum_{fixed nonempty face} (-1)^dim sign(g|face).
    signed=0
    for face in faces:
        xs=[i for i in range(N) if face>>i&1]
        ys=[g[i] for i in xs]
        if set(xs)!=set(ys):continue
        signed+=(-1)**(len(xs)-1)*sign_perm([xs.index(j) for j in ys])
    return 1-signed

autos=automorphisms()
assert len(autos)==8,len(autos)
autoset=set(autos)
assert R in autoset and S in autoset
ident=tuple(range(N))
assert compose(R,R)!=ident and compose(R,compose(R,compose(R,R)))==ident
assert compose(S,S)==ident
assert compose(S,compose(R,S))==compose(R,compose(R,R))
seen={ident};front=[ident]
while front:
    g=front.pop()
    for h in [compose(g,R),compose(g,S)]:
        if h not in seen:seen.add(h);front.append(h)
assert seen==autoset
assert character(ident)==1
assert character(R)==-1
assert character(S)==1
for a in range(4):
    ra=ident
    for _ in range(a):ra=compose(ra,R)
    for b in (0,1):
        g=ra if b==0 else compose(ra,S)
        assert character(g)==(-1)**a,(a,b,character(g))
print('CHVATAL_HIGHER_OK')
print('nvertices=',N,'edges=',len(EDGES),'faces=',len(faces),'f=',vec)
print('morse_pairs=',len(matched),'critical_masks=',sorted(unmatched),'critical_dimensions=',dict(crit))
print('directed_incidences=',incidences,'gradient_sort_visits=',visited)
print('automorphisms=',len(autos),'character_R=',character(R),'character_S=',character(S))
print('homology_F2_F3_F101= (1,0,0,1,0,0) unreduced')
