#!/usr/bin/env python3
"""Checks for the reciprocal-latency SEIR theorem.

Requires Python 3, sympy, scipy. Symbolic identities are exact;
finite integrations are regression checks, not global proofs.
"""
import math
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

R, l, S, E, I, J, v = sp.symbols('R l S E I J v', positive=True)
mu = 1/l
F = sp.Matrix([-R*S*I, R*S*I-l*E, l*E-I, I])
P = sp.Matrix([S, E+(1-1/l)*I, I/l, sp.Symbol('Recovered')])
D = sp.Matrix([[1,0,0,0],[0,1,1-1/l,0],[0,0,1/l,0],[0,0,0,1]])
transformed = (D*F)/l
rhs_dual = sp.Matrix([-R*P[0]*P[2],R*P[0]*P[2]-mu*P[1],mu*P[1]-P[2],P[2]])
assert all(sp.simplify(x)==0 for x in transformed-rhs_dual)
a=l/(1+l)
kappa=(l+1)**2/l
original_di_dy=(l*J-(l+1)*a*v)/(R*a*v)
assert sp.simplify(original_di_dy/a-kappa*(J-v)/(R*v)) == 0
print('exact conjugacy and scalar-phase identities: PASS')


def seir_peak(rep, rate, eps=1e-8):
    growth = (-(rate+1)+math.sqrt((rate-1)**2+4*rate*rep))/2
    ratio_e_to_i=(growth+1)/rate
    i0=eps/(1+ratio_e_to_i)
    e0=eps-i0
    def rhs(t,state):
        s,e,i=state
        return (-rep*s*i, rep*s*i-rate*e, rate*e-i)
    def peak(t,state):
        return rate*state[1]-state[2]
    peak.direction=-1
    peak.terminal=True
    result=solve_ivp(rhs,(0,2000),[1-eps,e0,i0],events=peak,
                     method='DOP853',rtol=2e-11,atol=2e-13,max_step=.3)
    assert result.success and len(result.t_events[0])==1
    s,e,i=result.y_events[0][0]
    assert 0<s<1/rep and e>0 and i>0
    return s

for rep in (1.5,2.0,3.0):
    peaks={rate:seir_peak(rep,rate) for rate in (.25,.5,1,2,4)}
    assert abs(peaks[.25]-peaks[4])<5e-8
    assert abs(peaks[.5]-peaks[2])<5e-8
    assert peaks[1]<peaks[2]<peaks[4]<1/rep
    print('rep',rep,'peaks:',peaks)

rep=2
s_end=brentq(lambda s:math.log(s)+rep*(1-s),.001,1/rep)
for rate in (.1,1,10):
    s=seir_peak(rep,rate)
    print('rate',rate,'post-peak infection fraction',s-s_end)
print('all checks PASS')
