#!/usr/bin/env python3
"""Independent standard-library numerical checks of the type-resolved tetrahedral shadow law.

The mathematical proof, not these finite checks, establishes the all-direction result.
"""
import math
import random

PI = math.pi
R0 = 2 * math.sqrt(2)
R1 = 4 * math.sqrt(2 / 3)
R2 = 2 * math.sqrt(3)
P3 = 1 - 6 * math.asin(1 / 3) / PI
P4 = 1 - P3
VERTICES = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))


def clamp(x):
    return max(-1.0, min(1.0, x))


def segment(h, t):
    """Spherical cap/hemisphere crossing area, unit sphere."""
    if t >= math.sqrt(1 - h * h):
        return 0.0
    if not (0 < h < 1 and 0 < t < 1):
        raise ValueError('expected the stated positive segment domain')
    return 2 * (math.acos(clamp(h / math.sqrt(1 - t*t)))
                - t * math.acos(clamp(h*t / math.sqrt((1-h*h)*(1-t*t)))))


def cdf_three(r):
    if r <= R0:
        return 0.0
    if r >= R2:
        return P3
    t = r/(2*math.sqrt(3))
    return P3 - 4*(1-t) + 6*segment(1/3,t)/PI


def cdf_four(r):
    if r <= R0:
        return 0.0
    if r >= 4:
        return P4
    t = r/4
    return P4 - 3*(1-t) + 6*segment(1/math.sqrt(3),t)/PI


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def cross(x,y):
    return (x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])


def convex_shadow(u):
    """Independent polygon projection/cross-product hull; no brightness identity used."""
    reference=(0,0,1) if abs(u[2]) < 0.9 else (1,0,0)
    e=cross(u, reference)
    norm=math.sqrt(dot(e,e)); e=tuple(t/norm for t in e)
    f=cross(u,e)
    points=sorted((dot(v,e),dot(v,f)) for v in VERTICES)
    def zcross(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lower=[];upper=[]
    for p in points:
        while len(lower)>1 and zcross(lower[-2],lower[-1],p)<=1e-12:lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper)>1 and zcross(upper[-2],upper[-1],p)<=1e-12:upper.pop()
        upper.append(p)
    hull=lower[:-1]+upper[:-1]
    a=abs(sum(hull[i][0]*hull[(i+1)%len(hull)][1] - hull[i][1]*hull[(i+1)%len(hull)][0]
             for i in range(len(hull)))/2)
    return a,len(hull)


def independent_segment_quadrature(h,t,steps=12000):
    """Surface-integration of the cap/hemisphere intersection over polar angle."""
    lo=math.asin(h);hi=math.acos(t)
    if hi<=lo:return 0.
    step=(hi-lo)/steps
    def f(th):
        v=h*math.cos(th)/(math.sqrt(1-h*h)*math.sin(th))
        return 2*math.acos(clamp(v))*math.sin(th)
    s=f(lo)+f(hi)
    for k in range(1,steps):
        s+=(4 if k%2 else 2)*f(lo+k*step)
    return s*step/3


def normal(rng):
    v=[rng.gauss(0,1) for _ in range(3)]
    d=math.sqrt(dot(v,v))
    return tuple(z/d for z in v)


