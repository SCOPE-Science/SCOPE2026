#!/usr/bin/env python3
"""Exact finite checks for a three-member symmetric-signal voting theorem."""
from fractions import Fraction as F
from itertools import product
from math import isclose

def explicit_accuracy(xs, bayes):
    n=len(xs)
    v=F(0)
    for bits in product((-1,1),repeat=n):
        prob_pos=F(1); prob_neg=F(1)
        for sig,x in zip(bits,xs):
            prob_pos*= F(1,2)+sig*x
            prob_neg*= F(1,2)-sig*x
        if bayes:
            v+=max(prob_pos,prob_neg)/2
        else:
            weight=sum((xi*sgn for xi,sgn in zip(xs,bits)),F(0))
            if weight>0: v+=prob_pos/2
            elif weight<0: v+=prob_neg/2
            else: v+=(prob_pos+prob_neg)/4
    return v

def claimed_gap(xs):
    z,y,x=sorted(xs)
    s=y+z
    threshold=s/(1+4*y*z)
    if threshold<x<s:
        return (x*(1+4*y*z)-s)/2
    if x==s and y*z>0:
        return (x*(1+4*y*z)-s)/4
    return F(0)

def exhaustive():
    checks=0; positive=0; max_grid=(F(0),None)
    vals=[F(i,40) for i in range(1,20)]
    for i,x in enumerate(vals):
        for j,y in enumerate(vals[:i+1]):
            for z in vals[:j+1]:
                xs=(x,y,z)
                a=explicit_accuracy(xs,True)
                w=explicit_accuracy(xs,False)
                g=a-w
                h=claimed_gap(xs)
                assert g==h,(xs,a,w,g,h)
                assert F(0)<=g<F(1,16),(xs,g)
                checks+=1
                positive+= (g>0)
                if g>max_grid[0]: max_grid=(g,xs)
    return checks,positive,max_grid

def two_agent():
    vals=[F(i,50) for i in range(1,25)]
    for x in vals:
        for y in vals:
            assert explicit_accuracy((x,y),True)==explicit_accuracy((x,y),False)
    return len(vals)**2

def limit_family():
    for N in (20,40,100,1000,100000):
        eps=F(1,N)
        xs=(F(1,2)-eps,F(1,4),F(1,4))
        exact=explicit_accuracy(xs,True)-explicit_accuracy(xs,False)
        assert exact==F(1,16)-F(5,8)*eps
    return True

if __name__=='__main__':
    print('two_agent_profiles',two_agent())
    print('three_agent_lattice',exhaustive())
    print('extremal_rational_family',limit_family())
    print('PASS')
