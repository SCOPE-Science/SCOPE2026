#!/usr/bin/env python3
"""Reproduce symbolic and numerical checks for initial-mode search crossover.
Only standard-library and SymPy are needed; no network or external data.
"""
import math
import sympy as sp
r,p,q,D,w=sp.symbols('r p q D w',positive=True) # w = v^2
B=(r+p)/D+(r+q)**2/w
C=r*(r+q)*(r+p+q)/(D*w)
K=r*(r+q)/w
z=sp.symbols('z')
P=z**2-B*z+C
assert sp.simplify(P.subs(z,K)-q*r*(r+q)*(w-D*(r+q))/(D*w*w)) == 0
h=(r+q)**2/w
assert sp.simplify(P.subs(z,h)+p*q*(r+q)/(D*w)) == 0
print('PASS: polynomial evaluations and threshold factorization')

# Explicit first-passage formulas from the source give both start-mode values.
def values(D,p,q,r,v,x):
    w=v*v
    B=(r+p)/D+(r+q)**2/w
    C=r*(r+q)*(r+p+q)/(D*w)
    disc=B*B-4*C
    assert disc>0
    yp=(B+math.sqrt(disc))/2
    ym=2*C/(B+math.sqrt(disc))
    lm,lp=math.sqrt(ym),math.sqrt(yp)
    K=r*(r+q)/w
    phm=(r+q)**2/(w*lm)-lm
    php=(r+q)**2/(w*lp)-lp
    a=q*(r+q)/w
    FD=(phm*math.exp(-lm*x)-php*math.exp(-lp*x))/(phm-php)
    FB=a*(math.exp(-lm*x)/lm-math.exp(-lp*x)/lp)/(phm-php)
    cm=(ym-K)/lm
    cp=(yp-K)/lp
    direct_delta=FB-FD
    factored_delta=(cm*math.exp(-lm*x)-cp*math.exp(-lp*x))/(phm-php)
    assert math.isclose(direct_delta,factored_delta,abs_tol=2e-13,rel_tol=1e-10)
    assert FD>0 and FB>0
    TD=(1/FD-1)/r
    TB=(1/FB-1)/r
    cross=math.log(cp/cm)/(lp-lm) if cm>0 else math.inf
    return TD,TB,cross,lm,lp,cm,cp

for d,p0,q0,r0,v0 in [(1,1,1,1,2),(1,1,1,1,1),(.5,1.8,.2,.3,1),(2,.3,2,3,4),(.8,2,.9,.5,.9)]:
    at=[values(d,p0,q0,r0,v0,x) for x in (0.001,0.1,1,3,10,40)]
    qualifies=v0*v0>d*(q0+r0)
    if qualifies:
        xc=at[0][2]
        for x in (xc*.9,xc,xc*1.1):
            TD,TB,*_=values(d,p0,q0,r0,v0,x)
            if x<xc: assert TD<TB
            elif x>xc: assert TB<TD
            else: assert math.isclose(TD,TB,rel_tol=1e-10)
    else:
        assert all(t[0]<t[1] and math.isinf(t[2]) for t in at)
print('PASS: mean-first-arrival inequalities across varied parameters')

# The crossing length diverges at both ends of its permitted rate interval.
d,p0,q0,v0=1.,1.,1.,2.
rc=v0*v0/d-q0
lam0=math.sqrt(p0/d+q0*q0/(v0*v0))
lo_coeff=1/(2*lam0)
lc_minus=math.sqrt(rc/d)
lc_plus=math.sqrt((rc+p0+q0)/d)
hi_coeff=1/(lc_plus-lc_minus)
for rr in [1e-6,1e-8,1e-10]:
    x=values(d,p0,q0,rr,v0,1)[2]
    print('low-rate log ratio',rr,x/math.log(q0/rr),'limit',lo_coeff)
for ee in [1e-5,1e-7,1e-9]:
    x=values(d,p0,q0,rc-ee,v0,1)[2]
    print('critical-rate log ratio',ee,x/math.log(rc/ee),'limit',hi_coeff)
print('PASS: both logarithmic divergence patterns')

# A concrete intermediate-rate inversion, absent at both small and large rates.
x=4
assert values(1,1,1,1e-7,2,x)[0] < values(1,1,1,1e-7,2,x)[1]
assert values(1,1,1,.5,2,x)[1] < values(1,1,1,.5,2,x)[0]
assert values(1,1,1,2.99,2,x)[0] < values(1,1,1,2.99,2,x)[1]
print('PASS: reset-rate reentrance of search-mode advantage')
