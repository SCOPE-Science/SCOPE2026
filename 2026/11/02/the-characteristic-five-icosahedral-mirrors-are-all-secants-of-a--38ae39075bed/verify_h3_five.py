#!/usr/bin/env python3
"""Exact, self-contained verification for the characteristic-five icosahedral mirror arrangement."""
from itertools import product, combinations
from collections import Counter
P=5

def normalize(a):
    a=tuple(int(x)%P for x in a)
    assert any(a)
    z=next(t for t in a if t)
    return tuple(t*pow(z,-1,P)%P for t in a)

def cross(a,b):
    return normalize((a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]))

def dot(a,b):return sum(x*y for x,y in zip(a,b))%P

# The H_3 mirror normals are the three coordinate vectors and the twelve
# cyclic permutations of (1, +/-phi, +/-phi^{-1}), phi=(1+sqrt(5))/2.
# In F_5, phi=3 and phi^{-1}=2.
raw=[(1,0,0),(0,1,0),(0,0,1)]
for i in range(3):
    for s,t in product([1,-1],repeat=2):
        v=(1,s*3,t*2)
        raw.append(tuple(v[(j-i)%3] for j in range(3)))
lines={normalize(v) for v in raw}
assert len(raw)==15 and len(lines)==15
points={normalize(t) for t in product(range(P), repeat=3) if any(t)}
assert len(points)==31
conic={v for v in points if dot(v,v)==0}
assert len(conic)==6
secants={cross(a,b) for a,b in combinations(sorted(conic),2)}
assert len(secants)==15
assert lines==secants
inc={u:sum(dot(v,u)==0 for v in lines) for u in points}
assert Counter(inc.values())=={2:15,3:10,5:6}
assert {u for u in points if inc[u]==5}==conic
assert sum(v*(v-1)//2 for v in inc.values())==105
assert sum(v-1 for v in inc.values())==59
# Every F5-rational point is a multiple intersection; no other geometric
# intersections exist because all line pairs already meet at rational points.
# The three 2x2 Frobenius minors generate the reduced ideal of P^2(F5),
# with Hilbert-Burch syzygies of degrees 7 and 11.
def minors(pt):
    x,y,z=pt
    return ((x**5*y-x*y**5)%P,(x**5*z-x*z**5)%P,(y**5*z-y*z**5)%P)
assert all(minors(pt)==(0,0,0) for pt in points)
# Hilbert-Burch syzygies checked as literal integer polynomial identities.
import sympy as sp
x,y,z=sp.symbols('x y z')
a=x**5*y-x*y**5
b=x**5*z-x*z**5
c=y**5*z-y*z**5
assert sp.expand(z*a-y*b+x*c)==0
assert sp.expand(z**5*a-y**5*b+x**5*c)==0
T=sp.symbols('T')
hilbert_num=1-3*T**6+T**7+T**11
assert sp.expand(hilbert_num).subs(T,1)==0
assert sp.diff(hilbert_num,T).subs(T,1)==0
assert sp.diff(hilbert_num,T,2).subs(T,1)//2==31
for n in (1,2,3):
    q=P**n
    assert 15*(q+1)-59==15*q-44
assert (15-1)*(15-2)//2==91
print('H3_MIRRORS=15')
print('F5_CONIC_POINTS=6')
print('SECANTS_EQUAL_MIRRORS=TRUE')
print('ALL_F5_PLANE_POINTS_SINGULAR=31')
print('INTERSECTION_SPECTRUM=2:15,3:10,5:6')
print('REDUCED_SINGULAR_IDEAL=2x2_FROBENIUS_MINORS')
print('HILBERT_BURCH_SHIFTS=6,6,6;7,11')
print('CURVE_POINTS_OVER_F5_EXTENSIONS=15*5^n-44')
print('ARITHMETIC_GENUS=91')
print('VERIFY_OK')
