#!/usr/bin/env python3
"""Exact checks for the cubic Pell even-window GCD formula, no dependencies."""
from math import gcd

NMAX = 120
P, Q = [0,1], [1,1]
for n in range(1, 3*NMAX+30):
    P.append(2*P[-1]+P[-2])
    Q.append(2*Q[-1]+Q[-2])

def sums(m):
    return [sum(P[n+j]**3 for j in range(1,2*m+1)) for n in range(4)]

assert [(P[n] % 8) for n in range(8)] == [0,1,2,5,4,5,6,1]
assert [(Q[n] % 16) for n in range(8)] == [1,1,3,7,1,9,3,15]
assert all(P[n+8] % 8 == P[n] % 8 for n in range(20))
assert all(Q[n+8] % 16 == Q[n] % 16 for n in range(20))

for m in range(1, NMAX+1):
    p,q = P[m],Q[m]
    assert q*q-2*p*p == (-1)**m
    ss = sums(m)
    # Since the characteristic polynomial has unit constant coefficient,
    # four consecutive windows generate the full infinite-window gcd.
    g=0
    for s in ss: g=gcd(g,s)
    if m%2:
        target=q//gcd(q,7)
        B=(4*q*q+3)*(P[3*m+3]+P[3*m])-21*q
        assert 56*ss[0] == q*B
    else:
        target=p*(3 if m%4==0 else 1)//gcd(p,7)
        B=(4*q*q-1)*(Q[3*m+3]+Q[3*m])-42*p
        assert 56*ss[0] == p*B
        assert B % 16 == 8
    assert g == target, (m,g,target)
    prior=sum(P[j]**3 for j in range(2*m))
    assert prior == 12*ss[2]+30*ss[1]-12*ss[0]-ss[3]
    assert gcd(gcd(P[2*m]**3,P[2*m+1]**3-1),g) == g
print('PASS: all even windows 2m for 1 <= m <=',NMAX)
print('PASS: initial sums, Pell norms, reversible recurrence and mod-16 certificate')
