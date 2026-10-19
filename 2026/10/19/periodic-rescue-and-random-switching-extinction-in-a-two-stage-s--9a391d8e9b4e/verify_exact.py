#!/usr/bin/env python3
"""Exact calculations for the two-stage semelparous switching theorem.

Requires Python 3 and SymPy. Finite checks corroborate, but do not replace,
the ergodic-theorem and Perron-Frobenius arguments in the proof.
"""
from fractions import Fraction as Q
from itertools import product
import random
import math
import sympy as s

q,x=s.symbols('q x')
b1,b2,c1,c2=s.symbols('b1 b2 c1 c2', positive=True)
B1=s.Matrix([[0,b1],[c1,0]])
B2=s.Matrix([[0,b2],[c2,0]])
assert B2*B1==s.diag(b2*c1,c2*b1)
assert B1*B2==s.diag(b1*c2,c1*b2)
assert B1*B1==b1*c1*s.eye(2)
assert B2*B2==b2*c2*s.eye(2)
A1=B1.subs({b1:4,c1:s.Rational(1,16)})
A2=B2.subs({b2:s.Rational(1,4),c2:1})
assert A1**2==A2**2==s.eye(2)/4
assert (A2*A1).eigenvals()=={s.Rational(1,64):1,s.Integer(4):1}
M=s.BlockMatrix([[q*A1,(1-q)*A1],[(1-q)*A2,q*A2]]).as_explicit()
f=(8*x*x+17*(1-q)*x+2-4*q)*(8*x*x-17*(1-q)*x+2-4*q)/64
assert s.simplify(M.charpoly(x).as_expr()-f)==0
p=8*x*x-17*(1-q)*x+2-4*q
assert s.factor(p.subs(x,1))==13*q-7
assert s.simplify(M.charpoly(x).as_expr().subs(x,1) + 3*(7*q-9)*(13*q-7)/64)==0
assert s.simplify(p.subs({x:1,q:s.Rational(7,13)}))==0
assert s.simplify(p.subs({x:1,q:s.Rational(1,2)}))<0
assert s.simplify(p.subs({x:1,q:s.Rational(3,4)}))>0

def matmul2(A,z):
    return (A[0][0]*z[0]+A[0][1]*z[1],A[1][0]*z[0]+A[1][1]*z[1])
A1q=((Q(0),Q(4)),(Q(1,16),Q(0)))
A2q=((Q(0),Q(1,4)),(Q(1),Q(0)))

def brute(t, qq):
    z0=(Q(1),Q(1))
    total=[Q(0),Q(0)]
    for moves in product((0,1),repeat=t-1):
        env=0
        prob=Q(1)
        zz=z0
        for i in range(t):
            if i:
                next_env=moves[i-1]
                prob*=qq if next_env==env else 1-qq
                env=next_env
            zz=matmul2((A1q,A2q)[env],zz)
        for j in range(2):total[j]+=prob*zz[j]
    return tuple(total)

def dynamic(t,qq):
    by_env=((Q(1),Q(1)),(Q(0),Q(0)))
    for i in range(t):
        left=tuple(qq*by_env[0][j]+(1-qq)*by_env[1][j] for j in range(2)) if i else by_env[0]
        right=tuple((1-qq)*by_env[0][j]+qq*by_env[1][j] for j in range(2)) if i else (Q(0),Q(0))
        by_env=(matmul2(A1q,left),matmul2(A2q,right))
    return tuple(sum(by_env[k][j] for k in range(2)) for j in range(2))

checked=0
for qq in [Q(1,10),Q(1,4),Q(1,2),Q(7,13),Q(3,4),Q(9,10)]:
    for t in range(1,9):
        assert dynamic(t,qq)==brute(t,qq), (qq,t)
        checked+=1

# Numerical trajectory diagnostics under two mixing chains. Not a proof of
# any almost-sure statement.
def sampled_log_rate(qq,steps,seed):
    gen=random.Random(seed)
    env=0
    z=[1.0,1.0]
    lognorm=0.0
    for i in range(steps):
        if i and gen.random()>qq:env=1-env
        A=((0.0,4.0,1/16),(0.0,1/4,1.0))[env]
        z=[A[1]*z[1],A[2]*z[0]]
        scale=max(z)
        lognorm+=math.log(scale)
        z=[t/scale for t in z]
    return lognorm/steps
for qq in [0.1,0.4,0.8]:
    observed=sampled_log_rate(qq,80000, int(1000*qq)+97)
    assert abs(observed+math.log(2))<0.10,(qq,observed)

print('PASS: symbolic products, spectral identities, characteristic factor, and threshold')
print('PASS: %d independent rational path-enumeration / block-recurrence comparisons' % checked)
print('PASS: sample-path numerical diagnostics for 3 mixing parameters')
print('EXACT: rho(A1)=rho(A2)=1/2; rho(A2 A1)^(1/2)=2')
print('EXACT: a.s. growth=1/2 for 0<q<1; E-mass growth crosses 1 at q=7/13')
