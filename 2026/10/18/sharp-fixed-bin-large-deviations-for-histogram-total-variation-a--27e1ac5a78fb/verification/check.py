#!/usr/bin/env python3
"""Finite checks for sharp adjacent-bin variation tails."""
from fractions import Fraction
from itertools import product
from math import exp, log
from scipy.optimize import brentq
from scipy.stats import binom

def coeff(s):
    return (-s[0],)+tuple(s[i-1]-s[i] for i in range(1,len(s)))+(s[-1],)
def all_score(w,z):
    return sum(z**k for k in w)
def canonical(n):
    return tuple(1 if i%2==0 else -1 for i in range(n-1))

def check_max():
    tested=0
    for n in range(3,12):
        can=canonical(n)
        opt={can,tuple(-x for x in can)} if n%2==0 else {can}
        for z in (Fraction(11,10),Fraction(4,3),Fraction(2,1),Fraction(5,1)):
            raw=[(all_score(coeff(s),z),s) for s in product((-1,1),repeat=n-1)]
            maximum=max(a for a,s in raw)
            winners={s for a,s in raw if a==maximum}
            assert winners==opt,(n,z,winners,opt)
            w=coeff(can)
            if n%2==0:
                expected=Fraction(n-2,2)*(z**2+z**-2)+(z+z**-1)
            else:
                expected=2*z**-1+Fraction(n-1,2)*z**2+Fraction(n-3,2)*z**-2
            assert maximum==expected
            tested+=len(raw)+1
    return tested

def check_endpoint():
    tested=0
    for n in range(3,9):
        # Maximize d(p) over all grid histograms up to N=10.
        for N in range(1,11):
            def comp(total,count):
                if count==1:
                    yield (total,)
                else:
                    for v in range(total+1):
                        for r in comp(total-v,count-1):yield (v,)+r
            for x in comp(N,n):
                d=sum(abs(x[i+1]-x[i]) for i in range(n-1))
                assert d<=2*N
                if d==2*N:
                    assert x[0]==x[-1]==0
                    assert all(x[i]*x[i+1]==0 for i in range(n-1))
                if x[0]==x[-1]==0 and all(x[i]*x[i+1]==0 for i in range(n-1)):
                    assert d==2*N
                tested+=1
    return tested

def check_rate():
    checked=0
    # Compare exact binomial tails for n=3 against lattice saddlepoint.
    n=3
    for t in (0.2,0.6,1.1,1.6):
        def logmgf(th):
            return log((exp(2*th)+2*exp(-th))/3)
        def derivative(th):
            return (2*exp(2*th)-2*exp(-th))/(exp(2*th)+2*exp(-th))
        th=brentq(lambda z:derivative(z)-t,0,8)
        # tilted Bernoulli success prob w=+2
        p=exp(2*th)/(exp(2*th)+2*exp(-th))
        var=9*p*(1-p)
        I=th*t-logmgf(th)
        for N in (60,120,240):
            import math
            k=math.ceil((N*t+N)/3)
            logactual=binom.logsf(k-1,N,1/3)
            delta=3*k-N-N*t
            logasym=-N*I+log(3)-th*delta-log(1-exp(-3*th))-.5*log(2*math.pi*N*var)
            # finite size within 50%, becomes tighter as N grows; avoid weak t at modest N
            assert abs(logactual-logasym)<.55,(N,t,logactual-logasym)
            checked+=1
    return checked
if __name__=='__main__':
    print('rational coefficient comparisons',check_max())
    print('exact histogram endpoint checks',check_endpoint())
    print('lattice asymptotic comparison checks',check_rate())
    print('PASS')
