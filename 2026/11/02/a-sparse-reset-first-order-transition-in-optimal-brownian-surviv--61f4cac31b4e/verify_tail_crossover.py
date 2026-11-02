#!/usr/bin/env python3
"""Numerical diagnostics for the two-reset Brownian survival-rate crossover.
Uses only Python standard library. Finite checks supplement, not replace, proof.
"""
import json, math

EPS = 1e-13
D = 1.0

def mixture(theta, L, c):
    p = c/(L*L)
    assert 0 < p < 1 and theta > 0
    q = p*math.exp(-theta) + (1-p)*math.exp(-L*theta)
    one_minus_q = p*(-math.expm1(-theta)) + (1-p)*(-math.expm1(-L*theta))
    return q, one_minus_q

def rate(theta,L,c):
    q, omq = mixture(theta,L,c)
    return theta**2/omq

def tail(theta,L,c):
    q, omq = mixture(theta,L,c)
    return theta**2*q/omq

def max_golden(f,lo,hi):
    gr=(math.sqrt(5)-1)/2
    x=hi-gr*(hi-lo); y=lo+gr*(hi-lo)
    fx=f(x);fy=f(y)
    for _ in range(160):
        if fx<fy:
            lo=x;x=y;fx=fy;y=lo+gr*(hi-lo);fy=f(y)
        else:
            hi=y;y=x;fy=fx;x=hi-gr*(hi-lo);fx=f(x)
    z=(lo+hi)/2
    return z,f(z)

def branches(L,c):
    uf,Ff=max_golden(lambda u:L*L*tail(u/L,L,c),.5,3)
    vn,Fn=max_golden(lambda v:L*L*tail(v,L,c),1,3)
    return uf,Ff,vn,Fn

def bisect(f,lo,hi):
    fl=f(lo);fh=f(hi)
    assert fl*fh<0,(fl,fh)
    for _ in range(80):
        mi=(lo+hi)/2
        fm=f(mi)
        if fl*fm<=0:hi=mi;fh=fm
        else:lo=mi;fl=fm
    return (lo+hi)/2

u=bisect(lambda a:2*(-math.expm1(-a))-a,1,2)
C=u*u/math.expm1(u)
cstar=math.exp(2)*C/4
A=u*u/(-math.expm1(-u))
K=(math.exp(2)/4)*cstar*A-cstar*cstar/math.exp(2)
checks=0

def check(cond,msg):
    global checks
    checks+=1
    if not cond:raise AssertionError(msg)

check(abs(A-2*u)<1e-12,"optimum relation")
check(1.1<cstar<1.3,"critical weight")
check(K>0,"positive shift")

# Independent survival-pole checks use the denominator of the Laplace
# transformed renewal equation, not the optimized objective function.
for L in (6,12,30,100):
    for c in (.1,.5,1.3,2.0):
        if c>=L*L:continue
        prev=0.0
        for j in range(1,101):
            theta=10**(-3+5*j/100)
            r=rate(theta,L,c)
            lam=tail(theta,L,c)
            q,_=mixture(theta,L,c)
            check(r>prev,"reset-rate parameter monotonicity")
            prev=r
            check(0<lam<r,"pole position")
            check(abs(r*q-lam)<=3e-13*max(1,lam),"renewal pole equation")
            check(abs((r-lam)-theta*theta)<3e-13*max(1,r),"spectral parameter")

# The scaled objective has two separated peaks. Check branch height and
# both candidate rate scales, and compare against a broad logarithmic grid.
phase=[]
for L in (25,50,100,200,400):
    for c in (0.7*cstar,1.0*cstar,1.3*cstar):
        uf,Ff,vn,Fn=branches(L,c)
        check(abs(uf-u)<.035,"far optimum tends to u")
        check(abs(vn-2)<.005,"near optimum tends to 2")
        check(abs(Ff-C)<.009,"far height")
        check(abs(Fn-4*c/math.exp(2))<.01,"near height")
        for j in range(1601):
            theta=math.exp(math.log(1e-6)+(math.log(30)-math.log(1e-6))*j/1600)
            check(L*L*tail(theta,L,c) <= max(Ff,Fn)+3e-10,"outside peak dominates")
        if c != cstar:
            check((Ff>Fn)==(c<cstar),"branch phase ordering")
        phase.append({"L":L,"c":c,"far":Ff,"near":Fn,"u_far":uf,"v_near":vn})

critical=[]
for L in (25,40,60,100,160,320,640):
    def gap(c):
        _,Ff,_,Fn=branches(L,c)
        return Ff-Fn
    cl=bisect(gap,0.95*cstar,1.2*cstar)
    uf,Ff,vn,Fn=branches(L,cl)
    check(abs(Ff-Fn)<1e-9,"coexistence")
    check(abs(uf-u)<.04,"far scale coexistence")
    check(abs(vn-2)<.003,"near scale coexistence")
    check(gap(.95*cstar)>0 and gap(1.2*cstar)<0,"branch swap")
    critrate_far=rate(uf/L,L,cl)
    critrate_near=rate(vn,L,cl)
    check(critrate_near>10*critrate_far,"separated optimizers")
    critical.append({"L":L,"c_L":cl,"L2(c_L-cstar)":L*L*(cl-cstar),"r_far":critrate_far,"r_near":critrate_near})
check(abs(critical[-1]['L2(c_L-cstar)']-K)<.08,"critical shift asymptotic")
print(json.dumps({"diagnostics":"PASS","checks":checks,"u_star":u,"C":C,"c_star":cstar,"A":A,"K":K,"critical":critical,"phase_sample":[phase[0],phase[2],phase[-1]]},indent=2))
