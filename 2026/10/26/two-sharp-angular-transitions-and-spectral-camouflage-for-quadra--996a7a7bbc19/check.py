#!/usr/bin/env python3
"""Independent finite-dimensional checks for quadratic radial concentration on balls.
Dependencies: Python 3, numpy, sympy, mpmath (see VERIFICATION.md).
"""
from fractions import Fraction as F
from math import factorial, sqrt
import random
import numpy as np
import sympy as sp
import mpmath as mp

checks=0
def assertcheck(cond,label):
    global checks
    if not cond: raise AssertionError(label)
    checks+=1


def moments(a, intervals):
    return [sum((F(a,a+k)*(v**(a+k)-u**(a+k)) for u,v in intervals),F(0)) for k in range(3)]

def eigs_rad(a,b):
    mu=a/(a+1); nu=a/(a+2)
    M=np.array([[1.,float(mu)],[float(mu),float(nu)]])
    B=np.array([[float(b[0]),float(b[1])],[float(b[1]),float(b[2])]])
    L=np.linalg.cholesky(M)
    V=np.linalg.eigvalsh(np.linalg.solve(L,np.linalg.solve(L,B.T).T))
    return V

# Exact sector decoupling and diagonal dominance, for varied masks.
rng=random.Random(16602026)
for dim in (2,4,6,8,12):
    a=dim//2; mu=F(a,a+1); nu=F(a,a+2); tau=nu/mu
    for _ in range(160):
        ts=sorted([F(rng.randint(1,999),1000) for j in range(4)])
        if len(set(ts))<4: continue
        intervals=((ts[0],ts[1]),(ts[2],ts[3]))
        b=moments(a,intervals)
        assertcheck(b[1]-(b[1]/mu)*mu==0,"offdiagonal vanish")
        lam1=b[1]/mu; lam2=b[2]/nu
        assertcheck((b[2]-lam1*nu)==nu*(lam2-lam1),"sector relation")
        vals=eigs_rad(a,b)
        linear_wins=(b[1]/b[0]>=mu and b[2]/b[1]<=tau)
        assertcheck((lam1>=vals[1]-1e-9) == linear_wins,"phase equivalence")
        assertcheck(vals[1]>=float(lam2)-1e-9,"radial dominance over quadrupole")

# Direct full two-dimensional polynomial Gram reconstruction, independent
# of the O(d) invariant-block calculation.
mons=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
def disk_monomial_moment(px,py,intervals):
    if px%2 or py%2:return F(0)
    i,j=px//2,py//2;k=i+j
    base=F(factorial(2*i)*factorial(2*j),4**k*factorial(i)*factorial(j)*factorial(k+1))
    return base*sum((v**(k+1)-u**(k+1) for u,v in intervals),F(0))

M=np.array([[float(disk_monomial_moment(x[0]+y[0],x[1]+y[1],((F(0),F(1)),))) for x in mons] for y in mons])
L=np.linalg.cholesky(M)
for intervals in [((F(1,3),F(2,3)),),((F(1,5),F(2,5)),(F(3,5),F(4,5))),((F(7,10),F(9,10)),)]:
    B=np.array([[float(disk_monomial_moment(x[0]+y[0],x[1]+y[1],intervals)) for x in mons] for y in mons])
    T=np.linalg.solve(L,np.linalg.solve(L,B.T).T)
    observed=np.linalg.eigvalsh(T)
    b=moments(1,intervals); vr=eigs_rad(1,b)
    expected=np.sort(np.array([vr[0],vr[1],float(b[1]/F(1,2)),float(b[1]/F(1,2)),float(b[2]/F(1,3)),float(b[2]/F(1,3))]))
    assertcheck(np.max(np.abs(observed-expected))<2e-12,"direct Gram spectrum")

# Exact radical two-annulus camouflage on a disk: b_k=m_k/2, k=0,1,2.
s2=sp.sqrt(2)
lo=(1-1/s2)/2;hi=(1+1/s2)/2
for k in (0,1,2):
    bk=sp.simplify(lo**(k+1)/(k+1)+(hi**(k+1)-sp.Rational(1,2)**(k+1))/(k+1))
    assertcheck(sp.simplify(bk-sp.Rational(1,2)/(k+1))==0,"camouflage exact moment")

# Thin-shell crossing roots and expansions with high precision, outside
# the exact-rational tests above.
mp.mp.dps=65
for dim in (2,3,4,5,8,12):
    aa=mp.mpf(dim)/2; mu=aa/(aa+1); tau=(aa+1)/(aa+2)
    for e_string in ('0.01','0.003','0.001'):
        ep=mp.mpf(e_string)
        def b(k,z):return aa/(aa+k)*((z+ep)**(aa+k)-(z-ep)**(aa+k))
        z1=mp.findroot(lambda z:b(1,z)/b(0,z)-mu,mu)
        z2=mp.findroot(lambda z:b(2,z)/b(1,z)-tau,tau)
        assertcheck(z1<z2,"two separated crossings")
        p1=mu-(aa-1)*ep**2/(3*mu);p2=tau-aa*ep**2/(3*tau)
        assertcheck(abs(z1-p1)<3*ep**4,"lower crossing expansion")
        assertcheck(abs(z2-p2)<3*ep**4,"upper crossing expansion")
        z=(z1+z2)/2
        assertcheck(b(1,z)/b(0,z)>mu and b(2,z)/b(1,z)<tau,"linear phase")
        for z in (z1-ep/2,z2+ep/2):
            assertcheck(not (b(1,z)/b(0,z)>mu and b(2,z)/b(1,z)<tau),"radial flanking phase")

print(f"PASS: {checks} assertions; exact moments, direct Gram matrices, mask phase, thin-shell roots")
