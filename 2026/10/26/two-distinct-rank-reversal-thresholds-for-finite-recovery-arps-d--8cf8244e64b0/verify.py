"""Reproducible finite checks for sharp rank reversals of two Arps curves.

Uses mpmath and sympy. These checks supplement, not replace, analytic proof.
"""
from __future__ import annotations
import random
import math
import mpmath as mp
import sympy as sp

mp.mp.dps = 55
z = sp.symbols('z', positive=True)
Gz = (z**3 + 2) / (z*(z**2+z+1))
assert sp.simplify(sp.diff(Gz,z) -
    (z**4+2*z**3-6*z**2-4*z-2)/(z**2*(z**2+z+1)**2)) == 0
# Unique positive root follows from the one-sign-change criterion and a sign switch.
P=z**4+2*z**3-6*z**2-4*z-2
assert P.subs(z,1)<0 and sp.LC(sp.Poly(P,z))>0
zz=mp.findroot(lambda u:u**4+2*u**3-6*u*u-4*u-2, (2, 3))
tC=mp.mpf(2)/3*(zz**3-1)

def f(t,b,D):return (1+b*D*t)**(-1/b)
def F(t,b,D):return -mp.expm1((1-1/b)*mp.log1p(b*D*t))/(D*(1-b))

def k(t,b1,b2,D1,D2): return f(t,b2,D2)/f(t,b1,D1)
def G(t,b1,b2,D1,D2): return F(t,b2,D2)/F(t,b1,D1)

b1=mp.mpf('0.5');b2=mp.mpf('0.75');D1=mp.mpf(1);D2=mp.mpf(2)
rr=k(2,b1,b2,D1,D2)
rc=G(tC,b1,b2,D1,D2)
assert abs(rr-mp.power(4,-mp.mpf(1)/3))<mp.mpf('1e-48')
assert mp.mpf('.71395')<rc<mp.mpf('.71397')
assert mp.mpf('.62996')<rr<mp.mpf('.62997')
assert 2*mp.power(4,-mp.mpf(1)/3)-mp.mpf(6)/5>0
r=mp.mpf(4)/5
rate_roots=[mp.findroot(lambda t:k(t,b1,b2,D1,D2)-r,ab)
            for ab in [(mp.mpf('.1'),mp.mpf('1')),(mp.mpf('7'),mp.mpf('9'))]]
volume_roots=[mp.findroot(lambda t:G(t,b1,b2,D1,D2)-r,ab)
            for ab in [(mp.mpf('.5'),mp.mpf('1.5')),(mp.mpf(50),mp.mpf(60))]]
assert rate_roots[0]<volume_roots[0]<rate_roots[1]<volume_roots[1]
expected=(mp.mpf('.31443330123343574424'),mp.mpf('.88552899899568682502'),
          mp.mpf('7.52685606701330204'),mp.mpf('55.82675518990436'))
for a,ex in zip((rate_roots[0],volume_roots[0],rate_roots[1],volume_roots[1]),expected):
    assert abs(a-ex)<mp.mpf('1e-12')
print('Exact shape reduction and high-precision witness: PASS')
print('rate threshold', mp.nstr(rr,25),'cum threshold',mp.nstr(rc,25))
print('crossings',*[mp.nstr(x,22) for x in (rate_roots[0],volume_roots[0],rate_roots[1],volume_roots[1])])

# Seeded generic tests of the monotonicity-derived finite phase diagram.
rng=random.Random(451945)
for i in range(160):
    b_lo=rng.uniform(.06,.55)
    b_hi=rng.uniform(b_lo+.02,.97)
    d_lo=rng.uniform(.15,2.)
    d_hi=rng.uniform(d_lo*1.06,d_lo*4.5)
    B1,B2,D1p,D2p=map(mp.mpf,map(str,(b_lo,b_hi,d_lo,d_hi)))
    tR=(D2p-D1p)/(D1p*D2p*(B2-B1))
    rho=D1p*(1-B1)/(D2p*(1-B2))
    t0=max(tR,mp.mpf('1e-9'))
    # H(t) increases strictly above tR. Geometric bracketing of its unique zero.
    def h(t):return F(t,B1,D1p)*k(t,B1,B2,D1p,D2p)-F(t,B2,D2p)
    left=t0;right=t0*2
    assert h(left)<0
    for j in range(300):
        if h(right)>0:break
        right*=2
    else:raise AssertionError('Unable to bracket unique cumulative minimum')
    for j in range(48):
        mid=(left+right)/2
        if h(mid)>0:right=mid
        else:left=mid
    tc=(left+right)/2
    rrate=k(tR,B1,B2,D1p,D2p)
    rcum=G(tc,B1,B2,D1p,D2p)
    rmax=min(mp.mpf(1),rho)
    assert mp.mpf(0)<rrate<rcum<rmax
    # Check sampled monotonic signs; derived analytically in RESULT.md.
    assert k(tR/2,B1,B2,D1p,D2p)>rrate and k(tR*2,B1,B2,D1p,D2p)>rrate
    assert G(tc/2,B1,B2,D1p,D2p)>rcum and G(tc*2,B1,B2,D1p,D2p)>rcum
    # Representative r on either side of the distinct second threshold.
    rmid=(rrate+rcum)/2
    assert rmid<rcum
    rval=(rcum+rmax)/2
    assert rval<rmax
print('160 seeded parameter threshold checks: PASS')
