"""Exact arithmetic and finite checks for two-geometric thinning classification."""
from fractions import Fraction as Q
from math import floor, ceil, log
from random import Random

def mixture_weight(q,r,t):
    lam=(t-q)/(r-q)
    return lam*(1-r)/(lam*(1-r)+(1-lam)*(1-q))

def pgf_coefficient(q,r,w,k):
    return w*(1-q)*q**k+(1-w)*(1-r)*r**k

def logjump(q,r,t,k):
    return (q**k+r**k-t**k)/k

def defect(q,r,t,k):
    return (1-q)*q**k+(1-r)*r**k-(1-t)*t**k

def rational_phi(q,r,t,k):
    return ((1-q)*q**k+(1-r)*r**k)/((1-t)*t**k)

def analytic_minimum(q,r,t):
    q,r,t=map(float,(q,r,t))
    return log((1-q)*log(t/q)/((1-r)*log(r/t)))/log(r/q)

def finite_acceptance(q,r,t):
    x=analytic_minimum(q,r,t)
    ks={max(1,floor(x)),max(1,ceil(x))}
    return all(defect(q,r,t,k)>=0 for k in ks),ks

def run():
    rng=Random(20261014)
    cases=0; approx=0; maxk=180
    for d in [7,11,17,23,41]:
        vals=[Q(i,d) for i in range(1,d)]
        for j in range(75):
            q,r=sorted(rng.sample(vals,2))
            lam=rng.choice(vals)
            t=q+lam*(r-q)
            w=mixture_weight(q,r,t)
            assert 0<w<1 and q<t<r
            assert pgf_coefficient(q,r,w,0)*(1-t)==(1-q)*(1-r)
            hprev=Q(0); h=Q(1)
            for k in range(0,16):
                lhs=pgf_coefficient(q,r,w,k)
                rhs=(1-q)*(1-r)/(1-t)*(h-t*hprev)
                assert lhs==rhs and lhs>=0
                hprev,h = h,(q+r)*h-q*r*hprev
            for k in range(1,100):
                assert logjump(q,r,t,k)>0
                assert defect(q,r,t,k)==k*logjump(q,r,t,k)-(k+1)*logjump(q,r,t,k+1)
                assert (defect(q,r,t,k)>=0)==(rational_phi(q,r,t,k)>=1)
            yes,ks=finite_acceptance(q,r,t)
            exhaustive=all(defect(q,r,t,k)>=0 for k in range(1,maxk+1))
            if yes!=exhaustive:
                raise AssertionError((q,r,t,w,ks,yes,exhaustive))
            cases+=1
    q=Q(1,10);r=Q(99,100);t=Q(19,20)
    w=mixture_weight(q,r,t)
    assert w==Q(17,89)
    assert defect(q,r,t,1)==Q(131,2500) # 0.0524
    assert defect(q,r,t,2)==-Q(6581,250000) # -0.026324
    for N in [90,180,360,720]:
        q=1-Q(10,N);r=1-Q(1,10*N);t=1-Q(3,N)
        assert q<t<r
        assert defect(q,r,t,N//3)<0
        first=next(k for k in range(1,N//3+1) if defect(q,r,t,k)<0)
        print('N',N,'first_failure',first,'at_third',defect(q,r,t,N//3)<0)
        approx+=1
    print('PASS exact rational cases',cases,'each with 99 levy checks and 180 full defect checks; delayed families',approx)
if __name__=='__main__': run()
