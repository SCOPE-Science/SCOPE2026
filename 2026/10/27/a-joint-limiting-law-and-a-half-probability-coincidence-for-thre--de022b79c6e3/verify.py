#!/usr/bin/env python3
"""Exact coefficient and finite-overpartition checks for three natural mex statistics."""
from math import exp, pi, isclose


def parts(n, top=None):
    if n == 0:
        yield ()
        return
    if top is None or top > n:
        top = n
    for j in range(top, 0, -1):
        for rem in parts(n-j, j):
            yield (j,) + rem


def count_brute(n):
    total = equal = 0
    tails = {}
    for p in parts(n):
        ss = sorted(set(p))
        for mask in range(1 << len(ss)):
            over = {v for i,v in enumerate(ss) if mask & (1 << i)}
            nonover = {v for v in ss if p.count(v) >= 2 or v not in over}
            a = b = c = 1
            while a in ss:
                a += 1
            while b in nonover:
                b += 1
            while c in over:
                c += 1
            assert b <= a
            total += 1
            equal += b == a
            for k,m in [(0,0), (1,1), (1,2), (2,2), (2,3), (3,4)]:
                tails[(k,m)] = tails.get((k,m),0) + (b > k and a > m)
    return total,equal,tails


def product_coeffs(n, k=0, m=0):
    """GF of overpartitions with B>k and A>m, to weight n."""
    coef=[0]*(n+1)
    coef[0]=1
    for j in range(1,max(n,k,m)+1):
        # permitted local factor: 1 for absent; q^j/(1-q^j) for each marking if present.
        # non-overlined present: (q^j+q^(2j))/(1-q^j)
        # any present: 2q^j/(1-q^j)
        if j <= k:
            # exactly q^j times F_j; for such j the local factor is q^j(1+q^j)/(1-q^j)
            num=[1,1]; shift=j
        elif j <= m:
            num=[2]; shift=j
        else:
            num=[1,1]; shift=0
        tmp=[0]*(n+1)
        for i in range(shift,n+1):
            tmp[i]=coef[i-shift]
            if len(num)==2 and i-shift-j>=0:tmp[i]+=coef[i-shift-j]
            elif len(num)==1:tmp[i]*=2
        for i in range(j,n+1):tmp[i]+=tmp[i-j]
        coef=tmp
    return coef[n]


def overpartition_counts(N):
    a=[0]*(N+1)
    for d in range(1,N+1):
        for odd in range(1,N//d+1,2):a[d*odd]+=2*d
    p=[1]+[0]*N
    for n in range(1,N+1):
        p[n]=sum(a[j]*p[n-j] for j in range(1,n+1))//n
    return p


def equal_count_from_product(p,N):
    H=[0]*(N+1)
    for k in range(1,N+2):
        t=k*(k-1)//2
        if t>N:break
        H[t]+=1
        r=1
        while t+k*r<=N:
            H[t+k*r]+=2*(-1 if r&1 else 1)
            r+=1
    return sum(H[j]*p[N-j] for j in range(N+1))


def main():
    p=overpartition_counts(900)
    assert [p[i] for i in range(11)] == [1,2,4,8,14,24,40,64,100,154,232]
    for n in range(0,12):
        count, equality, tails = count_brute(n)
        assert count==p[n],(n,count,p[n])
        assert equality == equal_count_from_product(p,n),(n,equality)
        for (k,m),t in tails.items():
            z=product_coeffs(n,k,m)
            assert z==t,(n,k,m,z,t)
    for n in (100,400,900):
        e=equal_count_from_product(p,n)
        print('n',n,'P(A=B)',float(e/p[n]))
    n=400
    # Direct coefficients of the joint event B>k,A>m at a nontrivial point.
    for k,m in [(2,3),(3,3),(4,6)]:
        q=float(product_coeffs(n,k,m)/p[n])
        saddle=pi/(2*n**0.5)
        bprod=exp(-saddle*k*(k+1)/2)
        for j in range(k+1,m+1):
            from math import log1p
            bprod*=2*exp(-saddle*j)/(1+exp(-saddle*j))
        print('n400',k,m,'exact',round(q,8),'boltzmann',round(bprod,8))
        assert abs(q-bprod)<0.16
    print('VERIFY_OK')

if __name__=='__main__': main()
