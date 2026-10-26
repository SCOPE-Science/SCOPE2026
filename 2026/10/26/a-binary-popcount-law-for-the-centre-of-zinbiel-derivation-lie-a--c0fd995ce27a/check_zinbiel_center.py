#!/usr/bin/env python3
"""Reproducible finite checks for a characteristic-dependent Zinbiel derivation-centre theorem.
These tests support, but do not replace, the integral identities and Lucas argument.
"""
from math import comb


def coef(i,j):
    return comb(i+j-1,j)


def deriv(h,m):
    return comb(m+h-1,m-1)


def bracket(i,j,p):
    return (comb(i+j-1,j-1)-comb(i+j-1,i-1)) % p


def nu2(x):
    r=0
    while x%2 == 0:
        r+=1
        x//=2
    return r


def expected(n,p):
    if p!=2:
        return [n] if n%p==1 else []
    return [i for i in range(1,n+1,2)
            if n<= i+(1<<nu2(i+1))-2]


def actual(n,p):
    return [i for i in range(1,n+1)
            if all(bracket(i,j,p)==0 for j in range(1,n-i+2))]


def check():
    # Integral Zinbiel relation: (a*b)*c=a*(b*c+c*b).
    for a in range(1,18):
        for b in range(1,18):
            for c in range(1,18):
                assert coef(a,b)*coef(a+b,c)==(coef(b,c)+coef(c,b))*coef(a,b+c)
    # Integral derivation identity, for every homogeneous D_h.
    for a in range(1,19):
        for b in range(1,19):
            for h in range(1,19):
                left=coef(a,b)*deriv(h,a+b)
                right=deriv(h,a)*coef(a+h-1,b)+deriv(h,b)*coef(a,b+h-1)
                assert left==right,(a,b,h)
    # Commutator coefficient via its value on the generator;
    # explicit matrix commutators for every finite basis vector.
    for n in range(2,15):
        for p in (2,3,5):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    for m in range(1,n+1):
                        out=m+i+j-2
                        if out>n:continue
                        d1=deriv(j,m)*deriv(i,m+j-1)
                        d2=deriv(i,m)*deriv(j,m+i-1)
                        expected_coeff=(bracket(i,j,p)*deriv(i+j-1,m))%p
                        assert (d1-d2)%p==expected_coeff,(n,p,i,j,m)
    # Direct centre of the full derivation algebra for small and medium sizes.
    tested=0
    for p,limit in ((2,150),(3,70),(5,55),(7,50),(11,40)):
        for n in range(2,limit+1):
            a=actual(n,p)
            e=expected(n,p)
            assert a==e,(p,n,a,e)
            if p==2:
                t=nu2(n+2)
                bitcount=((n+1)>>(t+1)).bit_count()
                assert len(a)==bitcount,(n,a,bitcount)
            tested+=1
    assert expected(13,2)==[7,11,13]
    assert expected(29,2)==[15,23,27,29]
    print('ZINBIEL_CENTRE_OK', 'test_size_pairs=',tested)

if __name__=='__main__':
    check()
