#!/usr/bin/env python3
"""Independent numerical probes for the explicit Scarpi-CQ phase formulas.

The mathematical assertions are proved analytically in RESULT.md; floating-point
checks below do not establish uniqueness of roots or infinite-domain assertions.
Run with Python 3 standard library: python verify_scarpi.py
"""
import math
import random


def psi(s, a, b, c):
    B = (a*s+b*c)/(s+c)
    return math.exp(-B*math.log(s))


def Q(x, a, b, c):
    return a*x+b/x+a+b+(a-b)*math.log(c*x)


def Theta(a,b,c):
    return 2*(a+b)+(a-b)*math.log(c*b/a)


def omega1(h,a,b,c):
    x = 1/(c*h)
    return psi(1/h,a,b,c)*Q(x,a,b,c)/(c*h*(1+x)**2)


def roots(a,b,c):
    assert Theta(a,b,c)<0
    x0=b/a
    l=x0
    while Q(l,a,b,c)<=0:
        l*=.5
    r=x0
    while Q(r,a,b,c)<=0:
        r*=2
    def bisect(lo,hi):
        flo=Q(lo,a,b,c)
        for _ in range(110):
            mi=.5*(lo+hi)
            if (Q(mi,a,b,c)>0)==(flo>0):
                lo=mi
            else:
                hi=mi
        return .5*(lo+hi)
    return bisect(l,x0),bisect(x0,r)


def close(x,y,rel=2e-6,abs_tol=1e-10):
    assert math.isclose(x,y,rel_tol=rel,abs_tol=abs_tol),(x,y)


def run():
    checks=0
    a,b,c=.2,.8,10.
    t=Theta(a,b,c)
    assert t<0; checks+=1
    xm,xp=roots(a,b,c)
    hmin=1/(c*xp);hmax=1/(c*xm)
    example_window=(hmin,hmax)
    close(xm,2.0085782207928813,1e-11);checks+=1
    close(xp,7.345437840932972,1e-11);checks+=1
    close(hmin,.0136138923459052,1e-11);checks+=1
    close(hmax,.0497864603752027,1e-11);checks+=1
    close(omega1(.025,a,b,c),-.0104835405750087,1e-10);checks+=1
    for h,sign in [(hmin*.5,1),(hmin*1.3,-1),(.025,-1),(hmax*.8,-1),(hmax*1.3,1)]:
        assert sign*omega1(h,a,b,c)>0;checks+=1
    smin=c*xm;smax=c*xp
    minv=psi(smin,a,b,c);maxv=psi(smax,a,b,c)
    floor=(maxv-minv)/2
    close(floor,.004601980837444,1e-11);checks+=1
    avg=.5*(minv+maxv)
    for lam in [1e3,1e5,1e8]:
        F=lambda s:avg*lam/(s+lam)
        grid=[smin+(smax-smin)*j/120 for j in range(121)]
        err=max(abs(F(s)-psi(s,a,b,c)) for s in grid)
        assert err>=floor-1e-12;checks+=1
        if lam==1e8:
            assert err-floor<2e-6;checks+=1
    for k in range(10):
        F=lambda s,k=k:sum((j+1)/((j+2)*s+3+j+k) for j in range(1,8))
        err=max(abs(F(smin)-minv),abs(F(smax)-maxv))
        assert err>=floor-1e-12;checks+=1
    # The representative parameters also obey the paper's sector assumption.
    assert math.pi/2*.8+.6*(1/math.e+.5*math.log(10))<math.pi;checks+=1
    rng=random.Random(20261028)
    neg_cases=0
    for i in range(600):
        a=.08+.84*rng.random();b=.08+.84*rng.random()
        c=math.exp(-4+8*rng.random())
        x0=b/a
        th=Theta(a,b,c)
        close(Q(x0,a,b,c),th,1e-11);checks+=1
        for x in [0.03,0.15,0.6,1,3,12,50]:
            dq=(x+1)*(a*x-b)/x**2
            eps=1e-6*x
            close((Q(x+eps,a,b,c)-Q(x-eps,a,b,c))/(2*eps),dq,2e-6)
            checks+=1
        for s in [.1,1,4,30]:
            eps=1e-5*s
            dlog=(math.log(psi(s+eps,a,b,c))-math.log(psi(s-eps,a,b,c)))/(2*eps)
            predicted=-Q(s/c,a,b,c)/(c*(1+s/c)**2)
            close(dlog,predicted,2e-6)
            checks+=1
        if th<-.001:
            neg_cases+=1
            xm,xp=roots(a,b,c)
            assert Q(xm*.9,a,b,c)>0 and Q(xp*1.1,a,b,c)>0
            assert Q(math.sqrt(xm*xp),a,b,c)<0
            hmid=1/(c*math.sqrt(xm*xp))
            assert omega1(hmid,a,b,c)<0
            assert omega1(1/(c*xm*.5),a,b,c)>0
            assert omega1(1/(c*xp*1.5),a,b,c)>0
            checks+=6
        elif th>.001:
            for h in [.003,.02,.2,2,30]:
                assert omega1(h,a,b,c)>0
                checks+=1
    assert neg_cases>20
    # Exact sign-tangency curve: first weight vanishes at its unique critical h.
    for a,b in [(.2,.8),(.8,.2),(.3,.7),(.7,.3)]:
        cc=(a/b)*math.exp(-2*(a+b)/(a-b))
        close(Theta(a,b,cc),0,abs_tol=1e-12);checks+=1
        h0=a/(cc*b)
        close(omega1(h0,a,b,cc),0,abs_tol=1e-12);checks+=1
        for h in [.7*h0,1.3*h0]:
            assert omega1(h,a,b,cc)>0;checks+=1
    print('VERIFICATION_OK',checks,'checks; negative parameter cases',neg_cases)
    print('example_theta',Theta(.2,.8,10),'first_lag',omega1(.025,.2,.8,10))
    print('example_window',*example_window,'positive_SOE_floor',floor)


if __name__=='__main__':
    run()
