#!/usr/bin/env python3
"""Reproduce exact rational tests for two-stage A-optimal input timing.
Run with Python 3, standard library only. These finite checks supplement a proof.
"""
from fractions import Fraction as Q
from random import Random

def causal(h, s, eta, beta):
    assert h > 0 and s > 0 and eta > 0 and beta > s
    cap = (s + h*beta)/(1+h)
    star = max(s, min(beta/2, cap))
    q = (star-s)/h
    p = beta-s-(1+h)*q
    return q, p, 1/(eta+star)+1/(eta+beta-star)

def det(h, s, eta, beta):
    cap=(beta-s)/(1+h)
    if cap >= s:
        q,p=cap,Q(0)
    else:
        q,p=Q(0),beta-s
    return q,p,1/(eta+s+h*q)+1/(eta+q+p)

def objective(h,s,eta,q,p,cor2):
    a=s+h*q
    d=q+p
    return (2*eta+a+d)/((eta+a)*(eta+d)-cor2)

rng=Random(20261018)
count=0
for h in [Q(1,16),Q(1,4),Q(1),Q(2),Q(4),Q(16)]:
    for s in [Q(1,2),Q(1),Q(3)]:
        for eta in [Q(1,3),Q(1),Q(5)]:
            for budget_mult in [Q(11,10),Q(2),Q(9,4),Q(3),Q(6),Q(10),Q(40)]:
                beta=s*budget_mult
                qc,pc,fc=causal(h,s,eta,beta)
                qd,pd,fd=det(h,s,eta,beta)
                assert qc>=0 and pc>=0 and s+(1+h)*qc+pc==beta
                assert s+(1+h)*qd+pd==beta
                assert objective(h,s,eta,qd,pd,h*qd*pd)==fd
                assert fd>=fc
                # Deterministic endpoint test: splitting at full budget cannot beat pure strategies.
                qmax=(beta-s)/(1+h)
                for k in range(21):
                    q=qmax*k/20
                    p=beta-s-(1+h)*q
                    assert objective(h,s,eta,q,p,h*q*p)>=fd
                    count+=1
                # Feasible arbitrary randomized / feedback moments via Cauchy bound.
                for _ in range(10):
                    q=qmax*Q(rng.randrange(101),100)
                    p=(beta-s-(1+h)*q)*Q(rng.randrange(101),100)
                    rho=Q(rng.randrange(-10,11),10)
                    cor2=rho*rho*(s+h*q)*p
                    assert objective(h,s,eta,q,p,cor2)>=fc
                    count+=1

h,s,eta,beta=Q(4),Q(1),Q(1),Q(3)
assert causal(h,s,eta,beta)==(Q(1,8),Q(11,8),Q(4,5))
assert det(h,s,eta,beta)==(Q(0),Q(2),Q(5,6))
assert Q(5,6)-Q(4,5)==Q(1,30)
# Exact equality of pure-stage costs at the stage-switch budget.
for h in [Q(1,9),Q(1),Q(4)]:
    s,eta=Q(2),Q(3)
    beta=s*(2+h)
    qmax=(beta-s)/(1+h)
    assert objective(h,s,eta,Q(0),beta-s,Q(0))==objective(h,s,eta,qmax,Q(0),Q(0))
print('PASS:',count,'exact-rational feasible checks and the exact gap witness.')
