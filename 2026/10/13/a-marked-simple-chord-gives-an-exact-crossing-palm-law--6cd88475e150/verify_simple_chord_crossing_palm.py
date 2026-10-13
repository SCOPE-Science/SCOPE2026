#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from collections import Counter
from math import comb

def matchings(points):
    points=tuple(points)
    if not points:
        yield ()
        return
    a=points[0]
    for idx in range(1,len(points)):
        b=points[idx]
        rest=points[1:idx]+points[idx+1:]
        for tail in matchings(rest):
            yield ((a,b),)+tail

def chord_stats(m,n):
    pairs=[tuple(sorted(e)) for e in m]
    S=sum(1 for a,b in pairs if b-a==1 or (a==0 and b==2*n-1))
    X=0
    for (a,b),(c,d) in combinations(pairs,2):
        if (a<c<b<d) or (c<a<d<b):
            X+=1
    return S,X

def tail(counter,total,t):
    return Fraction(sum(v for x,v in counter.items() if x>=t),total)

def run():
    laws={}
    matchings_checked=0
    moment_checks=0
    palm_checks=0
    stochastic_checks=0
    correlation_checks=0

    for n in range(1,8):
        rows=[chord_stats(m,n) for m in matchings(range(2*n))]
        laws[n]=rows
        matchings_checked+=len(rows)

    for n in range(2,8):
        rows=laws[n]
        prev=laws[n-1]
        N=len(rows)
        Np=len(prev)

        ES=Fraction(sum(s for s,x in rows),N)
        EX=Fraction(sum(x for s,x in rows),N)
        ESX=Fraction(sum(s*x for s,x in rows),N)
        ES2=Fraction(sum(s*s for s,x in rows),N)
        EX2=Fraction(sum(x*x for s,x in rows),N)

        cov=ESX-ES*EX
        varS=ES2-ES*ES
        varX=EX2-EX*EX

        assert ES==Fraction(2*n,2*n-1)
        assert EX==Fraction(n*(n-1),6)
        assert cov==Fraction(-2*n*(n-1),3*(2*n-1))
        assert varS==Fraction(4*n*(n-1),(2*n-1)**2)
        assert varX==Fraction(n*(n-1)*(n+3),45)
        moment_checks+=5

        # Correlation identity without floating point:
        # cov^2/(varS*varX) = 5/(n+3), with negative covariance.
        assert cov<0
        assert cov*cov*Fraction(n+3,5)==varS*varX
        correlation_checks+=1

        funcs=[
            lambda x: 1,
            lambda x: x,
            lambda x: x*x,
            lambda x: x*x*x,
        ]
        for f in funcs:
            lhs=Fraction(sum(s*f(x) for s,x in rows),N)
            rhs=ES*Fraction(sum(f(x) for s,x in prev),Np)
            assert lhs==rhs
            palm_checks+=1

        maxx=max(x for s,x in rows)
        for t in range(maxx+1):
            lhs=Fraction(sum(s*int(x==t) for s,x in rows),N)
            rhs=ES*Fraction(sum(int(x==t) for s,x in prev),Np)
            assert lhs==rhs
            palm_checks+=1

        cn=Counter(x for s,x in rows)
        cp=Counter(x for s,x in prev)
        for t in range(maxx+1):
            assert tail(cn,N,t)>=tail(cp,Np,t)
            stochastic_checks+=1

    print(
        "VERIFY_OK "
        f"matchings_checked={matchings_checked} "
        f"moment_checks={moment_checks} "
        f"palm_checks={palm_checks} "
        f"stochastic_checks={stochastic_checks} "
        f"correlation_checks={correlation_checks}"
    )

if __name__=="__main__":
    run()
