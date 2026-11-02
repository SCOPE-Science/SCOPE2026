#!/usr/bin/env python3
"""Reproduce the exact rational certificates for symmetric three-bit sampling."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def span(gens):
    s={0}
    for v in gens:
        s |= {u ^ v for u in tuple(s)}
    return frozenset(s)

SUBSPACES = sorted({span(c) for d in range(4) for c in combinations(range(1,8),d)},key=lambda t:(-len(t),tuple(sorted(t))))
assert len(SUBSPACES)==16
assert [sum(len(x)==2**j for x in SUBSPACES) for j in range(4)]==[1,7,7,1]


def weights(a,b):
    c=1-3*a-3*b
    assert a>=0 and b>=0 and c>=0
    return {v:(a if v.bit_count()==1 else b if v.bit_count()==2 else c) for v in range(1,8)}


def exact_markov(a,b):
    p=weights(a,b)
    expectation={s:Q(0) for s in SUBSPACES if 1 in s}
    for s in SUBSPACES:
        if 1 in s:continue
        stay=sum((p[v] for v in s if v),Q(0))
        assert stay<1
        rhs=Q(1)
        for v in range(1,8):
            if v not in s:
                rhs+=p[v]*expectation[span(tuple(s)+(v,))]
        expectation[s]=rhs/(1-stay)
    return expectation[span([])]


def closed(a,b):
    return (Q(3)-Q(2)/(1-a)-Q(3)/(1-b)+Q(2)/(3*(a+b))
            +Q(1)/(1-2*a-b)+Q(1)/(1-3*b))

cases=[(Q(3,13),Q(1,13)),(Q(1,3),Q(0)),(Q(1,6),Q(1,6)),
       (Q(0),Q(1,7)),(Q(1,4),Q(1,12)),(Q(1,5),Q(1,15)),
       (Q(1,20),Q(1,6))]
for a,b in cases:
    if 3*(a+b)<=1:
        assert exact_markov(a,b)==closed(a,b),(a,b)

assert closed(Q(3,13),Q(1,13))==Q(167,60)
assert Q(279,100)-Q(167,60)==Q(1,150)

# On each boundary, T-279/100 is a polynomial in t=3a or t=3b,
# divided by a positive rational denominator. These scaled polynomial
# numerators are exactly as displayed in RESULT.md.
POLYS={
    'c_zero':[1200,-3748,3616,-1163,221],
    'b_zero':[5400,-12933,8733,-1074],
    'a_zero':[5400,-14733,12744,-1611],
}
EXPECTED_MIN={
    'c_zero':(Q(8873,12288),11,2),
    'b_zero':(Q(24521,512),14,1),
    'a_zero':(Q(1557633,2048),10,2),
}


def polynomial(p,t):
    return sum(Q(c)*t**i for i,c in enumerate(p))


def bernstein_coeffs(p,j):
    d=len(p)-1
    monomial=[sum(Q(p[i])*comb(i,r)*Q(j)**(i-r)/Q(16)**i
                  for i in range(r,d+1)) for r in range(d+1)]
    return [sum(monomial[r]*Q(comb(k,r),comb(d,r)) for r in range(k+1))
            for k in range(d+1)]

for name,p in POLYS.items():
    degree=len(p)-1
    bcert=[bernstein_coeffs(p,j) for j in range(16)]
    minimum=min((x,j,k) for j,row in enumerate(bcert) for k,x in enumerate(row))
    assert minimum==EXPECTED_MIN[name],(name,minimum)
    assert all(x>0 for row in bcert for x in row)
    for j,row in enumerate(bcert):
        for u in (Q(0),Q(1,3),Q(1,2),Q(1)):
            lhs=sum(row[k]*comb(degree,k)*u**k*(1-u)**(degree-k)
                    for k in range(degree+1))
            assert lhs==polynomial(p,(Q(j)+u)/16)

# Verify independently that each polynomial describes the claimed
# boundary difference, including the exact positive denominator.
for t in (Q(1,8),Q(1,3),Q(1,2),Q(3,4),Q(7,8)):
    a=t/3
    gap=Q(279,100)
    q_c=300*a*(a-1)*(3*a-2)*(3*a+2)
    assert (closed(a,Q(1,3)-a)-gap)*q_c==polynomial(POLYS['c_zero'],t)/3
    q_b=300*a*(a-1)*(2*a-1)
    assert (closed(a,Q(0))-gap)*q_b==polynomial(POLYS['b_zero'],t)/27
    q_a=300*a*(a-1)*(3*a-1)
    assert (closed(Q(0),a)-gap)*q_a==polynomial(POLYS['a_zero'],t)/27


# Rational localization of the unique critical point: the proved Hessian
# bound is H >= I/10. Therefore the distance from a test point to the
# global minimizer is no greater than ten times its gradient norm.
a0,b0=Q(238169545370,10**12),Q(78518646238,10**12)
ga=(-Q(2)/(1-a0)**2-Q(2)/(3*(a0+b0)**2)
    +Q(2)/(1-2*a0-b0)**2)
gb=(-Q(3)/(1-b0)**2-Q(2)/(3*(a0+b0)**2)
    +Q(1)/(1-2*a0-b0)**2+Q(3)/(1-3*b0)**2)
assert abs(ga)+abs(gb)<Q(1,5*10**9)
assert Q(224,2187)>Q(1,10)
print('localization_center',a0,b0,'radius_lt',Q(2,10**9))

print('VERIFY_OK subspaces=16 exact_markov=7 witness=167/60 threshold_gap=1/150')
for name in POLYS:print(name,'bernstein_min',str(EXPECTED_MIN[name][0]),'cells',16)
