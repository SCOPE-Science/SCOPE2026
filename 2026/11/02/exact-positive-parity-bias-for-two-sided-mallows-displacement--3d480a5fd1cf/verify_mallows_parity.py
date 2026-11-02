#!/usr/bin/env python3
"""Finite exact q-series and numerical checks for the Mallows parity identity.

All computations are corroboration; the proof for every 0<t<1 uses
absolute convergence and two instances of the q-binomial theorem.
"""
import math
from fractions import Fraction


def series_inverse_qfactorials(N):
    # P_r(z) = prod_{k=1}^r(1-z^k)^(-1), truncated after z^N.
    allp = [[1] + [0] * N]
    for r in range(1, N+1):
        p = allp[-1][:]
        for j in range(r, N+1):
            p[j] += p[j-r]
        allp.append(p)
    return allp


def convolution(a, b, N):
    c = [0] * (N+1)
    for i, u in enumerate(a[:N+1]):
        if u:
            for j, v in enumerate(b[:N+1-i]):
                if v:
                    c[i+j] += u*v
    return c


def exact_series_check(N=16):
    pinv = series_inverse_qfactorials(N)
    lhs = [0]*(N+1)
    for r in range(N+1):
        for ell in range(N+1):
            offset = r*ell+r+ell
            if offset > N:
                continue
            product = convolution(pinv[r], pinv[ell], N-offset)
            sign = -1 if (r+ell)%2 else 1
            for j in range(N-offset+1):
                lhs[offset+j] += sign*product[j]

    rhs = [1]+[0]*N
    for k in range(1,N+1):
        # Coefficients of ((1-z^k)/(1+z^k))^2.
        fac = [0]*(N+1)
        fac[0] = 1
        # Identity 1 -4 z^k/(1+z^k)^2.
        for j in range(1,N//k+1):
            fac[j*k] = 4*j*((-1)**j)
        rhs = convolution(rhs,fac,N)
    # The double sum is unnormalized. Multiply by (1-z)(z;z)_infinity.
    norm = [1]+[0]*N
    for k in range(1,N+1):
        fac=[1]+[0]*N
        fac[k]=-1
        norm=convolution(norm,fac,N)
    fac=[1]+[0]*N
    fac[1]=-1
    norm=convolution(norm,fac,N)
    lhs_normalized=convolution(lhs,norm,N)
    assert lhs_normalized == rhs,(lhs_normalized,rhs)
    print('FORMAL_COEFFICIENTS_EXACT',N+1)
    print('COEFF_PREFIX',lhs_normalized[:12])


def finite_q_independent_check(t):
    # An independently summed, rapidly-convergent conditional representation.
    eps=1e-30
    K=20
    while t**K>eps:
        K*=2
    K+=20
    prod_positive=1.0
    prod_negative=1.0
    for k in range(1,K+1):
        prod_positive *= (1-t**k)
        prod_negative *= (1+t**k)
    target=(prod_positive/prod_negative)**2
    # Probability of right-inversion count r is (1-t)*t^r.
    # Conditional parity of left-inversion count is prod_{k=r+1}^inf
    # (1-t^k)/(1+t^k). Evaluate by backward product.
    ratio_tail=1.0
    total=0.0
    terms=[]
    for r in range(K,-1,-1):
        ratio_tail *= (1-t**(r+1))/(1+t**(r+1))
        terms.append((r,ratio_tail))
    for r,ratio in terms:
        total += (1-t)*((-t)**r)*ratio
    assert abs(total-target)<max(3e-13,abs(target)*1e-8),(t,total,target)
    print('NUMERIC',t,'signed_moment',f'{total:.16g}',
          'product',f'{target:.16g}', 'abs_diff',f'{abs(total-target):.2g}')


def strict_order_check():
    ts=[0.1,0.2,0.35,0.5,0.6,0.7,0.8]
    vals=[]
    for t in ts:
        p=1.0
        for k in range(1,350):
            p*=((1-t**k)/(1+t**k))**2
        vals.append(p)
    assert all(vals[j] > vals[j+1] for j in range(len(vals)-1))
    assert all(0<v<1 for v in vals)
    print('MONOTONE_PRODUCT_GRID',len(vals))


if __name__=='__main__':
    exact_series_check(18)
    for t in (0.1,0.25,0.35,0.5,0.6,0.8):
        finite_q_independent_check(t)
    strict_order_check()
    print('CHECKS_PASSED')
