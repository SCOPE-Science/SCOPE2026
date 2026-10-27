#!/usr/bin/env python3
"""Exact finite checks and independent floating constructions for rank-two RPCholesky.
Requires Python 3 standard library only. Not a proof of infinite quantifiers.
"""
from fractions import Fraction as F
from collections import defaultdict
import random, math

def tr(mat):return sum(mat[i][i] for i in range(len(mat)))

def gram(rows):return [[sum(rows[i][k]*rows[j][k] for k in (0,1)) for j in range(len(rows))] for i in range(len(rows))]

def law_from_gram(A):
    T=tr(A)
    assert T>0
    ret=defaultdict(F)
    for i,row in enumerate(A):
        if A[i][i]==0:continue
        residual=F(T)-F(sum(A[j][i]**2 for j in range(len(A))),A[i][i])
        ret[residual]+=F(A[i][i],T)
    return dict(ret)

def validate(rows):
    A=gram(rows)
    d=law_from_gram(A)
    T=tr(A)
    s11=sum(v[0]*v[0] for v in rows)
    s22=sum(v[1]*v[1] for v in rows)
    s12=sum(v[0]*v[1] for v in rows)
    det=s11*s22-s12*s12
    if not det:return 0
    avg=sum(x*p for x,p in d.items())
    assert sum(d.values())==1
    assert avg==F(2*det,T)
    second=sum((x-avg)**2*p for x,p in d.items())
    maxvar=F(det*(T*T-4*det),T*T)
    assert F(0)<=second<=maxvar
    discriminant=T*T-4*det
    lam_min=(float(T)-math.sqrt(float(discriminant)))/2
    lam_max=(float(T)+math.sqrt(float(discriminant)))/2
    for x in d:
        assert lam_min-1e-8<=float(x)<=lam_max+1e-8
    return len(d)

# Endpoints and deterministic extremizer: same spectrum (20,2).
for B,expected in [
    ([(3,0),(3,0),(1,1),(1,-1)], {F(2):F(9,11),F(11):F(2,11)}),
]:
    if expected is not None:
        assert law_from_gram(gram(B))==expected

endpoints=[[F(20),F(0)],[F(0),F(2)]]
assert law_from_gram(endpoints)=={F(2):F(10,11),F(20):F(1,11)}
deterministic=[[F(11),F(9)],[F(9),F(11)]]
assert law_from_gram(deterministic)=={F(40,11):F(1)}
assert validate([[3,0],[3,0],[1,1],[1,-1]])==2

rng=random.Random(20261024)
count=0
for n in range(2,10):
    for _ in range(140):
        B=[[F(rng.randint(-8,8)),F(rng.randint(-8,8))] for _ in range(n)]
        # May contain zero rows; those receive zero pivot probability.
        if sum(x*x+y*y for x,y in B)==0:continue
        count+=bool(validate(B))

# Realizability of an arbitrary finitely supported distribution, illustrated
# on three atoms using the explicit +/- construction.
for trial in range(100):
    l1=2+rng.uniform(0,20)
    l2=0.1+rng.uniform(0,0.9)*(l1-0.1)
    T=l1+l2
    mu=l2/T
    eta=0.02+0.9*rng.random()
    weights=[eta*(1-mu),1-eta,eta*mu]
    ts=[0,mu,1]
    rows=[]
    for w,t in zip(weights,ts):
        c=math.sqrt(w*T/2)
        rows.extend([(c*math.sqrt(1-t),c*math.sqrt(t)),
                     (c*math.sqrt(1-t),-c*math.sqrt(t))])
    S11=sum(x*x for x,y in rows)
    S22=sum(y*y for x,y in rows)
    S12=sum(x*y for x,y in rows)
    assert abs(S11-l1)<1e-9 and abs(S22-l2)<1e-9 and abs(S12)<1e-9
    for j in range(3):
        r=l2+(l1-l2)*ts[j]
        norm2=sum(z*z for z in rows[2*j])
        ray=l1*rows[2*j][0]**2/norm2+l2*rows[2*j][1]**2/norm2
        assert abs(T-ray-r)<1e-8
        assert abs((2*norm2/T)-weights[j])<1e-8

print('PASS: exact 1-step laws, expectations, variance envelopes, and ' + str(count) + ' integer Gram trials; 100 three-atom realisability trials.')
