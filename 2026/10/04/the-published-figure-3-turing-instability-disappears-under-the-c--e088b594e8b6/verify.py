#!/usr/bin/env python3
import math

def bisect(fun, lo, hi, n=120):
    flo=fun(lo); fhi=fun(hi)
    assert flo*fhi < 0.0
    for _ in range(n):
        mid=(lo+hi)/2.0; fm=fun(mid)
        if flo*fm <= 0.0:
            hi=mid; fhi=fm
        else:
            lo=mid; flo=fm
    return (lo+hi)/2.0

s=0.2; b=3.0; c=0.5; e=0.2; h=0.4; l=0.5; m=1.0; p=0.0; q=0.56; r=1.0

def poly(u): return 16*u**3-144*u**2+314*u+15
u=bisect(poly,3.8,4.0)
v=5*(1+u)/(2*u-5)

def f(u,v):
    D=1+m*u+p*v
    return u*(b*u/(c+u)-e-h*u)-l*u*v/D

def g(u,v):
    D=1+m*u+p*v
    return q*l*u*v*v/(D*(r+v))-s*v

assert abs(f(u,v)) < 1e-11 and abs(g(u,v)) < 1e-11
D=1+m*u+p*v
fu=u*(b*c/(c+u)**2-h+l*m*v/D**2)
fv=-l*u*(1+m*u)/D**2
gu=q*l*v*v*(1+p*v)/(D**2*(r+v))
gv=s*((1+m*u)/D-v/(r+v))
# Finite-difference cross-check.
eps=1e-6
fd_fu=(f(u+eps,v)-f(u-eps,v))/(2*eps)
fd_fv=(f(u,v+eps)-f(u,v-eps))/(2*eps)
fd_gu=(g(u+eps,v)-g(u-eps,v))/(2*eps)
fd_gv=(g(u,v+eps)-g(u,v-eps))/(2*eps)
for a,bv in [(fu,fd_fu),(fv,fd_fv),(gu,fd_gu),(gv,fd_gv)]:
    assert abs(a-bv) < 2e-8
tr=fu+gv
det=fu*gv-fv*gu
assert tr < -0.5 and det > 0.026

def modal(d1,d2,mu):
    A=d2*fu+d1*gv
    return tr-(d1+d2)*mu, det-A*mu+d1*d2*mu*mu, A

# Figure 3.
tau0,delta0,A3=modal(0.01,10.0,0.0)
assert tau0 < 0.0 and delta0 > 0.0 and A3 < -5.29
# A3<0 makes all coefficients of delta(mu) positive for mu>=0.
for mu in [0.0,0.01,0.1,0.83,1.0,10.0,100.0]:
    tau,delta,_=modal(0.01,10.0,mu)
    assert tau < 0.0 and delta > 0.0
_,delta83,_=modal(0.01,10.0,0.83)
assert abs(delta83-4.48731831648) < 2e-10
assert abs(delta83-(-0.06913)) > 4.5
# Figure 4 is also linearly stable.
_,_,A4=modal(0.1,1.0,0.0)
assert A4 < 0.0
for mu in [0.0,0.1,1.0,10.0,100.0]:
    tau,delta,_=modal(0.1,1.0,mu)
    assert tau < 0.0 and delta > 0.0
print('VERIFY_OK')
print('u0',repr(u))
print('v0',repr(v))
print('fu',repr(fu),'fv',repr(fv),'gu',repr(gu),'gv',repr(gv))
print('trace',repr(tr),'det',repr(det))
print('A_fig3',repr(A3),'delta_0.83',repr(delta83))
print('A_fig4',repr(A4))
