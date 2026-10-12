#!/usr/bin/env python3
"""Standalone numerical and exact-arithmetic diagnostics for tensor-sketch LS tails.

These are finite checks, not a proof of the limiting tail or moment threshold.
"""
import math
import random
from fractions import Fraction
from itertools import product

RNG = random.Random(314159)

def dot(a, b):
    return sum(x*y for x,y in zip(a,b))

def close(a, b, tol=2e-12):
    assert math.isfinite(a) and math.isfinite(b)
    assert abs(a-b) <= tol*max(1.,abs(a),abs(b)), (a,b)

def signed_error(a, z):
    return dot(a,z)/dot(a,a)

def gamma_abs_ratio_moment(d,p):
    if not 0 < p < d: raise ValueError('outside finite moment domain')
    return math.exp(math.lgamma((p+1)/2)+math.lgamma((d-p)/2)-.5*math.log(math.pi)-math.lgamma(d/2))

def surface_coordinate_abs_moment(dim,p):
    return math.exp(math.lgamma((p+1)/2)+math.lgamma(dim/2)-.5*math.log(math.pi)-math.lgamma((dim+p)/2))

def double_factorial_odd(k):
    if k==0: return 1
    result=1
    for j in range(1,2*k,2): result*=j
    return result

def radially_symmetric_product_normal_norm_moment(dim):
    """Exact E ||Z||^dim for even dim, with iid Z_i=X_iY_i."""
    assert dim%2==0
    half=dim//2
    def rec(rem,coords):
        if len(coords)==dim-1:
            yield coords+(rem,)
        else:
            for j in range(rem+1):yield from rec(rem-j,coords+(j,))
    acc=Fraction(0)
    for powers in rec(half,()):
        multinomial=math.factorial(half)
        term=1
        for j in powers:
            multinomial//=math.factorial(j)
            term*=double_factorial_odd(j)**2
        acc+=multinomial*term
    return acc

def rowwise_log_tail_constant_even(dim):
    v=math.pi**(dim/2)/math.gamma(1+dim/2)
    moment=float(radially_symmetric_product_normal_norm_moment(dim))
    return v/(math.pi**dim) * moment*surface_coordinate_abs_moment(dim,dim)

checks=0
# Case-1 exact Kronecker rows against the scalar product formula.
for r1,r2 in product(range(1,8),range(1,8)):
    for rep in range(15):
        P=[(RNG.gauss(0,1),RNG.gauss(0,1)) for _ in range(r1)]
        Q=[(RNG.gauss(0,1),RNG.gauss(0,1)) for _ in range(r2)]
        xs=[p[0]*q[0] for p in P for q in Q]
        zs=[p[1]*q[1] for p in P for q in Q]
        prod_ratio=dot([p[0] for p in P],[p[1] for p in P])/sum(p[0]**2 for p in P)
        prod_ratio*=dot([q[0] for q in Q],[q[1] for q in Q])/sum(q[0]**2 for q in Q)
        close(signed_error(xs,zs),prod_ratio)
        checks+=1
# Case-2 independent rowwise product: raw LS and conditional ratio agree.
for R in range(1,26):
    for rep in range(20):
        P=[(RNG.gauss(0,1),RNG.gauss(0,1)) for _ in range(R)]
        Q=[(RNG.gauss(0,1),RNG.gauss(0,1)) for _ in range(R)]
        W=[p[0]*q[0] for p,q in zip(P,Q)]
        Z=[p[1]*q[1] for p,q in zip(P,Q)]
        observed=[2.75*w+0.125*z for w,z in zip(W,Z)]
        actual=dot(W,observed)/dot(W,W)
        theoretical=2.75+0.125*signed_error(W,Z)
        close(actual,theoretical)
        checks+=1
# Dense normal: sample linear least-squares identity.
for R in range(1,26):
    for rep in range(8):
        X=[RNG.gauss(0,1) for _ in range(R)]
        Z=[RNG.gauss(0,1) for _ in range(R)]
        observed=[-1.5*x+0.2*z for x,z in zip(X,Z)]
        close(dot(X,observed)/dot(X,X),-1.5+0.2*signed_error(X,Z))
        checks+=1
# Gamma moment identities: E(Z/chi_r)^2 = 1/(r-2).
for d in range(3,70):
    close(gamma_abs_ratio_moment(d,2),1/(d-2))
    checks+=1
# Two exact coefficients from product-normal polar asymptotics.
assert radially_symmetric_product_normal_norm_moment(2)==2
assert radially_symmetric_product_normal_norm_moment(4)==48
close(rowwise_log_tail_constant_even(2),1/math.pi)
close(rowwise_log_tail_constant_even(4),3/math.pi**2)
checks+=4
# Finite exact sums check the least-squares numerator variance conditional on W.
for R in range(1,8):
    W=[Fraction(j+2, j+3) for j in range(R)]
    # Independent Rademacher signs, with exact E[Z_i^2]=1.
    mean2=Fraction(0)
    for signs in product((-1,1), repeat=R):
        q=sum(w*z for w,z in zip(W,signs)) /sum(w*w for w in W)
        mean2+=q*q/Fraction(2**R)
    close(float(mean2), 1/float(sum(w*w for w in W)))
    checks+=1
print(f'VERIFY_OK checks={checks}; C2=1/pi; C4=3/pi^2; finite checks do not certify tails')
