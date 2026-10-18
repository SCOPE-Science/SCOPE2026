#!/usr/bin/env python3
"""Exact-rational checks for peak-susceptibility bounds in a pulsed logistic flow."""
from fractions import Fraction as F
from itertools import product
from math import log

def f(E, x):
    return E*x / (1+(E-1)*x)

def one_period(initial, q, E):
    x=initial
    pres=[]
    for qi,Ei in zip(q,E):
        pres.append(x)
        x=f(Ei,qi*x)
    return x,pres

def periodic(q,E):
    # Rational Möbius fixed point: input 1 maps to a/(1+b), where a=product E_i q_i.
    gain=F(1)
    for qi,Ei in zip(q,E):gain*=qi*Ei
    y,_=one_period(F(1),q,E)
    # P(1)=gain/(1+b), b=gain/y-1, fixed point (gain-1)/b.
    b=gain/y-1
    assert gain>1 and b>0
    x=(gain-1)/b
    return x, one_period(x,q,E)[1]

def mstar(q,totalE):
    target=log(float(totalE))+sum(log(float(t)) for t in q)
    lo,hi=0.,1.
    for _ in range(100):
        mid=(lo+hi)/2
        phi=sum(log((1-float(qi)*mid)/(1-mid)) for qi in q)
        if phi<target:lo=mid
        else:hi=mid
    return (lo+hi)/2

checks=0
# Exact example: strength factors 1/2 and 3/4; exp(gaps)=4 and 2.
q=[F(1,2),F(3,4)]
start,pres=periodic(q,[F(4),F(2)])
assert start==F(2,3) and pres==[F(2,3),F(2,3)]
checks+=2
Q=F(3,8)
cluster=F(16,21)
assert F(2,3)<cluster
checks+=1
assert (F(8)*Q)==F(3)
checks+=1
assert F(9,8)==(F(8)*Q)**2/F(8)
checks+=1
# Distinct placements with equal total flow exponential factor 8.
for numerator in range(6,63):
    E1=F(numerator,8)
    E2=F(8)/E1
    if E1<=1 or E2<=1: continue
    _,s=periodic(q,[E1,E2])
    high=max(s)
    assert F(2,3)<=high<cluster,(E1,E2,s)
    if E1!=4:assert high>F(2,3)
    checks+=2
# Three heterogeneous pulses, 16 equally in exp-of-time; grid many distinct schedules.
q3=[F(1,2),F(2,3),F(3,4)]
Q3=F(1,4)
threshold=mstar(q3,F(16))
cluster3=F(16*Q3-1,1)/(Q3*(16-1))
for E1 in [F(5,4),F(3,2),F(2),F(3),F(4),F(5),F(6)]:
 for E2 in [F(5,4),F(3,2),F(2),F(3),F(4)]:
    E3=F(16)/(E1*E2)
    if E3<=1:continue
    _,s=periodic(q3,[E1,E2,E3])
    peak=max(s)
    assert float(peak)+1e-11>=threshold and peak<cluster3,(E1,E2,E3,peak,threshold)
    checks+=1
print('SUCCESS',checks,'exact-rational and numeric bound assertions')
print('exact optimum at exp gaps 4,2, peak =',pres[0],'; clustered supremum =',cluster)
print('three-pulse minimax target ~= %.12f ; upper ~= %.12f'%(threshold,float(cluster3)))
