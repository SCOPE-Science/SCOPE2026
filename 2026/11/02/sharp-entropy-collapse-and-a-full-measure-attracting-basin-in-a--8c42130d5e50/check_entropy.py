#!/usr/bin/env python3
"""Exact-rational structural tests for the two-slope tent composition.

These finite checks supplement the analytical entropy/dimension proof; they do
not numerically certify the full parameter range or infinite orbit claims.
"""
from fractions import Fraction as Q
import sympy as S

p=S.symbols('p',real=True)
R=S.Rational(9,10)*(2-p)/(1-p)
k=p/(2*(1-p))
a=5*p/(8+p)
assert S.cancel((R-1)*a-k)==0
assert S.cancel(R*(S.Rational(1,2)-a)+a-(R/2-k))==0
assert S.cancel((R-2)-(11*p-2)/(10*(1-p)))==0
assert S.cancel((S.Rational(1,2)-a)-(8-9*p)/(2*(8+p)))==0
assert S.cancel(((R/2-k)-S.Rational(1,2))-(8-9*p)/(20*(1-p)))==0


def params(pp):
    RR=Q(9,10)*(2-pp)/(1-pp)
    kk=pp/(2*(1-pp))
    aa=Q(5)*pp/(8+pp)
    return RR,kk,aa


def T(x,pp):
    z=Q(9,5)*min(x,1-x)
    if z<=pp:
        return z/2
    return ((1-pp/2)*z-pp/2)/(1-pp)


def cylinder_test(pp,nmax=8):
    RR,kk,aa=params(pp)
    assert RR>2 and 0<aa<Q(1,2)
    I=(aa,1-aa)
    assert T(I[0],pp)==aa and T(I[1],pp)==aa
    assert T(Q(1,2),pp)>I[1]
    def L(x): return (x+kk)/RR
    def H(x): return 1-(x+kk)/RR
    intervals=[I]
    for n in range(1,nmax+1):
        new=[]
        for l,u in intervals:
            new.extend([(L(l),L(u)),(H(u),H(l))])
        intervals=sorted(new)
        assert len(intervals)==2**n
        assert all(I[0]<=l<u<=I[1] for l,u in intervals)
        assert all(intervals[i][1]<intervals[i+1][0] for i in range(len(intervals)-1))
        assert sum((u-l for l,u in intervals),Q(0))==(I[1]-I[0])*(Q(2)/RR)**n
        for l,u in intervals:
            vl,vu=l,u
            for _ in range(n):
                vl,vu=T(vl,pp),T(vu,pp)
            assert {vl,vu}==set(I)
    return len(intervals)

assert cylinder_test(Q(1,2))==256
assert cylinder_test(Q(7,8))==256

for pp in [Q(1,20),Q(1,10),Q(2,11)]:
    RR,kk,aa=params(pp)
    assert 1<RR<=2
    assert Q(0)<pp/Q(9,5)<aa<Q(1,2)
    assert T(aa,pp)==aa and T(1-aa,pp)==aa
    assert aa<T(Q(1,2),pp)<=1-aa

for pp in [Q(8,9),Q(9,10),Q(19,20)]:
    assert T(Q(1,2),pp)<=Q(1,2)

print('PASS: exact polynomial identities, sample invariant cores, two full inverse branches, 1,020 or more finite cylinder endpoint/length tests, and critical boundary cases')

# Independent Type-1 regime below the t = 4/3 plateau threshold:
# the entire positive-entropy side retains slope less than two.
def T_general(x, tt, ss, pp):
    y=tt*min(x,1-x)
    return ss*y if y<=pp else ((1-ss*pp)*y-pp*(1-ss))/(1-pp)

tt=Q(6,5)
ss=Q(2,5)
pc=Q(5,17)
ps=Q(10,19)
assert ps>pc
for pp in [Q(1,100),Q(1,10),Q(1,4)]:
    rr=tt*(1-ss*pp)/(1-pp)
    aa=pp*(1-ss)/(tt*(1-ss*pp)-(1-pp))
    assert Q(1)<rr<Q(2)
    assert Q(0)<pp/tt<aa<Q(1,2)
    assert T_general(aa,tt,ss,pp)==aa
    assert T_general(1-aa,tt,ss,pp)==aa
    assert aa<T_general(Q(1,2),tt,ss,pp)<1-aa
assert T_general(Q(1,2),tt,ss,pc)==Q(1,2)
assert T_general(Q(1,2),tt,ss,Q(2,5))<Q(1,2)

print('PASS: independent low-slope branch and threshold orders without a full-shift plateau')
