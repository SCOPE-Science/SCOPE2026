#!/usr/bin/env python3
"""Independent numerical and exact checks of reflected cores of homothetic frusta.

Run with Python 3. No third-party packages are required. The general
claim is proved analytically in RESULT.md; finite checks are diagnostic.
"""
from fractions import Fraction
from math import log, exp


def predicted(m, t):
    if not (isinstance(m, int) and m >= 1 and 0 <= t <= 1):
        raise ValueError('domain')
    q = 2.0 ** (1.0 / m)
    threshold = 1 / (2*q-1)
    if t == 1:
        return .5, 1.0, threshold
    if t <= threshold:
        c = (q-1) / ((1-t)*(2*q-1))
        val = 2 / ((2*q-1)**m*(1-t**(m+1)))
    else:
        c = .5
        val = 2 * (((1+t)/2)**(m+1)-t**(m+1))/(1-t**(m+1))
    return c, val, threshold


def signed_area(P):
    return sum(P[i][0]*P[(i+1)%len(P)][1]-P[i][1]*P[(i+1)%len(P)][0] for i in range(len(P)))/2


def polygon_clip(subject, clipper):
    if signed_area(clipper) < 0:
        clipper = list(reversed(clipper))
    polygon = subject[:]
    for i in range(len(clipper)):
        a = clipper[i]
        b = clipper[(i+1)%len(clipper)]
        def cross(p): return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
        before = polygon
        polygon=[]
        if not before: return []
        for j, cur in enumerate(before):
            prev=before[j-1]
            cp,cc = cross(prev),cross(cur)
            if (cp < -1e-12) != (cc < -1e-12):
                fraction=cp/(cp-cc)
                polygon.append((prev[0]+fraction*(cur[0]-prev[0]),prev[1]+fraction*(cur[1]-prev[1])))
            if cc >= -1e-12: polygon.append(cur)
    return polygon


def trapezoid_ratio(t, cx, cy):
    T=[(-1.,0.),(1.,0.),(t,1.),(-t,1.)]
    R=[(2*cx-x,2*cy-y) for x,y in T]
    I=polygon_clip(T,R)
    return abs(signed_area(I)) / (1+t) if len(I)>=3 else 0.


def golden_maximum(fun,a=0.,b=1.):
    gr=(5**.5-1)/2
    c=b-gr*(b-a); d=a+gr*(b-a)
    fc=fun(c);fd=fun(d)
    for _ in range(90):
        if fc>fd:
            b,d,fd=d,c,fc
            c=b-gr*(b-a);fc=fun(c)
        else:
            a,c,fc=c,d,fd
            d=a+gr*(b-a);fd=fun(d)
    return ((a+b)/2,fun((a+b)/2))


def interval_overlap(r1,r2,shift):
    return max(0.0,min(r1,shift+r2)-max(-r1,shift-r2))


def square_frustum_ratio(t, cx, cy, cz, n=6000):
    lo=max(0,2*cz-1);hi=min(1,2*cz)
    if hi<=lo:return 0.
    h=(hi-lo)/n
    total=0.
    for i in range(n):
        z=lo+(i+.5)*h
        z2=2*cz-z
        r1=1-(1-t)*z
        r2=1-(1-t)*z2
        total+=interval_overlap(r1,r2,2*cx)*interval_overlap(r1,r2,2*cy)
    return (total*h)/(4*(1+t+t*t)/3)


def planar_examples():
    tests=(0.,.08,1/3,.40,.65,.91,.999)
    for t in tests:
        center,val,_ = predicted(1,t)
        independent=trapezoid_ratio(t,0,center)
        assert abs(independent-val)<5e-12,(t,independent,val)
        best=golden_maximum(lambda cy:trapezoid_ratio(t,0,cy))
        assert abs(best[1]-val)<3e-9,(t,best,val)
        assert abs(best[0]-center)<1e-5,(t,best,center)
        for dx in (-.015,.023,.07):
            assert trapezoid_ratio(t,dx,center)<val-1e-8,(t,dx)
    print('INDEPENDENT_PLANAR_CONVEX_CLIPPING_PASSED',len(tests))


def square_examples():
    tests=((0.,0.),(.22,0.),(.50,0.),(.65,0.),(.95,0.))
    for t,_ in tests:
        center,val,_=predicted(2,t)
        independent=square_frustum_ratio(t,0,0,center)
        assert abs(independent-val)<4e-7,(t,independent,val)
        for dz in (-.05,.05):
            if 0<center+dz<1:
                v=square_frustum_ratio(t,0,0,center+dz)
                assert v<val-1e-6,(t,dz,v,val)
        off=square_frustum_ratio(t,.04,-.025,center)
        assert off<val-1e-5,(t,off,val)
    print('INDEPENDENT_SQUARE_BASE_VOLUME_QUADRATURE_PASSED',len(tests))


def exact_linear_checks():
    # The planar threshold and normalized overlap reduce to exact fractions.
    assert Fraction(1, 2*2-1)==Fraction(1,3)
    for t in (Fraction(0),Fraction(1,10),Fraction(1,3)):
        core=Fraction(2,3)*(1/(1-t*t))
        assert core<=1 and core>=Fraction(2,3)
        c=Fraction(1,3)/(1-t)
        assert 0<c<=Fraction(1,2)
    for t in (Fraction(1,3),Fraction(1,2),Fraction(4,5)):
        core=(1+3*t)/(2*(1+t))
        assert core>=Fraction(3,4) and core<1
    print('EXACT_PLANAR_THRESHOLD_AND_BRANCH_IDENTITIES_PASSED')


def crossover_checks():
    L=log(2)
    for tau in (0,.25,.9,2*L,2.0,4.0,8.0):
        m=30000
        t=1-tau/m
        _,v,_=predicted(m,t)
        target=(2/(1+exp(tau/2))) if tau<=2*L else (1/(2*(1-exp(-tau))))
        assert abs(target-v)<.001,(tau,target,v)
    for m in (1,2,3,5,10,20,50):
        values=[predicted(m,j/20)[1] for j in range(21)]
        # At tiny t and large m, a strictly positive term t**(m+1) is
        # below machine precision. Diagnose monotonicity up to roundoff.
        assert all(values[i+1] >= values[i]-2e-15 for i in range(20)),m
        assert all(values[i+1]>values[i] for i in range(10,20)),m
    print('DIMENSIONAL_CROSSOVER_AND_MONOTONICITY_DIAGNOSTICS_PASSED')


if __name__=='__main__':
    exact_linear_checks()
    planar_examples()
    square_examples()
    crossover_checks()
    print('ALL_CHECKS_PASSED')
