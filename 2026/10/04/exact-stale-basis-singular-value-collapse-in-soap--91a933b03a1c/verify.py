import math
import random

def f_eps(z, eps):
    return z/(abs(z)+eps)

def eigvals_sym2(a,b,d):
    tr=a+d
    disc=math.sqrt((a-d)*(a-d)+4*b*b)
    return (0.5*(tr-disc),0.5*(tr+disc))

def cond_abs_eigs(a,b,d):
    lo,hi=eigvals_sym2(a,b,d)
    s=sorted((abs(lo),abs(hi)))
    assert s[0] > 0.0
    return s[1]/s[0]

random.seed(20261003)

# 45-degree stale basis: exact formula.
for _ in range(1000):
    kappa = 1.0 + 10.0**random.uniform(-3,3)
    eps = 10.0**random.uniform(-5,1)
    d = 0.5*(kappa+1.0)
    c = 0.5*(kappa-1.0)
    p = d/(d+eps)
    r = c/(c+eps)
    direct = (p+r)/(p-r)
    closed = kappa + (kappa*kappa-1.0)/(2.0*eps)
    assert abs(direct-closed) <= 2e-6*max(1.0,closed)
    smin = p-r
    smin_closed = 4.0*eps/((kappa+1.0+2.0*eps)*(kappa-1.0+2.0*eps))
    assert abs(smin-smin_closed) <= 2e-12*max(1.0,abs(smin))

    # Fresh eigenbasis.
    fresh = (kappa/(kappa+eps))/(1.0/(1.0+eps))
    fresh_closed = kappa*(1.0+eps)/(kappa+eps)
    assert abs(fresh-fresh_closed) < 2e-14*max(1.0,fresh_closed)

# General angular off-diagonal and half-saturation law.
for _ in range(1000):
    kappa = 1.0 + 10.0**random.uniform(-2,2)
    eps = 10.0**random.uniform(-8,-2)
    theta = random.uniform(1e-5, math.pi/2-1e-5)
    c = 0.5*(kappa-1.0)*abs(math.sin(2.0*theta))
    r = c/(c+eps)
    assert abs(abs(f_eps(c,eps))-r) < 1e-15

    if 2.0*eps < kappa-1.0:
        thalf = 0.5*math.asin(2.0*eps/(kappa-1.0))
        chalf = 0.5*(kappa-1.0)*math.sin(2.0*thalf)
        rhalf = chalf/(chalf+eps)
        assert abs(rhalf-0.5) < 2e-13

# Canonical practical-scale arithmetic.
kappa=2.0
eps=1e-8
closed = kappa + (kappa*kappa-1.0)/(2.0*eps)
assert abs(closed-150000002.0) < 1e-6
fresh = kappa*(1.0+eps)/(kappa+eps)
assert abs(fresh-1.000000005) < 2e-15

# Noncommuting limits: fixed nonzero angle then epsilon -> 0 gives rank-one sign matrix;
# zero angle first then epsilon -> 0 gives identity.
kappa=3.0
theta=0.1
for eps in (1e-2,1e-4,1e-6,1e-8):
    co=math.cos(theta)
    si=math.sin(theta)
    a=kappa*co*co+si*si
    d=kappa*si*si+co*co
    c=(kappa-1.0)*si*co
    A=f_eps(a,eps)
    B=f_eps(c,eps)
    D=f_eps(d,eps)
    small,_=sorted((abs(x) for x in eigvals_sym2(A,B,D)))
    if eps <= 1e-6:
        assert small < 2e-4

# At theta=0 the off diagonal is identically zero and the two diagonal gains tend to one.
for eps in (1e-2,1e-4,1e-6,1e-8):
    A=f_eps(kappa,eps)
    D=f_eps(1.0,eps)
    B=f_eps(0.0,eps)
    assert B == 0.0
    if eps <= 1e-6:
        assert abs(A-1.0) < 1e-6
        assert abs(D-1.0) < 1.1e-6

print("verification passed")
