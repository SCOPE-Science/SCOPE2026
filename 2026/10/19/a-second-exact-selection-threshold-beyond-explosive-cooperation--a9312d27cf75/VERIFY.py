#!/usr/bin/env python3
"""Reproducibility checks for the rare-mutation higher-order Fermi game.

Uses the standard library only. These finite computations supplement, but do not
replace, the analytic large-population proof.
"""
from fractions import Fraction as Q
import math

CHECKS = 0

def check(cond):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError('check %d failed' % CHECKS)

def payoff(x, c, A, B):
    # S=-A, T=1+B, b=A+B, total three-game coefficient C=c.
    return -A + (c+A-B)*x - c*x*x

def primitive(x, c, A, B):
    return -A*x + (c+A-B)*x*x/2 - c*x*x*x/3

def roots(c, A, B):
    L=c+A-B
    discr=L*L-4*c*A
    if discr<=0:
        return []
    t=math.sqrt(discr)
    return [(L-t)/(2*c),(L+t)/(2*c)]

def stationary(n,c,A=0.5,B=0.5,w=1.0):
    mu=n**-2
    def sig(t):
        return 1/(1+math.exp(-t))
    def rise(k):
        x=k/n
        return x*(1-x)*sig(w*payoff(x,c,A,B))+mu*(1-x)
    def fall(k):
        x=k/n
        return x*(1-x)*sig(-w*payoff(x,c,A,B))+mu*x
    logpi=[0.0]
    for k in range(n):
        logpi.append(logpi[-1]+math.log(rise(k))-math.log(fall(k+1)))
    shift=max(logpi)
    p=[math.exp(v-shift) for v in logpi]
    s=sum(p)
    p=[v/s for v in p]
    for k in [0,1,n//4,n//2,3*n//4,n-1,n]:
        if k<n:
            check(abs(math.log(p[k+1]/p[k])-(math.log(rise(k))-math.log(fall(k+1))))<1e-9 if p[k]*p[k+1]>1e-250 else True)
    check(abs(sum(p)-1)<1e-12)
    return p

def run():
    A=Q(1,2); B=Q(1,2)
    cfold=Q(2); cm=Q(8,3)
    for x in [Q(i,200) for i in range(201)]:
        check(payoff(x,cfold,A,B)==-cfold*(x-Q(1,2))**2)
        check(payoff(x,cm,A,B)==-cm*(x-Q(1,4))*(x-Q(3,4)))
        check(primitive(x,cm,A,B)==-A*x+cm*(x*x/2-x*x*x/3))
    check(primitive(Q(3,4),cm,A,B)==0)
    check(primitive(Q(1,2),cfold,A,B)<0)
    # Another exact game, A=3 and B=8: C_M=25, stable roots 1/5,3/5.
    A=Q(3); B=Q(8); cm=Q(25)
    check(payoff(Q(1,5),cm,A,B)==0)
    check(payoff(Q(3,5),cm,A,B)==0)
    check(primitive(Q(3,5),cm,A,B)==0)
    check(primitive(Q(1,5),cm,A,B)<0)
    # Non-symmetric parameter sets: numerically compare the potential sign around C_M.
    for aa,bb in [(0.3,0.7),(1.0,5.0),(3.0,8.0),(0.1,3.4),(4.0,0.2)]:
        cs=(math.sqrt(aa)+math.sqrt(bb))**2
        cp=(2*math.sqrt(aa/3)+math.sqrt(bb+aa/3))**2
        check(cp>cs)
        for sgn in [-1,0,1]:
            val=cp*(1+sgn*0.01)
            pair=roots(val,aa,bb)
            check(len(pair)==2)
            rminus,rplus=pair
            check(0<rminus<rplus<1)
            height=primitive(rplus,val,aa,bb)
            check(abs(height)<1e-9 if sgn==0 else (height>0 if sgn==1 else height<0))
            if sgn==0:
                check(abs(rplus-3*rminus)<1e-11)
    # Direct microscopic ordered-focal/model averaging at every count in a small population.
    n=8; c=3.0; w=0.9; mu=n**-2
    def sig(t):return 1/(1+math.exp(-t))
    for k in range(n+1):
        players=[1]*k+[0]*(n-k)
        inc=sum(sig(w*payoff(k/n,c,0.5,0.5)) for i in players for j in players if i==0 and j==1)/n**2
        dec=sum(sig(-w*payoff(k/n,c,0.5,0.5)) for i in players for j in players if i==1 and j==0)/n**2
        expected_inc=k*(n-k)/n**2*sig(w*payoff(k/n,c,0.5,0.5))
        expected_dec=k*(n-k)/n**2*sig(-w*payoff(k/n,c,0.5,0.5))
        check(abs(inc-expected_inc)<1e-14)
        check(abs(dec-expected_dec)<1e-14)
        check(abs((inc+mu*(n-k)/n)-(expected_inc+mu*(1-k/n)))<1e-14)
    # The stochastic selection boundary is delta=4/9 for a+b=6.
    for n in [150,300,600,1200]:
        below=stationary(n,6*.40)
        edge=stationary(n,6*(4/9))
        above=stationary(n,6*.52)
        check(below[0]>.9)
        check(edge[0]>.75)
        check(sum(above[int(.65*n):int(.95*n)]) > (.88 if n==150 else .97))
    print('PASS:',CHECKS,'exact and numeric assertions')

if __name__=='__main__': run()
