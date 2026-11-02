#!/usr/bin/env python3
"""Supplementary numerical checks for the two-site Sinkhorn geodesic theorem.

Requires Python 3 and mpmath. Analytic arguments are in RESULT.md; finite
checks below do not establish asymptotic limits or universal quantifiers.
"""
import mpmath as mp

mp.mp.dps = 55
Q = mp.mpf
K = mp.beta(Q(3)/4, Q(3)/4)
checks = 0

def close(actual, expected, tolerance=Q('1e-38')):
    global checks
    assert abs(actual-expected) <= tolerance*max(1,abs(expected)), (
        mp.nstr(actual,30), mp.nstr(expected,30))
    checks += 1

def h(x, beta):
    return (x*(1-x)+beta)**(-Q(1)/4)

def H(p,beta):
    if p == 0: return Q(0)
    if p == 1: return Z(beta)
    return mp.quad(lambda u: h(u,beta), [0,p])

def Z(beta):
    return 2*mp.quad(lambda u: h(u,beta), [0,Q(1)/2])

def quantile(t,beta):
    zz = Z(beta)
    lo,hi=Q(0),Q(1)/2
    if t == 0: return lo
    if t == Q(1)/2:return hi
    if t > Q(1)/2:return 1-quantile(1-t,beta)
    for _ in range(130):
        mid=(lo+hi)/2
        if H(mid,beta)<t*zz:lo=mid
        else:hi=mid
    return (lo+hi)/2

# Reproduce the exact quadratic optimal self-coupling and the two formulas
# for the Riemannian metric obtained from that previously known coupling.
for ep in [Q('0.7'),Q('1.3'),Q('4')]:
    C=Q('1.2')
    B=mp.expm1(2*C/ep)
    for p in [Q('0.01'),Q('0.1'),Q('0.3'),Q('0.5'),Q('0.9')]:
        a=p*(1-p)
        w=2*a/(1+mp.sqrt(1+4*B*a))
        close(B*w*w+w,a)
        lhs=ep/2*(a-w)/(w*(2*a-w))
        rhs=ep*B/(2*mp.sqrt(1+4*B*a))
        close(lhs,rhs)

# Temperature ordering and exact arclength inversion.
for t in [Q('0.1'),Q('0.25'),Q('0.4')]:
    vals=[]
    for beta in [Q('0.0001'),Q('0.05'),Q('4')]:
        p=quantile(t,beta)
        close(H(p,beta)/Z(beta),t,Q('1e-34'))
        assert p<t
        checks+=1
        vals.append(p)
    assert vals[0]<vals[1]<vals[2]<t
    checks+=1

# Normalization boundary coefficients:  Z_beta=K-8/3 beta^(3/4)+o().
for beta in [Q('1e-7'),Q('1e-9')]:
    deficit=(K-Z(beta))/beta**(Q(3)/4)
    assert abs(deficit-Q(8)/3)<Q('0.06')
    checks+=1

# Boundary time/mass profile: p=beta*y(s), t=s*beta^(3/4)/K.
for beta in [Q('1e-6'),Q('1e-8')]:
    for s in [Q('0.25'),Q('1'),Q('3')]:
        y=(1+Q(3)*s/4)**(Q(4)/3)-1
        actual=K*H(beta*y,beta)/(beta**(Q(3)/4)*Z(beta))
        assert abs(actual-s)<Q('0.02')
        checks+=1

# First-order interior displacement coefficient with beta^(3/4) scaling.
for t in [Q('0.25'),Q('0.4')]:
    p0=mp.findroot(lambda p: mp.betainc(Q(3)/4,Q(3)/4,0,p,regularized=True)-t,(Q('0.1'),Q('0.4')))
    coef=Q(4)/3*(1-2*t)*(p0*(1-p0))**Q('0.25')
    b=Q('1e-7')
    observed=(quantile(t,b)-p0)/b**(Q(3)/4)
    assert abs(observed-coef)<Q('0.025')
    checks+=1

print('PASS:',checks,'supplementary checks; K =',mp.nstr(K,23))
