#!/usr/bin/env python3
"""Independent finite-state and simulation checks for Kac-ring revival scaling."""
from itertools import product
from math import exp,log,sqrt
import random

def predicted(N,k,q):
    mean=q**k
    v=(1-q**(2*k)+2*sum(q**(2*d)-q**(2*k) for d in range(1,k)))/N
    return mean,v

def check_exact():
    for N in range(4,13):
        for k in range(1,N//2+1):
            p=.3;q=1-2*p
            vals=[]; probs=[]
            for es in product((-1,1),repeat=N):
                prob=1.
                for e in es: prob*=p if e==-1 else 1-p
                a=sum(__import__('math').prod(es[(i+j)%N] for j in range(k)) for i in range(N))/N
                vals.append(a);probs.append(prob)
            avg=sum(v*w for v,w in zip(vals,probs))
            var=sum(w*(v-avg)**2 for v,w in zip(vals,probs))
            m,tv=predicted(N,k,q)
            assert abs(avg-m)<5e-12,(N,k,avg,m)
            assert abs(var-tv)<5e-12,(N,k,var,tv)
    print('EXACT finite-state means/variances pass N=4..12, every k<=N/2')

def check_mc():
    rng=random.Random(20261013)
    q=.5;p=.25; lam=-log(q)
    N=6000
    k=round(log(N)/(2*lam))
    mu=sqrt(N)*q**k
    target_var=(1+q*q)/(1-q*q)
    abs_emp2=0.;mean_emp2=0.; count=500
    for _ in range(count):
        e=[-1 if rng.random()<p else 1 for i in range(N)]
        parity=1
        for x in e: parity*=x
        x=1
        for j in range(k): x*=e[j]
        s=x
        for i in range(1,N):
            x*=e[i-1]*e[(i+k-1)%N]
            s+=x
        z=parity*s*sqrt(N)/N
        abs_emp2+=z*z/count
        mean_emp2+=z/count
    expected=mu*mu+target_var
    assert abs(abs_emp2-expected)<max(0.5,0.33*expected),(abs_emp2,expected)
    assert abs(mean_emp2)<0.45,(mean_emp2, 'parity bias')
    print('MC signed magnetization moments',N,k,round(abs_emp2,3),round(expected,3),'passed; signed mean',round(mean_emp2,3))

if __name__=='__main__':
    check_exact();check_mc()
