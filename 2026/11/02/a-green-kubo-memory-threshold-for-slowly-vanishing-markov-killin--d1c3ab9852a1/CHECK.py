#!/usr/bin/env python3
"""Self-contained checks for slowly vanishing finite-state Markov killing."""
from fractions import Fraction as F
from math import exp, log, sqrt, isclose
from itertools import product

checks=0

def ok(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks+=1

def transition(rho):
    return [[(1+rho)/2,(1-rho)/2],[(1-rho)/2,(1+rho)/2]]

# Exact Green--Kubo identities and Poisson-resolvent solution.
for numerator in range(-9,10):
    rho=F(numerator,10)
    if abs(rho)>=1: continue
    P=transition(rho)
    pi=(F(1,2),F(1,2))
    h=[F(-1),F(1)]
    var=F(1)
    g=[-1/(1-rho),1/(1-rho)]
    ok(all(g[i]-sum(P[i][j]*g[j] for j in range(2))==h[i] for i in range(2)), 'Poisson')
    ok(sum(pi[i]*g[i] for i in range(2))==0, 'centered g')
    martvar=sum(pi[i]*sum(P[i][j]*(g[j]-sum(P[i][z]*g[z] for z in range(2)))**2 for j in range(2)) for i in range(2))
    sig=(1+rho)/(1-rho)
    ok(martvar==sig, 'martingale variance')
    ok(sig==var+2*rho/(1-rho), 'autocovariance sum')
    ok(sig>0, 'positive sigma')

# Finite-horizon matrix recursion is identical to direct path enumeration.
def direct(n, rho, gamma, init):
    p=transition(rho)
    out=0.
    for path in product(range(2),repeat=n+1):
        prob=init[path[0]]
        for k in range(1,n+1):
            prob*=exp(-(2 if path[k-1] else 0)/k**gamma)*p[path[k-1]][path[k]]
        out+=prob
    return out

def fw(n, rho, gamma, init, collect=False):
    p=transition(rho)
    q=list(init); logs=0.; H1=0.; H2=0.; selected={}
    for k in range(1,n+1):
        t=k**(-gamma); u=exp(-2*t)
        v=[q[0],q[1]*u]
        z=v[0]+v[1]
        logs+=log(z)
        q=[(v[0]*p[0][j]+v[1]*p[1][j])/z for j in range(2)]
        H1+=t;H2+=t*t
        if collect and k in (500,1000,3000,10000,20000,50000):
            sig=(1+rho)/(1-rho)
            selected[k]=logs+H1-sig*H2/2
    return logs,H1,H2,selected

for rho in (-0.5, 0, 0.5):
    for gamma in (0.4,0.5,0.7,1.0):
        for n in range(1,9):
            val=direct(n,rho,gamma,(0.3,0.7))
            a,b,c,d=fw(n,rho,gamma,(0.3,0.7))
            ok(isclose(exp(a),val,rel_tol=1e-11,abs_tol=1e-12),'path-sum')

# Static positive-matrix Perron root curvature is the stationary covariance sum.
for rho in (-0.5, -0.25, 0., 0.25, 0.5, 0.8):
    def eiglog(t):
        p=transition(rho)
        tr=p[0][0]+exp(-2*t)*p[1][1]
        de=exp(-2*t)*rho
        return log((tr+sqrt(tr*tr-4*de))/2)
    for h in (0.002,0.001):
        f2=(eiglog(h)-2*eiglog(0)+eiglog(-h))/h**2
        ok(abs(f2-(1+rho)/(1-rho))<0.006,'Perron curvature')

# Numerically distinguish the Green--Kubo polynomial powers with fixed marginal hazard.
for gamma in (0.4,0.5,0.65,1.0):
    for rho in (-0.5,0.5):
        logs,h1,h2,sel=fw(50000,rho,gamma,(0.3,0.7),True)
        ok(all(abs(sel[n])<100 for n in sel),'finite residual')
        ok(abs(sel[50000]-sel[20000]) < (0.10 if gamma==0.4 else 0.025),'residual stabilization')
    if gamma==0.5:
        A=fw(50000,0.5,gamma,(0.3,0.7))[0]
        B=fw(50000,-0.5,gamma,(0.3,0.7))[0]
        ok(abs((A-B)/(log(50000)) - F(4,3))<0.4,'critical power-difference scale')

print('CHECKS_PASSED', checks)
print('CHECKED exact two-state Poisson identities, finite path enumerations, Perron curvature, survival residuals')
print('CRITICAL_EXPONENTS rho=-1/2 : 1/6 ; rho=1/2 : 3/2 ; difference 4/3')
print('LIMITATION finite tests corroborate analytic proof, not a substitute')
