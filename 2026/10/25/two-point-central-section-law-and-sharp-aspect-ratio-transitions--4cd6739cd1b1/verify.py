#!/usr/bin/env python3
"""Independent numerical checks for square-antiprism central-plane sections.

Requires Python 3 standard library only. The analytical proof is in RESULT.md;
finite checks do not certify statements for all parameters or directions.
"""
import math
import random
import itertools

PI = math.pi
SQRT2 = math.sqrt(2.0)


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def norm(a):
    return math.sqrt(dot(a,a))

def vertices(h):
    return [(math.cos(k*PI/2),math.sin(k*PI/2),h) for k in range(4)]+[(math.cos(PI/4+k*PI/2),math.sin(PI/4+k*PI/2),-h) for k in range(4)]

def brute_edges(v):
    """Reconstruct actual hull edges via distinct supporting face planes."""
    result=[]
    for i,j in itertools.combinations(range(len(v)),2):
        planes=[]
        for k in range(len(v)):
            if k in (i,j):continue
            n=cross(sub(v[j],v[i]),sub(v[k],v[i]))
            if norm(n)<1e-10:continue
            d=[dot(n,sub(x,v[i])) for x in v]
            if max(d)>1e-9 and min(d)<-1e-9:continue
            if max(d)<=1e-9:n=tuple(-x for x in n)
            n=tuple(x/norm(n) for x in n)
            if not any(norm(sub(n,p))<1e-7 for p in planes):planes.append(n)
        if len(planes)>=2:result.append((i,j))
    return result

def predicted_edges():
    return sorted(tuple(sorted(pair)) for k in range(4) for pair in [(k,(k+1)%4),(4+k,4+(k+1)%4),(k,4+k),(k,4+(k-1)%4)])

def count_sign_crossings(v,edges,u):
    s=[dot(u,x) for x in v]
    return sum(s[i]*s[j]<0 for i,j in edges)

def projected_section_hull_count(v,edges,u):
    zaxis=(0,0,1) if abs(u[2])<.9 else (0,1,0)
    e1=cross(u,zaxis)
    e1=tuple(x/norm(e1) for x in e1)
    e2=cross(u,e1)
    hits=[]
    values=[dot(u,x) for x in v]
    for i,j in edges:
        a,b=values[i],values[j]
        if a*b>=0:continue
        t=a/(a-b)
        x=tuple((1-t)*v[i][q]+t*v[j][q] for q in range(3))
        hits.append((dot(x,e1),dot(x,e2)))
    assert len(hits)>=3
    # Monotone-chain hull from section points, independent of crossing count.
    hits=sorted(hits)
    def o(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[]
    for p in hits:
        while len(lo)>=2 and o(lo[-2],lo[-1],p)<1e-11:lo.pop()
        lo.append(p)
    hi=[]
    for p in hits[::-1]:
        while len(hi)>=2 and o(hi[-2],hi[-1],p)<1e-11:hi.pop()
        hi.append(p)
    return len(lo[:-1]+hi[:-1])

def p8(h):
    return 1.0-8.0/PI*(math.asin(math.cos(PI/8)/math.sqrt(1+h*h))-math.asin(1/math.sqrt(2*(1+h*h))))

def p8_from_edge_angles(h):
    r2=1+h*h
    alpha=math.acos(h*h/r2)
    beta=math.acos((1/SQRT2-h*h)/r2)
    return 4*(alpha+beta)/PI-3

def threshold(u,h):
    x,y,z=u
    if z<0:x,y,z=-x,-y,-z
    theta=math.atan2(y,x)%(PI/2)
    if theta>PI/4:theta=PI/2-theta
    c=h*z/math.hypot(x,y)
    t=max(math.sin(theta),math.cos(theta+PI/4))
    return 8 if c>t else 6

def gnorm(rng):
    a=tuple(rng.gauss(0,1) for _ in range(3))
    n=norm(a)
    return tuple(x/n for x in a)

E=predicted_edges()
assert len(E)==16
for h in [0.1,2**(-3/4),0.8,2.5]:
    v=vertices(h)
    assert sorted(brute_edges(v))==E
print('INDEPENDENT_SUPPORTING_PLANE_HULL_16_EDGES_OK')

for h in [0.15,2**(-3/4),1.75]:
    v=vertices(h)
    rng=random.Random(8394+round(h*1000))
    for _ in range(1200):
        u=gnorm(rng)
        n=count_sign_crossings(v,E,u)
        assert n==threshold(u,h),(h,u,n,threshold(u,h))
        assert projected_section_hull_count(v,E,u)==n
print('EXPLICIT_ORIENTATION_THRESHOLD_AND_INDEPENDENT_PLANE_HULL_OK_3600')

for h in [.04,.12,.3,2**(-3/4),1.,4.,20.]:
    p=p8(h)
    assert 0<p<1
    assert abs(p-p8_from_edge_angles(h))<1e-12,(h,p,p8_from_edge_angles(h))
    intervals=180000
    acc=0.0
    for i in range(intervals):
        phi=(i+.5)*PI/(4*intervals)
        t=max(math.sin(phi),math.cos(phi+PI/4))
        acc+=1-t/math.sqrt(h*h+t*t)
    pnum=acc/intervals
    assert abs(p-pnum)<3e-10,(h,p,pnum)
print('INDEPENDENT_EDGE_ANGLE_MEAN_AND_CONDITIONAL_SPHERE_QUADRATURE_OK')

h=2**(-3/4)
exact=8/PI*math.acos((2*SQRT2-1)/7)-3
assert abs(exact-p8(h))<1e-14
assert abs(exact-0.32704409713846822257)<1e-13
print('EQUAL_EDGE_ANTIPRISM_CLOSED_FORM_OK')

for h in [0.004,0.003,0.002]:
    assert abs(p8(h)/h**2/(4*SQRT2/PI)-1)<2e-4
for h in [300.,1000.,2500.]:
    c=8/PI*(math.cos(PI/8)-1/SQRT2)
    assert abs((1-p8(h))*h/c-1)<1e-4
print('SHARP_THIN_QUADRATIC_AND_TALL_INVERSE_HEIGHT_COEFFICIENTS_OK')

for h,seed,number,eps in [(2**(-3/4),43080,180000,0.004),(.2,99104,120000,0.004),(2.,71150,120000,0.004)]:
    rng=random.Random(seed)
    v=vertices(h)
    m=sum(count_sign_crossings(v,E,gnorm(rng))==8 for _ in range(number))
    empirical=m/number
    predicted=p8(h)
    assert abs(empirical-predicted)<eps,(h,empirical,predicted)
    print('INDEPENDENT_GAUSSIAN_SPHERE_SAMPLING_OK',h,number,round(empirical,6),round(predicted,6))
print('ALL_SQUARE_ANTIPRISM_CENTRAL_SECTION_CHECKS_OK')
