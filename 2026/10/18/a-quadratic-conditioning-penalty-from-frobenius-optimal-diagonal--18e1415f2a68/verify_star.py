"""Finite checks for diagonal congruence on SPD star matrices.

Requires Python 3 with numpy and sympy. Analytical proof in RESULT.md is
necessary for universal statements; finite tests here are diagnostics only.
"""
from fractions import Fraction
import numpy as np
import sympy as sp

checks = 0
for d in range(1, 9):
    u = sp.Matrix([1] * d) / sp.sqrt(d)
    for rho in [sp.Rational(1, 5), sp.Rational(1, 2), sp.Rational(4, 5), sp.Rational(9, 10), sp.Rational(99, 100)]:
        A = sp.eye(d+1)
        for k in range(d):
            A[0,k+1] = rho / sp.sqrt(d)
            A[k+1,0] = rho / sp.sqrt(d)
        a = (1-rho**2)/(1-rho**4/d)
        b = (1-rho**2/d)/(1-rho**4/d)
        # Verify exact stationarity and positive definiteness of objective Hessian.
        assert sp.simplify(a-1+rho**2*b)==0; checks+=1
        assert sp.simplify(b-1+rho**2*a/d)==0; checks+=1
        assert a > 0 and b > 0; checks+=1
        H = sp.eye(d+1)
        for k in range(1,d+1): H[0,k]=H[k,0]=rho**2/d
        assert H.det() == 1-rho**4/d; checks+=1
        # Equivalence of block eigenvalues to trace and determinant.
        tr = a+b
        det = a*b*(1-rho**2)
        block = sp.Matrix([[a,rho*sp.sqrt(a*b)],[rho*sp.sqrt(a*b),b]])
        assert sp.simplify(block.det()-det)==0; checks+=1
        assert sp.simplify(sp.trace(block)-tr)==0; checks+=1
        # Exact Frobenius comparison with identity.
        loss_a = sp.expand((a-1)**2+d*(b-1)**2+2*rho**2*a*b)
        assert sp.simplify(2*rho**2-loss_a)>0; checks+=1
        if d>1:
            assert sp.simplify(b-a)>0; checks+=1
        else:
            assert sp.simplify(b-a)==0; checks+=1

rng=np.random.default_rng(100834)
for d in [1,2,3,6,10]:
    for rho in [0.1,0.6,0.95,0.995]:
        A = np.eye(d+1)
        A[0,1:]=rho/np.sqrt(d)
        A[1:,0]=rho/np.sqrt(d)
        a=(1-rho*rho)/(1-rho**4/d)
        b=(1-rho*rho/d)/(1-rho**4/d)
        G=np.diag([np.sqrt(a)]+[np.sqrt(b)]*d)
        vals=np.linalg.eigvalsh(G@A@G)
        disc=np.sqrt((a-b)**2+4*rho*rho*a*b)
        Lplus=(a+b+disc)/2
        Lminus=(a+b-disc)/2
        assert np.isclose(vals[0],Lminus,rtol=1e-8,atol=1e-12); checks+=1
        assert np.isclose(vals[-1],Lplus,rtol=1e-8,atol=1e-12); checks+=1
        cond0=(1+rho)/(1-rho)
        assert np.isclose(vals[-1]/vals[0],(a+b+disc)/(a+b-disc),rtol=1e-8); checks+=1
        assert vals[-1]/vals[0]>=cond0*(1-1e-7); checks+=1
        if d>=2:
            assert vals[-1]/vals[0]>cond0*(1+1e-5); checks+=1
        for rep in range(300):
            scales=np.exp(rng.uniform(-2,2,d+1))
            B=np.diag(scales)@A@np.diag(scales)
            eigs=np.linalg.eigvalsh(B)
            assert eigs[-1]/eigs[0]>=cond0*(1-1e-9); checks+=1

# Dimension-dependent sharp leading coefficient for epsilon = 1-rho^2.
for d in [2,3,5,12]:
    target=(d-1)/d
    target_relative=(d-1)/(4*d)
    for eps in [1e-3,1e-4,1e-5]:
        rho=np.sqrt(1-eps)
        a=eps/(1-(1-eps)**2/d)
        b=(1-(1-eps)/d)/(1-(1-eps)**2/d)
        lplus=(a+b+np.sqrt((a-b)**2+4*(1-eps)*a*b))/2
        cond=lplus*lplus/(a*b*eps)
        opt=(1+rho)/(1-rho)
        assert abs(cond*eps*eps/target-1)<(15*eps); checks+=1
        assert abs((cond/opt)*eps/target_relative-1)<(15*eps); checks+=1

print('PASS',checks,'finite symbolic and numerical checks')
