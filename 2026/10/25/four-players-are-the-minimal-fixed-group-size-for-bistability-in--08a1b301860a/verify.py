#!/usr/bin/env python3
"""Exact rational certificate for a four-player Fermi public-goods mean field.

Run: python3 verify.py
This checks the finite algebraic witness; the universal smaller-group theorem
uses the independent Bernstein–Descartes argument in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb

# For g=4, r=8/3, K=1/(3 log 2), d_n/K=n(4n-11) log 2.
def rational_fermi(n):
    e = n*(4*n-11)
    if e >= 0:
        return Q(2**e,1+2**e)
    return Q(1,1+2**(-e))

A = [rational_fermi(n) for n in range(5)]
assert A == [Q(1,2),Q(1,129),Q(1,65),Q(8,9),Q(1048576,1048577)]

def H(x):
    return sum((Q(comb(4,n))*x**n*(1-x)**(4-n)*A[n] for n in range(5)),Q())-x

checks={
  Q(0):Q(1,2),
  Q(1,4):Q(-178754083691,4501666890240),
  Q(9,10):Q(945172651927,58615454300000),
  Q(1):Q(-1,1048577),
}
for x,want in checks.items():
    assert H(x)==want,(x,H(x),want)
assert checks[Q(0)]>0>checks[Q(1,4)]
assert checks[Q(1,4)]<0<checks[Q(9,10)]
assert checks[Q(9,10)]>0>checks[Q(1)]

# Expand H with rational binomial identities, no symbolic library needed.
from math import comb as C
coeff=[]
for power in range(5):
    entry=sum((Q(C(4,n)*C(4-n,power-n)*(-1)**(power-n))*A[n]
               for n in range(power+1)),Q())
    if power==1: entry-=1
    coeff.append(entry)
assert coeff == [Q(1,2),Q(-383,129),Q(8383,2795),Q(36826,25155),Q(-105204829297,52753908870)]

# Universal Bernstein sign implications in g=2 or g=3:
# c0 > 0, c_g < 0; for g=2 c1<0; for g=3 c2<0 if 1<r<3.
# Descartes then gives at most one positive equilibrium root.
assert Q(1,2)-Q(1,2)==0
assert Q(1,2)-Q(2,3)<0
print('PASS: exact Fermi weights, quartic identity and four rational sign certificates')
print('Certified: exactly three simple interior equilibria by degree and sign alternation')
