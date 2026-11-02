"""Exact quadratic-form checks and certified rational-power sign witnesses.

Run: python verify_weighted_triangle_barbell.py
Python 3 only; no external files or dependencies.
"""
from fractions import Fraction as F
from collections import deque
from math import log


def graph_dist(t):
    # vertices: A hub 0; A peripherals 1,2; B hub 3; B peripherals 4,5.
    adj={i:[] for i in range(6)}
    for u,v,w in [(0,1,1),(0,2,1),(1,2,1), (3,4,1),(3,5,1),(4,5,1),(0,3,t)]:
        adj[u].append((v,F(w)));adj[v].append((u,F(w)))
    # Exhaust all simple paths with DFS (not using the proposed metric formula).
    D=[[None]*6 for _ in range(6)]
    for i in range(6):
        todo=[(i,F(0),frozenset([i]))]
        while todo:
            v,d,seen=todo.pop()
            if D[i][v] is None or d < D[i][v]: D[i][v]=d
            for j,w in adj[v]:
                if j not in seen:todo.append((j,d+w,seen|{j}))
    return D


def q_direct(a,p,t):
    D=graph_dist(t)
    return sum(a[i]*a[j]*(D[i][j]**p if i!=j else 0)
               for i in range(6) for j in range(6))


def q_reduced(a,p,t):
    A=t**p;B=(t+1)**p;C=(t+2)**p;L=F(3,2);T=A-2*B+C
    X=a[1]+a[2];Y=a[4]+a[5];u=a[0]+X
    z2=(X-Y)**2/F(2);w2=(X+Y)**2/F(2)
    # Split into the two peripheral internal contrasts, the symmetric radial
    # sector, and the antisymmetric bridge 2x2 block.
    fluct=((a[1]-a[2])**2+(a[4]-a[5])**2)/2
    return (-fluct -2*A*u*u +2*(1+A-B)*u*(X-Y)
            -(L+T)*z2 -(L-T)*w2)

c=0
for t in (F(1,2),F(1),F(3,2),F(4),F(10)):
    for p in (0,1,2,3):
        for k in range(32):
            a=[F(((i*i+3*i+k*7)%13)-6,(i%3)+1) for i in range(6)]
            a[0]=-sum(a[1:])
            assert q_direct(a,p,t)==q_reduced(a,p,t),(t,p,k)
            c+=1
print('EXACT_DISTANCE_QUADRATIC_IDENTITY_OK cases=',c)

# All integer operations below; certificates for rational p=a/b use
# 10^-10 outward intervals for integer base powers via nth-power tests.
SCALE=10**10

def nth_power_bounds(base,a,b):
    x=base**a*(SCALE**b)
    v=int(base**(a/b)*SCALE)
    while (v+1)**b<=x:v+=1
    while v**b>x:v-=1
    assert v**b<=x<(v+1)**b
    return F(v,SCALE),F(v+1,SCALE)

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    a=[u*v for u in x for v in y]
    return (min(a),max(a))
def val(v):return (F(v),F(v))

def margins(t,a,b):
    A=nth_power_bounds(t,a,b)
    B=nth_power_bounds(t+1,a,b)
    C=nth_power_bounds(t+2,a,b)
    T=add(sub(A,mul(val(2),B)),C)
    H=add(sub(val(1),B),A)
    W=sub(val(F(3,2)),T)
    Z=sub(mul(A,add(val(F(3,2)),T)),mul(H,H))
    return W,Z

# The first potential loss at bridge 1 is the symmetric radial direction:
# at p=47/25 the radial margin is negative but the antisymmetric margin
# positive.  At bridge 10 the roles reverse at p=48/25.
w1,z1=margins(1,47,25)
w10,z10=margins(10,48,25)
assert w1[1]<0 and z1[0]>0, (w1,z1)
assert w10[0]>0 and z10[1]<0, (w10,z10)
print('OUTWARD_INTERVAL_SIGNS_OK t=1,p=47/25 W<0,Z>0; t=10,p=48/25 W>0,Z<0')
print('bounds t=1',tuple(tuple(float(z) for z in v) for v in (w1,z1)))
print('bounds t=10',tuple(tuple(float(z) for z in v) for v in (w10,z10)))

# Additional diagnostic for the simultaneous two-dimensional critical
# equality, not part of the analytical existence proof.
def positive_root(t, which):
    def margin(p):
        A=t**p;B=(t+1)**p;C=(t+2)**p;T=A-2*B+C
        return F(3,2)-T if which=='W' else A*(F(3,2)+T)-(1+A-B)**2
    lo,hi=1.,2.
    assert margin(lo)>0 and margin(hi)<0
    for _ in range(80):
        mid=(lo+hi)/2
        if margin(mid)>0: lo=mid
        else:hi=mid
    return (lo+hi)/2
for t in (1,4.5,4.6,10):
    p_w=positive_root(t,'W');p_z=positive_root(t,'Z')
    print('MODE_DIAGNOSTIC',t,format(p_w,'.12f'),format(p_z,'.12f'))
assert positive_root(4.5,'W')<positive_root(4.5,'Z')
assert positive_root(4.6,'W')>positive_root(4.6,'Z')
print('ALL_WEIGHTED_TRIANGLE_BARBELL_CHECKS_OK')
