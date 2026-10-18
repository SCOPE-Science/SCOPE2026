"""Reproducible integral discrete-Morse computation for the icosahedral 4-cut complex.

Requires Python 3 and SymPy. No external data. See RESULT.md for mathematical proof.
"""
import itertools
from collections import Counter
from functools import lru_cache
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

N=12
E=set()
def edge(a,b): E.add(tuple(sorted((a,b))))
for j in range(5):
    top=1+j;bot=6+j
    edge(0,top);edge(11,bot)
    edge(top,1+(j+1)%5);edge(bot,6+(j+1)%5)
    edge(top,bot);edge(top,6+(j-1)%5)
assert len(E)==30
adj=[0]*N
for a,b in E: adj[a]|=1<<b;adj[b]|=1<<a
assert all(x.bit_count()==5 for x in adj)
def disconnected(s):
    reached=s&-s
    while True:
        nxt=reached
        for j in range(N):
            if (reached>>j)&1: nxt |= adj[j]&s
        if nxt==reached: return reached!=s
        reached=nxt
facets=[((1<<N)-1)^sum(1<<i for i in tup)
        for tup in itertools.combinations(range(N),4)
        if disconnected(sum(1<<i for i in tup))]
assert len(facets)==285
faces=set()
for facet in facets:
    sub=facet
    while sub:
        faces.add(sub);sub=(sub-1)&facet
assert Counter(m.bit_count()-1 for m in faces)==dict(enumerate([12,66,220,495,792,912,720,285]))
permutation=[10,1,6,0,11,9,2,4,7,3,8,5]
alive=set(faces);matched={}
for v in permutation:
    for lo in sorted(alive):
        hi=lo|(1<<v)
        if not (lo&(1<<v)) and hi in alive:
            alive.remove(lo);alive.remove(hi);matched[lo]=hi
critical=set(alive)
assert Counter(x.bit_count()-1 for x in critical)=={0:1,6:6,7:21}
# Check absence of oriented gradient cycles by topological sorting.
indeg={m:0 for m in faces};arcs={m:[] for m in faces}
def boundary(m):
    vs=[i for i in range(N) if m&(1<<i)]
    return [(m^(1<<v),(-1)**k) for k,v in enumerate(vs)]
for m in faces:
    for lo,_ in boundary(m):
        if lo not in faces:continue
        a,b=(lo,m) if matched.get(lo)==m else (m,lo)
        arcs[a].append(b);indeg[b]+=1
stack=[m for m,v in indeg.items() if not v];reached=0
while stack:
    a=stack.pop();reached+=1
    for b in arcs[a]:
        indeg[b]-=1
        if indeg[b]==0:stack.append(b)
assert reached==len(faces)
uppers=set(matched.values())
@lru_cache(None)
def project(m):
    if m in critical:return {m:1}
    if m in uppers:return {}
    top=matched[m]
    pivot=dict(boundary(top))[m]
    result={}
    for facet,sgn in boundary(top):
        if facet==m:continue
        for c,k in project(facet).items():result[c]=result.get(c,0)-pivot*sgn*k
    return {c:k for c,k in result.items() if k}
c6=sorted(x for x in critical if x.bit_count()==7)
c7=sorted(x for x in critical if x.bit_count()==8)
idx={c:j for j,c in enumerate(c6)}
mat=[[0]*len(c7) for _ in c6]
for j,s in enumerate(c7):
    for f,sgn in boundary(s):
        for c,k in project(f).items():
            if c in idx:mat[idx[c]][j]+=sgn*k
D=smith_normal_form(Matrix(mat),domain=ZZ)
diagonal=[abs(int(D[i,i])) for i in range(min(D.shape))]
assert diagonal==[1,0,0,0,0,0]
assert sum(bool(a) for row in mat for a in row)==4
print('edges',len(E),'facets',len(facets),'faces',len(faces))
print('face vector',[sum(m.bit_count()==d+1 for m in faces) for d in range(8)])
print('acyclic matching critical',dict(sorted(Counter(m.bit_count()-1 for m in critical).items())))
print('Morse boundary SNF',diagonal)
print('homotopy: wedge 5 S^6 and 20 S^7')
