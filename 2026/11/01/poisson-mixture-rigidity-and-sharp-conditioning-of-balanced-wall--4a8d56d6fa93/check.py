"""Exact and numerical checks for the balanced-wall cyclic spin Fourier theorem.
Run with Python 3.10+: python check.py. Only the standard library is used.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, pi, cos, isclose
from cmath import exp


def corr_hypergeometric(n, t):
    w = n // 2
    return Fraction(sum((-1)**j*comb(t,j)*comb(n-t,w-j)
                        for j in range(max(0,w-(n-t)),min(w,t)+1)), comb(n,w))


def corr_product(n,t):
    if t%2:
        return Fraction(0)
    a = Fraction(1)
    for j in range(1,t//2+1):
        a *= Fraction(-(2*j-1),n-(2*j-1))
    return a


def spin_rooted(n, wall_set):
    x=[1]*n
    for j in range(1,n):
        x[j] = -x[j-1] if j-1 in wall_set else x[j-1]
    return x


def spectrum(n,cs):
    return [sum(float(cs[t])*cos(2*pi*l*t/n) for t in range(n))
            for l in range(n)]

checks=0
for n in range(4,129,4):
    m=n//2
    cs=[corr_hypergeometric(n,t) for t in range(n)]
    assert cs == [corr_product(n,t) for t in range(n)];checks+=n
    eig=spectrum(n,cs)
    assert abs(eig[0]-n/(n+2))<2e-10
    assert abs(sum(eig)-n)<3e-9
    for j in range(0,n//4):
        assert eig[j+1]>eig[j]+1e-10,(n,j,eig[j:j+2])
    assert all(abs(eig[j]-eig[j+n//2])<3e-10 for j in range(n//2))
    assert all(abs(eig[j]-eig[n//2-j])<3e-10 for j in range(1,n//2))
    assert eig[0]>0
    a=lambda j: abs(corr_product(n,2*j))
    sharp=Fraction(1)+2*sum((a(j) for j in range(1,n//4)),Fraction(0))+a(n//4)
    assert abs(eig[n//4]-float(sharp))<3e-10
    checks+=5+n//4

# Complete spin-ensemble moment enumeration, distinct from the hypergeometric calculation.
for n in (4,8,12,16):
    w=n//2
    totals=[0]*n
    for edges in combinations(range(n),w):
        x=spin_rooted(n,set(edges))
        for t in range(n):
            totals[t]+=x[0]*x[t]
    denom=comb(n,w)
    assert all(Fraction(totals[t],denom)==corr_product(n,t) for t in range(n))
    checks+=denom*n

# For a few modes, independently compare the Poisson-beta integral by midpoint quadrature.
# The analytical integral identity and its monotonicity are proved in RESULT.md.
for n in (4,8,12,16,20):
    m=n//2
    # B(1/2,m+1/2)= pi*comb(2m,m)/4**m
    beta=pi*comb(2*m,m)/4**m
    cs=[corr_product(n,t) for t in range(n)]
    eig=spectrum(n,cs)
    steps=40000
    for ell in (0,1,n//4):
        theta=4*pi*ell/n
        v=0.0
        for j in range(steps):
            r=((j+0.5)/steps)**2  # r=u^2 removes endpoint integrable singularity
            weight=2*(1-r**m)*(1-r*r)/(1+r)**(m+1)
            v+=weight/(1+2*r*cos(theta)+r*r)
        v/=steps*beta
        assert abs(v-eig[ell])<1e-6,(n,ell,v,eig[ell])
        checks+=1

for n in (40,80,160,320):
    m=n//2
    cs=[corr_product(n,t) for t in range(n)]
    lam_max=sum(abs(cs[t]) for t in range(0,n,2))
    cond=float(lam_max)*Fraction(n+2,n)
    assert abs(n*(cond-1)-4)<19/n,(n,cond)
    checks+=1

print('PASS',checks,'assertion groups/weighted enumerated moments')
