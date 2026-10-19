#!/usr/bin/env python3
"""Finite consistency tests for a sharp two-harmonic torus-map criterion.

The universal proof is analytic; these tests validate its algebraic formulas,
representative critical Jacobians, and finite-step inequalities.
"""
import math
import random
from fractions import Fraction

TESTS = 0

def check(ok, label='consistency'):
    global TESTS
    if not ok:
        raise AssertionError(label)
    TESTS += 1


def q2_exact(c):
    c = Fraction(c)
    return Fraction(1) if 6*c <= 1 else 4*(1+3*c)**3/(81*c)


def q(c):
    return math.sqrt(float(q2_exact(c)))


def g(s,c):
    v=math.sin(s)
    return v*(1+c*v*v)


def gp(s,c):
    v=math.sin(s)
    return math.cos(s)*(1+3*c*v*v)


def potential(s,c):
    v=math.cos(s)
    return (1+c)*v-c*v*v*v/3


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def mv(A,v):
    return [dot(row,v) for row in A]


CVALS=[Fraction(0),Fraction(1,10),Fraction(1,6),Fraction(1,5),
       Fraction(1,3),Fraction(1),Fraction(2),Fraction(25)]

for cf in CVALS:
    c=float(cf)
    qc=q(cf)
    # The squared exact maximum, and the maximizer of u(1+3c-3cu^2).
    u2=Fraction(1) if 6*cf<=1 else (1+3*cf)/(9*cf)
    u=math.sqrt(float(u2))
    peak=u*(1+3*c*(1-u*u))
    check(abs(peak-qc)<2e-13,'closed-form maximum')
    check(q2_exact(cf)>=1,'q^2 lower bound')
    if 6*cf>1:
        check(0<u<1,'interior maximizer')
        check(abs(1+3*c-9*c*u*u)<1e-12,'stationarity')
        s=math.acos(-u)
        check(abs(gp(s,c)+qc)<2e-12,'two interior minima')
        check(abs(gp(2*math.pi-s,c)+qc)<2e-12,'reflection minimum')
        check(qc>1,'sink regular at critical parameter')
    else:
        check(abs(gp(math.pi,c)+qc)<2e-12,'unique minimum at pi')
    for k in range(801):
        s=2*math.pi*k/801
        v=gp(s,c)
        check(abs(v)<=qc+2e-12,'global derivative bound')
        check(v*math.cos(s)>=-2e-12,'derivative sign')
        check(abs(g(s,c))<=1+c+2e-12,'unimodal amplitude')
        check(abs((potential(s+1e-6,c)-potential(s-1e-6,c))/(2e-6)+g(s,c))<1e-8,'potential derivative')

# Exact rational witness for cubic harmonic: c=1, u=2/3, q=16/9,
# hcrit=9/64. At all eight interior singular points the 3x3 Jacobian
# is (3/4)I-(1/4)J, with eigenvalues 0,3/4,3/4.
c=Fraction(1); u=Fraction(2,3); qexact=Fraction(16,9)
check(u*(1+3*c*(1-u*u))==qexact,'exact cubic harmonic min')
h=Fraction(9,64)
check(4*h*qexact==1,'exact critical step')
J=[[int(i==j) - h*qexact*(2 if i==j else 1) for j in range(3)] for i in range(3)]
check(J[0]==[Fraction(1,2),Fraction(-1,4),Fraction(-1,4)],'critical matrix row')
check(all(sum(row)==0 for row in J),'critical zero mode')
check(all(sum(J[i][j]*v[j] for j in range(3))==Fraction(3,4)*v[i]
          for v in ((1,-1,0),(1,0,-1)) for i in range(3)),'other two eigenvalues')
check(1-4*h>0,'critical sink remains hyperbolic')

# At c=1/6, g'(pi+t)=-1+(3/8)t^4+O(t^6).
for eps in [1e-1,5e-2,1e-2,5e-3]:
    x=(gp(math.pi+eps,1/6)+1)/(eps**4)
    check(abs(x-3/8)<2*eps**2,'quartic critical contact')

# Direct finite-step numerical inequalities for SPD weakly diagonal
# dominant path and three-leaf star incidence matrices.
K2=[[2,-1],[-1,2]]
K3=[[2,1,1],[1,2,1],[1,1,2]]
rng=random.Random(13579)
for K,lam in ((K2,3.0),(K3,4.0)):
    n=len(K)
    for cf in CVALS:
        c=float(cf)
        step=.91/(lam*q(cf))
        for iteration in range(340):
            z=[rng.random()*2*math.pi for _ in range(n)]
            v=[g(s,c) for s in z]
            kv=mv(K,v)
            new=[z[i]+step*kv[i] for i in range(n)]
            oldV=sum(potential(s,c) for s in z)
            newV=sum(potential(s,c) for s in new)
            bound=-step*(1-.5*step*lam*q(cf))*dot(v,kv)
            check(newV-oldV <= bound + 2e-12,'Lyapunov descent bound')
            for i in range(n):
                if math.pi/2+1e-12<z[i]<3*math.pi/2-1e-12:
                    check(math.pi/2-2e-12<=new[i]<=3*math.pi/2+2e-12,'forward slab')

print('VERIFY_OK',TESTS)
