#!/usr/bin/env python3
"""Exact checks for two-community mean-field stationary-state barrier.

All arithmetic uses Python's standard-library Fraction; this is a finite
reproducibility check, not a replacement for the analytic all-parameter proof.
"""
from fractions import Fraction as Q
from itertools import product


def original_rhs(x, y, b, c, e, f):
    S = x + y
    return (-x + (1-x) * (
        b*Q(1,2)*(S+e*(x-y)) +
        c*Q(1,4)*(S*S+f*(3*x*x-2*x*y-y*y))
    ))


def pressure(x,y,b,c,e,f):
    S=x+y
    return b*(1-e)*S/Q(2)+c*(1-f)*S*S/Q(4)+b*e*x+c*f*x*x


def h(x,u,v):
    return x/(1-x)-u*x-v*x*x


def derivative(x,u,v):
    return Q(1)/(1-x)**2-u-2*v*x


# Check exact rearrangement across a nontrivial grid, including boundary e,f.
num = 0
for x, y in product([Q(1,7),Q(2,7),Q(5,7)],repeat=2):
    for b,c,e,f in product([Q(1,5),Q(9,5)], [Q(3,7),Q(17,4)],
                             [Q(0),Q(1,2),Q(1)], [Q(0),Q(3,4),Q(1)]):
        rhs=original_rhs(x,y,b,c,e,f)
        pp=pressure(x,y,b,c,e,f)
        assert rhs == -x+(1-x)*pp
        L=b*(1-e)*(x+y)/2+c*(1-f)*(x+y)**2/4
        assert pp==L+b*e*x+c*f*x*x
        assert rhs/(1-x)==L-h(x,b*e,c*f)
        num+=1

# Exact constructive witness: genuinely asymmetric interior fixed point.
b=Q(19,54); c=Q(154,45); e=Q(27,95); f=Q(1)
x=Q(1,4); y=Q(1,2)
u=b*e; v=c*f
assert u==Q(1,10) and v==Q(154,45)
assert original_rhs(x,y,b,c,e,f)==0
assert original_rhs(y,x,b,c,e,f)==0
assert h(x,u,v)==h(y,u,v)==Q(17,180)
assert derivative(Q(2,5),u,v)==-Q(3,50)
assert 0<=e<=1 and 0<=f<=1 and x != y

# The prescribed positive common-pressure construction is exact at x,y.
L=b*(1-e)*(x+y)/2+c*(1-f)*(x+y)**2/4
assert L==Q(17,180)
assert b==u+2*L/(x+y)

# On sample u<1 and v<=1, h' positive, tested as a bounded numerical sanity check.
for uu in [Q(0),Q(1,10),Q(9,10)]:
    for vv in [Q(0),Q(1,2),Q(1)]:
        for z in [Q(i,50) for i in range(1,50)]:
            assert derivative(z,uu,vv)>0
print('PASS:',num,'exact original/reduced-equation identities, rational asymmetric equilibrium, derivative sign and monotone-regime checks')
