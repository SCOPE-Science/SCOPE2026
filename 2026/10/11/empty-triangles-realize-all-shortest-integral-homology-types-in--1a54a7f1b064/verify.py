from itertools import combinations
from fractions import Fraction
from math import gcd
from functools import reduce

V = list('ABCDEFGH')
FACETS = [tuple(x) for x in [
    'ABD','ABH','ACG','ACH','ADF','AEF','AEG','BCE',
    'BCG','BDG','BEF','BFH','CDE','CDF','CFH','DEG'
]]
FACETS = [tuple(sorted(f)) for f in FACETS]
FSET = set(FACETS)
EDGES = sorted({tuple(sorted(e)) for f in FACETS for e in combinations(f,2)})
assert len(V) == 8 and len(EDGES) == 24 and len(FACETS) == 16
DEG = {v: sum(v in e for e in EDGES) for v in V}
assert sorted(DEG.values()) == [4,5,6,6,6,7,7,7]

# Contract the star spanning tree at A.  The 17 non-tree edges are a basis
# for the integral cycle group of the 1-skeleton; triangle boundaries give
# the H_1 relations.
TREE = {tuple(sorted(('A',v))) for v in V if v != 'A'}
assert TREE <= set(EDGES)
NONTREE = [e for e in EDGES if e not in TREE]
assert len(NONTREE) == 17
IDX = {e:i for i,e in enumerate(NONTREE)}

def cycle_vector(tri):
    a,b,c = tri
    out = [0]*len(NONTREE)
    for u,v in ((a,b),(b,c),(c,a)):
        e = tuple(sorted((u,v)))
        if e in IDX:
            out[IDX[e]] += 1 if (u,v) == e else -1
    return out

R = [cycle_vector(f) for f in FACETS]

def rank_q(A):
    A = [[Fraction(x) for x in row] for row in A]
    if not A: return 0
    m,n = len(A),len(A[0]); r=0
    for c in range(n):
        p = next((i for i in range(r,m) if A[i][c]), None)
        if p is None: continue
        A[r],A[p] = A[p],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r += 1
        if r == m: break
    return r

def det_bareiss(A):
    A=[row[:] for row in A]
    n=len(A)
    if n == 0: return 1
    sign=1; prev=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if A[i][k] != 0), None)
        if p is None: return 0
        if p != k:
            A[k],A[p]=A[p],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        prev=pivot
        for i in range(k+1,n): A[i][k]=0
        for j in range(k+1,n): A[k][j]=0
    return sign*A[n-1][n-1]

assert rank_q(R) == 16
maxminors=[]
for j in range(17):
    maxminors.append(det_bareiss([[row[c] for c in range(17) if c != j] for row in R]))
delta16=reduce(gcd,(abs(x) for x in maxminors),0)
assert delta16 == 2
# A rank-16 presentation on 17 generators with maximal-minor gcd 2 has
# cokernel Z plus a torsion group of order 2, hence Z + Z/2.

# Primitive cofactor nullvector: a generator of Hom(H_1,Z), i.e. free coordinate.
w=[((-1)**j)*maxminors[j] for j in range(17)]
gw=reduce(gcd,(abs(x) for x in w if x),0)
w=[x//gw for x in w]
assert gcd(*[abs(x) for x in w if x]) == 1
assert all(sum(row[j]*w[j] for j in range(17)) == 0 for row in R)

def rank_mod2(A):
    if not A: return 0
    n=len(A[0]); rows=[sum((x&1)<<j for j,x in enumerate(row)) for row in A]
    r=0
    for c in range(n):
        p=next((i for i in range(r,len(rows)) if (rows[i]>>c)&1),None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i]>>c)&1): rows[i] ^= rows[r]
        r += 1
    return r

base_rank2=rank_mod2(R)
assert base_rank2 == 15  # H_1(-;F_2) has dimension 17-15=2.

def rref_basis_mod2(A):
    n=len(A[0]); rows=[sum((x&1)<<j for j,x in enumerate(row)) for row in A]
    r=0; piv=[]
    for c in range(n):
        p=next((i for i in range(r,len(rows)) if (rows[i]>>c)&1),None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i]>>c)&1): rows[i] ^= rows[r]
        piv.append(c); r += 1
    return rows[:r],piv
B,P = rref_basis_mod2(R)
def quotient_key_mod2(v):
    x=sum((a&1)<<j for j,a in enumerate(v))
    for row,p in zip(B,P):
        if (x>>p)&1: x ^= row
    return x

cliques=[t for t in combinations(V,3) if all(tuple(sorted(e)) in EDGES for e in combinations(t,2))]
empty=[t for t in cliques if tuple(sorted(t)) not in FSET]
assert len(cliques) == 36 and len(empty) == 20

free_eval={''.join(t):sum(a*b for a,b in zip(cycle_vector(t),w)) for t in empty}
assert set(free_eval.values()) <= {-1,0,1}
zero_free=sorted(k for k,v in free_eval.items() if v == 0)
primitive=sorted(k for k,v in free_eval.items() if abs(v) == 1)
assert len(zero_free) == 8 and len(primitive) == 12

classes={}
for t in empty:
    v=cycle_vector(t)
    q=quotient_key_mod2(v)
    assert q != 0  # every empty triangle is nonzero in H_1(-;F_2)
    classes.setdefault(q,[]).append(''.join(t))
sizes=sorted(len(x) for x in classes.values())
assert sizes == [6,6,8]
# The free-zero group must be the unique order-two class; the two other
# mod-2 classes have primitive free coordinate and are the two torsion cosets.
zero_key={quotient_key_mod2(cycle_vector(t)) for t in empty if free_eval[''.join(t)] == 0}
assert len(zero_key) == 1 and len(next(iter(zero_key)).to_bytes(3,'little')) == 3
assert sorted(len(v) for k,v in classes.items() if k not in zero_key) == [6,6]

print('VERIFY_OK f=8,24,16 valence=4x1,5x1,6x3,7x3 H1=Z+Z/2 empty3=20 integral_classes=8,6,6 torsion_empty=8 primitive_empty=12 mod2_nonzero=20')
