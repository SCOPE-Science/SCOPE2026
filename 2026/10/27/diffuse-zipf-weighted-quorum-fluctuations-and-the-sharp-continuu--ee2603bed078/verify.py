#!/usr/bin/env python3
"""Independent finite-population/quadrature checks of the diffuse Zipf quorum formulas."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from mpmath import zeta


def continuum(s, theta):
    b = 1.0 - s
    def f(u):
        # 1 - integral is numerically stable because exp suppresses x->0.
        val = quad(lambda x: b*x**(-s)*math.exp(-u*b*x**(-s)),
                   0.0, 1.0, epsabs=1e-11, limit=300)[0]
        return 1.0-val
    u = brentq(lambda u: f(u)-theta, 1e-8, 100.)
    D = quad(lambda x: b*b*x**(-2*s)*math.exp(-u*b*x**(-s)),
             0, 1, epsabs=1e-11, limit=300)[0]
    V = quad(lambda x: b*b*x**(-2*s)*math.exp(-u*b*x**(-s))
             *(-math.expm1(-u*b*x**(-s))),
             0, 1, epsabs=1e-11, limit=300)[0]
    delta = -(b*float(zeta(s))*(1-theta-u*D))/D
    return u,D,V,delta


def finite(s,theta,N):
    i=np.arange(1,N+1,dtype=np.float64)
    q=i**(-s)
    q=q/q.sum()
    a=N*q
    def mean(u):
        return float(np.dot(q,-np.expm1(-u*a)))
    u=brentq(lambda u:mean(u)-theta,1e-10,100.)
    p=-np.expm1(-u*a)
    D=float(np.dot(q,a*np.exp(-u*a)))
    V=float(N*np.dot(q*q, p*(1-p)))
    # Exact algebraic expressions for independent indicators.
    assert abs(mean(u)-theta)<2e-10
    assert V>0 and D>0
    return u,D,V


def main():
    checks=0
    for s,theta in [(.25,.5),(.5,.5),(.75,.5),(.75,.9)]:
        u,D,V,delta=continuum(s,theta)
        assert D>0 and V>0
        data=[]
        for N in [5000,20000,80000]:
            un,Dn,Vn=finite(s,theta,N)
            data.append((N,(un-u)*N**(1-s),Dn,Vn))
            assert abs(Dn-D)<0.09 and abs(Vn-V)<0.09
            checks+=3
        # Leading deterministic displacement: residual at largest N is
        # closer than at smallest N in these displayed regimes.
        assert abs(data[-1][1]-delta)<abs(data[0][1]-delta), (s,theta,data,delta)
        checks+=1
        print(f's={s:.2f} theta={theta:.2f} u={u:.8f} '
              f'D={D:.8f} V={V:.8f} delta={delta:.8f}; '
              f'finite shift={data[-1][1]:.8f}')
    print(f'PASS: {checks} numerical algebraic/asymptotic consistency assertions.')

if __name__=='__main__':
    main()
