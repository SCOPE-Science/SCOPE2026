#!/usr/bin/env python3
"""Finite, independent enumeration for power-of-two-support reflection complexity.

The infinite claim is established by the separate gap-counting proof. Here
factors are actually enumerated from a provably sufficient finite prefix.
"""

def prefix(n, leading_zero):
    # For each n, this contains the first pair of 1s at every gap <= n,
    # plus enough zero padding to witness 0^n and all single-1 factors.
    power=1
    while power < 4*n:
        power *= 2
    length=power+n+8
    word=bytearray(b'0'*length)
    j=1
    while j < length:
        word[j]=49
        j*=2
    return bytes(word) if leading_zero else bytes(word[1:])


def expected_reflection(n, leading_zero):
    if n==0:return 1
    if n==1:return 2
    if n==2:return 3
    if n==3:return 5
    return 2*((n+1)//2)+(2 if leading_zero else 1)


def expected_factors(n, leading_zero):
    if n==0:return 1
    if n==1:return 2
    if n==2:return 4
    if n==3:return 7 if leading_zero else 6
    B=1 << (n.bit_length()-1)
    return n+B//2+1+min(B//2,n-B)+(1 if leading_zero else 0)


def dyadic_Q(d,n):
    h=d//2
    if n<=d:return 0
    N=min(h,n-d)
    t=n-d-1
    lo=max(0,t-h+1)
    hi=min(h-1,t)
    S=max(0,hi-lo+1)
    Q=N-S//2
    assert Q==min(h,max(0,(n-d+1)//2)),(d,n,N,S,Q)
    return Q


def brute(n,leading_zero):
    w=prefix(n,leading_zero)
    factors={w[i:i+n] for i in range(len(w)-n+1)}
    return len({min(f,f[::-1]) for f in factors}),len(factors)


def main():
    lengths=list(range(1,181))+[191,199,255,256,257,319,383,511,512,513,767,1023,1024,1025]
    count=0
    for n in lengths:
        for leading_zero in (False,True):
            observed=brute(n,leading_zero)
            expected=(expected_reflection(n,leading_zero),expected_factors(n,leading_zero))
            assert observed==expected,(n,leading_zero,observed,expected)
            if n>=2:
                d=2
                multi=1 if not leading_zero or n in (2,3) else 2
                while d<n:
                    multi+=dyadic_Q(d,n)
                    d*=2
                assert observed[0]==1+(n+1)//2+multi,(n,leading_zero,multi)
            count+=1
    for n in range(4,65537):
        d=2
        total=0
        while d<n:
            total+=dyadic_Q(d,n)
            d*=2
        assert total==(n+1)//2-1,(n,total)
    print(f'VERIFY_OK actual_factor_and_reflection_enumerations={count} dyadic_identity_lengths=65533 maximum_length={max(lengths)}')

if __name__=='__main__':
    main()
