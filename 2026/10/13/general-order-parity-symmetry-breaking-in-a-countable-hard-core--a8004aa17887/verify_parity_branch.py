#!/usr/bin/env python3
import math

def masses(k,s):
    d=math.sinh((k-1)*s)
    return math.exp(k*s)*math.sinh(s)/d, math.exp(-k*s)*math.sinh(s)/d

def lsinh(x):
    return x-math.log(2.0)+math.log1p(-math.exp(-2.0*x))

def logadd(a,b):
    m=max(a,b)
    return m+math.log(math.exp(a-m)+math.exp(b-m))

def loglam(k,ell,s):
    la=logadd(math.log(ell)+lsinh((k-1)*s), lsinh((k+1)*s))
    return lsinh(s)-lsinh((k-1)*s)+k*(la-lsinh(k*s))

def lam(k,ell,s):
    return math.exp(loglam(k,ell,s))

def lc(k,ell):
    return (((k-1)*ell+k+1)**k)/(k**k*(k-1))

def bend(k):
    return (k+1)*(k+3)/(3*(k-1)**2)

def residual(k,ell,s):
    m1,m2=masses(k,s); L=lam(k,ell,s); D=1+ell+m1+m2
    r1=abs(m1-L*((1+m1)/D)**k)
    r2=abs(m2-L*((1+m2)/D)**k)
    return max(r1,r2)

def main():
    worst=0.0
    cases=0
    for k in range(2,13):
        ell=1.7*bend(k)+0.3
        for s in (0.03,0.11,0.37,0.83):
            worst=max(worst,residual(k,ell,s)); cases+=1
        # local downward bend above the threshold
        eps=2e-4
        assert lam(k,ell,eps) < lc(k,ell)
        # global return above Lc
        S=1.0
        while lam(k,ell,S) <= lc(k,ell):
            S*=1.5
            assert S < 50
        # two distinct roots for a level between a sampled local minimum and Lc
        xs=[i*S/2000 for i in range(1,2001)]
        vals=[lam(k,ell,x) for x in xs]
        j=min(range(len(vals)),key=vals.__getitem__)
        lmin=vals[j]; target=(lmin+lc(k,ell))/2
        signs=[]
        prev=lc(k,ell)-target
        roots=0
        for v in vals:
            cur=v-target
            if cur==0 or prev*cur<0: roots+=1
            prev=cur
        assert roots>=2
    # k=2 source specialization: M1*M2=1 and Lc=(ell+3)^2/4
    ell=2.3
    for s in (0.1,0.6,1.2):
        m1,m2=masses(2,s)
        assert abs(m1*m2-1.0) < 2e-12
    assert abs(lc(2,ell)-(ell+3)**2/4) < 1e-12
    assert worst < 5e-10
    print('VERIFY_OK cases=%d worst_residual=%.3e k2_specialization=1 two_root_orders=2..12' % (cases,worst))

if __name__=='__main__': main()
