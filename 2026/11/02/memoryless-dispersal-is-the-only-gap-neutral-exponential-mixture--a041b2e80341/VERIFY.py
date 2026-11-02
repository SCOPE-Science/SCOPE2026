#!/usr/bin/env python3
"""Deterministic, dependency-free finite consistency checks for the stated dispersal formulas.
These tests do not replace the analytic all-parameter proof.
"""
from math import exp, sqrt, isclose
from random import Random

checks=0

def near(x,y,tol=1e-11):
    global checks
    checks += 1
    assert abs(x-y) <= tol*max(1.,abs(x),abs(y)), (x,y)

def kappa_kernel(t,L,k):
    return k*exp(-k*(t%L))/(1-exp(-k*L))

def dloc(l,L,k):
    z=exp(-k*L)
    return (l-(1-exp(-k*l))/k+z*((exp(k*l)-1)/k-l))/(l*(1-z))

def matrix(starts,lengths,L,k):
    n=len(starts)
    mat=[[0.]*n for _ in range(n)]
    for i in range(n):
        mat[i][i]=dloc(lengths[i],L,k)
        for j in range(n):
            if i==j: continue
            off=(exp(k*lengths[j])-1)*(1-exp(-k*lengths[i]))/(k*lengths[j]*(1-exp(-k*L)))
            off*=exp(k*(starts[j]-starts[i]))
            if i<j: off*=exp(-k*L)
            mat[i][j]=off
    return mat

def matprod(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def trace(A):return sum(A[i][i] for i in range(len(A)))

def rho2(A):
    return (A[0][0]+A[1][1])/2+sqrt(((A[0][0]-A[1][1])/2)**2+A[0][1]*A[1][0])

def b(k,l1,l2,L):
    return (1-exp(-k*l1))*(1-exp(-k*l2))/(k*(1-exp(-k*L)))

def mixmatrix(g,l1,l2,L,ks,ws):
    s=[0,l1+g]
    Ms=[matrix(s,[l1,l2],L,k) for k in ks]
    return [[sum(w*Ms[r][i][j] for r,w in enumerate(ws)) for j in range(2)] for i in range(2)]

def explicit_rho(g,l1,l2,L,ks,ws,q1,q2):
    H=L-l1-l2
    f=lambda t:sum(w*b(k,l1,l2,L)*exp(-k*t) for k,w in zip(ks,ws))
    d1=sum(w*dloc(l1,L,k) for k,w in zip(ks,ws))*q1
    d2=sum(w*dloc(l2,L,k) for k,w in zip(ks,ws))*q2
    return (d1+d2)/2+sqrt(((d1-d2)/2)**2+q1*q2*f(g)*f(H-g)/(l1*l2))

def direct_offdiag(source_start,source_length,target_start,target_length,L,k,n=120):
    # Independent two-dimensional midpoint quadrature of the wrapped probability density.
    dx=source_length/n;dy=target_length/n
    total=0.
    for i in range(n):
        x=source_start+(i+.5)*dx
        for j in range(n):
            y=target_start+(j+.5)*dy
            total+=kappa_kernel(y-x,L,k)
    return total*dx*dy/source_length

for rate in (.6,2.5,11.):
    for gap in (.015,.16,.48):
        starts=[0,.13+gap];lengths=[.13,.21];L=1.
        A=matrix(starts,lengths,L,rate)
        for i,j in ((0,1),(1,0)):
            numerical=direct_offdiag(starts[j],lengths[j],starts[i],lengths[i],L,rate)
            near(numerical,A[i][j],2e-4)

rng=Random(9427)
for it in range(45):
    L=1.0
    lengths=[.025+rng.random()*.065 for _ in range(4)]
    free=L-sum(lengths)
    g1=[rng.random() for _ in lengths];g2=[rng.random() for _ in lengths]
    g1=[free*x/sum(g1) for x in g1];g2=[free*x/sum(g2) for x in g2]
    def starts(gs):
        s=[0.]
        for i in range(3):s.append(s[-1]+lengths[i]+gs[i])
        return s
    s1,s2=starts(g1),starts(g2)
    k=.2+8*rng.random()
    A=matrix(s1,lengths,L,k);B=matrix(s2,lengths,L,k)
    factors=[exp(-k*(s2[i]-s1[i])) for i in range(4)]
    for i in range(4):
        for j in range(4):near(B[i][j],factors[i]*A[i][j]/factors[j])
    for r in range(1,5):
        for i in range(4):near(matprod(A,A)[i][i],matprod(B,B)[i][i]) if r==2 else None
    P=A[:];Q=B[:]
    for r in range(1,5):
        near(trace(P),trace(Q));P=matprod(P,A);Q=matprod(Q,B)

for it in range(120):
    L=1.; l1=.04+.17*rng.random();l2=.04+.17*rng.random();H=L-l1-l2
    ks=[.1+14*rng.random() for _ in range(3)];w=[rng.random() for _ in ks];w=[x/sum(w) for x in w]
    q1=.2+3*rng.random();q2=.2+3*rng.random()
    mid=H/2
    values=[]
    for idx in range(13):
        g=H*idx/12
        M=mixmatrix(g,l1,l2,L,ks,w)
        A=[[q1*M[i][j] if i==0 else q2*M[i][j] for j in range(2)] for i in range(2)]
        near(rho2(A),explicit_rho(g,l1,l2,L,ks,w,q1,q2))
        near(explicit_rho(g,l1,l2,L,ks,w,q1,q2),explicit_rho(H-g,l1,l2,L,ks,w,q1,q2))
        values.append(rho2(A))
    for j in range(6):
        if max(ks)-min(ks)>1e-5:
            checks+=1;assert values[j]>values[j+1],(values,j)
        near(values[j],values[-1-j])

# Exact zero-gap and midpoint test crossing the linear persistence threshold.
L=1.;l=.1;ks=[2.,12.];ws=[.5,.5];H=L-2*l
for g,r_expected in ((0,.347057101751542),(.4,.31572839897952054),(.8,.347057101751542)):
    near(explicit_rho(g,l,l,L,ks,ws,1,1),r_expected)
checks+=1;assert 3*explicit_rho(0,l,l,L,ks,ws,1,1)>1
checks+=1;assert 3*explicit_rho(H/2,l,l,L,ks,ws,1,1)<1

# Single-rate mixture is gap-invariant including unequal widths.
for it in range(50):
    l1=.03+.17*rng.random();l2=.03+.17*rng.random();H=1-l1-l2;k=.1+10*rng.random()
    v=[explicit_rho(g,l1,l2,1,[k],[1.],1.4,.7) for g in (0,H/9,H/2,H*8/9,H)]
    for x in v:near(x,v[0])

print('VERIFY_OK assertions='+str(checks))
