"""Exact-rational checks for asynchronous closed-neighborhood averaging on stars.
Standard library only: python verification.py
All calculations use fractions, never floating-point approximations.
"""
from fractions import Fraction as Q
from itertools import product


def updates(x):
    m = len(x)-1
    center, *leaves = x
    yield (sum(x, Q(0))/Q(m+1), *leaves)
    for i in range(m):
        y=list(x)
        y[i+1]=(y[i+1]+center)/2
        yield tuple(y)


def coefficients(m):
    w=3*m+1
    return Q(1,(2*m+1)*w),Q(m-1,(2*m+1)*w*w)


def moments(x):
    m=len(x)-1
    d=[v-x[0] for v in x[1:]]
    E=sum((a*a for a in d),Q(0)); T=sum(d,Q(0))**2
    M=((m+1)*x[0]+2*sum(x[1:],Q(0)))/Q(3*m+1)
    a,b=coefficients(m)
    return M,E,T,M*M+a*E+b*T


def checks():
    count=0
    for m in range(1,9):
        n=m+1; w=3*m+1
        for seed in range(14):
            x=tuple(Q(((i+1)*(3*seed+5)+i*i) % 19,seed+2) for i in range(n))
            if seed==0: x=(Q(0),)+tuple(Q(1) for _ in range(m))
            M,E,T,K=moments(x)
            ys=list(updates(x))
            assert len(ys)==n
            assert sum((moments(y)[0] for y in ys),Q(0))/n==M
            assert sum((moments(y)[3] for y in ys),Q(0))/n==K
            e_expected=(1-Q(3,4*n))*E-Q(m+2,n*(m+1)**2)*T
            t_expected=Q(1,4*n)*E+Q(m-1+Q(1,(m+1)**2),n)*T
            assert sum((moments(y)[1] for y in ys),Q(0))/n==e_expected
            assert sum((moments(y)[2] for y in ys),Q(0))/n==t_expected
            a,b=coefficients(m)
            assert a*E+b*T==Q(E,(2*m+1)*w)+Q(m-1,(2*m+1)*w*w)*T
            assert e_expected<=E
            count+=6
    # Two-node process is random unbiased binary expansion; exact limit variance given by the squared difference divided by 12.
    assert coefficients(1)==(Q(1,12),Q(0)); count+=1
    for m in range(1,200):
        a,b=coefficients(m)
        # Initial center 0, all leaf opinions 1.
        var=a*m+b*m*m
        assert var==Q(m*(m+1)**2, (2*m+1)*(3*m+1)**2)
        assert var>0
        count+=1
    return count

if __name__=='__main__':
    print('PASS exact rational assertions:',checks())
