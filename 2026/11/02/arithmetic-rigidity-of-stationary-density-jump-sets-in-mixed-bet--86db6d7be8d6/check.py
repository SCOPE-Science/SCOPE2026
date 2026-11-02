#!/usr/bin/env python3
"""Exact finite-word tests for the stationary beta-mixture jump theorem.
No external dependencies. Finite checks illustrate and do not replace the proof.
"""
from collections import defaultdict
from fractions import Fraction as F

def tr(beta, x):
    z = beta*x
    return z-(z.numerator//z.denominator)

def build(b, beta, p, N):
    # indexed map names: the integer slope and the fractional slope
    maps=((F(b), F(1)-p),(beta,p))
    paths=[(F(1),F(1))] # current endpoint, word weight
    steps=defaultdict(F)
    steps[F(1)]+=1
    for _ in range(N):
        nxt=[]
        for t, weight in paths:
            for slope, prob in maps:
                nt=tr(slope,t)
                nw=weight*prob/slope
                if nt: steps[nt]+=nw
                nxt.append((nt,nw))
        paths=nxt
    return steps, maps

def L(steps, maps):
    ans=defaultdict(F)
    for t, c in steps.items():
        for slope, prob in maps:
            z=slope*t
            whole=z.numerator//z.denominator
            if whole: ans[F(1)]+=c*prob*whole/slope
            rem=z-whole
            if rem: ans[rem]+=c*prob/slope
    return ans

def eval_step(steps,x):
    return sum((w for t,w in steps.items() if x<t),F(0))

def test(b,beta,p,N):
    steps,maps=build(b,beta,p,N)
    r=(F(1)-p)/b; s=p/beta; q=r+s
    assert 0<q<1
    Z=sum(t*c for t,c in steps.items()); assert 1<=Z<=1/(1-q)
    assert sum(steps.values())<=1/(1-q)
    # Independent transfer-operator branch identity, tested exactly at endpoints and samples
    for slope,_ in maps:
        for t in [F(1), F(1,2), F(1,3), F(3,4), beta-1]:
            z=slope*t; whole=z.numerator//z.denominator; rem=z-whole
            for y in (F(1,7),F(2,7),F(4,7),F(6,7)):
                rhs=F(whole)/slope+(F(1)/slope if y<rem else F(0))
                lhs=sum((F(1)/slope for k in range((slope.numerator//slope.denominator)+2) if F(0)<= (y+k)/slope <t),F(0))
                assert lhs==rhs, (slope,t,y,lhs,rhs)
    trans=L(steps,maps)
    samples=[F(j,97) for j in range(1,97)]
    assert max(abs(eval_step(trans,x)-eval_step(steps,x)) for x in samples)<=q**(N+1)
    # Verify the expected jumps at the beta-> b^n points and rational beta^n points
    for j in range(N):
        # Rational beta can have a finite integer-map orbit; the theorem
        # uses the other, always-infinite rational-beta orbit instead.
        x=F(1)
        for _ in range(j+1): x=tr(beta,x)
        assert steps[x]>=s**(j+1)
        assert steps[x]/Z >= (1-q)*s**(j+1)
    return len(steps), q, Z

if __name__=='__main__':
    cases=[(2,F(3,2),F(1,3)),(3,F(4,3),F(2,5)),(4,F(7,4),F(3,7))]
    for b,beta,p in cases:
        for N in range(1,9):
            k,q,Z=test(b,beta,p,N)
        print('PASS',b,beta,p,'depth8 distinct step endpoints:',k,'q=',q,'Z8=',Z)
    print('PASS: 24 rational finite-word / transfer-operator / jump-bound tests')
