#!/usr/bin/env python3
"""Independent finite arithmetic checks of exact identities and sample norms.

The universal classification is proved analytically in RESULT.md.
"""
from fractions import Fraction as F
import random
from math import sqrt

def norm4(z):
    return (abs(z[0])**4+abs(z[1])**4)**.25

def defect(z, a, b):
    return sqrt(max(0.0, norm4(z)**2-norm4((a*z[0],b*z[1]))**2))

def exact_substitution_identity(a,b,t):
    u=a*a; v=b*b; h=t**4
    q2=(u*u+v*v*h)/(1+h)
    assert (u*u-q2)*(q2-v*v)== h*(u*u-v*v)**2/(1+h)**2

rng=random.Random(20261019)
checks=0
for ia in range(1,10):
    a=F(ia,10)
    for ib in range(1,ia+1):
        b=F(ib,10)
        for k in range(1,30):
            exact_substitution_identity(a,b,F(k,17)); checks+=1
for a,b in [(0.9,0.85),(0.9,0.81),(0.6,0.40),(0.4,0.2),(0.8,0.8),(0.0,0.0)]:
    assert b+1e-12>=a*a
    for k in range(1000):
        x=(complex(rng.uniform(-2,2),rng.uniform(-2,2)),complex(rng.uniform(-2,2),rng.uniform(-2,2)))
        y=(complex(rng.uniform(-2,2),rng.uniform(-2,2)),complex(rng.uniform(-2,2),rng.uniform(-2,2)))
        assert defect((x[0]+y[0],x[1]+y[1]),a,b)<=defect(x,a,b)+defect(y,a,b)+1e-9
        checks+=1
for a,b in [(0.9,0.80),(0.7,0.4),(0.4,0.0)]:
    assert b<a*a
    t=0.01
    assert defect((t,1),a,b)<defect((0,1),a,b)
    checks+=1
print('finite arithmetic and sample checks passed:',checks)
