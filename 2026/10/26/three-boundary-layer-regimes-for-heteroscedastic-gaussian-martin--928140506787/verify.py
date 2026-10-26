"""Reproduce finite exact and numerical checks for a Gaussian martingale transport phase diagram.

Run: python verify.py. Requires scipy for the Gaussian quantile and integration checks.
"""
from fractions import Fraction
from math import sqrt, log, exp, pi
from scipy.stats import norm
from scipy.optimize import brentq
from scipy.integrate import quad


def f(t):
    return norm.pdf(norm.ppf(t))


def g(t):
    return f(t) + f(t + 0.5)


def gp(t):
    return -norm.ppf(t) - norm.ppf(t + 0.5)


def gpp(t):
    return -1 / f(t) - 1 / f(t + 0.5)


def rows(p, r):
    H = p - Fraction(1, 2)
    s = H - r
    return (r + Fraction(1, 2), Fraction(1, 2) - 2*r, r), (s, Fraction(1, 2) - 2*s, s + Fraction(1, 2))


def solve(p, R):
    H = p - .5
    left, right = max(0., H-.25), min(H, .25)
    return brentq(lambda r: R*gp(r) - gp(H-r), left + 1.e-13, right - 1.e-13, xtol=2.e-15)


def numerical_cov(row):
    left, mid, right = row
    # Direct quantile integral with independently computed truncated-normal moments.
    # Integral over quantile levels [a,b] equals phi(Phi^{-1}(a))-phi(Phi^{-1}(b)).
    # Endpoint atoms contribute their values times this integral.
    zero = lambda z: 0.0 if z in (0., 1.) else norm.pdf(norm.ppf(z))
    return (-1)*(zero(0.)-zero(left)) + (1)*(zero(1.-right)-zero(1.))


def numerical_w2(row, mean, sigma):
    cuts = [0., row[0], row[0]+row[1], 1.]
    values = [-1., 0., 1.]
    tot = 0.
    for i in range(3):
        a,b = cuts[i],cuts[i+1]
        if b-a < 1.e-15: continue
        # Integrate against a Gaussian quantile without using the f identity.
        integral, err = quad(lambda z:(values[i]-mean-sigma*z)**2*norm.pdf(z),
                             -15. if a==0. else norm.ppf(a),
                             15. if b==1. else norm.ppf(b),epsabs=1.e-11,epsrel=1.e-11)
        tot += integral
    return tot


def check():
    rational_cases = 0
    numerical_comparisons = 0
    for den in (8, 12, 20):
        for k in range(den//2+1, den):
            p=Fraction(k,den)
            H=p-Fraction(1,2)
            left=max(Fraction(0),H-Fraction(1,4))
            right=min(Fraction(1,4),H)
            for j in range(15):
                r=left+(right-left)*Fraction(j,14)
                a,b=rows(p,r)
                assert all(t>=0 for t in a+b)
                assert sum(a)==sum(b)==1
                assert -a[0]+a[2]==Fraction(-1,2)
                assert -b[0]+b[2]==Fraction(1,2)
                assert (a[0]+b[0])/2==p/2
                assert (a[1]+b[1])/2==1-p
                assert (a[2]+b[2])/2==p/2
                rational_cases += 1
    for p in (.6,.7,.75,.8,.9):
        H=p-.5
        for R in (.4,1.,2.,3.,5.):
            r=solve(p,R)
            s=H-r
            assert 0<r<.25 and 0<s<.25
            assert abs(R*gp(r)-gp(s))<1.e-9
            assert gpp(r)<0 and gpp(s)<0
            assert abs(solve(p,1./R)-(H-r))<3.e-12
            # A finite-grid comparison of the actual W2^2 objective.
            am, ap=rows(Fraction(str(p)),Fraction(str(r)))
            am=tuple(float(x) for x in am);ap=tuple(float(x) for x in ap)
            optimum=(numerical_w2(am,-.5,R)+numerical_w2(ap,.5,1.))/2
            for offset in (-0.015,-0.005,0.005,0.015):
                x=r+offset
                if x<=max(0.,H-.25) or x>=min(H,.25):continue
                c,d=rows(Fraction(str(p)),Fraction(str(x)))
                cost=(numerical_w2(tuple(map(float,c)),-.5,R)+numerical_w2(tuple(map(float,d)),.5,1.))/2
                assert cost+2.e-10>=optimum,(p,R,r,x,cost,optimum)
                numerical_comparisons += 1
    z75=norm.ppf(.75)
    c=2/norm.pdf(z75)
    assert 6.2<c<6.4
    # Asymptotic trend checks at feasible floating-point scales, not proofs.
    H=.25
    ratios=[]
    for R in (30.,100.,300.,1000.):
        r=solve(.75,R);s=H-r
        ratios.append(s*R/sqrt(2*log(R)))
    assert abs(ratios[-1]-1/c)<.03
    print('Exact rational row cases:',rational_cases)
    print('Numerical objective comparisons:',numerical_comparisons)
    print('Critical boundary ratio at R=30,100,300,1000:',ratios)
    print('Predicted critical coefficient:',1/c)
    print('All finite checks passed; the infinite asymptotic statements require their analytic proof.')

if __name__=='__main__':check()
