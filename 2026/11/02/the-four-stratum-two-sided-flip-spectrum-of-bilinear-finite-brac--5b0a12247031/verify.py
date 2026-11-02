#!/usr/bin/env python3
"""Finite-field checks for the bilinear-brace flip probability theorem.

Run with Python 3 (standard library only). The general result is proved
symbolically in RESULT.md; these tests verify independent finite cases.
"""
from collections import Counter
from itertools import product


def bval(M,u,v,q):
    a,b,c,d=M
    return (a*u[0]*v[0]+b*u[0]*v[1]+c*u[1]*v[0]+d*u[1]*v[1])%q


def discriminant(M,q):
    a,b,c,d=M
    return (a*d-b*c)%q


def dependent_count(M,q):
    # Linear functionals in the second input: row u^T M and row u^T M^T.
    a,b,c,d=M
    res=0
    for x,y in product(range(q), repeat=2):
        if x==y==0: continue
        L0=(x*a+y*c)%q; L1=(x*b+y*d)%q
        R0=(a*x+b*y)%q; R1=(c*x+d*y)%q
        if (L0*R1-L1*R0)%q==0: res+=1
    return res


def predicted_s(M,q):
    a,b,c,d=M
    h=(b-c)%q
    if h==0 or ((a==0) and (d==0) and (b+c)%q==0):return q*q-1
    delta=h*h*pow(discriminant(M,q),-1,q)%q
    if delta==4%q:return q-1
    Delta=delta*(delta-4)%q
    return 2*(q-1) if pow(Delta,(q-1)//2,q)==1 else 0


def histogram(q):
    hist=Counter(); reps={}
    for M in product(range(q),repeat=4):
        if discriminant(M,q)==0:continue
        s=dependent_count(M,q)
        assert s==predicted_s(M,q),(q,M,s,predicted_s(M,q))
        hist[s]+=1
        reps.setdefault(s,M)
    expected={0:q*(q-1)**3//2,
              q-1:(q-1)*(q*q-1),
              2*(q-1):q*(q-1)*(q+1)*(q-3)//2,
              q*q-1:(q-1)*(q*q+1)}
    assert hist==Counter({k:v for k,v in expected.items() if v}), (q,hist,expected)
    assert sum(hist.values())==(q*q-1)*(q*q-q)
    # Independent ordered-pair counts for all representative matrices.
    V=list(product(range(q),repeat=2))
    for s,M in reps.items():
        L=sum(bval(M,u,v,q)==0 for u in V for v in V)
        F=sum(bval(M,u,v,q)==0 and bval(M,v,u,q)==0 for u in V for v in V)
        assert L==q*q+(q*q-1)*q, (q,M,L)
        assert F==2*q*q-1+(q-1)*s,(q,M,F,s)
    print(f'q={q}: GL2={sum(hist.values())}; strata='+str(dict(sorted(hist.items())))+'; joint/one-sided pairs verified')
    return reps


def r_of(M,A,B,q):
    x,y,z=A; u,v,w=B
    uv=bval(M,(x,y),(u,v),q)
    vu=bval(M,(u,v),(x,y),q)
    return ((u,v,(w+uv)%q),(x,y,(z-vu)%q))


def ybe_sample(M,q):
    Z=list(product(range(q),repeat=3))
    for a in Z:
        for b in Z:
            aa,bb=r_of(M,a,b,q)
            assert r_of(M,aa,bb,q)==(a,b)
    # Exhaustive Yang--Baxter on q=3; q^9 triples.
    for a in Z:
        for b in Z:
            for c in Z:
                u,v=r_of(M,a,b,q)
                v,w=r_of(M,v,c,q)
                u,v=r_of(M,u,v,q)
                rhsu,rhsv=r_of(M,b,c,q)
                rhsa,rhsu=r_of(M,a,rhsu,q)
                rhsu,rhsv=r_of(M,rhsu,rhsv,q)
                assert (u,v,w)==(rhsa,rhsu,rhsv)

if __name__=='__main__':
    for q in (3,5,7,11):
        reps=histogram(q)
        if q==3:
            for M in reps.values():ybe_sample(M,q)
            print('q=3: Yang--Baxter and involutive identities exhaustive on every nonempty stratum')
    print('VERIFY_OK')
