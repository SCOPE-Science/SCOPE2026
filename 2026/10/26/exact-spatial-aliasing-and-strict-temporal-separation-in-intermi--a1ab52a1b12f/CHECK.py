#!/usr/bin/env python3
"""Exact algebra and independent Markov-generator checks for an intermittent search process."""
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm

checks=0
def eq(a,b):
    global checks
    checks+=1
    assert sp.simplify(a-b)==0, str(sp.factor(a-b))
def near(a,b,rtol=2e-11,atol=2e-11):
    global checks
    checks+=1
    assert abs(a-b)<=atol+rtol*abs(b),(a,b)

a,b,r,d,v,k=sp.symbols('a b r d v k',positive=True,real=True)
L=b+r;S=a+b+r
Q=(d*k*k+a+r)*(L*L+v*v*k*k)-a*b*L
PD=r*(L*S+v*v*k*k)/Q
PB=r*L*(S+d*k*k)/Q
EQ=r/(r+d*k*k)
eq(PD-PB,r*k*k*(v*v-d*L)/Q)
eq(sp.factor(PD.subs(v*v,d*L)),EQ) if False else None
# Substitute squared v through an independent positive symbol, because SymPy does not reduce all v^2 substitutions after expanding.
for f in (PD,PB):
    eq(sp.factor(f.subs(v,sp.sqrt(d*L))),EQ)
eq(sp.simplify(-sp.diff(PD,k,2).subs(k,0)+sp.diff(PB,k,2).subs(k,0)), 2*(d-v*v/L)/S)
# Partial normalization and mode probabilities follow from generator.

def check(a0,b0,r0,d0,v0,times):
    global checks
    rates=np.array([[-a0,a0/2,a0/2], [b0,-b0,0], [b0,0,-b0]],float)
    # State probabilities at reset, delta_D or symmetric delta_V.
    for mode,reset_probs,piB in [('D',np.array([1.,0.,0.]),a0/(a0+b0+r0)),('V',np.array([0.,.5,.5]),(a0+r0)/(a0+b0+r0))]:
        state_Q=rates+r0*(np.tile(reset_probs,(3,1))-np.eye(3))
        p=np.linalg.solve(np.vstack([state_Q.T[:2],np.ones(3)]),np.array([0.,0.,1.]))
        near(sum(p),1.)
        near(p[1]+p[2],piB)
        A=rates.T-r0*np.eye(3)
        dr=np.array([0.,v0,-v0])
        m1=np.linalg.solve(A,-dr*p)
        near(sum(m1),0.)
        near(m1[1]-m1[2],v0*piB/(b0+r0))
        m2=np.linalg.solve(A,-(np.array([2*d0*p[0],0.,0.])+2*dr*m1))
        M=sum(m2)
        target=2*(d0*p[0]+v0*v0*piB/(b0+r0))/r0
        near(M,target)
        # Independent mode-resolved Fourier generator, complex arithmetic.
        for kval in (0.,.1,.7,2.,5.):
            K=np.array([-d0*kval**2, 1j*v0*kval,-1j*v0*kval],complex)
            mat=rates.T+np.diag(K)-r0*np.eye(3)
            f=np.linalg.solve(mat,-r0*reset_probs)
            near(sum(f).imag,0.)
            pred=r0*((b0+r0)*(a0+b0+r0)+v0*v0*kval*kval)/(float(Q.subs({a:a0,b:b0,r:r0,d:d0,v:v0,k:kval}))) if mode=='D' else r0*(b0+r0)*(a0+b0+r0+d0*kval*kval)/(float(Q.subs({a:a0,b:b0,r:r0,d:d0,v:v0,k:kval})))
            near(sum(f).real,pred)
            if abs(v0*v0-d0*(b0+r0))<1e-12:near(sum(f).real,r0/(r0+d0*kval*kval))
        # Independent 6x6 state-resolved cross-moment semigroup.
        B=np.diag(dr)
        gen=np.block([[A,B],[np.zeros((3,3)),state_Q.T]])
        init=np.concatenate((m2,m1))
        for lag in times:
            by_generator=sum((expm(gen*lag)@init)[:3])
            formula=math.exp(-r0*lag)*(M+v0*v0*piB/(b0*(b0+r0))*(1-math.exp(-b0*lag)))
            near(by_generator,formula)

for a0,b0,r0,d0 in [(2,3,1,2),(.1,1,1,1),(4,.5,1.2,.7),(.5,4,3,.3),(1.1,.7,.5,7),(.2,.3,.4,3),(.8,5,2,1.3)]:
    v0=math.sqrt(d0*(b0+r0))
    check(a0,b0,r0,d0,v0,[0.,.01,.3,1.,3.])
    # Off-balance: show formula still correct with no aliasing.
    check(a0,b0,r0,d0,v0*1.3,[0.,.1,.7,2.])

# Integrated gap and unique peak of the covariance aliasing failure.
t=sp.symbols('t',positive=True)
G=d*r/(b*S)*sp.exp(-r*t)*(1-sp.exp(-b*t))
eq(sp.integrate(G,(t,0,sp.oo)),d/(S*(b+r)))
tstar=sp.log(1+b/r)/b
eq(sp.simplify(sp.diff(G,t).subs(t,tstar)),0)
print('PASS:',checks,'exact symbolic / independent matrix-generator assertions')
