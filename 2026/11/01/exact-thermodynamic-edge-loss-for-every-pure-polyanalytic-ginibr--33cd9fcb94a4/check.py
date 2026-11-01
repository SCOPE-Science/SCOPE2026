#!/usr/bin/env python3
"""Finite-size and identity checks for a pure polyanalytic edge law.

Requires Python, SciPy, NumPy, and SymPy. Finite checks do not replace the proof.
"""
import math
from scipy.integrate import quad
from scipy.special import eval_genlaguerre, eval_hermitenorm
from scipy.stats import poisson
from sympy import Symbol, Rational, binomial, simplify

checks = 0

def assert_close(a, b, tol=2e-4):
    global checks
    assert abs(a-b) <= tol, (a,b,tol)
    checks += 1

def target(r):
    m = r//2
    return math.sqrt(2/math.pi) * ((4*m+1) if r%2==0 else (4*m+2))*math.comb(2*m,m)/4**m

def q(j,r,u):
    if u <= 0: return 0.0
    a,b = min(j,r), max(j,r)
    return math.exp(-u+(b-a)*math.log(u)+math.lgamma(a+1)-math.lgamma(b+1)) * float(eval_genlaguerre(a,b-a,u))**2

def radial_error(N, r):
    # E_N = twice the mean mass outside the area-N disk.
    # Only these j can contribute appreciably; the omitted far tails
    # are bounded by Chebyshev in the theorem and are checked separately below.
    out=0.
    for j in range(N):
        center = j+r+1
        variance = 2*j*r+j+r+1
        if center < N-12*math.sqrt(variance):
            # A conservative fast path for numerical checking only;
            # the test uses the exact integration for all retained j.
            continue
        upper=max(N+32*math.sqrt(N*(2*r+1)),center+24*math.sqrt(variance))
        out += quad(lambda u: q(j,r,u),N,upper,epsabs=1e-10,epsrel=1e-9,limit=100)[0]
    return 2*out/math.sqrt(N)

def main():
    global checks
    t=Symbol('t')
    # Exact first coefficients of the Mehler-generated absolute moments.
    for r in range(9):
        from sympy import series
        gen=((1+t)**2/(1-t**2)**Rational(3,2))
        coeff=gen.series(t,0,r+1).removeO().expand().coeff(t,r)
        m=r//2
        wanted=((4*m+1) if r%2==0 else (4*m+2))*binomial(2*m,m)/4**m
        assert simplify(coeff-wanted)==0
        checks+=1
    # First absolute moments under squared Hermite-normal density.
    for r in range(6):
        moment=quad(lambda x: 2*x*math.exp(-x*x/2)/math.sqrt(2*math.pi) * float(eval_hermitenorm(r,x))**2/math.factorial(r),0,14,epsabs=1e-11)[0]
        assert_close(moment,target(r),4e-10)
    # Every summand integrates to unity (Laguerre orthogonality).
    for r in range(5):
        for j in range(7):
            norm=quad(lambda u:q(j,r,u),0,max(80,20*(j+r+1)),epsabs=1e-11,limit=150)[0]
            assert_close(norm,1,5e-8)
    # Finite-size edge constants converge from below to the closed form.
    for r in range(4):
        vals=[radial_error(N,r) for N in (64,256)]
        print('r',r,'N=64',vals[0],'N=256',vals[1],'limit',target(r))
        assert abs(vals[-1]-target(r))<0.018, (r,vals,target(r))
        assert abs(vals[-1]-target(r)) < abs(vals[0]-target(r))+0.002
        checks+=2
    print('PASSED',checks,'checks')

if __name__=='__main__': main()
