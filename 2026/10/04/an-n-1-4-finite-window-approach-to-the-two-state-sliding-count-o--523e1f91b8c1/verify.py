#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import math


def coeff_path(path, r):
    """Coefficient of u in the stationary path probability as u -> 0."""
    s = 1-r
    entrances=sum(1 for a,b in zip(path,path[1:]) if a==0 and b==1)
    exits=sum(1 for a,b in zip(path,path[1:]) if a==1 and b==0)
    stays1=sum(1 for a,b in zip(path,path[1:]) if a==1 and b==1)
    if path[0]==0:
        if entrances != 1:
            return Fraction(0)
        return (s**stays1)*(r**exits)
    else:
        if entrances != 0:
            return Fraction(0)
        return Fraction(1,1)/r * (s**stays1)*(r**exits)


def enumerate_coeffs(n, r):
    pk=[Fraction(0) for _ in range(n+1)]
    for path in product((0,1), repeat=n):
        k=sum(path)
        if k:
            pk[k]+=coeff_path(path,r)
    ck=[Fraction(0) for _ in range(n)]
    for path in product((0,1), repeat=n+1):
        k0=sum(path[:n]); k1=sum(path[1:])
        if k1==k0+1:
            ck[k0]+=coeff_path(path,r)
    return pk, ck


def closed_coeffs(n,r):
    s=1-r
    pk=[Fraction(0) for _ in range(n+1)]
    for k in range(1,n):
        pk[k]=s**(k-1)*(2+(n-k-1)*r)
    pk[n]=s**(n-1)/r
    ck=[s**k for k in range(n)]
    return pk,ck


def check_exact():
    r=Fraction(2,5)
    x=Fraction(7,6)
    s=1-r
    for n in range(2,8):
        pk,ck=enumerate_coeffs(n,r)
        p2,c2=closed_coeffs(n,r)
        assert pk==p2, (n,pk,p2)
        assert ck==c2, (n,ck,c2)
        D=sum(ck[k]*((x if k==0 else x**(k+1)-x**k)**2) for k in range(n))
        M=sum(pk[k]*x**(2*k) for k in range(1,n+1))
        y=s*x*x
        D2=x*x+(x-1)**2*sum(y**k for k in range(1,n))
        M2=x*x*(sum((2+(n-j-2)*r)*y**j for j in range(n-1)) + y**(n-1)/r)
        assert D==D2, (n,D,D2)
        assert M==M2, (n,M,M2)


def rare_quotient(n,A=math.sqrt(2.0),B=1/math.sqrt(2.0)):
    h=n**(-0.25)
    rho=1-A*h
    eps=B*n**(-0.75)
    r=1-rho*rho
    x=(1-eps)/rho
    y=(1-eps)**2
    yn1=math.exp((n-1)*math.log(y))
    yn=yn1*y
    A0=(1-yn1)/(1-y)
    A1=(y-(n-1)*yn1+(n-2)*yn)/((1-y)**2)
    D=x*x+(x-1)**2*y*(1-yn1)/(1-y)
    M=x*x*(2*A0+r*((n-2)*A0-A1)+yn1/r)
    return n*D/(r*M)


def check_asymptotic():
    target=1/math.sqrt(2.0)
    ns=[10_000,100_000,1_000_000,10_000_000]
    vals=[]
    second=[]
    for n in ns:
        h=n**(-0.25)
        R=rare_quotient(n)
        vals.append((R-0.25)/h)
        second.append((R-0.25-target*h)/(h*h))
    assert all(vals[i+1] < vals[i] for i in range(len(vals)-1))
    assert abs(vals[-1]-target) < 0.02
    assert abs(second[-1]-0.875) < 0.03
    # Analytic minimizer checks for C(A,B).
    A=math.sqrt(2.0); B=1/math.sqrt(2.0)
    C=A/4+1/(8*B)+B/(2*A*A)
    assert abs(C-target) < 1e-14
    assert abs(B-A/2) < 1e-14


if __name__=='__main__':
    check_exact()
    check_asymptotic()
    print('VERIFY_OK')
