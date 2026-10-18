#!/usr/bin/env python3
"""Exact-arithmetic checks for a rank-three polar line-search dynamical identity."""
from fractions import Fraction as Q
from decimal import Decimal, localcontext

def polarized(s):
    nonzero=[u for u in s if u]
    if not nonzero:
        return list(s)
    mean=sum(abs(u) for u in nonzero)/len(nonzero)
    return [u-(mean if u>0 else -mean) if u else u for u in s]

count=0
for den in range(2,151):
    for num in range((den+1)//2,den):
        t=Q(num,den)
        start=[Q(1), t, Q(1)-t]
        up=polarized(start)
        got=sorted(map(abs,up),reverse=True)
        assert got[0]==got[1]+got[2]
        if t==Q(2,3):
            assert got==[Q(1,3),Q(1,3),Q(0)]
            assert polarized(up)==[Q(0)]*3
        elif t<Q(2,3):
            assert got[0]==Q(1,3)
            assert got[1]/got[0]==3*t-1
        else:
            assert got[0]==t-Q(1,3)
            assert got[1]/got[0]==1/(3*t-1)
        count+=1
for a in range(1,25):
    for b in range(1,a+1):
        v=[Q(a),Q(b)]; assert polarized(polarized(v))==[Q(0)]*2
with localcontext() as ctx:
    ctx.prec=90
    one=Decimal(1); two=Decimal(2); three=Decimal(3)
    t=(one+Decimal(13).sqrt())/Decimal(6)
    rate=t-one/three
    assert abs(t-1/(three*t-one))<Decimal('1e-80')
    v=[one,t,one-t]; baseline=sum(q*q for q in v)
    for k in range(26):
        vals=sorted(map(abs,v),reverse=True)
        assert abs(vals[1]/vals[0]-t)<Decimal('1e-65')
        assert abs(sum(q*q for q in v)/baseline-rate**(2*k))<Decimal('1e-65')
        v=polarized(v)
print('PASS: %d exact rational projective tests, 300 two-dimensional steps, 26 high-precision self-similar iterates' % count)
