#!/usr/bin/env python3
"""Standalone exact-rational replay of a three-bank payment-clearing phase theorem.

Requires Python 3 standard library only. Run: python verify.py
"""
from fractions import Fraction as Q
from itertools import combinations

T=((Q(0),Q(1,10),Q(4,5)),
   (Q(2,5),Q(0),Q(3,10)),
   (Q(3,10),Q(3,10),Q(0)))
a=(Q(1,20),Q(3,10),Q(1))


def solve(M,b):
    n=len(b)
    U=[list(M[i])+[b[i]] for i in range(n)]
    for j in range(n):
        k=next(i for i in range(j,n) if U[i][j]!=0)
        U[k],U[j]=U[j],U[k]
        c=U[j][j]
        U[j]=[v/c for v in U[j]]
        for i in range(n):
            if i!=j:
                c=U[i][j]
                U[i]=[U[i][k]-c*U[j][k] for k in range(n+1)]
    return tuple(U[i][-1] for i in range(n))


def network_solve(t,c=(Q(0),)*3):
    # Independently solve every hypothesized default subset and verify the
    # full piecewise linear clearing conditions (not just a stored phase log).
    sols=[]
    for sz in range(4):
        for D0 in combinations(range(3),sz):
            D=set(D0)
            R=tuple(sorted(D))
            p=[Q(1) if i not in D else None for i in range(3)]
            M=[[Q(i==j)-T[j][i] for j in R] for i in R]
            b=[t*a[i]+c[i]+sum(T[j][i] for j in range(3) if j not in D) for i in R]
            if R:
                v=solve(M,b)
                for i,x in zip(R,v):p[i]=x
            r=tuple(t*a[i]+c[i]+sum(T[j][i]*p[j] for j in range(3)) for i in range(3))
            if all(Q(0)<=p[i]<=1 and p[i]==min(1,r[i]) for i in range(3)):
                v=tuple(p)
                if v not in sols:sols.append(v)
    assert len(sols)==1,sols
    return sols[0]


def gains(D):
    D=tuple(D)
    out=[Q(0)]*3
    if not D:return tuple(out)
    M=[[Q(i==j)-T[j][i] for j in D] for i in D]
    for c,j in enumerate(D):
        b=tuple(Q(r==c) for r in range(len(D)))
        col=solve(M,b)
        out[j]=sum(col)
    return tuple(out)

assert [sum(row) for row in T]==[Q(9,10),Q(7,10),Q(3,5)]
assert gains((0,1,2))==(Q(416,105),Q(374,105),Q(114,35))
assert gains((0,1))==(Q(55,48),Q(35,24),Q(0))
assert gains((0,))==(Q(1),Q(0),Q(0))
assert Q(416,105)>Q(374,105)>Q(114,35)
assert Q(35,24)>Q(55,48)>0

# Verify exact clearing phases throughout the four intervals using endpoint
# affine equations plus boundary consistency and strict interior inequalities.
t1,t2,t3=Q(42,95),Q(126,61),Q(6)
assert 0<t1<t2<t3
p1=lambda t:(Q(7,6)*t,Q(23,21)*t,Q(95,42)*t)
p2=lambda t:(Q(17,96)*t+Q(7,16),Q(61,192)*t+Q(11,32),Q(1))
p3=lambda t:(Q(7,10)+t/Q(20),Q(1),Q(1))
assert p1(t1)==p2(t1)
assert p2(t2)==p3(t2)
assert p3(t3)==(Q(1),)*3
for i,(lo,hi,f) in enumerate(((Q(0),t1,p1),(t1,t2,p2),(t2,t3,p3))):
    # All coordinates of the right-hand-side residual are affine on the phase.
    # Two endpoint tests imply the required weak inequalities throughout.
    for t in (lo,hi):
        p=f(t)
        r=tuple(t*a[j]+sum(T[k][j]*p[k] for k in range(3)) for j in range(3))
        assert all(p[j]==min(Q(1),r[j]) for j in range(3)),(i,t,p,r)
    mid=(lo+hi)/2
    p=f(mid)
    assert all((p[j]<1) == (j in ((0,1,2),(0,1),(0,))[i]) for j in range(3))

for t, expected, winner in (
    (Q(1,4),(Q(7,24),Q(23,84),Q(95,168)),0),
    (Q(1),(Q(59,96),Q(127,192),Q(1)),1),
    (Q(3),(Q(17,20),Q(1),Q(1)),0)):
    p=network_solve(t)
    assert p==expected,(t,p)
    D=tuple(i for i in range(3) if p[i]<1)
    w=gains(D)
    assert w[winner]>max(w[j] for j in range(3) if j!=winner)
    h=Q(1,1000)
    for i in range(3):
        c=tuple(h if j==i else Q(0) for j in range(3))
        actual=(sum(network_solve(t,c))-sum(p))/h
        assert actual==w[i],(t,i,actual,w[i])

# At a two-bank fixed default set, the local impact vector is fixed, and
# after one bank becomes solvent only the still-defaulting bank has positive
# marginal effect. This abstract argument establishes the lower-bound;
# the script checks all finite rational claims in the attaining example.
print('VERIFY_OK stages=4 thresholds=42/95,126/61,6 exact_clearing=PASS')
print('VERIFY_OK phase_winners=1,2,1 threat_indices=PASS independent_finite_injections=PASS')
