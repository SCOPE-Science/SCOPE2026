#!/usr/bin/env python3
"""Reproducible finite checks for the centrally symmetric cyclic-hexagon normal law.
The theorem's proof is geometric; these random tests are not a proof."""
import math, random, itertools


def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def sub(a,b): return (a[0]-b[0], a[1]-b[1])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def area(poly):
    return abs(sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))/2) if len(poly)>=3 else 0.

def clip(poly,n,b):
    if not poly:return []
    out=[]
    for i in range(len(poly)):
        p=poly[i-1];q=poly[i]
        fp=dot(p,n)-b;fq=dot(q,n)-b
        if (fp>0 and fq<0) or (fp<0 and fq>0):
            t=fp/(fp-fq)
            out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
        if fq<=0:out.append(q)
    return out

def hexagon(gaps):
    a,b,c=gaps
    assert min(gaps)>0 and abs(a+b+c-math.pi)<1e-10
    ang=[0,a,a+b,math.pi,math.pi+a,math.pi+a+b]
    return [(math.cos(t),math.sin(t)) for t in ang]

def strips(vertices):
    S=[]
    for i in range(3):
        e=sub(vertices[(i+1)%6],vertices[i]);ell=math.sqrt(dot(e,e))
        u=(e[0]/ell,e[1]/ell)
        S.append((u,ell/2))
    return S

def p_three(vertices):
    p=vertices[:]
    for u,h in strips(vertices):
        p=clip(p,u,h);p=clip(p,(-u[0],-u[1]),h)
    return area(p)/area(vertices)

def count_direct(p,v):
    n=len(v);s=k=0; tol=1e-12
    for i in range(n):
        a=v[i];b=v[(i+1)%n];e=sub(b,a)
        t=dot(sub(p,a),e)/dot(e,e)
        if tol<t<1-tol:s+=1
        u=sub(v[(i-1)%n],a); w=sub(v[(i+1)%n],a); z=sub(p,a)
        if dot(z,u)>tol and dot(z,w)>tol:k+=1
    return s+k,s,k

def count_strips(p,v):
    return 4*sum(abs(dot(p,u))<h-1e-12 for u,h in strips(v))

def sample_points(v,N,seed):
    rr=random.Random(seed)
    weights=[abs(cross(v[i],v[(i+1)%6])) for i in range(6)]
    cum=list(itertools.accumulate(weights));total=cum[-1]
    import bisect
    for _ in range(N):
        j=bisect.bisect_left(cum,rr.random()*total)
        r=math.sqrt(rr.random());w=rr.random()
        a=v[j];b=v[(j+1)%6]
        yield (r*((1-w)*a[0]+w*b[0]),r*((1-w)*a[1]+w*b[1]))

def test():
    cases=[(math.pi/3,math.pi/3,math.pi/3),
           (math.pi/2,math.pi/4,math.pi/4),
           (2*math.pi/3,math.pi/6,math.pi/6),
           (0.35,1.05,math.pi-1.40),
           (1.8,0.55,math.pi-2.35)]
    total=0
    for j,gaps in enumerate(cases):
        v=hexagon(gaps);nu=p_three(v)
        target={4:nu,8:1-2*nu,12:nu}
        assert 0<nu<0.5
        count={4:0,8:0,12:0}
        for p in sample_points(v,50000,j*113+41):
            n,s,k=count_direct(p,v)
            assert s==k and n==count_strips(p,v),(j,p,n,s,k)
            assert n in count
            count[n]+=1
        err=max(abs(count[z]/50000-target[z]) for z in count)
        assert err<0.018,(j,err,count,target)
        if j==0:assert abs(nu-1/3)<1e-12,nu
        print('case',j,'p4=p12',round(nu,8),'sample',tuple(round(count[z]/50000,5) for z in (4,8,12)), 'maxerr',round(err,5))
        total+=50000
    # Independent stress test of the parity obstruction for an obtuse noncyclic hexagon.
    v=hexagon((math.pi/3,)*3)
    radii=[1.10,0.94,1.03]
    v=[(radii[i%3]*p[0],radii[i%3]*p[1]) for i,p in enumerate(v)]
    for i in range(6):
        u=sub(v[(i-1)%6],v[i]);w=sub(v[(i+1)%6],v[i])
        assert dot(u,w)<0, 'all vertex angles must be obtuse'
    counts={}
    for p in sample_points(v,40000,181):
        n,s,k=count_direct(p,v)
        assert n==s+k and s==k
        counts[n]=counts.get(n,0)+1
    assert counts.get(6,0)>100 and counts.get(10,0)>100,counts
    print('obtuse_noncyclic_obstruction',sorted(counts.items()))
    print('CYCLIC_HEXAGON_NORMAL_CHECK_OK samples='+str(total)+' classifications='+str(total)+' noncyclic_samples=40000')

if __name__=='__main__':test()
