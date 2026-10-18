#!/usr/bin/env python3
"""Reconstruct the Petersen five-cut complex, an acyclic Morse matching,
and its signed integral Morse boundary using exact arithmetic.
Python 3 standard library only; run from the containing directory.
"""
import itertools
import json
from collections import Counter, defaultdict, deque
from fractions import Fraction

N=10
vertices=list(itertools.combinations(range(5),2))
adjacency=[sum(1<<j for j,b in enumerate(vertices)
               if i!=j and set(a).isdisjoint(b)) for i,a in enumerate(vertices)]
def connected(S):
    seen=S&-S
    while True:
        new=seen
        for i in range(N):
            if seen>>i&1: new|=S&adjacency[i]
        if new==seen: return seen==S
        seen=new

facets=[]
for z in itertools.combinations(range(N),5):
    S=sum(1<<i for i in z)
    if not connected(S): facets.append(((1<<N)-1)^S)
faces=set()
for facet in facets:
    part=facet
    while part:
        faces.add(part)
        part=(part-1)&facet
assert len(facets)==120 and len(faces)==495
assert [sum(x.bit_count()==k for x in faces) for k in range(1,6)]==[10,45,120,200,120]

# Greedy vertex toggling, then verify acyclicity of the FULL Hasse digraph.
remaining=set(faces)
pairs=[]
for v in range(N):
    for low in sorted(remaining,key=lambda x:(x.bit_count(),x)):
        high=low|(1<<v)
        if not low>>v&1 and low in remaining and high in remaining:
            remaining.remove(low);remaining.remove(high)
            pairs.append((low,high))
assert len(pairs)==237
assert Counter(x.bit_count()-1 for x in remaining)=={0:1,3:8,4:12}
pairset=set(pairs)
digraph=defaultdict(list)
indegree={cell:0 for cell in faces}
edge_count=0
for high in faces:
    for i in range(N):
        if high>>i&1 and high.bit_count()>1:
            low=high^(1<<i)
            src,dest=(low,high) if (low,high) in pairset else (high,low)
            digraph[src].append(dest)
            indegree[dest]+=1
            edge_count+=1
queue=deque(k for k,v in indegree.items() if v==0)
visited=0
while queue:
    u=queue.popleft();visited+=1
    for v in digraph[u]:
        indegree[v]-=1
        if indegree[v]==0:queue.append(v)
assert visited==495 and edge_count==1850

# Signed simplicial boundary with the increasing vertex orientation.
boundary={cell:{cell^(1<<i):((-1)**(cell&((1<<i)-1)).bit_count())
                 for i in range(N) if cell>>i&1 and cell.bit_count()>1}
          for cell in faces}
active=set(faces)
not_cancelled=set(pairs)
# Eliminate each matched invertible two-term pair over the integers.
# Every chosen pivot is literally +1 or -1, not merely rationally invertible.
while not_cancelled:
    good=[p for p in not_cancelled if boundary[p[1]].get(p[0],0) in (-1,1)]
    assert good, "No unit Morse pivot available"
    low,high=max(good,key=pairs.index)
    sign=boundary[high][low]
    for cell in list(active):
        if cell!=high and cell.bit_count()==high.bit_count():
            a=boundary[cell].get(low,0)
            if a:
                for f,b in boundary[high].items():
                    if f!=low:
                        new=boundary[cell].get(f,0)-a*sign*b
                        if new: boundary[cell][f]=new
                        else:boundary[cell].pop(f,None)
                boundary[cell].pop(low,None)
    for cell in list(active):
        if cell.bit_count()==high.bit_count()+1:
            boundary[cell].pop(high,None)
    del boundary[low];del boundary[high]
    active.remove(low);active.remove(high)
    not_cancelled.remove((low,high))
assert active==remaining
C3=sorted(x for x in active if x.bit_count()==4)
C4=sorted(x for x in active if x.bit_count()==5)
M=[[boundary[c].get(r,0) for c in C4] for r in C3]
assert all(not boundary[c] for c in active if c.bit_count()<5)

# Exact rank via the field of fractions.
def rank(matrix):
    a=[[Fraction(z) for z in row] for row in matrix]
    pivot=0
    for c in range(len(a[0])):
        j=next((j for j in range(pivot,len(a)) if a[j][c]),None)
        if j is None:continue
        a[j],a[pivot]=a[pivot],a[j]
        b=a[pivot][c]
        a[pivot]=[t/b for t in a[pivot]]
        for k in range(len(a)):
            if k!=pivot and a[k][c]:
                coeff=a[k][c]
                a[k]=[x-coeff*y for x,y in zip(a[k],a[pivot])]
        pivot+=1
        if pivot==len(a):break
    return pivot

def determinant(x):
    # Small exact rational elimination; determinant is checked to be integer.
    a=[[Fraction(z) for z in row] for row in x]
    n=len(a);sgn=1;det=Fraction(1)
    for i in range(n):
        j=next((j for j in range(i,n) if a[j][i]),None)
        if j is None:return 0
        if j!=i:a[i],a[j]=a[j],a[i];sgn=-sgn
        z=a[i][i];det*=z
        for j in range(i+1,n):
            c=a[j][i]/z
            for k in range(i,n):a[j][k]-=c*a[i][k]
    out=det*sgn
    assert out.denominator==1
    return int(out)
assert rank(M)==7
rows=(0,1,2,3,4,5,6);cols=(3,4,5,7,8,9,10)
assert determinant([[M[i][j] for j in cols] for i in rows])==1
# A rank-seven matrix with a unimodular rank-seven minor has Smith invariants seven ones.
certificate=json.load(open('morse_certificate.json',encoding='utf-8'))
assert certificate=={'vertices': [list(a) for a in vertices],
                     'face_counts':[10,45,120,200,120],
                     'facet_count':120,'faces':495,'matching_pairs':237,
                     'hasse_edges':1850,'critical_3':C3,'critical_4':C4,
                     'morse_d4':M,'minor_rows':list(rows),'minor_cols':list(cols),
                     'minor_det':1,'rank':7}
print(json.dumps({'facets':120,'faces':495,'matching_pairs':237,
 'acyclic_hasse_nodes':visited,'critical_cells':{'0':1,'3':8,'4':12},
 'morse_d4_rank':7,'unimodular_rank_seven_minor':1,
 'reduced_homology':{'3':'Z','4':'Z^5'},
 'homotopy_type':'S^3 wedge (5 copies of S^4)'}))
