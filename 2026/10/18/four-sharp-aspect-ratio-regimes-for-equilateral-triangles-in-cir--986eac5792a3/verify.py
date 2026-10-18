"""Reproducible finite diagnostics for the equilateral-triangle/cylinder theorem.

The analytic proof, not finite sampling, establishes the universal claim.
Requires only Python 3's standard library.
"""
import math
import random

SQ3=math.sqrt(3.0)
T1=math.sqrt(2.0)
T2=math.sqrt(7.0/3.0)
T3=4.0/SQ3

def f(k):
    z=k*k
    if z<=0.5:
        return (1-z)/math.sqrt(3-4*z)
    if z<=4/7:
        return k*math.sqrt(1-z)
    return (4-z)/(4*SQ3)

def radius_from_x(k,u):
    v=k-u
    a2=1-u*u; b2=1-v*v; c2=(1-k)*(1+k)
    if min(a2,b2,c2)<-1e-12:
        return None
    a2=max(0,a2); b2=max(0,b2); c2=max(0,c2)
    area16=3*c2-(u-v)**2
    if area16<-1e-9:
        return None
    maximum=max(a2,b2,c2)
    if 2*maximum>=a2+b2+c2-1e-12:
        return math.sqrt(maximum)/2
    if area16<1e-13:
        return None
    return math.sqrt(a2*b2*c2/area16)

def max_side(h,r=1.0):
    l=h/r
    if l<=T1:
        return r*math.sqrt(l*l+1.5+0.5*math.sqrt(9-4*l*l))
    if l<=T2:
        return r*l*l/math.sqrt(l*l-1)
    if l<=T3:
        return r*(math.sqrt(l*l+3)+SQ3)/2
    return r*T3

def witness(h,r=1.0):
    s=max_side(h,r)
    if h==0:
        u=v=0.0; k=0.0
    elif h>=r*T3:
        k=1.0;u=v=0.5
    else:
        k=h/s
        if k*k<=0.5:
            u=0.0;v=k
        elif k*k<=4/7:
            p=2*k*k-1
            discriminant=max(0,k*k-4*p)
            u=(k-math.sqrt(discriminant))/2;v=k-u
        else:
            u=v=k/2
    xx=(0,s*u,s*k)
    a=s*math.sqrt(max(0,1-u*u))
    ac2=s*s*(1-k*k)
    bc2=s*s*(1-v*v)
    if k>1-1e-10:
        yz=((0.0,0.0),(a,0.0),(0.0,0.0))
        ox=a/2;oy=0
    else:
        cx=(ac2+a*a-bc2)/(2*a)
        cy=math.sqrt(max(0,ac2-cx*cx))
        yz=((0.0,0.0),(a,0.0),(cx,cy))
        ox=a/2
        oy=(ac2/2-ox*cx)/cy
    vertices=[(xx[i],yz[i][0]-ox,yz[i][1]-oy) for i in range(3)]
    return vertices,(u,v,k)

def side(v,w):
    return math.sqrt(sum((a-b)**2 for a,b in zip(v,w)))

# Direct full-space witnesses, independent of the formula for disk radius.
witness_count=0
for i in range(2001):
    h=3.5*i/2000
    if h==0:continue
    pts,uvk=witness(h)
    s=max_side(h)
    for j in range(3):
        for q in range(j+1,3):
            assert abs(side(pts[j],pts[q])-s)<3e-8, (h,pts,uvk)
    assert min(v[0] for v in pts)>-1e-9
    assert max(v[0] for v in pts)<h+1e-9
    assert all(y*y+z*z<=1+2e-8 for _,y,z in pts)
    witness_count+=1

# For each attainable longitudinal span and splitting, project an equilateral triangle
# into the transverse plane and calculate the actual minimum-enclosing disk radius.
grid_tests=0
for i in range(1001):
    k=i/1000
    for j in range(81):
        u=k*j/160
        got=radius_from_x(k,u)
        if got is not None:
            assert got>=f(k)-1e-9,(k,u,got,f(k))
            grid_tests+=1

# Randomized spatial orientations of the unit equilateral triangle.  These diagnostics
# use the axis dot products of the actual edges and the independently computed
# minimum covering circle rather than the optimized p-formula.
rng=random.Random(314159265)
orientations=0
for h in (0.05,0.3,0.8,1.2,T1,1.46,T2,1.8,T3,3.0,7.0):
    bound=max_side(h)
    for _ in range(12000):
        theta=rng.random()*2*math.pi
        q=math.sqrt(rng.random())
        dx=(0.0,q*math.cos(theta),q*math.cos(theta-math.pi/3))
        high=max(dx)-min(dx)
        if high<1e-14:continue
        u=sorted(dx)[1]-min(dx)
        actual_r=radius_from_x(high,u)
        if actual_r is None:continue
        candidate=min(h/high,1/actual_r)
        assert candidate <= bound+2e-9,(h,candidate,bound,high,u,actual_r)
        orientations+=1

# Exact algebraic spot checks on rational z in each of the three branches.
from fractions import Fraction as F
for z in (F(0),F(1,9),F(1,4),F(1,2),F(15,28),F(4,7),F(3,4),F(1)):
    if z<=F(1,2):
        p=F(0)
        expected=(1-z)**2/(3-4*z)
    elif z<=F(4,7):
        p=2*z-1
        expected=z*(1-z)
    else:
        p=z/4
        expected=(4-z)**2/48
    if z==1:
        continue
    algebra=(1-z)*((1+p)**2-z)/(3-4*z+4*p)
    assert algebra==expected

print('VERIFY_OK', 'witnesses=',witness_count, 'projected_grid=',grid_tests,
      'spatial_orientations=',orientations, 'transition_heights=',
      (T1,T2,T3), 'plateau=',T3)
