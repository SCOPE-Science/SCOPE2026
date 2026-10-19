#!/usr/bin/env python3
"""Exact arithmetic checks for the quorum-protection edge equilibrium example.

Requires Python 3.9+ standard library only. Run: python verify_quorum.py
The analytic all-size bound is proved in RESULT.md, not by enumeration.
"""
from fractions import Fraction as F
from math import comb

N, M = 4, 2
n = N - 1
rho, omega = F(1, 5), F(3, 5)
r, c, k, L = F(16, 5), F(1), F(7, 100), F(1)
a = r * c / N - c

def failure(j):
    return 1 - rho ** j

def one_group_difference(m):
    """Subtract the original realized-group payoffs, not the gain formula."""
    j = n - m
    ps = r*c*(m + 1)/N - c - k - L*failure(j)*(1-omega*int(m+1 >= M))
    pd = r*c*m/N - L*failure(j+1)*(1-omega*int(m >= M))
    return ps-pd

def bernstein_gain(m):
    j=n-m
    return (a-k+L*(1-rho)*rho**j*(1-omega*int(m>=M))
            +L*omega*(1-rho**j)*int(m==M-1))

gains = [one_group_difference(m) for m in range(n+1)]
assert gains == [bernstein_gain(m) for m in range(n+1)]
assert gains == [F(-659,2500),F(169,500),F(-103,500),F(1,20)]

def B(z):
    return sum(comb(n,m)*gains[m]*z**m*(1-z)**(n-m) for m in range(n+1))

def P(z):
    return (4864*z**3-8592*z**2+4512*z-659)/2500

# Independent Bernstein expansion: coefficient of z^h.
monomial=[]
for h in range(n+1):
    monomial.append(sum(comb(n,m)*gains[m]*comb(n-m,h-m)*(-1)**(h-m)
                        for m in range(h+1)))
assert monomial == [F(-659,2500),F(4512,2500),F(-8592,2500),F(4864,2500)]
for q in [F(0),F(1,5),F(1,4),F(1,3),F(3,5),F(2,3),F(3,4),F(9,10),F(19,20),F(1)]:
    assert B(q)==P(q)

# Disjoint rational brackets for the three roots: no floating-point root count.
intervals=[(F(1,5),F(1,4)),(F(3,5),F(2,3)),(F(9,10),F(19,20))]
for lo,hi in intervals:
    assert B(lo)*B(hi)<0
assert [B(q)>0 for q in [F(0),F(1,3),F(2,3),F(1)]] == [False,True,False,True]

# For a boundary equilibrium, the transverse eigenvalue A = k - L*omega*Psi.
def psi(z):
    return comb(n,M-1)*z**(M-1)*(1-z)**(n-M+1)*(1-rho**(n-M+1))

def A_at_edge_root(z):
    return k-L*omega*psi(z)

# For z in the first bracket, z(1-z)^2 >= (1/5)(3/4)^2.
assert k - L*omega*F(72,25)*F(1,5)*F(3,4)**2 < 0
# For z in the middle bracket, z(1-z)^2 >= (3/5)(1/3)^2.
assert k - L*omega*F(72,25)*F(3,5)*F(1,3)**2 < 0
# For z in the last bracket, z(1-z)^2 <= (1)(1/10)^2.
assert k - L*omega*F(72,25)*F(1)*F(1,10)**2 > 0
# The D and C vertex invasion eigenvalues are both strictly negative.
A_D=a+L*(1-rho)*rho**n
A_C=a+L*(1-rho)
assert A_D<0 and A_D-k<0
assert -A_C<0 and -k<0

# The witness has exactly three simple roots in (0,1), because n=3.
# General N uses the two monotone coefficient blocks (proof in RESULT.md).
print('PASS: original conditional payoffs, gain coefficients, exact cubic,')
print('four alternating signs, three isolating brackets, vertex and transverse signs.')
print('gains:',[str(x) for x in gains])
print('B(0),B(1/3),B(2/3),B(1):',[str(B(q)) for q in [F(0),F(1,3),F(2,3),F(1)]])
print('A_D, A_C:',A_D,A_C)
