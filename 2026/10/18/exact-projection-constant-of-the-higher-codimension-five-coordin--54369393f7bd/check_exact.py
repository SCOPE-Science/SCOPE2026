#!/usr/bin/env python3
"""Exact rational primal-dual certificate for a real maximum-norm projection."""
from fractions import Fraction as F

def vector(text):
    return [F(s) for s in text.split()]

u = vector('1 4/5 1/4 -1/4 -4/5')
v = vector('0 3/5 1 1 3/5')
a = vector('520/659 105/1318 110/659 -110/659 -105/1318')
b = vector('0 70/659 575/1318 575/1318 70/659')
rho = vector('104/659 315/1318 120/659 120/659 315/1318')
sigma = [vector(line) for line in (
    '1 1 1 -1 -1',
    '1 1 1 1 -257/315',
    '1 1 1 1 1',
    '-1 1 1 1 1',
    '-1 -257/315 1 1 1',
)]

def dot(x,y):
    return sum(p*q for p,q in zip(x,y))

assert dot(a,u)==1 and dot(a,v)==0
assert dot(b,u)==0 and dot(b,v)==1
Q = [[u[i]*a[j]+v[i]*b[j] for j in range(5)] for i in range(5)]
row_norms=[sum(map(abs,row)) for row in Q]
assert row_norms == [F(845,659)]*5
assert all(x>=0 for x in rho) and sum(rho)==1
assert all(abs(x)<=1 for row in sigma for x in row)
for j in range(5):
    assert sum(rho[i]*sigma[i][j]*u[i] for i in range(5)) == F(416,659)*u[j]
    assert sum(rho[i]*sigma[i][j]*v[i] for i in range(5)) == F(429,659)*v[j]
assert sum(rho[i]*sum(sigma[i][j]*Q[i][j] for j in range(5)) for i in range(5)) == F(845,659)
assert F(13,10)-F(845,659)==F(117,6590)
print('PASS exact rational primal-dual projection certificate; optimum 845/659')