def check():
    cases=0
    # Piecewise endpoints and type probabilities.
    assert abs(P3+P4-1)<1e-14
    assert abs(cdf_three(R0))<1e-14 and abs(cdf_four(R0))<1e-14
    assert abs(cdf_three(R2)-P3)<1e-14 and abs(cdf_four(4)-P4)<1e-14
    assert abs(cdf_three(R1)-(P3-4*(1-R1/(2*math.sqrt(3)))))<1e-13
    assert abs(cdf_four(R1)-(P4-3*(1-R1/4)))<1e-13
    cases+=7
    # Independent spherical cap/hemisphere surface integrations.
    for h,t in ((1/3,.83),(1/3,.90),(1/math.sqrt(3),.72),(1/math.sqrt(3),.76)):
        x=segment(h,t);y=independent_segment_quadrature(h,t)
        assert abs(x-y)<2e-7,(h,t,x,y)
        cases+=1
    # Both lower tails have the same proved quadratic limit.
    k=3/(2*math.sqrt(2)*PI)
    for eps in (0.02,0.01,0.005,0.002):
        v3=cdf_three(R0+eps)/eps**2
        v4=cdf_four(R0+eps)/eps**2
        assert abs(v3-k)<.55*eps and abs(v4-k)<.3*eps,(eps,v3,v4,k)
        cases+=2
    # Integrating the full sub-CDF recovers independently published conditional moments.
    # These moment values are prior-known and are not asserted as new.
    def simpson(fun, lo, hi, nsteps=12000):
        h=(hi-lo)/nsteps
        val=fun(lo)+fun(hi)
        for i in range(1,nsteps):
            val+=(4 if i%2 else 2)*fun(lo+i*h)
        return val*h/3
    omega=PI/2-3*math.asin(1/3)
    targets=((cdf_three,R2,P3,PI/(math.sqrt(3)*omega),4+8*math.sqrt(2)/(3*omega)),
             (cdf_four,4,P4,2*PI/(3*math.sqrt(3)*math.asin(1/3)),
              16/3+16*math.sqrt(2)/(9*math.asin(1/3))))
    for fun,hi,prob,mean,moment2 in targets:
        mu=(hi*prob-simpson(fun,R0,hi))/prob
        m2=(hi*hi*prob-simpson(lambda r:2*r*fun(r),R0,hi))/prob
        assert abs(mu-mean)<1e-7 and abs(m2-moment2)<1e-6,(mu,mean,m2,moment2)
        cases+=2
    # Independent polygon computation for actual viewing directions.
    rng=random.Random(180734)
    for j in range(700):
        u=normal(rng);t=tuple(abs(v) for v in u)
        area=2*max(sum(t),2*max(t))
        typ=3 if sum(t)>2*max(t) else 4
        check_area,n=convex_shadow(u)
        assert abs(check_area-area)<1e-10,(check_area,area,u)
        assert n==typ,(u,n,typ)
        cases+=2
    # Directional monotonicity and CDF range.
    for j in range(1,2000):
        r=R0+(4-R0)*j/2000
        v3,v4=cdf_three(r),cdf_four(r)
        assert -1e-10<=v3<=P3+1e-10 and -1e-10<=v4<=P4+1e-10
        assert v3>=cdf_three(r-1e-8)-1e-11 and v4>=cdf_four(r-1e-8)-1e-11
        cases+=2
    # Independently generated Haar directions yield approximate frequencies.
    thresholds=(2.85,2.95,3.,3.10,3.2,R1,3.34,R2,3.65,3.8,3.95)
    count_3=[0]*len(thresholds);count_4=[0]*len(thresholds)
    n=400_000;tri_count=0
    for _ in range(n):
        u=normal(rng);v=list(map(abs,u));is3=sum(v)>2*max(v)
        a=2*max(sum(v),2*max(v))
        if is3:tri_count+=1
        for j,threshold in enumerate(thresholds):
            if a<=threshold:
                if is3:count_3[j]+=1
                else:count_4[j]+=1
    assert abs(tri_count/n-P3)<.003
    for j,r in enumerate(thresholds):
        assert abs(count_3[j]/n-cdf_three(r))<.003,(r,'tri',count_3[j]/n,cdf_three(r))
        assert abs(count_4[j]/n-cdf_four(r))<.003,(r,'quad',count_4[j]/n,cdf_four(r))
        cases+=2
    cases+=1
    print(f'PASS: {cases} deterministic checks and {n:,} independent Haar-random directions')
    print('P(N=3)=',format(P3,'.15g'),'P(N=4)=',format(P4,'.15g'))
    print('Joint CDF at area=3:',cdf_three(3),cdf_four(3))


if __name__=='__main__':
    check()
