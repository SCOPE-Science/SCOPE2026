"""Numerical checks for quadratic Euclidean ball-proximal spectral-length bounds.

Run: python3 verify.py
Uses only the Python standard library.  The proof is analytical; tests are finite.
"""
from math import sqrt, log, exp, floor
from random import Random
from fractions import Fraction


def norm(x):
    return sqrt(sum(a*a for a in x))


def ball_step(eigs, x, radius):
    assert radius > 0 and all(v > 0 for v in eigs)
    if norm(x) <= radius:
        return [0.0 for _ in x], None

    def displacement(s):
        return norm([v * (s*a)/(1+s*a) for a,v in zip(eigs,x)])

    lo,hi = 0., 1.
    while displacement(hi) < radius:
        hi *= 2
    for _ in range(90):
        mid=(lo+hi)*.5
        if displacement(mid) < radius:
            lo=mid
        else:
            hi=mid
    s=(lo+hi)*.5
    return [v/(1+s*a) for a,v in zip(eigs,x)], s


def test_one(eigs,x,radii):
    x=list(x)
    D=norm(x)
    if D == 0: return 0
    minimum=min(eigs)
    p=1+int(floor(log(max(eigs)/minimum,2)+1e-13))
    groups=[[] for _ in range(p)]
    for j,a in enumerate(eigs):
        ix=int(floor(log(a/minimum,2)+1e-13))
        groups[min(ix,p-1)].append(j)
    band_sum=[0.0]*p
    total=0.
    checks=0
    for radius in radii:
        y,s=ball_step(eigs,x,radius)
        dist=norm([a-b for a,b in zip(x,y)])
        assert dist <= radius+1e-8
        if s is not None:
            assert abs(dist-radius)<=1e-8*(1+radius)
            for a,b,la in zip(x,y,eigs):
                assert abs(b-a/(1+s*la))<=1e-11*(1+abs(a))
                checks+=1
        for j,g in enumerate(groups):
            u=[x[i] for i in g]
            v=[y[i] for i in g]
            movement=norm([uu-vv for uu,vv in zip(u,v)])
            decrement=norm(u)-norm(v)
            assert movement <= 2*decrement+2e-9*(1+norm(u))
            band_sum[j]+=movement
            checks+=1
        total+=dist
        x=y
        if norm(x)<1e-13:break
    assert total<=2*sqrt(p)*D+1e-8
    assert total<=sqrt(len(eigs))*D+1e-8
    return checks


def gf_arclength(eigs,x,S=1.):
    # Composite Simpson quadrature in the natural logarithmic variable s=e^z.
    # Integrate [2^-p,S] and [0,2^-p] separately by Simpson's rule.
    p=len(eigs)
    s0=2.**(-p)
    def integrand(s):
        return norm([la*v*exp(-la*s) for la,v in zip(eigs,x)])
    def simpson(a,b,N):
        assert N%2==0
        h=(b-a)/N
        ans=integrand(a)+integrand(b)
        for j in range(1,N):
            ans+=(4 if j%2 else 2)*integrand(a+j*h)
        return ans*h/3
    # Dense small interval and log mapped quadrature for the remainder.
    left=simpson(0,s0,400)
    aa=log(s0);bb=log(S);N=5000;h=(bb-aa)/N
    def f(z):
        s=exp(z)
        return integrand(s)*s
    rest=f(aa)+f(bb)
    for j in range(1,N):
        rest+=(4 if j%2 else 2)*f(aa+j*h)
    return left+rest*h/3


def run():
    rng=Random(20261016)
    checks=0
    for _ in range(180):
        d=rng.randrange(1,18)
        eigs=[exp(rng.uniform(-2,11)) for _ in range(d)]
        x=[rng.uniform(-2,2) for _ in range(d)]
        radii=[rng.uniform(.001,.6) for _ in range(300)]
        checks+=test_one(eigs,x,radii)
    # Algebraic resolvent identity on rational SPD diagonal data.
    eigs=[Fraction(1),Fraction(2)]
    x=[Fraction(5),Fraction(7)]
    s=Fraction(1,3)
    y=[xx/(1+s*a) for xx,a in zip(x,eigs)]
    assert y == [Fraction(15,4),Fraction(21,5)]
    assert all(xi-yi==s*la*yi for xi,yi,la in zip(x,y,eigs))
    checks+=3
    c=exp(-.5)-exp(-1.)
    for p in (4,8,16,24,32):
        eigs=[2.**j for j in range(p)]
        x=[1./sqrt(p) for _ in range(p)]
        L=gf_arclength(eigs,x)
        assert L+1e-5>=c*sqrt(p)
        print('p=%d kappa=2^%d GF-length-through-time1=%.9f lower=%.9f' % (p,p-1,L,c*sqrt(p)))
        checks+=1
        # Comparison with implicit normalized-flow trajectories at decreasing radius.
        if p in (4,8,16,24):
            h=.006
            y=list(x)
            n=0
            while norm(y)>h and n<10000:
                y,_=ball_step(eigs,y,h)
                n+=1
            assert n<10000
            print('  radius=%.3f nonterminal=%d path-lower=%.6f' %(h,n,n*h))
            assert (n+1)*h >= c*sqrt(p)-.20
            checks+=1
    print('PASS:',checks,'finite checks')

if __name__=='__main__':
    run()
