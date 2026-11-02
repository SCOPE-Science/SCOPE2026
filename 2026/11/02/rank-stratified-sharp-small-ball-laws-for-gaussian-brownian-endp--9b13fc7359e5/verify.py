#!/usr/bin/env python3
"""Independent numerical checks for the Brownian endpoint small-ball theorem.

The analytic proof, rather than these finite checks, establishes the theorem.
Python 3 standard library only; no external data files.
"""
import math

PI = math.pi
CHECKS = 0

def check(ok, what):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(what)

def close(a, b, tol=1e-9, what=""):
    check(abs(a-b) <= tol*max(1, abs(a), abs(b)),
          what or f"{a} != {b} within {tol}")

def simpson(g, a, b, n=600):
    assert n % 2 == 0
    step = (b-a)/n
    s = g(a)+g(b)
    for i in range(1,n):
        s += (4 if i % 2 else 2)*g(a+i*step)
    return step*s/3

def f(u):
    return math.cos(PI*u/2) if abs(u)<1 else 0.0

def scaled_kernel(eps, u, v, terms=10):
    """A-free survival ratio: exp(lambda_1)*sum eigenvectors / denominator."""
    base=PI**2/(8*eps**2)
    s=0.0
    for n in range(1,terms+1):
        s += math.exp(-(n*n-1)*base)*math.sin(n*PI*(u+1)/2)*math.sin(n*PI*(v+1)/2)
    return s*math.exp(.5*eps**2*(v-u)**2)

def remainder(eps, terms=150):
    b=PI**2/(8*eps**2)
    return sum(n*n*math.exp(-(n*n-1)*b) for n in range(2,terms+1))

def rank_one_H(eps, lam, w0, w1):
    # u variable has physical endpoint value: sqrt(lam)*w_i*z; scaled by eps.
    lo=-1/max(abs(w0),abs(w1)); hi=-lo
    return eps / math.sqrt(2*PI*lam) * simpson(
        lambda t: f(w0*t)*f(w1*t)*math.exp(-eps**2*t*t/(2*lam)),lo,hi,900)

def rank_one_exact_scaled(eps, lam, w0,w1):
    b=1/max(abs(w0),abs(w1))
    return eps/math.sqrt(2*PI*lam)*simpson(
        lambda t: scaled_kernel(eps,w0*t,w1*t)*math.exp(-eps**2*t*t/(2*lam)), -b,b,600)

def rank_two_scaled(eps, lam0,lam1, n=100):
    h=2/n
    ratio_H=ratio_P=0.0
    for i in range(n+1):
        u=-1+i*h
        c0=1 if i in (0,n) else (4 if i%2 else 2)
        for j in range(n+1):
            v=-1+j*h
            c1=1 if j in (0,n) else (4 if j%2 else 2)
            dens=(eps**2/(2*PI*math.sqrt(lam0*lam1)))*math.exp(-.5*eps**2*(u*u/lam0+v*v/lam1))
            weight=c0*c1*dens
            ratio_H += weight*f(u)*f(v)
            ratio_P += weight*scaled_kernel(eps,u,v)
    return ratio_H*h*h/9, ratio_P*h*h/9

def run():
    # Principal-eigenfunction dominance, including negative signs of higher modes.
    for k in range(2,17):
        for j in range(1,60):
            theta=PI*j/60
            check(abs(math.sin(k*theta)) <= k*math.sin(theta)+1e-12,
                  "sine comparison")
    for eps in (.24,.36,.55,.72):
        rem=remainder(eps)
        check(rem<.013, "remainder threshold")
        for i in range(-9,10):
            for j in range(-9,10):
                u=i/10;v=j/10
                actual=scaled_kernel(eps,u,v)
                main=f(u)*f(v)
                lower=(1-rem)*main
                upper=math.exp(2*eps*eps)*(1+rem)*main
                check(lower-1e-10<=actual<=upper+1e-10, "uniform spectral inequality")
    # Integrated law for Brownian bridge with deterministic pinned endpoints.
    for eps in (.22,.37,.60):
        base=PI**2/(8*eps**2)
        series=math.sqrt(2*PI)/eps*sum(math.exp(-( (2*j+1)**2 )*base) for j in range(8))
        survival=math.sqrt(2*PI)/eps*math.exp(-base)*scaled_kernel(eps,0,0)
        close(survival, series,1e-13,"bridge exact spectral survival")
    # C=diag(0,1) is standard Brownian motion. Its survival is known independently.
    for eps in (.24,.39,.63):
        base=PI**2/(8*eps**2)
        known=(4/PI)*sum((-1)**j/(2*j+1)*math.exp(-((2*j+1)**2)*base) for j in range(8))
        h=rank_one_H(eps,1,0,1)
        p=rank_one_exact_scaled(eps,1,0,1)*math.sqrt(2*PI)/eps*math.exp(-base)
        close(p,known,3e-9,"Brownian motion direct exit law")
        check((1-remainder(eps))*h<=p/(math.sqrt(2*PI)/eps*math.exp(-base))+1e-11,
              "Brownian motion lower sandwich")
        check(p/(math.sqrt(2*PI)/eps*math.exp(-base))<=math.exp(2*eps*eps)*(1+remainder(eps))*h+1e-11,
              "Brownian motion upper sandwich")
    # Full rank and singular endpoints, independent quadrature routes.
    for eps in (.23,.38,.57):
        for lam,w in ((1.,(0.,1.)),(.5,(2**-.5,-2**-.5)),(.7,(2**-.5,2**-.5))):
            h=rank_one_H(eps,lam,*w)
            q=rank_one_exact_scaled(eps,lam,*w)
            check(h>0,"strict rank-one leading coefficient")
            check((1-remainder(eps))*h-1e-10<=q<=math.exp(2*eps*eps)*(1+remainder(eps))*h+1e-10,
                  "rank-one uniform inequality")
        h,q=rank_two_scaled(eps,.8,1.3,100)
        check(h>0,"strict rank-two leading coefficient")
        check((1-remainder(eps))*h-1e-10<=q<=math.exp(2*eps*eps)*(1+remainder(eps))*h+1e-10,
              "rank-two uniform inequality")
    # Fixed covariance rank limits; all asymptotic constants obtained independently.
    for eps in (.08,.04,.02):
        for lam,w in ((1.,(0.,1.)),(.5,(2**-.5,-2**-.5)),(.7,(2**-.5,2**-.5))):
            h=rank_one_H(eps,lam,*w)
            b=1/max(map(abs,w))
            integral=simpson(lambda t:f(w[0]*t)*f(w[1]*t),-b,b,900)
            const=integral/math.sqrt(lam)
            estimated=math.sqrt(2*PI)/eps*h
            check(abs(estimated/const-1)<.005,"rank-one sharp constant")
        h,_=rank_two_scaled(eps,.8,1.3,80)
        est=math.sqrt(2*PI)/eps*h
        const=16/(PI**2*math.sqrt(2*PI*.8*1.3))*eps
        check(abs(est/const-1)<.005,"rank-two sharp constant")
    print(f"PASS {CHECKS} deterministic mathematical/numerical assertions")
    print("Uniform killed-kernel sandwich: PASS")
    print("Pinned bridge, Brownian motion, singular and full-rank endpoints: PASS")
    print("Rank-dependent leading prefactors: PASS")
    print("Finite checks are supplementary; the analytic proof covers all dimensions and covariances specified.")

if __name__=='__main__':
    run()
