"""Exact normal-fan certificate for the 4-crown threefold; standard Python only.
Run: python3 check_crown_resolution.py
"""
from itertools import product, combinations
from fractions import Fraction
from math import gcd

P1 = [(0,1,0),(1,0,0),(0,0,0)]
P2 = [(0,1,1),(1,0,1),(0,0,1),(1,0,0),(0,0,0)]
P3 = [(-1,1,1),(0,0,1),(0,0,0)]
points = sorted({tuple(a[i]+b[i]+c[i] for i in range(3)) for a,b,c in product(P1,P2,P3)})

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det3(a,b,c): return dot(a,cross(b,c))
def primitive(a):
    g = gcd(gcd(abs(a[0]),abs(a[1])),abs(a[2]))
    return tuple(x//g for x in a)

def facets_of_points(pts):
    facets = set()
    for x,y,z in combinations(pts,3):
        n = cross(sub(y,x),sub(z,x))
        if n == (0,0,0): continue
        n = primitive(n)
        vals=[dot(n,p) for p in pts]
        d=dot(n,x)
        if d == max(vals): facets.add((n,d))
        elif d == min(vals): facets.add((tuple(-t for t in n),-d))
    return tuple(sorted(facets))

# Cramer's rule with explicit determinant of matrices whose jth column is b.
def solve(rows, b):
    den=det3(*rows)
    if not den:return None
    v=[]
    for j in range(3):
        r=[tuple(b[i] if k==j else rows[i][k] for k in range(3)) for i in range(3)]
        v.append(Fraction(det3(*r),den))
    assert all(dot(r,v)==t for r,t in zip(rows,b))
    return tuple(v)

def verts_from_ineq(ineq):
    out={}
    for tri in combinations(ineq,3):
        q=solve([x[0] for x in tri],[x[1] for x in tri])
        if q is None or any(dot(n,q)>d for n,d in ineq):continue
        act=frozenset(n for n,d in ineq if dot(n,q)==d)
        out[q]=act
    return out

assert len(points)==22
facets=facets_of_points(points)
assert len(facets)==8,facets
assert set(facets)=={
 ((-1,0,0),1),((1,1,0),2),((0,1,-1),1),((0,0,1),2),
 ((0,-1,0),0),((0,0,-1),0),((-1,-1,0),0),((-1,0,-1),0)
}
assert abs(det3((1,0,0),(0,0,1),(-1,1,1)))==1 # Full character lattice.
old=verts_from_ineq(facets)
assert len(old)==10
special={p:act for p,act in old.items() if len(act)==4}
assert set(special)=={(-1,3,2),(0,0,0)}
for p,act in old.items():
    if len(act)==3: assert abs(det3(*act))==1
    else: assert len(act)==4
for p,act in special.items():
    assert any(abs(det3(*tri))==1 for tri in combinations(act,3))
    assert all(abs(det3(*tri))==1 for tri in combinations(act,3))
# Independent circuit rays, all other old vertices regular.
assert special[(-1,3,2)].isdisjoint(special[(0,0,0)])
all_types=set()
for s,t in product((-1,1),repeat=2):
    bump={(-1,0,0):Fraction(s,100),(0,-1,0):Fraction(t,100)}
    ineq=tuple((n,Fraction(d)+bump.get(n,0)) for n,d in facets)
    vnew=verts_from_ineq(ineq)
    assert len(vnew)==12,(s,t,len(vnew),vnew)
    assert all(len(act)==3 and abs(det3(*act))==1 for act in vnew.values())
    assert set().union(*vnew.values()) == {n for n,d in facets}
    old_cones=[act for act in old.values()]
    assert all(any(act.issubset(oldact) for oldact in old_cones) for act in vnew.values())
    signature=tuple(frozenset(act for act in vnew.values() if act.issubset(special[p])) for p in sorted(special))
    assert all(len(side)==2 for side in signature)
    all_types.add(signature)
    print('orientation',s,t,'new vertices',len(vnew),'resolved pairs',signature)
assert len(all_types)==4
print('VERIFY_OK',len(points),'Minkowski lattice sums;',len(facets),'facets;',len(old),'original vertices;',len(special),'conifolds;',len(all_types),'smooth projective small resolutions')
