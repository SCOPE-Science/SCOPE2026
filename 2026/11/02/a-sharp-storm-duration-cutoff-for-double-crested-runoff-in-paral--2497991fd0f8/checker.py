"""Reproducible arithmetic checks for a finite-storm, two-route Nash-2 runoff law.

The theorem is proved analytically in RESULT.md. This standalone, standard-
library-only script compares independent numerical formulas and verifies
an exact rational two-crest witness.
"""
from fractions import Fraction
from math import exp, expm1, log, sqrt
from random import Random

ASSERTIONS = 0

def check(condition, explanation="check failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(explanation)

def impulse(t, rate):
    return rate * rate * t * exp(-rate*t) if t > 0 else 0.0

def cdf(t, rate):
    return 1-(1+rate*t)*exp(-rate*t) if t>0 else 0.0

def runoff(t, d, rate_ratio, weight):
    return (weight*(cdf(t,rate_ratio)-cdf(t-d,rate_ratio))
            +(1-weight)*(cdf(t,1)-cdf(t-d,1)))/d

def runoff_prime(t,d,r,p):
    return ((p*(impulse(t,r)-impulse(t-d,r))
            +(1-p)*(impulse(t,1)-impulse(t-d,1)))/d)

def k(d,a):
    return d/expm1(a*d)

def gap(d,r):
    return k(d,1)-k(d,r)

def R(s,d,r):
    kf=k(d,r);ks=k(d,1)
    return ((-expm1(-d))/(r*r*(-expm1(-r*d)))
            * exp((r-1)*s)*(ks-s)/(s-kf))

def turning(d,r):
    kf=k(d,r);ks=k(d,1)
    L=ks-kf
    disc=L*L-4*L/(r-1)
    if disc<=0:
        return None
    z=sqrt(disc)
    return ((ks+kf-z)/2,(ks+kf+z)/2)

def predict(d,r,p):
    pts=turning(d,r)
    if pts is None:
        return 1
    return 2 if R(pts[0],d,r)<p/(1-p)<R(pts[1],d,r) else 1

def scan_count(d,r,p,segments=3000):
    a=k(d,r);b=k(d,1)
    roots=0
    prev=runoff_prime(d+a,d,r,p)
    for j in range(1,segments+1):
        s=a+(b-a)*j/segments
        cur=runoff_prime(d+s,d,r,p)
        if prev*cur<0:
            roots+=1
        prev=cur
    return roots

def run():
    # At d=ln 2, r=8, s=m ln(2)/7:
    # R(s)=2**(m+1)*(7-m)/(255*m-7) and p/(1-p)=1/11.
    expected=[(1,1),(2,-1),(4,1),(6,-1)]
    for m,sign in expected:
        val=Fraction(2**(m+1)*(7-m),255*m-7)-Fraction(1,11)
        check((1 if val>0 else -1)==sign, "exact sign witness")
        check((1 if R(m*log(2)/7,log(2),8)>1/11 else -1)==sign)
    check(7*gap(log(2),8)>4)
    check(7*gap(2*log(2),8)<4)
    check(predict(log(2),8,1/12)==2)
    check(predict(2*log(2),8,1/12)==1)
    check(scan_count(log(2),8,1/12)==3)
    check(scan_count(2*log(2),8,1/12)==1)
    check((1-1/8)*7>4)
    lo,hi=1e-8,5.0
    for _ in range(70):
        mid=(lo+hi)/2
        if 7*gap(mid,8)>4: lo=mid
        else: hi=mid
    dc=(lo+hi)/2
    check(log(2)<dc<2*log(2))
    check(abs(7*gap(dc,8)-4)<1e-12)
    rng=Random(280629)
    for _ in range(180):
        r=1.1+11*rng.random()
        d=.025+1.5*rng.random()
        pts=turning(d,r)
        weights=[.03,.1,.25,.5,.8,.95]
        if pts:
            a=R(pts[0],d,r)
            b=R(pts[1],d,r)
            weights += [(a+b)/(a+b+2),a/(2*(1+a)),(1+b)/(2+b)]
        for p in weights:
            n=predict(d,r,p)
            detected=scan_count(d,r,p,500)
            if detected!=2*n-1:
                detected=scan_count(d,r,p,30000)
            check(detected==2*n-1,("root mismatch",r,d,p,n,detected))
        check(gap(d*.5,r)>gap(d,r))
        check(gap(d,r)>gap(d*1.5,r))
    for _ in range(100):
        r=1.1+10*rng.random()
        d=.1+2*rng.random()
        p=.01+.98*rng.random()
        t=.02+5*rng.random()
        if abs(t-d)<.001: continue
        eps=1e-5
        derivative=(runoff(t+eps,d,r,p)-runoff(t-eps,d,r,p))/(2*eps)
        check(abs(derivative-runoff_prime(t,d,r,p))<2e-7)
    print("PASS: %d checks, universal critical duration at r=8: %.12f"%(ASSERTIONS,dc))

if __name__ == '__main__':
    run()
