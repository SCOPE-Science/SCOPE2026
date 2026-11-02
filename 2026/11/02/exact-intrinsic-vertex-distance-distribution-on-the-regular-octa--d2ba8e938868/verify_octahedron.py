"""Reproducibility checks for the intrinsic vertex-distance law
on the unit-edge regular octahedron. Standard Python 3, no external packages.

Exact planar unfolding is carried out over Q(sqrt(3)), with coordinates
(x,y)=(sqrt(3)*u/2, v/2), u,v rational.
"""
from fractions import Fraction as Q
from itertools import combinations
import math
import random

FACES = {}
for i in range(4):
    e1, e2 = 'E'+str(i), 'E'+str((i+1)%4)
    FACES['T'+str(i)] = frozenset(('N',e1,e2))
    FACES['B'+str(i)] = frozenset(('S',e1,e2))
NEIGHBORS = {x: [] for x in FACES}
for a,b in combinations(FACES,2):
    if len(FACES[a] & FACES[b]) == 2:
        NEIGHBORS[a].append(b)
        NEIGHBORS[b].append(a)

def plus(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[0],x[1]-y[1]
def times(c,x):return c*x[0],c*x[1]
def dot(x,y):return Q(3,4)*x[0]*y[0]+Q(1,4)*x[1]*y[1]
def refl(p,a,b):
    u=sub(b,a);v=sub(p,a)
    return sub(times(2,plus(a,times(dot(v,u)/dot(u,u),u))),p)

root={'S':(Q(0),Q(0)),'E0':(Q(1),Q(1)),'E1':(Q(1),Q(-1))}
images=[]
def explore(face,coords,chain):
    if face[0]=='T':
        images.append((tuple(chain),coords['N']))
    for other in NEIGHBORS[face]:
        if other in chain:continue
        common=FACES[face]&FACES[other]
        a,b=tuple(common)
        old=next(iter(FACES[face]-common))
        new=next(iter(FACES[other]-common))
        c=coords.copy()
        c[new]=refl(c[old],coords[a],coords[b])
        explore(other,c,chain+[other])
explore('B0',root,['B0'])
points=sorted(set(p for chain,p in images))
vertex_images = [(Q(0),Q(0)), (Q(1),Q(1)), (Q(1),Q(-1))]
canonical=(Q(2),Q(0))
assert canonical in points
for im in points:
    for p in vertex_images:
        # Since squared-distance difference is affine in p, it is nonnegative
        # throughout a triangle if it is nonnegative at the vertices.
        delta=dot(sub(im,p),sub(im,p))-dot(sub(canonical,p),sub(canonical,p))
        assert delta >= 0, (im,p,delta)
print('EXACT unfoldings:',len(images),'distinct N images:',len(points),
      'all nearest-image inequalities certified at all three face vertices')
print('Image coordinates (sqrt(3)/2 * u, v/2):',points)

def F(r):
    if r<=0:return 0.0
    if r<=1:return math.pi*r*r/(3*math.sqrt(3))
    if r>=math.sqrt(3):return 1.0
    t=(3-math.sqrt(4*r*r-3))/2
    s=math.sqrt(3)*(1-t/2)
    return 1-t+(2*r*r/math.sqrt(3))*math.acos(min(1,max(-1,s/r)))

def distance(bottom,u,v):
    # Barycentric face point with S/N as the zero vertex; u,v are weights
    x=math.sqrt(3)/2*(u+v)
    y=(u-v)/2
    return math.hypot(x-(math.sqrt(3) if bottom else 0),y)

# Separate quadrature of each triangle using a uniform centroid grid.
# This integrates squared distance exactly as the polynomial is quadratic,
# up to O(grid^-2). It is not used to prove the infinite formula.
for n in [20,80,320]:
    top=bottom=0.
    count=0
    for i in range(n):
        for j in range(n-i):
            # Two triangles per grid square when i+j<n-1.
            u,v=(i+1/3)/n,(j+1/3)/n
            top+=distance(False,u,v)**2
            bottom+=distance(True,u,v)**2
            count+=1
            if i+j<n-1:
                u,v=(i+2/3)/n,(j+2/3)/n
                top+=distance(False,u,v)**2
                bottom+=distance(True,u,v)**2
                count+=1
    total=(top+bottom)/(2*count)
    assert abs(total-11/12)<0.001
    print('grid',n,'mean D^2',format(total,'.12f'))

rng=random.Random(821012)
N=300_000
sumsq=0.0
samples=[]
for k in range(N):
    # Uniform Dirichlet barycentric weights by folding the unit square.
    a=rng.random();b=rng.random()
    if a+b>1:a,b=1-a,1-b
    d=distance(k%2==0,a,b)
    sumsq+=d*d
    samples.append(d)
assert abs(sumsq/N-11/12)<0.01
for r in [0.25,0.5,0.75,math.sqrt(3)/2,0.9,1.0,1.05,1.25,1.5,1.7]:
    obs=sum(d<=r for d in samples)/N
    assert abs(obs-F(r))<0.008, (r,obs,F(r))
    print('CDF',format(r,'.9f'),'observed',format(obs,'.6f'),'exact',format(F(r),'.6f'))
print('Monte Carlo squared moment',format(sumsq/N,'.9f'),'exact',11/12)
for eps in [0.08,0.04,0.02]:
    ratio=(1-F(math.sqrt(3)-eps))/(eps*eps)
    assert abs(ratio-2/3)<0.04
    print('upper-tail ratio',format(eps,'.5f'),format(ratio,'.9f'))
print('ALL CHECKS PASSED')
