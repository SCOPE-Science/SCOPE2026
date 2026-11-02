#!/usr/bin/env python3
"""Exact rational identities and deterministic numerical checks for two-community opinion dynamics."""
from fractions import Fraction as Q
from itertools import product

checks = 0

def verify(pred, label):
    global checks
    if not pred:
        raise AssertionError(label)
    checks += 1

def F(x, s):
    return x*s/(x*s + (1-x)*(1-s))

def step(u,v,h,r):
    A = h*r
    B = Q(1)
    C = r
    D = h
    return F(u,(A*u+B*v)/(A+B)),F(v,(C*u+D*v)/(C+D))

# Exact reciprocity, strict monotonicity, and initial sign thresholds.
for h in [Q(3,2),Q(2),Q(3),Q(4),Q(5,2)]:
    for r in [Q(1,5),Q(1,2),Q(1),Q(2),Q(3),Q(4),Q(5)]:
        for d in [Q(1,10),Q(1,5),Q(2,5)]:
            u,v=Q(1)-d,d
            un,vn=step(u,v,h,r)
            a=h*r
            c=r
            verify((un>u)==(a>1),"first island initial drift")
            verify((vn>v)==(c>h),"second island initial drift")
            verify((un==u)==(a==1),"first island threshold tie")
            verify((vn==v)==(c==h),"second island threshold tie")
            verify(0<un<1 and 0<vn<1,"interior invariance")
            if r>=h:
                verify(un>u and vn>=v,"overdominant monotonic start")
            if r<=1/h:
                verify(un<=u and vn<v,"underdominant monotonic start")

# Exact critical corner identity and complementary-start first-step property.
for h in [Q(3,2),Q(2),Q(3),Q(4)]:
    for i in range(1,40):
        v=Q(i,41)
        vnext=step(Q(1),v,h,h)[1]
        verify(vnext==v*(1+v)/(1-v+2*v*v),"corner recurrence")
        verify(1/v-1/vnext==2*(1-v)/(1+v),"corner reciprocal increment")
        e=Q(i,82)
        uu,vv=step(1-e,e,h,h)
        verify(vv==e and uu>1-e,"critical complementary first step")

# General exact reciprocal identity, all points with v >= e.
for e in [Q(1,20),Q(1,5),Q(1,3)]:
    for j in range(1,31):
        v=e+(1-e)*Q(j,32)
        if v>=1: continue
        vv=F(v,(1-e+v)/2)
        verify(1/v-1/vv==2*(1-v)*(v-e)/(v*(1-e+v)),"exact critical reciprocal")

# The critical hitting-time constant is supported by numerical trajectories;
# the uniform asymptotic proof is in RESULT.md, not inferred from these runs.
def float_trajectory(h,d,threshold=.25,limit=200000):
    r=h
    u,v=1-d,d
    for t in range(limit):
        if v>=threshold:
            return t
        s1=(h*r*u+v)/(h*r+1)
        s2=(r*u+h*v)/(r+h)
        u,v=float(F(u,s1)),float(F(v,s2))
    raise RuntimeError('trajectory did not cross threshold')
for h in [1.5,2.,3.,6.]:
    previous = None
    for d in [0.01,0.001,0.0001]:
        t=float_trajectory(h,d)
        verify(abs(d*t-.5)<.06,"critical inverse-duration law")
        if previous is not None:
            verify(abs(d*t-.5)<previous,"convergence of critical coefficient")
        previous=abs(d*t-.5)

print('VERIFY_OK assertions=',checks)
