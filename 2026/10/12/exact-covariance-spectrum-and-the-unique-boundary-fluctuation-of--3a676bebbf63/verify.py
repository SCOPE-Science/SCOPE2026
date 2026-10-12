"""Exact overlap-enumeration verifier for consecutive triple patterns.
Run: python3 verify.py (Python standard library only).
"""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations
from math import factorial

PATS = tuple(permutations((1, 2, 3)))
# The stated theorem uses a different explicit order; do not rely on tuple ordering.
PATS = ((1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1))
A360 = ((46,-23,-23,7,7,-14),(-23,28,10,-20,-2,7),(-23,10,28,-2,-20,7),(7,-20,-2,28,10,-23),(7,-2,-20,10,28,-23),(-14,7,7,-23,-23,46))
B360 = ((-74,67,67,-38,-38,16),(67,-32,-35,40,-2,-38),(67,-35,-32,-2,40,-38),(-38,40,-2,-32,-35,67),(-38,-2,40,-35,-32,67),(16,-38,-38,67,67,-74))
E=(1,1,1,1,1,1)
W=(0,1,-1,1,-1,0)
A=(0,1,-1,-1,1,0)
B=(2,-1,-1,-1,-1,2)
U=(1,0,0,0,0,-1)
V=(0,1,1,-1,-1,0)

def pat(t):
    return tuple(sorted(t).index(x)+1 for x in t)

def dotrow(M,v):
    return tuple(sum(row[k]*v[k] for k in range(6)) for row in M)

def add(x,y):return tuple(a+b for a,b in zip(x,y))

def scale(s,x):return tuple(s*a for a in x)

def cov_formula(n):
    return tuple(tuple(F(n*A360[i][j]+B360[i][j],360) for j in range(6)) for i in range(6))

def overlap_cov(d):
    counts = Counter()
    for q in permutations(range(d+3)):
        counts[(pat(q[:3]),pat(q[d:d+3]))]+=1
    return tuple(tuple(F(counts[(p,q)],factorial(d+3))-F(1,36) for q in PATS) for p in PATS)

V0=tuple(tuple((F(1,6) if i==j else F(0))-F(1,36) for j in range(6)) for i in range(6))
V1,V2=overlap_cov(1),overlap_cov(2)
for n in range(4,20):
    C=cov_formula(n)
    for i in range(6):
        for j in range(6):
            direct=(n-2)*V0[i][j]+(n-3)*(V1[i][j]+V1[j][i])+(n-4)*(V2[i][j]+V2[j][i])
            assert C[i][j]==direct,(n,i,j,C[i][j],direct)
    assert dotrow(C,E)==scale(0,E)
    assert dotrow(C,W)==scale(F(1,8),W)
    assert dotrow(C,A)==scale(F(12*n-13,120),A)
    assert dotrow(C,B)==scale(F(16*n-29,120),B)
    assert dotrow(C,U)==add(scale(F(2*n-3,12),U),scale(-F(2*n-7,24),V))
    assert dotrow(C,V)==add(scale(-F(2*n-7,12),U),scale(F(4*n-7,24),V))

for n in range(4,9):
    count=0
    csum=[0]*6
    second=[[0]*6 for _ in range(6)]
    end_counts=Counter()
    for perm in permutations(range(n)):
        count+=1
        h=Counter(pat(perm[i:i+3]) for i in range(n-2))
        v=[h[x] for x in PATS]
        for i in range(6):
            csum[i]+=v[i]
            for j in range(6): second[i][j]+=v[i]*v[j]
        tr=sum(a*b for a,b in zip(W,v))
        boundary=int(perm[0]<perm[1])-int(perm[-2]<perm[-1])
        assert tr==boundary
        end_counts[tr]+=1
    for i in range(6):
        assert F(csum[i],count)==F(n-2,6)
        for j in range(6):
            assert F(second[i][j],count)-F(csum[i]*csum[j],count*count)==cov_formula(n)[i][j],(n,i,j)
    assert end_counts[-1]*4==count and end_counts[0]*2==count and end_counts[1]*4==count
    print('n',n,'permutations',count,'exact-covariance entries',36,'boundary-law verified')
print('VERIFY_OK')
