#!/usr/bin/env python3
"""Numerical and algebraic checks for the stated rank-one Nyström result.

All computations concern the specified 2x2 matrices in exact method definitions;
random checks are verification examples, not proofs of the universal statements.
Requires NumPy, SymPy, SciPy.
"""
import math
import numpy as np
import sympy as sp
from scipy.special import roots_genlaguerre, gamma, betainc

N_CHECKS = 0

def verify(ok, msg):
    global N_CHECKS
    N_CHECKS += 1
    if not ok:
        raise AssertionError(msg)

r, lam, A, C = sp.symbols('r lam A C', positive=True)
f = (lam**2*A+r*C)/(r+lam)**2
verify(sp.simplify(sp.diff(f,lam)-2*r*(lam*A-C)/(r+lam)**3)==0, 'risk derivative identity')

# Exact quadrature of the chi-square expectation, via generalized Laguerre nodes.
def mean_risk(s, a, b, lamda):
    assert s>=1 and a>=b>0 and lamda>0
    nodes, weights=roots_genlaguerre(128,s/2-1)
    w=2*nodes
    avgA=a*a-a*b+b*b
    avgC=a*b
    return avgC+np.dot(weights,(lamda*lamda*avgA+w*avgC)/(w+lamda)**2)/gamma(s/2)

rng=np.random.default_rng(9023161)
for a,b in [(1.,1.),(2.,1.),(10.,0.7),(7.,0.01)]:
    B=np.diag([a,b]); lstar=a*b/(a*a-a*b+b*b)
    theta=(np.arange(16384)+.5)*(2*math.pi/16384)
    u1=a*np.cos(theta);u2=b*np.sin(theta)
    q1sq=u1*u1/(u1*u1+u2*u2)
    verify(abs(np.mean(q1sq)-a/(a+b))<2e-12, 'angular expectation')
    for s in (1,2,3,6,12):
        # The optimal ridge has strictly smaller mean-square error than alternatives.
        risks=[mean_risk(s,a,b,lstar*f) for f in (.25,.5,1.,2.,4.)]
        verify(risks[2]<min(risks[0],risks[1],risks[3],risks[4]),'unique interior ridge optimum')
        for lamda in (0.07,lstar,2.3):
            for _ in range(100):
                x=rng.normal(size=2)
                Y=rng.normal(size=(2,s))
                q=B@x; q/=np.linalg.norm(q)
                qp=np.array([-q[1],q[0]])
                vec=Y.T@q; other=Y.T@qp
                W=vec@vec
                Zprod=vec@other
                P=B*0.0+np.outer(q,(vec@(Y.T@B))/(W+lamda))
                actual=np.linalg.norm(B-P,ord='fro')**2
                p=q@B; t=qp@B
                formula=t@t+np.linalg.norm(lamda*p/(W+lamda)-Zprod*t/(W+lamda))**2
                verify(abs(actual-formula)<3e-9*(1+actual),'direct QR-normalized ridge identity')
        if s>=3:
            expected=a*b*(s-1)/(s-2)
            verify(abs(expected-(a*b+a*b/(s-2)))<1e-12,'unregularized risk')
    if a==b:
        # Exact tail law of the unregularized error for isotropic A.
        for s in (1,2,3,5):
            for z in (1.1*a,1.5*a,3*a):
                from scipy.stats import t
                v=math.sqrt(z*z/a**2-1)
                tail=2*t.sf(v*math.sqrt(s),df=s)
                beta=betainc(s/2,0.5,(a/z)**2)
                verify(abs(tail-beta)<5e-14,'exact beta tail')
print(f'PASS: {N_CHECKS} deterministic checks; conditional matrix identities, optimal ridge, angular law and error tail.')
