#!/usr/bin/env python3
from itertools import product, combinations
from collections import defaultdict

# Petersen graph: outer 5-cycle 0..4, spokes i--(5+i), inner star 5+i -- 5+(i+2 mod 5).
n=10
adj=[set() for _ in range(n)]
edges=set()
def add(a,b):
    if a>b: a,b=b,a
    edges.add((a,b)); adj[a].add(b); adj[b].add(a)
for i in range(5):
    add(i,(i+1)%5)
    add(i,5+i)
    add(5+i,5+((i+2)%5))
edges=sorted(edges)
assert len(edges)==15 and all(len(adj[v])==3 for v in range(n))

oriented=[]; oid={}
for a,b in edges:
    for t,h in ((a,b),(b,a)):
        oid[(t,h)]=len(oriented); oriented.append((t,h))
assert len(oriented)==30

# A face is an acyclic matching on the graph Hasse diagram. For a graph this is
# equivalently a partial orientation with outdegree <=1 at every vertex, no edge
# used from both ends, and no directed cycle.
faces=[]
byk=defaultdict(list)
for choices in product(*[[-1]+sorted(adj[v]) for v in range(n)]):
    ok=True
    for v,w in enumerate(choices):
        if w!=-1 and choices[w]==v:
            ok=False; break
    if not ok:
        continue
    for s in range(n):
        seen=set(); x=s
        while choices[x]!=-1:
            if x in seen:
                ok=False; break
            seen.add(x); x=choices[x]
        if not ok:
            break
    if not ok:
        continue
    mask=0
    for v,w in enumerate(choices):
        if w!=-1:
            mask |= 1 << oid[(v,w)]
    faces.append(mask); byk[mask.bit_count()].append(mask)

expected_counts={0:1,1:30,2:390,3:2880,4:13305,5:39882,6:77640,7:94800,8:66000,9:20000}
counts={k:len(v) for k,v in byk.items()}
assert counts==expected_counts, (counts, expected_counts)
assert len(faces)==314928
S=set(faces)
# Closure and dimension checks.
for m in faces:
    y=m
    while y:
        b=y & -y; y-=b
        assert (m^b) in S
assert not byk.get(10)

# Independent face-count check from the matrix-forest theorem:
# det(I+xL)=sum_F x^{|E(F)|} prod_C |C|. The coefficient of x^k is exactly
# the number of rooted spanning forests with k edges, i.e. the number of faces
# with k primitive vectors.
L=[[0]*n for _ in range(n)]
for i in range(n):
    L[i][i]=len(adj[i])
    for j in adj[i]: L[i][j]=-1

def det_bareiss(A):
    A=[row[:] for row in A]
    m=len(A)
    if m==0: return 1
    sign=1; prev=1
    for k in range(m-1):
        if A[k][k]==0:
            p=next((r for r in range(k+1,m) if A[r][k]),None)
            if p is None: return 0
            A[k],A[p]=A[p],A[k]; sign=-sign
        piv=A[k][k]
        for i in range(k+1,m):
            for j in range(k+1,m):
                A[i][j]=(A[i][j]*piv-A[i][k]*A[k][j])//prev
        prev=piv
        for i in range(k+1,m): A[i][k]=0
        for j in range(k+1,m): A[k][j]=0
    return sign*A[m-1][m-1]
forest_counts={0:1}
for k in range(1,n+1):
    total=0
    for I in combinations(range(n),k):
        A=[[L[i][j] for j in I] for i in I]
        total += det_bareiss(A)
    forest_counts[k]=total
for k in range(10):
    assert forest_counts[k]==expected_counts[k], (k,forest_counts[k],expected_counts[k])
assert forest_counts[10]==0

# Mod-2 boundary ranks. Rows are (k-1)-faces and columns are k-faces, where
# k is cardinality, so this is the reduced simplicial chain complex including
# the augmentation in k=1. We stream columns to keep memory bounded.
def make_col(m, rows, k):
    if k==1: return 1
    x=0; y=m
    while y:
        b=y&-y; y-=b
        x ^= 1 << rows[m^b]
    return x

def rank_stream(k, low=False, reverse=False):
    rows=None if k==1 else {m:i for i,m in enumerate(byk[k-1])}
    seq=reversed(byk[k]) if reverse else byk[k]
    basis={}; r=0
    for m in seq:
        x=make_col(m,rows,k)
        while x:
            if low:
                b=x&-x; p=b.bit_length()-1
            else:
                p=x.bit_length()-1
            y=basis.get(p)
            if y is None:
                basis[p]=x; r+=1; break
            x ^= y
    return r

expected_ranks={1:1,2:29,3:361,4:2519,5:10786,6:29096,7:48544,8:46256,9:19706}
ranks={}
for k in range(1,10):
    r1=rank_stream(k,low=False,reverse=False)
    r2=rank_stream(k,low=True,reverse=True)
    assert r1==r2==expected_ranks[k], (k,r1,r2,expected_ranks[k])
    ranks[k]=r1

betti={}
for k in range(1,10):
    betti[k-1]=expected_counts[k]-ranks[k]-ranks.get(k+1,0)
expected_betti={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:38,8:294}
assert betti==expected_betti, (betti, expected_betti)
red_euler=sum(((-1)**(k-1))*expected_counts[k] for k in range(1,10))-1
assert red_euler==256
assert sum(((-1)**d)*b for d,b in betti.items())==256

print('PETERSEN_MORSE_VERIFY_OK')
print('face_counts_cardinality_0_to_9=', [expected_counts[k] for k in range(10)])
print('boundary_ranks_cardinality_1_to_9=', [ranks[k] for k in range(1,10)])
print('reduced_betti_dimensions_0_to_8=', [betti[d] for d in range(9)])
print('reduced_euler=', red_euler)
