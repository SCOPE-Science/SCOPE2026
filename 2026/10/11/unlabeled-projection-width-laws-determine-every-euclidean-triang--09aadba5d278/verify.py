#!/usr/bin/env python3
"""Finite cross-checks for exact random-direction width law of triangles.
Uses Python, NumPy and SciPy; tests do not replace geometric proof.
"""
import numpy as np, math
from math import pi, acos, sqrt


def lengths_angles(A,B,C):
    P=np.array((A,B,C),dtype=float)
    lengths=np.array([np.linalg.norm(P[1]-P[2]), np.linalg.norm(P[2]-P[0]),np.linalg.norm(P[0]-P[1])])
    a,b,c=lengths
    angles=np.array([acos(np.clip((b*b+c*c-a*a)/(2*b*c),-1,1)),acos(np.clip((c*c+a*a-b*b)/(2*c*a),-1,1)),acos(np.clip((a*a+b*b-c*c)/(2*a*b),-1,1))])
    area=abs(np.linalg.det(np.array([P[1]-P[0],P[2]-P[0]])))/2
    heights=2*area/lengths
    return P,lengths,angles,heights


def cdf_sector(t,s,U,V):
    lo=U-pi/2
    hi=pi/2-V
    if t<=0:return 0.0
    z=acos(max(0,min(1,t/s)))
    return (max(0.0,min(hi,-z)-lo)+max(0.0,hi-max(lo,z)))/pi

def cdf_triangle(t, lengths,angles):
    a,b,c=lengths
    A,B,C=angles
    return cdf_sector(t,a,B,C)+cdf_sector(t,b,C,A)+cdf_sector(t,c,A,B)

def density_triangle(t, lengths,angles,heights):
    a,b,c=lengths;A,B,C=angles; ha,hb,hc=heights
    def term(s,low,high):
        return (1.0/sqrt(s*s-t*t)) if low<t<high else 0.0
    if max(angles)<pi/2-1e-11:
        return (term(a,hb,a)+term(a,hc,a)+term(b,ha,b)+term(b,hc,b)+term(c,ha,c)+term(c,hb,c))/pi
    if abs(max(angles)-pi/2)<1e-11:
        # Relabel until the right angle is at A.
        if abs(A-pi/2)>1e-11:
            i=int(np.argmax(angles)); return density_triangle(t,np.roll(lengths,-i),np.roll(angles,-i),np.roll(heights,-i))
        return (term(a,hb,a)+term(a,hc,a)+term(b,ha,b)+term(c,ha,c))/pi
    # Relabel obtuse vertex to A.
    if A<pi/2:
        i=int(np.argmax(angles)); return density_triangle(t,np.roll(lengths,-i),np.roll(angles,-i),np.roll(heights,-i))
    return (term(a,hb,a)+term(a,hc,a)+term(b,ha,hc)+term(c,ha,hb))/pi

def brute_cdf(P, ts, N=140000):
    th=(np.arange(N)+0.5)*pi/N
    U=np.column_stack((np.cos(th),np.sin(th)))
    proj=U@P.T
    ws=proj.max(axis=1)-proj.min(axis=1)
    return np.array([(ws<=t).mean() for t in ts]), ws

def do_case(P):
    pts,lens,angs,hs=lengths_angles(*P)
    ts=np.linspace(0.01,1.03*max(lens),75)
    pred=np.array([cdf_triangle(t,lens,angs) for t in ts])
    empirical,w=brute_cdf(pts,ts)
    maxcdf=np.max(np.abs(pred-empirical))
    # Numerical integration of pdf via Gauss-Legendre in each subinterval avoiding endpoints.
    from scipy.integrate import quad
    ends=sorted(set([0,*list(lens),*list(hs)]))
    calc=0.0;mass=0.0
    for x,y in zip(ends[:-1],ends[1:]):
        val,e=quad(lambda t:density_triangle(t,lens,angs,hs),x,y,epsabs=2e-9,epsrel=2e-9,limit=100)
        mass+=val
        v,e=quad(lambda t:t*density_triangle(t,lens,angs,hs),x,y,epsabs=2e-9,epsrel=2e-9,limit=100)
        calc+=v
    theo=lens.sum()/pi
    errmean=abs(calc-theo)
    assert maxcdf<1.7e-5,(maxcdf,lens,angs)
    assert abs(mass-1)<1e-8,(mass,lens,angs)
    assert errmean<1e-8,(calc,theo)
    assert abs(np.min(w)-min(hs))<8e-5
    assert abs(np.max(w)-max(lens))<8e-5
    return float(maxcdf),float(abs(mass-1)),float(errmean)

if __name__=='__main__':
    shapes=[((0,0),(4,0),(1.5,3)),((0,0),(3,0),(1.5,4)),((0,0),(4,0),(-1,1)),((0,0),(4,0),(0,3)),((0,0),(3,0),(1.5,math.sqrt(6.75))),((0,0),(3,0),(0,3)),((0,0),(2,0),(.6,1.4)),((0,0),(1.1,0),(-.3,.7))]
    rng=np.random.default_rng(10039)
    for k in range(16):
        aa=rng.uniform(1,5);x=rng.uniform(-1,aa+1);y=rng.uniform(0.5,4)
        shapes.append(((0,0),(aa,0),(x,y)))
    errs=[]
    for P in shapes: errs.append(do_case(P))
    print('VERIFY_OK',len(shapes),'triangle shapes x 75 CDF thresholds / each', 'max_errors',np.max(errs,axis=0))

# Supplementary singularity-weight and signed-jump checks.
def verify_singularities(P):
    pts,ls,ang,hs=lengths_angles(*P)
    amax=float(max(ang));kind='acute' if amax<pi/2-1e-10 else 'right' if abs(amax-pi/2)<1e-10 else 'obtuse'
    # Noncoincident side lengths are dealt with by grouping.
    sorted_lengths=sorted(float(x) for x in ls)
    groups=[]
    for s in sorted_lengths:
        if groups and abs(s-groups[-1][0])<1e-8:
            groups[-1][1]+=1
        else: groups.append([s,1])
    total=0
    for s,m in groups:
        if kind=='acute': wanted=2*m
        elif kind=='right': wanted=(2 if abs(s-max(ls))<1e-8 else m)
        else: wanted=(2 if abs(s-max(ls))<1e-8 else 0)
        eps=1e-9*min(ls)
        test=max(0.0,s-eps)
        empirical=pi*sqrt(s*s-test*test)*density_triangle(test,ls,ang,hs)
        assert abs(empirical-wanted)<0.003, (kind,s,m,wanted,empirical)
        total+=wanted
    assert total=={'acute':6,'right':4,'obtuse':2}[kind]
    if kind=='obtuse':
        i=int(np.argmax(ang)); vals=np.roll(hs,-i); ha,hb,hc=vals
        tiny=1e-8*min(ls)
        at_min=density_triangle(ha+tiny,ls,ang,hs)-density_triangle(max(0,ha-tiny),ls,ang,hs)
        assert at_min>0,at_min
        for h in sorted(set((round(hb,11),round(hc,11)))):
            jump=density_triangle(h+tiny,ls,ang,hs)-density_triangle(h-tiny,ls,ang,hs)
            assert jump<0,(h,jump)
    return kind

if __name__=='__main__':
    categories={}
    for P in shapes:
        k=verify_singularities(P)
        categories[k]=categories.get(k,0)+1
    print('SINGULARITY_CHECKS_OK',categories)
