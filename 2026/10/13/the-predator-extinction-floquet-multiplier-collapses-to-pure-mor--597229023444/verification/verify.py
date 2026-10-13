#!/usr/bin/env python3
import math

def check(r,K,eta,h,p1,El,p2,mu):
    kappa=1.0-p1*El
    assert 0.0<h<eta*K and 0.0<kappa<1.0 and 0.0<=p2*El<1.0 and mu>0.0
    T=(1.0/r)*math.log((eta*K-kappa*h)/(kappa*(eta*K-h)))
    ratio=(eta*K-kappa*h)/(eta*K-h)
    integ=-math.log(kappa)-(r+mu)*T
    rho_source=(1.0-p2*El)*ratio*math.exp(integ)
    rho_exact=(1.0-p2*El)*math.exp(-mu*T)
    assert T>0.0
    assert math.isclose(ratio,kappa*math.exp(r*T),rel_tol=1e-12,abs_tol=1e-14)
    assert math.isclose(rho_source,rho_exact,rel_tol=1e-12,abs_tol=1e-14)
    assert 0.0<rho_exact<1.0
    return T,rho_exact

for args in [
    (2.0,100.0,0.6,30.0,0.3,2.0,0.2,1.0),
    (1.1,50.0,0.7,20.0,0.2,1.0,0.4,0.3),
    (3.0,80.0,0.8,25.0,0.1,2.0,0.0,0.9),
    (0.7,120.0,0.55,40.0,0.25,1.5,0.3,0.2),
]:
    check(*args)

r,K,eta,h,p1,El,mu=2.0,100.0,0.6,30.0,0.3,2.0,1.0
kappa=1.0-p1*El
pbar=p1*h/(eta*K-kappa*h)
T,rho_low=check(r,K,eta,h,p1,El,0.1,mu)
_,rho_pub=check(r,K,eta,h,p1,El,0.2,mu)
assert math.isclose(T,math.log(2.0),rel_tol=1e-12)
assert math.isclose(pbar,0.1875,rel_tol=1e-12)
assert 0.1<pbar
assert math.isclose(rho_low,0.4,rel_tol=1e-12)
assert math.isclose(rho_pub,0.3,rel_tol=1e-12)
print("VERIFY_OK")
