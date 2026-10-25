#!/usr/bin/env python3
"""Exact rational checks of a three-node pure neighborhood-compromise phase transition.

This code checks finite edge words and exact moment identities; its finite enumerations
are not the proof of almost-sure convergence or nonconvergence.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial

EDGES = [(0,1), (1,2)]
NEIGHBORS = {0:(1,), 1:(0,2), 2:(1,)}

def pure_ndw_step(x, chosen_edge, rho, epsilon):
    i,j=EDGES[chosen_edge]
    y=list(x)
    mi=sum(x[k] for k in NEIGHBORS[j])/len(NEIGHBORS[j])
    mj=sum(x[k] for k in NEIGHBORS[i])/len(NEIGHBORS[i])
    ri=abs(x[i]-mi) < epsilon
    rj=abs(x[j]-mj) < epsilon
    if ri: y[i]=x[i]+rho*(x[j]-x[i])
    if rj: y[j]=x[j]+rho*(x[i]-x[j])
    return tuple(y),(ri,rj)

def calc_var(values):
    mean=sum(values,F(0))/len(values)
    return sum(((v-mean)**2 for v in values),F(0))/len(values)

count=0
for rho in (F(1,2),F(1,3),F(1,5)):
    for eps in (F(1,4),F(1,2),F(3,5),F(1,1)):
        for c0 in (F(0),F(2,5),F(1)):
            for depth in range(0,10):
                for word in product((0,1),repeat=depth):
                    v=(F(0),c0,F(1))
                    total=sum(v)
                    for e in word:
                        nv, gate=pure_ndw_step(v,e,rho,eps)
                        if eps<=F(1,2):
                            assert nv[0]==0 and nv[2]==1
                            expected=(1-rho)*v[1]+rho*e
                            assert nv[1]==expected
                        else:
                            assert 0<=nv[0]<=nv[1]<=nv[2]<=1
                            assert nv[2]-nv[0]<=1
                            assert sum(nv)==total
                            assert all(gate)
                        v=nv
                    count+=1
print('exact edge-word trajectories checked:',count)

# Exact contraction identity on a random bilateral edge when both leaf gates are open.
# Variance about the conserved arithmetic mean decreases by 2*rho*(1-rho)
# times the squared discrepancy on the selected edge.
contract_checks=0
for rho in (F(1,2),F(1,3)):
    for a,c,b in product((F(0), F(1,5), F(2,5), F(3,5), F(4,5), F(1)), repeat=3):
        if not a<=c<=b: continue
        x=(a,c,b)
        mu=sum(x)/3
        V=sum(((v-mu)**2 for v in x),F(0))
        for e in (0,1):
            y,g=pure_ndw_step(x,e,rho,F(2))
            assert g==(True,True)
            diff=x[EDGES[e][0]]-x[EDGES[e][1]]
            Vy=sum(((v-mu)**2 for v in y),F(0))
            assert Vy==V-2*rho*(1-rho)*diff*diff
            contract_checks+=1
        assert (c-a)**2+(b-c)**2-V==(a+b-2*c)**2/3
print('exact bilateral energy checks:',contract_checks)

# Exact finite-time moments of center AR(1) for the closed-leaf case.
moment_checks=0
for rho in (F(1,2),F(1,3),F(1,5)):
    lam=1-rho
    c0=F(2,5)
    for depth in range(0,9):
        vals=[]
        for word in product((0,1), repeat=depth):
            c=c0
            for e in word:
                c=lam*c+rho*e
            vals.append(c)
        assert sum(vals,F(0))/len(vals)==F(1,2)+lam**depth*(c0-F(1,2))
        assert calc_var(vals)==rho/(4*(2-rho))*(1-lam**(2*depth))
        moment_checks+=1
print('exact AR(1) moment checks:',moment_checks)

# At rho=1/2, the exact finite law is a shifted uniform dyadic mesh,
# whose CDF has Kolmogorov error at most 2^{-depth} from uniform [0,1].
for depth in range(1,11):
    values=[]
    for word in product((0,1),repeat=depth):
        c=F(2,5)
        for b in word: c=(c+b)/2
        values.append(c)
    expected=[(F(2,5)+k)/2**depth for k in range(2**depth)]
    assert sorted(values)==expected
print('uniform dyadic stationary-limit mesh checks:',10)

# Generic star locked-leaf condition, using exact rational means, for 3+ leaves.
for leaves in ((F(0),F(0),F(1),F(1)),(F(0),F(1),F(1),F(0))):
    avg=sum(leaves,F(0))/len(leaves)
    for eps in (F(1,4),F(1,2)):
        assert all(abs(z-avg)>=eps for z in leaves)
print('locked-leaf gate checks: PASS')
print('ALL EXACT CHECKS PASS')
