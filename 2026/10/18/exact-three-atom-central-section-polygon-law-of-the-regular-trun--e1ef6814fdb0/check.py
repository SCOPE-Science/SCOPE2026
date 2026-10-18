#!/usr/bin/env python3
"""Independent reproducibility checks for regular truncated tetrahedron central sections.
Standard library only; the exact proof is given separately in RESULT.md.
"""
import math, random
from fractions import Fraction as F
from collections import Counter
from itertools import combinations

TETRA = [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
PAIRS = [(i,j) for i in range(4) for j in range(4) if i!=j]
VERTS = [tuple(2*TETRA[i][k]+TETRA[j][k] for k in range(3)) for i,j in PAIRS]
INDEX = {k:v for v,k in enumerate(PAIRS)}
EDGES = set()
for i in range(4):
    for j,k in combinations([t for t in range(4) if t!=i],2):
        EDGES.add(tuple(sorted((INDEX[i,j],INDEX[i,k]))))
for i,j in combinations(range(4),2):
    EDGES.add(tuple(sorted((INDEX[i,j],INDEX[j,i]))))
EDGES = sorted(EDGES)
assert len(VERTS)==12 and len(EDGES)==18

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def norm(a): return math.sqrt(dot(a,a))
def triple(a,b,c): return dot(a,cross(b,c))
def omega(a,b,c):
    na,nb,nc=norm(a),norm(b),norm(c)
    den=na*nb*nc+dot(a,b)*nc+dot(b,c)*na+dot(c,a)*nb
    return 2*math.atan2(abs(triple(a,b,c)),den)

def angle_forms(p,q):
    return (1-p-3*q,1-3*p-q,-1+3*p-q,-1-p+3*q)
BASE=[(F(0),F(0)),(F(1),F(0)),(F(1),F(1))]
def clip(poly,idx,sign):
    if not poly: return []
    result=[]
    for u,v in zip(poly,poly[1:]+poly[:1]):
        fu=angle_forms(*u)[idx]*(1 if sign else -1)
        fv=angle_forms(*v)[idx]*(1 if sign else -1)
        if fu>=0: result.append(u)
        if (fu<0<fv) or (fv<0<fu):
            lam=fu/(fu-fv)
            result.append((u[0]+lam*(v[0]-u[0]),u[1]+lam*(v[1]-u[1])))
    clean=[]
    for w in result:
        if not clean or clean[-1]!=w:clean.append(w)
    if len(clean)>1 and clean[0]==clean[-1]:clean.pop()
    return clean

def zone(signs):
    poly=BASE[:]
    for idx,sign in enumerate(signs):poly=clip(poly,idx,sign)
    return poly

def area(poly):
    rays=[(F(1),p,q) for p,q in poly]
    return sum(omega(rays[0],rays[i],rays[i+1]) for i in range(1,len(rays)-1))

def N_edges(n):
    s=[dot(v,n)>0 for v in VERTS]
    return sum(s[i]!=s[j] for i,j in EDGES)

def N_formula(n):
    x,y,z=sorted(map(abs,n),reverse=True)
    a,b,c,d=(x-y-3*z,x-3*y-z,-x+3*y-z,-x-y+3*z)
    sa,sb,sc,sd=map(lambda t:int(t>0),(a,b,c,d))
    return 4+sa+sb+sc+sd-2*sa*sb

def hull_count(n):
    a,b,c=n
    basis = cross(n,(0,0,1)) if abs(c)<max(abs(a),abs(b)) else cross(n,(0,1,0))
    bnorm=norm(basis)
    basis=tuple(x/bnorm for x in basis)
    second=cross(n,basis)
    nn=norm(n)
    second=tuple(x/nn for x in second)
    s=[dot(v,n) for v in VERTS]
    pts=[]
    for i,j in EDGES:
        if s[i]*s[j]>=0: continue
        denom=s[i]-s[j]
        pt=tuple((s[i]*VERTS[j][k]-s[j]*VERTS[i][k])/denom for k in range(3))
        pts.append((dot(pt,basis),dot(pt,second)))
    pts=sorted(set(pts))
    def orient(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lower=[]
    for p in pts:
        while len(lower)>=2 and orient(lower[-2],lower[-1],p)<=1.e-9:lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(pts):
        while len(upper)>=2 and orient(upper[-2],upper[-1],p)<=1.e-9:upper.pop()
        upper.append(p)
    return len(lower)+len(upper)-2

EXPECTED={
    (0,0,0,0): (4,[(F(1,2),F(1,2)),(F(1,4),F(1,4)),(F(2,5),F(1,5))]),
    (0,0,1,0): (5,[(F(1),F(0)),(F(1),F(2,3)),(F(1,2),F(1,2)),(F(2,5),F(1,5))]),
    (0,0,1,1): (6,[(F(1),F(2,3)),(F(1),F(1)),(F(1,2),F(1,2))]),
    (1,0,0,0): (5,[(F(1,3),F(0)),(F(2,5),F(1,5)),(F(1,4),F(1,4))]),
    (1,0,1,0): (6,[(F(1,3),F(0)),(F(1),F(0)),(F(2,5),F(1,5))]),
    (1,1,0,0): (4,[(F(0),F(0)),(F(1,3),F(0)),(F(1,4),F(1,4))]),
}

def predictions():
    from itertools import product
    allzones={}
    for s in product((0,1),repeat=4):
        poly=zone(s)
        if len(poly)<3 or area(poly)<1e-12:continue
        allzones[s]=poly
    assert len(allzones)==len(EXPECTED)
    for s,(n,poly) in EXPECTED.items():
        assert allzones[s]==poly, (s, allzones[s],poly)
        center=(sum(p for p,q in poly)/len(poly),sum(q for p,q in poly)/len(poly))
        signs=tuple(int(v>0) for v in angle_forms(*center))
        assert signs==s
        ray=(F(1),*center)
        assert N_edges(ray)==n==N_formula(ray), (s,n,center)
    probs=Counter()
    for s,poly in allzones.items():probs[EXPECTED[s][0]]+=area(poly)*12/math.pi
    assert abs(sum(probs.values())-1)<1.e-13
    u,v,w=(2,1,1),(4,1,1),(5,2,1)
    p4_compact=(24/math.pi)*(math.atan(2/(18*math.sqrt(10)+10*math.sqrt(30)+23*math.sqrt(6)+39*math.sqrt(2)))+math.atan(1/(6*math.sqrt(5)+9*math.sqrt(2)+13+4*math.sqrt(10))))
    assert abs(probs[4]-p4_compact)<1.e-13
    E=18*math.acos(F(7,11))/math.pi
    assert abs(sum(n*p for n,p in probs.items())-E)<1.e-13
    print('EXHAUSTIVE_EXACT_RATIONAL_CHAMBER_PARTITION_OK',len(allzones),'regions')
    print('SOLID_ANGLES_AND_EXPECTED_VERTEX_IDENTITY_OK',E)
    print('P4_P5_P6',*(f'{probs[i]:.15f}' for i in (4,5,6)))
    return probs

def main():
    probs=predictions()
    rng=random.Random(45678)
    counts=Counter()
    for i in range(10000):
        n=tuple(rng.gauss(0,1) for _ in range(3))
        exact=N_edges(n)
        other=N_formula(n)
        assert exact==other,(i,n,exact,other)
        if i<1800:
            cv=hull_count(n)
            assert cv==exact,(i,n,cv,exact)
        counts[exact]+=1
    for v in (4,5,6):assert abs(counts[v]/10000-probs[v])<.02
    print('DIRECT_INDEPENDENT_CONVEX_HULL_RECONSTRUCTIONS_OK',1800)
    print('SIGNED_PERMUTATION_COUNTS_AND_SPHERICAL_SAMPLING_OK',10000)
    print('ALL_TRUNCATED_TETRAHEDRON_CHECKS_OK')
if __name__=='__main__': main()
