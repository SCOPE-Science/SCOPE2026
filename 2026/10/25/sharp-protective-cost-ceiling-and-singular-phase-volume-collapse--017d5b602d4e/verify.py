#!/usr/bin/env python3
"""Exact-rational and numerical spot checks for a quorum-protection payoff theorem.
All mathematical statements and assumptions are documented in RESULT.md.
No network access or third-party dependencies are required.
"""
from fractions import Fraction as F
from math import comb, sqrt, gamma


def pivotal_sum(n, a, x, z, rho):
    b = n - a
    y = 1 - x - z
    return comb(n, a)*z**a*sum(comb(b,j)*y**j*x**(b-j)*(1-rho**j) for j in range(b+1))


def pivotal_closed(n, a, x, z, rho):
    b = n - a
    return comb(n,a)*z**a*((1-z)**b-(rho*(1-z)+(1-rho)*x)**b)


def max_closed(n,a,rho):
    b=n-a
    return (1-rho**b)*F(comb(n,a))*F(a,n)**a*F(b,n)**b


def area(n, a, rho, eps, subdivisions=3000):
    # Exact 1-D profile: for each z near its binomial maximum, determine the
    # largest x with pivotal(x,z) above the desired threshold by bisection.
    b=n-a
    m=float(max_closed(n,a,F(str(rho))))
    z0=a/n
    threshold=(1-eps)*m
    def peak(z):
        return pivotal_closed(n,a,0.0,z,rho)
    def xwidth(z):
        if z<=0 or z>=1 or peak(z)<=threshold:
            return 0.0
        lo=0.0; hi=1.0-z
        for _ in range(58):
            mid=(lo+hi)/2
            if pivotal_closed(n,a,mid,z,rho)>threshold:
                lo=mid
            else:
                hi=mid
        return (lo+hi)/2
    # Bracket the two intersections of x=0 boundary with the level set.
    lo=0.0; hi=z0
    for _ in range(65):
        mid=(lo+hi)/2
        if peak(mid)>threshold: hi=mid
        else: lo=mid
    zl=(lo+hi)/2
    lo=z0; hi=1.0
    for _ in range(65):
        mid=(lo+hi)/2
        if peak(mid)>threshold: lo=mid
        else: hi=mid
    zr=(lo+hi)/2
    steps=subdivisions + subdivisions%2
    h=(zr-zl)/steps
    s=xwidth(zl)+xwidth(zr)
    for j in range(1,steps):
        s+=(4 if j%2 else 2)*xwidth(zl+h*j)
    return h*s/3


def predicted(n,a,rho,eps):
    b=n-a
    D=n**3/(2*a*b)
    if rho>0:
        H=n*(1-rho)*rho**(b-1)/(1-rho**b)
        return 4/(3*H*sqrt(D))*eps**1.5
    B=gamma(.5)*gamma(1+1/b)/gamma(1.5+1/b)
    return b/(n*sqrt(D))*B*eps**(.5+1/b)


def main():
    cnt=0
    for n in range(2,8):
        for a in range(1,n):
            for rho in (F(0),F(1,3),F(1,2),F(2,3)):
                maxv=max_closed(n,a,rho)
                assert pivotal_closed(n,a,F(0),F(a,n),rho)==maxv
                cnt+=1
                for sx in range(0,9):
                    for sz in range(0,9-sx):
                        x=F(sx,8); z=F(sz,8)
                        lhs=pivotal_sum(n,a,x,z,rho)
                        rhs=pivotal_closed(n,a,x,z,rho)
                        assert lhs==rhs, (n,a,x,z,rho,lhs,rhs)
                        assert 0<=rhs<=maxv, (n,a,x,z,rho,rhs,maxv)
                        cnt+=2
    reports=[]
    for n,a,rho in [(2,1,.5),(2,1,0.),(4,2,.5),(4,2,0.),(5,2,.5),(5,2,0.),(8,3,.5),(8,3,0.)]:
        eps=.001
        observed=area(n,a,rho,eps)
        expected=predicted(n,a,rho,eps)
        ratio=observed/expected
        assert abs(ratio-1)<.02, (n,a,rho,ratio)
        reports.append((n,a,rho,round(ratio,6)))
    print('Exact-rational pivotality and upper-bound assertions:',cnt)
    print('Numerical small-epsilon area ratio observations:',reports)
    print('All finite checks passed; they are not proofs of infinite assertions.')

if __name__=='__main__':
    main()
