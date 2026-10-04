#!/usr/bin/env python3
import math
from scipy.integrate import quad
from scipy.special import gamma, betaln

def K(r, ns):
    if not (ns >= r + 1):
        raise ValueError("need ns >= r+1")
    a = r/2.0
    b = (ns-r)/2.0
    lam = r/ns
    u0 = r/(ns+r)
    logB = betaln(a,b)
    def f(u):
        if u <= 0.0 or u >= 1.0:
            return 0.0
        logpdf=(a-1)*math.log(u)+(b-1)*math.log1p(-u)-logB
        return (((1+lam)*u-lam)**2/u) * math.exp(logpdf)
    val, err = quad(f, u0, 1.0, epsabs=1e-12, epsrel=1e-12, limit=300)
    return ns*val

def H(r):
    a=r/2.0
    norm=(2.0**a)*gamma(a)
    def f(q):
        return ((q-r)**2/q) * q**(a-1)*math.exp(-q/2.0)/norm
    val, err=quad(f, r, math.inf, epsabs=1e-12, epsrel=1e-12, limit=300)
    return val

k=K(4,100)
assert abs(k-0.6087790589777283) < 2e-12, k
thr=math.sqrt(k/4.0)
assert abs(thr-0.3901214743441228) < 2e-12, thr
h4=H(4)
assert abs(h4-4.0*math.exp(-2.0)) < 2e-12, h4
assert abs(math.sqrt(h4/4.0)-math.exp(-1.0)) < 2e-12
# Convergence sanity checks for fixed r.
assert abs(K(4,2000)-h4) < 0.004
# Risk ordering on opposite sides of the exact boundary.
def risk(r, ns, nt, sigma=1.0):
    return r*sigma*sigma/(ns+nt) + sigma*sigma*ns*K(r,ns)/(nt*(ns+nt))
def source_risk(r, ns, sigma=1.0):
    return r*sigma*sigma/ns
ns=100; r=4
t_low=max(1, int(math.floor(0.9*thr*ns)))
t_high=int(math.ceil(1.1*thr*ns))
assert risk(r,ns,t_low) > source_risk(r,ns)
assert risk(r,ns,t_high) < source_risk(r,ns)
print("VERIFY_OK")
print(f"K_4_100={k:.15f}")
print(f"threshold_4_100={thr:.15f}")
print(f"H_4={h4:.15f}")
