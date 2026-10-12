#!/usr/bin/env python3
from fractions import Fraction
from math import gcd


def factor(n):
    out={}
    d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1
            n//=d
        d += 1
    if n>1: out[n]=out.get(n,0)+1
    return out


def sigma_int_s(n,s):
    # exact for integer s, including negative s
    ans=Fraction(1,1)
    for p,e in factor(n).items():
        ans *= sum((Fraction(p,1)**(j*s) for j in range(e+1)), Fraction(0,1))
    return ans


def check_case(s,a,b,c,d,N=1000):
    assert a*d==b*c
    assert c % a != 0
    assert gcd(c,d) % gcd(a,b) != 0
    for n in range(1,N+1):
        assert sigma_int_s(a*n+b,s) < sigma_int_s(c*n+d,s), (s,n)
    return N


def main():
    checks=0
    # s>0: u=2,v=3,q=6,r=1
    for s in (1,2,3):
        checks += check_case(s,12,2,18,3)
    # s<0: u=3,v=2,q=6,r=1
    for s in (-1,-2,-3):
        checks += check_case(s,18,3,12,2)
    # s=0: u=2,v=9,q=18,r=1
    checks += check_case(0,36,2,162,9)

    # exact algebraic side-conditions for the three templates
    templates=[(2,3,6,1),(3,2,6,1),(2,9,18,1)]
    for u,v,q,r in templates:
        assert gcd(r,u*v)==1
        for p in factor(u*v):
            assert q % p == 0
        a,b,c,d=u*q,u*r,v*q,v*r
        assert a*d==b*c
        assert (c % a)!=0
        assert gcd(a,b)==u*gcd(q,r)
        assert gcd(c,d)==v*gcd(q,r)
        assert gcd(c,d)%gcd(a,b)!=0
        checks += 8

    print('VERIFY_OK')
    print('exact_progression_inequality_checks='+str(7*1000))
    print('algebraic_template_checks='+str(3*8))
    print('total_assertion_groups='+str(checks))

if __name__=='__main__':
    main()
