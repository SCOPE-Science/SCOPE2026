"""Reproduce the spherical polygon-type law for the regular truncated tetrahedron.
Python >=3.10; numpy and mpmath required. Uses exact fractions for combinatorics.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from math import acos, atan2, pi, sqrt
import numpy as np
import mpmath as mp

T=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
V=sorted({tuple(2*a+b for a,b in zip(A,B)) for A in T for B in T if A!=B})
E=[(i,j) for i,j in combinations(range(len(V)),2)
   if sum((a-b)**2 for a,b in zip(V[i],V[j]))==8]
assert len(V)==12 and len(E)==18
assert all(sum((V[i][k]**2 for k in range(3)))==11 for i in range(12))
assert all(sum(V[i][k]*V[j][k] for k in range(3))==7 for i,j in E)
assert Counter(i for e in E for i in e)=={i:3 for i in range(12)}

def cross_count(y,z):
    s=[v[0]+v[1]*y+v[2]*z for v in V]
    assert all(t != 0 for t in s), ('boundary', y,z)
    return sum(s[i]*s[j] < 0 for i,j in E)

# Each tuple lists the vertices (y,z) of one spherical angular cell in
# the standard chamber 0<=z<=y<=1 with normal proportional to (1,y,z).
P=[
(5, [(1,F(2,3)),(1,0),(F(2,5),F(1,5)),(F(1,2),F(1,2))]),
(6, [(1,0),(F(1,3),0),(F(2,5),F(1,5))]),
(4, [(F(1,3),0),(0,0),(F(1,4),F(1,4))]),
(4, [(F(1,4),F(1,4)),(F(1,2),F(1,2)),(F(2,5),F(1,5))]),
(5, [(F(2,5),F(1,5)),(F(1,3),0),(F(1,4),F(1,4))]),
(6, [(F(1,2),F(1,2)),(1,1),(1,F(2,3))]),
]

def pol_area(poly):
    return abs(sum(y*z2-y2*z for (y,z),(y2,z2) in zip(poly,poly[1:]+poly[:1])))/2
assert sum((pol_area([(F(y),F(z)) for y,z in v]) for _,v in P),F()) == F(1,2)
assert {n for n,_ in P}=={4,5,6}
for n,verts in P:
    yy=sum((F(y) for y,z in verts),F())/len(verts)
    zz=sum((F(z) for y,z in verts),F())/len(verts)
    assert cross_count(yy,zz)==n, (n, yy,zz,cross_count(yy,zz))

# All vertex-sign lines are among the chamber boundaries or four internal
# critical lines. The latter are z=(1+y)/3, z=3y-1, z=1-3y, z=(1-y)/3.
# Every region thus has constant crossing count, checked at one interior point.
lines=set()
for v in V:
    if v[2]:
        slope=F(-v[1],v[2]); const=F(-v[0],v[2])
        if any(0<F(const+slope*F(j,100))<F(j,100) for j in range(1,101)):
            lines.add((slope,const))
assert lines=={(F(1,3),F(1,3)),(F(3),F(-1)),(F(-3),F(1)),(F(-1,3),F(1,3))}, lines
print('EXACT_VERTEX_AND_CHAMBER_PARTITION_PASSED')

# Direct determinant formula for spherical triangle area.
def det3(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
       -a[1]*(b[0]*c[2]-b[2]*c[0])
       +a[2]*(b[0]*c[1]-b[1]*c[0]))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def solid(rays):
    a,b,c=rays
    D=abs(det3(a,b,c))
    la,lb,lc=(sqrt(dot(v,v)) for v in rays)
    denom=la*lb*lc+dot(a,b)*lc+dot(b,c)*la+dot(c,a)*lb
    return 2*atan2(D,denom)

mp.mp.dps=60
S1=10*mp.sqrt(6)+4*mp.sqrt(30)+17*mp.sqrt(2)+7*mp.sqrt(10)
S2=6*mp.sqrt(11)+4*mp.sqrt(22)+8*mp.sqrt(6)+11*mp.sqrt(3)
A= [(1,1,0),(3,1,0),(5,2,1)]
B= [(2,1,1),(1,1,1),(3,3,2)]
assert abs(det3(*A))==2 and abs(det3(*B))==1
assert abs(mp.mpf(solid(A))-2*mp.atan(2/S1))<mp.mpf('1e-13')
assert abs(mp.mpf(solid(B))-2*mp.atan(1/S2))<mp.mpf('1e-13')
P6=24/mp.pi*(mp.atan(2/S1)+mp.atan(1/S2))
EN=18/mp.pi*mp.acos(mp.mpf(7)/11)
P4=P6+5-EN
P5=EN-4-2*P6
assert min(P4,P5,P6)>0 and abs(P4+P5+P6-1)<mp.mpf('1e-45')
print('EXACT_SOLID_ANGLE_AND_EDGE_CROFTON_IDENTITIES_PASSED')

# Independently calculate all six spherical cell areas (spherical triangle
# triangulation via vertex rays), not merely the two hexagonal cells.
def area(poly):
    rays=[(1,float(y),float(z)) for y,z in poly]
    return sum(solid([rays[0],rays[i],rays[i+1]]) for i in range(1,len(rays)-1))
areas={4:0.,5:0.,6:0.}
for n,p in P: areas[n]+=area(p)
assert abs(sum(areas.values())-pi/12)<1e-12, areas
for n,expected in [(4,P4),(5,P5),(6,P6)]:
    assert abs(12*areas[n]/pi-float(expected))<1e-12, (n,areas[n],expected)
print('INDEPENDENT_ALL_SIX_SPHERICAL_CELL_AREAS_PASSED')

# Exact rational lower certificate for the strict pentagonal majority.
# Standard rational bounds: 333/106 < pi < 355/113.
pl,pu=F(333,106),F(355,113)
assert float(pl)<pi<float(pu)
rootlo={2:F(1414,1000),3:F(1732,1000),6:F(2449,1000),
        10:F(3162,1000),11:F(3316,1000),22:F(4690,1000),30:F(5477,1000)}
assert all(z*z<m for m,z in rootlo.items())
s1lo=10*rootlo[6]+4*rootlo[30]+17*rootlo[2]+7*rootlo[10]
s2lo=6*rootlo[11]+4*rootlo[22]+8*rootlo[6]+11*rootlo[3]
t=rootlo[2]/3
atanlo=t-t**3/3+t**5/5-t**7/7
meanlo=36/pu*atanlo
qhi=24/pl*(2/s1lo+1/s2lo)  # atan(x) <= x for x >= 0
assert meanlo-4-2*qhi>F(518,1000)
print('RATIONAL_PENTAGON_MAJORITY_CERTIFICATE_PASSED')

rng=np.random.default_rng(314159)
counts=Counter()
for n in rng.normal(size=(240000,3)):
    counts[cross_count(*np.sort(np.abs(n))[::-1][1:]/np.max(np.abs(n)))] += 1
for k,p in [(4,P4),(5,P5),(6,P6)]:
    obs=counts[k]/240000
    assert abs(obs-float(p))<.011,(k,obs,p)
print('INDEPENDENT_HAAR_NORMAL_MONTE_CARLO_PASSED',dict(counts))
print('PROBABILITIES',*[mp.nstr(v,22) for v in [P4,P5,P6,EN]])
print('ALL_CHECKS_PASSED')
