#!/usr/bin/env python3
"""Exact, self-contained checker for a finite icosahedral simplicial complex."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N = 12
EDGES = [
(0,1),(0,5),(0,7),(0,8),(0,11),(1,2),(1,5),(1,6),(1,8),
(2,3),(2,6),(2,8),(2,9),(3,4),(3,6),(3,9),(3,10),
(4,5),(4,6),(4,10),(4,11),(5,6),(5,11),(7,8),(7,9),
(7,10),(7,11),(8,9),(9,10),(10,11)]
GENS = [
(0,5,6,3,10,11,4,8,1,2,9,7),
(1,0,7,10,4,5,11,2,8,9,3,6),
]
E = tuple(range(N))
A = [0]*N
for u,v in EDGES:
    A[u]|=1<<v; A[v]|=1<<u
assert len(EDGES)==30 and all(a.bit_count()==5 for a in A)
assert len({(i,j,k) for i,j,k in combinations(range(N),3) if A[i]>>j&1 and A[j]>>k&1 and A[k]>>i&1})==20

def independent2(mask):
    return all((A[i]&mask).bit_count()<=1 for i in range(N) if mask>>i&1)

# Independent definition: forbid all triples with a vertex adjacent to the other two.
FORBIDDEN = {((1<<i)|(1<<j)|(1<<k)) for i in range(N)
             for j,k in combinations([v for v in range(N) if A[i]>>v&1],2)}

def forbidden_free(mask):
    return not any((mask&t)==t for t in FORBIDDEN)

assert all(independent2(m)==forbidden_free(m) for m in range(1<<N))
F = {m for m in range(1,1<<N) if independent2(m)}
fvec = tuple(sum(m.bit_count()==d+1 for m in F) for d in range(4))
assert fvec == (12,66,140,105) and len(F)==323
assert all(m.bit_count()<=4 for m in F)
print('vertices_edges_triangles', N,len(EDGES),20)
print('independent2_faces',len(F),'f_vector',fvec,'forbidden_triples',len(FORBIDDEN))

# Lexicographic vertex patchwork matching, excluding the empty simplex.
remaining=set(F); pairs=[]
for i in range(N):
    for lo in sorted(remaining):
        up=lo|(1<<i)
        if (lo>>i&1)==0 and up in remaining:
            remaining.remove(lo);remaining.remove(up)
            pairs.append((lo,up))
assert len(pairs)==149
crit={d:sorted(m for m in remaining if m.bit_count()==d+1) for d in range(4)}
assert [len(crit[d]) for d in range(4)]==[1,0,2,22]
print('morse_pairs',len(pairs),'critical_dimensions',(1,0,2,22))

# Check the full Hasse graph: unmatched cover arrows upper -> lower,
# matched cover arrows lower -> upper.
match=set(pairs)
out={m:[] for m in F}; indegree={m:0 for m in F}; arcs=0
for up in F:
    if up.bit_count()<2: continue
    for i in range(N):
        if up>>i&1:
            lo=up^(1<<i)
            if (lo,up) in match: a,b=lo,up
            else: a,b=up,lo
            out[a].append(b);indegree[b]+=1;arcs+=1
queue=deque(x for x in F if indegree[x]==0); visits=0
while queue:
    a=queue.popleft();visits+=1
    for b in out[a]:
        indegree[b]-=1
        if indegree[b]==0:queue.append(b)
assert visits==len(F) and arcs==972
print('hasse_arcs',arcs,'acyclic_visits',visits)

lower_to_upper=dict(pairs);upper_to_lower={b:a for a,b in pairs}

def boundary(mask):
    return {mask^(1<<i):(-1)**j for j,i in enumerate(i for i in range(N) if mask>>i&1)}

@lru_cache(None)
def projection_2(s):
    if s in remaining: return {s:1}
    if s in upper_to_lower: return {}
    up=lower_to_upper[s]
    terms=boundary(up)
    pivot=terms.pop(s)
    assert abs(pivot)==1
    z=defaultdict(int)
    for other,c in terms.items():
        for t,q in projection_2(other).items():
            z[t]-=c*q*pivot
    return {t:q for t,q in z.items() if q}

C2=crit[2]; C3=crit[3]
columns=[]
for up in C3:
    z=defaultdict(int)
    for s,c in boundary(up).items():
        for t,q in projection_2(s).items():z[t]+=c*q
    columns.append(tuple(z[t] for t in C2))
assert len(columns)==22 and all(len(x)==2 for x in columns)
minors=[(i,j,columns[i][0]*columns[j][1]-columns[i][1]*columns[j][0])
        for i,j in combinations(range(22),2)]
witness=next((i,j,d) for i,j,d in minors if abs(d)==1)
assert witness and sum(x!=(0,0) for x in columns)>0
print('integer_Morse_boundary_columns',columns)
print('unimodular_minor',witness,'rank',2,'Smith_diagonal',(1,1))

# Independently compute simplicial Betti ranks over small prime fields.
def rank_modp(M,p):
    basis={};r=0
    for row in M:
        v=dict((j,x%p) for j,x in row.items() if x%p)
        while v:
            pivot=min(v)
            if pivot not in basis:
                a=pow(v[pivot],-1,p)
                basis[pivot]={i:(q*a)%p for i,q in v.items() if q%p}
                r+=1;break
            fac=v[pivot]
            for i,q in basis[pivot].items():
                v[i]=(v.get(i,0)-fac*q)%p
                if not v[i]:v.pop(i,None)
    return r
s_by_dim=[[m for m in sorted(F) if m.bit_count()==d+1] for d in range(4)]
rows=[]
for d in range(1,4):
    index={m:i for i,m in enumerate(s_by_dim[d-1])}
    rows.append([{index[s]:c for s,c in boundary(m).items()}
                 for m in s_by_dim[d]])
for p in (2,3,5):
    r1,r2,r3=[rank_modp(z,p) for z in rows]
    betti=(len(s_by_dim[0])-1-r1,len(s_by_dim[1])-r1-r2,
           len(s_by_dim[2])-r2-r3,len(s_by_dim[3])-r3)
    assert betti==(0,0,0,20)
    print('mod',p,'boundary_ranks',(r1,r2,r3),'reduced_betti',betti)

# Group generated by two automorphisms of the graph.
def compose(p,q):return tuple(p[q[i]] for i in range(N))
G={E}; queue=deque([E])
for g in GENS:
    assert sorted(g)==list(range(N))
    assert all((A[g[i]]>>g[j]&1)==(A[i]>>j&1) for i in range(N) for j in range(N))
while queue:
    x=queue.popleft()
    for y in GENS:
        z=compose(x,y)
        if z not in G:G.add(z);queue.append(z)
P=sorted(G)
assert len(P)==120
P_index={p:i for i,p in enumerate(P)};identity=P_index[E]
product=[[P_index[compose(p,q)] for q in P] for p in P]
inverse=[next(j for j in range(120) if product[i][j]==identity) for i in range(120)]
central=[i for i in range(120) if all(product[i][j]==product[j][i] for j in range(120))]
assert len(central)==2
Z=next(i for i in central if i!=identity)
comms={product[product[product[a][b]][inverse[a]]][inverse[b]]
       for a in range(120) for b in range(120)}
assert len(comms)==60 and Z not in comms
assert all(product[a][b] in comms for a in comms for b in comms)
rotation=comms

def order(g):
    a=identity
    for k in range(1,121):
        a=product[a][g]
        if a==identity:return k
    raise AssertionError('bad order')
orders=[order(g) for g in range(120)]

def orientation(g,m):
    ix=[i for i in range(N) if m>>i&1]
    image=[P[g][i] for i in ix]
    if set(ix)!=set(image): return 0
    q=[ix.index(v) for v in image]
    swaps=sum(q[i]>q[j] for i in range(len(q)) for j in range(i+1,len(q)))
    return -1 if swaps%2 else 1

def char(g):
    # Only nonzero reduced homology is in dimension three.
    reduced_euler=-1 + sum(((-1)**(m.bit_count()-1))*orientation(g,m) for m in F)
    return -reduced_euler
CH=[char(g) for g in range(120)]
assert CH[identity]==20 and CH[Z]==10
assert sum(CH)==120 # invariant multiplicity one
assert all(CH[product[product[h][g]][inverse[h]]]==CH[g]
           for g in range(120) for h in range(120))
classes=[];not_seen=set(rotation)
while not_seen:
    x=min(not_seen)
    cls={product[product[h][x]][inverse[h]] for h in rotation}
    not_seen-=cls
    classes.append(cls)
classes.sort(key=lambda x:(orders[next(iter(x))],min(x)))
assert [(len(c),orders[next(iter(c))]) for c in classes]==[(1,1),(15,2),(20,3),(12,5),(12,5)]
char_even=[];char_odd=[]
for c in classes:
    g=next(iter(c))
    assert all(CH[h]==CH[g] for h in c)
    assert (CH[g]+CH[product[Z][g]])%2==0
    char_even.append((CH[g]+CH[product[Z][g]])//2)
    char_odd.append((CH[g]-CH[product[Z][g]])//2)
assert char_even==[15,3,0,0,0]
assert char_odd==[5,1,-1,0,0]
print('full_group_size',len(P),'central_inversion_character',CH[Z])
print('rotation_classes_sizes',[len(c) for c in classes])
print('rotation_classes_orders',[orders[next(iter(c))] for c in classes])
print('central_even_character',char_even,'central_odd_character',char_odd)
# Rational character table inner products; 5A and 5B traces vanish,
# so two irrational 3-dimensional characters have the same integer multiplicity.
def mults(t):
    a,b,c,d,e=t
    nums=[a+15*b+20*c+12*d+12*e, 3*a-15*b,
          3*a-15*b,4*a+20*c-12*d-12*e,5*a+15*b-20*c]
    assert all(x%60==0 for x in nums)
    return tuple(x//60 for x in nums)
assert mults(char_even)==(1,0,0,1,2)
assert mults(char_odd)==(0,0,0,0,1)
print('A5_irrep_order',('1','3','3prime','4','5'))
print('central_even_irrep_multiplicities',mults(char_even))
print('central_odd_irrep_multiplicities',mults(char_odd))
print('full_group_invariant_rank',sum(CH)//120)
print('ALL_CHECKS_PASS')
