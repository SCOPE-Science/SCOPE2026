#!/usr/bin/env python3
"""Finite quadrature and symbolic-identity cross-checks for a planar curvature Hessian.
Only checks finite cases; the accompanying analytic proof establishes the theorem.
"""
import math

def f(y, R):
    assert 0 < y < R
    return (y*y*(1-y/R))**(1/3)

def derivatives(r, R):
    v=f(r,R)
    L=(2*R-3*r)/(3*r*(R-r))
    second=-2*R*R*v/(9*r*r*(R-r)**2)
    return v, v*L, second

def coef(r,R,k):
    v,fp,fpp=derivatives(r,R)
    return (-fpp-fp/(r*(k*k-1)))/2

def measured(r,R,k,e,N=8192):
    s=r/math.sqrt(r*r+(e*e/2)*(1-k*k))
    integ=0.0
    for i in range(N):
        theta=2*math.pi*(i+.5)/N
        rho=s*(r+e*(1-k*k)*math.cos(k*theta))
        assert 0 < rho < R
        integ += f(rho,R)
    integ *= 2*math.pi/N
    return (2*math.pi*f(r,R)-integ)/(e*e*math.pi*(k*k-1)**2)

def main():
    for r in (0.4,2/3,0.85):
        for k in (2,3,6):
            expected=coef(r,1.0,k)
            got=measured(r,1.0,k,4e-5)
            assert math.isclose(got,expected,rel_tol=4e-4,abs_tol=2e-7),(r,k,got,expected)
        a=[coef(r,1.0,k) for k in range(2,20)]
        if r<2/3:assert all(a[j]<a[j+1] for j in range(len(a)-1))
        elif r>2/3:assert all(a[j]>a[j+1] for j in range(len(a)-1))
        else:assert max(a)-min(a)<1e-12
    for r in (.2,.4,.65,.75,.85):
        v,fp,fpp=derivatives(r,1.0)
        assert abs(fpp + 2*v/(9*r*r*(1-r)**2))<1e-11
        assert coef(r,1.0,2)>0
    print('RELATIVE_AFFINE_HESSIAN_FINITE_CHECKS_OK')
if __name__=='__main__':main()
