#!/usr/bin/env python3
"""Exact formal-power-series checks for an overcubic tuple congruence."""
from math import isqrt


def theta_product(N):
    f=[0]*(N+1)
    g=[0]*(N+1)
    f[0]=g[0]=1
    for j in range(1,isqrt(N)+1):
        f[j*j]+=2*(-1)**j
    for j in range(1,isqrt(N//2)+1):
        g[2*j*j]+=2*(-1)**j
    return mul(f,g,N)


def mul(a,b,N,mod=None):
    c=[0]*(N+1)
    for i,ai in enumerate(a[:N+1]):
        if not ai:continue
        for j,bj in enumerate(b[:N+1-i]):
            if bj:c[i+j]+=ai*bj
    if mod:
        c=[v%mod for v in c]
    return c


def inv(a,N):
    assert a[0]==1
    b=[1]+[0]*N
    for n in range(1,N+1):
        b[n]=-sum(a[k]*b[n-k] for k in range(1,n+1))
    return b


def power(a,e,N,mod=None):
    r=[1]+[0]*N
    b=[v%mod for v in a] if mod else a[:]
    while e:
        if e&1:r=mul(r,b,N,mod)
        e//=2
        if e:b=mul(b,b,N,mod)
    return r


def independent_product(N):
    """Truncated Euler product: F=prod (1-z^(4j))/(1-z^j)^2/(1-z^(2j))."""
    b=[1]+[0]*N
    for j in range(1,N+1):
        for _ in range(2):
            for n in range(j,N+1): b[n]+=b[n-j]
        if 2*j<=N:
            for n in range(2*j,N+1): b[n]+=b[n-2*j]
        if 4*j<=N:
            for n in range(N,4*j-1,-1):b[n]-=b[n-4*j]
    return b


def main():
    N=191
    A=theta_product(N)
    F=inv(A,N)
    assert F==independent_product(N)
    F3=power(F,3,N)
    assert (F3[5],F3[7]) == (1248,9792)
    F4=power(F,4,N)
    assert all(x%8==0 for x in F4[1:])
    C=[(F4[0]-1)//8]+[x//8 for x in F4[1:]]
    CC=mul(C,C,N)
    ACC=mul(A,CC,N)
    assert ACC[5]==360 and ACC[7]==7424
    assert all(ACC[j]%2==0 for j in range(1,N+1,2))
    assert all(A[j]==0 for j in range(N+1) if j%8 in (5,7))
    tests=0
    for i in range(3,8):
        mod=1<<(i+4)
        for k in range(4):
            t=(1<<(i-3))*(2*k+1)
            M=4*t-1
            BM=power(F,M,N,mod)
            for n in range(1,N+1,2):
                assert (BM[n]-((1-t)*A[n]+t*F3[n])) % (1<<(i+3)) == 0,(i,k,n)
                tests+=1
            for n in range(N+1):
                if n%8==5:
                    assert BM[n]%(1<<(i+2))==0,(i,k,n)
                if n%8==7:
                    assert BM[n]%(1<<(i+3))==0,(i,k,n)
            assert BM[5]%(1<<(i+3)) == (1<<(i+2)),(i,k)
            assert BM[7]%(1<<(i+4)) == (1<<(i+3)),(i,k,BM[7])
    print(f'VERIFY_OK exact_integer_checks={tests} i=3..7 k=0..3 N={N} sharp_both=True')

if __name__=='__main__':main()
