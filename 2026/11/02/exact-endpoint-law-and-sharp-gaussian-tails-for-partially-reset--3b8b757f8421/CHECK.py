#!/usr/bin/env python3
"""Independent exact-arithmetic moment and endpoint-constant checks.
Run: python3 partial_ou_tail_checker.py
"""
from fractions import Fraction as F
from math import comb, factorial, gamma, isfinite

def beta_mixed(theta, j, ell):
    out = theta * F(factorial(ell),1)
    for r in range(ell + 1):
        out /= theta + j + r
    return out

def test(kappa, diffusion, rho, c, degree=8):
    theta = rho/(2*kappa)
    z = [F(1)]
    for k in range(1, degree+1):
        numerator = sum(F(comb(k,j))*c**(2*j)*beta_mixed(theta,j,k-j)*z[j] for j in range(k))
        denominator = 1-c**(2*k)*beta_mixed(theta,k,0)
        z.append(numerator/denominator)
    moment = F(1)
    vbar = diffusion/kappa
    for k in range(1, degree+1):
        moment *= F(2*kappa*k,1)/(2*kappa*k+rho*(1-c**(2*k)))
        assert z[k] == moment, (k,kappa,rho,c)
        gauss_moment = F(factorial(2*k),2**k*factorial(k))*vbar**k*z[k]
        generator_moment = F(factorial(2*k),1)*diffusion**k
        for j in range(1,k+1):
            generator_moment /= 2*kappa*j+rho*(1-c**(2*j))
        assert gauss_moment == generator_moment
    return 2*degree, theta, z

checks=0
configs=[(F(1),F(1),F(1),F(1,2)),(F(3,2),F(5,3),F(2),F(2,3)),(F(1,4),F(7,2),F(3,5),F(3,4)),(F(5),F(1,7),F(13,4),F(1,10)),(F(7,3),F(3),F(1,5),F(4,5))]
for conf in configs:
    n,theta,z=test(*conf)
    checks+=n
    # Positive, geometrically convergent binomial expansion for the endpoint constant.
    kappa,D,rho,c=conf
    vbar=D/kappa
    C_low=float(vbar**(-theta)); C_up=float((vbar*(1-c*c))**(-theta))
    sm=0.0
    rise=1.0
    for k,m in enumerate(z):
        if k: rise*=float(theta+k-1)/k
        assert rise > 0 and m > 0 and c**(2*k) >= 0
        sm+=rise*float(c**(2*k)*m)
        checks+=1
    partial=C_low*sm
    assert C_low<=partial<=C_up
    checks+=1
    print('case',*(str(x) for x in conf),'theta',float(theta),'endpoint_const_truncated',repr(partial),'rigorous_lower',repr(C_low),'rigorous_upper',repr(C_up))
print('PASSED exact recursions / Gaussian moments / endpoint bound:',checks,'assertions')
