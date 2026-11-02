#!/usr/bin/env python3
"""Finite-state and convergent-weight checks for an exclusion process.

Usage: python verify.py
Requires only Python's standard library.  Assertions inspect algebraic
identities and finite approximations; the asymptotic theorem is proved
independently in RESULT.md.
"""
from __future__ import annotations

import itertools
import math
from fractions import Fraction

CHECKS = 0

def check(truth, message):
    global CHECKS
    CHECKS += 1
    if not truth:
        raise AssertionError(message)


def cluster_count(bits):
    n = len(bits)
    return sum(bits[i] == 1 and bits[(i + 1) % n] == 0 for i in range(n))


def head_count(bits):
    n = len(bits)
    return sum(bits[i] == 1 and bits[(i+1)%n] == 1 and bits[(i+2)%n] == 0 for i in range(n))


def tail_count(bits):
    n = len(bits)
    return sum(bits[i] == 1 and bits[(i+1)%n] == 0 and bits[(i+2)%n] == 1 for i in range(n))


def canonical_classes(n, k, q):
    """Normalized run-count weights, without large binomial integers."""
    L = n-k
    assert 2 <= k <= n-2 and q > 0
    w = [1.0]
    for c in range(1, min(k, L)):
        w.append(w[-1]*(k-c)*(L-c)/(c*(c+1)*q))
    total = sum(w)
    return [(c, v/total) for c,v in enumerate(w,1)]


def conditional(n,k,c):
    """E[A], E[B], E[A^2], E[B^2], E[AB] for uniform cyclic run sizes."""
    L=n-k
    EM = c*(c-1)/(k-1)
    EMfac2 = c*(c-1)**2*(c-2)/((k-1)*(k-2)) if k>=3 else 0.0
    EA = c-EM
    EA2 = c*c-2*c*EM+EM+EMfac2
    EB = c*(c-1)/(L-1)
    EBfac2 = c*(c-1)**2*(c-2)/((L-1)*(L-2)) if L>=3 else 0.0
    EB2 = EB+EBfac2
    return EA,EB,EA2,EB2,EA*EB


def moment_data(n,k,q,alpha=1.):
    allc=canonical_classes(n,k,q)
    EC2=0.; EA=EB=EA2=EB2=EAB=0.
    for c,p in allc:
        ec=conditional(n,k,c)
        EC2+=p*c*(c-1)
        EA+=p*ec[0]; EB+=p*ec[1]
        EA2+=p*ec[2]; EB2+=p*ec[3]; EAB+=p*ec[4]
    mean=alpha*(EA+q*EB)/n
    second=(alpha/n)**2*(EA2+2*q*EAB+q*q*EB2)
    return EC2,mean,second-mean*mean,EB,EB2


def enumerate_exact(n,k,q):
    z=0; cc={}; EA=EB=EA2=EB2=EAB=0
    for positions in itertools.combinations(range(n),k):
        arr=tuple(int(i in positions) for i in range(n))
        c=cluster_count(arr)
        a=head_count(arr)
        b=tail_count(arr)
        W=q**(k-c)
        z+=W
        cc[c]=cc.get(c,0)+1
        EA+=W*a;EB+=W*b;EA2+=W*a*a;EB2+=W*b*b;EAB+=W*a*b
    return cc,tuple(x/z for x in (EA,EB,EA2,EB2,EAB))


def stationary_balance(n,k,q):
    """Check *every* global-balance equation using exact rational rates."""
    states={}
    for loc in itertools.combinations(range(n),k):
        x=tuple(int(i in loc) for i in range(n))
        c=cluster_count(x)
        states[x]=q**(k-c)
    inflow={x:Fraction(0) for x in states}
    outflow={x:Fraction(0) for x in states}
    for x,w in states.items():
        for i in range(n):
            if x[i] == 1 and x[(i+1)%n] == 0:
                rate=(Fraction(int(x[(i-1)%n]))+q*int(x[(i+2)%n]))
                if rate:
                    y=list(x); y[i]=0; y[(i+1)%n]=1; y=tuple(y)
                    outflow[x]+=w*rate
                    inflow[y]+=w*rate
    for x in states:
        check(inflow[x]==outflow[x], f'global balance failed n={n} k={k} state={x}')


def run():
    # Independently enumerate binary cyclic states, rather than assuming
    # the conditional run-composition formulas.
    for n in range(7,13):
        for k in range(3,n-2):
            classes,raw=enumerate_exact(n,k,1.7)
            for c,count in classes.items():
                predicted=Fraction(n,c)*math.comb(k-1,c-1)*math.comb(n-k-1,c-1)
                check(count==predicted, f'run-count formula n={n}, k={k}, c={c}')
            classes_normalized=canonical_classes(n,k,1.7)
            exact_weights=[float(Fraction(n,c)*math.comb(k-1,c-1)*math.comb(n-k-1,c-1))*1.7**(-c) for c in range(1,min(k,n-k)+1)]
            for (_,p),w in zip(classes_normalized,exact_weights):
                check(abs(p-w/sum(exact_weights))<1e-12, 'normalized class weight')
            EA=EB=EA2=EB2=EAB=0.
            for c,p in classes_normalized:
                cond=conditional(n,k,c)
                EA+=p*cond[0];EB+=p*cond[1]
                EA2+=p*cond[2];EB2+=p*cond[3];EAB+=p*cond[4]
            for expected,got in zip((EA,EB,EA2,EB2,EAB),raw):
                check(abs(expected-got)<1e-10, f'run conditional moments n={n}, k={k}: {expected},{got}')
    for n in range(6,11):
        for k in range(2,n-1):
            stationary_balance(n,k,Fraction(7,4))

    rho=0.37; lam=2.5; alpha=1.7
    z=rho*(1-rho)/lam
    # Independent evaluation of the limiting Bessel-series weights.
    t=1.0; sm=t; e=0.
    for c in range(2,45):
        t *= z/(c*(c-1))
        sm+=t
        e+=c*(c-1)*t
    check(abs(e/sm-z)<1e-14, 'Bessel-law factorial-moment identity')
    for n in (500, 2000, 8000):
        k=round(rho*n);q=lam*n*n
        ec2,mean,var,eb,eb2=moment_data(n,k,q,alpha)
        assert math.isfinite(var)
        print(f'N={n}: E[C(C-1)]={ec2:.10f}, E[j]={mean:.10f}, Var(j)/N={var/n:.10f}, N E[B]={n*eb:.10f}')
        target=(z,alpha*rho,alpha*alpha*lam*rho,rho/lam)
        observed=(ec2,mean,var/n,n*eb)
        error=max(abs(a-b) for a,b in zip(observed,target))
        check(error<.04 if n==500 else error<.012 if n==2000 else error<.004,
              'strong-recovery limits')
    print(f'PASS: {CHECKS} independent finite assertions')

if __name__=='__main__':
    run()
