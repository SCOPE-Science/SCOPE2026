#!/usr/bin/env python3
"""Exact rational check for a finite semi-Markov first-passage identity.

The mathematical proof does not depend on this illustrative calculation.
"""
from functools import lru_cache
from fractions import Fraction as F
import sympy as sp

P = sp.Matrix([
    [0, sp.Rational(1,2), sp.Rational(1,2)],
    [sp.Rational(1,3), 0, sp.Rational(2,3)],
    [sp.Rational(3,4), sp.Rational(1,4), 0],
])
mu = sp.Matrix([
    [0, 1, 2],
    [sp.Rational(3,2), 0, sp.Rational(1,2)],
    [1, 2, 0],
])
v = sp.Matrix([[mu[i,j]**2/2 for j in range(3)] for i in range(3)])
I = sp.eye(3)
# Solve stationarity exactly with one normalization equation.
A = (P.T-I)
A[2,:] = sp.Matrix([[1,1,1]])
pi = A.inv()*sp.Matrix([0,0,1]); pi=sp.Matrix(pi)
assert (P.T*pi-pi)==sp.zeros(3,1)
mean_mu = sum(pi[i]*P[i,j]*mu[i,j] for i in range(3) for j in range(3))
mean_v = sum(pi[i]*P[i,j]*v[i,j] for i in range(3) for j in range(3))
B = sp.cancel(mean_v/mean_mu)
g = sp.Matrix([[v[i,j]-B*mu[i,j] for j in range(3)] for i in range(3)])
gbar = sp.Matrix([sum(P[i,j]*g[i,j] for j in range(3)) for i in range(3)])
K=I-P+sp.ones(3,1)*sp.Matrix([list(pi)] ) # rank-one projection, row pi
h=K.inv()*gbar
assert (I-P)*h==gbar
osc=max(h)-min(h)
mu_max=max(mu[i,j] for i in range(3) for j in range(3) if P[i,j])

# All edge marks below are positive, giving a finite recursion over every path.
base={ (i,j):sp.Rational(mu[i,j]) for i in range(3) for j in range(3) if P[i,j] }
gauge={ (i,j):mu[i,j]+sp.Rational(1,4)*(i-j) for (i,j) in base }
unit={ e:sp.Integer(1) for e in base }
choices={'mean_dwell':base,'perturbed_dwell':gauge,'raw_count':unit}

@lru_cache(None)
def moments(i,level,marks_items):
    # Recursively integrate the jump-chain path until the first marked crossing.
    marks=dict(marks_items)
    # Returns E M, E M², E V, E g-total, E h(end), E overshoot, E overshoot²
    # For an initial pre-jump state i, M=sum means, V=sum variances.
    rows=[]
    for j in range(3):
        if not P[i,j]:continue
        a=marks[(i,j)]; m=mu[i,j]; vv=v[i,j]; gg=g[i,j]
        if a>=level:
            vals=(m,m*m,vv,gg,h[j],a-level,(a-level)**2)
        else:
            rest=moments(j,level-a,marks_items)
            em,em2,ev,eg,eh,eu,eu2=rest
            vals=(m+em,m*m+2*m*em+em2,vv+ev,gg+eg,eh,eu,eu2)
        rows.append((P[i,j],vals))
    return tuple(sp.factor(sum(p*vals[n] for p,vals in rows)) for n in range(7))

checks=0
for label,marks in choices.items():
    assert min(marks.values())>0
    marks_items=tuple(sorted(marks.items()))
    for k in map(sp.Rational,('1/2','1','3/2','2','3','4','5','7')):
        em,em2,ev,eg,eh,eu,eu2=moments(0,k,marks_items)
        var_M=em2-em**2
        var_H=ev+var_M
        # Poisson martingale stopping equality.
        assert sp.factor(eg-(h[0]-eh))==0, (label,k,'martingale')
        # Universal finite threshold exact decomposition.
        assert sp.factor(var_H-B*em-(var_M+h[0]-eh))==0,(label,k,'decomposition')
        assert sp.factor(var_H-B*em+osc)>=0,(label,k,'bound')
        if label=='mean_dwell':
            # for optimal alpha=mu, marked overshoot is same as time overshoot.
            assert em==k+eu
            assert sp.factor(var_M-(eu2-eu**2))==0
            assert var_M <= mu_max**2/4
        checks+=1
print('pi=',list(pi))
print('mean_mu=',mean_mu,'mean_v=',mean_v,'B=',B)
print('h=',list(h),'osc=',osc,'mu_max=',mu_max)
print('PASS: exact finite-first-passage tests:',checks)
