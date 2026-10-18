#!/usr/bin/env python3
"""Exact finite certificate for the two-independence complex of the Durer graph."""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N=12
ORDER=(2,11,10,0,6,8,7,1,5,9,3,4)

def graph():
    adj=[0]*N
    def e(a,b):
        adj[a]|=1<<b;adj[b]|=1<<a
    for i in range(6):
        e(i,(i+1)%6)
        e(i,6+i)
        e(6+i,6+(i+2)%6)
    assert all(x.bit_count()==3 for x in adj)
    return adj

ADJ=graph()

def allowed(mask):
    remain=mask
    while remain:
        start=remain&-remain;remain ^= start
        reached=start;front=start
        while front:
            bit=front&-front;front ^= bit
            v=bit.bit_length()-1
            add=ADJ[v]&mask&~reached
            reached|=add
            front|=add
        if reached.bit_count()>2:return False
        remain &= ~reached
    return True

# Independently characterize all faces by forbidden connected triples.
BAD_TRIPLES=[]
for a in range(N):
    for b in range(a+1,N):
        for c in range(b+1,N):
            edges=int(bool(ADJ[a]&(1<<b)))+int(bool(ADJ[a]&(1<<c)))+int(bool(ADJ[b]&(1<<c)))
            if edges>=2:BAD_TRIPLES.append((1<<a)|(1<<b)|(1<<c))
for m in range(1<<N):
    via_forbidden=not any((m&triple)==triple for triple in BAD_TRIPLES)
    assert allowed(m)==via_forbidden,(m,'independent membership disagreement')

FACES={m for m in range(1,1<<N) if allowed(m)}
F_BY_D={d:sorted(x for x in FACES if x.bit_count()==d+1) for d in range(6)}
assert len(FACES)==809
assert [len(F_BY_D[d]) for d in range(6)]==[12,66,188,285,204,54]
assert set(F_BY_D[0]) == {1<<i for i in range(N)}

unpaired=set(FACES)
PAIR_LOWER={};PAIR_UPPER={}
for v in ORDER:
    b=1<<v
    for x in sorted(FACES):
        if x not in unpaired or x&b:continue
        y=x|b
        if y in unpaired:
            unpaired.remove(x);unpaired.remove(y)
            PAIR_LOWER[x]=y
            PAIR_UPPER[y]=x
assert len(PAIR_LOWER)==402 and len(unpaired)==5
crit=sorted(unpaired,key=lambda x:(x.bit_count(),x))
assert Counter(x.bit_count()-1 for x in crit)=={0:1,3:3,4:1}

# Acyclicity of the gradient vector field: all codimension-one faces.
# Unmatched cover relations point down; matched cover relations point up.
indeg={x:0 for x in FACES}
arcs={x:[] for x in FACES}
num_cover=0
for face in FACES:
    if face.bit_count()==1:continue
    m=face
    while m:
        b=m&-m;m^=b;sub=face^b
        num_cover+=1
        if PAIR_UPPER.get(face)==sub:src,dst=sub,face
        else:src,dst=face,sub
        arcs[src].append(dst);indeg[dst]+=1
q=deque(x for x in FACES if indeg[x]==0);seen=0
while q:
    x=q.popleft();seen+=1
    for y in arcs[x]:
        indeg[y]-=1
        if indeg[y]==0:q.append(y)
assert seen==len(FACES),('cyclic Morse matching',seen)

# Signed simplicial incidence of facet obtained by removing vertex v.
def signed_facets(y):
    vs=[i for i in range(N) if y&(1<<i)]
    for j,v in enumerate(vs):
        yield y^(1<<v),(-1 if j%2 else 1)

crit3=tuple(x for x in crit if x.bit_count()==4)
crit4=next(x for x in crit if x.bit_count()==5)
@lru_cache(None)
def proj3(x):
    if x in unpaired:return {x:1}
    if x in PAIR_UPPER:return {}
    y=PAIR_LOWER[x]
    piv=next(coeff for sub,coeff in signed_facets(y) if sub==x)
    result=defaultdict(int)
    for sub,coeff in signed_facets(y):
        if sub==x:continue
        for k,a in proj3(sub).items():result[k]-=coeff*piv*a
    return {k:v for k,v in result.items() if v}

boundary=defaultdict(int)
for sub,coeff in signed_facets(crit4):
    for k,a in proj3(sub).items():boundary[k]+=coeff*a
assert {k:v for k,v in boundary.items() if v}=={},('nonzero integral Morse boundary',dict(boundary))

# Independent homology ranks of all simplicial boundary matrices over F_2.
def rank2(columns):
    piv={}
    for col in columns:
        while col:
            i=col.bit_length()-1
            if i not in piv:
                piv[i]=col;break
            col^=piv[i]
    return len(piv)
R={}
for d in range(1,6):
    base={x:i for i,x in enumerate(F_BY_D[d-1])}
    cols=[]
    for y in F_BY_D[d]:
        bits=0
        for x,_ in signed_facets(y):bits^=1<<base[x]
        cols.append(bits)
    R[d]=rank2(cols)
betti={d:len(F_BY_D[d])-R.get(d,0)-R.get(d+1,0)-(1 if d==0 else 0) for d in range(6)}
assert {d:b for d,b in betti.items() if b}=={3:3,4:1}

# Extra independent membership check: every 3-subset fails iff connected.
for a in range(N):
    for b in range(a+1,N):
        for c in range(b+1,N):
            mask=(1<<a)|(1<<b)|(1<<c)
            pairs= int(bool(ADJ[a]&(1<<b))) + int(bool(ADJ[a]&(1<<c))) + int(bool(ADJ[b]&(1<<c)))
            assert allowed(mask) == (pairs<=1)

print('DURER_IND2_INTEGRAL_HOMOTOPY_VERIFIED')
print('forbidden_triples',len(BAD_TRIPLES),'faces',len(FACES),'dimensions',[len(F_BY_D[d]) for d in range(6)])
print('pairs',len(PAIR_LOWER),'cover_relations',num_cover,'critical_cells',dict(Counter(x.bit_count()-1 for x in crit)))
print('critical_3',crit3,'critical_4',crit4,'morse_boundary',dict(boundary))
print('mod2_boundary_ranks',R,'reduced_betti',betti)
