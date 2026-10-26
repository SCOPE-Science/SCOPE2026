"""Exact arithmetic checks for a quorum-protection D/S replicator edge.

Run using Python 3.9+: python verify.py
This checks finite examples and exact identities; it does not replace the
Bernstein sign-variation proof for arbitrary group size.
"""
from fractions import Fraction as Q
from math import comb
from itertools import product


def bernstein_b(n, m, rho, omega):
    d = 1-rho
    return [rho**(n-j) if j <= m-2 else
            rho**(n-m+1)+omega*(1-rho**(n-m+1))/d if j == m-1 else
            (1-omega)*rho**(n-j) for j in range(n+1)]


def binom_expected(vals, z):
    n=len(vals)-1
    return sum((Q(comb(n,j))*vals[j]*z**j*(1-z)**(n-j)
                for j in range(n+1)),Q(0))


def raw_diff(n, m, rho, omega, z, r, c, k, loss):
    N=n+1
    def pd(j):
        prot = 1-omega if j >= m else Q(1)
        return r*c*j/N-loss*(1-rho**(n-j+1))*prot
    def ps(j):
        prot = 1-omega if j+1 >= m else Q(1)
        return r*c*(j+1)/N-c-k-loss*(1-rho**(n-j))*prot
    return sum((Q(comb(n,j))*z**j*(1-z)**(n-j)*(ps(j)-pd(j))
                for j in range(n+1)),Q(0))


def derived_diff(n,m,rho,omega,z,r,c,k,loss):
    a = r*c/(n+1)-c
    return loss*(1-rho)*binom_expected(bernstein_b(n,m,rho,omega),z)+a-k


def variations(seq):
    signs=[1 if v>0 else -1 for v in seq if v]
    return sum(x!=y for x,y in zip(signs,signs[1:]))


checks=0
for n,m,rho,omega,z in product(
    range(2,10),range(2,10),
    [Q(1,5),Q(1,2),Q(4,5)],
    [Q(0),Q(1,3),Q(1,2),Q(1)],
    [Q(0),Q(1,9),Q(1,2),Q(3,5),Q(1)]):
    if m>n: continue
    r,c,k,loss=Q(3,2),Q(1),Q(9,50),Q(5,2)
    assert raw_diff(n,m,rho,omega,z,r,c,k,loss)==derived_diff(n,m,rho,omega,z,r,c,k,loss)
    b=bernstein_b(n,m,rho,omega)
    assert all(b[i+1]>b[i] for i in range(0,m-1))
    assert all(b[i+1]>=b[i] for i in range(m,n))
    diff=[b[i+1]-b[i] for i in range(n)]
    assert variations(diff)<=2
    for h in [Q(0),Q(1,10),Q(1,3),Q(3,4),Q(2)]:
        assert variations([x-h for x in b])<=3
    checks+=1

n,m,rho,omega=3,2,Q(1,5),Q(1,2)
r,c,k,loss=Q(2),Q(1),Q(9,50),Q(5,2)
a=r*c/(n+1)-c
assert a==-Q(1,2)
assert bernstein_b(n,m,rho,omega)==[Q(1,125),Q(16,25),Q(1,10),Q(1,2)]
assert (k-a)/(loss*(1-rho))==Q(17,50)
assert [derived_diff(n,m,rho,omega,z,r,c,k,loss) for z in
        [Q(0),Q(1,2),Q(3,5),Q(3,4)]] == \
        [-Q(83,125),Q(1,500),-Q(124,15625),Q(13,2000)]
# Confirm polynomial coefficients by four exact interpolation nodes.
for z in [Q(0),Q(1,11),Q(1,2),Q(3,5),Q(3,4),Q(1)]:
    expected=(528*z**3-879*z**2+474*z-83)/125
    assert derived_diff(n,m,rho,omega,z,r,c,k,loss)==expected
    checks+=1
# A=P_C-P_D is negative throughout [1/2,3/5]:
# At the middle fixed point, B crosses down, and the transverse eigenvalue
# x*(P_C-avg payoff) equals A because P_D=P_S on this edge.
for z in [Q(1,2),Q(11,20),Q(3,5)]:
    psi=Q(72,25)*z*(1-z)**2
    assert k-loss*omega*psi<0
    checks+=1
print(f"PASS: {checks} exact checks; 3 simple D/S roots in disjoint rational intervals")
