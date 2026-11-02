"""Reproducible exact and numerical tests for the one-hub sampling theorem.

Requires Python 3, numpy, sympy. The general theorem is proved in RESULT.md;
finite tests are only consistency and regression checks.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp

COUNT = 0

def check(condition, explanation='check failed'):
    global COUNT
    assert bool(condition), explanation
    COUNT += 1

m,a,b,t,p,L=sp.symbols('m a b t p L', real=True)
c=1+(m-1)*b
alpha=c/m
Delta=alpha-a*a
pr=sp.cancel((alpha+a)/(1+alpha+2*a))
lr=sp.cancel(Delta/(1+alpha+2*a))
F=sp.expand(Delta*p*(1-p)-L*(alpha+(1-alpha)*p)+L*L)
check(sp.factor(F.subs(L, lr)+Delta*(p-pr)**2)==0, 'radial square identity')
tr=sp.symbols('tr', positive=True)
check(sp.factor((tr-(1-b))*(c-(1-b))-m*a*a*tr-m*(tr*(b-a*a)-b*(1-b)))==0,
      'leaf-radial crossing identity')
check(sp.factor(((c+m*a)*(b-a*a)-b*(1-b)*(1+a))-(a+b)*(m*(b-a*a)-a*(1-b)))==0,
      'branch-switch identity')


def analytic(mv,av,bv):
    cv=1+(mv-1)*bv
    assert mv>=2 and av>0 and -1/(mv-1)<bv<1 and mv*av*av<cv
    t0=(cv+mv*av)/(1+av)
    t1=bv*(1-bv)/(bv-av*av) if bv>av*av else math.inf
    tx=min(t0,t1)
    hh=tx/(mv+tx)
    ll=(cv-mv*av*av)/(mv+cv+2*mv*av) if t0<=t1 else (1-bv)/(mv+tx)
    return hh,ll,tx,t0,t1


def smallest(mv,av,bv,pv):
    cv=1+(mv-1)*bv
    qv=(1-pv)/mv
    M=np.array([[pv,av*np.sqrt(mv*pv*qv)],[av*np.sqrt(mv*pv*qv),cv*qv]])
    return min(float(np.linalg.eigvalsh(M)[0]),float(qv*(1-bv)))

rng=np.random.default_rng(20261028)
branches=set()
for mv in range(3,17):
    for bv in [-1/(2*(mv-1)),0.,1/8,1/3,2/3,7/8]:
        cv=1+(mv-1)*bv
        for av in [0.015,0.055,0.105,0.19,0.29,0.41,0.57,0.75]:
            if mv*av*av>=cv: continue
            hh,ll,tx,t0,t1=analytic(mv,av,bv)
            branches.add('radial' if t0<=t1 else 'leaf')
            check(0<hh<1 and ll>0, 'strict interior')
            check(abs(smallest(mv,av,bv,hh)-ll)<1e-11,'spectral optimum')
            qv=(1-hh)/mv
            G=np.full((mv+1,mv+1),bv)
            np.fill_diagonal(G,1.)
            G[0,1:]=av
            G[1:,0]=av
            pw=np.array([hh]+[qv]*mv)
            eigs=np.linalg.eigvalsh(np.sqrt(pw)[:,None]*G*np.sqrt(pw)[None,:])
            check(abs(float(eigs[0])-ll)<3e-11,'full Gram spectrum')
            # Strict nonoptimality of distinct probabilities: random interior simplex.
            for j in range(6):
                pv=rng.dirichlet(np.ones(mv+1))
                lamb=np.linalg.eigvalsh(np.sqrt(pv)[:,None]*G*np.sqrt(pv)[None,:])[0]
                check(lamb<=ll+2e-11, 'arbitrary probabilities comparison')
            for hp in [0.,1e-5,0.04,0.15,0.35,0.65,0.87,.99999,1.]:
                check(smallest(mv,av,bv,hp)<=ll+2e-11, 'symmetric global comparison')
check(branches=={'radial','leaf'},'both branches tested')

# Rational exact phase boundary: m=3, a=1/4, b=7/52.
mv=3; av=Fraction(1,4); bv=Fraction(7,52)
cv=1+(mv-1)*bv
t0=(cv+mv*av)/(1+av)
t1=bv*(1-bv)/(bv-av*av)
check(t0==t1, 'exact regime boundary')
check(mv*av*av<cv, 'boundary is SPD')

# Rational multi-size asymptotic fixed-t regime (a=1/5, b=1/3).
a0=Fraction(1,5); b0=Fraction(1,3)
fixed=b0*(1-b0)/(b0-a0*a0)
for mv in [3,4,5,10,20,40,80,160]:
    cv=1+(mv-1)*b0
    check(mv*a0*a0<cv,'asymptotic positive definiteness')
    h,l,tx,t0,t1=analytic(mv,float(a0),float(b0))
    if mv*(b0-a0*a0)>=a0*(1-b0):
        check(abs(tx-float(fixed))<1e-12,'dimension-independent scale')

print(f'PASS: {COUNT} assertions; both spectral branches and exact phase boundary covered.')
