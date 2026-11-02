"""Exact algebraic reconstruction of the snub-cubical edge list.
Run python3 verify_geometry.py snub_edges.txt; only Python standard library.
Coordinates use Z[t]/(t^3-t^2-t-1) and t^-1=t^2-t-1.
"""
from decimal import Decimal,getcontext
from itertools import permutations,product
import sys

getcontext().prec=70
T=Decimal('1.8')
for _ in range(15): T-= (T**3-T**2-T-1)/(3*T*T-2*T-1)
assert Decimal('1.839286755214161')-Decimal('0.000000000000001')<T<Decimal('1.839286755214161')+Decimal('0.000000000000001')
P=((1,0,0),(-1,-1,1),(0,1,0))
def pval(c):return Decimal(c[0])+T*Decimal(c[1])+T*T*Decimal(c[2])
def sq(a):
    z=[0]*5
    for i in range(3):
        for j in range(3):z[i+j]+=a[i]*a[j]
    return (z[0]+z[3]+z[4],z[1]+z[3]+2*z[4],z[2]+z[3]+2*z[4])
pts=[]
for perm in permutations(range(3)):
    inv=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))%2
    for ss in product((-1,1),repeat=3):
        if sum(s>0 for s in ss)%2==inv:
            pts.append(tuple(tuple(ss[i]*a for a in P[perm[i]]) for i in range(3)))
assert len(pts)==24
pts.sort(key=lambda v:tuple(pval(x) for x in v))
assert len({tuple(pval(x) for x in v) for v in pts})==24
edge_squared=(2,4,-2)
E=[]
D={}
for i in range(24):
    for j in range(i+1,24):
        dd=(0,0,0)
        for a in range(3):
            c=tuple(pts[i][a][k]-pts[j][a][k] for k in range(3))
            v=sq(c)
            dd=tuple(dd[k]+v[k] for k in range(3))
        D[dd]=D.get(dd,0)+1
        if dd==edge_squared:E.append((i,j))
# Decimal evaluation is only used to certify a wide separating numerical gap,
# never to decide adjacency (the exact polynomial equality does that).
edge_d2=pval(edge_squared)
other=min(pval(x) for x in D if x!=edge_squared)
assert Decimal('2.59')<edge_d2<Decimal('2.60')
assert other>Decimal('5.18')
assert len(E)==60
A=[0]*24
for i,j in E:A[i]|=1<<j;A[j]|=1<<i
assert all(a.bit_count()==5 for a in A)
tri=sum((A[i]&A[j]).bit_count() for i,j in E)//3
assert tri==32
found=[tuple(map(int,l.split())) for l in open(sys.argv[1] if len(sys.argv)>1 else 'snub_edges.txt') if l.strip()]
assert E==found,(E,found)
print('PASS: exact cubic-ring geometric edge equality; 24 vertices, 60 edges, 5-regular, 32 triangles')
print('edge squared = 2+4t-2t^2 ~',edge_d2)
print('smallest distinct other squared distance >',other)
