#!/usr/bin/env python3
"""Independent numerical checks of planar-rhombus radial laws.

Mathematical inputs and outputs only; all computations are reproducible.
"""
from __future__ import annotations
import math, random
from scipy.integrate import quad

SEED=8122026
rng=random.Random(SEED)


def exact_cdf(s,beta,r):
    if r<=0:return 0.0
    rmax=2*s*math.cos(beta)
    if r>=rmax:return 1.0
    sn=math.sin(2*beta)
    z=s*sn/r
    if z>=1:
        return beta*r*r/(s*s*sn)
    a=math.asin(z)
    start=max(0.,a-beta)
    end=min(beta,math.pi-a-beta)
    if end<=start:
        return beta*r*r/(s*s*sn)
    cota=1/math.tan(beta+start)
    cotb=1/math.tan(beta+end)
    outer=s*s*sn*sn*(cota-cotb)
    raw=beta*r*r-r*r*(end-start)+outer
    return raw/(s*s*sn)


def quadrature_cdf(s,beta,r):
    sn=math.sin(2*beta)
    def integrand(th):
        rho=s*sn/math.sin(beta+th)
        return min(r*r,rho*rho)
    return quad(integrand,0,beta,epsabs=2e-11,epsrel=2e-11,limit=120)[0]/(s*s*sn)


# Sample U,V correctly from independent coordinates.
def sample_independent(s,beta,N):
    cb=math.cos(beta);sb=math.sin(beta)
    out=[]
    for _ in range(N):
        u=rng.random();v=rng.random()
        out.append(s*math.hypot(cb*(u+v),sb*(u-v)))
    return out


def predicted_fourth(s,beta):
    c=math.cos(2*beta)
    return s**4*(28/45+c+4*c*c/9)

cases=[(3,math.pi*.315),(3,math.pi/4),(3,.60),(4,.68),(5,.40),(7,.24),(15,.1)]
max_quad=0
max_mc=0
max_second=0
max_fourth=0
for n,b in cases:
    assert 0<b<math.pi/n
    s=1.2+0.3*rng.random()
    rmax=2*s*math.cos(b)
    vals=sample_independent(s,b,120000)
    m2=sum(v*v for v in vals)/len(vals)
    m4=sum(v**4 for v in vals)/len(vals)
    p2=s*s*(2/3+0.5*math.cos(2*b))
    p4=predicted_fourth(s,b)
    max_second=max(max_second,abs(m2-p2)/p2)
    max_fourth=max(max_fourth,abs(m4-p4)/p4)
    checkpoints=[1e-5,.2,.4,.6,.85,.95,1.0]
    for t in checkpoints:
        r=t*rmax
        f1=exact_cdf(s,b,r)
        f2=quadrature_cdf(s,b,r)
        max_quad=max(max_quad,abs(f1-f2))
        fm=sum(v<=r for v in vals)/len(vals)
        max_mc=max(max_mc,abs(fm-f1))
        assert -1e-12<=f1<=1+1e-12,(n,b,r,f1)
    assert abs(exact_cdf(s,b,rmax)-1)<1e-12
    print(f'n={n:2d} beta={b:.7f} s={s:.6f} E2={p2:.9f} E4={p4:.9f} F(s)={exact_cdf(s,b,s):.9f}')
print('max_cdf_quadrature_absolute_residual:',max_quad)
print('max_cdf_monte_carlo_absolute_residual:',max_mc)
print('max_empirical_E2_relative_residual:',max_second)
print('max_empirical_E4_relative_residual:',max_fourth)
assert max_quad < 1e-9
assert max_mc < 0.009
assert max_second < 0.012
assert max_fourth < 0.02

# For non-isometric pairs or larger sets with matched beta, compare law exactly.
for beta in [.08,.17,.24]:
    admissible=[n for n in range(3,25) if beta<math.pi/n]
    assert len(admissible)>=5
    print('matching_angle',beta,'admissible_side_counts',admissible,
          'identical_p2',1*(2/3+math.cos(2*beta)/2))

# First-contact asymptotics using high-precision quadrature.
from mpmath import mp
mp.dps=65

def cdf_mp(beta,r):
    s=mp.mpf(1)
    beta=mp.mpf(beta);r=mp.mpf(r)
    sn=mp.sin(2*beta)
    rmax=2*mp.cos(beta)
    if r<=0:return mp.mpf(0)
    if r>=rmax:return mp.mpf(1)
    z=sn/r
    if z>=1: return beta*r*r/sn
    a=mp.asin(z)
    lo=max(mp.mpf(0),a-beta)
    hi=min(beta,mp.pi-a-beta)
    if hi<=lo:return beta*r*r/sn
    return (beta*r*r-r*r*(hi-lo)+sn*sn*(mp.cot(beta+lo)-mp.cot(beta+hi)))/sn

for fraction in [mp.mpf('0.20'),mp.mpf('0.25'),mp.mpf('0.30')]:
    b=mp.pi*fraction
    if b<mp.pi/4:
        r0=1
        expo=2
        coeff=1/mp.cos(2*b)
    elif b==mp.pi/4:
        r0=1
        expo=mp.mpf(3)/2
        coeff=4*mp.sqrt(2)/3
    else:
        r0=mp.sin(2*b)
        expo=mp.mpf(3)/2
        coeff=8*mp.sqrt(2)/(3*mp.sqrt(mp.sin(2*b)))
    delta=mp.mpf('1e-9')
    ffull=b*(r0+delta)**2/mp.sin(2*b)
    ratio=(ffull-cdf_mp(b,r0+delta))/delta**expo
    print('phase_beta_over_pi',mp.nstr(fraction,7),'predicted_coeff',mp.nstr(coeff,18),'observed',mp.nstr(ratio,18),'relative_err',mp.nstr(abs(ratio/coeff-1),8))
    assert abs(ratio/coeff-1)<mp.mpf('0.001')

for fraction in [mp.mpf('.20'),mp.mpf('.25'),mp.mpf('.30')]:
    b=mp.pi*fraction
    rm=2*mp.cos(b)
    d=mp.mpf('1e-7')
    observed=(1-cdf_mp(b,rm-d))/d**2
    theoretical=1/(2*mp.cos(b)**2)
    print('upper_tail_beta_over_pi',mp.nstr(fraction,8),'predicted',mp.nstr(theoretical,13),'actual',mp.nstr(observed,13))
    assert abs(observed/theoretical-1)<mp.mpf('0.00005')
print('ALL CHECKS PASS')
