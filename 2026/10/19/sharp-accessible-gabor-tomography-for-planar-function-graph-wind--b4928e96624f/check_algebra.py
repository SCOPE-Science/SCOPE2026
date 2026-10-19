#!/usr/bin/env python3
"""Exact symbolic polynomial cross-checks of the planar-graph mass lemma.
Uses only integer arithmetic in Z[q,z]; finite tests do not establish positivity.
"""
from collections import defaultdict

def add(*ps):
    out=defaultdict(int)
    for p in ps:
        for k,v in p.items():out[k]+=v
    return {k:v for k,v in out.items() if v}

def mul(a,b):
    out=defaultdict(int)
    for (qa,za),av in a.items():
        for (qb,zb),bv in b.items():out[(qa+qb,za+zb)]+=av*bv
    return {k:v for k,v in out.items() if v}

def scale(a,n):return {k:n*v for k,v in a.items() if n*v}

def sub(a,b):return add(a,scale(b,-1))
def sq(a):return mul(a,a)
def cube(a):return mul(a,sq(a))
ONE={(0,0):1}; Q={(1,0):1}; Z={(0,1):1}
U=add(Q,ONE)
# P(z)=z^2-(q+1)z+q-1, and B_q(z) as in the result.
P=add(sq(Z),scale(mul(U,Z),-1),Q,scale(ONE,-1))
B=add(scale(cube(Z),2),scale(mul(Q,sq(Z)),-2),
      mul(add(sq(Q),Q,scale(ONE,-6)),Z),
      scale(sq(Q),-1),scale(Q,3),scale(ONE,-2))
# Clear the denominator z^2(q+1)^2 of the probability lemma deficit.
LHS=add(sq(sq(Z)),Q,scale(ONE,-2),
        sq(sub(sub(mul(U,Z),sq(Z)),sub(Q,scale(ONE,2)))),
        scale(mul(add(Q,scale(ONE,3)),sq(Z)),-1))
RHS=mul(sub(Z,ONE),B)
assert LHS==RHS,('factorization',sub(LHS,RHS))
REMAINDER=mul(sub(Q,ONE),sub(mul(add(Q,scale(ONE,2)),Z),Q))
assert B==add(mul(scale(add(Z,ONE),2),P),REMAINDER), 'quadratic remainder'
print('VERIFY_OK exact_polynomial_identities=2 ring=Z[q,z]')
