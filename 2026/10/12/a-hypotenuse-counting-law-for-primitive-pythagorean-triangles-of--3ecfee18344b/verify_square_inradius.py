#!/usr/bin/env python3
"""Integer regression of square-inradius Pythagorean parameterization against Euclid enumeration."""
from math import gcd, isqrt, cos, sqrt, pi

def euclid_count(X):
    out=set()
    for m in range(2,isqrt(X)+1):
        for n in range(1,m):
            if m*m+n*n>X:break
            if ((m-n)%2==0 or gcd(m,n)>1):continue
            r=n*(m-n)
            if isqrt(r)**2==r:
                out.add((m*m-n*n,2*m*n,m*m+n*n))
    return out

def parameter_count(X):
    out=set()
    u=1
    while 2*u**4<=X:
        v=1
        while (u*u+v*v)**2+u**4<=X:
            if gcd(u,v)==1:
                m=u*u+v*v;n=u*u
                out.add((m*m-n*n,2*m*n,m*m+n*n))
            v+=2
        u+=1
    return out

def constant(n=100000):
    h=(pi/2)/n
    integrand=lambda t:1/sqrt(1+cos(t)**4)
    integral=h/3*(integrand(0)+integrand(pi/2)+4*sum(integrand(i*h) for i in range(1,n,2))+2*sum(integrand(i*h) for i in range(2,n,2)))
    return 2*integral/(pi*pi)

if __name__=='__main__':
    for bound in (100,1000,10000,100000,1000000,2000000):
        left=euclid_count(bound);right=parameter_count(bound)
        assert left==right,(bound,sorted(left-right)[:4],sorted(right-left)[:4])
        print(f'EXACT_MATCH X={bound} count={len(left)}')
    print('FIRST_10',sorted(parameter_count(1000000),key=lambda a:a[2])[:10])
    print(f'CONSTANT_APPROX {constant():.12f}')
    print('FINITE_CHECK_OK')
