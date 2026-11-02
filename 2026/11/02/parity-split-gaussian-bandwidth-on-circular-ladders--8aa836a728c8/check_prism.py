#!/usr/bin/env python3
"""Independent numerical illustrations of the proved circular-ladder spectral law.
No finite computation is used in place of the all-order inequalities.
"""
from math import exp, cos, sin, pi

def g(r, t):
    return exp(-t*r*r)-exp(-t*(r+1)*(r+1))

def f(t):
    return 1-3*exp(-t)+4*sum((-1)**r*exp(-t*r*r) for r in range(2, 30))

def fp(t):
    return 3*exp(-t)-4*sum((-1)**r*r*r*exp(-t*r*r) for r in range(2, 30))

def q(t):
    return -sum((-1)**r*r*r*g(r, t) for r in range(1, 30))

def bisect(fn, lo, hi):
    assert fn(lo)<0<fn(hi)
    for _ in range(90):
        mid=(lo+hi)/2
        if fn(mid)<0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def modes(n,t):
    d=[min(j,n-j) for j in range(n)]
    a=[exp(-t*r*r) for r in d]
    b=[exp(-t*(r+1)*(r+1)) for r in d]
    plus=[sum((a[j]+b[j])*cos(2*pi*k*j/n) for j in range(n)) for k in range(n)]
    minus=[sum((a[j]-b[j])*cos(2*pi*k*j/n) for j in range(n)) for k in range(n)]
    return plus,minus

def direct_residual(n,t,k):
    # Fourier/layer antisymmetric vector, computed directly with 2n-by-2n kernel.
    v=[complex(cos(2*pi*k*j/n),sin(2*pi*k*j/n))*sgn
       for sgn in (1,-1) for j in range(n)]
    lam=modes(n,t)[1][k]
    err=0.0
    for s in range(2):
        for i in range(n):
            lhs=0j
            for r in range(2):
                for j in range(n):
                    d=min(abs(i-j),n-abs(i-j))+abs(s-r)
                    lhs+=exp(-t*d*d)*v[r*n+j]
            err=max(err,abs(lhs-lam*v[s*n+i]))
    return err

tstar=bisect(f,1,1.2)
cstar=pi*pi*q(tstar)/fp(tstar)
assert 1<tstar<1.2 and cstar>0
assert abs(tstar-1.0378840547056856)<2e-12
assert abs(cstar-3.3545514058685084)<2e-10
for n in (20,21,24,25,32,33,40,41,80,81):
    k=n//2
    fn=lambda t:modes(n,t)[1][k]
    tn=bisect(fn,1,1.2)
    for t in (1,tn-1e-4,tn+1e-4,1.4,3.0):
        plus,minus=modes(n,t)
        assert min(plus)>0, (n,t,'plus')
        assert min(minus)==min(minus[k],minus[-k]) or abs(min(minus)-minus[k])<1e-11
        if t<tn: assert minus[k]<0,(n,t,'negative side')
        if t>tn: assert min(minus)>0,(n,t,'positive side')
    if n%2==0:
        assert abs(tn-tstar)<1e-8
    if n%2==1 and n>=41:
        assert abs(n*n*(tstar-tn)-cstar)<0.002
    assert direct_residual(n,tn+0.001,k)<2e-11
    print('n=',n,'critical_t=',format(tn,'.12f'),
          'nullity=',(1 if n%2==0 else 2))
print('limiting_t=',format(tstar,'.14f'),'odd_coefficient=',format(cstar,'.14f'))
print('PASS: 10 finite cases, Fourier-versus-direct matrix eigenpairs, thresholds, parity asymptotics')
