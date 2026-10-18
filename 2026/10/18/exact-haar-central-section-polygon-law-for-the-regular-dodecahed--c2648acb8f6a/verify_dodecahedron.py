"""Exact arithmetic certificate for regular-dodecahedron central sections.
All scalars are pairs of integers representing a+b*sqrt(5).
Execute with Python 3.9 or later; no external packages needed.
"""
from itertools import product, combinations
from collections import Counter, defaultdict
from math import acos, pi, sqrt

zero=(0,0)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def sign(x):
    a,b=x
    if not b: return (a>0)-(a<0)
    if not a: return (b>0)-(b<0)
    if (a>0)==(b>0): return 1 if a>0 else -1
    cmp=(a*a>5*b*b)-(a*a<5*b*b)
    return cmp if a>0 else -cmp

def dot(u,v):
    z=zero
    for x,y in zip(u,v): z=add(z,mul(x,y))
    return z

def cross(u,v):
    return tuple(sub(mul(u[(i+1)%3],v[(i+2)%3]),mul(u[(i+2)%3],v[(i+1)%3])) for i in range(3))

def vneg(v): return tuple(neg(x) for x in v)

def vsub(v,w):return tuple(sub(x,y) for x,y in zip(v,w))

one=(2,0) # all vertex coordinates are doubled: actual 2*+-1 = +-2
phi=(1,1) # 2*phi = 1+sqrt(5)
invphi=(-1,1) # 2/phi = sqrt(5)-1
z=zero
V=[]
for a,b,c in product((-1,1), repeat=3):V.append(tuple((2*x,0) for x in (a,b,c)))
for a,b in product((-1,1),repeat=2):V.append((z, (a*invphi[0],a*invphi[1]),(b*phi[0],b*phi[1])))
for a,b in product((-1,1),repeat=2):V.append(((a*invphi[0],a*invphi[1]),(b*phi[0],b*phi[1]),z))
for a,b in product((-1,1),repeat=2):V.append(((a*phi[0],a*phi[1]),z,(b*invphi[0],b*invphi[1])))
assert len(V)==20 and len(set(V))==20
assert {dot(v,v) for v in V}=={(12,0)}
rep=[]
for v in V:
    if not any(v==w or v==vneg(w) for w in rep):rep.append(v)
assert len(rep)==10
assert all(v in rep or vneg(v) in rep for v in V)
# 30 shortest edges, exact squared Euclidean distance of doubled vertices.
E=[(i,j) for i,j in combinations(range(20),2) if dot(vsub(V[i],V[j]),vsub(V[i],V[j]))==(24,-8)]
assert len(E)==30
assert all(sign(sub(dot(vsub(V[i],V[j]),vsub(V[i],V[j])),(24,-8)))>=0 for i,j in combinations(range(20),2))
assert all(sum(i in pair for pair in E)==3 for i in range(20))
assert all((i,j) in E or dot(vsub(V[i],V[j]),vsub(V[i],V[j]))!=(24,-8) for i,j in combinations(range(20),2))
# 45 unordered pairs of distinct great circles. Exactly two antipodal
# intersections per pair, no three great circles concurrent.
P=[]
for i,j in combinations(range(10),2):
    q=cross(rep[i],rep[j]); assert any(sign(x) for x in q)
    assert all(sign(dot(q,rep[k]))!=0 for k in range(10) if k not in (i,j))
    for eps in (-1,1): P.append((i,j,q if eps==1 else vneg(q)))
assert len(P)==90
# Each vertex of the great-circle arrangement has exactly four adjacent
# sign chambers; collect their incident corners by sign vector.
regions=defaultdict(list)
for i,j,q in P:
    s0=[sign(dot(q,w)) for w in rep]
    assert s0.count(0)==2 and s0[i]==s0[j]==0
    for si,sj in product((-1,1),repeat=2):
        s=s0[:];s[i]=si;s[j]=sj
        regions[tuple(s)].append((i,j))
assert len(regions)==92
T=Counter()
for s,corners in regions.items():
    assert len(corners)==len(set(corners))
    # section side count: sign-changing polyhedron edges
    sv=tuple(s[rep.index(v)] if v in rep else -s[rep.index(vneg(v))] for v in V)
    crossing=sum(sv[i]!=sv[j] for i,j in E)
    # at a chamber corner, inward spherical boundary normals are
    # s_i * rep[i], s_j * rep[j], so interior angle cos is their
    # NEGATIVE Euclidean normalized dot product. |rep|^2 = 12.
    cosine_nums=tuple(sorted((-s[i]*s[j]*dot(rep[i],rep[j])[0], -s[i]*s[j]*dot(rep[i],rep[j])[1]) for i,j in corners))
    T[(crossing,len(corners),cosine_nums)]+=1
print('Distinct chambers',len(regions),'classification table:')
for (edges,vertices,angles),mult in sorted(T.items()):
    print('multiplicity',mult,'section_sides',edges,'chamber_vertices',vertices,'angle_cos_times_12',Counter(angles))
assert sorted((k[0],k[1],v) for k,v in T.items())==[(6,6,20),(8,3,60),(10,5,12)]
# canonical three angle sets; cosine = numerator / 12
assert T[(6,6,tuple(sorted([(-4,0)]*3+[ (0,-4)]*3))) ]==20
assert T[(8,3,tuple(sorted([(4,0)]*2+[(0,4)]))) ]==60
assert T[(10,5,tuple(sorted([(-4,0)]*5))) ]==12
alpha=acos(1/3);beta=acos(sqrt(5)/3)
areas={6:2*pi-3*(alpha+beta),8:2*alpha+beta-pi,10:2*pi-5*alpha}
assert all(a>0 for a in areas.values())
assert abs(sum({6:20,8:60,10:12}[k]*a for k,a in areas.items())-4*pi)<1e-12
print('Probabilities:', {k:({6:20,8:60,10:12}[k]*a/(4*pi)) for k,a in areas.items()})
print('All exact ring and combinatorial checks passed.')
