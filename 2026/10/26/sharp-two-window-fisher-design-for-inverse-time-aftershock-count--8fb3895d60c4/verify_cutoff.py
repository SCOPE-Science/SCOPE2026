"""Reproduce the two-count offset-information theorem for an inverse-time Poisson rate.
Run: python3 verify_cutoff.py (Python standard library only).
"""
from math import exp, expm1, log1p, isclose
from random import Random

def A(u):
    if abs(u)<1e-5:
        return u/2+u*u/6+u**3/24+u**4/120
    return expm1(u)/u-1

def B(v):
    if abs(v)<1e-5:
        return v/2-v*v/6+v**3/24-v**4/120
    return 1+expm1(-v)/v

def root(L):
    low,high=0.,L
    for _ in range(100):
        mid=(low+high)/2
        if A(mid)>B(L-mid):high=mid
        else:low=mid
    return (low+high)/2

def J(L,u):
    h=-expm1(-u); H=-expm1(-L)
    return L/(u*(L-u))*(h-u*H/L)**2

def fisher_direct(K,c,tau,T):
    U=log1p(tau/c);L=log1p(T/c);V=L-U
    m1=K*U;m2=K*V
    # Independent differentiation of log((c+tau)/c) and its difference.
    dm1=K*(1/(c+tau)-1/c)
    dm2=K*(1/(c+T)-1/(c+tau))
    i_kk=(U*U/m1+V*V/m2)
    i_kc=U*dm1/m1+V*dm2/m2
    i_cc=dm1*dm1/m1+dm2*dm2/m2
    return i_cc-i_kc*i_kc/i_kk

r=Random(459123)
N=2200
for i in range(N):
    L=r.uniform(0.04,16.0)
    u=root(L)
    assert 0<u<L/2, (L,u)
    assert A(u)-B(L-u)<1e-11 and A(u)-B(L-u)>-1e-11
    K=exp(r.uniform(-2,2));c=exp(r.uniform(-2,2))
    T=c*expm1(L);tau=c*expm1(u)
    x=fisher_direct(K,c,tau,T)
    y=K/c**2*J(L,u)
    assert isclose(x,y,rel_tol=5e-10,abs_tol=1e-11),(L,u,x,y)
    # The maximum is strict and global: check arbitrary competing intervals.
    w=L*r.uniform(.0005,.9995)
    assert J(L,w)<=J(L,u)*(1+1e-12), (L,u,w)
    # Verify the unbinned information by integrating the score analytically.
    H=-expm1(-L)
    unb=K/c**2*((1-exp(-2*L))/2-H**2/L)
    assert 0<x<=unb*(1+1e-10),(x,unb)

star_lo,star_hi=.01,4.
for i in range(150):
    m=(star_lo+star_hi)/2
    if expm1(m)>2*m:star_hi=m
    else:star_lo=m
star=(star_lo+star_hi)/2
eta=8*star/(1+2*star)**2
assert abs(star-1.2564312086261695)<1e-12
assert abs(eta-.8145287551781475)<1e-12
for L in (4,10,100,1000):
    assert root(L)<star
    if L>10:assert star-root(L)<2/L
for L in (.05,.01,.003):
    u=root(L)
    val=J(L,u)
    # Stable asymptotic checks without cancellation of full information.
    assert abs(u/L-.5)< L/10
    assert abs(val/(L**3)-1/16)<L/10
print(f'PASS: {N} independent Fisher comparisons, maximum checks, unbinned comparisons')
print('positive-root u*:',format(star,'.16g'))
print('limiting tau/c:',format(2*star,'.16g'))
print('limiting information efficiency:',format(eta,'.16g'))
print('relative short-horizon efficiency: 0.75 (analytic asymptotics)')
