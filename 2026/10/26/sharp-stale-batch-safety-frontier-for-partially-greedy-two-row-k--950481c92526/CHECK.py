"""Reproduce finite exact-arithmetic checks for the two-row stale-snapshot theorem.

Requires Python 3 standard library only. Finite tests supplement, not replace,
the proof of the universal parameter bound.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
import random

EXACT = 0
NUMERIC = 0

def dot(x, y):
    return sum(a*b for a,b in zip(x,y))

def expected_formula(k,theta,c,rr,beta):
    p=(1+theta)/2 if abs(rr)<1 else F(1,2)
    q=1-p
    A=p+q*rr*rr
    B=p*p+q*q*rr*rr+2*c*p*q*rr
    return -2*k*beta*A+k*beta*beta*(A+(k-1)*B)

for c,s in [(F(0),F(1)),(F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(15,17),F(8,17))]:
    assert c*c+s*s == 1
    u=(F(1),F(0)); w=(c,s)
    for theta in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
        for k in range(1,6):
            for rr in [F(0),F(1,3),F(2,3),F(1),F(-1,4)]:
                e=(F(1),(rr-c)/s)
                for beta in [F(1,4),F(1,2),F(1),F(3,2)]:
                    p = (1+theta)/2 if abs(rr)<1 else F(1,2)
                    q=1-p
                    delta=F(0)
                    for draws in product((0,1),repeat=k):
                        prob=F(1)
                        update=[F(0),F(0)]
                        for i in draws:
                            prob*=p if i==0 else q
                            vector=u if i==0 else w
                            residual=F(1) if i==0 else rr
                            for j in range(2):update[j]+=residual*vector[j]
                        new=[e[j]-beta*update[j] for j in range(2)]
                        delta+=prob*(dot(new,new)-dot(e,e))
                    assert delta==expected_formula(k,theta,c,rr,beta)
                    EXACT+=1

rng=random.Random(260708313)
for _ in range(4000):
    c=rng.random()*.999
    theta=rng.random()*.999
    k=rng.randint(1,40)
    S=sqrt(theta*theta+(1-theta*theta)*c*c)
    R=(1+S)/2
    cap=4/(k+1+(k-1)*S)
    if c>1e-7:
        t=(S-theta)/(c*(1-theta))
        assert -1e-8<=t<=1+1e-8
        p=(1+theta)/2; q=1-p
        A=p+q*t*t
        B=p*p+q*q*t*t+2*c*p*q*t
        assert abs(B/A-R)<1e-8
        for scale,desired in [(0.8,-1),(1.2,1)]:
            beta=scale*cap
            val=-2*k*beta*A+k*beta**2*(A+(k-1)*B)
            assert val*desired>0
    NUMERIC+=1

# Full greedy selection and two simultaneous unit-relaxed stale commits
# induce an orthogonal Householder reflection whenever the maximum is unique.
for _ in range(1000):
    c=rng.random()*.999
    s=sqrt(1-c*c)
    e=[rng.uniform(-3,3),rng.uniform(-3,3)]
    r1=e[0];r2=c*e[0]+s*e[1]
    if abs(abs(r1)-abs(r2))<1e-9:continue
    u=(1.,0.) if abs(r1)>abs(r2) else (c,s)
    r=dot(e,u)
    y=[e[j]-2*r*u[j] for j in range(2)]
    assert abs(dot(y,y)-dot(e,e))<1e-10*(1+dot(e,e))
    NUMERIC+=1
print('EXACT_EXPECTATION_IDENTITIES',EXACT)
print('NUMERICAL_SHARP_BOUNDARY_AND_REFLECTION_CHECKS',NUMERIC)
print('CHECKS_OK')
