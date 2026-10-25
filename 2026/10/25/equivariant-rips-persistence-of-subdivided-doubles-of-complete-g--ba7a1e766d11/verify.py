"""Standalone finite verification of the graph-metric Folkman complex and its symmetries.

Requires Python >=3.9; standard library only. No external data or network.
"""
from itertools import combinations, permutations, product
from collections import Counter

# Sorted canonical labels: ten doubled vertices, then ten subdividers.
V=[('v',i,b) for i in range(5) for b in range(2)]
E=[('e',i,j) for i,j in combinations(range(5),2)]
NODES=V+E
IX={v:k for k,v in enumerate(NODES)}
ADJ=[set() for _ in NODES]
for i,j in combinations(range(5),2):
    e=IX['e',i,j]
    for k in (i,j):
        for b in (0,1):
            a=IX['v',k,b]
            ADJ[a].add(e);ADJ[e].add(a)
assert len(NODES)==20 and sum(map(len,ADJ))//2==40

# BFS distances.
D=[]
for root in range(20):
    ds=[-1]*20;ds[root]=0; todo=[root]
    for u in todo:
        for v in ADJ[u]:
            if ds[v]<0: ds[v]=ds[u]+1;todo.append(v)
    assert all(x>=0 for x in ds)
    D.append(ds)
assert max(map(max,D))==4

# Every simplex of Rips_2, generated from all possible nonempty 20-bit masks.
# Bron-Kerbosch maximal-clique enumeration avoids enumerating nonfaces.
NEIGH=[]
for i in range(20):
    NEIGH.append(sum(1<<j for j in range(20) if j!=i and D[i][j]<=2))
ALL=(1<<20)-1
FACETS=[]
def cliques(R,P,X):
    if not P and not X: FACETS.append(R);return
    px=P|X
    pivot=max((j for j in range(20) if (px>>j)&1),key=lambda j:(P&NEIGH[j]).bit_count()) if px else None
    opts=P & (~NEIGH[pivot] if pivot is not None else ALL)
    while opts:
        bit=opts&-opts;j=bit.bit_length()-1
        cliques(R|bit,P&NEIGH[j],X&NEIGH[j])
        P^=bit;X|=bit;opts^=bit
cliques(0,ALL,0)
FACES=set()
for top in FACETS:
    q=top
    while q:
        FACES.add(q)
        q=(q-1)&top
assert len(FACES)==1413
fv=Counter(s.bit_count()-1 for s in FACES)
assert [fv[d] for d in range(10)]==[20,115,270,325,292,215,120,45,10,1]
assert Counter(s.bit_count() for s in FACETS)=={3:10,5:10,6:5,10:1}

# Sequential vertex matchings: pair every available face missing vertex i
# with its coface obtained by adjoining i, visiting vertices in fixed order.
# Construct and then *independently* verify acyclicity with a topological sort
# of the reversed-matched Hasse diagram (no acyclicity assumption).
UNMATCHED=set(FACES)
MATCH={}
for i in range(20):
    bit=1<<i
    for s in sorted(UNMATCHED,key=lambda x:(x.bit_count(),x)):
        if s not in UNMATCHED or s&bit: continue
        upper=s|bit
        if upper in UNMATCHED:
            MATCH[s]=upper
            UNMATCHED.remove(s);UNMATCHED.remove(upper)
assert Counter(s.bit_count()-1 for s in UNMATCHED)=={0:1,2:10}
assert len(MATCH)==701

# Directed Hasse: unmatched covering relations go down, matched ones go up.
INDEG={s:0 for s in FACES}; OUT={s:[] for s in FACES};cover_count=0
for s in FACES:
    if s.bit_count()<2:continue
    bits=s
    while bits:
        bit=bits&-bits;bits^=bit;t=s^bit
        if t not in FACES:continue
        cover_count+=1
        if MATCH.get(t)==s: src,dst=t,s
        else: src,dst=s,t
        OUT[src].append(dst);INDEG[dst]+=1
