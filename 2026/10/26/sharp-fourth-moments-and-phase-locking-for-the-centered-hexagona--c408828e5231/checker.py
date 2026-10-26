#!/usr/bin/env python3
"""Reproduce finite algebraic and numerical checks for the centered hexagonal Fourier packet.
Public mathematics and reproducibility only; never a substitute for the proof.
"""
import cmath
import math
import random
from collections import defaultdict

ROOTS = ((1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1))
SUPPORT = ((0,0),) + ROOTS


def l4_moment(coeff):
    conv = defaultdict(complex)
    for i, x in enumerate(SUPPORT):
        for j, y in enumerate(SUPPORT):
            conv[(x[0]+y[0],x[1]+y[1])] += coeff[i]*coeff[j]
    return sum(abs(z)**2 for z in conv.values())


def critical_t():
    def p(t):
        return 2*t*t*t+6*t*t-3*t-12
    lo, hi = 0.0, 4.0
    for _ in range(110):
        mid = (lo+hi)/2
        if p(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def best_constant(t):
    return (t**4+36*t*t+48*t+90)/(t*t+6)**2


def complex_maximizer(t, a, b):
    vals=[t]
    vals.extend(cmath.exp(1j*(x*a+y*b)) for x,y in ROOTS)
    return vals


def tests():
    rng = random.Random(0xA2026)
    count=0
    t=critical_t(); K=best_constant(t)
    assert 1.3580109426<t<1.3580109428
    assert 3.6562899692<K<3.6562899694
    count+=2
    # Exact combinatorial constant-coefficient fourth moments.
    assert l4_moment([1]*7)==175
    assert l4_moment([0]+[1]*6)==90
    count+=2
    # Shell fourth moment has an independent closed autocorrelation expression.
    for _ in range(300):
        mags=[rng.random()*4 for j in range(6)]
        B=sum(x*x for x in mags)
        pairprod=[mags[0]*mags[1],mags[2]*mags[3],mags[4]*mags[5]]
        expr=2*B*B-sum(x**4 for x in mags)+8*sum(pairprod[i]*pairprod[j] for i in range(3) for j in range(i+1,3))
        assert abs(l4_moment([0]+mags)-expr)<1e-8
        assert expr<=2.5*B*B+1e-8
        count+=2
    # Exact polynomial identity at 50 integer center/arm choices.
    for aa in range(10):
        for bb in range(5):
            calculated=l4_moment([aa]+[bb]*6)
            expected=aa**4+36*aa*aa*bb*bb+48*aa*bb**3+90*bb**4
            assert calculated==expected,(aa,bb,calculated,expected)
            count+=1
    for _ in range(1500):
        coeff=[complex(rng.uniform(-2,2),rng.uniform(-2,2)) for i in range(7)]
        B=sum(abs(z)**2 for z in coeff)
        assert l4_moment(coeff)<=K*B*B+2e-10*max(1.,B*B)
        count+=1
    for _ in range(400):
        u,v=rng.uniform(-5,5),rng.uniform(-5,5)
        coeff=complex_maximizer(t,u,v)
        assert abs(l4_moment(coeff)-K*(sum(abs(z)**2 for z in coeff))**2)<5e-11
        count+=1
    # Exact discrete orthogonality for all squared frequency sums, q>=5.
    for q in (5,6,7):
        for _ in range(8):
            coeff=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for i in range(7)]
            avg=sum(abs(sum(c*cmath.exp(2j*math.pi*(x*j+y*k)/q) for c,(x,y) in zip(coeff,SUPPORT)))**4 for j in range(q) for k in range(q))/q**2
            assert abs(avg-l4_moment(coeff))<2e-11
            count+=1
    # Tensor inequality: the 6 allowed corners have norm 3/sqrt(2).
    corners=((0,1,0),(0,0,1),(1,0,1),(1,1,0),(0,0,0),(1,1,1))
    for _ in range(1000):
        r=[[rng.random(),rng.random()] for j in range(3)]
        cube=sum(r[0][i]*r[1][j]*r[2][k] for i,j,k in corners)
        upper=3/math.sqrt(2)*math.prod(math.hypot(*p) for p in r)
        assert cube<=upper+1e-12
        count+=1
    # Strict peak and boundary checks.
    for s in (0.,.01,.1,.5,1.,1.35,1.36,2.,5.,10.,100.):
        assert best_constant(s) <= K+1e-12
        count+=1
    print('checks_passed',count,'t=',format(t,'.15g'),'K=',format(K,'.15g'))

if __name__=='__main__':
    tests()
