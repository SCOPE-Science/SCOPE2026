"""Numerical consistency checks for renewal first-passage fluctuation monotonicity.

Pure-Python checks, with no claims of exhaustive verification.
"""
from math import exp, expm1, isfinite
import random


def mixture_values(lengths, weights, q):
    assert all(v > 0 for v in lengths)
    assert all(w >= 0 for w in weights)
    assert abs(sum(weights)-1.0) < 1.e-12
    m = sum(v*w for v,w in zip(lengths,weights))
    e = sum(w*exp(-q*v) for v,w in zip(lengths,weights))
    b = (1-e)/m
    bp = sum(w*v*exp(-q*v) for v,w in zip(lengths,weights))/m
    bpp = -sum(w*v*v*exp(-q*v) for v,w in zip(lengths,weights))/m
    z=q
    assert 0 < b < z
    h=z*z+z*z*bp-z*b-b*b
    f=h/(z-b)**2
    g=3*b*b-5*b*bp*z-b*bpp*z*z-b*z+2*bp*bp*z*z+bp*z*z+bpp*z**3
    derivative=g/(z-b)**3
    return f,derivative,g,m


def core_kernel(x,y):
    ax=-expm1(-x)
    ay=-expm1(-y)
    lx=1-(1+x)*exp(-x)
    ly=1-(1+y)*exp(-y)
    return (-x*y*(x*exp(-x)*ay+y*exp(-y)*ax)+(6-x-y)*lx*ly)/2


def independent_kernel(lengths,weights,q):
    return sum(w*ww*core_kernel(q*v,q*u)
               for v,w in zip(lengths,weights)
               for u,ww in zip(lengths,weights))


def run_tests():
    rng=random.Random(8122024)
    checks=0
    max_rel=0
    for i in range(300):
        n=1+rng.randrange(5)
        lengths=[exp(rng.uniform(-1.4,1.4)) for j in range(n)]
        raw=[rng.expovariate(1) for j in range(n)]
        weights=[r/sum(raw) for r in raw]
        q=exp(rng.uniform(-1.0,2.2))
        f,df,g,m=mixture_values(lengths,weights,q)
        kernel=independent_kernel(lengths,weights,q)
        discrepancy=abs(g*m*m-kernel)
        scale=1+abs(g*m*m)+abs(kernel)
        rel=discrepancy/scale
        max_rel=max(max_rel,rel)
        assert rel<2e-11,(i,rel)
        assert g <0 and df <0 and f>1, (i,f,df)
        d=1e-4*min(1.0,q)
        plus=mixture_values(lengths,weights,q+d)[0]
        minus=mixture_values(lengths,weights,q-d)[0]
        approx=(plus-minus)/(2*d)
        assert abs(approx-df) <= 0.0002*(1+abs(df)),(i,approx,df)
        checks+=1
    print('PASS: %d distinct mixtures; covariance-square derivative and kernel agree.' % checks)
    print('Maximum normalized algebraic residual:',max_rel)
    print('All tested derivatives strictly negative and CV squared > 1.')
    for aa in [0.0,0.2,0.6,0.95]:
        a,b=1-aa,1+aa
        for q in [0.1,0.4,1,2,5,12]:
            f,d,_,_=mixture_values([a,b],[0.5,0.5],q)
            assert d<0 and f>1
    print('PASS: 24 uniform-interval target configurations (inside support).')
    for q in [0.5,1,2,4,16,128]:
        f,_,_,_=mixture_values([1],[1.0],q)
        print('Center-target uniform-distance law, q=%g: CV^2=%.9f'%(q,f))

if __name__=='__main__':
    run_tests()
