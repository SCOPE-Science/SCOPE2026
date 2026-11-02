#!/usr/bin/env python3
"""Finite arithmetic checks for the normalized even-parameter trace theorem.

Run: python3 verify.py (Python 3 standard library only).
Finite checks supplement, but do not replace, the mathematical argument.
"""
from math import gcd


def primes_upto(n):
    out=[]
    for q in range(2,n+1):
        if all(q%d for d in range(2,int(q**0.5)+1)):
            out.append(q)
    return out


def mobius(n):
    k=n
    count=0
    for p in primes_upto(int(k**0.5)+1):
        if k%p==0:
            k//=p
            if k%p==0:
                return 0
            count+=1
    if k>1:
        count+=1
    return -1 if count%2 else 1


def legendre(d,p):
    t=pow(d%p,(p-1)//2,p)
    return 0 if t==0 else (1 if t==1 else -1)


def p_part(x,p):
    c=1
    while x%p==0 and x!=0:
        x//=p
        c*=p
    return c


def trace(u,n):
    q=[1,u]
    for j in range(2,n+1):
        q.append(2*u*q[-1]+q[-2])
    return q


def run():
    P=primes_upto(43)
    N=120
    tests=0
    inversions=0
    prime_patterns={}
    for u in range(1,11):
        q=trace(u,max(N,2*P[-1]+4))
        for p in P:
            a=[1]+[p_part(q[n],p) for n in range(1,N+1)]
            if p==2:
                predicted=1 if u%2 else 2
                good=(u%2==1)
                r=None
            else:
                r=next((n for n in range(1,2*p+3) if q[n]%p==0),None)
                predicted=1 if r is None else 2*r//gcd(2*r,p-1)
                good=not (p%4==3 and legendre(u*u+1,p)==-1)
                assert (predicted==1)==good,(u,p,r,predicted,good)
                if r is not None:
                    assert 2*r<=p+1
            transforms=[]
            denominators=[]
            for n in range(1,N+1):
                total=sum(mobius(n//d)*a[d] for d in range(1,n+1) if n%d==0)
                transforms.append(total)
                denominators.append(n//gcd(n,abs(total)))
                assert (predicted*total)%n==0,(u,p,n,total,predicted)
                if n>=2 and total!=0:
                    assert total<0 or total>0
                if p!=2 and r is not None and n>=2:
                    allowed=False
                    if n%r==0:
                        z=n//r
                        if z%2==0:
                            z//=2
                        if z==1:
                            allowed=True
                        elif z>1:
                            t=z
                            while t%p==0:t//=p
                            allowed=(t==1)
                    assert (allowed or total==0),(u,p,n,total,r)
                inversions+=1
            from math import lcm
            observed=1
            for d in denominators:
                observed=lcm(observed,d)
            assert observed==predicted,(u,p,observed,predicted)
            if p!=2 and r is not None:
                c=p_part(q[r],p)
                assert transforms[2*r-1]==1-c,(u,p,r,transforms[2*r-1])
                assert transforms[2*r-1]<0
            elif p==2 and not good:
                assert transforms[1]==1-(1<<((u&-u).bit_length()-1))
            else:
                assert all(t==0 for t in transforms[1:])
            tests+=1
        prime_patterns[u]=sum(1 for p in P if p>2 and p%4==3 and legendre(u*u+1,p)==-1)
    print(f'VERIFY_OK parameter_prime_cases={tests} mobius_coefficients={inversions} prime_bound=43 index_bound={N} negative_witnesses=yes')
    print('Small-prime inert-obstruction counts by parameter:',prime_patterns)

if __name__=='__main__':
    run()
