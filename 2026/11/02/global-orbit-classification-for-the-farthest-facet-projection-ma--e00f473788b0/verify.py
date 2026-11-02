"""Exact checks for a farthest-face projection map on regular simplices.
Uses only Python standard-library fractions and combinatorics.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial

def step(a):
    d=len(a)-1
    m=max(a)
    arg=[i for i,x in enumerate(a) if x==m]
    if len(arg)>1:return tuple(a), None
    j=arg[0]
    return tuple((Q(0) if i==j else a[i]+a[j]/d) for i in range(d+1)),j

def canonical_cycle(order):
    d=len(order)-1
    vals=[Q(2*k,d*(d+1)) for k in range(d+1)]
    # order lists labels from smallest to largest
    a=[None]*(d+1)
    for k,i in enumerate(order):a[i]=vals[k]
    return tuple(a)

for d in range(3,7):
    count=0
    for order in permutations(range(d+1)):
        a=canonical_cycle(order)
        b=a
        labels=[]
        for s in range(d+1):
            b,j=step(b)
            assert j==order[d-s]
            labels.append(j)
            assert b!=a or s==d
        assert b==a
        count+=1
    assert count==factorial(d+1)
    for h in range(1,40):
        # strict order, exact rational barycentric coordinates with one zero
        vals=[Q(0)]+[Q(k*k+h, sum(j*j+h for j in range(1,d+1))) for k in range(1,d+1)]
        b=tuple(vals)
        lab=[]
        for s in range(d+1):
            b,j=step(b)
            lab.append(j)
        assert len(set(lab))==d+1
    w=[Q(0),Q(1),Q(1)]+[Q(k) for k in range(2,d)]
    Z=sum(w)
    w=tuple(z/Z for z in w)
    seen=[]
    for t in range(d+1):
        z,j=step(w)
        if j is None:break
        w=z
        seen.append(j)
    assert step(w)[1] is None
    print(f'd={d}, {count} distinct labeled periodic points, {count//(d+1)} cycles OK; tie stops after {len(seen)} steps')

# Differential of the four-step return in ambient barycentric coordinates.
# At phase (0,1/6,1/3,1/2) the itinerary is facet 3,2,1,0.
# Affine differential M_j sends e_j to (1/d) sum_{i !=j}e_i and e_i to e_i (i!=j).
def mul(A,B):
    n=len(A); m=len(A[0]); p=len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]
d=3;n=4
M=[[Q(int(i==k)) for k in range(n)] for i in range(n)]
for j in [3,2,1,0]:
    A=[[Q(int(i==k)) if k!=j else (Q(0) if i==j else Q(1,d)) for k in range(n)] for i in range(n)]
    M=mul(A,M)
# Tangent of facet 0 consists vectors with component 0 zero and sum 1..3 zero.
# use e1-e3, e2-e3 in barycentric coordinates
B=[[Q(0),Q(0)],[Q(1),Q(0)],[Q(0),Q(1)],[Q(-1),Q(-1)]]
C=mul(M,B)
assert C[0]==[0,0]
assert [sum(C[i][k] for i in range(4)) for k in range(2)]==[0,0]
E=[C[1],C[2]]
tr=E[0][0]+E[1][1]
det=E[0][0]*E[1][1]-E[0][1]*E[1][0]
print('tetrahedral return matrix:',E,'trace',tr,'det',det)
assert tr==Q(-14,81)
assert det==Q(1,81)
print('CHECK_OK')
