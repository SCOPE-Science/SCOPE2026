#!/usr/bin/env python3
"""Numerical checks of the conformal-matrix invariant reduction.

Dependencies: Python 3 standard library. This is supplementary to the
analytic proof and does not certify all-time asymptotics.
"""
import math


def deriv(y, n, c):
    a, b, t = y
    r2 = a*a+b*b
    return (-n*(a-1.)+c*a/r2, c*b/r2, r2**(-1.+1./n))


def rk4(y, h, n, c):
    p = deriv(y,n,c)
    q = deriv(tuple(z + .5*h*v for z,v in zip(y,p)),n,c)
    r = deriv(tuple(z + .5*h*v for z,v in zip(y,q)),n,c)
    s = deriv(tuple(z + h*v for z,v in zip(y,r)),n,c)
    return tuple(z+h*(pv+2*qv+2*rv+sv)/6 for z,pv,qv,rv,sv in zip(y,p,q,r,s))


def test_case(d,n,beta,seed):
    assert d % 2 == 0 and d>=2 and n>=2
    c=(n-1)*(d-1)/(2*beta)
    a,b,t=1.,seed,0.
    h=.025
    steps=120000
    aa=(1+math.sqrt(1+4*c/n))/2
    checked=0
    for iteration in range(steps):
        a,b,t=rk4((a,b,t),h,n,c)
        assert 1.-1.e-10<=a<=aa+1.e-10, (d,n,iteration,a,aa)
        assert (b*seed)>0 and abs(b)>=abs(seed)
        checked+=2
    r=math.hypot(a,b)
    k=b*b*(a-1.)
    q=abs(b)**(2./n)/(2*c*t/n)
    assert abs(k/(c/n)-1)<.04, (d,n,beta,k,c/n)
    assert abs(q-1)<.15, (d,n,beta,q)
    assert (d/2)*(a-1.)**2<.001
    return checked+3, (d,n,beta,round(a,9),round(abs(b),6),round(t,6),round(k/(c/n),8),round(q,8))


def test_geometry():
    # Explicit orthogonal, skew-symmetric J in every even dimension.
    assert all(((-1)**2==1 for _ in range(10)))
    count=0
    for d in (2,4,6,8):
        J=[[0 for _ in range(d)] for _ in range(d)]
        for k in range(0,d,2):
            J[k][k+1]=-1
            J[k+1][k]=1
        for i in range(d):
            for j in range(d):
                assert J[i][j]==-J[j][i]
                z=sum(J[i][k]*J[k][j] for k in range(d))
                assert z==(-1 if i==j else 0)
                count+=2
        for a,b in ((1,2),(2,-3),(.1,.4)):
            W=[[a*(i==j)+b*J[i][j] for j in range(d)] for i in range(d)]
            for i in range(d):
                for j in range(d):
                    z=sum(W[i][k]*W[j][k] for k in range(d))
                    assert abs(z-(a*a+b*b)*(i==j))<1e-11
                    count+=1
    return count


def test_entropy_derivatives():
    # Along the isosingular plane the *original* pairwise entropy quotient
    # approaches the stated repeated-singular-value continuation.
    count=0
    for n in (2,3,4,6):
        for r in (0.4,1.0,3.0,13.0):
            e=1.e-6
            s1=r*(1+e); s2=r
            original=.5*math.log((s1*s1-s2*s2)/(s1**(2/n)-s2**(2/n)))
            limit=.5*math.log(n)+(1.-1./n)*math.log(r)
            assert abs(original-limit)<4.e-6, (n,r,original,limit)
            count+=1
    return count

if __name__=='__main__':
    checks=test_geometry()+test_entropy_derivatives()
    for case in ((2,2,1.,1.),(4,3,2.,-2.),(6,5,3.,.75)):
        nchecks, obs=test_case(*case)
        checks+=nchecks
        print('CASE',obs)
    print('VERIFY_OK: checks=',checks)
