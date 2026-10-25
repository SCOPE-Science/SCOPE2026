#!/usr/bin/env python3
"""Reproduce the integral homology of the 7-by-7 toroidal queen complex.

Pure Python 3 standard library. Faces are nonattacking placements; no
external stored input, library graph implementation, or algebra package.
"""
from collections import Counter, deque
from functools import lru_cache
from math import gcd

N = 7
V = 49
ORDER = [8,5,46,36,24,47,4,17,32,19,44,37,35,7,2,34,27,3,15,10,42,6,40,13,20,18,48,16,21,38,9,30,33,0,29,26,25,45,22,31,41,12,23,11,14,39,43,28,1]
assert sorted(ORDER) == list(range(V))

def nonattacking(i, j):
    x,y=divmod(i,N); a,b=divmod(j,N)
    return x!=a and y!=b and (x-y-a+b)%N!=0 and (x+y-a-b)%N!=0

# Algebraic Paley-graph isomorphism: F49=F7[w], w*w=3,
# linear coordinate map (x,y) -> (2x+3y,2x+y).
# A nonzero field element is a square iff its norm is a square in F7.
def paley_square_diff(i,j):
    x,y=divmod(i,N); a,b=divmod(j,N)
    dx=(x-a)%N;dy=(y-b)%N
    X=(2*dx+3*dy)%N;Y=(2*dx+dy)%N
    norm=(X*X-3*Y*Y)%N
    return norm in (1,2,4)
assert all(nonattacking(i,j)==paley_square_diff(i,j)
           for i in range(V) for j in range(i+1,V))

# Enumerate every clique/queen placement exactly once by increasing labels.
neighbor=[0]*V
for i in range(V):
    for j in range(V):
        if i!=j and nonattacking(i,j):neighbor[i]|=1<<j
faces_by_size={1:[1<<i for i in range(V)]}
for k in range(2,V+1):
    nxt=[]
    for f in faces_by_size[k-1]:
        hi=f.bit_length()-1
        candidates=((1<<V)-1)^((1<<(hi+1))-1)
        for j in range(hi+1,V):
            if candidates>>j&1 and f&~neighbor[j]==0:
                nxt.append(f|(1<<j))
    if not nxt:break
    faces_by_size[k]=nxt
F=set(x for arr in faces_by_size.values() for x in arr)
expected=[49,588,2156,2450,882,196,28]
assert [len(faces_by_size.get(k,[])) for k in range(1,8)]==expected
assert len(F)==6349 and max(faces_by_size)==7
maximal=[s for s in F if not any((s|(1<<i)) in F for i in range(V) if not s>>i&1)]
assert Counter(s.bit_count() for s in maximal)=={5:294,7:28}

# Repeated element-toggle acyclic matching, with full Hasse DAG check.
rem=set(F);pairs=[]
for vertex in ORDER:
    bit=1<<vertex
    for s in sorted(rem):
        if s in rem and not s&bit and s|bit in rem:
            rem.remove(s);rem.remove(s|bit);pairs.append((s,s|bit))
assert len(pairs)==3093 and len(rem)==163
crit=Counter(x.bit_count()-1 for x in rem)
assert crit=={0:1,2:21,3:141}
matching=set(pairs)
indegree={s:0 for s in F}
adj={s:[] for s in F}
incidences=0
for face in F:
    if face.bit_count()==1:continue
    temp=face
    while temp:
        bit=temp&-temp;temp-=bit
        sub=face^bit
        if (sub,face) in matching:src,dst=sub,face
        else:src,dst=face,sub
        adj[src].append(dst);indegree[dst]+=1;incidences+=1
queue=deque(s for s in F if indegree[s]==0);visited=0
while queue:
    s=queue.popleft();visited+=1
    for t in adj[s]:
        indegree[t]-=1
        if indegree[t]==0:queue.append(t)
assert visited==len(F)

# Chain collapse: signed projection to the unmatched 2-cells.
critical2=sorted(s for s in rem if s.bit_count()==3)
critical3=sorted(s for s in rem if s.bit_count()==4)
crit_index={s:i for i,s in enumerate(critical2)}
low2={s:t for s,t in pairs if s.bit_count()==3}
upper2={t for s,t in pairs if t.bit_count()==3}
def boundary(f):
    bits=[];t=f
    while t:
        bit=t&-t;t-=bit;bits.append(bit)
    return [(f^bit, 1 if j%2==0 else -1)
            for j,bit in enumerate(bits)]
