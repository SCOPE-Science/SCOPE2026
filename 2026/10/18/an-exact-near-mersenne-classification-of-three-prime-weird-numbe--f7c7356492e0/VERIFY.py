"""Exact arithmetic checks for near-boundary three-prime weird numbers.

The infinite classification follows from its symbolic proof; the checks below
compare two independently expressed finite predicates, not prove infinitude.
"""
from math import isqrt


def primes_through(n):
    if n < 2:
        return []
    sieve = bytearray(b'\x01') * (n+1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00'*(((n-p*p)//p)+1)
    return [i for i in range(n+1) if sieve[i]]


def directly_weird(M,p,q):
    h = p-M
    a = M*(p+1)-h*q
    if a <= 0:
        return False
    # Exact possible subset sums from proper divisors. The missing pq block
    # cannot occur since 0<a<Mp<pq; coefficients for 1,p,q lie in [0,M].
    for t in range(min(M,a//q)+1):
        b=a-t*q
        if b % p <= M and b//p <= M:
            return False
    return True


def prediction(M,p,q):
    h=p-M
    if not (h>0 and p>h*h and q>p):
        raise ValueError('outside theorem domain')
    T=M*(p+1)
    return ((h+1)*q > T > h*q and
            (h*(q+1)) % p in range(1,h))


def main():
    total_odd=0
    actual_totals=[]
    strip_totals=[]
    witnesses=[]
    for k in range(1,11):
        M=(1<<(k+1))-1
        # Abundance forces h*q < M*(p+1), p>M. Since p>=M+2,
        # max q is at most floor(M*(M+3)/2).
        prime_list=primes_through(M*(M+3)//2)
        prime_set=set(prime_list)
        count_all=count_strip=0
        for p in prime_list:
            if not (M < p < 2*M):
                continue
            h=p-M
            qmax=(M*(p+1)-1)//h
            for q in prime_list:
                if q<=p:continue
                if q>qmax:break
                weird=directly_weird(M,p,q)
                if k<=3:
                    a=M*(p+1)-(p-M)*q
                    n=(1<<k)*p*q
                    reach={0}
                    if a>0:
                        for d in range(1,n):
                            if d!=n and n%d==0 and d<=a:
                                reach |= {v+d for v in reach if v+d<=a}
                    brute=(a>0 and a not in reach)
                    assert weird==brute, ('proper divisor subset',k,p,q)
                if weird:count_all+=1
                if p>h*h:
                    count_strip+=int(weird)
                    predicted=prediction(M,p,q)
                    assert weird==predicted, ('classification',k,M,p,q,weird,predicted)
                    if weird:
                        a=M*(p+1)-h*q
                        assert 0<a<q
                        assert 3*a < (M+1)*(M+2), (k,p,q,a)
                        assert a <= M*(M+3)//3
                        if len(witnesses)<12:
                            witnesses.append((k,M,p,q,a))
                    total_odd+=1
        actual_totals.append(count_all)
        strip_totals.append(count_strip)
    assert actual_totals==[1,1,5,3,10,23,29,53,115,210],actual_totals
    assert strip_totals==[1,0,3,1,5,5,10,9,32,51],strip_totals
    for q,a in [(887,736),(971,400),(1021,200)]:
        assert directly_weird(63,67,q)
        assert prediction(63,67,q)
        assert 63*(68)-4*q == a
    print('VERIFY_OK')
    print('direct_total_by_k:', actual_totals)
    print('near_strip_by_k:',strip_totals)
    print('near_pairs_checked:',total_odd)
    print('witnesses:',witnesses)


if __name__=='__main__':
    main()
