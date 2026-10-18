"""Independent finite checks for the unit-square finite-plank area theorem.

Requires SymPy and Shapely. Finite tests are not substitutes for the proof.
Run: python checks/verify.py
"""
import math
import random
import sympy as sp
from shapely.geometry import Polygon, box
from shapely.ops import unary_union

W,A,B,D,s = sp.symbols('W A B D s', real=True)
rho2 = A*A+B*B
assert sp.simplify(A+B-A*B-((1+rho2)/2-(1-A-B)**2/2))==0
assert sp.simplify((sp.sqrt(2)*W-W**2/2)-(A+B-A*B) - ((W**2-rho2)+(sp.sqrt(2)*W-A-B)*(2-sp.sqrt(2)*W-A-B))/2)==0
assert sp.simplify((1+W*W)/2-(A+B-A*B) - ((W**2-rho2)+(1-A-B)**2)/2)==0
r=sp.sqrt(2*W*W-1)
a=(1+r)/(2*W)
b=(1-r)/(2*W)
assert sp.simplify(a*a+b*b-1)==0
assert sp.simplify((a+b-W)**2/(4*a*b) - (1-W*W)/2)==0

Q=box(-.5,-.5,.5,.5)

def strip(n,t,w):
    a,b=n
    tangent=(-b,a)
    L=6.
    c1=(a*(t-w/2),b*(t-w/2))
    c2=(a*(t+w/2),b*(t+w/2))
    verts=[(c1[0]+L*tangent[0],c1[1]+L*tangent[1]),
           (c1[0]-L*tangent[0],c1[1]-L*tangent[1]),
           (c2[0]-L*tangent[0],c2[1]-L*tangent[1]),
           (c2[0]+L*tangent[0],c2[1]+L*tangent[1])]
    return Polygon(verts)

def f(w):
    return math.sqrt(2)*w-w*w/2 if w<=1/math.sqrt(2) else (1+w*w)/2

# Every claimed optimizing direction realizes the formula, independently
# via polygon/strip intersections.
for i in range(1,50):
    w=.02+.96*i/50
    if w<=1/math.sqrt(2): angle=math.pi/4
    else: angle=math.pi/4-math.acos(1/(math.sqrt(2)*w))
    n=(math.cos(angle),math.sin(angle))
    area=Q.intersection(strip(n,0.,w)).area
    assert abs(area-f(w))<3e-12,(w,area,f(w))

rng=random.Random(20261017)
families=0
single=0
for k in range(340):
    w=.02+.95*rng.random()
    parts=rng.randint(1,5)
    proportions=[rng.uniform(.05,1) for _ in range(parts)]
    proportions=[p*w/sum(proportions) for p in proportions]
    polys=[]; qdirs=[]
    for p in proportions:
        theta=2*math.pi*rng.random()
        n=(math.cos(theta),math.sin(theta))
        t=rng.uniform(-.4,.4)
        polys.append(Q.intersection(strip(n,t,p)))
        qdirs.append((abs(n[0]),abs(n[1])))
    covered=unary_union(polys).area
    assert covered<=f(w)+2e-10,(k,w,covered,f(w))
    aa=sum(p*q[0] for p,q in zip(proportions,qdirs))
    bb=sum(p*q[1] for p,q in zip(proportions,qdirs))
    deficit=w*w-aa*aa-bb*bb
    pair=sum(proportions[i]*proportions[j]*sum((qdirs[i][h]-qdirs[j][h])**2 for h in (0,1))
             for i in range(parts) for j in range(i+1,parts))
    assert abs(deficit-pair)<2e-12
    assert covered<=aa+bb-aa*bb+2e-10
    assert f(w)-covered>=deficit/2-2e-10
    families+=1
    theta=math.pi/4*rng.random()
    n=(math.cos(theta),math.sin(theta))
    t=rng.uniform(-.3,.3)
    area=Q.intersection(strip(n,t,w)).area
    assert area<=f(w)+2e-10
    single+=1
print('VERIFY_OK symbolic_identities=5 attaining_directions=49 families='+str(families)+' random_single_planks='+str(single))