@lru_cache(None)
def proj(s):
    if s in crit_index:return {crit_index[s]:1}
    if s in upper2:return {}
    t=low2[s]
    facets=boundary(t)
    pivot_sign=next(co for face,co in facets if face==s)
    out={}
    for face,co in facets:
        if face==s:continue
        for i,val in proj(face).items():
            out[i]=out.get(i,0)-pivot_sign*co*val
    return {i:v for i,v in out.items() if v}
A=[[0]*len(critical3) for _ in critical2]
for j,t in enumerate(critical3):
    for face,sgn in boundary(t):
        for i,c in proj(face).items():A[i][j]+=sgn*c
nnz=sum(1 for row in A for x in row if x)
assert nnz==1055 and max(abs(x) for row in A for x in row)==3

# Integrity check: a standalone, fixed signed matrix digest for reproducibility.
import hashlib
matrix_text=''.join('\t'.join(map(str,row))+'\n' for row in A)
matrix_hash=hashlib.sha256(matrix_text.encode('utf-8')).hexdigest()

# Integral elementary unimodular row/column operations:
# 20 unit pivots, then a 1-by-121 row with gcd 9.
B=[row[:] for row in A];rows=len(B);cols=len(B[0]);units=0
for k in range(rows):
    pos=next(((i,j) for i in range(k,rows)
              for j in range(k,cols) if abs(B[i][j])==1),None)
    if pos is None:break
    i,j=pos
    B[i],B[k]=B[k],B[i]
    for row in B:row[j],row[k]=row[k],row[j]
    if B[k][k]==-1:B[k]=[-v for v in B[k]]
    assert B[k][k]==1
    for i in range(k+1,rows):
        c=B[i][k]
        if c:
            B[i]=[a-c*b for a,b in zip(B[i],B[k])]
    for j in range(k+1,cols):
        c=B[k][j]
        if c:
            for i in range(rows):B[i][j]-=c*B[i][k]
    units+=1
assert units==20 and rows==21 and cols==141
assert all(B[k][k]==1 and all(B[k][j]==0 for j in range(cols) if j!=k)
           for k in range(20))
assert all(B[20][k]==0 for k in range(20))
final_row=B[20][20:]
final_gcd=0
for x in final_row:final_gcd=gcd(final_gcd,abs(x))
assert final_gcd==9 and any(final_row)

# Independent simplicial boundary ranks over F2: torsion has odd order,
# so mod-two Betti numbers agree with the free integral ranks.
def gf2_rank(vecs):
    basis={}
    for x in vecs:
        while x:
            bit=x.bit_length()-1
            if bit not in basis:basis[bit]=x;break
            x^=basis[bit]
    return len(basis)
ranks={1:0}
for k in range(2,8):
    low_index={f:j for j,f in enumerate(sorted(faces_by_size[k-1]))}
    cols=[]
    for f in faces_by_size[k]:
        v=0
        for sub,_ in boundary(f):v^=1<<low_index[sub]
        cols.append(v)
    ranks[k]=gf2_rank(cols)
assert [ranks[k] for k in range(2,8)]==[48,540,1616,714,168,28]
print('VERIFY_OK')
print('PALey49_QUEENS_ISOMORPHISM 1176_PAIRS')
print('FACE_VECTOR',','.join(map(str,expected)))
print('MAXIMAL_FACES 5:294,7:28')
print('MORSE_MATCHING pairs=3093 critical0=1 critical2=21 critical3=141')
print('HASSE_ACYCLIC nodes=%d incidences=%d'%(len(F),incidences))
print('MORSE_MATRIX 21x141 nnz=%d sha256=%s'%(nnz,matrix_hash))
print('UNIMODULAR_CERTIFICATE unit_pivots=20 last_row_gcd=%d'%(final_gcd))
print('INTEGRAL_REDUCED_HOMOLOGY H2=Z/9 H3=Z^120 other=0')
print('F2_BOUNDARY_RANKS',','.join(str(ranks[k]) for k in range(2,8)))
