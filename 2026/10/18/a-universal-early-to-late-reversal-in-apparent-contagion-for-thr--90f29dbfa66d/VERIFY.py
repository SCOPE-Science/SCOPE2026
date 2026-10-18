#!/usr/bin/env python3
"""Standalone verification of exact transient SIR-group identity.
Only the Python standard library is needed.
"""
import math

def states(lam,t):
    A=math.exp(-(1+2*lam)*t)
    B=2*lam*A*(-math.expm1(-t))
    D=4/(1+lam)*math.exp(-(1+lam)*t)*(-math.expm1(-lam*t)-lam*(math.exp(-lam*t)-math.exp(-(1+lam)*t)))
    # equivalent stable form: 1-(1+lam)exp(-lam*t)+lam exp(-(1+lam)*t)
    return A,B,D

def h(lam,t):
    A,B,D=states(lam,t)
    return B/(2*A+D)

def uni(lam,t):
    # independent forward solution for the states A,B,C,D,F,G,absorbed.
    # transitions: A->B 2lam, A->absorbed 1; B->C 2lam,B->D 2;
    # C->F 3; D->F lam,D->absorbed 1; F->G 2;G->absorbed 1.
    outs=(((1,2*lam),(6,1)),((2,2*lam),(3,2)),((4,3),),((4,lam),(6,1)),((5,2),),((6,1),),())
    q=max(sum(v for _,v in row) for row in outs)
    P=[]
    for row in outs:
        rr=[0.0]*7
        for j,v in row:rr[j]+=v/q
        rr[len(P)]+=1-sum(rr)
        P.append(rr)
    v=[1.0]+[0.0]*6; weights=math.exp(-q*t)
    result=[weights*x for x in v]
    for n in range(1,160):
        nv=[sum(v[i]*P[i][j] for i in range(7)) for j in range(7)]
        v=nv;weights*=q*t/n
        for j in range(7): result[j]+=weights*v[j]
    return result

nchecks=0
for lam in (0.2,0.5,1.,2.,4.,7.):
    for t in (0.005,0.03,0.1,0.5,1.,2.,4.):
        A,B,D=states(lam,t)
        p=uni(lam,t)
        for v,w in ((A,p[0]),(B,p[1]),(D,p[3])):
            assert abs(v-w)<2e-12,(lam,t,v,w)
            nchecks+=1
        assert A>=0 and B>=0 and D>=-1e-14
        nchecks+=1
        assert abs(h(lam,t)-B/(2*A+D))<1e-13
        nchecks+=1

def means(t,la=1,lb=2):
    a,b,d=states(la,t);aa,bb,dd=states(lb,t)
    w1a=2*a+d;w1b=2*aa+dd
    v1=(la*w1a+lb*w1b)/(w1a+w1b)
    v2=(la*b+lb*bb)/(b+bb)
    return v1,v2
for t,sign in ((0.001,1),(0.03,1),(0.1,1),(0.25,1),(2.,-1),(3.,-1),(4.,-1)):
    v1,v2=means(t)
    assert sign*(v2-v1)>0,(t,v1,v2)
    nchecks+=1
print('PASS checks:',nchecks)
for t in (.1,2.):print('t=',t,'lambda1,lambda2=',means(t))
