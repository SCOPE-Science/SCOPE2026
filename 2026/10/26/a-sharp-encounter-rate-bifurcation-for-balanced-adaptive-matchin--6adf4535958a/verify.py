#!/usr/bin/env python3
"""Exact-rational checks for balanced-target two-sided matching equilibria.

This checker corroborates finite instances; general assertions are proved in RESULT.md.
Run with: python verify.py
"""
from fractions import Fraction as F
from itertools import product


def cap_sum(v, x):
    return sum((min(F(z), x) for z in v), F(0))


def cap_inverse(v, R):
    """Inverse of x -> sum min(v_i,x) for 0<R<sum(v)."""
    v = tuple(map(F, v)); R = F(R)
    assert F(0) < R < sum(v)
    levels = sorted(set(v)); prev = F(0); accum = F(0)
    for h in levels:
        active = sum(z > prev for z in v)
        top = accum + active * (h - prev)
        if R <= top:
            x = prev + (R - accum) / active
            assert cap_sum(v, x) == R
            return x
        prev, accum = h, top
    raise AssertionError('inverse domain')


def check_equilibrium(c, d, K, a, b):
    c = tuple(map(F,c)); d=tuple(map(F,d)); K=F(K)
    assert len(c)==len(a) and len(d)==len(b)
    assert all(F(0)<z<=1 for z in a+b)
    A=sum(a); B=sum(b)
    assert all(ai == min(F(1), ci/(K*B)) for ai,ci in zip(a,c))
    assert all(bj == min(F(1), dj/(K*A)) for bj,dj in zip(b,d))
    R=K*A*B
    assert R==sum(min(ci,K*B) for ci in c)
    assert R==sum(min(dj,K*A) for dj in d)
    return R


def test_instance(c, d):
    c=tuple(map(F,c));d=tuple(map(F,d));T=sum(c)
    assert T==sum(d) and T>0
    Kc=max(c)*max(d)/T
    checks=0
    for t in range(1,20):
        R=T*F(t,20)
        x=cap_inverse(c,R);y=cap_inverse(d,R)
        K=x*y/R
        assert K<Kc, (c,d,K,Kc)
        a=tuple(min(F(1),ci/x) for ci in c)
        b=tuple(min(F(1),dj/y) for dj in d)
        assert check_equilibrium(c,d,K,a,b)==R
        checks+=1
    for f in (F(1), F(9,8), F(4,3), F(2), F(5)):
        K=f*Kc
        low=max(d)/K; high=T/max(c)
        assert low<=high
        for A in (low, (low+high)/2, high):
            a=tuple(ci*A/T for ci in c)
            b=tuple(dj/(K*A) for dj in d)
            assert check_equilibrium(c,d,K,a,b)==T
            checks+=1
    mc=sum(z==max(c) for z in c)
    md=sum(z==max(d) for z in d)
    eta=F(1,1)/(mc*max(c))+F(1,1)/(md*max(d))-F(1,1)/T
    assert eta>0
    for h in (100,1000,10000):
        eps=F(1,h)
        if eps < min(c) and eps < min(d):
            R=T-eps
            x=cap_inverse(c,R);y=cap_inverse(d,R)
            # Near threshold only the largest target(s) are unsaturated.
            assert x==max(c)-eps/mc
            assert y==max(d)-eps/md
            K=x*y/R
            lhs=(Kc-K)/eps
            assert abs(lhs-Kc*eta) < F(1000, h)*Kc
            checks+=1
    return checks



def check_homogeneous_selection():
    """Independent numerical spot checks of the proved projected-flow selection law."""
    from math import sqrt
    cases=0
    for M in (1,2,4):
        for N in (1,3):
            T=6.0
            c=T/M; d=T/N
            Kc=c/N
            for scale in (0.6,1.0,1.5,3.0):
                K=scale*Kc
                for u in (0.08,0.4,0.75,1.0):
                    for v in (0.08,0.4,0.75,1.0):
                        A=M*u; B=N*v
                        h=A-B
                        if K<=Kc:
                            Ae,Be=float(M),float(N)
                        else:
                            hmin=d/K-N; hmax=M-c/K
                            hsel=max(hmin,min(h,hmax))
                            Ae=(hsel+sqrt(hsel*hsel+4*T/K))/2
                            Be=Ae-hsel
                        # The projected Euler scheme approximates the continuous flow.
                        dt=0.001
                        for _ in range(25000):
                            speed=T-K*A*B
                            A=min(M,max(0.0,A+dt*speed))
                            B=min(N,max(0.0,B+dt*speed))
                        assert abs(A-Ae)<0.001 and abs(B-Be)<0.001, (M,N,K,u,v,A,B,Ae,Be)
                        cases+=1
    return cases

def main():
    N=0; cases=0
    # Every ordered positive integer sequence of size <=3 and sum <=9.
    grouped={}
    for n in range(1,4):
        for seq in product(range(1,7),repeat=n):
            T=sum(seq)
            if T<=9:
                grouped.setdefault(T,[]).append(seq)
    for T,vecs in sorted(grouped.items()):
        for c in vecs:
            for d in vecs:
                N+=test_instance(c,d)
                cases+=1
    # Explicit heterogeneous high-encounter equilibrium.
    c=(F(1),F(2));d=(F(1),F(2)); K=F(2)
    A=F(5,4)
    a=tuple(ci*A/F(3) for ci in c)
    b=tuple(dj/(K*A) for dj in d)
    assert a==(F(5,12),F(5,6))
    assert b==(F(2,5),F(4,5))
    assert check_equilibrium(c,d,K,a,b)==3
    flow_cases=check_homogeneous_selection()
    print('PASS projected-flow selection trials',flow_cases)
    print('PASS instances',cases,'rational equilibrium checks',N)
    print('PASS balanced example',tuple(map(str,a)),tuple(map(str,b)))

if __name__=='__main__': main()
