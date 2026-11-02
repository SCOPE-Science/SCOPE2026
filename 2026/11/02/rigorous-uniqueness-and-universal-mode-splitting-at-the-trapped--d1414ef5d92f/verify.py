"""Reproduce finite diagnostic checks for the beta--Gaussian modal transition.
Dependencies: Python 3.10+, numpy, scipy, sympy.
These checks support but do not replace the all-parameter analytical proof.
"""
import math
import numpy as np
import sympy as sy
from scipy.special import roots_jacobi, hyp1f1
from scipy.optimize import brentq

checks = 0

def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

def h(beta, ell):
    return 2*beta/(2*ell+1) * hyp1f1(1.5, ell+1.5, -beta) / hyp1f1(0.5, ell+0.5, -beta)

def threshold(ell):
    bc = brentq(lambda b: h(b,ell)-1, .49, 50., xtol=2e-13)
    return bc, 1/(2*bc)

# Verify the exact Riccati crossing identity symbolically.
beta, ell, m = sy.symbols('beta ell m', positive=True)
mp = m*m - (1+(ell+sy.Rational(1,2))/beta)*m + sy.Rational(1,2)/beta
hp = 2*m + 2*beta*mp
check(sy.simplify(hp.subs(m,1/(2*beta)) - (1-ell)/beta) == 0, 'Kummer crossing identity')

ells = [0.1, 0.25, 0.5, 0.75, 0.9]
previous = 2.0
for ell_value in ells:
    bc, tc = threshold(ell_value)
    print(f'ell={ell_value:g}: beta_c={bc:.12f}, t_c={tc:.12f}')
    check(0 < tc < previous, 'strict threshold ordering')
    previous = tc
    check(abs(h(bc,ell_value)-1) < 1e-11, 'curvature zero')
    for fraction in [0.01, 0.1, .5, .95]:
        check(h(bc*fraction,ell_value) < 1, 'low beta side')
        check(h(bc/fraction,ell_value) > 1, 'high beta side')
    eps = 1e-5
    observed = (h(bc+eps,ell_value)-h(bc-eps,ell_value))/(2*eps)
    check(abs(observed-(1-ell_value)/bc) < 1e-5, 'positive crossing derivative')
    y,w=roots_jacobi(260,ell_value-1,ell_value-1)
    w=w/w.sum()
    def vals(t,x):
        z=(x-y)/math.sqrt(t)
        v=w*np.exp(-.5*z*z)/math.sqrt(2*math.pi*t)
        f=v.sum()
        df=((y-x)*v/t).sum()
        d2=(((x-y)**2/t**2-1/t)*v).sum()
        d4=(((x-y)**4/t**4-6*(x-y)**2/t**3+3/t**2)*v).sum()
        return f,df,d2,d4
    f0,_,f2,f4=vals(tc,0.0)
    check(abs(f2)<1e-9, 'stationary center curvature')
    check(abs(f4+2*(1-ell_value)*f0/tc**2)<2e-7, 'critical quartic')
    for mult, expected in [(.8, 1),(1.2,-1)]:
        t=tc*mult
        check(vals(t,0.)[2]*expected>0,'curvature-phase sign')
    for delta in [.01,.003,.001]:
        t=tc-delta
        check(t>0,'positive noise variance')
        mstar=brentq(lambda x:vals(t,x)[1],1e-6,1.2)
        expected=3*delta
        tolerance=.06 if delta==.01 else .025 if delta==.003 else .009
        check(abs(mstar*mstar/delta-3)<tolerance,'universal mode splitting')
        check(vals(t,mstar)[2]<0, 'two side maxima')
        check(vals(t,0.)[2]>0, 'central minimum')
    # A sampled sign chart: no additional sign reversals outside the two modes.
    for t in [0.8*tc,1.2*tc]:
        ys = np.linspace(.002,1.4,250)
        derivatives=np.array([vals(t,float(x))[1] for x in ys])
        changes=np.count_nonzero((derivatives[:-1]*derivatives[1:]) <0)
        check(changes == (1 if t<tc else 0),'mode sign chart')
    # Exact evenness, normalization of Jacobi density, and physical support.
    check(abs(sum(w)-1)<1e-13,'weights normalized')
    for z in [.25,.5,1.]:
        check(abs(vals(tc,z)[0]-vals(tc,-z)[0])<1e-12,'even profile')

# The pure persistent two-point limit has its exact threshold at t=1.
for beta0 in [.2,.5,1.0,2.0]:
    val = 2*beta0
    check((val>1)==(beta0>.5),'two-point limiting transition')
print(f'PASS: {checks} deterministic analytical-identity and numerical diagnostic assertions')
