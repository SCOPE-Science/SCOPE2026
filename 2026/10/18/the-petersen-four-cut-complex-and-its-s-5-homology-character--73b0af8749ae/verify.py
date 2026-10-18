"""Exact standalone certificate for the Petersen ordinary four-cut complex.
Run: python3 verify.py. Python >=3.9, no third-party dependencies.
"""
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial

PAIRS=list(combinations(range(5),2))
INDEX={v:i for i,v in enumerate(PAIRS)}
N=10
ADJ=[[0]*N for _ in range(N)]
for i,j in combinations(range(N),2):
    if set(PAIRS[i]).isdisjoint(PAIRS[j]):
        ADJ[i][j]=ADJ[j][i]=1

def connected(nodes):
    seen={nodes[0]}; queue=[nodes[0]]
    for x in queue:
        for y in nodes:
            if y not in seen and ADJ[x][y]:
                seen.add(y);queue.append(y)
    return len(seen)==len(nodes)

facets={((1<<N)-1)^sum(1<<v for v in quad)
        for quad in combinations(range(N),4) if not connected(quad)}
assert len(facets)==140
faces={0}
for facet in facets:
    sub=facet
    while sub:
        faces.add(sub)
        sub=(sub-1)&facet
assert len(faces)==766
assert [sum(x.bit_count()==d for x in faces) for d in range(7)]==[1,10,45,120,210,240,140]
assert all(f.bit_count()==6 for f in facets)

# Lexicographic staged matching, selecting only presently unmatched nonempty faces.
unmatched=faces-{0}
matched={}
for vertex in range(N):
    for low in sorted(unmatched):
        if not (low>>vertex)&1:
            high=low|(1<<vertex)
            if high in unmatched:
                matched[low]=high
    for low,high in list(matched.items()):
        # Remove only pairs created in this stage; the previous pairs are absent.
        if low in unmatched:
            unmatched.remove(low);unmatched.remove(high)
assert len(matched)==(765-27)//2
assert Counter(x.bit_count()-1 for x in unmatched)==Counter({0:1,5:26})

# Verify entire directed Hasse graph of nonempty faces is acyclic:
# matched covering edges low -> high, all other covering edges high -> low.
vertex_faces=faces-{0}
edges_out={f:[] for f in vertex_faces}
indegree={f:0 for f in vertex_faces}
for high in vertex_faces:
    for v in range(N):
        if (high>>v)&1:
            low=high^(1<<v)
            if low==0:continue
            if matched.get(low)==high: a,b=low,high
            else: a,b=high,low
            edges_out[a].append(b);indegree[b]+=1
queue=deque(v for v in vertex_faces if indegree[v]==0)
visited=0
while queue:
    u=queue.popleft();visited+=1
    for v in edges_out[u]:
        indegree[v]-=1
        if indegree[v]==0:queue.append(v)
assert visited==len(vertex_faces), ('Cyclic discrete Morse matching',visited)

# Independent mod-two boundary-rank check. It is not needed for the
# homotopy theorem, but triangulation and matching provide distinct checks.
levels=[[f for f in faces if f.bit_count()==s] for s in range(7)]
levels=[sorted(arr) for arr in levels]

def f2rank(rows):
    pivots={}
    for row in rows:
        while row:
            p=row.bit_length()-1
            if p not in pivots:
                pivots[p]=row;break
            row^=pivots[p]
    return len(pivots)

ranks={}
for d in range(1,6):
    targets={f:i for i,f in enumerate(levels[d])}
    columns=[]
    for high in levels[d+1]:
        mask=0
        for bit in range(N):
            if (high>>bit)&1:
                mask^=1<<targets[high^(1<<bit)]
        columns.append(mask)
    ranks[d]=f2rank(columns)
assert ranks=={1:9,2:36,3:84,4:126,5:114},ranks

EXPECTED={(1,1,1,1,1):26,(2,1,1,1):6,(2,2,1):-2,
          (3,1,1):2,(3,2):0,(4,1):0,(5,):1}
SIZES={(1,1,1,1,1):1,(2,1,1,1):10,(2,2,1):15,
       (3,1,1):20,(3,2):20,(4,1):30,(5,):24}

def cycle_type(p):
    seen=set();lengths=[]
    for i in range(5):
        if i in seen:continue
        x=i;ell=0
        while x not in seen:
            seen.add(x);ell+=1;x=p[x]
        lengths.append(ell)
    return tuple(sorted(lengths,reverse=True))

def eval_character(p):
    p10=[INDEX[tuple(sorted((p[a],p[b])))] for a,b in PAIRS]
    trace=0
    for mask in faces:
        verts=[i for i in range(N) if (mask>>i)&1]
        images=[p10[v] for v in verts]
        if sum(1<<x for x in images)!=mask:continue
        inversions=sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))
        trace+=(-1)**(len(verts)+inversions)
    return trace

def irred_character(p):
    fix=sum(p[i]==i for i in range(5))
    trans=sum(tuple(sorted((p[a],p[b])))==(a,b) for a,b in PAIRS)
    std=fix-1
    two=trans-fix # 2-subset module = triv + standard + (3,2)
    squared=[p[p[i]] for i in range(5)]
    ext=(std*std-(sum(squared[i]==i for i in range(5))-1))//2
    sign=(-1)**(5-len(cycle_type(p)))
    # Order (5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1),(1^5).
    return (1,std,two,ext,sign*two,sign*std,sign)

classes=Counter()
inner=[0]*7
for perm in permutations(range(5)):
    typ=cycle_type(perm)
    classes[typ]+=1
    top_trace=eval_character(perm)
    assert top_trace==EXPECTED[typ], (perm,typ,top_trace)
    irr=irred_character(perm)
    for i in range(7):inner[i]+=top_trace*irr[i]
assert classes==Counter(SIZES),classes
assert [Fraction(x,120) for x in inner]==[1,2,1,2,0,0,0]
print('VERIFY_OK facets=140 faces=766 matching_pairs=369 critical_0=1 critical_5=26')
print('VERIFY_OK acyclic_hasse_vertices=765 all_S5_elements=120 mod2_boundary_ranks='+str(ranks))
