"""Independent finite checks of the beautiful-cactus labelled EGF.
Run: python3 verify.py (Python 3 standard library only).
Finite verification supplements, but does not replace, the block-decomposition proof.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import factorial

N = 10

def addpoly(a,b):
    c=defaultdict(Q)
    for k,v in a.items(): c[k]+=v
    for k,v in b.items(): c[k]+=v
    return {k:v for k,v in c.items() if v}

def scalep(a,c): return {k:v*c for k,v in a.items() if v*c}
def mulpoly(a,b):
    c=defaultdict(Q)
    for (a1,a2),v in a.items():
        for (b1,b2),w in b.items(): c[(a1+b1,a2+b2)]+=v*w
    return {k:v for k,v in c.items() if v}

def zero(): return [{} for _ in range(N)]
def X():
    x=zero();x[1]={(0,0):Q(1)}
    return x

def add(a,b): return [addpoly(u,v) for u,v in zip(a,b)]
def neg(a):return [scalep(p,-1) for p in a]
def scale(a,c):return [scalep(p,c) for p in a]
def shift(a):return [{}]+a[:-1]
def mark(a,s,t):return [{(i+s,j+t):v for (i,j),v in p.items()} for p in a]
def mul(a,b):
    c=zero()
    for i in range(N):
        for j in range(N-i):
            if a[i] and b[j]:c[i+j]=addpoly(c[i+j],mulpoly(a[i],b[j]))
    return c

def exp_series(a):
    assert a[0]=={}
    e=zero();e[0]={(0,0):Q(1)}
    for n in range(1,N):
        p={}
        for k in range(1,n+1):
            p=addpoly(p,scalep(mulpoly(a[k],e[n-k]),Q(k,n)))
        e[n]=p
    return e

# EGF of a vertex-rooted cactus branch with an exterior parent block.
x=X();T=x
for _ in range(N+1):
    T2=mul(T,T);T5=mul(mul(T2,T2),T)
    even=zero();p=T5
    for j in range((N-5)//2+1):
        even=add(even,p)
        p=mul(p,T2)
    triangle=mark(add(mul(x,T),scale(mul(x,x),Q(-1,2))),1,0)
    F=add(add(T,triangle),mark(scale(even,Q(1,2)),0,1))
    nxt=shift(exp_series(F))
    if nxt==T:break
    T=nxt
R=add(T,mark(scale(shift(mul(add(T,neg(x)),add(T,neg(x)))),Q(1,2)),1,0))
series=[]
for n in range(1,N):
    d={ij:v*factorial(n-1) for ij,v in R[n].items()}
    assert all(c.denominator==1 and c>=0 for c in d.values())
    series.append({ij:int(c) for ij,c in d.items()})
assert [sum(z.values()) for z in series]==[1,1,4,28,290,3936,66472,1352632,32325372]
assert series[5][(0,1)]==60
print('EXACT_BIVARIATE_COEFFICIENTS_OK', [sum(z.values()) for z in series])

# Independently enumerate simple connected labelled graphs through six vertices
# and test the five induced forbidden patterns directly.
PATTERNS={
    'C4':(4,[(0,1),(1,2),(2,3),(3,0)]),
    'C5':(5,[(0,1),(1,2),(2,3),(3,4),(4,0)]),
    'gem':(5,[(0,1),(1,2),(2,3)]+[(4,j) for j in range(4)]),
    'net':(6,[(0,1),(1,2),(0,2),(0,3),(1,4),(2,5)]),
    'watch':(6,[(0,1),(0,2),(0,3),(1,2),(1,3),(0,4),(1,5)])
}

def iso_masks(k,edges):
    pairs=list(combinations(range(k),2));idx={e:i for i,e in enumerate(pairs)}
    masks=set()
    for p in permutations(range(k)):
        v=0
        for a,b in edges:
            aa,bb=sorted((p[a],p[b]));v|=1<<idx[(aa,bb)]
        masks.add(v)
    return masks

FORB={k:iso_masks(k,edges) for k,edges in PATTERNS.values()}
# Actually each size has several forbidden patterns: accumulate their orbits.
FORB={}
for k,edges in PATTERNS.values(): FORB.setdefault(k,set()).update(iso_masks(k,edges))

def connected(adj):
    n=len(adj);seen=1
    while True:
        more=seen
        for u in range(n):
            if seen>>u&1:more|=adj[u]
        if more==seen:break
        seen=more
    return seen==(1<<n)-1

def biconnected_blocks(adj):
    # Tarjan stack of edges; every nontrivial block must be a single edge or a cycle.
    n=len(adj);time=0;disc=[-1]*n;low=[0]*n;stack=[];blocks=[]
    def dfs(u,parent):
        nonlocal time
        disc[u]=low[u]=time;time+=1
        for v in range(n):
            if not adj[u]>>v&1:continue
            if disc[v]==-1:
                stack.append((u,v));dfs(v,u);low[u]=min(low[u],low[v])
                if low[v]>=disc[u]:
                    block=[]
                    while True:
                        e=stack.pop();block.append(e)
                        if e==(u,v):break
                    blocks.append(block)
            elif v!=parent and disc[v]<disc[u]:
                low[u]=min(low[u],disc[v]);stack.append((u,v))
    dfs(0,-1)
    return blocks

def cactus_cycle_profile(adj):
    if not connected(adj):return None
    tri=even=0
    for edges in biconnected_blocks(adj):
        if len(edges)==1:continue
        vertices={v for a,b in edges for v in (a,b)}
        deg={v:0 for v in vertices}
        for a,b in edges:deg[a]+=1;deg[b]+=1
        if len(edges)!=len(vertices) or any(v!=2 for v in deg.values()):return None
        if len(vertices)==3:tri+=1
        elif len(vertices)%2==0 and len(vertices)>=6:even+=1
    return tri,even

def induced_forbidden(adj):
    n=len(adj)
    for k,orbits in FORB.items():
        if k>n:continue
        pairs=list(combinations(range(k),2))
        for vs in combinations(range(n),k):
            mask=0
            for p,(i,j) in enumerate(pairs):
                if adj[vs[i]]>>vs[j]&1:mask|=1<<p
            if mask in orbits:return True
    return False

for n in range(1,7):
    pairs=list(combinations(range(n),2));hist=defaultdict(int);total=0
    for mask in range(1<<len(pairs)):
        adj=[0]*n
        for idx,(u,v) in enumerate(pairs):
            if mask>>idx&1:
                adj[u]|=1<<v;adj[v]|=1<<u
        profile=cactus_cycle_profile(adj)
        if profile is None:continue
        # Independent forbidden-subgraph inspection, not the triangle-degree rule.
        if induced_forbidden(adj):continue
        hist[profile]+=1;total+=1
    assert dict(hist)==series[n-1],(n,dict(hist),series[n-1])
    print('DIRECT_CACTUS_FORBIDDEN_ENUM_OK',n,total)
print('VERIFY_OK')
