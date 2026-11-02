#!/usr/bin/env python3
"""Finite reproducibility checks for the prime-power-base valuation theorem."""
from math import comb


def vp(n, p):
    z = 0
    while n % p == 0:
        n //= p
        z += 1
    return z, n


def coeffs(p, a, m, N):
    k = p ** a
    s = vp(m, p)[0]
    modulus = p ** (s + a + 3)
    # (1-x)^(km) H(x)=(1-x^k)^m H(x^k): integral recurrence.
    c = [0] * (N + 1)
    c[0] = 1
    left = [(-1) ** (i + 1) * comb(k * m, i) % modulus
            for i in range(min(k*m, N) + 1)]
    right = [(-1) ** j * comb(m, j) % modulus
             for j in range(min(m, N//k) + 1)]
    for n in range(1, N + 1):
        z = 0
        for i in range(1, min(n,k*m)+1):
            z += left[i] * c[n-i]
        if n % k == 0:
            for j in range(min(m,n//k)+1):
                z += right[j] * c[n//k-j]
        c[n] = z % modulus
    return c, modulus


def verify():
    cases = [(2,2,4,3000),(2,2,12,2500),(2,3,8,1500),
             (3,2,3,1500),(3,3,9,800),(5,2,5,600),
             (2,1,2,1500),(3,1,1,1500)]
    total=0
    for p,a,m,N in cases:
        s = vp(m,p)[0]
        assert (s >= a if p==2 else s >= a-1)
        seq, modulus=coeffs(p,a,m,N)
        for n in range(1,N+1):
            t,u=vp(n,p)
            r=t%a
            e=s+a-r
            leading=(m//(p**s))*pow(u,-1,p)%p
            assert (seq[n]//(p**e))%p == leading, (p,a,m,n,seq[n],e)
            assert seq[n]%(p**e)==0
            total+=1
        # Specialize the exact first coefficient (m*k).
        assert seq[1]==(m*p**a)%modulus
    # Verify the formal-log coefficient using independent divisor summation.
    for k in [2,3,4,8,9,25,27]:
        for n in range(1,1001):
            numerator=1
            power=1
            while power<=n:
                if n%power==0:
                    numerator+= (k-1)*power
                power*=k
            q=n
            vk=0
            while q%k==0:
                q//=k
                vk+=1
            # Correct sum counts 1 + (k-1)(1+k+...+k^v) = k^(v+1)
            assert numerator == k**(vk+1)
    # Legendre bounds invoked in the proof.
    for p in (2,3,5,7):
        v=0
        for j in range(2,1001):
            t=j
            while t%p==0:
                v+=1
                t//=p
            if p==2: assert v<=j-1
            else: assert 2*v<=j-1
    print('VERIFY_OK', total, 'coefficient/unit cases; log and factorial bounds')

if __name__=='__main__':
    verify()
