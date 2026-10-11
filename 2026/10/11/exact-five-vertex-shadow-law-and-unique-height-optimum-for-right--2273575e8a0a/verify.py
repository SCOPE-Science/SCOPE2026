#!/usr/bin/env python3
"""Independent finite diagnostics for the exact shadow-probability theorem."""
import math, random
from itertools import product

def p(a,b,h):
    z=a*b/math.sqrt((a*a+h*h)*(b*b+h*h))
    return (2/math.pi)*(math.atan(a/h)+math.atan(b/h)-2*math.asin(z))

def F(a,b,t):
    s=a*a+b*b; c=a*b
    return 2*c*(2*t+s)/((t+c)*math.sqrt(t+s))

def t_opt(a,b):
    l=0.0; u=max(a,b)**2
    while F(a,b,u)>a+b: u*=2
    for _ in range(105):
        m=(l+u)/2
        if F(a,b,m)>a+b: l=m
        else: u=m
    return (l+u)/2

def hull_count(points):
    pts=sorted(points)
    def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p0 in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p0)<=0:lo.pop()
        lo.append(p0)
    hi=[]
    for p0 in pts[::-1]:
        while len(hi)>=2 and cross(hi[-2],hi[-1],p0)<=0:hi.pop()
        hi.append(p0)
    return len(lo)+len(hi)-2

def projected_hull_count(a,b,h,normal):
    # Independent 3D orthogonal projection using an explicit orthonormal basis.
    ux,uy,uz=normal
    L=math.hypot(ux,uy)
    if L<1e-12: return 4
    e=(-uy/L,ux/L,0.0)
    f=(-uz*ux/L,-uz*uy/L,L)
    verts=[(sa*a,sb*b,0.) for sa,sb in product((-1,1),repeat=2)]+[(0.,0.,h)]
    pts=[(sum(x*y for x,y in zip(v,e)),sum(x*y for x,y in zip(v,f))) for v in verts]
    return hull_count(pts)

rng=random.Random(20261008)
for a,b,h in [(1.,1.,1.),(1.,1.,math.sqrt(2)),(0.5,2.,1.),(1.,3.,2.),(2.,2.,0.1),(1.,8.,3.)]:
    samples=5000; total=0
    for _ in range(samples):
        z=rng.uniform(-1,1); phi=rng.uniform(0,2*math.pi)
        w=math.sqrt(1-z*z)
        total+=int(projected_hull_count(a,b,h,(w*math.cos(phi),w*math.sin(phi),z))==5)
    assert abs(total/samples-p(a,b,h))<0.04,(a,b,h,total/samples,p(a,b,h))
    t=t_opt(a,b); ht=math.sqrt(t)
    assert abs(F(a,b,t)-(a+b))<2e-12
    assert p(a,b,0.93*ht)<p(a,b,ht)
    assert p(a,b,1.07*ht)<p(a,b,ht)
for t in [0.2,0.8,1.,1.5,3.]:
    s=4.;delta=1.e-5
    def shape_value(ss):
        r=(ss+math.sqrt(ss*ss-4))/2
        return p(math.sqrt(r),1/math.sqrt(r),math.sqrt(t))
    target=math.sqrt(t)/(math.pi*(t*t+t*s+1))*((t-1)/math.sqrt(s+2)+2/math.sqrt(t+s))
    approx=(shape_value(s+delta)-shape_value(s-delta))/(2*delta)
    assert target>0 and abs(target-approx)<2e-8,(target,approx)
for r in [1e3,1e4,1e5]:
    h=math.sqrt(t_opt(r,1.))
    c=(1-p(r,1,h))*math.sqrt(r)
    assert abs(c-4/math.pi)<0.06,(r,c)
assert abs(p(1,1,math.sqrt(2))-0.3509593121836436)<1e-13
print('VERIFY_OK: independent planar hulls, exact law, strict height optimum, fixed-area derivative, and thin-base asymptotics')
