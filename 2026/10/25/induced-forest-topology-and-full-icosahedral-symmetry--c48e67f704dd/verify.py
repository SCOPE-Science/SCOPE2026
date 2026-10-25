#!/usr/bin/env python3
"""Exact finite certificate for the induced-forest complex of the icosahedral graph.

Python 3 standard library only. It checks all graph vertex subsets, the full
Morse matching and its acyclicity, modular boundary ranks, and all 120 signed
Lefschetz characters. Mathematical interpretation is in RESULT.md.
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction

N = 12
EDGES = ((0,1),(0,5),(0,7),(0,8),(0,11),(1,2),(1,5),(1,6),(1,8),
         (2,3),(2,6),(2,8),(2,9),(3,4),(3,6),(3,9),(3,10),
         (4,5),(4,6),(4,10),(4,11),(5,6),(5,11),(7,8),(7,9),
         (7,10),(7,11),(8,9),(9,10),(10,11))
ROT5 = (0,8,9,3,6,1,2,11,7,10,4,5)
ROT3 = (5,0,7,9,2,1,8,4,11,10,3,6)
ANTIPODE = (3,10,11,0,8,9,7,6,4,5,1,2)
IDENTITY = tuple(range(N))
ADJ = [0]*N
for u,v in EDGES:
    ADJ[u] |= (1<<v)
    ADJ[v] |= (1<<u)
assert len(EDGES) == 30 and all(x.bit_count()==5 for x in ADJ)

def forest_union_find(mask):
    parent = list(range(N))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for u,v in EDGES:
        if ((mask>>u)&1) and ((mask>>v)&1):
            ru,rv = root(u),root(v)
            if ru == rv:
                return False
            parent[ru] = rv
    return True

def forest_dfs(mask):
    reached = 0
    for v in range(N):
        if not ((mask>>v)&1) or ((reached>>v)&1):
            continue
        reached |= (1<<v)
        stack = [(v,-1)]
        while stack:
            at,old = stack.pop()
            nexts = ADJ[at] & mask
            for j in range(N):
                if (nexts>>j)&1 and j!=old:
                    if (reached>>j)&1:
                        return False
                    reached |= (1<<j)
                    stack.append((j,at))
    return True

F = set()
for mask in range(1<<N):
    valid = forest_union_find(mask)
    assert valid == forest_dfs(mask), (mask,valid)
    if valid: F.add(mask)
assert len(F)==984
assert [sum(m.bit_count()==k for m in F) for k in range(7)] == [1,12,66,200,345,300,60]
assert not any(m.bit_count()>6 for m in F)
max_facets = Counter(m.bit_count() for m in F if all((m | (1<<j)) not in F for j in range(N) if not ((m>>j)&1)))
assert max_facets=={5:60,6:60}

# Each face is paired at most once by the lexicographic first valid toggle.
remaining=set(F)
matching=[]
for vertex in range(N):
    for low in sorted(remaining):
        high=low|(1<<vertex)
        if not ((low>>vertex)&1) and high in remaining:
            remaining.remove(low)
            remaining.remove(high)
            matching.append((low,high))
assert len(matching)==472 and Counter(m.bit_count()-1 for m in remaining)=={4:40}
assert (0,1) in matching

# Reverse matching Hasse arrows; all other Hasse arrows go downward.
M=set(matching)
indegree={m:0 for m in F}
arrows={m:[] for m in F}
incidences=0
for high in F:
    if high==0:continue
    for j in range(N):
        if not ((high>>j)&1): continue
        low=high^(1<<j)
        assert low in F
        if (low,high) in M:
            start,end=low,high
        else:
            start,end=high,low
        arrows[start].append(end)
        indegree[end]+=1
        incidences+=1
q=deque(x for x,v in indegree.items() if v==0)
visited=0
while q:
    u=q.popleft();visited+=1
    for v in arrows[u]:
        indegree[v]-=1
        if indegree[v]==0:q.append(v)
assert visited==len(F) and incidences==3984

# Independent reduced simplicial homology over two different primes.
def rank_boundary(k,prime):
    if k<=0:return 0
    cols=sorted(m for m in F if m.bit_count()==k+1)
    lows=sorted(m for m in F if m.bit_count()==k)
    index={m:i for i,m in enumerate(lows)}
    piv={}
    for face in cols:
        chain={}
        js=[j for j in range(N) if (face>>j)&1]
        for t,j in enumerate(js):chain[index[face^(1<<j)]] = (1 if t%2==0 else prime-1)
        while chain:
            r=max(chain)
            if r not in piv:
                scale=pow(chain[r],-1,prime)
                piv[r]={i:(a*scale)%prime for i,a in chain.items()}
                break
            factor=chain[r]
            for i,v in piv[r].items():
                v=(chain.get(i,0)-factor*v)%prime
                if v:chain[i]=v
                else:chain.pop(i,None)
    return len(piv)
rank_vectors={}
for p in (2,3):
    ranks=[rank_boundary(k,p) for k in range(1,6)]
    # H_0 ordinary has rank 1, H_k=C_k-rank(d_k)-rank(d_{k+1}).
    c=[sum(m.bit_count()==k+1 for m in F) for k in range(6)]
    r=[0]+ranks+[0]
    betti=[c[k]-r[k]-r[k+1] for k in range(6)]
    assert betti==[1,0,0,0,40,0],(p,ranks,betti)
    assert ranks==[11,55,145,200,60],(p,ranks)
    rank_vectors[p]=ranks

# Check icosahedron triangulation and prove automorphism-group upper bound.
TRIANGLES = [tuple(v for v in range(N) if m>>v&1) for m in range(1<<N)
             if m.bit_count()==3 and all((ADJ[u]>>v)&1 for u,v in
                                         ((i,j) for i in range(N) if m>>i&1 for j in range(i+1,N) if m>>j&1))]
assert len(TRIANGLES)==20
for u,v in EDGES:
    assert sum(u in t and v in t for t in TRIANGLES)==2
Tidx={t:i for i,t in enumerate(TRIANGLES)}
dual={i:set() for i in range(len(TRIANGLES))}
for u,v in EDGES:
    a,b=[Tidx[t] for t in TRIANGLES if u in t and v in t]
    dual[a].add(b);dual[b].add(a)
seen={0}; stack=[0]
while stack:
    for j in dual[stack.pop()]:
        if j not in seen:seen.add(j);stack.append(j)
assert len(seen)==20

# Permutation group with 60 rotational and 120 full graph automorphisms.
def compose(p,q):return tuple(p[q[i]] for i in range(N))
def group(gens):
    s={IDENTITY};todo=[IDENTITY]
    while todo:
        x=todo.pop()
        for g in gens:
            y=compose(x,g)
            if y not in s:s.add(y);todo.append(y)
    return s
def order(p):
    x=IDENTITY
    for k in range(1,121):
        x=compose(x,p)
        if x==IDENTITY:return k
    raise AssertionError('permutation order > 120')
R=group((ROT5,ROT3))
ALL=group((ROT5,ROT3,ANTIPODE))
assert len(R)==60 and len(ALL)==120 and ANTIPODE not in R
assert order(ROT5)==5 and order(ROT3)==3 and order(compose(ROT5,ROT3))==2
assert order(ANTIPODE)==2 and all(compose(ANTIPODE,r)==compose(r,ANTIPODE) for r in R)
assert all(all((ADJ[i]>>j)&1 == (ADJ[p[i]]>>p[j])&1 for i in range(N) for j in range(N)) for p in ALL)
# An automorphism is determined by a directed triangular flag: 12*5*2=120.
# The connected triangular dual ensures a fixed flag forces every face fixed.

def signed_trace(p):
    ans=-1   # reduced chain complex: empty face has dimension -1
    for face in F:
        if face==0:continue
        old=[i for i in range(N) if face>>i&1]
        new=[p[i] for i in old]
        if sorted(new)!=old:continue
        inv=sum(new[i]>new[j] for i in range(len(new)) for j in range(i+1,len(new)))
        sign=-1 if inv%2 else 1
        ans += (-1 if (len(old)-1)%2 else 1)*sign
    return ans
rotation=Counter((order(p),signed_trace(p)) for p in R)
coset=Counter((order(compose(ANTIPODE,p)),signed_trace(compose(ANTIPODE,p))) for p in R)
assert rotation=={(1,40):1,(2,-4):15,(3,1):20,(5,0):24},rotation
assert coset=={(2,-10):1,(2,2):15,(6,-1):20,(10,0):24},coset

# Rational A5 characters, indexed by element orders 1,2,3,5.
CHAR = {'trivial':(1,1,1,1),'four':(4,0,1,-1),
        'five':(5,1,-1,0),'six':(6,-2,0,1)}
# The six-dimensional rational character combines the Galois-conjugate 3s,
# so its squared complex-character norm is two; the others have norm one.
WEIGHTS=(1,15,20,24)
def multiplicities(target):
    result={}
    for name,ch in CHAR.items():
        numerator=sum(w*x*y for w,x,y in zip(WEIGHTS,target,ch))
        denominator=60*(2 if name=='six' else 1)
        assert numerator%denominator==0,(name,numerator,denominator)
        result[name]=numerator//denominator
    assert all(x>=0 for x in result.values())
    return result
# Split by antipodal eigenvalues using half-sums of traces.
rot=(40,-4,1,0)
anti=(-10,2,-1,0)
even=tuple((x+y)//2 for x,y in zip(rot,anti))
odd=tuple((x-y)//2 for x,y in zip(rot,anti))
assert even==(15,-1,0,0) and odd==(25,-3,1,0)
assert multiplicities(even)=={'trivial':0,'four':1,'five':1,'six':1}
assert multiplicities(odd)=={'trivial':0,'four':2,'five':1,'six':2}
print('faces=984 f_vector=[12,66,200,345,300,60] maximal_faces=(size5:60,size6:60)')
print('acyclic_matching=472 critical=(dimension4:40) Hasse_incidences=3984')
print('boundary_ranks_mod_2_3=[11,55,145,200,60] reduced_H4=40 other_reduced_betti=0')
print('aut_order=120 A5_order=60 antipode_trace=-10')
print('rotation_order_trace=', sorted(rotation.items()))
print('antipodal_coset_order_trace=', sorted(coset.items()))
print('antipodal_even=[4]+[5]+[6] antipodal_odd=2[4]+[5]+2[6]')
print('VERIFY_OK')
