"""Independent finite checks for the equal-marginal Gaussian Aitken theorem.

The mathematical proof is in RESULT.md; tests do not establish the theorem.
Run: python verify.py
"""
from fractions import Fraction as F
from math import exp, pi, sqrt
import random


def kernel(r,a,sigma,rho):
    mX=a*(r-1)
    mD=a*(r-1)**2
    vX=2*sigma**2*(1-rho)
    vD=6*sigma**2*(1-rho)
    c=-3*sigma**2*(1-rho)
    if vD <= 0: raise ValueError('The common-noise case is separate')
    condvar=vX-c*c/vD
    condmean=mX-c*mD/vD
    return (exp(-mD*mD/(2*vD))/sqrt(2*pi*vD)*(condvar+condmean**2),condvar,condmean)


def gram_corr(u,v,w):
    # Three unit-length vectors generate an arbitrary valid equal-margin covariance.
    def norm(x):return sqrt(sum(z*z for z in x))
    z=[tuple(x) for x in (u,v,w)]
    z=[tuple(q/norm(x) for q in x) for x in z]
    return [[sum(z[i][k]*z[j][k] for k in range(len(z[i]))) for j in range(3)] for i in range(3)]


def general_kernel(C,r,a,sigma=1):
    mx=a*(r-1)
    md=a*(r-1)**2
    vx=C[1][1]+C[0][0]-2*C[0][1]
    vd=C[2][2]+4*C[1][1]+C[0][0]-4*C[1][2]+2*C[0][2]-4*C[0][1]
    c=C[1][2]-2*C[1][1]+C[0][1]-C[0][2]+2*C[0][1]-C[0][0]
    # simplified covariance: C12 - 2C11 + 3C01 - C02 - C00
    if vd <= 1e-12:return None
    condvar=vx-c*c/vd
    condmean=mx-c*md/vd
    K=exp(-md*md/(2*vd))/sqrt(2*pi*vd)*(condvar+condmean*condmean)
    return K,condvar,condmean


def run():
    checks=0
    # Exact rational formulas for every equicorrelation covariance tested.
    for rho in [F(-1,2),F(-2,5),F(0),F(1,3),F(2,3),F(99,100)]:
        s=F(3,2);r=F(2,5);a=F(7,4)
        C=[[s*s*(1 if i==j else rho) for j in range(3)] for i in range(3)]
        vx=C[1][1]+C[0][0]-2*C[0][1]
        vd=C[2][2]+4*C[1][1]+C[0][0]-4*C[1][2]+2*C[0][2]-4*C[0][1]
        c=C[1][2]-2*C[1][1]+3*C[0][1]-C[0][2]-C[0][0]
        assert (vx,vd,c)==(2*s*s*(1-rho),6*s*s*(1-rho),-3*s*s*(1-rho))
        assert vx-c*c/vd==s*s*(1-rho)/2
        assert a*(r-1)-c/vd*a*(r-1)**2==a*(r*r-1)/2
        checks+=5
    # No numerical counterexample to the claimed positive conditional numerator.
    g=random.Random(2956)
    for i in range(2000):
        vectors=[[g.gauss(0,1) for _ in range(3)] for __ in range(3)]
        C=gram_corr(*vectors)
        outcome=general_kernel(C,0.32,1.7)
        assert outcome is not None
        K,var,mu=outcome
        assert var >= -1e-8 and K>0
        checks+=1
    # The one-sided coefficient strictly approaches zero at the common-noise boundary.
    vals=[kernel(0.4,2,1,rho)[0] for rho in (0,0.5,0.9,0.99,0.999)]
    assert vals[-1] < vals[-2] and vals[-1] < 1e-5
    checks+=2
    # Equal-variance affine dependence implies perfect correlation by exact algebra.
    for r in [F(1,3),F(1,2),F(2,3)]:
        # Var((1+r) eps1 - r eps0) - sigma² = 2r(1+r)(sigma²-Cov)
        sigma2=F(4)
        for cov in [F(-3),F(0),F(3),F(4)]:
            lhs=(1+r)**2*sigma2+r*r*sigma2-2*r*(1+r)*cov-sigma2
            assert lhs==2*r*(1+r)*(sigma2-cov)
            checks+=1
    print(f'PASS: {checks} deterministic finite checks; analytic proof separately required')

if __name__=='__main__':run()
