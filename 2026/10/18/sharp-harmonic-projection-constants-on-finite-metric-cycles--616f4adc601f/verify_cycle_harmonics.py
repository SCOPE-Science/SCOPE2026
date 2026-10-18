"""Numerical cross-checks for real harmonic projections on finite metric cycles.

Scientific computation only: analytic proof establishes all dimensions.
Requires numpy and scipy.
"""
import math
import numpy as np
from scipy.optimize import linprog


def closed(m):
    assert m>=3
    if m%2:
        u=math.pi/(2*m)
        return (2/m)*(1/math.sin(u)-math.sin(u))
    if m%4==2:
        return 4/(m*math.sin(math.pi/m))
    return 4/(m*math.tan(math.pi/m))


def median_norm(m):
    a=np.cos(2*np.pi*np.arange(m)/m)
    return (2/m)*np.abs(a-np.median(a)).sum()


def linprog_norm(n,k):
    a=np.cos(2*np.pi*k*np.arange(n)/n)
    # Maximizing the pairing over all edge increments in [-1,1] with sum zero.
    result=linprog(-a, A_eq=np.ones((1,n)), b_eq=np.zeros(1),
                   bounds=[(-1,1)]*n, method='highs')
    assert result.success, (n,k,result.message)
    return -2*result.fun/n


def run():
    count=0
    cases=[]
    for m in range(3,2001):
        err=abs(median_norm(m)-closed(m))
        assert err<3e-11,(m,err,median_norm(m),closed(m))
        count+=1
    for n in range(3,65):
        for k in range(1,(n-1)//2+1):
            m=n//math.gcd(n,k)
            a=linprog_norm(n,k)
            b=closed(m)
            assert abs(a-b)<5e-10, (n,k,m,a,b)
            cases.append((n,k,m))
    assert abs(closed(3)-1)<1e-12
    assert abs(closed(4)-1)<1e-12
    assert all(closed(m)>1.000001 for m in range(5,2001))
    print('PASS',count,'exact-formula sample identities;',len(cases),'constrained linear programs')
    print('Examples',[(m,round(closed(m),12)) for m in range(3,13)])


if __name__=='__main__':
    run()
