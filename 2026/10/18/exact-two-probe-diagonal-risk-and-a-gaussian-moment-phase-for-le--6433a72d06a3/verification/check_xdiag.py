"""Reproducible finite checks for a scalar-matrix XDiag risk theorem.

Run: python verification/check_xdiag.py
Requires Python 3 and numpy.
Numerical evidence supplements and does not replace the analytic proof.
"""
import itertools
import math
from fractions import Fraction
import numpy as np

checks = 0

def confirm(condition, msg):
    global checks
    assert condition, msg
    checks += 1


def xdiag_scalar(probes, scalar=1.):
    n, k = probes.shape
    ans = np.zeros(n)
    for j in range(k):
        others = np.delete(probes, j, axis=1)
        P = others @ np.linalg.pinv(others) if k>1 else np.zeros((n,n))
        w = probes[:,j]
        ans += scalar * (np.diag(P) + ((np.eye(n)-P) @ w)/w)
    return ans/k


# All sign-product patterns enumerate the exact binomial two-probe law.
for n in range(2, 10):
    a = Fraction(3, 2)
    errors = []
    for t in itertools.product((-1,1),repeat=n):
        S = sum(t)
        err = [-(a/Fraction(n))*t[i]*(S-t[i]) for i in range(n)]
        errors.append(err)
        if n<=7:
            probes=np.column_stack((np.ones(n),np.array(t,dtype=float)))
            actual=xdiag_scalar(probes,float(a))
            confirm(np.allclose(actual,float(a)+np.array([float(e) for e in err]),atol=5e-13),"two-sign-probe identity")
    N=len(errors)
    for i in range(n):
        confirm(sum(e[i] for e in errors)==0,"Rademacher zero mean")
        for j in range(n):
            cov=sum(e[i]*e[j] for e in errors)/N
            wanted=a*a*Fraction(n-1 if i==j else 1,n*n)
            confirm(cov==wanted,"exact covariance")
    mse=sum(sum(x*x for x in e) for e in errors)/N
    confirm(mse==a*a*Fraction(n-1,n),"exact total mean square")

# Every diagonal PSD input: two Rademacher LOO terms coincide, with exact risk.
for n in range(2,9):
    for case in range(5):
        amps=[Fraction((i+case)%5+1, i+1) for i in range(n)]
        if case==4:
            amps=[Fraction(1) if i<2 else Fraction(0) for i in range(n)]
        T=sum(q*q for q in amps)
        S4=sum(q**4 for q in amps); S6=sum(q**6 for q in amps)
        cov_exact=[[Fraction(0) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j:
                    cov_exact[i][j]=amps[i]**2*(S4-amps[i]**4)/T**2
                else:
                    cov_exact[i][j]=amps[i]**3*amps[j]**3/T**2
        errors=[]
        for t in itertools.product((-1,1),repeat=n):
            res=[-amps[i]*t[i]*sum(amps[l]**2*t[l] for l in range(n) if l!=i)/T for i in range(n)]
            errors.append(res)
            if n<=7:
                x=np.ones(n); y=np.array(t,dtype=float)
                Qx=np.array([float(a) for a in amps])*x
                Qy=np.array([float(a) for a in amps])*y
                Px=np.outer(Qx,Qx)/float(T); Py=np.outer(Qy,Qy)/float(T)
                estimates=[]
                for w,P in ((x,Py),(y,Px)):
                    A=np.array([float(a) for a in amps]); estimates.append(A*np.diag(P)+(np.eye(n)-P)@(A*w)/w)
                target=np.array([float(amps[i]+res[i]) for i in range(n)])
                confirm(np.allclose(estimates[0],estimates[1],atol=2e-12),"LOO component identity")
                confirm(np.allclose(estimates[0],target,atol=2e-12),"diagonal exact formula")
        for i in range(n):
            confirm(sum(row[i] for row in errors)==0,"unbiased finite mean")
            for j in range(n):
                actual=sum(e[i]*e[j] for e in errors)/len(errors)
                confirm(actual==cov_exact[i][j],"exact general-diagonal covariance")
        mse=sum(sum(e_i*e_i for e_i in e) for e in errors)/len(errors)
        confirm(mse==(T*S4-S6)/(T*T),"general-diagonal MSE")
        confirm(mse<=T/Fraction(4),"one-quarter upper bound")
        if case==4:confirm(mse==T/Fraction(4),"one-quarter equality")

rng=np.random.default_rng(753199)
# Direct leave-one-out checks: exact endpoints and intermediate nonzero error.
for n in range(2,9):
    for k in range(1,n+3):
        for repeat in range(8):
            W=rng.normal(size=(n,k))
            ans=xdiag_scalar(W,scalar=1.7)
            if k==1 or k>=n+1:
                confirm(np.allclose(ans,1.7,atol=5e-11),"Gaussian exact endpoint")
            else:
                confirm(np.all(np.isfinite(ans)),"intermediate well-defined a.s.")
                if repeat==0:
                    confirm(not np.allclose(ans,1.7,atol=1e-8),"intermediate is nontrivial")

# Symbolic reduced two-dimensional formula from direct projectors.
for _ in range(3000):
    W=rng.normal(size=(2,2))
    x,y=W[:,0],W[:,1]
    U=x[1]/x[0]; V=y[1]/y[0]
    formula=1 - .5*U*V*(1/(1+U*U)+1/(1+V*V))
    confirm(np.isclose(xdiag_scalar(W)[0],formula,rtol=2e-12,atol=2e-12),"Cauchy quotient identity")

# Local residue at a probe coordinate approaching zero. Other terms are bounded.
for n in range(2,7):
    for k in range(2,n+1):
        for rep in range(15):
            W=rng.normal(size=(n,k))
            W[0,0]=0
            P=W[:,1:] @ np.linalg.pinv(W[:,1:])
            residue=-sum(P[0,l]*W[l,0] for l in range(1,n))/k
            if abs(residue)<1e-5:continue
            vals=[]
            for eps in (1e-4,1e-5):
                V=W.copy();V[0,0]=eps
                vals.append((xdiag_scalar(V)[0]-1)*eps)
            confirm(abs(vals[-1]-residue)<2e-3,"Gaussian pole residue")

# Tail constant: t Pr(estimate-first-coordinate > a+t) -> a/pi^2 for n=k=2.
N=3_000_000
U=rng.standard_cauchy(N); V=rng.standard_cauchy(N)
err=-.5*(U*V/(1+U*U)+U*V/(1+V*V))
for t in (50,100,200):
    cplus=t*np.mean(err>t); cminus=t*np.mean(err < -t)
    target=1/math.pi**2
    confirm(abs(cplus-target)<.025 and abs(cminus-target)<.025,"tail constant Monte Carlo")
    print(f"tail_threshold={t} tP(+)= {cplus:.6f} tP(-)= {cminus:.6f}; predicted={target:.6f}")
print(f"PASS: {checks} analytical/enumerative/Monte Carlo checks")