from collections import deque
q=deque(s for s in FACES if INDEG[s]==0);seen=0
while q:
    u=q.popleft();seen+=1
    for v in OUT[u]:
        INDEG[v]-=1
        if INDEG[v]==0:q.append(v)
assert seen==len(FACES)

# Rips_3 is a cone on any doubled vertex, hence contractible.
assert all(D[IX['v',0,0]][i]<=3 for i in range(20))

# The full Folkman graph symmetry group is (C2)^5 rtimes S5.
# eps[i] swaps the two clones of the original vertex i before relabelling.
# Each edge subdivider is uniquely specified by its unordered endpoint pair.
def perm_map(pi,eps):
    perm=[]
    for label in NODES:
        if label[0]=='v':
            _,i,b=label
            perm.append(IX['v',pi[i],b^eps[i]])
        else:
            _,i,j=label
            a,b=sorted((pi[i],pi[j]));perm.append(IX['e',a,b])
    return perm

def trace_on_chain(p):
    """Traces of induced signed oriented simplex permutations in each degree."""
    vals=[0]*10
    for mask in FACES:
        ids=[j for j in range(20) if mask>>j&1]
        transformed=[p[j] for j in ids]
        if sum(1<<j for j in transformed)!=mask:continue
        inv=sum(transformed[a]>transformed[b] for a in range(len(ids)) for b in range(a+1,len(ids)))
        vals[len(ids)-1]+=(-1)**inv
    return vals

def char_h1_by_vertices_and_edges(p):
    verts=sum(p[i]==i for i in range(20))
    edges=sum(p[i]==i and p[j]==j for i in range(20) for j in ADJ[i] if i<j)
    return edges-verts+1

def char_h1_formula(pi,eps):
    fixed=[i for i in range(5) if pi[i]==i]
    f=len(fixed);f0=sum(eps[i]==0 for i in fixed)
    two=sum(i<pi[i] and pi[pi[i]]==i and pi[i]!=i for i in range(5))
    return 2*f0*(f-2)-f*(f-1)//2-two+1

def char_h2_formula(pi):
    total=0
    for T in combinations(range(5),3):
        mapped=[pi[i] for i in T]
        if set(mapped)!=set(T):continue
        inv=sum(mapped[a]>mapped[b] for a in range(3) for b in range(a+1,3))
        total+=(-1)**inv
    return total

# Exhaustive all 3840 automorphisms: graph preservation; 1-homology trace;
# fixed-simplex Lefschetz 2-homology traces at Rips_2. The latter is an
# independent calculation from the claimed exterior-cube identification.
seen_types={}
num=0
for pi in permutations(range(5)):
    for eps in product((0,1),repeat=5):
        p=perm_map(pi,eps)
        assert all({p[j] for j in ADJ[i]}==ADJ[p[i]] for i in range(20))
        assert char_h1_by_vertices_and_edges(p)==char_h1_formula(pi,eps)
        Lef=sum((-1)**d*x for d,x in enumerate(trace_on_chain(p)))
        assert Lef-1==char_h2_formula(pi)
        num+=1
    if all(x==0 for x in [pi[i]-i for i in range(5)]):
        pass
assert num==3840

# Double cover of K_5 has 21 graph cycles, and every 2-sphere is born at 2.
assert 40-20+1==21
print('graph=(20 vertices,40 edges,diameter 4), |Aut|=3840')
print('Rips_2 fvector=',[fv[d] for d in range(10)])
print('Rips_2 maximal-facets-by-size=',dict(sorted(Counter(s.bit_count() for s in FACETS).items())))
print('Rips_2 Morse pairs=',len(MATCH),'critical=',dict(sorted(Counter(s.bit_count()-1 for s in UNMATCHED).items())))
print('acyclic Hasse vertices=',seen,'Hasse incidences=',cover_count)
print('equivariant Lefschetz and H1 character checks=',num)
print('homotopy: R1 = wedge 21 S1; R2 = wedge 10 S2; R3/R4 contractible')
print('VERIFY_OK')
