#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

def pmf(ps):
    a=[Fraction(1)]
    for p in ps:
        b=[Fraction(0)]*(len(a)+1)
        for k,x in enumerate(a):
            b[k]+=x*(1-p); b[k+1]+=x*p
        a=b
    return a

def gmd(a):
    return sum(abs(i-j)*x*y for i,x in enumerate(a) for j,y in enumerate(a))

def c01(rest):
    a=pmf(rest)
    return sum(x*x for x in a), sum(a[k]*a[k+1] for k in range(len(a)-1))

def inc(rest,p,q,pt,qt):
    s=p+q; r=p*q; rt=pt*qt; c0,c1=c01(rest)
    return 4*(rt-r)*((c0-c1)*(s-r-rt)+c1)

def cdf_identity(a):
    F=Fraction(0); z=Fraction(0)
    for k in range(len(a)-1):
        F+=a[k]; z+=2*F*(1-F)
    return z

def endpoints(n,mu):
    m=mu.numerator//mu.denominator; d=mu-m
    return 2*d*(1-d), gmd(pmf([mu/Fraction(n)]*n))

def run():
    ic=ac=sc=0
    for den in range(2,8):
        vals=[Fraction(i,den) for i in range(den+1)]
        for rl in range(0,3):
            for rest in product(vals, repeat=rl):
                c0,c1=c01(rest); assert c0>=c1; ac+=1
                for p in vals:
                    for q in vals:
                        s=p+q; pt=qt=s/2
                        if pt>1: continue
                        lhs=gmd(pmf(list(rest)+[pt,qt]))-gmd(pmf(list(rest)+[p,q]))
                        rhs=inc(list(rest),p,q,pt,qt)
                        assert lhs==rhs; ic+=1
                        if pt*qt>p*q: assert lhs>0; sc+=1
    cc=0
    for n in range(1,31):
        for den in range(2,8):
            for num in range(den+1):
                a=pmf([Fraction(num,den)]*n)
                assert gmd(a)==cdf_identity(a); cc+=1
    gg=gv=0
    for n in range(2,5):
        for den in range(2,6):
            vals=[Fraction(i,den) for i in range(den+1)]
            groups={}
            for v in product(vals, repeat=n):
                mu=sum(v,Fraction(0)); groups.setdefault(mu,[]).append(gmd(pmf(v))); gv+=1
            for mu,gs in groups.items():
                lo,hi=endpoints(n,mu)
                assert min(gs)==lo and max(gs)<=hi; gg+=1
    print(f"VERIFY_OK increment_checks={ic} autocorrelation_checks={ac} strict_checks={sc} cdf_checks={cc} grid_groups={gg} grid_vectors={gv}")

if __name__=="__main__": run()
