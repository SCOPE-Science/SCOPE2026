#!/usr/bin/env python3
"""Exact finite verification of integer representations of odd centered powers."""
from math import gcd

EXPECTED = {(2, 2, 4, 1), (4, 2, 34, 1), (4, 3, 17, 4),
            (11, 2, 1093, 263), (13, 2, 51118, 503)}


def upper(k):
    assert k >= 2
    return max(k, (2**k - 2)//k)


def algorithm_modular(k):
    ans = []
    for m in range(2, upper(k)+1):
        X,Y,Z=m**k,(m+1)**k,(2*m+1)**k
        assert gcd(X,Y)==1
        v = (Z*pow(Y,-1,X))%X
        assert 0<=v<X
        if v*Y<=Z:
            u,rem=divmod(Z-v*Y,X)
            assert rem==0
            ans.append((k,m,u,v))
    return ans


def algorithm_congruences(k):
    ans=[]
    for m in range(2,upper(k)+1):
        X,Y,Z=m**k,(m+1)**k,(2*m+1)**k
        # Reduction modulo m and modulo m squared forces v=1+m*j, j=k (mod m).
        j_max=(2**k-2)//m
        j=k%m
        while j<=j_max:
            v=1+m*j
            R=Z-v*Y
            if R>=0 and R%X==0:
                ans.append((k,m,R//X,v))
            j+=m
    return ans


def verify_full():
    all_a=[];all_b=[]
    for k in range(2,21):
        a=algorithm_modular(k)
        b=algorithm_congruences(k)
        assert a==b,(k,a,b)
        all_a+=a; all_b+=b
    assert set(all_a)==EXPECTED
    assert len(all_a)==len(EXPECTED)
    for k,m,u,v in all_a:
        assert (2*m+1)**k==u*m**k+v*(m+1)**k
    print('PASS: exact independent algorithms agree on complete k=2..20 range')
    print('Per-exponent finite domains:')
    for k in range(2,21):
        print(k,upper(k)-1)
    print('Solutions:',sorted(all_a))

if __name__=='__main__': verify_full()
