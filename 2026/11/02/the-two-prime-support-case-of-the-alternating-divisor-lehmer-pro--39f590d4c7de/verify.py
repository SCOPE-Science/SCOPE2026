"""Reproducible arithmetic checks for a two-prime-support alternating-divisor theorem.

Independent of the proof: computes beta by divisor convolution, and separately
by prime-power products. Checks all integers in a prescribed finite interval
and several parameter identities. No finite check is used as an infinite proof.
"""
import math

def beta_convolution_all(N):
    # beta(n) = sum_{d|n} d * Liouville(n/d).
    spf=list(range(N+1))
    for p in range(2,math.isqrt(N)+1):
        if spf[p]==p:
            for j in range(p*p,N+1,p):
                if spf[j]==j:spf[j]=p
    lam=[1]*(N+1)
    omega=[0]*(N+1)
    for n in range(2,N+1):
        p=spf[n]
        lam[n]=-lam[n//p]
        omega[n]=omega[n//p] + (1 if (n//p)%p else 0)
    out=[0]*(N+1)
    for d in range(1,N+1):
        for j in range(1,N//d+1):
            out[d*j]+=d*lam[j]
    return out,omega

def pp_beta(p,a):
    return (p**(a+1)+(-1)**a)//(p+1)

def beta_product(n):
    z=1;d=2
    while d*d<=n:
        if n%d==0:
            a=0
            while n%d==0:
                n//=d;a+=1
            z*=pp_beta(d,a)
        d += 1 if d==2 else 2
    if n>1:z*=n-1
    return z

def check():
    N=50000
    vals,omega=beta_convolution_all(N)
    hits=[]; low_support=0
    for n in range(2,N+1):
        if vals[n] != beta_product(n):
            raise AssertionError(('convolution/product', n))
        if omega[n]<=2:
            low_support+=1
            if (n-1)%vals[n]==0:
                hits.append(n)
    # At this finite bound, primes and 4 are the only congruence witnesses.
    primes=[n for n in range(2,N+1) if n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))]
    assert hits == sorted(primes+[4]), (hits[:25], len(hits),len(primes))
    assert 0<low_support<N
    for p in (3,5,7,11,13,17):
        for b in range(2,12,2):
            B=pp_beta(p,b)
            assert B%2==1
            assert B>p**b*(p-1)//p
            for a in range(1,15):
                A=pp_beta(2,a)
                n=2**a*p**b
                assert (n-1)%(A*B)!=0
    print(f'CHECK_OK all_n=2..{N}; two_support_count={low_support}; exceptional_composite=4; parameter_pairs={6*5*14}')

if __name__=='__main__':check()
